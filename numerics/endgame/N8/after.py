"""N8: design T, tilt profile of the end E_Y left behind: at touch-down, after Harry has walked away W, and at the entry of the
final approach.  Usage: python after.py v eps"""
import sys, math, numpy as np
import designT
vs = sys.argv[1]; eps = float(sys.argv[2])
arm, info = designT.setup(vs, eps, dps=80, verbose=False)
nn = 1 + info['n_near']; sE = abs(info['zE'])
def show(tag):
    X = arm.Y[:nn]; d = np.diff(X, axis=0); ds = np.hypot(*d.T); s = np.cumsum(ds) - 0.5 * ds
    psi = np.unwrap(np.arctan2(d[:, 1], d[:, 0])); dev = psi - psi[0]; out = []
    for r in (1e-3 * sE, 0.1 * sE, sE, 10 * sE, 1e3 * sE, 1e-6, 1e-4, 1e-3):
        if r < 30 * eps or r > s[-2] / 3 or (r >= 1e-6 and r < 1e4 * sE): continue
        if dev[np.searchsorted(s, r)] == 0 or dev[np.searchsorted(s, 3 * r)] == 0: continue
        i = np.searchsorted(s, r); j = np.searchsorted(s, 3 * r)
        out.append(f"r={r:.0e}: {abs(dev[i]):.2e} (a'={math.log(abs(dev[j]/dev[i]))/math.log(s[j]/s[i]):.3f})")
    print(f"{tag:34s} " + "; ".join(out), flush=True)
v = float(vs)
print(f"v={vs} eps={eps:g}: s_e = |E_Y - X0| = {sE:.2e};  mu = {v/(1-v):.4f}, (1-2v)/(1+v) = {(1-2*v)/(1+v):.4f}, 1/(1+v) = {1/(1+v):.4f};  tilt (local exponent)")
show("at touch-down")
W = 0.0; th = [1e-3, 1e-2, 0.1, 1.0]
while True:
    kt = arm.n - 2
    r0 = math.hypot(*(arm.Y[kt] - arm.p)); arm.leg(kt, 8); arm.n = kt + 1; W += r0
    if th and W >= th[0]: show(f"after walking away W={th.pop(0):g}")
    if arm.arclen()[-1] < 0.3:
        show("at the entry of the final approach"); break
