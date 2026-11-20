"""N7: collect summary tables from out/in_v*_e*_g1.02_k1_hop.npz.  python tables.py v1,v2,..."""
import sys, os, glob, json, math, numpy as np
import analyze
vs = sys.argv[1].split(',')
for v in vs:
    fns = glob.glob(f'out/in_v{v}_e*_g1.02_k1_hop.npz')
    recs = []
    for fn in fns:
        z, rows, c, s = analyze.load(fn)
        eps = s['eps']
        d = analyze.derived(rows, c, float(v), eps)
        m = d['L'] > 16 * eps
        hook = m & (d['L'] < 0.1 * s['L0'])
        i = int(np.argmax(np.abs(d['bE']) * m))
        r = dict(eps=eps, T=s['T_over_L0'], tl=s['sup_time_over_L'], Q=s['supQ'], Qhook=float(d['Q'][hook].max()) if hook.any() else float('nan'),
                 bE=s['sup_bE'], B=s['sup_B'], K=s['sup_K'], span=s['sup_span'], rate=s['max_hull_rate'], wind=s['winding'],
                 Dpk=float(d['D'][i]), seen=s['seen_ok'], legs=s['legs'])
        recs.append(r)
    recs.sort(key=lambda r: -r['eps'])
    print(f"\nv = {v}")
    print("| eps | sup|Q| (all; hook part L<L0/10) | sup bearing of E (at D=) | sup sector B | sup K~ | sup span | max hull rate | T/L0; sup_L time/L | winding | all seen |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for r in recs:
        print(f"| {r['eps']:g} | {r['Q']:.4f}; {r['Qhook']:.4f} | {r['bE']:.4f} ({r['Dpk']:.1e}) | {r['B']:.4f} | {r['K']:.5f} | {r['span']:.3f} | {r['rate']:.4f} | {r['T']:.4f}; {r['tl']:.4f} | {r['wind']:.2f} | {r['seen']} |")
    # growth exponents between eps <= 1e-12 runs (least squares of log X vs log(1/eps))
    deep = [r for r in recs if r['eps'] <= 1e-12 and r['Q'] < 2]
    if len(deep) >= 3:
        x = np.log([1 / r['eps'] for r in deep])
        for key in ('Qhook', 'bE', 'B', 'K', 'T'):
            y = np.log([abs(r[key]) for r in deep])
            p, cov = np.polyfit(x, y, 1, cov=True)
            print(f"  growth exponent of sup {key} in 1/eps (eps<=1e-12, {len(deep)} runs): p = {p[0]:+.2e} +- {math.sqrt(cov[0,0]):.1e}")
