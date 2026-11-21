"""Figure: the path of the proof (Design T + greedy chase) at v = 0.1, eps = 0.02; six snapshots of the front.
Note: snitchsim.simulate walks the whole front of regularised (virtual) candidates, including the sliver [b_e, alpha0)
seen at touch-down and the labels near direction 0; the proof cuts the front at b_e and uses true candidates plus the
limit point Z_s.  So the picture shows a close variant of the path of Theorem 1.1.
Output: fig_designT.pdf"""
import numpy as np
import snitchsim as s

plt = s.style()
v, eps = 0.1, 0.02
t1, a0 = s.design_T_data(v)
T_TD = 4.2066  # touch-down time at these parameters (printed below)
o = s.simulate(v=v, eps=eps, n=5000, snap_times=[1.25, t1 + 1.0, T_TD + 2.5, T_TD + 6.0])
snaps = o["snaps"]
keys = sorted(k for k in snaps if k != "end")
t_td = o["t_td"]
td = dict(t=t_td, X=o["X_td"], seen=o["seen_td"], P=o["P_td"], trail=o["trail"][o["trail"][:, 0] <= t_td + 1e-9])
panels = [snaps[keys[0]], snaps[keys[1]], td, snaps[keys[2]], snaps[keys[3]], snaps["end"]]
titles = ["(a) run 1: straight through", "(b) run 2: towards the front",
          "(c) tangential touch-down", "(d) walking along the front", "(e) still walking",
          "(f) every direction seen"]

allX = np.concatenate([p["X"] for p in panels] + [o["trail"][:, 1:3]])
xlim = (allX[:, 0].min() - 0.08, allX[:, 0].max() + 0.08)
ylim = (allX[:, 1].min() - 0.08, allX[:, 1].max() + 0.08)


def draw(ax, sn, title):
    X, seen, P, trail = sn["X"], sn["seen"], sn["P"], sn["trail"]
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), ls=(0, (2, 2)), lw=0.6, color=s.LIGHT, zorder=0)
    ax.plot(X[:, 0], X[:, 1], color=s.LIGHT, lw=1.1, zorder=1)
    idx = np.where(~seen)[0]
    if len(idx):
        breaks = np.where(np.diff(idx) > 1)[0]
        starts = np.concatenate([[0], breaks + 1])
        ends = np.concatenate([breaks, [len(idx) - 1]])
        for a, b in zip(starts, ends):
            seg = X[idx[a]:idx[b] + 1]
            ax.plot(seg[:, 0], seg[:, 1], color=s.PRIMARY, lw=1.9, solid_capstyle="round", zorder=2)
    ax.plot(trail[:, 1], trail[:, 2], color=s.ACCENT, lw=1.0, zorder=3)
    ax.plot([trail[-1, 1], P[0]], [trail[-1, 2], P[1]], color=s.ACCENT, lw=1.0, zorder=3)
    ax.plot(*P, "o", color=s.ACCENT, ms=4.2, zorder=4)
    ax.plot(0, 0, "o", color="black", ms=2.0, zorder=4)
    ax.set_title(title + f"\n$t = {sn['t']:.2f}$", pad=1, fontsize=8.5)
    ax.set_aspect("equal")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")


fig, axs = plt.subplots(2, 3, figsize=(7.0, 5.0))
for ax, sn, ti in zip(axs.flat, panels, titles):
    draw(ax, sn, ti)
ax = axs[0, 0]
ax.annotate("Harry", xy=panels[0]["P"], xytext=(1.35, -0.85), color=s.ACCENT, fontsize=8,
            arrowprops=dict(arrowstyle="-", color=s.ACCENT, lw=0.5))
ax.annotate("start", xy=(0, 0), xytext=(-0.55, -0.35), color="black", fontsize=8,
            arrowprops=dict(arrowstyle="-", color="black", lw=0.5))
ax.text(xlim[0] + 0.05, ylim[1] - 0.25, "unseen part of the front", color=s.PRIMARY, fontsize=7.5)
ax.text(xlim[0] + 0.05, ylim[1] - 0.55, "seen part", color=(0.6, 0.64, 0.68), fontsize=7.5)
ax.text(xlim[0] + 0.05, ylim[1] - 0.85, "Harry's path", color=s.ACCENT, fontsize=7.5)
axs[0, 0].annotate("starting circle", xy=(np.cos(4.0), np.sin(4.0)), xytext=(-1.3, -1.45), color=s.MUTED, fontsize=7, arrowprops=dict(arrowstyle="-", color=s.MUTED, lw=0.5))
axs[0, 2].annotate("tail end, left\nbehind Harry", xy=o["X_td"][-1], xytext=(1.2, -0.75), color=s.PRIMARY, fontsize=7.5,
                   arrowprops=dict(arrowstyle="-", color=s.PRIMARY, lw=0.5))
fig.subplots_adjust(wspace=0.03, hspace=0.12)
fig.savefig("fig_designT.pdf")
print("t_td", t_td, "t_stop", o["t_stop"], "legs", len(o["legs"]))

