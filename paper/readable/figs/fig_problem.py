"""Figure 1: the problem.  (a) the rule of motion; (b) candidates fleeing while Harry runs straight (v = 0.25 for
visibility), and the front at several times.  Output: fig_problem.pdf"""
import numpy as np
import snitchsim as s

plt = s.style()
v, eps = 0.25, 0.04
fig, axs = plt.subplots(1, 2, figsize=(6.8, 3.0), gridspec_kw=dict(width_ratios=[1, 1.55]))

# (a) the rule
ax = axs[0]
H = np.array([0.0, 0.0])
S = np.array([1.0, 0.55])
ax.add_patch(plt.Circle(H, 0.32, color=s.ACCENT, alpha=0.12, lw=0))
ax.plot(*H, "o", color=s.ACCENT, ms=6)
ax.text(-0.08, -0.2, "Harry $H(t)$", color=s.ACCENT, ha="center", va="top", fontsize=8.5)
ax.annotate("", xy=H + np.array([0.42, -0.25]), xytext=H, arrowprops=dict(arrowstyle="-|>", color=s.ACCENT, lw=1.2))
ax.text(0.45, -0.38, "speed $\\leq 1$,\nany direction", color=s.ACCENT, fontsize=7.5, va="top")
ax.plot(*S, "o", color=s.GOLD, ms=6)
ax.text(S[0] - 0.05, S[1] + 0.1, "Snitch $S(t)$", color=s.GOLD, fontsize=8.5, ha="right")
u = (S - H) / np.linalg.norm(S - H)
ax.plot([H[0], S[0]], [H[1], S[1]], ls=(0, (2, 2)), color=s.MUTED, lw=0.7)
ax.annotate("", xy=S + 0.38 * u, xytext=S, arrowprops=dict(arrowstyle="-|>", color=s.GOLD, lw=1.4))
ax.text(S[0] + 0.42 * u[0] + 0.03, S[1] + 0.38 * u[1] - 0.12, "speed $v$,\nstraight away\nfrom Harry",
        color=s.GOLD, fontsize=7.5, va="top")
ax.annotate("vision radius $\\varepsilon$", xy=(-0.226, 0.226), xytext=(-0.55, 0.75), color=s.ACCENT, fontsize=7.5,
            arrowprops=dict(arrowstyle="-", color=s.ACCENT, lw=0.5))
ax.set_xlim(-0.7, 1.75)
ax.set_ylim(-0.9, 1.15)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("(a) the rule of the chase", pad=2)

# (b) candidates fleeing during run 1
ax = axs[1]
n_traj = 24
al = 2 * np.pi * np.arange(n_traj) / n_traj
dense = np.linspace(0, 2 * np.pi, 1441)[:-1]
alphas = np.unique(np.concatenate([al, dense]))
t1 = 2.0
times = [0.0, 0.7, 1.4, 2.0]
X = np.stack([np.cos(alphas), np.sin(alphas)], 1)
seen = np.zeros(len(alphas), bool)
P = np.zeros(2)
d = np.array([1.0, 0.0])
dt = 0.002
t = 0.0
traj = [X.copy()]
fronts = {0.0: (X.copy(), seen.copy())}
while t < t1 - 1e-12:
    X = s.rk4_step(X, P, d, dt, v, eps)
    P = P + dt * d
    t += dt
    seen |= np.hypot(*(X - P).T) <= eps
    traj.append(X.copy())
    for tt in times:
        if abs(t - tt) < dt / 2:
            fronts[tt] = (X.copy(), seen.copy())
traj = np.array(traj)
isel = [int(np.argmin(np.abs(alphas - a))) for a in al]
for i in isel:
    ax.plot(traj[:, i, 0], traj[:, i, 1], color=s.GOLD, lw=0.8, alpha=0.9)
    ax.plot(traj[-1, i, 0], traj[-1, i, 1], "o", color=s.GOLD, ms=2.2)
shades = [s.LIGHT, (0.55, 0.68, 0.80), (0.30, 0.50, 0.68), s.PRIMARY]
for tt, c, ang in zip(times, shades, [3.0, 3.45, 3.9, 4.35]):
    if tt not in fronts:
        continue
    Xf, sf = fronts[tt]
    Xf = np.vstack([Xf, Xf[:1]])
    ax.plot(Xf[:, 0], Xf[:, 1], color=c, lw=1.3 if tt > 0 else 1.0, ls="-" if tt > 0 else (0, (2, 2)),
            label=f"$t={tt:g}$")
ax.legend(loc="upper left", frameon=False, title="front at time", title_fontsize=7.5, fontsize=7,
          bbox_to_anchor=(-0.02, 1.0), handlelength=1.5)
ax.plot([0, t1], [0, 0], color=s.ACCENT, lw=1.3)
ax.plot(t1, 0, "o", color=s.ACCENT, ms=4.5)
ax.plot(0, 0, "o", color="black", ms=2.5)
ax.annotate("Harry's path", xy=(1.6, 0), xytext=(1.25, -0.75), color=s.ACCENT, fontsize=8,
            arrowprops=dict(arrowstyle="-", color=s.ACCENT, lw=0.5))
ax.annotate("direction 0:\ncaught", xy=(1.0, 0.0), xytext=(1.55, 0.55), color=s.MUTED, fontsize=7.5,
            arrowprops=dict(arrowstyle="-", color=s.MUTED, lw=0.5))
ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-2.2, 2.25)
ax.set_ylim(-1.6, 1.6)
ax.set_title("(b) all candidates at once: the front", pad=2)
fig.subplots_adjust(wspace=0.05)
fig.savefig("fig_problem.pdf")


