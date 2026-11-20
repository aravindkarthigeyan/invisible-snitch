"""N7: the same model as inward.py (phases (i)-(iii), hop legs) in multiprecision ball arithmetic (python-flint acb),
ABSOLUTE coordinates, no E-centring, no cancellation tricks.  Purpose: (1) validate the double-precision E-centred
code where both work, (2) show that the breakdown of the double runs at great depth is round-off (noise amplified
by the eccentricity of the linearised flow), not dynamics.
Usage: python mpcheck.py v eps [g=1.1 prec=400 nsub=8 epsc=0.001 tau1=0.03 cdep=0.02 Lstop=200]
"""
import sys, os, math, time, json
import numpy as np
import mpmath as mp
from flint import acb, arb, ctx
import n7, inward

HERE = os.path.dirname(os.path.abspath(__file__))


def to_c(z):
    return complex(float(z.real.mid()), float(z.imag.mid()))


def arm_t0_mp(vs, eps, alpha_top, g, dps):
    """nodes of the left arm at t_0 (same labels as n7.arm_nodes_t0), absolute positions with O = 0, in mpmath."""
    mp.mp.dps = dps
    v = mp.mpf(vs); vf = float(vs)
    a_s = n7.alpha_seen(vf, eps)
    d0fac = 1e-4 * eps ** (1.5 * vf); G = g ** (1.0 / (1 - vf))
    xs = [0.0, d0fac / (1 - vf)]
    while a_s * (1 + xs[-1]) < alpha_top:
        x = xs[-1]; xs.append(x * (g + (G - g) * x / (1 + x)) if x < 1e6 else (1 + x) * G - 1)
    xs[-1] = alpha_top / a_s - 1.0
    thst = mp.acos(-v); sst = mp.sqrt(1 - v * v)
    gf = lambda b: mp.sin(b) / mp.tan(b / 2) ** v
    Z = []
    for x in xs:
        al = mp.mpf(a_s) * (1 + mp.mpf(x))
        Tt = mp.tan(al / 2) ** (1 + v)
        d = mp.mpf(0)
        for _ in range(200):
            dn = mp.asin((Tt * gf(thst + d) + 2 * v * mp.sin(d / 2) ** 2) / sst)
            if abs(dn - d) <= mp.mpf(10) ** (-dps + 5) * abs(dn): d = dn; break
            d = dn
        rho = gf(al) / gf(thst + d)
        Z.append(rho * mp.expj(-(thst + d)))
    return Z, thst


def mp2acb(z, dps):
    return acb(arb(mp.nstr(z.real, dps)), arb(mp.nstr(z.imag, dps)))


def rk4_nodes(Z, n, P0, u, dt, v, skip=-1):
    """nodes x' = v (x - P)/|x - P|, Harry P(t) = P0 + u t, one RK4 step dt (all quantities acb/arb)."""
    h = dt; hv = dt * v; half = arb(0.5)
    P1 = P0 + u * (h * half); P2 = P0 + u * h
    for i in range(n):
        if i == skip: continue
        x = Z[i]
        r = x - P0; k1 = r / abs(r)
        r = x + k1 * (hv * half) - P1; k2 = r / abs(r)
        r = x + k2 * (hv * half) - P1; k3 = r / abs(r)
        r = x + k3 * hv - P2; k4 = r / abs(r)
        Z[i] = (x + (k1 + (k2 + k3) * 2 + k4) * (hv / 6)).mid()     # drop the ball radius (interval wrapping, not error)
    return P2.mid()


def main():
    vs = sys.argv[1]; eps = float(sys.argv[2])
    o = dict(g=1.1, prec=400, nsub=8, epsc=0.001, tau1=0.03, cdep=0.02, Lstop=200.0, delta=0.1, dentry=0.01, tag='')
    for a in sys.argv[3:]:
        k, x = a.split('='); o[k] = type(o[k])(x)
    ctx.prec = o['prec']; dps = int(o['prec'] * 0.30)
    vf = float(vs); v = arb(vs)
    t0 = time.time()
    Zm, thst = arm_t0_mp(vs, eps, 2 * o['delta'], o['g'], dps)
    Z = [mp2acb(z, dps) for z in Zm]; n = len(Z)
    print(f'# v={vs} eps={eps} nodes={n} prec={o["prec"]} bits; setup {time.time()-t0:.0f}s', flush=True)
    P = acb(0); u0 = acb(arb(mp.nstr(mp.cos(thst), dps)), arb(mp.nstr(mp.sin(thst), dps)))
    # (ii-a) straight departure, geometric steps dt = cdep * |P - z_E|
    tau = 0.0
    while tau < o['tau1'] * (1 - 1e-14):
        d = abs(to_c(Z[0] - P)); dt = o['cdep'] * d
        if tau + dt > o['tau1'] or o['tau1'] - (tau + dt) < 0.2 * dt: dt = o['tau1'] - tau
        P = rk4_nodes(Z, n, P, u0, arb(dt), v); tau += dt
    print(f'# departure done {time.time()-t0:.0f}s', flush=True)
    # (ii-b) coarse headings
    pth = inward.load_path(vf, o['epsc'], o['delta']); T = pth['tau']; U = pth['u']
    i0 = int(np.searchsorted(T, o['tau1'], side='right')) - 1
    for i in range(i0, len(U)):
        a = max(T[i], o['tau1']); dt = T[i + 1] - a
        if dt <= 0: continue
        Pc = to_c(P)
        dmin = min(abs(to_c(Z[j]) - Pc) for j in list(range(0, n, max(1, n // 40))) + [n - 1, n - 2, n - 3])
        ns = max(1, int(math.ceil(dt / (0.1 * dmin))))
        uu = acb(float(U[i].real), float(U[i].imag))
        for _ in range(ns):
            P = rk4_nodes(Z, n, P, uu, arb(dt) / ns, v)
        if T[i] > 1.0 and abs(to_c(Z[n - 1] - P)) < o['dentry']: break
    print(f'# entry reached {time.time()-t0:.0f}s', flush=True)
    # (iii) hop walk
    Iv = float(mp.quad(lambda x: 1 / (1 - mp.mpf(vs) * x * (2 - x)), [0, 1]))
    rows = []; taus = []; kt = n - 1; first = True
    while True:
        seg = [to_c(Z[i + 1] - Z[i]) for i in range(n - 1)]
        ds = np.abs(np.array(seg)); s = np.concatenate([[0.0], np.cumsum(ds)]); L = s[-1]
        if not first and (L < o['Lstop'] * eps or n < 12): break
        kt = n - 1 if first else n - 2
        r = Z[kt] - P; r0 = abs(r); u = r / r0; r0f = float(r0.mid())
        tauleg = (r0f - eps) / (1 - vf) + eps * Iv
        if not first:
            # diagnostics at the leg start (Harry on node n-1)
            uc = to_c(u); rel = np.array([to_c(Z[i] - P) for i in range(n - 1)])
            beta = np.angle(rel * np.conj(uc))
            T_ = np.array(seg) / ds; mid = np.array([to_c((Z[i] + Z[i + 1]) * arb(0.5) - P) for i in range(n - 1)])
            sphi = (T_.real * mid.imag - T_.imag * mid.real) / np.abs(mid)
            K = float((sphi ** 2 / np.abs(mid) * ds).sum())
            psi = np.unwrap(np.angle(np.array(seg))); sm = 0.5 * (s[1:] + s[:-1]); use = sm >= 4 * eps
            ls = np.log(sm[use]); grid = np.arange(ls[0], ls[-1], 0.02); Q = 0.0
            if len(grid) > 16:
                pg = np.interp(grid, ls, psi[use]); Q = float(np.abs((pg[13:] - pg[:-13]) / 0.26).max())
            rows.append([0.0, L, abs(rel[0]), beta[0], max(0, beta.max()) - min(0, beta.min()), K, Q, math.atan2(uc.imag, uc.real)])
        dt = arb(tauleg) / o['nsub']
        for _ in range(o['nsub']):
            P = rk4_nodes(Z, kt, P, u, dt, v)          # nodes beyond the target only (the rest is dropped; the target is met exactly)
        Z[kt] = P
        n = kt + 1; taus.append(tauleg); first = False
        if len(taus) % 200 == 0:
            print(f'# leg {len(taus)} L={L:.3e} n={n} bE={rows[-1][3]:+.5f} Q={rows[-1][6]:.5f} rad(P)={float(P.real.rad()):.1e} {time.time()-t0:.0f}s', flush=True)
    rows = np.array(rows); tg = np.cumsum(np.array(taus)[::-1])[::-1]; rows[:, 0] = tg[1:len(rows) + 1]
    tag = o['tag'] or f'mp_v{vs}_e{eps:g}_g{o["g"]}'
    np.savez(os.path.join(HERE, 'out', tag + '.npz'), rows=rows, cols=np.array(['tgo', 'L', 'D', 'bE', 'B', 'K', 'Q', 'heading']))
    m = rows[:, 1] > 16 * eps
    print(json.dumps(dict(v=vf, eps=eps, g=o['g'], prec=o['prec'], legs=len(taus), supQ=float(rows[m, 6].max()),
                          sup_bE=float(np.abs(rows[m, 3]).max()), sup_B=float(rows[m, 4].max()), sup_K=float(rows[m, 5].max()),
                          T_over_L=float((rows[m, 0] / rows[m, 1]).max()), secs=round(time.time() - t0))))
    # plateau table per decade of D
    k = 0
    while 10.0 ** (-k - 1) > rows[-1, 2]:
        w = (rows[:, 2] < 10.0 ** (-k)) & (rows[:, 2] > 10.0 ** (-k - 1))
        if w.sum() > 2 and (k < 6 or k % 4 == 0):
            hd = np.unwrap(rows[:, 7]); q = np.polyfit(-np.log(rows[w, 2]), hd[w], 1)[0]
            print(f'D in 1e-{k+1}..1e-{k}: bE={rows[w,3].mean():+.5f} B={rows[w,4].max():.5f} K={rows[w,5].mean():.5f} supQ={rows[w,6].max():.5f} q_head={q:+.5f} T/L={(rows[w,0]/rows[w,1]).mean():.5f}')
        k += 1


if __name__ == '__main__':
    main()
