"""near_const.py -- stream R-near, round 9.  Evaluates D' of Proposition 4.3'' (r9/near/prop_near.tex).

    D' = sup over theta in (0,2] and r = R/lambda >= max(1, K_eps theta) of  Dcal(theta, r),
    Dcal = theta*H_0(theta) + theta * sum_{k=1}^{k*} H^*_r(k theta/kappa; theta)                     (discrete form)
         <= theta*H_0 + theta*H^*_r(theta/kappa) + kappa * int_{theta/kappa}^{K_f} H^*_r(x;theta) dx      (integral form)

Rigour of the evaluation (Lemma E of the report): every theta-occurrence is replaced by the cell endpoint that increases
the bound (all dependences monotone), the bottom cell (0, th_b] uses theta-free kernels plus explicit estimates on
(0, x1]; inner integrals are UPPER Riemann-Stieltjes sums of non-increasing kernels against non-decreasing budgets;
x-integrals are upper sums of non-increasing majorants (kernel at the left end, increasing factors at the right end).
So every printed bound is an upper bound up to floating-point rounding.

Tilt constants enter only through: CA (tilt of a sub-pair with the same left end), CB (same right end), CTL (general),
CmuA = 1 + kappa CA^2 (L2 budget slope).  Old (Def 3.3): CA, CB, CTL = CA + CB.  New (R-tilt Lemma T): CA = CB = C_T,
CTL = 2 C_T (two steps through (a',b)), CmuA = C_mu = 1 + kappa C_T^2.

usage:  python near_const.py [--old] [--CT value] [--quick]
"""
import sys
import numpy as np
from math import sqrt, log, ceil

INP = dict(gam=0.614267, R=0.001014, m=0.0561202, kap=1.01594, cA=0.996095, KR=31.9496, Kf=5.03588, Ke=999.98,
           qc=2.05829, dL=1.0000602, d1=1.0001202, v0=6e-5, fF=0.136962)
CT_RTILT = 2.9108574          # r9/tilt/tilt_constants.out, main tuple p


def old_tilt(P):
    g, kap, cA, qc, m = P['gam'], P['kap'], P['cA'], P['qc'], P['m']
    ct = lambda r: (kap ** 0.5 * r ** (0.5 + g) + m / 2) / cA
    CA = ct(qc) / (1 - qc ** (-g))
    return CA, CA + ct(3)


class C:
    def __init__(self, P, mode='new', CT=CT_RTILT):
        self.__dict__.update(P)
        self.mode = mode
        if mode == 'old':
            self.CA, self.CB = old_tilt(P)
            self.CTL = self.CA + self.CB
        else:
            self.CA = self.CB = CT
            self.CTL = 2 * CT
        self.CmuA = 1 + self.kap * self.CA ** 2
        self.C1A = sqrt(self.kap * self.CmuA)
        self.CV = sqrt(1 + self.kap * self.CB ** 2)
        self.c6 = (1 + self.d1) / self.cA
        self.uc = 1 / self.CmuA
        self.chi = self.kap * self.dL
        self.dLp = 3 * self.dL - 2


# ---------------------------------------------------------------------------------------------------------------
def budgets(c, s, thf):
    lam = np.maximum(s, thf / 2)
    Om = np.minimum(1.0, c.CmuA * lam)
    Q = c.kap * lam * Om
    return Om, Q, np.sqrt(Q)


def budgets_c(c, s):
    Om = np.minimum(1.0, c.CmuA * s)
    Q = c.kap * s * Om
    return Om, Q, np.sqrt(Q)


def p_nochord(c, y, ell):
    """offset bounds of Lemma O' without the chord route (valid for every y >= 0, ell = max(y, theta/2))"""
    L2 = c.CV * np.sqrt(c.kap * ell * (1 + y))
    S = (1 + c.kap * ell / c.cA) * np.sqrt(c.kap * ell / (1 + ell)) * np.sqrt(1 + y)
    return np.minimum(L2, S) * (1 + y) ** c.gam


def pfrak(c, y, thf):
    y = np.asarray(y, float)
    ell = np.maximum(y, thf / 2)
    base = p_nochord(c, y, ell)
    chord = c.kap * c.CTL * y * (1 + y) ** c.gam
    val = np.where(y >= thf / 2, np.minimum(base, chord), base)
    return np.where(y > 0, val, 0.0)


def pstar(c, z, thf):
    """sup_{0<=y<=z} pfrak(y): pfrak is increasing on (0, thf/2) and on [thf/2, inf)"""
    z = np.asarray(z, float)
    zz = np.maximum(z, 0.0)
    h = thf / 2
    left = p_nochord(c, np.minimum(zz, h), np.full_like(zz, h))
    right = pfrak(c, np.maximum(zz, h), thf)
    val = np.where(zz < h, left, np.maximum(left, right))
    return np.where(z > 0, val, 0.0)


def pL(c, y, thf):
    """Lemma O'(L): offset bound from (CA)+(J1) on the pair (a',b) of any length (no tilt constant), units lambda"""
    y = np.asarray(y, float)
    ell = np.maximum(y, thf / 2)
    val = (1 + c.kap * ell / c.cA) * np.sqrt(2 * c.kap * (c.kap - c.cA) * (1 + y) * ell / (1 + ell))
    return np.where(y > 0, val, 0.0)


def pLstar(c, z, thf):
    """sup_{0<y<=z} pL(y): pL is increasing in y"""
    z = np.asarray(z, float)
    return np.where(z > 0, pL(c, np.maximum(z, 1e-300), thf), 0.0)


def P0(c, th):
    lam = lambda s: max(s, th / 2)
    Gb = lambda s: min(c.C1A * lam(s), sqrt(c.kap * lam(s)))
    if th <= 1:
        return Gb(th)
    alt = min(c.kap * c.CA * th ** (1 + c.gam),
              sqrt(max(c.kap * th - c.cA, 0) * c.CmuA * th ** (1 + 2 * c.gam)),
              c.kap ** 1.5 / (2 * c.cA) * th ** (2 + c.gam))
    return max(Gb(1.0), alt)


def sgrid(lo, n):
    pts = [np.array([0.0, 1.0]), np.linspace(0, 1, n // 4)]
    if lo > 0:
        pts += [np.geomspace(max(lo, 1e-16), 1.0, n), np.array([lo])]
    s = np.unique(np.concatenate(pts))
    return s[(s >= 0) & (s <= 1)]


def ust(Kmat, Phi):
    return Kmat[:, 0] * Phi[0] + Kmat[:, :-1] @ np.diff(Phi)


# ---------------------------------------------------------------------------------------------------------------
class Cell:
    """all r-independent pieces for theta in [th_lo, th_hi] (bottom: (0, th_hi])"""

    def __init__(self, c, th_lo, th_hi, nx=500, ns=700, bottom=False, x1=1e-7):
        self.c, self.th_lo, self.th_hi, self.bottom, self.x1 = c, th_lo, th_hi, bottom, x1
        th_b = th_hi
        if bottom:
            K1f = lambda w: 1.0 / np.maximum(w / c.c6, c.cA * w - c.d1 * th_b)
        else:
            K1f = lambda w: 1.0 / np.maximum(th_lo, c.cA * w - c.d1 * th_hi)
        M1f = lambda w: th_hi / np.maximum(th_hi, c.cA * w - c.d1 * th_hi)
        thf = th_hi
        xlo = x1 if bottom else th_lo / c.kap
        extra = [] if bottom else [np.arange(1, 400) * th_lo / c.kap]
        xs = np.unique(np.concatenate([np.geomspace(xlo, c.Kf, nx), np.linspace(xlo, c.Kf, nx // 2), [c.Kf]] + extra))
        xs = xs[(xs >= xlo) & (xs <= c.Kf)]
        xl, xr = xs[:-1], xs[1:]
        if bottom:
            s = sgrid(1e-15, ns); Om, Q, G = budgets_c(c, s)
        else:
            s = sgrid(thf / 2, ns); Om, Q, G = budgets(c, s, thf)
        W = xl[:, None] + s[None, :]
        K1 = K1f(W); M1 = M1f(W); K2 = K1 * K1; MK = M1 * K1
        OmA = lambda sig, t: np.minimum(1.0, c.CmuA * np.maximum(sig, t / 2))
        IND_T = np.where(xl < c.c6 * th_hi, OmA(c.c6 * th_hi - xl, th_hi), 0.0)
        IND_H = np.where(xl < c.c6 * th_hi, c.CmuA * c.c6, 0.0) if bottom else IND_T / th_lo
        if bottom:
            Mx, Kx = M1f(xl), K1f(xl)
            iH = c.CmuA / 2 * Mx + ust(K1, Om) + IND_H
            iT = min(1.0, c.CmuA * th_b / 2) * Mx + ust(M1, Om) + IND_T
            qH = c.kap * c.CmuA / 4 * Mx ** 2 + ust(K2, Q)
            qT = c.kap * c.CmuA / 4 * th_b * Mx ** 2 + ust(MK, Q)
            j2H = c.C1A / 2 * Mx * Kx + ust(K2, G)
            j2T = c.C1A / 2 * Mx ** 2 + ust(MK, G)
            j1H = c.C1A / 2 * Mx + ust(K1, G)
            j1T = c.C1A / 2 * th_b * Mx + ust(M1, G)
        else:
            iH = ust(K1, Om) + IND_H; iT = ust(M1, Om) + IND_T
            qH = ust(K2, Q); qT = ust(MK, Q)
            j2H = ust(K2, G); j2T = ust(MK, G)
            j1H = ust(K1, G); j1T = ust(M1, G)
        pf = pfrak(c, xr, thf)
        ps = pstar(c, xr if bottom else xr - th_lo / c.kap, thf)
        Lf = 0.5 * (c.dL * pf + c.dLp * ps)
        LfL = 0.5 * (c.dL * pL(c, xr, thf) + c.dLp * pLstar(c, xr if bottom else xr - th_lo / c.kap, thf)) / c.m
        self.linLH, self.linLT = LfL * j2H, LfL * j2T     # offset of Lemma O'(L); multiply by r^gamma
        self.xl, self.xr, self.dx = xl, xr, xr - xl
        self.IH, self.IT = c.dL * iH, c.dL * iT
        self.SH = c.dL / 2 * qH + Lf * j2H              # short-type II
        self.ST = c.dL / 2 * qT + Lf * j2T
        self.LH = c.dL * j1H / c.m                       # long-type II, times r^gamma
        self.LT = c.dL * j1T / c.m
        # pieces for the term breakdown
        self.quadH, self.linH = c.dL / 2 * qH, Lf * j2H
        self.quadT, self.linT = c.dL / 2 * qT, Lf * j2T
        # gap-0 leg, theta-prefactored
        W0 = s[None, :]
        if bottom:
            M0 = M1f(W0); K0 = K1f(np.maximum(W0, 1e-300)); MK0 = M0 * K0; MK0[:, 0] = 0.0
            i0 = min(1.0, c.CmuA * th_b / 2) + ust(M0, Om)[0] + OmA(c.c6 * th_b, th_b)
            q0 = c.kap * c.CmuA / 4 * th_b + ust(MK0, Q)[0] + 2 * c.kap * c.CmuA * c.c6 * s[1]
            atomG = sqrt(c.kap * th_b / 2 * min(1.0, c.CmuA * th_b / 2))
            lin0 = 0.5 * c.dLp * c.C1A * (atomG + ust(M0 ** 2, G)[0])
        else:
            M0 = M1f(W0); K0 = K1f(W0)
            i0 = ust(M0, Om)[0] + OmA(c.c6 * th_hi, th_hi)
            q0 = ust(M0 * K0, Q)[0]
            lin0 = 0.5 * c.dLp * P0(c, th_hi) * ust(M0 * K0, G)[0]
        self.TH0 = c.dL * i0 + c.dL / 2 * q0 + lin0
        self.TH0parts = dict(I=c.dL * i0, quad=c.dL / 2 * q0, lin=lin0)
        if bottom:
            self._crude()

    def _crude(self):
        """explicit estimates on (0, x1] for the bottom cell (Lemma E(iii)); long part with factor (1+x1)^gam"""
        c, x1, u = self.c, self.x1, self.c.uc
        A_i, B_i = c.CmuA / 2 + c.CmuA * c.c6, c.CmuA * c.c6
        A_q, B_q = c.kap * c.CmuA / 4 + c.kap * c.c6 ** 2 / u, 2 * c.kap * c.CmuA * c.c6 ** 2
        cj2, dj2 = c.C1A * c.c6 * (0.5 + c.c6), sqrt(c.kap) * c.c6 ** 2 / 3 * u ** -1.5
        A_1, B_1 = c.C1A / 2 + c.c6 * sqrt(c.kap) * u ** -0.5, c.C1A * c.c6
        g1 = (1 + x1) ** (c.gam + 0.5)
        a_l, b_l = 0.5 * g1 * c.dL * c.kap * c.CTL, 0.5 * g1 * c.dLp * c.CV * sqrt(c.kap)
        Lx1 = a_l * x1 + b_l * sqrt(x1)
        lfc = c.dL * (1 + x1) ** c.gam / c.m
        il = lambda x: x * log(1 + u / x) + u * log(1 + x / u)
        lg = log(1 + u / x1)
        self.I_cr = (c.dL * (A_i * x1 + B_i * il(x1)) + c.dL / 2 * (A_q * x1 + B_q * il(x1))
                     + a_l * cj2 * x1 + 2 * b_l * cj2 * sqrt(x1) + Lx1 * dj2 * x1 + lfc * (A_1 * x1 + B_1 * il(x1)))
        Hx1 = (c.dL * (A_i + B_i * lg) + c.dL / 2 * (A_q + B_q * lg) + a_l * cj2 + b_l * cj2 / sqrt(x1) + Lx1 * dj2
               + lfc * (A_1 + B_1 * lg))
        self.T_cr = c.kap * x1 * Hx1

    def bound(self, r_lo=None, r_hi=None, which=None):
        """cell bound for r in [r_lo, r_hi] (None: r >= K_f+1, i.e. short-type only).
        which: None (total) or one of 'I','quad','lin','long' for the term attribution."""
        c = self.c
        if r_lo is None:
            mode = np.zeros(len(self.xl), int)                       # 0 short, 1 long, 2 either
        else:
            mode = np.where(self.xr <= r_lo - 1, 0, np.where(self.xl > r_hi - 1, 1, 2))
        rf = np.minimum(r_hi if r_hi is not None else 1.0, 1 + self.xr) ** c.gam    # long-type times: r < 1+x
        rs = (r_hi ** c.gam) if r_hi is not None else np.inf                       # short-type: r <= r_hi only
        def comb(I, quad, lin, L, linL):
            linS = np.minimum(lin, linL * rs)
            useD = L * rf <= quad + linL * rf                    # long-type: 1/D route or offset route (L)
            Lv = np.where(useD, L * rf, quad + linL * rf)
            Sv = quad + linS
            if which is not None:
                z = 0 * I
                I, Sv, Lv = dict(I=(I, z, z), quad=(z, quad, np.where(useD, 0, quad)),
                                 lin=(z, linS, np.where(useD, 0, linL * rf)),
                                 long=(z, z, np.where(useD, L * rf, 0)))[which]
            return I + np.where(mode == 0, Sv, np.where(mode == 1, Lv, np.maximum(Sv, Lv)))
        H = comb(self.IH, self.quadH, self.linH, self.LH, self.linLH)
        TH = comb(self.IT, self.quadT, self.linT, self.LT, self.linLT)
        Hst = np.maximum.accumulate(H[::-1])[::-1]
        THst = np.maximum.accumulate(TH[::-1])[::-1]
        TH0 = self.TH0 if which is None else self.TH0parts.get(which, 0.0)
        if self.bottom:
            Icr = self.I_cr if which is None else 0.0
            Tcr = self.T_cr if which is None else 0.0
            legs = max(Tcr, THst[0]) + c.kap * (Icr + self.x1 * Hst[0] + np.sum(Hst * self.dx))
            return TH0 + legs
        integ = THst[0] + c.kap * np.sum(Hst * self.dx)
        kmax = int(ceil(c.kap * c.Kf / self.th_lo)) - 1
        if kmax <= 200000:
            z = np.arange(1, kmax + 1) * self.th_lo / c.kap
            idx = np.clip(np.searchsorted(self.xl, z, side='right') - 1, 0, len(self.xl) - 1)
            legs = min(np.sum(THst[idx]), integ)
        else:
            legs = integ
        return TH0 + legs


def cell_sup(c, cell, dr=0.05, which=None):
    """sup over admissible r of the cell bound; r-cells of width dr on [max(1,K_eps th_lo), K_f+1], plus r >= K_f+1"""
    best = cell.bound(None, None, which)
    arg = None
    rmin = max(1.0, c.Ke * cell.th_lo)
    if rmin < c.Kf + 1:
        r = rmin
        while r < c.Kf + 1:
            r2 = min(r + dr, c.Kf + 1)
            v = cell.bound(r, r2, which)
            if v > best:
                best, arg = v, (r, r2)
            r = r2
    return best, arg


def Dprime(c, th_b=1e-7, q=1.03, nx=500, ns=700, dr=0.05):
    out = []
    cb = Cell(c, 0.0, th_b, nx, ns, bottom=True)
    v, a = cell_sup(c, cb, dr)
    out.append((0.0, th_b, v, a))
    hi = th_b
    while hi < 2.0:
        lo, hi = hi, min(hi * q, 2.0)
        cl = Cell(c, lo, hi, nx, ns)
        v, a = cell_sup(c, cl, dr)
        out.append((lo, hi, v, a))
    return out


def old_D(c):
    g, kap, Kf, dL = c.gam, c.kap, c.Kf, c.dL
    PsiI = 2 + log(Kf)
    TI = dL * (kap * c.c6 + 2) + c.c6 * c.chi * PsiI
    Ta = dL / c.c6 + c.chi * (2 + log(Kf))
    Tb = 2 ** g * (2 * dL + c.chi * (3 / 4 + (Kf ** g - 1) / (2 * g)))
    k0 = max(c.C1A, kap * 2 ** g * c.CA)
    DI = c.CmuA * TI
    t1 = c.c6 ** 2 * c.C1A ** 2 * Ta
    t2 = 2 * c.c6 ** 2 * kap * c.CTL * c.C1A * Tb
    t3 = 4 * dL * c.c6 * c.C1A * k0
    DIIl = c.c6 * (Kf + 1) ** g * c.C1A * Ta / c.m
    return dict(DI=DI, t1=t1, t2=t2, t3=t3, DIIs=t1 + t2 + t3, DIIl=DIIl, D=DI + max(t1 + t2 + t3, DIIl))


def report(c, quick=False):
    print(f"[{c.mode} tilt] C_A={c.CA:.6f} C_B={c.CB:.6f} C_TL={c.CTL:.6f} C_muA={c.CmuA:.6f} C_1A={c.C1A:.6f} "
          f"C_V={c.CV:.6f} c6={c.c6:.6f}")
    if c.mode == 'old':
        od = old_D(c)
        print("  OLD Prop 4.3: D_I={DI:.2f} D_IIs={DIIs:.2f} (= {t1:.1f} + {t2:.1f} + {t3:.1f}) D_IIl={DIIl:.2f} D={D:.2f}"
              .format(**od))
    nx, ns, q, dr = (250, 350, 1.08, 0.1) if quick else (500, 700, 1.03, 0.05)
    res = Dprime(c, q=q, nx=nx, ns=ns, dr=dr)
    worst = max(res, key=lambda t: t[2])
    bot = res[0]
    short_max = max((t for t in res if t[3] is None), key=lambda t: t[2])
    long_cells = [t for t in res if t[3] is not None]
    print(f"  bottom cell (0,1e-7]: {bot[2]:.3f};  cells evaluated: {len(res)}")
    for t in res[::max(1, len(res) // 18)]:
        print(f"    theta in [{t[0]:.3e},{t[1]:.3e}]  bound {t[2]:8.3f}  " + (f"r in [{t[3][0]:.2f},{t[3][1]:.2f}]" if t[3] else "short"))
    print(f"  max over short-type-binding cells: {short_max[2]:.3f} at theta in [{short_max[0]:.4g},{short_max[1]:.4g}]")
    if long_cells:
        lw = max(long_cells, key=lambda t: t[2])
        print(f"  max over cells where a long-type r binds: {lw[2]:.3f} at theta in [{lw[0]:.3g},{lw[1]:.3g}], r in "
              f"[{lw[3][0]:.2f},{lw[3][1]:.2f}]")
    print(f"  ==> D' <= {worst[2]:.3f}   (worst cell theta in [{worst[0]:.4g},{worst[1]:.4g}], r: {worst[3]})")
    # attribution at the worst cell (each term majorised separately)
    if worst[0] > 0:
        cl = Cell(c, worst[0], worst[1], nx, ns)
    else:
        cl = Cell(c, 0.0, worst[1], nx, ns, bottom=True)
    rr = worst[3] if worst[3] else (None, None)
    parts = {w: cl.bound(rr[0], rr[1], which=w) for w in ('I', 'quad', 'lin', 'long')}
    print("  attribution at the worst cell (separately majorised; sum >= total): " +
          ", ".join(f"{k} {v:.2f}" for k, v in parts.items()) + f"; of which gap-0 leg {cl.TH0:.2f}")
    for nm, t in (('short', short_max),) + ((('long', max(long_cells, key=lambda t: t[2])),) if long_cells else ()):
        cl2 = Cell(c, t[0], t[1], nx, ns) if t[0] > 0 else Cell(c, 0.0, t[1], nx, ns, bottom=True)
        r2 = t[3] if t[3] else (None, None)
        pp = {w: cl2.bound(r2[0], r2[1], which=w) for w in ('I', 'quad', 'lin', 'long')}
        print(f"  attribution, worst {nm} cell: " + ", ".join(f"{k} {v:.2f}" for k, v in pp.items()))
    th = c.fF ** 2 + 2 * c.v0 * worst[2]
    print(f"  theta_bar(v0={c.v0}) = {th:.5f};  v0 at which (P6) binds: {(1 - c.fF ** 2) / (2 * worst[2]):.4e}")
    return worst[2]


if __name__ == "__main__":
    args = sys.argv[1:]
    quick = '--quick' in args
    P = dict(INP)
    print("INPUTS (main tuple p of r9/base_short/verify_constants.out): " + ", ".join(f"{k}={v}" for k, v in P.items()))
    if '--old' in args or '--both' in args:
        report(C(P, 'old'), quick)
    if '--old' not in args:
        CT = float(args[args.index('--CT') + 1]) if '--CT' in args else CT_RTILT
        report(C(P, 'new', CT), quick)
