"""r9/tilt/tilt_constants.py -- stream R-tilt: new tilt constants and the resulting near-pair constant D.

Reads the INPUTS of r9/base_short/verify_constants.py (same strings), recomputes the old constants (as a check against
verify_constants.out) and the new ones of reports/R9-tilt.md:

  s(r)      = (kappa^{1/2}/c_A) * ( r/2 if r<=2 else (r-1)^{1/2} )            one-step factor (Lemma T(o))
  r_*       = max(q, 2q/(q-1)),   omega_* = (1 - m^2 r_*/(4 c_A))^{-1/2}
  C_T       = omega_* * max( sigma_q s(q), s(2q/(q-1)) )                     replaces C_A, C_B, C_TL
  C_mu      = 1 + kappa C_T^2                                                replaces C_muA (enters only via logs / shapes)
  D_I'      = T_I + c6 chi log C_mu
  Pi_alpha  = c6^2 kappa [ dL/c6 + chi (2 + log C_mu - 1/(2K_f)) ]
  Pi_0      = dL * max( 2 c6^2 kappa S_0 , kappa^2 2^gamma / c_A )
  Pi_beta   = 2 c6^2 kappa chi int_0^{K_f} B,  B(x) = x^{1/2}(1+x)^gamma (1+kappa x/c_A) k3(x)
  D_IIs'    = Pi_alpha + Pi_0 + Pi_beta
  D_IIl'    = c6 (K_f+1)^gamma kappa^{1/2} T_l / m,   T_l = dL/c6 + chi (3 + log K_f - C_mu^{-1/2})     (drop-in)
  D_IIl''   = sup_{1<=mu<=K_f+1} [ S(mu) + Lambda(mu) ]                                              (split long case)
  C_p'      = kappa^{1/2}(1+1/K_f)^{1/2+gamma} K_f^{-1/2} + kappa C_T (1+1/K_f)^gamma

All sup / integral evaluations are rigorous upper bounds (monotone pieces + Riemann/grid upper sums at 40 digits);
an independent mp.quad value is printed next to each integral.
"""
import importlib.util
import os
import sys

import mpmath as mp

mp.mp.dps = 40
M = mp.mpf
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, '..', 'base_short', 'verify_constants.py')

# ---- load the INPUTS dict without running verify_constants (its main runs at import only under __main__) ----------
spec = importlib.util.spec_from_file_location('vc', BASE)
vc = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0]]
spec.loader.exec_module(vc)
INP = {k: M(s) for k, s in vc.INPUTS.items()}


def kfun(C):
    """dimensionless profile functions and their primitives (closed forms), for a given C = C_mu >= 1."""
    C = M(C)
    rC = mp.sqrt(C)

    def kk(z):   # int_z^inf eta^-3 min(1,eta) min(1,C eta)
        if z >= 1:
            return 1 / (2 * z ** 2)
        if z >= 1 / C:
            return 1 / z - M(1) / 2
        return C * mp.log(1 / (C * z)) + C - M(1) / 2

    def Ikk(X):  # int_0^X kk
        X = M(X)
        if X <= 1 / C:
            return C * (X * mp.log(1 / (C * X)) + X) + (C - M(1) / 2) * X if X > 0 else M(0)
        v = 2 - 1 / (2 * C)
        if X <= 1:
            return v + mp.log(C * X) - (X - 1 / C) / 2
        v += mp.log(C) - (1 - 1 / C) / 2
        return v + (1 - 1 / X) / 2

    def k2(z):   # int_z^inf eta^-2 (min(1,eta) min(1,C eta))^{1/2}
        if z >= 1:
            return 1 / z
        if z >= 1 / C:
            return 2 / mp.sqrt(z) - 1
        return rC * (mp.log(1 / (C * z)) + 2) - 1

    def Ik2(X):  # int_0^X k2
        X = M(X)
        if X <= 0:
            return M(0)
        if X <= 1 / C:
            return rC * (X * mp.log(1 / (C * X)) + 3 * X) - X
        v = 3 / rC - 1 / C
        if X <= 1:
            return v + 4 * (mp.sqrt(X) - 1 / rC) - (X - 1 / C)
        v += 4 * (1 - 1 / rC) - (1 - 1 / C)
        return v + mp.log(X)

    def k3(z):   # int_z^inf eta^-3 (min(1,eta) min(1,C eta))^{1/2}
        if z >= 1:
            return 1 / (2 * z ** 2)
        if z >= 1 / C:
            return M(2) / 3 * z ** (-M(3) / 2) - M(1) / 6
        return rC / z - C ** (M(3) / 2) / 3 - M(1) / 6

    return kk, Ikk, k2, Ik2, k3


def compute(gam, label, qc=None, verbose=True):
    I = INP
    R, m, s0, kap, cA = I['R'], I['m'], I['s0'], I['kap'], I['cA']
    KR, Kf, Ke, eta1 = I['KR'], I['Kf'], I['Keps'], I['eta1']
    qc = I['qc'] if qc is None else M(qc)
    dL, dl1 = I['dL'], I['delta1']
    gam = M(gam)
    out = {}
    chig = kap * dL
    c6 = (1 + dl1) / cA
    # ---------------- old constants (Def 3.3) ----------------
    ct = lambda r: (mp.sqrt(kap) * r ** (M(1) / 2 + gam) + m / 2) / cA
    sq = 1 / (1 - qc ** (-gam))
    CA = sq * ct(qc)
    CB = CA + ct(M(3))
    CTL = CA + CB
    CmuA = 1 + kap * CA ** 2
    C1A = mp.sqrt(kap * CmuA)
    crho = cA - (2 * dl1 + kap) / Kf
    rf = 1 + 1 / (Kf - 2)
    Cp = kap * (ct(rf) + CB * (1 + 1 / Kf) ** gam)
    B3 = 2 * kap ** M(1.5) * Cp / crho ** 3
    PsiI = 2 + mp.log(Kf)
    TI = dL * (kap * c6 + 2) + c6 * chig * PsiI
    Ta = dL / c6 + chig * (2 + mp.log(Kf))
    Tb = 2 ** gam * (2 * dL + chig * (M(3) / 4 + (Kf ** gam - 1) / (2 * gam)))
    k0 = max(C1A, kap * 2 ** gam * CA)
    DI = CmuA * TI
    DIIs_terms = (c6 ** 2 * C1A ** 2 * Ta, 2 * c6 ** 2 * kap * CTL * C1A * Tb, 4 * dL * c6 * C1A * k0)
    DIIs = sum(DIIs_terms)
    DIIl = c6 * (Kf + 1) ** gam * C1A * Ta / m
    Dold = DI + max(DIIs, DIIl)
    B5 = 2 / crho * ((Cp + mp.sqrt(kap) * Kf ** (-1 - gam)) ** 2 / crho ** 2 + Kf ** (-2 * gam))
    out.update(CA=CA, CB=CB, CTL=CTL, CmuA=CmuA, C1A=C1A, k0=k0, DI=DI, DIIs=DIIs, DIIl=DIIl, Dold=Dold, Cp=Cp,
               B3=B3, B5=B5, TI=TI, Ta=Ta, Tb=Tb)
    out['DIIs_terms'] = DIIs_terms

    # ---------------- new constants ----------------
    s = lambda r: mp.sqrt(kap) / cA * (r / 2 if r <= 2 else mp.sqrt(r - 1))
    r2 = 2 * qc / (qc - 1)
    rstar = max(qc, r2)
    omarg = 1 - m ** 2 * rstar / (4 * cA)
    assert omarg > 0
    om = 1 / mp.sqrt(omarg)
    CT = om * max(sq * s(qc), s(r2))
    Cmu = 1 + kap * CT ** 2
    rC = mp.sqrt(Cmu)
    kk, Ikk, k2, Ik2, k3 = kfun(Cmu)
    # side conditions used in the proofs
    sides = [
        ('m^2 r_*/(4 c_A) < 1', m ** 2 * rstar / (4 * cA), '<', 1),
        ('C_mu K_f >= 1', Cmu * Kf, '>=', 1),
        ('C_mu >= (1+2gamma) kappa / c_A   [B monotone, small x]', Cmu, '>=', (1 + 2 * gam) * kap / cA),
        ('gamma <= c_A/kappa               [B monotone, middle]', gam, '<=', cA / kap),
        ('K_f (2gamma-1) <= 3 c_A/kappa    [B monotone, x>=1]', Kf * (2 * gam - 1), '<=', 3 * cA / kap),
        ('K_f >= 1', Kf, '>=', 1),
    ]
    ok = all({'<': a < b, '<=': a <= b, '>=': a >= b}[rel] for _, a, rel, b in sides)

    # D_I'
    DIn = TI + c6 * chig * mp.log(Cmu)
    # Pi_alpha
    IkkK = Ikk(Kf)
    assert abs(IkkK - (2 + mp.log(Cmu) - 1 / (2 * Kf))) < M(10) ** -30
    Pa = c6 ** 2 * kap * (dL / c6 + chig * IkkK)
    # Pi_0: S_0 = sup_{0<xi<=2} f(xi), f = xi * A(xi) * k3(c6 xi), A increasing, k3 decreasing.
    A = lambda xi: mp.sqrt(min(xi, 1) * min(Cmu * xi, 1))
    xi0 = M(10) ** -6  # on (0, xi0]: f <= C xi / c6  (A = C^{1/2} xi, k3(z) <= C^{1/2}/z)
    S0 = Cmu * xi0 / c6
    n = 20000
    grid = [xi0 * (2 / xi0) ** (M(i) / n) for i in range(n + 1)]   # geometric grid on [xi0, 2]
    for i in range(n):
        a_, b_ = grid[i], grid[i + 1]
        S0 = max(S0, b_ * A(b_) * k3(c6 * a_))
    S0point = max(g * A(g) * k3(c6 * g) for g in grid)
    P0a = 2 * c6 ** 2 * kap * S0
    P0b = kap ** 2 * 2 ** gam / cA
    P0 = dL * max(P0a, P0b)
    # Pi_beta: int_0^{K_f} B, B non-increasing (proved under the side conditions)
    P = lambda x: (1 + x) ** gam * (1 + kap * x / cA)
    B = lambda x: mp.sqrt(x) * P(x) * k3(x)
    c0 = Cmu ** M(1.5) / 3 + M(1) / 6
    # on (0,1/C]: B = P(x) u(x), u = C^{1/2} x^{-1/2} - c0 x^{1/2} >= 0, P increasing; U = primitive of u.
    U = lambda x: 2 * rC * mp.sqrt(x) - M(2) / 3 * c0 * x ** M(1.5)
    ns = 400
    sg = [M(0)] + [(1 / Cmu) * (M(10) ** -8) ** (1 - M(i) / ns) for i in range(ns + 1)]   # 0, geometric to 1/C

    def IBsmall_up(X):   # rigorous upper bound of int_0^X B, X <= 1/C
        tot = M(0)
        for i in range(len(sg) - 1):
            a_, b_ = sg[i], min(sg[i + 1], X)
            if b_ <= a_:
                break
            tot += P(b_) * (U(b_) - U(a_))
        return tot

    IB_small = IBsmall_up(1 / Cmu)                                      # rigorous bound of int_0^{1/C} B
    # left Riemann sums on [1/C, K_f] (upper sums since B is non-increasing); cumulative table for S(mu)
    nb = 6000
    xs = [1 / Cmu + (Kf - 1 / Cmu) * M(i) / nb for i in range(nb + 1)]
    h = (Kf - 1 / Cmu) / nb
    cumB = [IB_small]
    for i in range(nb):
        cumB.append(cumB[-1] + h * B(xs[i]))
    IB = cumB[-1]
    IBq = mp.quad(B, [0, 1 / Cmu, 1, Kf])
    # monotonicity spot check of B on the grid
    mono = all(B(xs[i]) >= B(xs[i + 1]) for i in range(nb))
    Pb = 2 * c6 ** 2 * kap * chig * IB
    DIIsn = Pa + P0 + Pb
    # D_IIl' (drop-in)
    Ik2K = Ik2(Kf)
    assert abs(Ik2K - (3 + mp.log(Kf) - 1 / rC)) < M(10) ** -30
    Tl = dL / c6 + chig * Ik2K
    DIIln = c6 * (Kf + 1) ** gam * mp.sqrt(kap) * Tl / m
    # D_IIl'' (split long case): sup over mu of S(mu) + Lambda(mu); grid upper bound.
    def cumB_upper(X):   # upper bound of int_0^X B for 0 <= X <= K_f
        if X <= 1 / Cmu:
            return IBsmall_up(X)
        j = int(mp.ceil((X - 1 / Cmu) / h))
        return cumB[min(j, nb)]

    def S_up(mu):
        X = min(mu - 1, Kf)
        return c6 ** 2 * kap * (dL / c6 + chig * Ikk(X)) + P0 + 2 * c6 ** 2 * kap * chig * cumB_upper(X)

    def Lam(mu_lo, mu_hi):   # upper bound of Lambda on [mu_lo, mu_hi]
        if mu_lo - 1 >= Kf:
            return M(0)
        return c6 * mp.sqrt(kap) / m * mu_hi ** gam * (dL / c6 + chig * (Ik2K - Ik2(mu_lo - 1)))

    nm = 3000
    mus = [1 + Kf * M(i) / nm for i in range(nm + 1)]
    best, argbest = M(0), None
    for i in range(nm):
        val = S_up(mus[i + 1]) + Lam(mus[i], mus[i + 1])
        if val > best:
            best, argbest = val, mus[i]
    DIIlsplit = max(best, S_up(Kf + 1))
    Lam1 = Lam(M(1), M(1))
    # far pairs
    Cpn = mp.sqrt(kap) * (1 + 1 / Kf) ** (M(1) / 2 + gam) / mp.sqrt(Kf) + kap * CT * (1 + 1 / Kf) ** gam
    B3n = 2 * kap ** M(1.5) * Cpn / crho ** 3
    B5n = 2 / crho * ((Cpn + mp.sqrt(kap) * Kf ** (-1 - gam)) ** 2 / crho ** 2 + Kf ** (-2 * gam))
    Dn_dropin = DIn + max(DIIsn, DIIln)
    Dn_split = DIn + max(DIIsn, DIIlsplit)
    out.update(s_q=s(qc), sq=sq, r2=r2, s_r2=s(r2), om=om, CT=CT, Cmu=Cmu, DIn=DIn, Pa=Pa, S0=S0, S0point=S0point,
               P0a=P0a, P0b=P0b, P0=P0, IB=IB, IBq=IBq, IB_small=IB_small, mono=mono, Pb=Pb, DIIsn=DIIsn,
               Tl=Tl, DIIln=DIIln, DIIlsplit=DIIlsplit, argmu=argbest, Lam1=Lam1, Cpn=Cpn, B3n=B3n, B5n=B5n,
               Dn_dropin=Dn_dropin, Dn_split=Dn_split, sides=sides, sides_ok=ok, qc=qc)
    if verbose:
        f = lambda x: mp.nstr(x, 8)
        print('=' * 100)
        print('%s   gamma=%s  q=%s' % (label, mp.nstr(gam, 7), mp.nstr(qc, 7)))
        print('-- old (Def 3.3; must agree with verify_constants.out)')
        print('   C_A=%s C_B=%s C_TL=%s C_muA=%s C_1A=%s k0=%s' % tuple(map(f, (CA, CB, CTL, CmuA, C1A, k0))))
        print('   D_I=%s  D_IIs=%s [= %s + %s + %s]  D_IIl=%s  D=%s' % (f(DI), f(DIIs), *map(f, DIIs_terms), f(DIIl),
                                                                   f(Dold)))
        print('   C_p=%s B_3=%s B_5=%s' % (f(Cp), f(B3), f(B5)))
        print('-- new')
        print('   s(q)=%s sigma_q=%s 2q/(q-1)=%s s(2q/(q-1))=%s omega_*=%s' % tuple(map(f, (s(qc), sq, r2, s(r2), om))))
        print('   C_T (= new C_A = C_B = C_TL) = %s      C_mu = 1+kappa C_T^2 = %s   (C_1 := (kappa C_mu)^1/2 = %s)'
              % (f(CT), f(Cmu), f(mp.sqrt(kap * Cmu))))
        for nm_, a, rel, b in sides:
            print('   side: %-55s %s %s %s' % (nm_, f(a), rel, f(b)))
        print('   side conditions: %s ; B non-increasing on grid: %s' % ('OK' if ok else 'FAIL', mono))
        print('   D_I\'      = T_I + c6 chi log C_mu                = %s' % f(DIn))
        print('   Pi_alpha  = c6^2 kappa[dL/c6+chi(2+log C_mu-1/(2Kf))] = %s' % f(Pa))
        print('   S_0 (rigorous grid bound) = %s  (pointwise max on grid %s);  2c6^2 kappa S_0 = %s ; kappa^2 2^g/c_A = %s'
              % (f(S0), f(S0point), f(P0a), f(P0b)))
        print('   Pi_0      = %s' % f(P0))
        print('   int_0^Kf B: rigorous upper %s   (mp.quad %s; [0,1/C] piece bound %s)' % (f(IB), f(IBq), f(IB_small)))
        print('   Pi_beta   = 2 c6^2 kappa chi int B              = %s' % f(Pb))
        print('   D_IIs\'    = %s' % f(DIIsn))
        print('   T_l = %s ;  D_IIl\' (drop-in) = %s' % (f(Tl), f(DIIln)))
        print('   D_IIl\'\' (split) = %s  (attained near mu=%s; Lambda(1)=%s)' % (f(DIIlsplit), f(argbest), f(Lam1)))
        print('   C_p\'=%s  B_3\'=%s  B_5\'=%s' % (f(Cpn), f(B3n), f(B5n)))
        print('   D new (drop-in, D_I\'+max(D_IIs\',D_IIl\'))   = %s    (old %s, ratio %s)'
              % (f(Dn_dropin), f(Dold), f(Dold / Dn_dropin)))
        print('   D new (split long case)                    = %s    (ratio %s)' % (f(Dn_split), f(Dold / Dn_split)))
    return out


if __name__ == '__main__':
    print('INPUTS:', ', '.join('%s=%s' % (k, v) for k, v in vc.INPUTS.items()))
    main = compute(INP['gam'], 'main tuple p')
    A = compute(INP['gD'], 'stage-A tuple p_A')
    # optimal chain ratio q for C_T (q is a free parameter of the tuple; it enters only C_A in the old text)
    s = lambda r, kap=INP['kap'], cA=INP['cA']: mp.sqrt(kap) / cA * (r / 2 if r <= 2 else mp.sqrt(r - 1))
    g = INP['gam']
    vals = []
    for i in range(101, 600):
        q = M(i) / 100
        vals.append((max(s(q) / (1 - q ** (-g)), s(2 * q / (q - 1))), q))
    v, qopt = min(vals)
    print('=' * 100)
    print('optimal chain ratio: q = %s gives max(sigma_q s(q), s(2q/(q-1))) = %s (vs %s at q_c)'
          % (mp.nstr(qopt, 4), mp.nstr(v, 8), mp.nstr(max(s(INP['qc']) / (1 - INP['qc'] ** (-g)),
                                                          s(2 * INP['qc'] / (INP['qc'] - 1))), 8)))
    compute(INP['gam'], 'main tuple p with optimal q', qc=qopt)
