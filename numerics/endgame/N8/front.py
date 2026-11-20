"""N8: exact front for a straight run from the centre along +x for time t (ANY t, also t > t_0 = 1/(1-v): Harry has run
THROUGH the front).  Candidate alpha in (0, pi), polar (rho, beta) about Harry (t, 0):
    rho g(beta) = g(alpha),   rho (cos beta + v) = cos alpha + v - (1 - v^2) t,   g(b) = sin b / tan^v(b/2).
We solve for gamma = pi - beta in log-scale (no loss for points almost straight behind Harry).  Double and mpmath."""
import math, numpy as np, mpmath as mp


def Ffun(lg, v):
    """(cos beta + v)/g(beta) with beta = pi - gamma, gamma = exp(lg)."""
    g_ = np.exp(lg)
    return (v - np.cos(g_)) / (np.sin(g_) * np.tan(g_ / 2) ** v)


def front(alpha, v, t):
    """positions relative to Harry (x forward): returns (x, y, rho, gamma) for labels alpha in (0, 2 pi) (mirror for > pi)."""
    alpha = np.atleast_1d(np.asarray(alpha, float))
    a = np.where(alpha <= math.pi, alpha, 2 * math.pi - alpha); sgn = np.where(alpha <= math.pi, 1.0, -1.0)
    ga = np.sin(a) / np.tan(a / 2) ** v
    R = (np.cos(a) + v - (1 - v * v) * t) / ga
    lo = np.full_like(a, -700.0); hi = np.full_like(a, math.log(math.pi) - 1e-15)
    for _ in range(200):                      # F is increasing in gamma (decreasing in beta)
        mid = 0.5 * (lo + hi); up = Ffun(mid, v) < R
        lo = np.where(up, mid, lo); hi = np.where(up, hi, mid)
    gam = np.exp(0.5 * (lo + hi))
    rho = ga / (np.sin(gam) * np.tan(gam / 2) ** v)
    return -rho * np.cos(gam), sgn * rho * np.sin(gam), rho, gam


def front_mp(alpha, vs, t, guess=None):
    """same in mpmath for one label alpha (mpf) in (0, pi); returns complex position relative to Harry."""
    v = mp.mpf(vs)
    ga = mp.sin(alpha) / mp.tan(alpha / 2) ** v
    R = (mp.cos(alpha) + v - (1 - v * v) * t) / ga
    f = lambda lg: (v - mp.cos(mp.e ** lg)) / (mp.sin(mp.e ** lg) * mp.tan(mp.e ** lg / 2) ** v) - R
    if guess is None:
        guess = math.log(front(float(alpha), float(vs), float(t))[3][0])
    lg = mp.findroot(f, mp.mpf(guess))
    gam = mp.e ** lg
    rho = ga / (mp.sin(gam) * mp.tan(gam / 2) ** v)
    return mp.mpc(-rho * mp.cos(gam), rho * mp.sin(gam))


def gmax(v):
    b = math.acos(v); return math.sin(b) / math.tan(b / 2) ** v


def alpha_seen(v, eps):
    """edge of the hole: g(alpha_s) = eps g_max (labels |alpha| < alpha_s are seen during the straight run)."""
    gm = gmax(v); lo, hi = math.log(1e-300), math.log(math.acos(v))
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if math.sin(math.exp(mid)) / math.tan(math.exp(mid) / 2) ** v < eps * gm: lo = mid
        else: hi = mid
    return math.exp(0.5 * (lo + hi))


if __name__ == '__main__':
    # F4: the front behind Harry after running through, near the axis: tilt of the tangent from the perpendicular to the axis
    for v in (0.3, 0.2, 0.1, 0.05):
        t0 = 1 / (1 - v)
        for D1 in (0.03, 0.1, 0.3):
            al = np.geomspace(1e-60, 0.3, 4000)
            x, y, rho, gam = front(al, v, t0 + D1)
            tilt = np.arctan(np.gradient(x, y))                  # angle of the tangent from the y-direction (signed)
            pred = -v * y / ((1 - v * v) * D1)
            sel = [np.searchsorted(y, q) for q in (1e-30, 1e-20, 1e-10, 1e-5, 1e-3, 1e-2)]
            print(f"v={v} D1={D1}: " + "  ".join(f"y={y[i]:.1e}: tilt={tilt[i]:+.3e} (parabola {pred[i]:+.3e})" for i in sel))
        # silhouette: argmin of beta
        t1 = t0 + 0.1; al = np.linspace(0.01, 3.0, 200001); x, y, rho, gam = front(al, v, t1)
        i = np.argmax(gam); print(f"   silhouette at t1=t0+0.1: numerical alpha0={al[i]:.5f}, formula arccos(v+1/t1)={math.acos(v+1/t1):.5f}")
