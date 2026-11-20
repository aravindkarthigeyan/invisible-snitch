"""N8: tables from design-T runs (out/T_v*_e*_D*.npz)."""
import sys, glob, json, math, numpy as np
cols = None
for v in sys.argv[1].split(','):
    print(f"\nv = {v}   mu = {float(v)/(1-float(v)):.4f}   (1-2v)/(1+v) = {(1-2*float(v))/(1+float(v)):.4f}")
    print("| eps | T_total | all seen | s_e=|Y1-X0| | tilt at Y1 | final stretch (L<0.2): sup bearing, sup B, sup K~, sup|Q|, sup time/L | hole: gap/eps, heading change in/out (rad) |")
    fns = sorted(glob.glob(f'out/T_v{v}_e*_D0.1.npz'), key=lambda f: -json.loads(str(np.load(f)['summary']))['eps'])
    for fn in fns:
        z = np.load(fn); s = json.loads(str(z['summary'])); rows = z['rows']; c = {k: i for i, k in enumerate(z['cols'])}
        lab = z['labels']; eps = s['eps']
        iu = int(np.argmin(np.abs(lab - max(s['alpha_s'], 1e-12))))          # index of the upper hole edge node
        n = rows[:, c['n']].astype(int); hd = np.unwrap(rows[:, c['heading']])
        k = int(np.argmin(np.abs(n - (iu + 2))))                 # record where Harry stands on the lower hole edge
        gap = rows[k, c['step']]
        dh_in = hd[k] - hd[max(k - 3, 0)]; dh_out = hd[min(k + 3, len(hd) - 1)] - hd[k]
        prof = z['prof']
        print(f"| {eps:g} | {s['T_total']:.4f} | {s['seen_ok']} | {abs(complex(0)) if False else ''}{s['Delta_e']:.2e} (label) | {prof[0][1]:.1e}@r={prof[0][0]:.0e} | "
              f"{s['final_sup_bE']:.4f}, {s['final_sup_B']:.4f}, {s['final_sup_K']:.5f}, {s['final_supQ']:.4f}, {s['final_sup_time_over_L']:.4f} | {gap/eps:.3g}, {dh_in:+.2e} / {dh_out:+.2e} |")
