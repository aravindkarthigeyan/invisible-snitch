"""N7 plots: python plots.py v eps1,eps2,...  (uses out/in_v{v}_e{eps}_g1.02_k1_hop.npz)"""
import sys, os, math, numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import analyze
v = float(sys.argv[1]); epss = sys.argv[2].split(',')
suffix = sys.argv[3] if len(sys.argv) > 3 else '_g1.02_k1_hop'
fig, ax = plt.subplots(2, 3, figsize=(17, 9))
for e in epss:
    fn = f'out/in_v{v}_e{e}{suffix}.npz'
    if not os.path.exists(fn): continue
    z, rows, c, summ = analyze.load(fn); d = analyze.derived(rows, c, v, float(e))
    m = d['L'] > 16 * float(e)
    D = d['D'][m]
    ax[0, 0].semilogx(D, np.abs(d['bE'][m]), label=f'eps={e}')
    ax[0, 1].semilogx(D, d['Q'][m], label=f'eps={e}')
    ax[0, 2].semilogx(D, d['K'][m])
    ax[1, 0].semilogx(D, d['B'][m])
    x = -np.log(D); q = np.gradient(d['head'][m], x)
    ax[1, 1].semilogx(D, q)
    ax[1, 2].semilogx(D, (d['tgo'] / d['L'])[m])
for a, t in zip(ax.ravel(), ['|bearing of far end E from heading| (rad)', 'sup|Q| over remaining arc (sigma>=4eps), window 1.3',
                             'K~ = int sin^2(phi)/rho ds over the remaining arc', 'sector opening B of the remainder at Harry (rad)',
                             'winding rate of the heading, d(heading)/d log(1/D)', '(time to finish)/L']):
    a.set_title(t, fontsize=10); a.set_xlabel('D = |Harry - E|'); a.grid(alpha=0.3); a.invert_xaxis()
ax[0, 0].legend(fontsize=7)
fig.suptitle(f'N7 inward walk (construction C on the left arm), v={v}: universal curves; each eps only cuts the curve off', fontsize=12)
fig.tight_layout(); fig.savefig(f'out/inward_v{v}.png', dpi=110)
# Q profiles
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
fn = f'out/in_v{v}_e{epss[-1]}{suffix}.npz'
z, rows, c, summ = analyze.load(fn)
PL = z['prof_L']
for i in range(0, len(PL), max(1, len(PL) // 12)):
    pr = z[f'prof{i}']
    ax[0].semilogx(pr[0], pr[2], label=f'L={PL[i]:.0e}', lw=0.8)
    ax[1].semilogx(pr[0], pr[1], label=f'L={PL[i]:.0e}', lw=0.8)
ax[0].set_xlim(1e-8, 1.2); ax[1].set_xlim(1e-8, 1.2); ax[0].set_ylim(-0.6, 0.6)
ax[0].set_title(f'Q = d psi/d log sigma of the remaining arc vs sigma/L, v={v}, eps={epss[-1]}'); ax[0].legend(fontsize=6)
ax[1].set_title('tangent angle psi(sigma) - psi(E)'); ax[0].grid(alpha=0.3); ax[1].grid(alpha=0.3)
fig.tight_layout(); fig.savefig(f'out/Qprofile_v{v}.png', dpi=110)
