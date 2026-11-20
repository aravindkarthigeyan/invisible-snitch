"""N8: design T at the touch-down time t_2 (exact state): the quantities of hypothesis (ST_end) of P7.
 (i)   (E1): sup over pairs of the remaining arc of N / lambda^{1/2+a'},  N = sqrt(2E), E = arc - chord, for
       eps/2 <= lambda <= lambda0, a' in {1, 1/2, 1/4, 0.1}; separately for the forward arc next to X0 (Harry-centred, exact),
       for the neighbourhood of the end E_Y left behind, for the hole edges and for the bulk;
 (ii)  the end E_Y: position, tilt profile;  (iii) (E2): separation (min chord for pairs with lambda > lambda0).
Usage: python touch.py v eps [D1=0.1]"""
import sys, os, math, json
import numpy as np, mpmath as mp
from numpy.lib.stride_tricks import sliding_window_view
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'N7'))
import designT, front as fr

APS = (1.0, 0.5, 0.25, 0.1)


def pair_stats(X, lam_min, lam_max, ms=None):
    """For the polyline X: pairs (i, i+m), m = 1, 2, 4, ...; returns arrays lambda (= arc length of the pair), N."""
    d = np.diff(X, axis=0); ds = np.hypot(d[:, 0], d[:, 1]); psi = np.unwrap(np.arctan2(d[:, 1], d[:, 0]))
    n = len(ds); lam = []; Nn = []; pos = []
    cs = np.concatenate([[0.0], np.cumsum(ds)])
    m = 2
    while m <= n:
        wp = sliding_window_view(psi, m); wd = sliding_window_view(ds, m)
        l = wd.sum(1)
        rel = wp - wp[:, :1]
        mean = (wd * rel).sum(1) / l
        Ev = 0.5 * (wd * (rel - mean[:, None]) ** 2).sum(1)          # small-angle form (no cancellation)
        c = np.hypot(*(X[m:] - X[:-m]).T)
        Ee = l - c
        E = np.where(Ee > 1e-9 * l, Ee, Ev)
        ok = (l >= lam_min) & (l <= lam_max)
        lam.append(l[ok]); Nn.append(np.sqrt(2 * np.maximum(E[ok], 0))); pos.append(cs[:-m][ok])
        m = max(m + 1, int(m * 1.5))
    return np.concatenate(lam), np.concatenate(Nn), np.concatenate(pos)


def sup_table(name, lam, N):
    out = []
    for a in APS:
        r = N / lam ** (0.5 + a)
        k = int(np.argmax(r)); out.append(f"a'={a}: C0={r[k]:.3g} (at lambda={lam[k]:.1e})")
    print(f"  {name:38s} " + "; ".join(out))
    return [float((N / lam ** (0.5 + a)).max()) for a in APS]


def forward_arc(vs, eps, D1, g=1.02, dps=80, lmax=0.3):
    mp.mp.dps = dps
    v = float(vs); vm = mp.mpf(vs); t1 = 1 / (1 - vm) + mp.mpf(D1)
    a0 = mp.acos(vm + 1 / t1); z0 = fr.front_mp(a0, vs, t1); rho0 = abs(z0); uT = z0 / rho0; tau2 = rho0 / (1 - vm)
    dd = [eps / 8]
    while dd[-1] < lmax: dd.append(dd[-1] * g)
    zd, l1, l2 = designT.state_at_merge_dbl(float(a0) + np.array(dd), v, float(t1), complex(uT), float(tau2))
    X = [(0.0, 0.0)]
    for i, d in enumerate(dd):
        z = designT.state_at_merge_mp(a0 + mp.mpf(d), vs, t1, uT, tau2, l1[i], l2[i])
        X.append((float(z.real), float(z.imag)))
    return np.array(X)


if __name__ == '__main__':
    vs = sys.argv[1]; eps = float(sys.argv[2]); D1 = 0.1
    for a in sys.argv[3:]:
        k, x = a.split('='); D1 = float(x) if k == 'D1' else D1
    v = float(vs); lam0 = 0.1
    print(f"design T, touch-down state, v={vs} eps={eps:g} D1={D1}; lambda0={lam0}; N <= C0 lambda^(1/2+a') : smallest admissible C0")
    # forward arc (Harry-centred)
    XF = forward_arc(vs, eps, D1)
    lam, N, pos = pair_stats(XF, eps / 2, lam0)
    r1 = sup_table("forward arc next to X0", lam, N)
    d = np.diff(XF, axis=0); psi = np.arctan2(d[:, 1], d[:, 0]); s = np.cumsum(np.hypot(*d.T))
    ex = []
    for r in (1e3 * eps, 1e-8, 1e-5, 1e-3, 1e-2):
        if r < 30 * eps: continue
        i = np.searchsorted(s, r); j = np.searchsorted(s, 3 * r)
        ex.append(f"s={r:.0e}: tilt {psi[i]:+.2e}, a'={math.log(abs(psi[j]/psi[i]))/math.log(s[j]/s[i]):.4f}")
    print("     tilt of the forward arc against Harry's heading: " + "; ".join(ex) + f"   [(1-2v)/(1-v) = {(1-2*v)/(1-v):.4f}]")
    # whole chain (E-centred): near E_Y, hole, bulk
    arm, info = designT.setup(vs, eps, D1=D1, dps=80, verbose=False)
    X = arm.Y[:arm.n]; nn = info['n_near']
    zE = info['zE']
    print(f"  end E_Y: |E_Y - X0| = {abs(zE):.3e} = {abs(zE)/eps:.3e} eps = {abs(zE)/math.sqrt(eps):.3e} sqrt(eps) "
          f"= eps^{math.log(abs(zE))/math.log(eps):.4f}; lateral offset from Harry's line {abs(zE.imag)/eps:.3f} eps  [1/(2-2v) = {1/(2-2*v):.4f}]")
    lamE, NE, posE = pair_stats(X[:nn + 40], eps / 2, lam0)
    r2 = sup_table("neighbourhood of the end E_Y", lamE, NE)
    lab = info['labels']
    iu = int(np.argmin(np.abs(lab - info['alpha_s'])))
    # the hole, exactly (mp), centred at its upper edge: labels +-alpha_s g^k on both sides, straight gap in between
    mp.mp.dps = 80
    vm = mp.mpf(vs); t1 = 1 / (1 - vm) + mp.mpf(D1); a0 = mp.acos(vm + 1 / t1); z0 = fr.front_mp(a0, vs, t1); rho0 = abs(z0)
    uT = z0 / rho0; tau2 = rho0 / (1 - vm)
    hl = [info['alpha_s']]
    while hl[-1] < 0.05: hl.append(hl[-1] * 1.05)
    zd, l1, l2 = designT.state_at_merge_dbl(np.array(hl), v, float(t1), complex(uT), float(tau2))
    zu = [designT.state_at_merge_mp(mp.mpf(a), vs, t1, uT, tau2, l1[i], l2[i]) for i, a in enumerate(hl)]
    zdm, l1m, l2m = designT.state_at_merge_dbl(np.array(hl), v, float(t1), complex(uT), float(tau2), mirror=True)
    zl = [designT.state_at_merge_mp(2 * mp.pi - mp.mpf(a), vs, t1, uT, tau2, l1m[i], l2m[i]) for i, a in enumerate(hl)]
    ref = zu[0]
    XH = np.array([(float((z - ref).real), float((z - ref).imag)) for z in zu[::-1] + zl])
    lamH, NH, posH = pair_stats(XH, eps / 2, lam0)
    r3 = sup_table("across the hole (cut: straight gap)", lamH, NH)
    gapw = float(abs(zl[0] - zu[0]))
    dH = np.diff(XH, axis=0); psH = np.unwrap(np.arctan2(dH[:, 1], dH[:, 0])); k0 = len(zu) - 1
    print(f"     hole: width {gapw:.3e} = {gapw/eps:.3g} eps = eps^{math.log(gapw)/math.log(eps):.4f} [1/(1+v) = {1/(1+v):.4f}]; "
          f"tangent turn across the gap: edge-to-edge chord vs upper edge tangent {psH[k0]-psH[k0-1]:+.2e}, vs lower {psH[k0+1]-psH[k0]:+.2e} rad")
    # bulk: both sides of the hole separately (the chain cannot resolve the hole itself in double precision; it is treated exactly above)
    k1 = iu - 60; k2 = iu + 62
    lamB1, NB1, _ = pair_stats(X[nn:k1:3], eps / 2, lam0); lamB2, NB2, _ = pair_stats(X[k2:arm.n:3], eps / 2, lam0)
    lamB = np.concatenate([lamB1, lamB2]); NB = np.concatenate([NB1, NB2])
    r4 = sup_table("rest of the arc (bulk)", lamB, NB)
    # (E2) separation
    S = X[::max(1, arm.n // 2500)]; dS = np.diff(S, axis=0); cs = np.concatenate([[0.0], np.cumsum(np.hypot(*dS.T))])
    U = cs[-1]; best = 1e9; best_all = 1e9
    for i in range(0, len(S), 5):
        far = np.abs(cs - cs[i]) > lam0
        if far.any(): best_all = min(best_all, float(np.hypot(*(S[far] - S[i]).T).min()))
        far2 = far & ~(((cs < 0.3) & (cs[i] > U - 0.3)) | ((cs[i] < 0.3) & (cs > U - 0.3)))      # exclude tail-vs-start pairs
        if far2.any(): best = min(best, float(np.hypot(*(S[far2] - S[i]).T).min()))
    # the tail (arc next to E_Y) as seen from Harry at X0: K_tail = int sin^2(phi)/rho ds over the first 0.3 of the tail
    p = arm.p; dd = np.diff(X, axis=0); dl = np.hypot(*dd.T); mid = 0.5 * (X[1:] + X[:-1]) - p; rm = np.hypot(*mid.T)
    sph = (dd[:, 0] * mid[:, 1] - dd[:, 1] * mid[:, 0]) / (dl * rm); ct = np.cumsum(dl); m = ct < 0.3
    Kt = float((sph[m] ** 2 / rm[m] * dl[m]).sum())
    print(f"  (E2) separation: min chord over pairs with arclength > {lam0}: {best:.4f} (excluding tail-vs-start pairs; with them: {best_all:.2e} = |E_Y - X0|);"
          f"  U = {U:.4f};  K_tail at touch-down = {Kt:.3e}")
    print(json.dumps(dict(v=v, eps=eps, forward=r1, endE=r2, hole=r3, bulk=r4, c_sep=best, U=float(U), sE=abs(zE), gap=gapw, K_tail=Kt)))
