"""cert_Dprime.py -- referee R9near_1.  Certified upper bound for D' of r9/near/prop_near.tex (Lemma E).

Same cell scheme as r9/near/near_const.py (whose monotonicity reductions were audited and are proved in
reports/referee-R9-near-1.md), but every number is an UPPER bound (or, for denominators and subtracted
quantities, a LOWER bound) obtained rigorously:

  * scalar constants (parameters given as decimal strings, C_T, C_mu = 1 + kappa C_T^2, c6, C_V, C_1A, P_0, the
    bottom-cell closed forms, r^gamma) are computed with mpmath.iv (outward rounded interval arithmetic) and converted to
    float64 with one extra outward ulp;
  * (1+y)^gamma, y in [0, 7], is majorised by a table T_j >= (1 + j h)^gamma, h = 2^-15, computed with mpmath.iv
    (gamma upper end; the map is increasing in y and in gamma for 1+y >= 1), and looked up at j = ceil(y/h);
  * array operations use IEEE-754 float64 (+ - * / sqrt are correctly rounded), followed by np.nextafter towards
    +inf (upper bounds) or -inf (lower bounds); max/min are exact;
  * dot products / sums of NON-NEGATIVE terms (any evaluation order, FMA or not) satisfy fl(S) >= (1 - gamma_n) S,
    gamma_n = n u/(1 - n u) (Higham, Thm 3.1 / Sec. 2.6); the computed value is multiplied by (1 + 1e-11) (n <= 10^6).

usage: python cert_Dprime.py [--tuple p|pA] [--CT 2.911] [--old] [--q 1.03 --nx 500 --ns 700 --dr 0.05]
"""
import sys, time, math
import numpy as np
from mpmath import iv, mpf

iv.prec = 80
INF = np.inf

# ----------------------------------------------------------------------------------------------- directed rounding
def U(x):
    return np.nextafter(x, INF)


def Dn(x):
    return np.nextafter(x, -INF)


def fhi(I):
    """float upper bound of an iv interval"""
    return float(np.nextafter(float(I.b), INF))


def flo(I):
    return float(np.nextafter(float(I.a), -INF))


SUMF = 1.0 + 1e-11           # inflation for float sums of n <= NMAX non-negative terms: gamma_n < 5.6e-12 < 1e-11
NMAX = 50000


def usum(a):
    a = np.asarray(a, float)
    assert a.size <= NMAX and np.all(a >= 0)
    return float(U(U(np.sum(a)) * SUMF))


def udot(K, d):
    """upper bound of K @ d, K, d >= 0 (rows of K)"""
    assert K.shape[1] <= NMAX and np.all(K >= 0) and np.all(d >= 0)
    return U(U(K @ d) * SUMF)


# ----------------------------------------------------------------------------------------------- parameters
DEC = dict(gam='0.614267', R='0.001014', m='0.0561202', kap='1.01594', cA='0.996095', KR='31.9496', Kf='5.03588',
           Ke='999.98', qc='2.05829', dL='1.0000602', d1='1.0001202', v0='6e-5', fF='0.136962')
GAM_A = '0.614666'                      # stage-A tuple p_A: gamma -> gamma_D (verify_constants.out INPUTS gD)


def old_tilt_iv(P):
    g, kap, cA, qc, m = P['gam'], P['kap'], P['cA'], P['qc'], P['m']
    ct = lambda r: (iv.sqrt(kap) * iv.mpf(r) ** (iv.mpf('0.5') + g) + m / 2) / cA
    CA = ct(qc) / (1 - qc ** (-g))
    return CA, CA + ct(3)


class Const:
    def __init__(self, gam_str, CT_str='2.911', mode='new'):
        P = {k: iv.mpf(v) for k, v in DEC.items()}
        P['gam'] = iv.mpf(gam_str)
        self.P = P
        kap, cA, d1, dL = P['kap'], P['cA'], P['d1'], P['dL']
        if mode == 'old':
            CA, CB = old_tilt_iv(P)
            CTL = CA + CB
        else:
            CA = CB = iv.mpf(CT_str)
            CTL = 2 * CA
        CmuA = 1 + kap * CA ** 2
        self.I = dict(CA=CA, CB=CB, CTL=CTL, CmuA=CmuA, C1A=iv.sqrt(kap * CmuA), CV=iv.sqrt(1 + kap * CB ** 2),
                      c6=(1 + d1) / cA, uc=1 / CmuA, dLp=3 * dL - 2, kmc=kap - cA, Kf1=P['Kf'] + 1,
                      k32_2cA=kap ** iv.mpf('1.5') / (2 * cA))
        self.I.update(P)
        for k, v in self.I.items():                     # float enclosures
            setattr(self, k + '_hi', fhi(v))
            setattr(self, k + '_lo', flo(v))
        self.mode, self.gam_str, self.CT_str = mode, gam_str, CT_str
        # (1+y)^gamma table, increasing; gamma upper end
        self.h = 2.0 ** -15
        n = int(7.2 / self.h) + 2
        t0 = time.time()
        g = iv.mpf(P['gam'].b)
        tab = np.empty(n)
        for j in range(n):
            tab[j] = fhi((1 + iv.mpf(j) * iv.mpf(self.h)) ** g)
        self.powtab = tab
        self.tab_time = time.time() - t0

    def pow_u(self, z):
        """upper bound of z^gamma for float array z >= 1 (z itself an upper bound of the true base)"""
        y = np.asarray(z, float) - 1.0          # z - 1 is exact (Sterbenz) for 1 <= z <= 2; else rounding -> use U
        y = U(y)
        j = np.ceil(y / self.h).astype(np.int64)   # y/h exact (power of 2)
        j = np.maximum(j, 0)
        assert np.all(j < len(self.powtab))
        return self.powtab[j]


# ----------------------------------------------------------------------------------------------- budgets (lo, hi)
def budgets(c, s, thf):
    lam = np.maximum(s, thf / 2)                       # exact
    Om_hi = np.minimum(1.0, U(c.CmuA_hi * lam)); Om_lo = np.minimum(1.0, Dn(c.CmuA_lo * lam))
    Q_hi = U(U(c.kap_hi * lam) * Om_hi); Q_lo = Dn(Dn(c.kap_lo * lam) * Om_lo)
    G_hi = U(np.sqrt(Q_hi)); G_lo = Dn(np.sqrt(np.maximum(Q_lo, 0)))
    return (Om_lo, Om_hi), (Q_lo, Q_hi), (G_lo, G_hi)


def budgets_c(c, s):
    return budgets(c, s, 0.0)


def ust(K, Phi):
    """upper Riemann-Stieltjes sum: K[:,0]*Phi(0) + sum_i K[:,i] (Phi(s_{i+1}) - Phi(s_i)); K upper, Phi=(lo,hi)"""
    lo, hi = Phi
    d = np.maximum(U(hi[1:] - lo[:-1]), 0.0)
    return U(U(K[:, 0] * hi[0]) + udot(K[:, :-1], d))


# ----------------------------------------------------------------------------------------------- offsets (upper)
def ell_ratio_u(ell):
    return U(ell / Dn(1.0 + ell))


def p_nochord(c, y, ell):
    L2 = U(c.CV_hi * U(np.sqrt(U(U(c.kap_hi * ell) * U(1.0 + y)))))
    fac = U(1.0 + U(U(c.kap_hi * ell) / c.cA_lo))
    S = U(U(fac * U(np.sqrt(U(c.kap_hi * ell_ratio_u(ell))))) * U(np.sqrt(U(1.0 + y))))
    return U(np.minimum(L2, S) * c.pow_u(U(1.0 + y)))


def pfrak(c, y, thf):
    y = np.asarray(y, float)
    ell = np.maximum(y, thf / 2)
    base = p_nochord(c, y, ell)
    chord = U(U(U(c.kap_hi * c.CTL_hi) * y) * c.pow_u(U(1.0 + y)))
    val = np.where(y >= thf / 2, np.minimum(base, chord), base)
    return np.where(y > 0, val, 0.0)


def pstar(c, z, thf):
    z = np.asarray(z, float)
    zz = np.maximum(z, 0.0)
    h = thf / 2
    left = p_nochord(c, np.minimum(zz, h), np.full_like(zz, h))
    right = pfrak(c, np.maximum(zz, h), thf)
    val = np.where(zz < h, left, np.maximum(left, right))
    return np.where(z > 0, val, 0.0)


def pL(c, y, thf):
    y = np.asarray(y, float)
    ell = np.maximum(y, thf / 2)
    fac = U(1.0 + U(U(c.kap_hi * ell) / c.cA_lo))
    inner = U(U(U(U(2.0 * c.kap_hi) * c.kmc_hi) * U(1.0 + y)) * ell_ratio_u(ell))
    val = U(fac * U(np.sqrt(inner)))
    return np.where(y > 0, val, 0.0)


def pLstar(c, z, thf):
    z = np.asarray(z, float)
    return np.where(z > 0, pL(c, np.maximum(z, 1e-300), thf), 0.0)


def P0_u(c, th):
    """upper bound of P_0(theta) at the float theta = th (P_0 is non-decreasing in theta)"""
    I = c.I
    t = iv.mpf(th)
    lam = lambda s: iv.mpf(max(s, th / 2))
    Gb = lambda s: iv.sqrt(I['kap'] * lam(s) * min_iv(1, I['CmuA'] * lam(s)))
    if th <= 1:
        return fhi(Gb(th))
    a1 = I['kap'] * I['CA'] * t ** (1 + I['gam'])
    a2 = iv.sqrt((I['kap'] * t - I['cA']) * I['CmuA'] * t ** (1 + 2 * I['gam']))
    a3 = I['k32_2cA'] * t ** (2 + I['gam'])
    alt = min(fhi(a1), fhi(a2), fhi(a3))
    return max(fhi(Gb(1.0)), alt)


def min_iv(a, b):
    a = iv.mpf(a); b = iv.mpf(b)
    return iv.mpf([min(a.a, b.a), min(a.b, b.b)])


# ----------------------------------------------------------------------------------------------- grids
def sgrid(lo, n):
    pts = [np.array([0.0, 1.0]), np.linspace(0, 1, n // 4)]
    if lo > 0:
        pts += [np.geomspace(max(lo, 1e-16), 1.0, n), np.array([lo])]
    s = np.unique(np.concatenate(pts))
    return s[(s >= 0) & (s <= 1)]


# ----------------------------------------------------------------------------------------------- one theta-cell
class Cell:
    def __init__(self, c, th_lo, th_hi, nx=500, ns=700, bottom=False, x1=1e-7):
        self.c, self.th_lo, self.th_hi, self.bottom, self.x1 = c, th_lo, th_hi, bottom, x1
        thb = th_hi
        d1th = U(c.d1_hi * th_hi)                        # upper bound of delta1*theta_h

        def den_lin(W):                                   # lower bound of c_A W - delta1 theta_h  (W lower bound)
            return Dn(Dn(c.cA_lo * W) - d1th)

        if bottom:
            def K1f(W):
                return U(1.0 / np.maximum(Dn(W / c.c6_hi), den_lin(W)))
        else:
            def K1f(W):
                return U(1.0 / np.maximum(th_lo, den_lin(W)))

        def M1f(W):
            return np.minimum(1.0, U(th_hi / np.maximum(th_hi, den_lin(W))))

        thf = th_hi
        xlo = x1 if bottom else float(Dn(th_lo / c.kap_hi))
        xend = c.Kf_hi
        extra = [] if bottom else [np.arange(1, 400) * xlo]
        xs = np.unique(np.concatenate([np.geomspace(xlo, xend, nx), np.linspace(xlo, xend, nx // 2), [xlo, xend]] + extra))
        xs = xs[(xs >= xlo) & (xs <= xend)]
        assert xs[0] == xlo and xs[-1] == xend
        xl, xr = xs[:-1], xs[1:]
        if bottom:
            s = sgrid(1e-15, ns); Om, Q, G = budgets_c(c, s)
        else:
            s = sgrid(thf / 2, ns); Om, Q, G = budgets(c, s, thf)
        assert s[0] == 0.0 and s[-1] == 1.0
        W = Dn(xl[:, None] + s[None, :])
        K1 = K1f(W); M1 = M1f(W); K2 = U(K1 * K1); MK = U(M1 * K1)

        def OmA_u(sig, t):
            return np.minimum(1.0, U(c.CmuA_hi * np.maximum(sig, t / 2)))

        c6th = U(c.c6_hi * th_hi)
        ind = xl < c6th
        IND_T = np.where(ind, OmA_u(U(c6th - xl), th_hi), 0.0)
        IND_H = np.where(ind, U(c.CmuA_hi * c.c6_hi), 0.0) if bottom else U(IND_T / th_lo)
        if bottom:
            Mx, Kx = M1f(xl), K1f(xl)
            a_om = U(c.CmuA_hi / 2)
            iH = U(U(U(a_om * Mx) + ust(K1, Om)) + IND_H)
            iT = U(U(U(min(1.0, U(c.CmuA_hi * thb / 2)) * Mx) + ust(M1, Om)) + IND_T)
            kc4 = U(U(c.kap_hi * c.CmuA_hi) / 4)
            qH = U(U(kc4 * U(Mx * Mx)) + ust(K2, Q))
            qT = U(U(U(kc4 * thb) * U(Mx * Mx)) + ust(MK, Q))
            ca = U(c.C1A_hi / 2)
            j2H = U(U(ca * U(Mx * Kx)) + ust(K2, G))
            j2T = U(U(ca * U(Mx * Mx)) + ust(MK, G))
            j1H = U(U(ca * Mx) + ust(K1, G))
            j1T = U(U(U(ca * thb) * Mx) + ust(M1, G))
        else:
            iH = U(ust(K1, Om) + IND_H); iT = U(ust(M1, Om) + IND_T)
            qH = ust(K2, Q); qT = ust(MK, Q)
            j2H = ust(K2, G); j2T = ust(MK, G)
            j1H = ust(K1, G); j1T = ust(M1, G)
        pf = pfrak(c, xr, thf)
        zs = xr if bottom else np.maximum(U(xr - Dn(th_lo / c.kap_hi)), 0.0)
        ps = pstar(c, zs, thf)
        Lf = U(0.5 * U(U(c.dL_hi * pf) + U(c.dLp_hi * ps)))
        LfL = U(U(0.5 * U(U(c.dL_hi * pL(c, xr, thf)) + U(c.dLp_hi * pLstar(c, zs, thf)))) / c.m_lo)
        self.linLH, self.linLT = U(LfL * j2H), U(LfL * j2T)
        self.xl, self.xr, self.dx = xl, xr, U(xr - xl)
        self.IH, self.IT = U(c.dL_hi * iH), U(c.dL_hi * iT)
        self.quadH, self.linH = U(U(c.dL_hi / 2) * qH), U(Lf * j2H)
        self.quadT, self.linT = U(U(c.dL_hi / 2) * qT), U(Lf * j2T)
        self.LH = U(U(c.dL_hi * j1H) / c.m_lo)
        self.LT = U(U(c.dL_hi * j1T) / c.m_lo)
        self.onex_g = c.pow_u(U(1.0 + xr))              # (1 + x_r)^gamma, for long-type times r < 1 + x
        # gap-0 leg, theta-prefactored
        W0 = s[None, :]
        if bottom:
            M0 = M1f(W0); K0 = K1f(np.maximum(W0, 1e-300)); MK0 = U(M0 * K0); MK0[:, 0] = 0.0
            assert s[1] <= c.uc_lo
            i0 = U(U(min(1.0, U(c.CmuA_hi * thb / 2)) + ust(M0, Om)[0]) + OmA_u(c6th, thb))
            q0 = U(U(U(c.kap_hi * c.CmuA_hi / 4) * thb) + ust(MK0, Q)[0])
            q0 = U(q0 + U(U(U(U(2 * c.kap_hi) * c.CmuA_hi) * c.c6_hi) * s[1]))
            atomG = fhi(iv.sqrt(c.I['kap'] * iv.mpf(thb) / 2 * min_iv(1, c.I['CmuA'] * iv.mpf(thb) / 2)))
            lin0 = U(U(U(0.5 * c.dLp_hi) * c.C1A_hi) * U(atomG + ust(U(M0 * M0), G)[0]))
        else:
            M0 = M1f(W0); K0 = K1f(W0)
            i0 = U(ust(M0, Om)[0] + OmA_u(c6th, th_hi))
            q0 = ust(U(M0 * K0), Q)[0]
            lin0 = U(U(U(0.5 * c.dLp_hi) * P0_u(c, th_hi)) * ust(U(M0 * K0), G)[0])
        self.TH0 = float(U(U(U(c.dL_hi * i0) + U(U(c.dL_hi / 2) * q0)) + lin0))
        if bottom:
            self._crude()

    def _crude(self):
        """explicit majorants on (0, x1] (prop_near Lemma E(iii)); all scalars in mpmath.iv"""
        c, I = self.c, self.c.I
        x1 = iv.mpf(self.x1)
        kap, Cmu, c6, C1A, CV, CTL, dL, dLp, gam, m = (I[k] for k in
                                                        ('kap', 'CmuA', 'c6', 'C1A', 'CV', 'CTL', 'dL', 'dLp', 'gam', 'm'))
        u = 1 / Cmu
        A_i, B_i = Cmu / 2 + Cmu * c6, Cmu * c6
        A_q, B_q = kap * Cmu / 4 + kap * c6 ** 2 / u, 2 * kap * Cmu * c6 ** 2
        cj2, dj2 = C1A * c6 * (iv.mpf('0.5') + c6), iv.sqrt(kap) * c6 ** 2 / 3 * u ** iv.mpf('-1.5')
        A_1, B_1 = C1A / 2 + c6 * iv.sqrt(kap) * u ** iv.mpf('-0.5'), C1A * c6
        g1 = (1 + x1) ** (gam + iv.mpf('0.5'))
        a_l, b_l = g1 * dL * kap * CTL / 2, g1 * dLp * CV * iv.sqrt(kap) / 2
        Lx1 = a_l * x1 + b_l * iv.sqrt(x1)
        lfc = dL * (1 + x1) ** gam / m
        il = x1 * iv.log(1 + u / x1) + u * iv.log(1 + x1 / u)
        lg = iv.log(1 + u / x1)
        I_cr = (dL * (A_i * x1 + B_i * il) + dL / 2 * (A_q * x1 + B_q * il) + a_l * cj2 * x1 + 2 * b_l * cj2 * iv.sqrt(x1)
                + Lx1 * dj2 * x1 + lfc * (A_1 * x1 + B_1 * il))
        Hx1 = (dL * (A_i + B_i * lg) + dL / 2 * (A_q + B_q * lg) + a_l * cj2 + b_l * cj2 / iv.sqrt(x1) + Lx1 * dj2
               + lfc * (A_1 + B_1 * lg))
        self.I_cr = fhi(I_cr)
        self.T_cr = fhi(kap * x1 * Hx1)

    def bound(self, r_lo=None, r_hi=None):
        c = self.c
        if r_lo is None:
            mode = np.zeros(len(self.xl), int)
            rs = INF
            rf = np.ones(len(self.xl))
        else:
            # short-type for every r in the cell iff x_r <= r_lo - 1; long-type iff x_l > r_hi - 1
            mode = np.where(self.xr <= Dn(r_lo - 1.0), 0, np.where(self.xl > U(r_hi - 1.0), 1, 2))
            rs = fhi(iv.mpf(r_hi) ** c.I['gam'])
            rf = np.minimum(rs, self.onex_g)

        def comb(I, quad, lin, L, linL):
            linS = np.minimum(lin, U(linL * rs)) if np.isfinite(rs) else lin
            Lv = np.minimum(U(L * rf), U(quad + U(linL * rf)))
            Sv = U(quad + linS)
            return U(I + np.where(mode == 0, Sv, np.where(mode == 1, Lv, np.maximum(Sv, Lv))))

        H = comb(self.IH, self.quadH, self.linH, self.LH, self.linLH)
        TH = comb(self.IT, self.quadT, self.linT, self.LT, self.linLT)
        Hst = np.maximum.accumulate(H[::-1])[::-1]
        THst = np.maximum.accumulate(TH[::-1])[::-1]
        kap = c.kap_hi
        if self.bottom:
            legs = U(max(self.T_cr, THst[0]) + U(kap * U(U(self.I_cr + U(self.x1 * Hst[0])) + usum(U(Hst * self.dx)))))
            return float(U(self.TH0 + legs))
        integ = U(THst[0] + U(kap * usum(U(Hst * self.dx))))
        kmax = int(math.ceil(U(U(c.kap_hi * c.Kf_hi) / self.th_lo))) - 1
        if kmax <= 40000:
            z0 = float(Dn(self.th_lo / c.kap_hi))
            z = Dn(np.arange(1, kmax + 1) * z0)
            idx = np.clip(np.searchsorted(self.xl, z, side='right') - 1, 0, len(self.xl) - 1)
            legs = min(usum(THst[idx]), float(integ))
        else:
            legs = float(integ)
        return float(U(self.TH0 + legs))


def cell_sup(c, cell, dr=0.05):
    best, arg = cell.bound(None, None), None              # r >= r_end: short-type only (r_end >= K_f + 1)
    rmin = max(1.0, float(Dn(c.Ke_lo * cell.th_lo)))
    r_end = c.Kf1_hi
    if rmin < r_end:
        r = rmin
        while r < r_end:
            r2 = min(r + dr, r_end)
            v = cell.bound(r, r2)
            if v > best:
                best, arg = v, (r, r2)
            r = r2
    return best, arg


def Dprime(c, th_b=1e-7, q=1.03, nx=500, ns=700, dr=0.05, log=print):
    out = []
    cb = Cell(c, 0.0, th_b, nx, ns, bottom=True)
    v, a = cell_sup(c, cb, dr)
    out.append((0.0, th_b, v, a))
    hi = th_b
    while hi < 2.0:
        lo, hi = hi, min(hi * q, 2.0)                  # consecutive cells share the float endpoint exactly
        cl = Cell(c, lo, hi, nx, ns)
        v, a = cell_sup(c, cl, dr)
        out.append((lo, hi, v, a))
    assert out[-1][1] == 2.0
    return out


if __name__ == "__main__":
    A = sys.argv[1:]
    get = lambda k, d: type(d)(A[A.index(k) + 1]) if k in A else d
    tup = get('--tuple', 'p')
    CT = get('--CT', '2.911')
    mode = 'old' if '--old' in A else 'new'
    q, nx, ns, dr = get('--q', 1.03), get('--nx', 500), get('--ns', 700), get('--dr', 0.05)
    gam = DEC['gam'] if tup == 'p' else GAM_A
    t0 = time.time()
    c = Const(gam, CT, mode)
    print(f"tuple {tup} (gamma={gam}), tilt mode {mode}, C_T={CT if mode == 'new' else '-'}; grid q={q} nx={nx} ns={ns} dr={dr}")
    for k in ('CA', 'CB', 'CTL', 'CmuA', 'C1A', 'CV', 'c6'):
        print(f"  {k:5s} in [{c.I[k].a}, {c.I[k].b}]")
    print(f"  (1+y)^gamma table: {len(c.powtab)} entries, {c.tab_time:.1f}s")
    res = Dprime(c, q=q, nx=nx, ns=ns, dr=dr)
    worst = max(res, key=lambda t: t[2])
    for t in res[::max(1, len(res) // 20)]:
        print(f"    theta in [{t[0]:.4e},{t[1]:.4e}]  bound {t[2]:9.4f}  " + (f"r in [{t[3][0]:.3f},{t[3][1]:.3f}]" if t[3] else "short/r>=Kf+1"))
    print(f"  cells: {len(res)};  bottom cell bound {res[0][2]:.4f}")
    print(f"  ==> CERTIFIED  D' <= {worst[2]:.6f}   (worst cell theta in [{worst[0]:.6g},{worst[1]:.6g}], r: {worst[3]})")
    I = c.I
    Dc = iv.mpf(np.nextafter(worst[2], INF))
    th = I['fF'] ** 2 + 2 * I['v0'] * Dc
    print(f"  theta_bar = fF^2 + 2 v0 D' <= {fhi(th):.8f}  (P6 needs < 1)")
    print(f"  time {time.time() - t0:.1f}s")
