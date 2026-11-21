"""Figure: why the start matters.  Harry leaves an end of the front behind him and runs straight away from it.
(a) first contact / corner start: the left-behind arm starts as a straight ray making the angle omega = 2 asin v with
    Harry's backward direction; (b) tangential start: the left-behind arm starts tangent to Harry's path (a parabola
    y = s^2/2 behind him, its first piece of length z0 already seen).
For each case the arm at time t = 1 is shown under three magnifications of a window at its end, all rescaled to the
same size.  True Snitch dynamics (exact straight-run motion, integrated numerically).  Output: fig_hook.pdf"""
import numpy as np
from scipy.integrate import solve_ivp
import snitchsim as s

plt = s.style()
v = 0.2
t_end = 1.0


def flow(z0s, T):
    """true candidates from initial points z0s (complex), Harry at x = t on the real axis; positions at time T."""
    def rhs(t, y):
        n = len(y) // 2
        x = y[:n] - t
        yy = y[n:]
        r = np.hypot(x, yy)
        return np.concatenate([v * x / r, v * yy / r])
    y0 = np.concatenate([z0s.real, z0s.imag])
    sol = solve_ivp(rhs, [0, T], y0, rtol=1e-10, atol=1e-13, method="DOP853")
    n = len(z0s)
    return sol.y[:n, -1] + 1j * sol.y[n:, -1]


def corner_arm(rs, T):
    om = 2 * np.arcsin(v)
    # scale invariance: point at distance r behaves like r * (point at distance 1 at time T/r)
    lam = np.geomspace(T / rs.max() / 2, T / rs.min() * 2, 3000)
    def rhs(t, y):
        r = complex(y[0] - t, y[1])
        w = v * r / abs(r)
        return [w.real, w.imag]
    z1 = np.exp(1j * (np.pi - om))
    sol = solve_ivp(rhs, [0, lam.max()], [z1.real, z1.imag], t_eval=np.concatenate([[0], lam]), rtol=1e-12,
                    atol=1e-14, method="DOP853")
    Zr, Zi = sol.y[0], sol.y[1]
    tl = sol.t
    lt = T / rs
    return rs * (np.interp(lt, tl, Zr) + 1j * np.interp(lt, tl, Zi))


zooms = [1.0, 1e-2, 1e-4, 1e-6]
cols = [s.PRIMARY, (0.25, 0.47, 0.66), (0.45, 0.64, 0.80), (0.66, 0.79, 0.90)]
fig, axs = plt.subplots(1, 2, figsize=(6.8, 2.6))

# (a) corner
rs = np.geomspace(1e-9, 1.5, 4000)
arm = corner_arm(rs, t_end)
end = arm[0]
ax = axs[0]
for zf, c in zip(zooms, cols):
    d = (arm - end)
    k = np.abs(d) <= zf
    w = d[k] / zf
    ax.plot(w.real, w.imag, color=c, lw=1.8, label=((f"$10^{{{int(round(np.log10(zf)))}}}$" if zf < 1 else "$1$")))
ax.plot(0, 0, "o", color="black", ms=3)
ax.set_title("(a) start at first contact (a corner)", pad=3)

# (b) tangential
z0 = 0.03
sgrid = np.concatenate([[0.0], np.geomspace(1e-9, 1.5, 4000)])
init = -(z0 + sgrid) + 1j * 0.5 * (z0 + sgrid) ** 2
fin = flow(init, t_end)
end = fin[0]
ax = axs[1]
for zf, c in zip(zooms, cols):
    d = fin - end
    k = np.abs(d) <= zf
    w = d[k] / zf
    ax.plot(w.real, w.imag, color=c, lw=1.8, label=((f"$10^{{{int(round(np.log10(zf)))}}}$" if zf < 1 else "$1$")))
ax.plot(0, 0, "o", color="black", ms=3)
ax.set_title("(b) tangential touch-down", pad=3)

for ax in axs:
    ax.set_aspect("equal")
    ax.set_xlim(-1.08, 0.12)
    ax.set_ylim(-0.12, 1.02)
    ax.axhline(0, color=s.LIGHT, lw=0.6, zorder=0)
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(s.LIGHT)
    ax.text(0.05, -0.09, "end", fontsize=7.5, color="black")
axs[1].legend(loc="upper right", frameon=False, title="size of zoom window", title_fontsize=7.5, fontsize=7)
axs[0].annotate("", xy=(0.11, 0.0), xytext=(-0.12, 0.0), arrowprops=dict(arrowstyle="-|>", color=s.ACCENT, lw=1.0))
axs[1].annotate("", xy=(0.11, 0.0), xytext=(-0.12, 0.0), arrowprops=dict(arrowstyle="-|>", color=s.ACCENT, lw=1.0))

fig.subplots_adjust(wspace=0.08)
fig.savefig("fig_hook.pdf")




