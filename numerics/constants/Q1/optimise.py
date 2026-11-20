"""
optimise.py -- maximise the admissible v of Corollary End* (referee/Q1-claims.md) for given data
(a', C0, lambda0, c_sep, U_max), over the free parameters
    gam, m, s0, kappa1, c_A, K_R, K_f, K_eps, eta, q
with the dependent choices (all optimal, since every side condition is monotone in them):
    d = 1/(1-v), delta1 = exp(2v/(1-v)), nu = c_amp*v, A0 = exp(LHS of P4), f = LHS of P5,
    R = min(1, lambda0, c_sep/(c_A K_R), (s0 m min(1,K_f/K_R)^nu / C0)^(1/a')).
Search: float arithmetic (Nelder-Mead multistart + differential evolution); the reported optimum is then
RE-VERIFIED in mpmath (50 digits) at v_rep = v*(1 - 1e-6), with every dependent quantity inflated by a relative 1e-30,
and every condition (P0)-(P7), (Pc), (C0)-(C6) printed with its slack.  Status of the output: NUMERICAL verification of
explicit inequalities (the inequalities themselves are PROVED to imply the theorem in Q1-claims.md).

Usage:  python optimise.py            (all data sets, writes out/*.txt)
        python optimise.py quick      (fewer restarts)
"""
import sys, os, math, time, json
import numpy as np
import mpmath
from scipy.optimize import minimize, differential_evolution
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from q1const import FloatLib, MpLib, derived, theorem_conditions, corollary_conditions, check

FL = FloatLib()
NAMES = ['gam', 'm', 's0', 'k1', 'cA', 'KR', 'Kf', 'Ke', 'eta', 'q']


def sig(x):
    return 1.0 / (1.0 + math.exp(-x)) if x > -700 else 0.0


def theta_from_x(x, D, opts):
    ap = D['ap']
    th = {}
    th['gam'] = min(ap, 0.999) * sig(x[0])
    th['m'] = math.exp(x[1])
    th['s0'] = sig(x[2])
    th['k1'] = 1 + sig(x[3]) / 3
    th['cA'] = sig(x[4])
    th['KR'] = 1 + (opts.get('KR_max', 32.0) - 1) * sig(x[5])
    th['Kf'] = 3 + math.exp(x[6])
    th['Ke'] = 1.5 + (opts['Ke_max'] - 1.5) * sig(x[7])
    th['eta'] = th['Kf'] / (th['Kf'] + 1) * sig(x[8])
    th['q'] = 1 + math.exp(x[9])
    return th


def x_from_theta(th, D, opts):
    lg = lambda y: math.log(y / (1 - y))
    ap = D['ap']
    return np.array([lg(th['gam'] / min(ap, 0.999)), math.log(th['m']), lg(th['s0']), lg(3 * (th['k1'] - 1)), lg(th['cA']),
                     lg((th['KR'] - 1) / (opts.get('KR_max', 32.0) - 1)), math.log(th['Kf'] - 3), lg((th['Ke'] - 1.5) / (opts['Ke_max'] - 1.5)),
                     lg(th['eta'] * (th['Kf'] + 1) / th['Kf']), math.log(th['q'] - 1)])


def build(th, v, D, opts, L=FL, infl=1e-8):
    """Assemble the full parameter dict for given free parameters th and v (backend L).  infl: relative inflation
    of the dependent quantities d, delta1, nu, A0, f (used in the mpmath verification to stay strictly inside)."""
    o = L.one
    p = {k: L.num(th[k]) * o for k in th}
    p['v'] = L.num(v) * o
    p['U'] = L.num(D['U']) * o
    up = 1 + L.num(infl) * o
    p['d'] = 1 / (1 - p['v']) * up
    p['dl1'] = L.exp(2 * p['v'] / (1 - p['v'])) * up
    p['R'] = o * 0.5           # placeholder, R does not enter c except via M, r1
    c = derived(p, L)
    p['nu'] = c['camp'] * p['v'] * up
    ap, C0, lam0, csep = (L.num(D[k]) * o for k in ('ap', 'C0', 'lam0', 'csep'))
    fac = (p['Kf'] / p['KR']) ** p['nu'] if p['Kf'] < p['KR'] else o
    Rc6 = (p['s0'] * p['m'] * fac / C0) ** (1 / ap)
    R = min(o, lam0, csep / (p['cA'] * p['KR']), Rc6)
    if opts.get('R_cap') is not None:
        R = min(R, L.num(opts['R_cap']) * o)
    p['R'] = R * (1 - L.num(infl) * o)       # stay strictly inside (C1),(C4),(C6)
    p['dtail'] = L.num(opts.get('delta_tail', 0.0)) * o
    c = derived(p, L)
    p['A0'] = L.exp(p['v'] * (2 * c['a1'] * p['d'] / (c['crho'] * p['Kf']) + c['a2'] * c['chi'] * p['U'] / (c['cR'] * p['R']))) * up
    p['f'] = p['s0']           # placeholder for computing T1..T3
    conds, terms = theorem_conditions(p, c, L, with_Pc=opts['with_Pc'])
    p['f'] = p['A0'] * (terms['T1'] + terms['T2'] + terms['T3']) * up
    return p, c


def all_conditions(p, c, D, opts, L=FL):
    conds, terms = theorem_conditions(p, c, L, with_Pc=opts['with_Pc'])
    Dm = {k: L.num(D[k]) * L.one for k in ('ap', 'C0', 'lam0', 'csep')}
    conds += corollary_conditions(p, c, Dm, L)
    if opts.get('cap_CTLm') is not None:
        conds.append(('cap C_TL*m', c['CTL'] * p['m'], L.num(opts['cap_CTLm']) * L.one, '<='))
    return conds, terms


def feasible(th, v, D, opts):
    try:
        p, c = build(th, v, D, opts)
        if c['crho'] <= 0 or c['cR'] <= 0 or p['R'] <= 0:
            return False
        conds, _ = all_conditions(p, c, D, opts)
        mg = 1e-9                       # relative safety margin in the float search (mpmath check then passes robustly)
        for name, lhs, rhs, kind in conds:
            if not lhs <= rhs - mg * abs(rhs):
                return False
        return True
    except (ValueError, ZeroDivisionError, OverflowError):
        return False


def vmax(th, D, opts, lo=-16.0, hi=-1.0, it=45):
    if not feasible(th, 10 ** lo, D, opts):
        return 0.0
    for _ in range(it):
        mid = (lo + hi) / 2
        if feasible(th, 10 ** mid, D, opts):
            lo = mid
        else:
            hi = mid
    return 10 ** lo


def objective(x, D, opts):
    try:
        th = theta_from_x(x, D, opts)
    except OverflowError:
        return 0.0
    v = vmax(th, D, opts)
    return -math.log10(v) if v > 0 else 50.0


DEFAULT_START = dict(gam=None, m=0.4, s0=0.35, k1=1.05, cA=0.97, KR=2.4, Kf=8.0, Ke=200.0, eta=0.5, q=2.3)


def optimise(D, opts, quick=False, seed=1):
    rng = np.random.default_rng(seed)
    best = None
    starts = []
    for gfrac in (0.97, 0.9, 0.7, 0.5):
        th = dict(DEFAULT_START)
        th['gam'] = gfrac * min(D['ap'], 0.999)
        th['Ke'] = min(th['Ke'], 0.8 * opts['Ke_max'])
        th['KR'] = min(th['KR'], 1 + 0.8 * (opts.get('KR_max', 32.0) - 1))
        if opts.get('cap_CTLm') is not None:
            th['m'] = 0.01
        starts.append(x_from_theta(th, D, opts))
    nrand = 2 if quick else 6
    for _ in range(nrand):
        starts.append(starts[0] + rng.normal(0, 1.0, size=10))
    for x0 in starts:
        r = minimize(objective, x0, args=(D, opts), method='Nelder-Mead',
                     options=dict(maxiter=3000 if quick else 8000, xatol=1e-7, fatol=1e-9, adaptive=True))
        r = minimize(objective, r.x, args=(D, opts), method='Nelder-Mead',
                     options=dict(maxiter=3000 if quick else 8000, xatol=1e-8, fatol=1e-10, adaptive=True))
        if best is None or r.fun < best.fun:
            best = r
    if not quick:
        bounds = [(b - 4, b + 4) for b in best.x]
        r = differential_evolution(objective, bounds, args=(D, opts), seed=seed, maxiter=150, popsize=12, tol=1e-10,
                                   polish=False, init='latinhypercube', x0=best.x)
        r = minimize(objective, r.x, args=(D, opts), method='Nelder-Mead',
                     options=dict(maxiter=8000, xatol=1e-9, fatol=1e-11, adaptive=True))
        if r.fun < best.fun:
            best = r
    th = theta_from_x(best.x, D, opts)
    return th, vmax(th, D, opts, it=60)


def verify(th, v, D, opts, dps=50):
    L = MpLib(dps)
    vr = mpmath.mpf(v) * (1 - mpmath.mpf('1e-6'))
    p, c = build(th, vr, D, opts, L=L, infl=mpmath.mpf('1e-30'))
    conds, terms = all_conditions(p, c, D, opts, L=L)
    res = check(conds)
    return p, c, res, terms


def old_range(D):
    """v0 of the published cor:End (gamma = min(a'/2,1/4)) and of rem:E-restart(1) (free gamma <= min(a',1/4))."""
    ap, C0, lam0, csep, U = D['ap'], D['C0'], D['lam0'], D['csep'], D['U']
    def R_of(g):
        return min(1, lam0 / 32, csep / 16, (g / (400 * C0)) ** (1 / ap))
    g = min(ap / 2, 0.25)
    v_pub = min(2e-11 * g * g, 1e-6 * g * R_of(g) / (4 * U + 2))
    best = 0
    for g in np.linspace(1e-4, min(ap, 0.25), 4000):
        vv = min(2e-11 * g * g, (ap - g) / 22, 1e-6 * g * R_of(g) / (4 * U + 2))
        best = max(best, vv)
    return v_pub, best


def fmt(x, n=6):
    return mpmath.nstr(x, n) if isinstance(x, mpmath.mpf) else ('%.*g' % (n, x))


def report(tag, D, opts, th, v, out):
    p, c, res, terms = verify(th, v, D, opts)
    allok = all(r[4] for r in res)
    v_pub, v_free = old_range(D)
    w = out.write
    w('=' * 100 + '\n')
    w('DATA %s: a\'=%s C0=%s lambda0=%s c_sep=%s U_max=%s   options=%s\n' % (tag, D['ap'], D['C0'], D['lam0'], D['csep'], D['U'],
                                                                         json.dumps(opts)))
    w('old v0 (published cor:End, gamma=min(a\'/2,1/4)) = %.3e ;  old v0 with free gamma (rem:E-restart(1)) = %.3e\n' % (v_pub, v_free))
    w('NEW v (verified in mpmath 50 digits at v*(1-1e-6)) = %s    ALL CONDITIONS HOLD: %s\n' % (fmt(p['v'], 8), allok))
    w('gain factor vs published: %.3g ; vs free-gamma: %.3g\n' % (float(p['v']) / v_pub, float(p['v']) / v_free))
    w('free parameters: ' + ', '.join('%s=%s' % (k, fmt(p[k], 8)) for k in NAMES) + '\n')
    w('dependent:  R=%s  M=m R^-gam=%s  nu=%s  d=%s  delta1=%s  A0=%s  f=%s\n' % tuple(fmt(p[k], 8) for k in
                                                                                    ('R', 'm', 'nu', 'd', 'dl1', 'A0', 'f')) )
    w('   (M = %s)\n' % fmt(c['M'], 8))
    w('tilt constants: C_A=%s C_B=%s C_TL=%s ; tilt at scale R: C_TL*m=%s (C_A*m=%s, C_B*m=%s)\n' % tuple(
        fmt(x, 6) for x in (c['CA'], c['CB'], c['CTL'], c['CTL'] * p['m'], c['CA'] * p['m'], c['CB'] * p['m'])))
    w('other: c6=%s c_rho=%s c_R=%s c_amp=%s chi=%s C1A=%s CmuA=%s Cp=%s B2U=%s B2e=%s B3=%s B5=%s I5=%s\n' % tuple(
        fmt(c[k], 6) for k in ('c6', 'crho', 'cR', 'camp', 'chi', 'C1A', 'CmuA', 'Cp', 'B2U', 'B2e', 'B3', 'B5', 'I5')))
    w('near: D_I=%s D_IIs=%s (alpha %s, beta %s, g=0 %s) D_IIl=%s ; tauI=%s tau_al=%s tau_be=%s\n' % tuple(
        fmt(c[k], 6) for k in ('D_I', 'D_IIs', 'D_IIs_al', 'D_IIs_be', 'D_IIs_0', 'D_IIl', 'tauI', 'tau_al', 'tau_be')))
    w('far (P5) terms (times A0): s0=%s forcing g>eta R: %s forcing g<=eta R: %s\n' % tuple(fmt(terms[k], 6) for k in ('T1', 'T2', 'T3')))
    if opts['with_Pc']:
        Kt = 16 * p['dl1'] + 2 * p['m'] ** 2 * (1 + 1 / p['gam']) + 2 * p['dl1'] * p['k1'] * p['U'] / c['r1']
        w('(c): r1=%s  c0=m^2/2=%s  Ktilde <= %s  (mu*Ktilde = %s; thm:R needs mu*K* < 1)\n' % (fmt(c['r1'], 6), fmt(p['m'] ** 2 / 2, 6), fmt(Kt, 6), fmt(Kt * p['v'] / (1 - p['v']), 4)))
    LJ = mpmath.exp(terms['Xfar'] + c['B5'] * c['I5'] * p['v'] * p['m'] ** 2) + p['v'] * p['k1'] * c['tauI']
    dtail = (p['k1'] - p['v'] * p['k1'] * c['tauI']) / mpmath.exp(terms['Xfar'] + c['B5'] * c['I5'] * p['v'] * p['m'] ** 2) - 1
    w('budgets: P6: f^2=%s  2vD_I=%s  2vD_IIs=%s (alpha %s beta %s g=0 %s)  2vD_IIl=%s  ; P7: exp-part-1=%s  v k1 tauI=%s  kappa1-1=%s\n' % tuple(
        fmt(x, 4) for x in (p['f'] ** 2, 2 * p['v'] * c['D_I'], 2 * p['v'] * c['D_IIs'], 2 * p['v'] * c['D_IIs_al'], 2 * p['v'] * c['D_IIs_be'],
                            2 * p['v'] * c['D_IIs_0'], 2 * p['v'] * c['D_IIl'],
                            mpmath.exp(terms['Xfar'] + c['B5'] * c['I5'] * p['v'] * p['m'] ** 2) - 1, p['v'] * p['k1'] * c['tauI'], p['k1'] - 1)))
    w('budgets: P5 (f = A0*(...)): A0=%s s0=%s far-forcing(g>etaR)=%s [U-part %s, eta-part %s] near-gap forcing=%s ; R limited by: C4 %s, C6 %s, C1 %s\n' % tuple(
        fmt(x, 4) for x in (p['A0'], terms['T1'], terms['T2'], terms['T2'] * c['B2U'] * c['chi'] * p['U'] / p['R'] / (c['B2U'] * c['chi'] * p['U'] / p['R'] + c['B2e']),
                            terms['T2'] * c['B2e'] / (c['B2U'] * c['chi'] * p['U'] / p['R'] + c['B2e']), terms['T3'],
                            mpmath.mpf(D['csep']) / (p['cA'] * p['KR']), (p['s0'] * p['m'] * ((p['Kf'] / p['KR']) ** p['nu'] if p['Kf'] < p['KR'] else 1) / mpmath.mpf(D['C0'])) ** (1 / mpmath.mpf(D['ap'])), mpmath.mpf(D['lam0']))))
    w('(J1) achieved: l <= L_J lambda with L_J = %s (< kappa1 = %s); admissible start stretch delta_tail (P7_delta) < %s\n' % (
        fmt(LJ, 8), fmt(p['k1'], 8), fmt(dtail, 6)))
    w('legs: advance >= eps/kappa1, #legs <= kappa1 U/eps, T_stop - t_s <= kappa1 U/(1-v) = %s ; eps <= R/K_eps = %s\n' % (
        fmt(p['k1'] * p['U'] / (1 - p['v']), 6), fmt(p['R'] / p['Ke'], 6)))
    w('conditions (name, lhs, rhs, relative slack (rhs-lhs)/|rhs|):\n')
    binding = []
    for name, lhs, rhs, kind, ok, sl in res:
        rel = sl / abs(rhs) if rhs != 0 else sl
        flag = '' if ok else '   <-- FAILS'
        if ok and rel < mpmath.mpf('1e-3'):
            if name.split()[0] in ('P1', 'P3', 'P4', 'P5'):
                flag = '   <-- tight by construction (dependent quantity set equal)'
            else:
                flag = '   <-- binding'
                binding.append(name)
        w('   %-24s %-16s %s %-16s  %s%s\n' % (name, fmt(lhs, 10), kind, fmt(rhs, 10), fmt(rel, 3), flag))
    w('BINDING: %s\n' % ', '.join(binding))
    out.flush()
    return dict(tag=tag, v=float(p['v']), ok=allok, binding=binding, R=float(p['R']), m=float(p['m']), M=float(c['M']),
                gam=float(p['gam']), CTL=float(c['CTL']), CTLm=float(c['CTL'] * p['m']), v_pub=v_pub, v_free=v_free)


DATA = {
    'round6 a=1/2':        dict(ap=0.5, C0=0.86, lam0=1 / 40, csep=0.024, U=6.5),
    'round6 a=0.99':       dict(ap=0.99, C0=5.21, lam0=1 / 40, csep=0.024, U=6.5),
    'Q3 a=1/2 (C0=0.70)':  dict(ap=0.5, C0=0.70, lam0=1 / 40, csep=0.024, U=6.5),
    'Q3 a=0.99 (C0=4.25)': dict(ap=0.99, C0=4.25, lam0=1 / 40, csep=0.024, U=6.5),
}


def make_runs():
    runs = []
    for tag, D in DATA.items():
        runs.append((tag, D, dict(with_Pc=True, Ke_max=1e3, cap_CTLm=None)))
    for tag in ('round6 a=1/2', 'round6 a=0.99'):
        runs.append((tag + ' [no (Pc)]', DATA[tag], dict(with_Pc=False, Ke_max=1e3, cap_CTLm=None)))
        runs.append((tag + ' [cap C_TL m<=0.33]', DATA[tag], dict(with_Pc=True, Ke_max=1e3, cap_CTLm=0.33)))
        runs.append((tag + ' [K_eps<=64]', DATA[tag], dict(with_Pc=True, Ke_max=64.0, cap_CTLm=None)))
    for tag in ('Q3 a=1/2 (C0=0.70)', 'Q3 a=0.99 (C0=4.25)'):
        runs.append((tag + ' [Q2: delta_tail=2e-5, no (Pc)]', DATA[tag], dict(with_Pc=False, Ke_max=1e3, cap_CTLm=None, delta_tail=2e-5)))
        runs.append((tag + ' [Q2: delta_tail=2e-5, cap C_TL m<=0.33]', DATA[tag], dict(with_Pc=True, Ke_max=1e3, cap_CTLm=0.33, delta_tail=2e-5)))
    runs.append(('round6 a=1/2 [K_R uncapped]', DATA['round6 a=1/2'], dict(with_Pc=True, Ke_max=1e3, cap_CTLm=None, KR_max=1e6)))
    # Q3 family: N <= 4.4 lam^{3/2-3v_T}: C0(a') = 4.4 lam0^{1-3e-6-a'}; scan a'
    for ap in (0.3, 0.5, 0.7, 0.9, 0.99):
        D = dict(ap=ap, C0=4.4 * (1 / 40) ** (1 - 3e-6 - ap), lam0=1 / 40, csep=0.024, U=6.5)
        runs.append(('Q3 family a=%g' % ap, D, dict(with_Pc=True, Ke_max=1e3, cap_CTLm=None)))
    # sensitivity to separation data
    for lam0, csep in ((0.05, 0.05), (0.1, 0.1)):
        D = dict(ap=0.5, C0=0.70, lam0=lam0, csep=csep, U=6.5)
        runs.append(('sens a=1/2 C0=0.70 lam0=%g csep=%g' % (lam0, csep), D, dict(with_Pc=True, Ke_max=1e3, cap_CTLm=None)))
    return runs


def main():
    quick = 'quick' in sys.argv
    od = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
    os.makedirs(od, exist_ok=True)
    summary = []
    runs = make_runs()
    sel =[a for a in sys.argv[1:] if a.startswith('idx=')]
    if 'merge' in sys.argv:
        fn = os.path.join(od, 'optimise.txt')
        with open(fn, 'w', encoding='utf-8') as out:
            for k in range(len(runs)):
                rf = os.path.join(od, 'run_%02d.txt' % k)
                if os.path.exists(rf):
                    out.write(open(rf, encoding='utf-8').read())
                    summary.append(json.load(open(os.path.join(od, 'run_%02d.json' % k))))
            write_summary(out, summary)
        print('written', fn)
        return
    if sel:
        k = int(sel[0][4:])
        tag, D, opts = runs[k]
        t0 = time.time()
        with open(os.path.join(od, 'run_%02d.txt' % k), 'w', encoding='utf-8') as out:
            th, v = optimise(D, opts, quick=quick)
            s = report(tag, D, opts, th, v, out)
        s['time'] = time.time() - t0
        s['theta'] = th
        json.dump(s, open(os.path.join(od, 'run_%02d.json' % k), 'w'), indent=1)
        print('%-45s v=%.4e ok=%s binding=%s (%.0fs)' % (tag, s['v'], s['ok'], s['binding'], s['time']), flush=True)
        return
    fn = os.path.join(od, 'optimise_quick.txt' if quick else 'optimise.txt')
    with open(fn, 'w', encoding='utf-8') as out:
        for tag, D, opts in runs:
            t0 = time.time()
            th, v = optimise(D, opts, quick=quick)
            s = report(tag, D, opts, th, v, out)
            s['time'] = time.time() - t0
            summary.append(s)
            print('%-45s v=%.4e ok=%s binding=%s (%.0fs)' % (tag, s['v'], s['ok'], s['binding'], s['time']), flush=True)
        write_summary(out, summary)
    print('written', fn)


def write_summary(out, summary):
    if True:
        out.write('\nSUMMARY\n')
        for s in summary:
            out.write('%-45s v_new=%.4e  v_pub=%.3e  v_freegamma=%.3e  gain=%.3g  R=%.4g m=%.4g gam=%.4g C_TL*m=%.4g  binding=%s\n' % (
                s['tag'], s['v'], s['v_pub'], s['v_free'], s['v'] / s['v_pub'], s['R'], s['m'], s['gam'], s['CTLm'],
                ','.join(s['binding'])))


if __name__ == '__main__':
    main()








