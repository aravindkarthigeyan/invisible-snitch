"""Figure: the life of a pair of points on the front during the walk (v = 0.1, eps = 0.01).
For pairs (a, b) of angular label length lambda (arclength at touch-down about 1.1 lambda) the relative change
100 (N(t)/N(t_td) - 1) of the bendiness N = sqrt(2(l - c)) is plotted against time, with the phases 'far'
(gap g >= K_f lambda_u, K_f = 10, lambda_u = arclength of the pair at touch-down), 'near' (0 <= g < K_f lambda_u) and
'passed'.  Note: this run uses eps = 0.01, whereas fig_designT.py uses eps = 0.02.
Output: fig_timeline.pdf"""
import numpy as np
import snitchsim as s

plt = s.style()
v, eps = 0.1, 0.01
t1, a0 = s.design_T_data(v)
lams = [0.02, 0.1]
amid = a0 + 3.2
base_grid = 2 * np.pi * np.arange(9000) / 9000
pairs = []
extra = []
for lam in lams:
    pa, pb = amid, amid + lam
    pairs.append((pa % (2 * np.pi), pb % (2 * np.pi)))
    extra.append(np.linspace(pa, pb, 400) % (2 * np.pi))
alphas = np.concatenate([base_grid, [a0]] + extra)
o = s.simulate(v=v, eps=eps, alphas=alphas, dt=eps / 4, pair_labels=pairs, verbose=False)
rec = o["pairs"]
t = rec[:, 0]
base = rec[:, 1].astype(int)
al = o["alphas"]
# label coordinate u = arclength at touch-down
Xtd = o["X_td"]
u = np.concatenate([[0.0], np.cumsum(np.hypot(*np.diff(Xtd, axis=0).T))])
idx = []
for (pa, pb) in pairs:
    ia = int(np.argmin(np.abs(((al - pa + np.pi) % (2 * np.pi)) - np.pi)))
    ib = int(np.argmin(np.abs(((al - pb + np.pi) % (2 * np.pi)) - np.pi)))
    idx.append((ia, ib))
t_td = o["t_td"]
K_f = 10
fig, axs = plt.subplots(1, len(lams), figsize=(6.8, 2.5), sharey=False)
for k, (lam, (ia, ib), ax) in enumerate(zip(lams, idx, axs)):
    l = rec[:, 2 + 2 * k]
    c = rec[:, 3 + 2 * k]
    N = np.sqrt(np.maximum(2 * (l - c), 0))
    lam_u = u[ib] - u[ia]
    ok = (t >= t_td) & (base >= 0)
    g = np.where(ok, u[ia] - u[np.maximum(base, 0)], np.nan)
    far = ok & (g >= K_f * lam_u)
    near = ok & (g >= 0) & (g < K_f * lam_u)
    passed = ok & (g < 0)
    y0 = N[np.searchsorted(t, t_td)]
    y = 100 * (N / y0 - 1)
    pre = t <= t_td
    ax.plot(t[pre], y[pre], color=s.MUTED, lw=1.2)
    ax.plot(t[far], y[far], color=s.PRIMARY, lw=1.6)
    ax.plot(t[near], y[near], color=s.ACCENT, lw=1.6)
    tn0 = t[near].min()
    tn1 = t[near].max()
    ymax, ymin = 3.0, -2.0
    ax.axvspan(t[ok].min(), tn0, color=s.PRIMARY, alpha=0.06, lw=0)
    ax.axvspan(tn0, tn1, color=s.ACCENT, alpha=0.10, lw=0)
    ax.axvline(t_td, color=s.LIGHT, lw=0.8)
    ax.set_xlim(0, tn1 + 0.6)
    ax.set_ylim(ymin, ymax)
    ax.axhline(0, color=s.LIGHT, lw=0.6, zorder=0)
    ax.text(t_td / 2, ymax * 0.92, "Design T", ha="center", va="top", fontsize=7.5, color=s.MUTED)
    ax.text((t_td + tn0) / 2, ymax * 0.92, "far: Harry is\nmany pair-lengths\naway", ha="center", va="top",
            fontsize=7.5, color=s.PRIMARY)
    ax.text(tn0 - 0.2, ymax * 0.55, "near", ha="right", va="center", fontsize=7.5, color=s.ACCENT)
    ax.annotate("", xy=(tn0 + 0.02, ymax * 0.55), xytext=(tn0 - 0.18, ymax * 0.55),
                arrowprops=dict(arrowstyle="-|>", color=s.ACCENT, lw=0.6))
    ax.set_xlabel("time $t$")
    ax.set_title(f"pair of length $\\lambda = {lam:g}$", pad=2)
    for sp in ["top", "right"]:
        ax.spines[sp].set_visible(False)
    print(f"lam={lam}: rel change % at td {y[np.searchsorted(t, t_td)]:.4f}, at near start {y[near][0]:.4f},"
          f" at near end {y[near][-1]:.4f}; near phase [{tn0:.3f},{tn1:.3f}]")
axs[0].set_ylabel("change of bendiness $N$\nsince touch-down (%)")
fig.subplots_adjust(wspace=0.25)
fig.savefig("fig_timeline.pdf")



