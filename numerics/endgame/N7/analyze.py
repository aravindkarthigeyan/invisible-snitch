"""N7: analysis of an inward-walk run (npz of inward.py): scale profiles, winding / strain rates, fixed-point test.
Usage: python analyze.py out/in_....npz [plot]"""
import sys, os, json, math
import numpy as np


def load(fn):
    z = np.load(fn, allow_pickle=True)
    cols = [str(c) for c in z['cols']]; c = {k: i for i, k in enumerate(cols)}
    return z, z['rows'], c, json.loads(str(z['summary']))


def derived(rows, c, v, eps):
    R = rows
    L = R[:, c['L']]; D = R[:, c['D']]
    lD = np.log(D)
    head = np.unwrap(R[:, c['heading']]); los = np.unwrap(R[:, c['los']])
    M = R[:, [c['M0'], c['M1'], c['M2'], c['M3']]].reshape(-1, 2, 2); lg = R[:, c['Mlog']]
    thst = math.acos(-v); e0 = np.array([math.cos(thst), -math.sin(thst)])          # arm direction at E at t_0
    Me = M @ e0; nMe = np.hypot(Me[:, 0], Me[:, 1])
    psiE = np.unwrap(np.arctan2(Me[:, 1], Me[:, 0]))                                # tangent at E (outward), transported
    logMe = np.log(nMe) + lg
    logdet = np.log(np.abs(M[:, 0, 0] * M[:, 1, 1] - M[:, 0, 1] * M[:, 1, 0])) + 2 * lg
    # eccentricity: ratio of singular values
    sv = np.linalg.svd(M, compute_uv=False); logecc = np.log(sv[:, 0] / sv[:, 1])
    # theta_E: angle from the direction E -> Harry to the tangent at E
    losEH = los + math.pi
    thE = np.angle(np.exp(1j * (psiE - losEH)))
    out = dict(L=L, D=D, head=head, los=los, psiE=psiE, thE=thE, logMe=logMe, logdet=logdet, logecc=logecc,
               bE=R[:, c['bE']], B=R[:, c['B']], K=R[:, c['K']], Q=R[:, c['Q']], Qmin=R[:, c['Qmin']], Qmax=R[:, c['Qmax']],
               span=R[:, c['span']], tgo=R[:, c['tgo']], Pi=R[:, c['Pi']], sQ=R[:, c['sQ']])
    return out


def rates(d, lo, hi):
    """mean rates per e-fold of D on the window lo < D < hi."""
    m = (d['D'] > lo) & (d['D'] < hi)
    if m.sum() < 3: return None
    x = -np.log(d['D'][m])
    f = lambda y: np.polyfit(x, y[m], 1)[0]
    return dict(q_head=f(d['head']), q_los=f(d['los']), q_psiE=f(d['psiE']), lam1=f(d['logMe']), mu_det=f(d['logdet']),
                ecc=f(d['logecc']), bE=float(np.mean(d['bE'][m])), thE=float(np.mean(d['thE'][m])),
                B=float(np.max(d['B'][m])), K=float(np.mean(d['K'][m])), Q=float(np.max(d['Q'][m])),
                T_over_L=float(np.mean((d['tgo'] / d['L'])[m])), D_over_L=float(np.mean((d['D'] / d['L'])[m])),
                Pi_over_L=float(np.mean((d['Pi'] / d['L'])[m])))


if __name__ == '__main__':
    fn = sys.argv[1]
    z, rows, c, summ = load(fn)
    v = summ['v']; eps = summ['eps']; mu = v / (1 - v)
    d = derived(rows, c, v, eps)
    print(f"# {fn}  v={v} eps={eps}  mu={mu:.5f}")
    print("# window(D)      bE      thE     B      K      supQ   q_head   q_los   q_psiE   lam1   mu_det   ecc_rate  T/L   "
          "| mu_eff=v/(cos bE - v)   sin^2 thE   pred (mu_eff - v)/(mu_eff (2+v))   q_pred=mu_eff sin cos")
    k = 0
    while 10.0 ** (-k - 1) > 30 * eps and k < 130:
        hi = 10.0 ** (-k); lo = 10.0 ** (-k - 1)
        r = rates(d, lo, hi)
        if r and (k < 12 or k % 4 == 0):
            mueff = v / (math.cos(r['bE']) - v)
            s2 = math.sin(r['thE']) ** 2
            pred = (mueff - v) / (mueff * (2 + v))
            print(f"1e-{k+1:<3d}..1e-{k:<3d} {r['bE']:+.4f} {r['thE']:+.4f} {r['B']:.4f} {r['K']:.4f} {r['Q']:.4f} "
                  f"{r['q_head']:+.4f} {r['q_los']:+.4f} {r['q_psiE']:+.4f} {r['lam1']:.4f} {r['mu_det']:.4f} {r['ecc']:+.4f} "
                  f"{r['T_over_L']:.4f} | {mueff:.4f} {s2:.5f} {pred:.5f} {mueff*math.sin(abs(r['thE']))*math.cos(r['thE']):.4f}")
        k += 1
