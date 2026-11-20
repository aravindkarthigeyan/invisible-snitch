"""N8: the seen hole of design T as a piece of VIRTUAL front.  Candidates |alpha| <= alpha_s enter the eps-disc while Harry
runs through; virtual candidates (field v F, F = C^1 cut-off of P6a) are integrated through the pass and compared with the
true (exact) front at t1 = t0 + D1.  Is there a kink at scale eps?   Usage: python hole.py v [D1]"""
import sys, math, numpy as np
import front as fr
v = float(sys.argv[1]); D1 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.1
t0 = 1 / (1 - v)
def F(X, eps):
    r = np.hypot(X[:, 0], X[:, 1]); f = np.where(r >= eps, 1.0, (r / eps) * (2 - r / eps))
    return (f / np.maximum(r, 1e-300))[:, None] * X
for eps in (1e-3, 1e-4, 1e-5, 1e-6, 1e-7):
    a_s = fr.alpha_seen(v, eps)
    al = np.concatenate([np.linspace(1e-3 * a_s, a_s, 60), a_s * np.geomspace(1.0, 50.0, 60)[1:]])
    ta = t0 - 30 * eps
    x, y, rho, gam = fr.front(al, v, ta)
    X = np.stack([x, y], 1)                      # relative to Harry, Harry moves along +x: X' = v F(X) - (1, 0)
    t = ta; u = np.array([1.0, 0.0])
    def rhs(X): return v * F(X, eps) - u
    while t < t0 + D1 - 1e-15:
        d = max(np.hypot(X[:, 0], X[:, 1]).min(), eps / 4); dt = min(0.02 * d, t0 + D1 - t)
        k1 = rhs(X); k2 = rhs(X + 0.5 * dt * k1); k3 = rhs(X + 0.5 * dt * k2); k4 = rhs(X + dt * k3)
        X = X + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4); t += dt
    xt, yt, _, _ = fr.front(al, v, t0 + D1)
    out = al > 1.5 * a_s; ins = al < a_s
    err_out = np.hypot(X[out, 0] - xt[out], X[out, 1] - yt[out]).max()
    w = yt[np.argmin(np.abs(al - a_s))]            # half-width of the hole (true)
    dx = X[ins, 0] - xt[ins]; dy = X[ins, 1] - yt[ins]
    # virtual front inside the hole: tilt against the y-direction
    tv = np.gradient(X[:, 0], X[:, 1])
    print(f"v={v} eps={eps:g}: alpha_s={a_s:.2e}; hole half-width {w:.3e} = {w/eps:.2f} eps; unseen candidates: |virtual - exact| <= {err_out:.1e}; "
          f"inside the hole: virtual lags the true front by dx in [{dx.min()/eps:+.3f}, {dx.max()/eps:+.3f}] eps, |dy| <= {np.abs(dy).max()/eps:.3f} eps; "
          f"max tilt of the virtual front in/near the hole {np.abs(tv[al < 3 * a_s]).max():.3e} (true front: {v*w/((1-v*v)*D1):.1e})")
