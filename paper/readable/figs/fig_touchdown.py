"""Figure: the front at the touch-down time, seen from Harry (rotated so that the run-2 heading points right).
v = 0.1, eps = 0.01.  Output: fig_touchdown.pdf"""
import numpy as np
import snitchsim as s

plt = s.style()
v, eps = 0.1, 0.01
t1, a0 = s.design_T_data(v)
xi = np.concatenate([-np.geomspace(0.6, 1e-6, 1500), [0.0], np.geomspace(1e-6, 0.6, 1500)])
alphas = a0 + xi
o = s.simulate(v=v, eps=eps, alphas=alphas, dt=eps / 8, walk=False)
nh = o["nhat"]
X, seen, P = o["X_td"], o["seen_td"], o["P_td"]
al = o["alphas"]
# walk order puts alpha0 first; restore order by xi
xi_l = ((al - a0 + np.pi) % (2 * np.pi)) - np.pi
srt = np.argsort(xi_l)
X, seen, xi_l = X[srt], seen[srt], xi_l[srt]
# heading frame: z along nhat, y perpendicular
R = np.array([[nh[0], nh[1]], [-nh[1], nh[0]]])
Z = (X - P) @ R.T
tr = o["trail"]
TR = (tr[:, 1:3] - P) @ R.T

fig, ax = plt.subplots(figsize=(6.6, 3.0))
W = 0.42
# swept band of Harry's vision disc along run 2
band = TR[(TR[:, 0] > -W - 0.1)]
ax.fill_between([-W - 0.05, 0.0], [-eps, -eps], [eps, eps], color=s.ACCENT, alpha=0.10, lw=0)
circ = plt.Circle((0, 0), eps, color=s.ACCENT, alpha=0.25, lw=0)
ax.add_patch(circ)
ax.plot([-W - 0.05, 0], [0, 0], color=s.ACCENT, lw=1.2)
ax.annotate("", xy=(0.0, 0), xytext=(-0.06, 0), arrowprops=dict(arrowstyle="-|>", color=s.ACCENT, lw=1.2))
# front pieces
fwd = xi_l >= 0
tail_unseen = (xi_l < 0) & ~seen
tail_seen = (xi_l < 0) & seen
ax.plot(Z[fwd, 0], Z[fwd, 1], color=s.PRIMARY, lw=2.0, solid_capstyle="round")
ax.plot(Z[tail_unseen, 0], Z[tail_unseen, 1], color=s.PRIMARY, lw=2.0, solid_capstyle="round")
ax.plot(Z[tail_seen, 0], Z[tail_seen, 1], color=(0.6, 0.64, 0.68), lw=2.0, solid_capstyle="butt")
# tail end
iE = np.where(tail_unseen)[0].max()
E = Z[iE]
ax.plot(*E, "o", color=s.PRIMARY, ms=4)
ax.plot(0, 0, "o", color=s.ACCENT, ms=4.5, zorder=5)
ax.set_aspect("equal")
ax.set_xlim(-W, W)
ax.set_ylim(-0.075, 0.16)
ax.axis("off")
ax.annotate("Harry at touch-down", xy=(0, 0), xytext=(0.02, 0.045), color=s.ACCENT, fontsize=8,
            arrowprops=dict(arrowstyle="-", color=s.ACCENT, lw=0.5))
ax.text(-W + 0.01, -0.03, "run 2 (Harry's path)", color=s.ACCENT, fontsize=8)
ax.annotate("forward arc: walked next", xy=Z[fwd][np.argmin(np.abs(Z[fwd, 0] - 0.3))], xytext=(0.12, 0.13),
            color=s.PRIMARY, fontsize=8, arrowprops=dict(arrowstyle="-", color=s.PRIMARY, lw=0.5))
ax.annotate("tail end $x^0(U)$", xy=E, xytext=(E[0] - 0.21, -0.06), color=s.PRIMARY, fontsize=8,
            arrowprops=dict(arrowstyle="-", color=s.PRIMARY, lw=0.5))
ax.annotate("seen while grazing", xy=Z[tail_seen][len(Z[tail_seen]) // 2], xytext=(-0.17, 0.05),
            color=s.MUTED, fontsize=8, arrowprops=dict(arrowstyle="-", color=s.MUTED, lw=0.5))
ax.annotate("tail arc: walked last", xy=Z[tail_unseen][np.argmin(np.abs(Z[tail_unseen, 0] + 0.3))],
            xytext=(-0.25, 0.13), color=s.PRIMARY, fontsize=8,
            arrowprops=dict(arrowstyle="-", color=s.PRIMARY, lw=0.5))
# distance bracket from E to Harry
ax.annotate("", xy=(E[0], -0.022), xytext=(0, -0.022), arrowprops=dict(arrowstyle="<->", color=s.MUTED, lw=0.6))
ax.text(E[0] / 2, -0.034, r"$z_0\asymp\varepsilon^{1/(2-2v)}$", color=s.MUTED, fontsize=8, ha="center", va="top")
fig.savefig("fig_touchdown.pdf")
print("t_td", o["t_td"], "E", E, "eps^(1/(2-2v))", eps ** (1 / (2 - 2 * v)))

