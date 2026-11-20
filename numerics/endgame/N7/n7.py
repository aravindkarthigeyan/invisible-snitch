"""N7 core: deep-scale simulator for a left-behind arm (NUMERICAL model, see reports/N7-1.md).

Representation.  The arm is a chain of material (virtual-candidate) nodes stored RELATIVE TO ITS LAST-MET END E
("E-centred coordinates"): Y_i = x_i - x_E, Y_0 = 0, nodes geometric in distance from E.  Harry is stored as
p = P - x_E.  Evolution:   Y_i' = v [F(Y_i - p) - F(-p)],   p' = w + v F(p)    (w = Harry's velocity, |w| <= 1),
F = the C^1 virtual field of P6a (unit radial outside the eps-disc).  The difference of unit vectors is evaluated by a
cancellation-free formula, so scales 1e-100 next to scales 1 cost no precision; increments are accumulated with
compensated (two-sum) summation.  Time stepping: RK4.
"""
import math
import numpy as np
from numba import njit


# ---------------------------------------------------------------------------------------------- kernels
@njit(cache=True)
def F2(x, y, eps):
    rho = math.hypot(x, y)
    if rho >= eps:
        return x / rho, y / rho
    s = (2.0 * eps - rho) / (eps * eps)
    return x * s, y * s


@njit(cache=True)
def relF(Yx, Yy, px, py, eps):
    """F(Y - p) - F(-p), stable for |Y| << |p|."""
    ax = -px; ay = -py
    bx = Yx - px; by = Yy - py
    na = math.hypot(ax, ay); nb = math.hypot(bx, by)
    if na >= eps and nb >= eps and (Yx * Yx + Yy * Yy) < 0.25 * na * na:
        dn = (2.0 * (ax * Yx + ay * Yy) + Yx * Yx + Yy * Yy) / (na + nb)
        q = dn / (na * nb)
        return Yx / nb - ax * q, Yy / nb - ay * q
    f1x, f1y = F2(bx, by, eps); f2x, f2y = F2(ax, ay, eps)
    return f1x - f2x, f1y - f2y


@njit(cache=True)
def p_stages(p, pc, wx, wy, dt, v, eps, ps):
    """RK4 for p' = w + v F(p); stores the 4 stage positions in ps, updates p (compensated)."""
    x = p[0]; y = p[1]
    ps[0, 0] = x; ps[0, 1] = y
    fx, fy = F2(x, y, eps); k1x = wx + v * fx; k1y = wy + v * fy
    x2 = x + 0.5 * dt * k1x; y2 = y + 0.5 * dt * k1y; ps[1, 0] = x2; ps[1, 1] = y2
    fx, fy = F2(x2, y2, eps); k2x = wx + v * fx; k2y = wy + v * fy
    x3 = x + 0.5 * dt * k2x; y3 = y + 0.5 * dt * k2y; ps[2, 0] = x3; ps[2, 1] = y3
    fx, fy = F2(x3, y3, eps); k3x = wx + v * fx; k3y = wy + v * fy
    x4 = x + dt * k3x; y4 = y + dt * k3y; ps[3, 0] = x4; ps[3, 1] = y4
    fx, fy = F2(x4, y4, eps); k4x = wx + v * fx; k4y = wy + v * fy
    ix = dt / 6.0 * (k1x + 2 * k2x + 2 * k3x + k4x) + pc[0]
    iy = dt / 6.0 * (k1y + 2 * k2y + 2 * k3y + k4y) + pc[1]
    s = x + ix; bb = s - x; pc[0] = (x - (s - bb)) + (ix - bb); p[0] = s
    s = y + iy; bb = s - y; pc[1] = (y - (s - bb)) + (iy - bb); p[1] = s


@njit(cache=True)
def adv_chain(Y, C, n0, n1, ps, dt, v, eps):
    h = dt * v
    for i in range(n0, n1):
        x = Y[i, 0]; y = Y[i, 1]
        k1x, k1y = relF(x, y, ps[0, 0], ps[0, 1], eps)
        k2x, k2y = relF(x + 0.5 * h * k1x, y + 0.5 * h * k1y, ps[1, 0], ps[1, 1], eps)
        k3x, k3y = relF(x + 0.5 * h * k2x, y + 0.5 * h * k2y, ps[2, 0], ps[2, 1], eps)
        k4x, k4y = relF(x + h * k3x, y + h * k3y, ps[3, 0], ps[3, 1], eps)
        ix = h / 6.0 * (k1x + 2 * k2x + 2 * k3x + k4x) + C[i, 0]
        iy = h / 6.0 * (k1y + 2 * k2y + 2 * k3y + k4y) + C[i, 1]
        s = x + ix; bb = s - x; C[i, 0] = (x - (s - bb)) + (ix - bb); Y[i, 0] = s
        s = y + iy; bb = s - y; C[i, 1] = (y - (s - bb)) + (iy - bb); Y[i, 1] = s


@njit(cache=True)
def mindist(Y, n0, n1, p, skip):
    m = 1e300
    for i in range(n0, n1):
        if i == skip:
            continue
        d = math.hypot(Y[i, 0] - p[0], Y[i, 1] - p[1])
        if d < m:
            m = d
    return m


@njit(cache=True)
def run_w(Y, C, n, Tr, TrC, p, pc, wx, wy, T, cstep, v, eps, noise, seed):
    """Harry moves with constant velocity w for time T; adaptive steps dt = cstep * max(min distance, eps/4)."""
    ps = np.zeros((4, 2)); t = 0.0; nst = 0
    if noise > 0:
        np.random.seed(seed)
    while t < T * (1 - 1e-14):
        d = mindist(Y, 0, n, p, -1)
        if d < 0.25 * eps:
            d = 0.25 * eps
        dt = cstep * d
        if t + dt > T or T - (t + dt) < 0.2 * dt:
            dt = T - t
        p_stages(p, pc, wx, wy, dt, v, eps, ps)
        adv_chain(Y, C, 0, n, ps, dt, v, eps)
        adv_chain(Tr, TrC, 0, Tr.shape[0], ps, dt, v, eps)
        if noise > 0:
            for i in range(1, n):
                Y[i, 0] *= 1.0 + noise * np.random.randn(); Y[i, 1] *= 1.0 + noise * np.random.randn()
        t += dt; nst += 1
    return nst


@njit(cache=True)
def run_leg(Y, C, n, Tr, TrC, p, pc, kt, nsub, v, eps, tau):
    """Harry runs straight at node kt (pursuit of a radially fleeing target is a straight line) for the exact meeting
    time tau, uniform RK4 substeps.  Returns the RK4 mismatch of the target (its own ODE is singular at the meeting point)."""
    ps = np.zeros((4, 2))
    rx = Y[kt, 0] - p[0]; ry = Y[kt, 1] - p[1]; r0 = math.hypot(rx, ry)
    ux = rx / r0; uy = ry / r0
    dt = tau / nsub
    for _ in range(nsub):
        p_stages(p, pc, ux, uy, dt, v, eps, ps)
        adv_chain(Y, C, 0, n, ps, dt, v, eps)
        adv_chain(Tr, TrC, 0, Tr.shape[0], ps, dt, v, eps)
    mis = math.hypot(Y[kt, 0] - p[0], Y[kt, 1] - p[1])
    # the target moves on Harry's ray and is met exactly at time tau: put it at Harry's (smoothly integrated) position
    Y[kt, 0] = p[0]; Y[kt, 1] = p[1]; C[kt, 0] = pc[0]; C[kt, 1] = pc[1]
    return mis


# ---------------------------------------------------------------------------------------------- geometry at t_0
def gfun(b, v):
    return np.sin(b) / np.tan(b / 2) ** v


def exact_t0(alpha, v):
    """Front at first contact t_0 = 1/(1-v) (paper Lemma ST-front / P6c Claim 1): polar (rho, beta) about Harry of the
    candidate alpha in (0, pi):  rho g(beta) = g(alpha),  rho (cos beta + v) = -(1 - cos alpha).
    Returns rho and delta = beta - theta*, cos theta* = -v (delta computed without cancellation)."""
    alpha = np.atleast_1d(np.asarray(alpha, float))
    thst = math.acos(-v); sst = math.sqrt(1 - v * v)
    Tt = np.tan(alpha / 2) ** (1 + v)                      # = (1 - cos a)/g(a)
    d = np.zeros_like(alpha)
    for _ in range(400):
        c = Tt * gfun(thst + d, v)
        dn = np.arcsin(np.clip((c + 2 * v * np.sin(d / 2) ** 2) / sst, -1, 1))
        if np.max(np.abs(dn - d)) < 1e-17:
            d = dn; break
        d = dn
    rho = gfun(alpha, v) / gfun(thst + d, v)
    return rho, d


def alpha_seen(v, eps):
    """alpha_s: g(alpha_s) = eps g_max (candidates |alpha| <= alpha_s are seen during the straight phase)."""
    gmax = gfun(math.acos(v), v)
    lo, hi = math.log(1e-300), math.log(math.acos(v))
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if gfun(math.exp(mid), v) < eps * gmax: lo = mid
        else: hi = mid
    return math.exp(0.5 * (lo + hi))


def arm_nodes_t0(v, eps, alpha_top, g, d0fac=None):
    """Left arm at t_0, E-centred; E = label 2pi - alpha_s.  Nodes geometric (ratio g) in the t_0-distance from E,
    starting at d0 = d0fac*eps (default 1e-4 eps^{1.5 v}: the piece next to E is later stretched by ~(1/eps)^{v/(1+v)}),
    and geometric (ratio ~g) in the t_0-radius for alpha >> alpha_s.  Differences to E are evaluated without
    cancellation.  Frame: Harry came along +x to the corner O; the right arm leaves O in the direction e^{+i theta*},
    the left arm in e^{-i theta*}.  Returns alpha, rho (t_0-radius from O), Y (n,2), p0 = O - x_E."""
    a_s = alpha_seen(v, eps)
    if d0fac is None: d0fac = 1e-4 * eps ** (1.5 * v)
    G = g ** (1.0 / (1 - v))
    xs = [0.0, d0fac / (1 - v)]
    while a_s * (1 + xs[-1]) < alpha_top:
        x = xs[-1]; xs.append(x * (g + (G - g) * x / (1 + x)) if x < 1e6 else (1 + x) * G - 1)
    x = np.array(xs); x[-1] = alpha_top / a_s - 1.0
    al = a_s * (1 + x); Dl = a_s * x
    rho, d = exact_t0(al, v)
    thst = math.acos(-v); sst = math.sqrt(1 - v * v)
    rs = rho[0]; ds_ = d[0]
    # stable relative increments for labels close to alpha_s
    r_sin = 2 * np.cos(0.5 * (al + a_s)) * np.sin(0.5 * Dl) / math.sin(a_s)            # sin(al)/sin(a_s) - 1
    r_tan = np.sin(0.5 * Dl) / (np.cos(0.5 * al) * math.sin(0.5 * a_s))                # tan(al/2)/tan(a_s/2) - 1
    dlg = np.log1p(r_sin) - v * np.log1p(r_tan)                                        # log g(al) - log g(a_s)
    dd = ds_ * np.expm1((1 + v) * np.log1p(r_tan))                                     # delta - delta_s (leading order)
    xi = np.expm1(dlg + (2 * v / sst) * dd)                                            # rho/rho_s - 1
    near = x < 1e-3
    xi = np.where(near, xi, rho / rs - 1.0); dd = np.where(near, dd, d - ds_)
    re = rs * (xi * np.cos(d) - 2 * np.sin(0.5 * (d + ds_)) * np.sin(0.5 * dd))
    im = -rs * (xi * np.sin(d) + 2 * np.cos(0.5 * (d + ds_)) * np.sin(0.5 * dd))
    z = (re + 1j * im) * np.exp(-1j * thst)
    Y = np.stack([z.real, z.imag], 1); Y[0] = 0.0
    zE = rs * np.exp(-1j * (thst + ds_))
    return al, rho, Y, np.array([-zE.real, -zE.imag])


def close_time(c, v, eps):
    """meeting time with a virtual target at distance c straight ahead: int_0^c d rho / (1 - v f(rho))."""
    x, w = np.polynomial.legendre.leggauss(16)
    def seg(a, b):
        xx = 0.5 * (b - a) * x + 0.5 * (a + b)
        f = np.where(xx >= eps, 1.0, (xx / eps) * (2 - xx / eps))
        return 0.5 * (b - a) * np.sum(w / (1 - v * f))
    if c <= eps: return seg(0.0, c)
    return seg(0.0, eps) + (c - eps) / (1 - v)


# ---------------------------------------------------------------------------------------------- state
class Arm:
    def __init__(self, v, eps, Y, p0):
        self.v = v; self.eps = eps
        self.Y = np.ascontiguousarray(Y, float); self.C = np.zeros_like(self.Y); self.n = len(Y)
        self.p = np.array(p0, float); self.pc = np.zeros(2)
        self.t = 0.0
        self.trd = 1e-8 * eps
        self.Tr = np.array([[self.trd, 0.0], [0.0, self.trd]]); self.TrC = np.zeros((2, 2)); self.trlog = 0.0
        self.noise = 0.0; self.seed = 1

    def renorm_tr(self):
        m = np.abs(self.Tr).max()
        if m > 1e-4 * math.hypot(*self.p) or m > 1e-4 * self.eps:
            s = self.trd / m
            self.Tr *= s; self.TrC *= s; self.trlog -= math.log(s)

    def M(self):
        """linearised flow map at E since t = 0 (columns = images of e_x, e_y), returned as (M / |M|_max, log scale)."""
        M = (self.Tr / self.trd).T.copy()
        m = np.abs(M).max()
        return M / m, self.trlog + math.log(m)

    def move(self, w, T, cstep=0.02):
        if T <= 0: return
        # split so that the tracers can be renormalised
        nst = run_w(self.Y, self.C, self.n, self.Tr, self.TrC, self.p, self.pc, w[0], w[1], T, cstep, self.v, self.eps,
                    self.noise, self.seed)
        self.seed += 1
        self.t += T; self.renorm_tr()
        return nst

    def move_geom(self, w, T, cstep=0.02, chunk=2.0):
        """same as move, in chunks growing geometrically with the distance (for tracer renormalisation)."""
        done = 0.0
        while done < T * (1 - 1e-14):
            d = max(math.hypot(*self.p), self.eps)
            dt = min(chunk * d, T - done)
            if T - done - dt < 1e-3 * dt: dt = T - done
            self.move(w, dt, cstep); done += dt

    def leg(self, kt, nsub=8):
        r = self.Y[kt] - self.p; r0 = math.hypot(*r)
        tau = close_time(r0, self.v, self.eps)
        u = r / r0
        mis = run_leg(self.Y, self.C, self.n, self.Tr, self.TrC, self.p, self.pc, kt, nsub, self.v, self.eps, tau)
        self.t += tau; self.renorm_tr()
        return u, tau, r0, mis

    def arclen(self):
        d = np.diff(self.Y[:self.n], axis=0)
        return np.concatenate([[0.0], np.cumsum(np.hypot(d[:, 0], d[:, 1]))])


def interp_arc(X, s, sq):
    """4-point Lagrange (cubic) interpolation of the polyline nodes X (parameter s, increasing) at parameter values sq."""
    n = len(s)
    j = np.clip(np.searchsorted(s, sq, side='right') - 1, 1, n - 3)
    out = np.zeros((len(sq), 2))
    for a in range(-1, 3):
        w = np.ones(len(sq))
        for b in range(-1, 3):
            if b != a:
                w *= (sq - s[j + b]) / (s[j + a] - s[j + b])
        out += w[:, None] * X[j + a]
    return out
