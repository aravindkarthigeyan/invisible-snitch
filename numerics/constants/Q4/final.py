"""
code/Q4/final.py -- the final constant v0 of the proof chain
    touch-down (H_T)   : Theorem Q.H of referee/Q3-claims.md  (code/Q3/constants.py, + (SC51) of referee-RQ3-1)
    core               : Theorem / Corollary End* of referee/Q1-claims.md, FINAL  (code/Q1/q1const.py, imported unchanged)
    assembly           : Theorems Q2.E', Q2.D, Lemma Q2.H, Theorem Q2.M of referee/Q2-claims.md (side conditions §4.2,
                         replicated from code/Q2/assembly_constants.py) with the referee fixes of RQ2-1/RQ2-2:
                         (F-H)/(M2) eps <= delta0 in the H-list; (F-D)/(M1) Q2.D applied with the actual duration
                         t_w - t_td <= D (constants are computed with the bound D; all are non-decreasing in D).
The INTERIM End* formulas of code/Q2/assembly_constants.py::endstar() are NOT used: the core is q1const.derived /
theorem_conditions / corollary_conditions verbatim.

Free parameters (search):  core  gam, m, s0, k1, cA, KR, Kf, Ke, eta1 (Q1's eta), q, R
                           assembly  ombar, kfac, dfrac (delta0 = dfrac*R)
                           touch-down  vbar, eta (Q3 window), G (Q3), a' = 1 - muT_bar (optimal: see report)
Dependent (set to their smallest admissible value):  d = 1/(1-v), delta1 = e^{2v/(1-v)}, nu = c_amp v,
   gamma_D = gam + nu + eta_N, A0 = exp(max LHS(P4) over main/stage A), f = max LHS(P5) over main/stage A.
Stage A = Corollary End* on [0,U_A] with p_A := p, gam -> gamma_D (Q2-claims §4.2), c_sep^A = min(c_sep, kappa2(U_min-U_A)).

Usage:
   python final.py search  [eta=0.1] [KRmax=32]    float search, writes out/search_<tag>.json
   python final.py verify                            verify the stored optimum + the rounded values in mpmath, out/final.txt
"""
import sys, os, math, json, time
import numpy as np
import mpmath
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'Q1'))
sys.path.insert(0, os.path.join(HERE, '..', 'Q3'))
from q1const import FloatLib, MpLib, derived, theorem_conditions, corollary_conditions, check   # FINAL End*
import constants as q3c                                                                          # Q3 Theorem Q.H
mpmath.mp.dps = 50
FL = FloatLib()

# ----------------------------------------------------------------------------------------------------------------
# touch-down data (Q3), cached; exact 50-digit values from chain(); (SC51) added (referee-RQ3-1 §3)
_Q3 = {}


def q3_chain(vbar, eta, epsbar='1e-3', G=None):
    key = (str(vbar), str(eta), str(epsbar), None if G is None else str(G))
    if key not in _Q3:
        K, cond = q3c.chain(str(vbar), str(eta), str(epsbar), G=None if G is None else str(G))
        mpmath.mp.dps = 50
        cond = dict(cond)
        xb = K['xe_bar']; zT = K['z_T']
        cond['(SC51a) z_T xbar_e + epsbar < 1'] = zT * xb + K['eb'] < 1
        cond['(SC51b) G + z_T xbar_e <= 1'] = K['G'] + zT * xb <= 1
        _Q3[key] = (K, cond)
    return _Q3[key]


def q3_data(vbar, eta, L, epsbar='1e-3', G=None, ap=None):
    """(H_T*) data of Q2-claims §4.1 (Q3 form).  ap=None: a' = 1 - muT_bar (largest admissible), C0 = c_N."""
    K, cond = q3_chain(vbar, eta, epsbar, G)
    o = L.one
    cv = (lambda x: float(x)) if isinstance(L, FloatLib) else (lambda x: mpmath.mpf(x))
    muTb = K['muT']; mub = K['mu']
    apmax = 1 - muTb
    a = apmax if ap is None else mpmath.mpf(ap)
    d = dict(v_T=cv(K['v']), eps_T=cv(K['eb']), T2=cv(K['T2']), U_max=cv(K['U_max']), U_min=cv(1), lam0=cv(K['lam0']),
             c_sep=cv(K['c_sep']), kappa2=cv(K['kap2']), K_fw=cv(K['th_v']), G_T=cv(K['G']), K_tl=cv(K['c_T4']),
             kz=cv(1), c_zlo=cv(K['h_t'] * K['xe_lo']), c_zhi=cv(K['z_T'] * K['xe_hi']), c_y=cv(K['c_y']),
             mu_b=cv(mub), muT_b=cv(muTb), ap=cv(a), ap_max=cv(apmax), C0=cv(K['c_N'] * K['lam0'] ** (1 - muTb - a)),
             c_N=cv(K['c_N']))
    return d, cond, K


# ----------------------------------------------------------------------------------------------------------------
def build(th, v, data, L, fixed=None, infl=0.0):
    """All conditions of the chain (core main + stage A, corollary main + stage A, assembly) at (v, eps_*).
    th: free parameters; fixed: optional dict of the dependent quantities (d, dl1, nu, gD, A0, f, R, eps) used as given.
    Returns (conds, der).  conds: list of (name, lhs, rhs, kind)."""
    o = L.one
    N = lambda x: (L.num(x) * o) if not isinstance(x, str) else L.num(x)
    up = 1 + N(infl)
    v = N(v)
    P = {k: N(th[k]) for k in ('gam', 'm', 's0', 'k1', 'cA', 'KR', 'Kf', 'Ke', 'q', 'ombar', 'kfac', 'dfrac')}
    P['eta'] = N(th['eta1'])
    fx = fixed or {}
    # ---- dependent majorants (P1), (P3) ----
    p = dict(gam=P['gam'], m=P['m'], s0=P['s0'], k1=P['k1'], cA=P['cA'], KR=P['KR'], Kf=P['Kf'], Ke=P['Ke'],
             eta=P['eta'], q=P['q'], v=v, U=N(data['U_max']))
    p['d'] = N(fx['d']) if 'd' in fx else 1 / (1 - v) * up
    p['dl1'] = N(fx['dl1']) if 'dl1' in fx else L.exp(2 * v / (1 - v)) * up
    p['R'] = N(th['R']) if 'R' not in fx else N(fx['R'])
    c0 = derived(p, L)
    p['nu'] = N(fx['nu']) if 'nu' in fx else c0['camp'] * v * up
    nu = p['nu']
    R = p['R']
    # ---- assembly geometry (Q2-claims §4.2) ----
    kap2 = data['kappa2']
    cA, KR, k1 = p['cA'], p['KR'], p['k1']
    W1 = cA * KR * R / kap2
    om_bar = P['ombar']
    zeta = L.sqrt(1 - om_bar ** 2) - v
    etaD = v / zeta
    etaN = 1.375 * o * v / zeta
    gD = N(fx['gD']) if 'gD' in fx else (p['gam'] + nu + etaN) * up
    eps = N(fx['eps']) if 'eps' in fx else min(data['eps_T'], R / p['Ke'], (R / (100 * data['c_zhi'])) ** 2)
    delta0 = P['dfrac'] * R
    UA = W1 + delta0 + R
    UE = W1 + R
    D = (k1 * W1 + eps) / (1 - v)
    z0max = data['c_zhi'] * L.sqrt(eps)
    Xs = UE + z0max + D
    Gf = W1 + eps + delta0
    # ---- core: main (U = U_max) and stage A (gam -> gamma_D, U = U_A) ----
    pA = dict(p); pA['gam'] = gD; pA['U'] = UA
    c = derived(p, L); cAA = derived(pA, L)
    # A0, f: smallest admissible common values (P4), (P5) for both applications
    def p4(pp, cc):
        return pp['v'] * (2 * cc['a1'] * pp['d'] / (cc['crho'] * pp['Kf']) + cc['a2'] * cc['chi'] * pp['U'] / (cc['cR'] * pp['R']))
    if 'A0' in fx:
        A0 = N(fx['A0'])
    else:
        A0 = L.exp(max(p4(p, c), p4(pA, cAA))) * up
    p['A0'] = A0; pA['A0'] = A0
    p['f'] = p['s0']; pA['f'] = p['s0']
    _, tm = theorem_conditions(p, c, L, with_Pc=False)
    _, tA = theorem_conditions(pA, cAA, L, with_Pc=False)
    if 'f' in fx:
        f = N(fx['f'])
    else:
        f = max(A0 * (tm['T1'] + tm['T2'] + tm['T3']), A0 * (tA['T1'] + tA['T2'] + tA['T3'])) * up
    p['f'] = f; pA['f'] = f
    C = []
    cm, tm = theorem_conditions(p, c, L, with_Pc=False)
    C += [('[main core] ' + n, l, r, k) for (n, l, r, k) in cm]
    Dm = dict(ap=data['ap'], C0=data['C0'], lam0=data['lam0'], csep=data['c_sep'])
    C += [('[main cor] ' + n, l, r, k) for (n, l, r, k) in corollary_conditions(p, c, Dm, L)]
    cA_sep = min(data['c_sep'], kap2 * (data['U_min'] - UA))
    cs, tA = theorem_conditions(pA, cAA, L, with_Pc=False)
    C += [('[stage A core] ' + n, l, r, k) for (n, l, r, k) in cs]
    DA = dict(Dm); DA['csep'] = cA_sep
    C += [('[stage A cor] ' + n, l, r, k) for (n, l, r, k) in corollary_conditions(pA, cAA, DA, L)]
    C += [('U_min - U_A >= W1 (stage-A pairs good)', W1, data['U_min'] - UA, '<='),
          ('gamma_D >= gam + nu + eta_N (exponents in (TW))', p['gam'] + nu + etaN, gD, '<='),
          ('S3* eps <= R/K_eps', eps, R / p['Ke'], '<=')]
    # ---- Lemma Q2.H (stage-A constants) ----
    mu = max(v / (1 - v), data['mu_b']); muT = max(3 * v / (1 + v), data['muT_b'])
    CAm1, CBm1, cA1, m1, dl1 = cAA['CA'] * p['m'], cAA['CB'] * p['m'], cA, p['m'], p['dl1']
    kad = k1
    C3m = 2 * CBm1 + CAm1
    sig = data['K_fw'] * Gf ** (1 - mu)
    ksig = (1 + sig / 2) / (1 - sig ** 2 / 2)
    thf = data['K_fw'] * Gf ** (1 - mu - gD)
    rho_st = cA1 * (R - delta0 - eps) - dl1 * eps
    Krot = (kad / (1 - v)) * (2 * R / (cA1 * delta0) + (W1 + eps) / rho_st)
    om0 = CAm1 * (delta0 / R) ** gD + ksig * sig + v * Krot
    ctau = 1 / (1 - m1 ** 2 / 2)
    thh1 = (CAm1 * R ** (-gD) + 2 ** gD * ksig * thf + v * 4 * kad * C3m / (cA1 * (1 - v)) * 2 ** gD * R ** (-gD))
    thh = ctau ** gD * max(thh1, om0 * delta0 ** (-gD))
    C += [('H: G_f <= G_T', Gf, data['G_T'], '<='), ('H: delta0 <= R/2', delta0, R / 2, '<='),
          ('H: eps <= delta0  [fix F-H/M2]', eps, delta0, '<='),
          ('H: sigma <= 1/2', sig, o / 2, '<='), ('H: rho_* >= eps', eps, rho_st, '<='),
          ('H: m1^2 < 2', m1 ** 2, 2 * o, '<'), ('H: gamma_h <= 1-mu', gD, 1 - mu, '<='),
          ('H: U_A >= W1+2eps+delta0 (legs common)', W1 + 2 * eps + delta0, UA, '<='),
          ('H: kappa_adv <= 2 (advance in [eps/2,R1])', kad, 2 * o, '<='),
          ('H: K_R1 >= 1', o, KR, '<=')]
    # ---- Theorem Q2.D ----
    th0 = data['K_tl'] * data['kz'] ** (-(1 - muT)) * Xs ** (1 - muT - gD)
    thy = data['c_y'] * 2 ** (2 - muT) * z0max ** (1 - muT - gD)        # Q3 form |y0| <= c_y (z0+eps)^(2-muT)
    th0y = max(th0, thy)
    Th0 = th0 + v * th0y / zeta ** 2 + v * thh / (zeta ** 2 * (1 - etaD) * (gD - etaD))
    omT = Th0 * Xs ** gD
    xc = (om0 / thh) ** (1 / gD)
    Lh = 1 / (2 * gD) + max(0 * o, L.log((D + eps) / xc))
    Kw = (Th0 + th0y / zeta) ** 2 * Xs ** (2 * gD) / (gD * zeta) + 2 * om0 ** 2 * Lh / (zeta ** 3 * (1 - etaD) ** 2)
    dt = L.exp(v * Kw) - 1
    k = P['kfac'] * 4 * (1 + dt) / zeta
    Thb = Th0 + th0y / zeta + thh / (zeta * (1 - etaD))
    cn = L.sqrt(1 + dt) * k ** gD / (gD * zeta)
    omy = thy * Xs ** gD
    Thp = (1 + omy + v) * (1 + 1 / k) ** gD * Th0 / (1 - omT ** 2 / 2) + th0y + thh / (1 - etaD)
    cbeta = 2 * (1 + dt) ** (3 * o / 2) * k ** (gD - 1) / (zeta ** 3 * (1 - gD))
    Ktail = cn * Thb + cbeta * Thp
    TS = (1 + D / (k * R)) ** etaN * (data['C0'] * R ** data['ap'] + v * Ktail * R ** gD)
    C += [('D: X_* <= 1', Xs, o, '<='), ('D: zeta > 0', 0 * o, zeta, '<'), ('D: ombar <= 1/2', om_bar, o / 2, '<='),
          ('D: kfac >= 1', o, P['kfac'], '<='),
          ('D: theta0 X_*^g <= ombar', th0 * Xs ** gD, om_bar, '<='),
          ('D: theta_y X_*^g <= ombar', omy, om_bar, '<='), ('D: omega0 <= ombar', om0, om_bar, '<='),
          ('D: omega_T <= 1/2', omT, o / 2, '<='), ('D: eta=v/zeta <= gamma_D/2', etaD, gD / 2, '<='),
          ('D: gamma_D <= 1-muT', gD, 1 - muT, '<='), ('D: gamma_D < 1', gD, o, '<'),
          ('D: 1+gamma_D <= 2-muT (y0, Q3 form)', 1 + gD, 2 - muT, '<='),
          ('D: z0max <= 1', z0max, o, '<='),
          ('D: z0 >= eps/zeta', eps / zeta, data['c_zlo'] * eps ** (1 / (2 - 2 * v)), '<='),
          ('D: U_E <= G_T', UE, data['G_T'], '<=')]
    # ---- (TW), (PT) ----
    LJexp = L.exp(tm['Xfar'] + c['B5'] * c['I5'] * v * p['m'] ** 2)
    P7L = LJexp + v * k1 * c['tauI']
    startfac = (p['Kf'] / KR) ** nu if p['Kf'] < KR else o
    C += [('TW: gamma_D + nu <= a\' (C5 for stage A; also gamma_D <= a\')', gD + nu, data['ap'], '<='),
          ('TW (TS) tail start bound', TS, p['s0'] * p['m'] * startfac, '<='),
          ('TW far at t_w: max(Kf,KR)R <= U_min-U_E-W1-eps', max(KR, p['Kf']) * R, data['U_min'] - UE - W1 - eps, '<='),
          ('PT (Q1 form P7_delta) (1+dt)e^(..) + v k1 tauI < k1', (1 + dt) * LJexp + v * k1 * c['tauI'], k1, '<'),
          ('PT (Q2 form) (1+dt) LHS(P7) < k1', (1 + dt) * P7L, k1, '<'),
          ('v <= vbar (= v_T)', v, data['v_T'], '<='), ('eps_* <= epsbar', eps, data['eps_T'], '<='),
          ('E\': U >= 2W1+R+eps (U >= U_min)', 2 * W1 + R + eps, data['U_min'], '<=')]
    if th.get('capCTL') is not None:       # optional variant: old tilt normalisation (NOT needed by Q2's proofs)
        C += [('VARIANT cap C_TL m', c['CTL'] * p['m'], N(th['capCTL']), '<='),
              ('VARIANT cap C_TL m (stage A)', cAA['CTL'] * p['m'], N(th['capCTL']), '<=')]
    T0 = data['T2'] + k1 * data['U_max'] / (1 - v)
    der = dict(v=v, R=R, M=c['M'], W1=W1, gamma=p['gam'], gamma_D=gD, nu=nu, eta_N=etaN, eta_D=etaD, zeta=zeta,
               eps_star=eps, delta0=delta0, U_A=UA, U_E=UE, D=D, X_star=Xs, G_f=Gf, z0max=z0max,
               sigma=sig, k_sigma=ksig, theta_f=thf, rho_star=rho_st, K_rot=Krot, omega0=om0, theta_h1=thh1,
               theta_h=thh, c_tau=ctau, theta0=th0, theta_y=thy, Theta0=Th0, omega_T=omT, omega_y=omy, x_c=xc, L_h=Lh,
               K_w=Kw, delta_tail=dt, k=k, Theta_b=Thb, Theta_p=Thp, c_n=cn, c_beta=cbeta, K_tail=Ktail, TS=TS,
               TS_rhs=p['s0'] * p['m'] * startfac, C0Ra=data['C0'] * R ** data['ap'], T0=T0, csepA=cA_sep,
               d=p['d'], dl1=p['dl1'], A0=A0, f=f, P7L=P7L, LJexp=LJexp, Xfar=tm['Xfar'],
               P5terms_main=(tm['T1'], tm['T2'], tm['T3']), P5terms_A=(tA['T1'], tA['T2'], tA['T3']),
               Pc_m2=p['m'] ** 2, Pc_r1=c['r1'])
    return C, der, (p, c, pA, cAA)


def ok_all(C, margin=0.0):
    for (n, l, r, k) in C:
        if isinstance(l, complex) or isinstance(r, complex):
            return False
        if k == '<=':
            if not l <= r - margin * abs(r): return False
        else:
            if not l < r - margin * abs(r): return False
    return True


# ----------------------------------------------------------------------------------------------------------------
# search (float)
NAMES = ['gam', 'm', 's0', 'k1', 'cA', 'KR', 'Kf', 'Ke', 'eta1', 'q', 'rfrac', 'ombar', 'kfac', 'dfrac']
sg = lambda x: 1 / (1 + math.exp(-x)) if x > -700 else 0.0


def theta(x, data, opts):
    th = {}
    th['gam'] = (float(data['ap']) - 1e-4) * sg(x[0])
    th['m'] = math.exp(x[1]); th['s0'] = sg(x[2]); th['k1'] = 1 + sg(x[3]) / 3; th['cA'] = sg(x[4])
    th['KR'] = 1 + (opts['KRmax'] - 1) * sg(x[5]); th['Kf'] = 3 + math.exp(x[6]); th['Ke'] = 1.5 + (opts['Kemax'] - 1.5) * sg(x[7])
    th['eta1'] = th['Kf'] / (th['Kf'] + 1) * sg(x[8]); th['q'] = 1 + math.exp(x[9]); th['rfrac'] = sg(x[10])
    th['ombar'] = 0.5 * sg(x[11]); th['kfac'] = 1 + math.exp(x[12]); th['dfrac'] = 0.5 * sg(x[13])
    # R: rfrac times the largest R allowed by (C1), (C4), (C6) of the main corollary (nu estimated at v = 6e-5)
    fac = 1.0
    if opts.get('capCTL') is not None:
        th['capCTL'] = opts['capCTL']
    th['R'] = th['rfrac'] * min(float(data['lam0']), float(data['c_sep']) / (th['cA'] * th['KR']),
                                (th['s0'] * th['m'] * fac / float(data['C0'])) ** (1 / float(data['ap'])), 1.0)
    return th


def unx(th, data, opts):
    lg = lambda y: math.log(y / (1 - y))
    return np.array([lg(th['gam'] / (float(data['ap']) - 1e-4)), math.log(th['m']), lg(th['s0']), lg(3 * (th['k1'] - 1)),
                     lg(th['cA']), lg((th['KR'] - 1) / (opts['KRmax'] - 1)), math.log(th['Kf'] - 3),
                     lg((th['Ke'] - 1.5) / (opts['Kemax'] - 1.5)), lg(th['eta1'] * (th['Kf'] + 1) / th['Kf']),
                     math.log(th['q'] - 1), lg(th['rfrac']), lg(th['ombar'] / 0.5), math.log(th['kfac'] - 1),
                     lg(th['dfrac'] / 0.5)])


def feasible(th, v, data):
    try:
        C, _, _ = build(th, v, data, FL, infl=1e-9)
        return ok_all(C, 1e-9)
    except (ValueError, ZeroDivisionError, OverflowError, TypeError):
        return False


def vmax(th, data, lo=-14.0, hi=None, it=40):
    if hi is None:
        hi = math.log10(float(data['v_T']))
    if feasible(th, 10 ** hi, data):
        return 10 ** hi
    if not feasible(th, 10 ** lo, data):
        return 0.0
    for _ in range(it):
        mid = (lo + hi) / 2
        if feasible(th, 10 ** mid, data): lo = mid
        else: hi = mid
    return 10 ** lo


def optimise(data, opts, start, seed=1, nrand=4, maxiter=6000, de=True, scale=0.7):
    from scipy.optimize import minimize, differential_evolution
    def obj(x):
        try:
            th = theta(x, data, opts)
        except (OverflowError, ValueError, ZeroDivisionError):
            return 50.0
        vv = vmax(th, data)
        return -math.log10(vv) if vv > 0 else 50.0
    rng = np.random.default_rng(seed)
    x0 = unx(start, data, opts)
    best = None
    for s in range(nrand + 1):
        xs = x0 if s == 0 else (best.x if best is not None else x0) + rng.normal(0, scale, size=len(x0))
        r = minimize(obj, xs, method='Nelder-Mead', options=dict(maxiter=maxiter, xatol=1e-7, fatol=1e-9, adaptive=True))
        r = minimize(obj, r.x, method='Nelder-Mead', options=dict(maxiter=maxiter, xatol=1e-8, fatol=1e-10, adaptive=True))
        print('   start %d: v = %.5e' % (s, 10 ** -r.fun), flush=True)
        if best is None or r.fun < best.fun:
            best = r
    if de:
        bounds = [(b - 3, b + 3) for b in best.x]
        r = differential_evolution(obj, bounds, seed=seed, maxiter=80, popsize=10, tol=1e-10, polish=False,
                                   init='latinhypercube', x0=best.x)
        r = minimize(obj, r.x, method='Nelder-Mead', options=dict(maxiter=maxiter, xatol=1e-9, fatol=1e-11, adaptive=True))
        print('   DE+NM: v = %.5e' % (10 ** -r.fun), flush=True)
        if r.fun < best.fun:
            best = r
    th = theta(best.x, data, opts)
    return th, vmax(th, data, it=60)


START = dict(gam=0.6156, m=0.06348, s0=0.05443, k1=1.0211, cA=0.9943, KR=31.9, Kf=5.05, Ke=999.0, eta1=0.8334, q=2.058,
             rfrac=0.98, ombar=0.4, kfac=1.3, dfrac=0.25)


def cmd_search(args):
    kv = dict(a.split('=') for a in args if '=' in a)
    eta = kv.get('eta', '0.1'); KRmax = float(kv.get('KRmax', 32)); vbar = kv.get('vbar', '1e-4')
    capCTL = kv.get('capCTL')
    opts = dict(KRmax=KRmax, Kemax=1e3, capCTL=None if capCTL is None else float(capCTL))
    data, cond, K = q3_data(vbar, eta, FL)
    bad = [k for k, ok in cond.items() if not ok]
    assert not bad, bad
    start = dict(START)
    if 'start' in kv:
        start = json.load(open(kv['start']))['theta']
    start['KR'] = min(start['KR'], 1 + 0.97 * (KRmax - 1))
    if capCTL is not None:
        start.update(m=0.015, rfrac=0.9)
    tag = 'eta%s_KR%g_vbar%s' % (eta, KRmax, vbar) + ('' if capCTL is None else '_capCTL%s' % capCTL)
    t0 = time.time()
    th, v = optimise(data, opts, start, nrand=int(kv.get('nrand', 3)), de=kv.get('de', '1') == '1',
                     scale=float(kv.get('scale', 0.7)))
    tag = kv.get('tag', tag)
    print('%s: v = %.6e (%.0fs)' % (tag, v, time.time() - t0), flush=True)
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    json.dump(dict(tag=tag, eta=eta, vbar=vbar, KRmax=KRmax, v=v, theta=th), open(os.path.join(HERE, 'out', 'search_%s.json' % tag), 'w'), indent=1)


# ----------------------------------------------------------------------------------------------------------------
# verification (mpmath, 50 digits)
MP = MpLib(50)


def mpf(x):
    return mpmath.mpf(x) if not isinstance(x, float) else mpmath.mpf(repr(x))


def rnd(x, sig, mode):
    """round mpf x to `sig` significant digits, up or down."""
    x = mpmath.mpf(x)
    if x == 0:
        return x
    e = int(mpmath.floor(mpmath.log10(abs(x)))) - sig + 1
    s = mpmath.mpf(10) ** e
    y = (mpmath.ceil(x / s) if mode == 'up' else mpmath.floor(x / s)) * s
    return mpmath.mpf(mpmath.nstr(y, sig + 2, strip_zeros=False)) if False else y


def table_conditions(C, out, title):
    res = check(C)
    allok = all(r[4] for r in res)
    out.append('-- %s: %d conditions, ALL HOLD: %s' % (title, len(res), allok))
    tight = []
    for name, lhs, rhs, kind, ok, sl in res:
        rel = sl / abs(rhs) if rhs != 0 else sl
        flag = '' if ok else '   <-- FAILS'
        if ok and rel < mpmath.mpf('1e-2'):
            flag = '   <-- within 1%'
            tight.append((name, rel))
        out.append('   %-62s %-18s %-2s %-18s rel.slack %s%s' % (name, mpmath.nstr(lhs, 12), kind, mpmath.nstr(rhs, 12),
                                                                 mpmath.nstr(rel, 3), flag))
    return allok, tight


def q3_block(vbar, eta, out):
    K, cond = q3_chain(vbar, eta)
    bad = [k for k, ok in cond.items() if not ok]
    out.append('-- Q3 touch-down side conditions (SC1)-(SC50) + (SC51) at vbar=%s, eta=%s, epsbar=1e-3: %d conditions, %s'
               % (vbar, eta, len(cond), 'ALL HOLD' if not bad else 'FAIL: ' + '; '.join(bad)))
    return not bad, K


def verify_point(th, v, vbar, eta, out, title, fixed=None):
    data, cond, K = q3_data(vbar, eta, MP)
    okq3, _ = q3_block(vbar, eta, out)
    C, der, (p, c, pA, cAA) = build(th, v, data, MP, fixed=fixed, infl=0 if fixed else mpmath.mpf('1e-30'))
    allok, tight = table_conditions(C, out, title)
    return allok and okq3, tight, data, der, p, c, pA, cAA, K


def binding_at(th, v, vbar, eta, fac=1.02):
    """conditions that fail when v (and vbar) are raised by the factor fac, all other parameters fixed."""
    data, _, _ = q3_data(vbar, eta, FL)
    C, _, _ = build(th, v * fac, dict(data, v_T=v * fac * 10), FL, infl=1e-12)
    return [n for (n, l, r, k) in C if not ((l <= r) if k == '<=' else (l < r))]


def cmd_verify(args):
    kv = dict(a.split('=') for a in args if '=' in a)
    od = os.path.join(HERE, 'out')
    runs = [json.load(open(os.path.join(od, f))) for f in sorted(os.listdir(od)) if f.startswith('search_')]
    out = ['SEARCH RESULTS (float search, vbar=1e-4 data for the search):']
    for r in sorted(runs, key=lambda r: -r['v']):
        out.append('   %-28s v = %.5e   gam=%.4f KR=%.3f Kf=%.3f R=%.3e m=%.4f' % (r['tag'], r['v'], r['theta']['gam'],
                   r['theta']['KR'], r['theta']['Kf'], r['theta']['R'], r['theta']['m']))
    pick = kv.get('pick')
    best = max(runs, key=lambda r: r['v']) if pick is None else [r for r in runs if r['tag'] == pick][0]
    th = best['theta']; eta = best['eta']
    # ---- 1. the optimum itself, vbar := v (rounded up to 3 digits), v := 0.999999 v* ----
    v_star = best['v']
    vbar1 = '%.3g' % (v_star * 1.001)
    data1, _, _ = q3_data(vbar1, eta, FL)
    v_opt = vmax(th, data1, it=60)      # re-optimised v for the Q3 data at vbar1 (data change by < 1e-6 relative)
    out.append('\n=== 1. OPTIMUM (%s): v_opt = %.6e with Q3 data at vbar = %s, eta = %s ===' % (best['tag'], v_opt, vbar1, eta))
    vv = mpf(v_opt) * (1 - mpmath.mpf('1e-6'))
    ok1, tight1, data, der, p, c, pA, cAA, K = verify_point(th, vv, vbar1, eta, out, 'all conditions at v = %s' % mpmath.nstr(vv, 8))
    out.append('   binding (fail at 1.02 v_opt): ' + '; '.join(binding_at(th, v_opt, vbar1, eta)))
    out.append('   eps_* = %s ; T0 = %s' % (mpmath.nstr(der['eps_star'], 6), mpmath.nstr(der['T0'], 8)))
    # ---- 2. SAFE ROUNDED values ----
    v0 = mpf(kv.get('v0', '%.1g' % (math.floor(v_opt / 10 ** math.floor(math.log10(v_opt))) * 10 ** math.floor(math.log10(v_opt)))))
    vbar0 = mpmath.nstr(v0, 6)
    thr = {k: rnd(mpf(th[k]), 6, 'down' if k in ('R',) else 'up') for k in th if k != 'rfrac'}
    thr['R'] = rnd(mpf(th['R']), 4, 'down')
    data0, _, _ = q3_data(vbar0, eta, MP)
    _, d0, _ = build(thr, v0, data0, MP, infl=mpmath.mpf('1e-7'))
    fixed = dict(d=rnd(d0['d'], 8, 'up'), dl1=rnd(d0['dl1'], 8, 'up'), nu=rnd(d0['nu'], 6, 'up'),
                 gD=rnd(d0['gamma_D'], 6, 'up'), A0=rnd(d0['A0'], 6, 'up'), f=rnd(d0['f'], 6, 'up'),
                 eps=rnd(d0['eps_star'], 1, 'down'), R=thr['R'])
    out.append('\n=== 2. SAFE ROUNDED VALUES: v0 = %s, vbar = v0, eta = %s; every condition re-verified at exactly these values ===' %
               (mpmath.nstr(v0, 6), eta))
    ok2, tight2, data, der, p, c, pA, cAA, K = verify_point(thr, v0, vbar0, eta, out, 'all conditions at the rounded values', fixed=fixed)
    T0r = mpmath.ceil(der['T0'] * 100) / 100
    out.append('   T0 = %s  -> rounded up T0 = %s ; eps_* = %s' % (mpmath.nstr(der['T0'], 10), mpmath.nstr(T0r, 6), mpmath.nstr(fixed['eps'], 3)))
    out.append('   (Pc) (only for End*(c), not used by Q2): m^2 = %s <= 1/2: %s ; r1 = %s > 0: %s' % (
        mpmath.nstr(der['Pc_m2'], 5), der['Pc_m2'] <= 0.5, mpmath.nstr(der['Pc_r1'], 5), der['Pc_r1'] > 0))
    # spot checks of monotonicity: smaller v, smaller eps
    for vs, es in ((v0 / 2, fixed['eps']), (v0 / 1000, fixed['eps'] / 1000)):
        fx = dict(fixed, eps=es)
        C, _, _ = build(thr, vs, data0, MP, fixed=fx)
        out.append('   spot check v = %s, eps = %s: all hold = %s' % (mpmath.nstr(vs, 3), mpmath.nstr(es, 3), ok_all(C)))
    # ---- 3. table ----
    out.append('\n=== 3. CONSTANTS AT THE ROUNDED VALUES ===')
    tab = constants_table(thr, fixed, der, p, c, pA, cAA, K, data, v0, eta, T0r)
    out += tab
    txt = '\n'.join(out)
    open(os.path.join(od, 'final.txt'), 'w', encoding='utf-8').write(txt + '\n')
    json.dump(dict(theta_rounded={k: str(x) for k, x in thr.items()}, fixed={k: str(x) for k, x in fixed.items()},
                   v0=str(v0), eta=eta, T0=str(T0r), ok=bool(ok2)), open(os.path.join(od, 'final.json'), 'w'), indent=1)
    print(txt)


def constants_table(th, fixed, der, p, c, pA, cAA, K, data, v0, eta, T0r):
    s = lambda x, n=6: mpmath.nstr(mpmath.mpf(x), n)
    rows = []
    R = lambda name, val, note='': rows.append('| %s | %s | %s |' % (name, val, note))
    rows.append('| constant | value | source / role |')
    rows.append('|---|---|---|')
    R('**v0**', s(v0), 'main theorem: every v <= v0')
    R('**eps_***', s(fixed['eps'], 3), 'min(eps_T, R/K_eps, (R/(100 c_zhi))^2), rounded down')
    R('**T0**', s(T0r, 6), 'T2 + kappa1 U_max/(1-v0), rounded up')
    rows.append('| *touch-down (Q3, Theorem Q.H, column vbar = v0, eta = %s, epsbar = 1e-3)* | | |' % eta)
    for nm, key, note in (('vbar = v_T', 'v', ''), ('eta (window)', 'eta', ''), ('x1', 'x1', ''), ('T2', 'T2', 't_td <= T2'),
                          ('U_max', 'U_max', '1 <= U <= U_max'), ('lambda0', 'lam0', '(T1) range'), ('c_sep', 'c_sep', '(T2)'),
                          ('kappa2', 'kap2', '(T2prime)'), ('c_N', 'c_N', '(T1prime) N <= c_N lam^{3/2-muT}'),
                          ('theta_v = K_fw', 'th_v', '(T3prime)'), ('c_T4 = K_tl', 'c_T4', '(T4prime)'),
                          ('z_T xe_hi = c_zhi', None, '(T5prime) z0 <= c_zhi eps^{1/2}'),
                          ('h_t xe_lo = c_zlo', None, '(T5prime) z0 >= c_zlo eps^{1/(2-2v)}'),
                          ('c_y', 'c_y', '(T5prime) |y0| <= c_y (z0+eps)^{2-muT}'), ('G_T = G', 'G', ''),
                          ('theta_T', 'theta_T', '(T3)-(T5), gamma_T = 1/4'), ('C_z', 'C_z', '(T5)'),
                          ('muT_bar', 'muT', '3 vbar/(1+vbar)')):
        if key is None:
            val = K['z_T'] * K['xe_hi'] if 'c_zhi' in nm else K['h_t'] * K['xe_lo']
        else:
            val = K[key] if key != 'eta' else mpmath.mpf(eta)
        R(nm, s(val), note)
    R("a' = 1 - muT_bar", s(data['ap'], 10), "largest admissible; C0 = c_N lam0^{1-muT-a'} = c_N")
    R('C0', s(data['C0']), '(T1*)')
    rows.append('| *core End* (Q1 final), main application: U = U_max, data (a\', C0, lam0, c_sep)* | | |')
    for k_ in ('gam', 'R', 'm', 's0', 'f', 'k1', 'cA', 'KR', 'Kf', 'Ke', 'eta', 'q', 'nu', 'd', 'dl1', 'A0'):
        R({'gam': 'gamma', 'k1': 'kappa1', 'cA': 'c_A', 'KR': 'K_R', 'Kf': 'K_f', 'Ke': 'K_eps', 'eta': 'eta (Q1, far forcing)',
           'dl1': 'delta1'}.get(k_, k_), s(p[k_], 7), 'free' if k_ not in ('f', 'nu', 'd', 'dl1', 'A0') else 'dependent (rounded up)')
    for k_ in ('M', 'chi', 'c6', 'CA', 'CB', 'CTL', 'C1A', 'crho', 'cR', 'camp', 'B2U', 'B2e', 'B3', 'Cp', 'B5', 'I5',
               'tauI', 'tau_al', 'tau_be', 'D_I', 'D_IIs', 'D_IIl'):
        R(k_, s(c[k_]), 'derived')
    R('C_TL m', s(c['CTL'] * p['m']), 'tilt at scale R (old cap 0.33 not needed)')
    R('X_far', s(der['Xfar']), '(P7)')
    R('L_J = e^(X_far+B5 I5 v m^2) + v k1 tauI', s(der['P7L'], 10), '< kappa1')
    R('P6 budget f^2 + 2v(D_I + max(D_IIs,D_IIl))', s(p['f'] ** 2 + 2 * p['v'] * (c['D_I'] + max(c['D_IIs'], c['D_IIl'])), 8), '< 1')
    rows.append('| *stage A (Cor. End* on [0,U_A], gamma -> gamma_D)* | | |')
    R('gamma_D', s(fixed['gD'], 7), 'gam + nu + eta_N rounded up')
    for k_ in ('CA', 'CB', 'CTL', 'D_IIs'):
        R(k_ + ' (stage A)', s(cAA[k_]), '')
    R('c_sep^A', s(der['csepA']), 'min(c_sep, kappa2(U_min-U_A))')
    rows.append('| *assembly (Q2.E\', Q2.H, Q2.D, Q2.M)* | | |')
    for k_ in ('W1', 'delta0', 'U_A', 'U_E', 'D', 'X_star', 'G_f', 'z0max', 'zeta', 'eta_N', 'sigma', 'rho_star', 'K_rot',
               'omega0', 'theta_h', 'theta0', 'theta_y', 'Theta0', 'omega_T', 'omega_y', 'K_w', 'delta_tail', 'k', 'Theta_b',
               'Theta_p', 'c_n', 'c_beta', 'K_tail', 'C0Ra', 'TS', 'TS_rhs'):
        R(k_, s(der[k_]), '')
    R('omega_bar', s(th['ombar']), 'free'); R('k_fac', s(th['kfac']), 'free'); R('delta0/R', s(th['dfrac']), 'free')
    return rows


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'search':
        cmd_search(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'verify':
        cmd_verify(sys.argv[2:])
