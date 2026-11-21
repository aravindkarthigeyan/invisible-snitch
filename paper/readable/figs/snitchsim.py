"""Shared simulation code for the figures of the readable proof (human/snitch_human.tex).

Harry's path is the one of the proof: Design T (run 1 along the x-axis for t1 = 1/(1-v) + 1, run 2 straight towards the
candidate alpha0 = arccos(v + 1/t1) until he meets it), followed by the greedy chase: at the start of each leg Harry picks
the label a_{j+1} an arclength eps further along the front and runs straight at x_{a_{j+1}} until he meets it.

Candidates are *virtual* candidates: they move by x' = v F(x - P) with the regularised field F of Definition 2.1
(F(x) = x/|x| for |x| >= eps, F(x) = (|x|/eps)(2 - |x|/eps) x/|x| inside the eps-disc).  A label counts as seen once
|x - P| <= eps; up to that moment the virtual candidate is the true candidate.

Integration: classical RK4 with Harry's position linear in t on each step.
"""
import math
import numpy as np

PRIMARY = (24 / 255, 78 / 255, 119 / 255)
ACCENT = (181 / 255, 68 / 255, 42 / 255)
MUTED = (90 / 255, 102 / 255, 115 / 255)
LIGHT = (0.78, 0.81, 0.84)
GOLD = (0.80, 0.58, 0.10)


def style():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["cmr10"],
        "axes.unicode_minus": False,
        "mathtext.fontset": "cm",
        "axes.formatter.use_mathtext": True,
        "font.size": 9,
        "axes.titlesize": 9.5,
        "axes.labelsize": 9,
        "legend.fontsize": 8,
        "axes.edgecolor": MUTED,
        "axes.labelcolor": "black",
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "pdf.fonttype": 42,
    })
    return plt


def field(r, v, eps):
    """v F(r) for an array r of shape (n,2)."""
    rho = np.hypot(r[:, 0], r[:, 1])
    f = np.where(rho >= eps, 1.0, (rho / eps) * (2.0 - rho / eps))
    with np.errstate(invalid="ignore", divide="ignore"):
        s = np.where(rho > 0, v * f / rho, 0.0)
    return r * s[:, None]


def true_field(r, v):
    rho = np.hypot(r[:, 0], r[:, 1])
    return r * (v / np.maximum(rho, 1e-300))[:, None]


def rk4_step(X, P, d, h, v, eps):
    """One RK4 step of x' = vF(x - P(t)) with P(t) = P + d (t - t0)."""
    k1 = field(X - P, v, eps)
    Pm = P + 0.5 * h * d
    k2 = field(X + 0.5 * h * k1 - Pm, v, eps)
    k3 = field(X + 0.5 * h * k2 - Pm, v, eps)
    Pe = P + h * d
    k4 = field(X + h * k3 - Pe, v, eps)
    return X + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


def design_T_data(v):
    t1 = 1.0 / (1.0 - v) + 1.0
    a0 = math.acos(v + 1.0 / t1)
    return t1, a0


def simulate(v=0.1, eps=0.02, alphas=None, n=4000, dt=None, snap_times=(), walk=True, t_max=40.0,
             record_trail_every=0.01, pair_labels=None, verbose=False):
    """Run Design T (+ greedy chase).  Returns a dict with snapshots and the trail.

    alphas: label grid (radians); default n uniform labels plus alpha0 itself.
    pair_labels: list of (alpha_a, alpha_b); their excess E = l - c is recorded at every step (labels must be in grid).
    """
    t1, a0 = design_T_data(v)
    if alphas is None:
        alphas = np.sort(np.concatenate([2 * np.pi * np.arange(n) / n, [a0]]))
    alphas = np.unique(np.asarray(alphas, float) % (2 * np.pi))
    # order labels along the walk: alpha0 first, then counter-clockwise
    key = (alphas - a0) % (2 * np.pi)
    order = np.argsort(key)
    alphas = alphas[order]
    i0 = int(np.argmin(np.abs(((alphas - a0 + np.pi) % (2 * np.pi)) - np.pi)))
    alphas = np.roll(alphas, -i0)
    X = np.stack([np.cos(alphas), np.sin(alphas)], 1)
    seen = np.zeros(len(alphas), bool)
    if dt is None:
        dt = min(0.004, eps / 4)
    P = np.zeros(2)
    t = 0.0
    snaps = {}
    snap_times = sorted(snap_times)
    trail = [(0.0, P[0], P[1])]
    next_trail = record_trail_every
    pair_idx = []
    if pair_labels:
        for (pa, pb) in pair_labels:
            ia = int(np.argmin(np.abs(((alphas - pa + np.pi) % (2 * np.pi)) - np.pi)))
            ib = int(np.argmin(np.abs(((alphas - pb + np.pi) % (2 * np.pi)) - np.pi)))
            pair_idx.append((ia, ib))
    pair_rec = []
    cur = dict(base=-1)

    def record_pairs():
        if not pair_idx:
            return
        row = [t, cur["base"]]
        for (ia, ib) in pair_idx:
            seg = X[ia:ib + 1]
            l = np.sum(np.hypot(*np.diff(seg, axis=0).T))
            c = np.hypot(*(X[ib] - X[ia]))
            row += [l, c]
        pair_rec.append(row)

    def take_snaps(phase, base=None):
        while snap_times and t >= snap_times[0] - 1e-12:
            st = snap_times.pop(0)
            snaps[st] = dict(t=t, X=X.copy(), seen=seen.copy(), P=P.copy(), trail=np.array(trail), phase=phase,
                             base=base)

    def advance(d, h):
        nonlocal X, P, t, next_trail
        X = rk4_step(X, P, d, h, v, eps)
        P = P + h * d
        t += h
        r = X - P
        seen[np.hypot(r[:, 0], r[:, 1]) <= eps] = True
        if t >= next_trail:
            trail.append((t, P[0], P[1]))
            next_trail += record_trail_every
        record_pairs()

    record_pairs()
    # --- run 1
    d = np.array([1.0, 0.0])
    while t < t1 - 1e-12:
        h = min(dt, t1 - t)
        advance(d, h)
        take_snaps("run1")
    # --- run 2: straight at x_{alpha0}(t1) until meeting it
    d = X[0] - P
    d = d / np.linalg.norm(d)
    nhat = d.copy()
    while True:
        gap = np.hypot(*(X[0] - P))
        if gap < 1e-9:
            break
        h = min(dt, gap / (1.0 + v) * 0.98) if gap < 3 * dt else dt
        if h < 1e-10:
            break
        advance(d, h)
        take_snaps("run2")
    P = X[0].copy()
    t_td = t
    trail.append((t, P[0], P[1]))
    X_td = X.copy()
    seen_td = seen.copy()
    take_snaps("td", base=0)
    out = dict(v=v, eps=eps, t1=t1, a0=a0, nhat=nhat, t_td=t_td, alphas=alphas, X_td=X_td, seen_td=seen_td,
               P_td=P.copy())
    if not walk:
        out.update(snaps=snaps, trail=np.array(trail), X=X, seen=seen, pairs=np.array(pair_rec))
        return out
    # --- greedy chase
    base = 0
    cur["base"] = 0
    nlab = len(alphas)
    legs = []
    while t < t_max:
        seglen = np.hypot(*np.diff(X[base:], axis=0).T)
        cum = np.concatenate([[0.0], np.cumsum(seglen)])
        k = int(np.searchsorted(cum, eps, side="right") - 1)
        tgt = base + max(k, 1)
        if tgt >= nlab - 1:
            tgt = nlab - 1
            # final leg: everything up to the end is within eps of P already (or nearly so)
            legs.append((t, base, tgt))
            break
        d = X[tgt] - P
        dn = np.linalg.norm(d)
        if dn < 1e-12:
            base = tgt
            continue
        d = d / dn
        legs.append((t, base, tgt))
        while True:
            gap = np.hypot(*(X[tgt] - P))
            if gap < 1e-9:
                break
            h = min(dt, gap / (1.0 + v) * 0.98) if gap < 3 * dt else dt
            if h < 1e-10:
                break
            advance(d, h)
            take_snaps("walk", base=base)
        P = X[tgt].copy()
        base = tgt
        cur["base"] = base
        if verbose and len(legs) % 100 == 0:
            print(f"  t={t:.3f} base={base}/{nlab} seen={seen.mean():.3f}")
    t_stop = t
    trail.append((t, P[0], P[1]))
    snap_times.clear()
    snaps["end"] = dict(t=t, X=X.copy(), seen=seen.copy(), P=P.copy(), trail=np.array(trail), phase="done", base=base)
    out.update(snaps=snaps, trail=np.array(trail), X=X, seen=seen, t_stop=t_stop, legs=legs,
               pairs=np.array(pair_rec))
    return out


