"""Illustrative simulation of the capture path ("design T") from the paper.

Harry: speed 1, starts at the origin.  Candidates: the possible Snitch positions,
one per starting direction, all starting on the unit circle.  Each candidate moves
by the modified rule  S' = v (S - H) / max(|S - H|, eps)  used in the proof (it
agrees with the real Snitch until the candidate is first seen).

The path:
  1. run straight along the x-axis for t1 = 1/(1-v) + 1 (through the front);
  2. run straight at the candidate alpha0 = arccos(v + 1/t1) (tangential touch-down);
  3. walk the front: always head straight for the next unseen candidate in angular
     order, all the way round, until every candidate has been within eps.

Step 3 is a simplified version of the proof's "Construction C" (which steps along
the front by chord length eps); it is meant to show the shape of the argument, not
to reproduce the proof's constants.

Usage:
  python simulate_design_T.py                 # prints the sweep time
  python simulate_design_T.py --gif out.gif   # also writes an animation (needs matplotlib, pillow)
"""
import argparse
import math

import numpy as np


def simulate(v=0.1, eps=0.03, n=360, record_every=0.08, t_max=80.0):
    alpha = 2 * np.pi * np.arange(n) / n
    S = np.stack([np.cos(alpha), np.sin(alpha)], axis=1)
    seen = np.zeros(n, dtype=bool)
    H = np.zeros(2)
    t, dt = 0.0, min(0.004, eps / 3)
    t1 = 1 / (1 - v) + 1
    phase, direction, i0, ptr = "run1", np.array([1.0, 0.0]), None, 0
    frames, trail, next_rec, t_touch = [], [H.copy()], 0.0, None

    while t < t_max:
        d = S - H
        r = np.hypot(d[:, 0], d[:, 1])
        S += (v * dt / np.maximum(r, eps))[:, None] * d

        if phase == "run1" and t >= t1:
            a0 = math.acos(min(1.0, v + 1 / t1))
            i0 = int(round(a0 / (2 * np.pi) * n)) % n
            u = S[i0] - H
            direction, phase = u / np.linalg.norm(u), "run2"
        elif phase == "run2" and seen[i0]:
            phase, ptr, t_touch = "walk", i0, t
        if phase == "walk":
            k = 0
            while k < n and seen[(ptr + k) % n]:
                k += 1
            ptr = (ptr + k) % n
            u = S[ptr] - H
            direction = u / (np.linalg.norm(u) or 1.0)

        H = H + direction * dt
        t += dt
        d = S - H
        seen |= np.hypot(d[:, 0], d[:, 1]) <= eps

        if t >= next_rec:
            trail.append(H.copy())
            frames.append((t, S.copy(), seen.copy(), H.copy(), np.array(trail), phase))
            next_rec += record_every
        if seen.all():
            trail.append(H.copy())
            frames.append((t, S.copy(), seen.copy(), H.copy(), np.array(trail), "done"))
            return t, t_touch, frames
    return None, t_touch, frames


def make_gif(frames, path, eps, v):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation, PillowWriter

    gold, teal, grey, ink = "#B07A10", "#0B6E86", "#B5BFC7", "#16212B"
    fig, ax = plt.subplots(figsize=(5.4, 5.4), dpi=100)
    fig.patch.set_facecolor("#F8FAFB")
    keep = frames[:: max(1, len(frames) // 150)] + [frames[-1]] * 18

    def draw(k):
        t, S, seen, H, trail, phase = keep[k]
        ax.clear()
        ax.set_facecolor("#F8FAFB")
        R = max(2.3, 1.1 * np.abs(S[~seen]).max() if (~seen).any() else 2.3, 1.1 * np.abs(H).max())
        ax.set_xlim(-R, R); ax.set_ylim(-R, R); ax.set_aspect("equal"); ax.axis("off")
        ax.add_patch(plt.Circle((0, 0), 1, fill=False, ls="--", lw=0.8, color=grey))
        ax.scatter(S[seen, 0], S[seen, 1], s=2, color=grey, lw=0)
        un = ~seen
        ax.scatter(S[un, 0], S[un, 1], s=5, color=gold, lw=0)
        ax.plot(trail[:, 0], trail[:, 1], color=teal, lw=1.4, alpha=0.8)
        ax.add_patch(plt.Circle(H, max(eps, R / 120), color=teal, alpha=0.25))
        ax.plot(*H, "o", color=teal, ms=4)
        label = {"run1": "1  run through the front", "run2": "2  tangential touch-down",
                 "walk": "3  walk the front", "done": "4  every direction seen"}[phase]
        ax.text(-R * 0.96, R * 0.9, f"{label}\nt = {t:5.2f}   v = {v}", color=ink,
                family="monospace", fontsize=9, va="top")

    anim = FuncAnimation(fig, draw, frames=len(keep))
    anim.save(path, writer=PillowWriter(fps=18))
    plt.close(fig)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--v", type=float, default=0.1)
    ap.add_argument("--eps", type=float, default=0.03)
    ap.add_argument("--n", type=int, default=360)
    ap.add_argument("--gif")
    a = ap.parse_args()
    t_done, t_touch, frames = simulate(a.v, a.eps, a.n)
    print(f"v={a.v} eps={a.eps} n={a.n}: touch-down at t={t_touch:.2f}, "
          + (f"every direction seen at t={t_done:.2f}" if t_done else "not finished"))
    if a.gif:
        make_gif(frames, a.gif, a.eps, a.v)
        print("wrote", a.gif)
