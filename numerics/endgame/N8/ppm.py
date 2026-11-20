"""N8: PURE PURSUIT MERGE (lead's candidate), local test in double precision (absolute coordinates, eps >= 1e-9).
Harry runs straight along +x for time r1 (exact front), then heads at every instant at the virtual candidate with label
a(t) = c (t - r1) until he meets it.  Virtual candidates x' = v F(x - P).  Nodes: labels graded around the capture label a_c
(found by iteration: spacing max(hmin, 0.02 |a - a_c|)).  Diagnostics at capture: forward arc (labels > a_c), unseen end
behind (first label < a_c never within eps), tilts against Harry's heading and their local exponents, (E1) constants.
Usage: python ppm.py v c r1 [eps ...]"""
import sys, os, math, json
import numpy as np
from numba import njit
import front as fr
from touch import pair_stats, APS


@njit(cache=True)
def interp(X, A, a):
    n = A.shape[0]
    lo = 0; hi = n - 1
    while hi - lo > 1:
        m = (lo + hi) // 2
        if A[m] <= a: lo = m
        else: hi = m
    j = lo
    if j < 1: j = 1
    if j > n - 3: j = n - 3
    x = 0.0; y = 0.0
    for p in range(-1, 3):
        w = 1.0
        for q in range(-1, 3):
            if q != p: w *= (a - A[j + q]) / (A[j + p] - A[j + q])
        x += w * X[j + p, 0]; y += w * X[j + p, 1]
    return x, y


@njit(cache=True)
def deriv(X, P, A, a, v, eps, dX):
    n = X.shape[0]
    for i in range(n):
        rx = X[i, 0] - P[0]; ry = X[i, 1] - P[1]; r = math.hypot(rx, ry)
        if r >= eps: f = 1.0 / r
        else: f = (2.0 * eps - r) / (eps * eps)
        dX[i, 0] = v * f * rx; dX[i, 1] = v * f * ry
    tx, ty = interp(X, A, a)
    dx = tx - P[0]; dy = ty - P[1]; d = math.hypot(dx, dy)
    return dx / d, dy / d, d


@njit(cache=True)
def pursue(X, A, P, t, r1, c, v, eps, mind, cstep, tmax):
    n = X.shape[0]
    k1 = np.zeros((n, 2)); k2 = np.zeros((n, 2)); k3 = np.zeros((n, 2)); k4 = np.zeros((n, 2)); Xs = np.zeros((n, 2)); Ps = np.zeros(2)
    ux = 1.0; uy = 0.0; nst = 0; dmin_all = 1e9
    while t < tmax:
        u1x, u1y, d = deriv(X, P, A, c * (t - r1), v, eps, k1)
        if d <= 1e-3 * eps:
            ux = u1x; uy = u1y; break
        dm = 1e9
        for i in range(n):
            q = math.hypot(X[i, 0] - P[0], X[i, 1] - P[1])
            if q < mind[i]: mind[i] = q
            if q < dm: dm = q
        dt = cstep * max(dm, 0.5 * eps)
        if dt > 0.5 * d / (1 - v): dt = max(0.5 * d / (1 - v), 1e-4 * eps)     # do not overshoot the capture
        for i in range(n):
            Xs[i, 0] = X[i, 0] + 0.5 * dt * k1[i, 0]; Xs[i, 1] = X[i, 1] + 0.5 * dt * k1[i, 1]
        Ps[0] = P[0] + 0.5 * dt * u1x; Ps[1] = P[1] + 0.5 * dt * u1y
        u2x, u2y, d2 = deriv(Xs, Ps, A, c * (t + 0.5 * dt - r1), v, eps, k2)
        for i in range(n):
            Xs[i, 0] = X[i, 0] + 0.5 * dt * k2[i, 0]; Xs[i, 1] = X[i, 1] + 0.5 * dt * k2[i, 1]
        Ps[0] = P[0] + 0.5 * dt * u2x; Ps[1] = P[1] + 0.5 * dt * u2y
        u3x, u3y, d3 = deriv(Xs, Ps, A, c * (t + 0.5 * dt - r1), v, eps, k3)
        for i in range(n):
            Xs[i, 0] = X[i, 0] + dt * k3[i, 0]; Xs[i, 1] = X[i, 1] + dt * k3[i, 1]
        Ps[0] = P[0] + dt * u3x; Ps[1] = P[1] + dt * u3y
        u4x, u4y, d4 = deriv(Xs, Ps, A, c * (t + dt - r1), v, eps, k4)
        for i in range(n):
            X[i, 0] += dt / 6 * (k1[i, 0] + 2 * k2[i, 0] + 2 * k3[i, 0] + k4[i, 0])
            X[i, 1] += dt / 6 * (k1[i, 1] + 2 * k2[i, 1] + 2 * k3[i, 1] + k4[i, 1])
        P[0] += dt / 6 * (u1x + 2 * u2x + 2 * u3x + u4x); P[1] += dt / 6 * (u1y + 2 * u2y + 2 * u3y + u4y)
        t += dt; nst += 1; ux = u1x; uy = u1y
    return t, ux, uy, nst


def run(v, c, r1, eps, a_c, hmin, amax=1.6):
    lab = [a_c]
    while lab[-1] < amax: lab.append(lab[-1] + max(hmin, 0.02 * (lab[-1] - a_c)))
    lo = [a_c]
    while lo[-1] > -0.6: lo.append(lo[-1] - max(hmin, 0.02 * (a_c - lo[-1])))
    A = np.array(lo[::-1][:-1] + lab)
    # exact positions at time r1 (labels may be negative: mirror)
    x, y, rho, gam = fr.front(np.abs(A) + 1e-300, v, r1)
    X = np.stack([r1 + x, np.sign(A) * y], 1)
    P = np.array([r1, 0.0]); mind = np.full(len(A), 1e9)
    t, ux, uy, nst = pursue(X, A, P, r1, r1, c, v, eps, mind, 0.05, 50.0)
    return dict(A=A, X=X, P=P, t=t, u=np.array([ux, uy]), mind=mind, a_cap=c * (t - r1), nst=nst)


def analyse(v, c, r1, eps):
    a_c = None; hmin = 2e-3
    res = run(v, c, r1, 1e-3 if eps < 1e-3 else eps, 0.5, 5e-3)
    a_c = res['a_cap']
    while True:                                   # refine the grid around the capture label
        res = run(v, c, r1, eps, a_c, hmin)
        if abs(res['a_cap'] - a_c) < 20 * hmin and hmin <= eps / 4: break
        a_c = res['a_cap']
        if hmin > eps / 4: hmin = max(hmin / 10, eps / 4)
    A, X, P, u, mind = res['A'], res['X'], res['P'], res['u'], res['mind']
    R = (X - P); xa = R[:, 0] * u[0] + R[:, 1] * u[1]; ya = -R[:, 0] * u[1] + R[:, 1] * u[0]      # Harry's frame (x ahead)
    Z = np.stack([xa, ya], 1)
    out = dict(v=v, c=c, r1=r1, eps=eps, t_cap=res['t'], a_cap=res['a_cap'], steps=res['nst'])
    fwd = A > res['a_cap']; ZF = np.vstack([[0.0, 0.0], Z[fwd]])
    d = np.diff(ZF, axis=0); s = np.cumsum(np.hypot(*d.T)); psi = np.arctan2(d[:, 1], d[:, 0])
    txt = []
    for r in (3 * eps, 30 * eps, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1):
        if r < 2 * eps or r > 0.2: continue
        i = np.searchsorted(s, r); j = np.searchsorted(s, 3 * r)
        if j < len(s) and psi[i] != 0: txt.append(f"s={r:.0e}: {psi[i]:+.2e} (a'={math.log(abs(psi[j]/psi[i]))/math.log(s[j]/s[i]):+.2f})")
    lam, N, _ = pair_stats(ZF, eps / 2, 0.1)
    out['fwd_C0'] = [float((N / lam ** (0.5 + a)).max()) for a in APS]
    print(f"v={v} c={c} r1={r1} eps={eps:g}: capture at t={res['t']:.5f}, label {res['a_cap']:.6f}, {res['nst']} steps")
    print("   forward arc, tilt against the heading: " + "; ".join(txt))
    print("   forward arc (E1): " + "; ".join(f"a'={a}: C0={x:.3g}" for a, x in zip(APS, out['fwd_C0'])))
    # behind: first never-seen candidate
    beh = np.nonzero((A < res['a_cap']) & (mind > eps))[0]
    if len(beh):
        ie = beh[-1]; zE = Z[ie]
        ZB = Z[:ie + 1][::-1]                              # from E_Y backwards
        d = np.diff(ZB, axis=0); s = np.cumsum(np.hypot(*d.T)); psi = np.unwrap(np.arctan2(d[:, 1], d[:, 0]))
        tilt0 = psi - math.pi * np.sign(psi[0])            # against Harry's line (pointing backwards)
        txt = []
        for r in (3 * eps, 30 * eps, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1):
            if r < 2 * eps or r > 0.2: continue
            i = np.searchsorted(s, r); j = np.searchsorted(s, 3 * r)
            if j < len(s) and tilt0[i] != tilt0[0] and tilt0[j] != tilt0[0]: txt.append(f"r={r:.0e}: {tilt0[i]:+.2e} (a'={math.log(abs((tilt0[j]-tilt0[0])/(tilt0[i]-tilt0[0])))/math.log(s[j]/s[i]):+.2f})")
        lam, N, _ = pair_stats(ZB, eps / 2, 0.1)
        out['E_C0'] = [float((N / lam ** (0.5 + a)).max()) for a in APS]
        out.update(E_dist=float(np.hypot(*zE)), E_lat=float(abs(zE[1])))
        print(f"   end E_Y left behind: label {A[ie]:.6f}, distance {np.hypot(*zE):.3e} = {np.hypot(*zE)/eps:.1f} eps = {np.hypot(*zE)/math.sqrt(eps):.3f} sqrt(eps),"
              f" lateral offset {abs(zE[1])/eps:.2f} eps; tangent at E_Y vs Harry's line {tilt0[0]:+.2e} rad")
        print("   tilt of the arc behind E_Y against Harry's line (exponent of tilt - tilt(E_Y)): " + "; ".join(txt))
        print("   end E_Y (E1): " + "; ".join(f"a'={a}: C0={x:.3g}" for a, x in zip(APS, out['E_C0'])))
    else:
        print("   everything behind the capture label (tracked range) was seen")
    print(json.dumps(out), flush=True)
    return out


if __name__ == '__main__':
    v = float(sys.argv[1]); c = float(sys.argv[2]); r1 = float(sys.argv[3])
    for e in ([float(x) for x in sys.argv[4:]] or [1e-3, 1e-4, 1e-5, 1e-6]):
        analyse(v, c, r1, e)
