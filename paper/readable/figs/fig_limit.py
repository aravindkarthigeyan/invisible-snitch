"""Figure: the paths of the proof for shrinking vision radius eps (v = 0.1).  They converge as eps -> 0, and the
finishing time stays bounded.  Output: fig_limit.pdf"""
import numpy as np
import snitchsim as s

plt = s.style()
v = 0.1
epss = [0.08, 0.04, 0.02, 0.01]
cols = [(0.66, 0.79, 0.90), (0.45, 0.64, 0.80), (0.25, 0.47, 0.66), s.PRIMARY]
fig, axs = plt.subplots(1, 2, figsize=(6.8, 3.2), gridspec_kw=dict(width_ratios=[1.35, 1]))
ax = axs[0]
res = []
for eps, c in zip(epss, cols):
    n = int(round(60 / eps))
    o = s.simulate(v=v, eps=eps, n=n, dt=eps / 4)
    tr = o["trail"]
    ax.plot(tr[:, 1], tr[:, 2], color=c, lw=1.1, label=f"$\\varepsilon = {eps:g}$,  done at $t = {o['t_stop']:.2f}$")
    res.append((eps, o["t_stop"], tr))
    print(eps, o["t_stop"])
ax.plot(0, 0, "o", color="black", ms=2.5)
ax.set_aspect("equal")
ax.axis("off")
ax.legend(loc="upper center", frameon=False, fontsize=7, bbox_to_anchor=(0.5, 0.02), ncol=2, columnspacing=1.0)
ax.set_title("(a) the paths for four vision radii\n(they overlap at this scale)", pad=2)

# (b) distance between consecutive paths as functions of time
ax = axs[1]
tt = np.linspace(0, min(r[1] for r in res), 800)
def interp(tr, tq):
    return np.stack([np.interp(tq, tr[:, 0], tr[:, 1]), np.interp(tq, tr[:, 0], tr[:, 2])], 1)
ref = interp(res[-1][2], tt)
for (eps, ts, tr), c in zip(res[:-1], cols[:-1]):
    dd = np.hypot(*(interp(tr, tt) - ref).T)
    ax.plot(tt, dd, color=c, lw=1.2, label=f"$\\varepsilon = {eps:g}$")
ax.set_xlabel("time $t$")
ax.set_ylabel("distance to the path for $\\varepsilon = 0.01$")
ax.legend(frameon=False, fontsize=7)
for sp in ["top", "right"]:
    ax.spines[sp].set_visible(False)
ax.set_title("(b) how far apart they are", pad=8)
fig.subplots_adjust(wspace=0.38)
fig.savefig("fig_limit.pdf")


