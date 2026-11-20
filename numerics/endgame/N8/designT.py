"""N8: design T ("run through, tangent chase, walk round") at depth.  NUMERICAL; the state at the merge is EXACT.

  1. Harry runs straight along +x from the centre for time t1 = 1/(1-v) + D1 (through the front; exact front, front.py).
  2. He turns and runs straight at the candidate alpha0 = arccos(v + 1/t1): this is the silhouette point of the front seen
     from Harry (bearing extremum), so the run is TANGENT to the front at the meeting point X0 (C has a double zero there,
     and C is conserved).  Exact by the same two integrals.  Candidates alpha in (b_e, alpha0) are seen during this run
     (closest approach C2/g_max <= eps); the front on the apex side of b_e is left behind tangentially.
  3. Construction C (legs) on increasing labels from alpha0 all the way round, across the seen hole |alpha| < alpha_s at
     the apex, into the last-met end Y1 = label b_e (+ 2 pi).
The whole unseen front is one E-centred chain (E = Y1), geometric near E and near the hole, uniform (label step H) in the
bulk; legs go from node to node (= step H in the bulk, 2 % of the remaining length near E), true eps-legs for L < 64 eps.
Usage: python designT.py v eps [D1=0.1 H=0.002 g=1.02 dps=60 rec=1 tag=]"""
import sys, os, math, time, json
import numpy as np, mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'N7'))
import n7, inward, front as fr


NFALL = [0]


def solve_gamma_mp(R, v, guess):
    """gamma = pi - beta with (cos beta + v)/g(beta) = R.  For R >> 1 (beta -> 0) solve in log(beta) instead."""
    if R > 2:
        fb = lambda lb: (mp.cos(mp.e ** lb) + v) * mp.tan(mp.e ** lb / 2) ** v / mp.sin(mp.e ** lb) - R
        lb0 = mp.log(((1 + v) / (2 ** v * R)) ** (1 / (1 - v)))
        lb = mp.findroot(fb, lb0, tol=mp.mpf(10) ** (-mp.mp.dps + 8))
        return mp.pi - mp.e ** lb
    f = lambda lg: (v - mp.cos(mp.e ** lg)) / (mp.sin(mp.e ** lg) * mp.tan(mp.e ** lg / 2) ** v) - R
    try:
        lg = mp.findroot(f, mp.mpf(guess), tol=mp.mpf(10) ** (-mp.mp.dps + 8))
    except Exception:
        NFALL[0] += 1
        lo, hi = mp.mpf(-900), mp.log(mp.pi) - mp.mpf(10) ** (-30)
        for _ in range(4 * mp.mp.dps):
            mid = (lo + hi) / 2
            if f(mid) < 0: lo = mid
            else: hi = mid
        lg = (lo + hi) / 2
    return mp.e ** lg


def state_at_merge_mp(alpha, vs, t1, uT, tau2, guess1, guess2):
    """exact position (complex; frame: x along the tangent run, origin = Harry at the merge) of candidate alpha (mpf)."""
    v = mp.mpf(vs)
    a = alpha if alpha <= mp.pi else 2 * mp.pi - alpha
    ga = mp.sin(a) / mp.tan(a / 2) ** v
    gam = solve_gamma_mp((mp.cos(a) + v - (1 - v * v) * t1) / ga, v, guess1)
    rho = ga / (mp.sin(gam) * mp.tan(gam / 2) ** v)
    z = mp.mpc(-rho * mp.cos(gam), rho * mp.sin(gam))
    if alpha > mp.pi: z = mp.conj(z)
    w = z / uT                                   # position relative to Harry at t1 in the frame of the second run
    r = abs(w); b = mp.arg(w); sg = 1 if b >= 0 else -1; b = abs(b)
    if b == 0: return mp.mpc(r - (1 - v) * tau2, 0)
    C2 = r * mp.sin(b) / mp.tan(b / 2) ** v; h2 = r * (mp.cos(b) + v) - (1 - v * v) * tau2
    gam2 = solve_gamma_mp(h2 / C2, v, guess2)
    b2 = mp.pi - gam2
    rho2 = C2 * mp.tan(b2 / 2) ** v / mp.sin(b2)
    return mp.mpc(rho2 * mp.cos(b2), sg * rho2 * mp.sin(b2))


def state_at_merge_dbl(alpha, v, t1, uT, tau2, mirror=False):
    x, y, rho, gam = fr.front(alpha, v, t1)
    if mirror: y = -y                              # candidate with label 2 pi - alpha
    w = (x + 1j * y) / uT
    r = np.abs(w); b = np.angle(w); sg = np.where(b >= 0, 1.0, -1.0); b = np.maximum(np.abs(b), 1e-300)
    C2 = r * np.sin(b) / np.tan(b / 2) ** v; h2 = r * (np.cos(b) + v) - (1 - v * v) * tau2
    R = h2 / C2
    lo = np.full_like(r, -700.0); hi = np.full_like(r, math.log(math.pi) - 1e-15)
    for _ in range(200):
        mid = 0.5 * (lo + hi); up = fr.Ffun(mid, v) < R
        lo = np.where(up, mid, lo); hi = np.where(up, hi, mid)
    lg2 = 0.5 * (lo + hi); g2 = np.exp(lg2)
    rho2 = C2 / (np.sin(g2) * np.tan(g2 / 2) ** v)
    return -rho2 * np.cos(g2) + 1j * sg * rho2 * np.sin(g2), np.log(gam), lg2


def setup(vs, eps, D1=0.1, H=0.002, g=1.02, dps=60, verbose=True, fine_start=1):
    mp.mp.dps = dps
    v = float(vs); vm = mp.mpf(vs); t1 = 1 / (1 - vm) + mp.mpf(D1); t1f = float(t1)
    a0 = mp.acos(vm + 1 / t1)
    z0 = fr.front_mp(a0, vs, t1); rho0 = abs(z0); uT = z0 / rho0; tau2 = rho0 / (1 - vm)
    uTf = complex(uT); tau2f = float(tau2); gm = fr.gmax(v)

    # end of the seen strip: C2(alpha0 - Delta) = eps g_max  (closest approach during the tangent run = eps)
    def C2(Delta):
        w = fr.front_mp(a0 - Delta, vs, t1) / uT; b = abs(mp.arg(w)); r = abs(w)
        return r * mp.sin(b) / mp.tan(b / 2) ** vm
    lo, hi = mp.log(mp.mpf(10) ** (-150)), mp.log(a0 / 4)
    for _ in range(140):
        mid = (lo + hi) / 2
        if C2(mp.e ** mid) < eps * gm: lo = mid
        else: hi = mid
    De = mp.e ** ((lo + hi) / 2); ae = a0 - De
    a_s = fr.alpha_seen(v, eps)
    d = [eps / 100.0]
    while d[-1] * (g - 1) < H: d.append(d[-1] * g)
    aeF = float(ae)
    near = [ae - mp.mpf(x) for x in d]; near_d = d
    lastn = aeF - d[-1]
    hole = [max(a_s, 1e-12)]      # (double precision cannot resolve the hole itself at depth: the leg across it then also skips
                                  #  the unseen labels alpha_s < |alpha| < 1e-12; the hole is treated exactly in touch.py)
    while hole[-1] * 0.1 < H and hole[-1] * 1.1 < 0.5 * lastn: hole.append(hole[-1] * 1.1)
    nu = max(1, int(round((lastn - hole[-1]) / H)))
    uni = list(np.linspace(lastn, hole[-1], nu + 1)[1:-1])
    upper = [float(x) for x in uni] + hole[::-1]                  # decreasing labels, ends at alpha_s
    # lower side: parametrised by a' = 2 pi - label (so that tiny labels next to the hole keep full precision)
    a0f = float(a0)
    nl = int(round((2 * math.pi - a0f - hole[-1]) / H))
    lower = hole + list(np.linspace(hole[-1], 2 * math.pi - a0f, nl + 1)[1:-1])        # a' increasing: from the hole edge round to X0
    ahead = []
    if fine_start:                                 # geometric nodes just ahead of X0 (first legs of C short, as eps-legs are)
        dd = [float(De) * 1e-4]
        while dd[-1] * (g - 1) < H: dd.append(dd[-1] * g)
        ahead = dd[::-1]                           # label offsets alpha0 + d, decreasing d (towards X0)
        lower = [x for x in lower if x < 2 * math.pi - a0f - dd[-1] - 0.5 * H]
    zu, lg1, lg2 = state_at_merge_dbl(np.array(upper), v, t1f, uTf, tau2f)
    zl, _, _ = state_at_merge_dbl(np.array(lower), v, t1f, uTf, tau2f, mirror=True)
    zf = np.concatenate([zu, zl]); far = np.array(upper + [2 * math.pi - x for x in lower])
    zE_d, lg1E, lg2E = state_at_merge_dbl(np.array([aeF]), v, t1f, uTf, tau2f)
    zE = state_at_merge_mp(ae, vs, t1, uT, tau2, lg1E[0], lg2E[0])
    Y = [(0.0, 0.0)]
    for a in near:
        z = state_at_merge_mp(a, vs, t1, uT, tau2, lg1E[0], lg2E[0]) - zE
        Y.append((float(z.real), float(z.imag)))
    zEc = complex(zE)
    Yf = zf - zEc
    Ya = []
    if ahead:
        z0d, lg1X, lg2X = state_at_merge_dbl(a0f + np.array(ahead), v, t1f, uTf, tau2f)
    for i, dlt in enumerate(ahead):                # exact (mp) positions of the nodes just ahead of X0
        z = state_at_merge_mp(a0 + mp.mpf(dlt), vs, t1, uT, tau2, lg1X[i], lg2X[i]) - zE
        Ya.append((float(z.real), float(z.imag)))
    Y = np.array(Y + [(q.real, q.imag) for q in Yf] + Ya + [(-zEc.real, -zEc.imag)])
    labels = np.concatenate([[aeF], [float(a) for a in near], far, [a0f + x for x in ahead], [a0f]])
    arm = n7.Arm(v, eps, Y, np.array([-zEc.real, -zEc.imag]))
    arm.p[:] = arm.Y[arm.n - 1]
    info = dict(t1=t1f, alpha0=a0f, Delta_e=float(De), alpha_s=a_s, tau2=tau2f, rho0=float(rho0), n=arm.n, n_near=len(near),
                labels=labels, zE=zEc)
    if verbose:
        print(f"# v={vs} eps={eps:g} D1={D1}: t1={t1f:.5f} alpha0={a0f:.6f} Delta_e={float(De):.3e} alpha_s={a_s:.3e} "
              f"chase length {float(rho0):.4f} time {tau2f:.4f}; nodes {arm.n} ({len(near)} near E); E - X0 = {zEc:.4e}; "
              f"lateral offset of E from Harry's line / eps = {abs(zEc.imag)/eps:.3f}", flush=True)
    return arm, info


def profile(arm, n_use, eps):
    """deviation profile of the end E: tilt of the tangent (relative to the tangent at E) against tip distance."""
    X = arm.Y[:n_use]; d = np.diff(X, axis=0); ds = np.hypot(d[:, 0], d[:, 1]); s = np.cumsum(ds) - 0.5 * ds
    psi = np.unwrap(np.arctan2(d[:, 1], d[:, 0])); dev = psi - psi[0]
    out = []
    for k in np.arange(math.floor(math.log10(eps)) + 1, 0):
        i = int(np.searchsorted(s, 10.0 ** k)); j = int(np.searchsorted(s, 3 * 10.0 ** k))
        if i < 3 or j >= len(s) - 1 or dev[i] == 0 or dev[j] == 0: continue
        out.append((s[i], dev[i], math.log(abs(dev[j] / dev[i])) / math.log(s[j] / s[i])))
    return out, psi[0]


def main():
    vs = sys.argv[1]; eps = float(sys.argv[2])
    o = inward.parse([]); o.update(hull=0, skip0=1, rec=1)
    kw = dict(D1=0.1, H=0.002, g=1.02, dps=60, fine_start=1); tag = ''
    for a in sys.argv[3:]:
        k, x = a.split('=')
        if k in kw: kw[k] = type(kw[k])(x)
        elif k == 'tag': tag = x
        else: o[k] = type(o[k])(x)
    v = float(vs); t0 = time.time()
    arm, info = setup(vs, eps, **kw)
    prof, psiE = profile(arm, 1 + info['n_near'], eps)
    print(f"# end Y1 right after the merge (tangent at Y1 makes {abs(abs(psiE) - math.pi):.3e} rad with Harry's line): tip distance, tilt, local exponent a'")
    for q in prof[::max(1, len(prof) // 12)]: print(f"#   r={q[0]:.1e} tilt={q[1]:+.3e} a'={q[2]:.4f}")
    rows, profs, summ = inward.walk_in(arm, o, rec_prof=[])
    c = {k: i for i, k in enumerate(inward.COLS)}
    Ttot = info['t1'] + info['tau2'] + summ['T']
    L = rows[:, c['L']]; D = rows[:, c['D']]; hd = np.unwrap(rows[:, c['heading']])
    res = dict(v=v, eps=eps, **{k: info[k] for k in ('t1', 'alpha0', 'Delta_e', 'alpha_s', 'tau2', 'n')}, T_walk=summ['T'], T_total=Ttot,
               legs=summ['legs'], seen_ok=summ['seen_ok'], secs=round(time.time() - t0))
    fin = (L < 0.2) & (L > 16 * eps)
    res.update(final_supQ=float(rows[fin, c['Q']].max()), final_sup_bE=float(np.abs(rows[fin, c['bE']]).max()),
               final_sup_B=float(rows[fin, c['B']].max()), final_sup_K=float(rows[fin, c['K']].max()),
               final_sup_time_over_L=float((rows[fin, c['tgo']] / L[fin]).max()))
    # hole crossing: the connector is the longest step among the legs near the hole
    st = rows[:, c['step']]; dh = np.abs(np.diff(hd))
    res.update(max_heading_jump=float(dh.max()), L_at_max_jump=float(L[int(np.argmax(dh))]))
    print(json.dumps(res))
    print("# final approach into Y1 per decade of D: |bearing of Y1|, sector B, K~, sup|Q| (remaining arc), winding rate, T/L, local exponent of the bearing in D")
    k = 0; prev = None
    while 10.0 ** (-k - 1) > 30 * eps and k < 140:
        w = (D < 10.0 ** (-k)) & (D > 10.0 ** (-k - 1)) & (L < 0.3)
        if w.sum() > 2:
            b = float(np.mean(np.abs(rows[w, c['bE']]))); q = np.polyfit(-np.log(D[w]), hd[w], 1)[0]
            ex = math.log10(prev / b) if prev and b > 0 else float('nan')
            if k < 8 or k % 3 == 0:
                print(f"D in 1e-{k+1}..1e-{k}: bE={b:.3e} B={rows[w, c['B']].max():.3e} K={rows[w, c['K']].mean():.3e} supQ={rows[w, c['Q']].max():.3e} "
                      f"q={q:+.2e} T/L={(rows[w, c['tgo']] / L[w]).mean():.5f} exponent={ex:.3f}")
            prev = b
        k += 1
    tag = tag or f"T_v{vs}_e{eps:g}_D{kw['D1']}"
    np.savez(os.path.join(HERE, 'out', tag + '.npz'), rows=rows, cols=np.array(inward.COLS), summary=json.dumps(res),
             labels=info['labels'], prof=np.array(prof))


if __name__ == '__main__':
    main()
