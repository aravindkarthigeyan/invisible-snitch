"""N7 summary plots: (1) all v: bearing of E and theta_E vs D with the fixed-point prediction; (2) generic last end, omega comparison;
(3) multiprecision vs double."""
import os, math, numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import analyze
runs = [('0.4', '1e-16'), ('0.3', '1e-50'), ('0.2', '1e-50'), ('0.1', '1e-100'), ('0.05', '1e-100'), ('0.02', '1e-140')]
fig, ax = plt.subplots(1, 3, figsize=(19, 5.5))
for v, e in runs:
    fn = f'out/in_v{v}_e{e}_g1.02_k1_hop.npz'
    if not os.path.exists(fn): continue
    z, rows, c, s = analyze.load(fn); vf = float(v); d = analyze.derived(rows, c, vf, float(e))
    m = d['L'] > 16 * float(e); D = d['D'][m]
    ax[0].semilogx(D, np.abs(d['bE'][m]) / vf, label=f'v={v} (eps={e})')
    s2 = np.sin(d['thE'][m]) ** 2; mueff = vf / (np.cos(d['bE'][m]) - vf); pred = (mueff - vf) / (mueff * (2 + vf))
    l, = ax[1].semilogx(D, s2, label=f'v={v}'); ax[1].semilogx(D, pred, '--', color=l.get_color(), lw=0.8)
    ax[2].semilogx(np.exp(-vf * np.log(1 / D)), np.abs(d['bE'][m]) / vf, label=f'v={v}')
ax[0].set_title('|bearing of the far end E from the heading| / v'); ax[0].set_xlabel('D = |Harry - E|'); ax[0].invert_xaxis(); ax[0].legend(fontsize=7)
ax[1].set_title('sin^2(theta_E) (solid) and the fixed-point law (mu_eff - v)/(mu_eff (2+v)) (dashed)'); ax[1].set_xlabel('D'); ax[1].invert_xaxis(); ax[1].set_ylim(0, 0.3); ax[1].legend(fontsize=7)
ax[2].set_title('same as left, against D^v (collapse of the transient for small v)'); ax[2].set_xlabel('D^v'); ax[2].invert_xaxis(); ax[2].set_xscale('linear')
for a in ax: a.grid(alpha=0.3)
fig.tight_layout(); fig.savefig('out/all_v_bearing_fixedpoint.png', dpi=110)
# generic last end
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
for k, v in enumerate(('0.2', '0.1')):
    for om, lab in (('0', 'omega=0 (tangential, strategy b)'), ('0.02', 'omega=0.02'), ('corner', 'omega=2 arcsin v (corner)'), ('1.5708', 'omega=pi/2')):
        fn = f'out/gen_v{v}_e1e-36_om{om}_k1.0_s1.npz'
        if not os.path.exists(fn): continue
        z, rows, c, s = analyze.load(fn)
        m = (rows[:, c['L']] > 1e-30) & (rows[:, c['D']] < 0.1)
        ax[k].loglog(rows[m, c['D']], np.abs(rows[m, c['bE']]) + 1e-18, label=lab)
    ax[k].set_title(f'generic last end (arc, curvature 1), v={v}: |bearing of the far end| on the final inward walk'); ax[k].set_xlabel('D'); ax[k].invert_xaxis()
    ax[k].legend(fontsize=8); ax[k].grid(alpha=0.3); ax[k].set_ylim(1e-12, 1)
fig.tight_layout(); fig.savefig('out/generic_end_omega.png', dpi=110)
# multiprecision vs double
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
for k, (v, e, g) in enumerate((('0.4', '1e-30', '1.1'), ('0.3', '1e-80', '1.15'))):
    fm = f'out/mp_v{v}_e{e}_g{g}.npz'; fd = {'0.4': 'out/in_v0.4_e1e-30_g1.02_k1_hop.npz', '0.3': 'out/in_v0.3_e1e-70_g1.02_k1_hop.npz'}[v]
    if os.path.exists(fd):
        z, rows, c, s = analyze.load(fd); ax[k].semilogx(rows[:, c['D']], np.clip(np.abs(rows[:, c['bE']]), 0, 1), 'r-', lw=0.8, label='double precision, 2 % steps (same model; eps=1e-30 resp. 1e-70): round-off breakdown')
    if os.path.exists(fm):
        r = np.load(fm)['rows']; ax[k].semilogx(r[:, 2], np.abs(r[:, 3]), 'k-', lw=1.5, label='multiprecision (flint acb, 400/500 bits), 10-15 % steps')
    ax[k].set_title(f'v={v}, eps={e}: |bearing of E|'); ax[k].set_xlim(1, float(e) * 1e2); ax[k].set_xlabel('D'); ax[k].legend(fontsize=8); ax[k].grid(alpha=0.3)
fig.tight_layout(); fig.savefig('out/mp_vs_double.png', dpi=110)
