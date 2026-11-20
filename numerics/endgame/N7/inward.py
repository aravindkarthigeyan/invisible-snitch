"""N7: the real construction's endgame at depth.  Model (see reports/N7-1.md):
 (i)   left arm at t_0 from the exact formulas, labels alpha in [alpha_s(eps), 2 delta];
 (ii)  Harry: straight along the right arm (heading e^{i theta*}) for tau <= tau1, then the headings of the real
       start-S + C_cut path computed at a coarse eps_c (P6e simulator) up to the entry time (base label 2pi - 2delta);
 (iii) inward walk with the leg rule of C: 'hop' = legs from node to node of the geometric grid (step = fixed fraction of
       the remaining length) while L > blob*eps, then true legs of arclength eps on a refined grid to the end;
       'eps' = true legs of arclength eps from the entry on (validation).
Usage: python inward.py v eps [key=value ...]   keys: g khop nsub tau1 epsc delta mode blob cdep rec noise tag
"""
import sys, os, math, time, json
import numpy as np
from scipy.spatial import ConvexHull
import n7

HERE = os.path.dirname(os.path.abspath(__file__))


def load_path(v, epsc, delta):
    return np.load(os.path.join(HERE, 'out', f'path_v{v}_e{epsc}_d{delta}.npz'))


def diag(arm, u, t, sig_min_fac=4.0, want_profile=False, hull=True):
    """Diagnostics at a leg start: Harry stands on the top node (base); the remaining arc is nodes 0..n-1 (0 = far end E)."""
    v, eps, n = arm.v, arm.eps, arm.n
    X = arm.Y[:n]; p = arm.p
    d = np.diff(X, axis=0); ds = np.hypot(d[:, 0], d[:, 1]); s = np.concatenate([[0.0], np.cumsum(ds)])
    L = s[-1]; D = math.hypot(*p)
    r = X[:-1] - p; rho = np.hypot(r[:, 0], r[:, 1])
    beta = np.arctan2(u[0] * r[:, 1] - u[1] * r[:, 0], u[0] * r[:, 0] + u[1] * r[:, 1])
    out = dict(tgo=0.0, L=L, D=D, n=n, bE=beta[0], bmax=max(0.0, beta.max()), bmin=min(0.0, beta.min()))
    out['B'] = out['bmax'] - out['bmin']
    mid = 0.5 * (X[1:] + X[:-1]) - p; rm = np.hypot(mid[:, 0], mid[:, 1])
    T = d / ds[:, None]
    sphi = (T[:, 0] * mid[:, 1] - T[:, 1] * mid[:, 0]) / rm
    ok = rm >= eps
    out['K'] = float((sphi[ok] ** 2 / rm[ok] * ds[ok]).sum())
    # full K = int T.A T ds over the whole remaining arc from Harry's position on (A = DF, incl. the eps-disc)
    cphi = (T[:, 0] * mid[:, 0] + T[:, 1] * mid[:, 1]) / rm; xx = rm / eps
    tat = np.where(ok, sphi ** 2 / rm, (2 / eps) * (1 - xx) * cphi ** 2 + ((2 - xx) / eps) * sphi ** 2)
    out['Kfull'] = float((tat * ds).sum())
    psi = np.unwrap(np.arctan2(d[:, 1], d[:, 0])); sm = 0.5 * (s[1:] + s[:-1])
    use = sm >= sig_min_fac * eps
    out['span'] = float(psi[use].max() - psi[use].min()) if use.any() else 0.0
    out['psiE'] = float(psi[min(3, len(psi) - 1)]); out['psiB'] = float(psi[-1])
    out['heading'] = math.atan2(u[1], u[0]); out['los'] = math.atan2(-p[1], -p[0])
    # Q = d psi / d log sigma (sigma = arclength from E): window ratio ~1.3 (as P6f) and pointwise
    ls = np.log(np.maximum(sm, 1e-300))
    Qs = 0.0; Qf = 0.0; sQ = 0.0; Qmin = 0.0; Qmax = 0.0
    if use.sum() > 8:
        i0 = int(np.argmax(use))
        lsu = ls[i0:]; psu = psi[i0:]
        grid = np.arange(lsu[0], lsu[-1], 0.02)
        if len(grid) > 16:
            pg = np.interp(grid, lsu, psu)
            w = 13                                           # 13 * 0.02 = log(1.3)
            Qw = (pg[w:] - pg[:-w]) / (0.02 * w)
            Qp = np.gradient(psu, lsu)
            Qs = float(np.abs(Qw).max()); Qf = float(np.abs(Qp[1:-1]).max()) if len(Qp) > 2 else 0.0
            k = int(np.argmax(np.abs(Qw))); sQ = float(math.exp(grid[k] + 0.01 * w) / L)
            Qmin = float(Qw.min()); Qmax = float(Qw.max())
            if want_profile:
                out['profile'] = (np.exp(lsu) / L, psu - psu[0], Qp)
    out.update(Q=Qs, Qfine=Qf, sQ=sQ, Qmin=Qmin, Qmax=Qmax)
    if hull:
        pts = np.vstack([p[None, :], X]) / max(D, L, 1e-300)
        try:
            hp = pts[ConvexHull(pts).vertices]
            out['Pi'] = float(np.hypot(*(hp - np.roll(hp, 1, axis=0)).T).sum() * max(D, L))
        except Exception:
            out['Pi'] = 2 * D
    M, lg = arm.M()
    out['M'] = M.ravel().tolist(); out['Mlog'] = lg
    return out


COLS = ['tgo', 'L', 'D', 'n', 'bE', 'bmax', 'bmin', 'B', 'K', 'span', 'psiE', 'psiB', 'heading', 'los', 'Q', 'Qfine', 'sQ',
        'Qmin', 'Qmax', 'Pi', 'Mlog', 'M0', 'M1', 'M2', 'M3', 'step', 'tau', 'Kfull']


def refine_blob(arm, h):
    """resample the remaining chain (smooth on the scale of its distance from E) to spacing <= h; cubic interpolation;
    the original nodes are kept exactly."""
    n = arm.n; X = arm.Y[:n] + arm.C[:n]
    s = arm.arclen()
    sq = [0.0]; keep = [0]
    for i in range(1, n):
        m = max(1, int(math.ceil((s[i] - s[i - 1]) / h)))
        for a in range(1, m):
            sq.append(s[i - 1] + (s[i] - s[i - 1]) * a / m)
        sq.append(s[i]); keep.append(len(sq) - 1)
    sq = np.array(sq)
    Xn = n7.interp_arc(X, s, sq)
    Xn[np.array(keep)] = X
    arm.Y = np.ascontiguousarray(Xn); arm.C = np.zeros_like(arm.Y); arm.n = len(Xn)
    arm.p = arm.Y[arm.n - 1].copy(); arm.pc[:] = 0


def setup(v, eps, o):
    """phases (i), (ii): returns the arm at the entry time (Harry near the top node), and info."""
    delta = o['delta']
    al, rho0, Y, p0 = n7.arm_nodes_t0(v, eps, 2 * delta, o['g'])
    arm = n7.Arm(v, eps, Y, p0); arm.noise = o['noise']
    thst = math.acos(-v); u0 = np.array([math.cos(thst), math.sin(thst)])
    info = dict(alpha=al, rho0=rho0, Y0=Y.copy())
    if o['epsc'] > 0:
        pth = load_path(v, o['epsc'], delta)
        tau = pth['tau']; uu = pth['u']
        tau1 = o['tau1']
        if tau1 > 0:
            arm.move_geom(u0, tau1, o['cdep'])
        i0 = int(np.searchsorted(tau, tau1, side='right')) - 1
        for i in range(i0, len(uu)):
            a = max(tau[i], tau1); dt = tau[i + 1] - a
            if dt <= 0: continue
            arm.move(np.array([uu[i].real, uu[i].imag]), dt, 0.1 if tau1 > 0 else o['cdep'])
            if tau[i] > 1.0 and math.hypot(*(arm.Y[arm.n - 1] - arm.p)) < o['dentry']:
                break                                # close to the top node: the walk starts with a straight run to it
        info['tau_entry'] = float(tau[-1])
    else:                                           # pure straight-departure model + surrogate detour (testing only)
        arm.move_geom(u0, o['tau1'], o['cdep'])
    info['psi_entry'] = None
    return arm, info


def walk_in(arm, o, rec_prof=()):
    """phase (iii).  Returns rows (array, columns COLS), profiles, summary."""
    v, eps = arm.v, arm.eps
    rows = []; profs = []; t_start = None; taus = []; rowleg = []
    rec = o['rec']; nsub = o['nsub']; khop = o['khop']; blob = o['blob']; mode = o['mode']
    # leg 0: run to the top node
    if not o.get('skip0', 0):
        u, tau, r0, mis = arm.leg(arm.n - 1, nsub)
    t_start = arm.t
    L0 = arm.arclen()[-1]
    prof_L = list(rec_prof); j = 0; maxmis = 0.0; in_blob = False; seen_ok = True
    rng = np.random.default_rng(12345)
    while True:
        n = arm.n; s = arm.arclen(); L = s[-1]
        if L <= eps:
            break
        if (not in_blob) and (mode == 'eps' or L < blob * eps):
            if L < 4 * blob * eps:
                refine_blob(arm, eps / 4); in_blob = True
                n = arm.n; s = arm.arclen(); L = s[-1]
        if mode == 'hop' and not in_blob:
            kt = max(n - 1 - khop, 0); step = L - s[kt]
        else:
            # true leg of C: target at arclength eps from the base (inserted as a node)
            starg = L - eps
            k = int(np.searchsorted(s, starg, side='right')) - 1          # s[k] <= starg < s[k+1]
            X = arm.Y[:n] + arm.C[:n]
            if n >= 4:
                tg = n7.interp_arc(X, s, np.array([starg]))[0]
            else:
                w_ = (starg - s[k]) / (s[k + 1] - s[k]); tg = X[k] + w_ * (X[k + 1] - X[k])
            # every dropped node is within arclength eps of Harry, hence within distance eps: seen
            dd = np.hypot(*(arm.Y[k + 1:n] - arm.p).T)
            if dd.size and dd.max() > eps * (1 + 1e-9): seen_ok = False
            arm.Y[k + 1] = tg; arm.C[k + 1] = 0.0; arm.n = k + 2; n = arm.n; kt = k + 1; step = eps
            # (the base node is replaced by the target; Harry's own position p is kept)
        r = arm.Y[kt] - arm.p; uu = r / math.hypot(*r)
        want = (j % rec == 0) or in_blob and (j % max(1, rec // 4) == 0)
        if want and arm.n >= 4 and not (mode != 'hop' and not in_blob and False):
            # for diag the chain must end at Harry's position: temporarily view nodes 0..kt plus base p
            Ysave = None
            if mode != 'hop' or in_blob:
                # chain = nodes 0..kt (kt = target), base = p : build a temporary arm view
                tmpY = np.vstack([arm.Y[:kt + 1], arm.p[None, :]])
                view = n7.Arm.__new__(n7.Arm); view.__dict__.update(arm.__dict__); view.Y = tmpY; view.n = kt + 2
                dg = diag(view, uu, arm.t, want_profile=bool(prof_L and L <= prof_L[0]), hull=o['hull'])
            else:
                dg = diag(arm, uu, arm.t, want_profile=bool(prof_L and L <= prof_L[0]), hull=o['hull'])
            if 'profile' in dg:
                profs.append((L, ) + dg.pop('profile'))
                while prof_L and L <= prof_L[0]: prof_L.pop(0)
            M = dg.pop('M')
            dg.update(M0=M[0], M1=M[1], M2=M[2], M3=M[3], step=step, tau=0.0)
            rows.append([dg.get(c, np.nan) for c in COLS]); rowleg.append(j)
        if mode != 'hop' or in_blob:
            # legs of the true rule: drop everything above the target
            pass
        u, tau, r0, mis = arm.leg(kt, nsub); taus.append(tau)
        maxmis = max(maxmis, mis / max(r0, 1e-300))
        arm.n = kt + 1
        if arm.noise > 0:
            arm.Y[1:arm.n] *= 1.0 + arm.noise * rng.standard_normal((arm.n - 1, 2))
        j += 1
    tg = np.concatenate([np.cumsum(np.array(taus)[::-1])[::-1], [0.0]])     # time to go at the start of leg j
    T = tg[0]
    rows = np.array(rows); rows[:, 0] = tg[np.array(rowleg)]
    summ = dict(v=v, eps=eps, L0=L0, T=T, T_over_L0=T / L0, legs=j, maxmis=maxmis, seen_ok=seen_ok)
    return rows, profs, summ


def summarize(rows, summ, eps, Lmin_fac=16.0):
    c = {k: i for i, k in enumerate(COLS)}
    ok = rows[:, c['L']] > Lmin_fac * eps
    R = rows[ok]
    tgo = R[:, c['tgo']]; L = R[:, c['L']]; Pi = R[:, c['Pi']]
    with np.errstate(all='ignore'):
        rate = -np.diff(Pi) / np.diff(tgo) if len(R) > 2 else np.array([np.nan])
    out = dict(summ)
    out.update(supQ=float(R[:, c['Q']].max()), supQfine=float(R[:, c['Qfine']].max()),
               sup_bE=float(np.abs(R[:, c['bE']]).max()), sup_B=float(R[:, c['B']].max()),
               sup_K=float(R[:, c['K']].max()), sup_Kfull=float(R[:, c['Kfull']].max()), sup_span=float(R[:, c['span']].max()),
               max_hull_rate=float(np.nanmax(rate)), sup_time_over_L=float((tgo / L).max()),
               winding=float(np.unwrap(R[:, c['heading']])[-1] - R[0, c['heading']]) if len(R) else 0.0)
    return out


def parse(argv):
    o = dict(g=1.02, khop=1, nsub=8, tau1=0.03, epsc=0.001, delta=0.1, mode='hop', blob=64.0, cdep=0.02, rec=1,
             noise=0.0, tag='', hull=1, save=1, dentry=0.01, skip0=0)
    for a in argv:
        k, x = a.split('=')
        o[k] = type(o[k])(x) if not isinstance(o[k], str) else x
    return o


if __name__ == '__main__':
    v = float(sys.argv[1]); eps = float(sys.argv[2]); o = parse(sys.argv[3:])
    t0 = time.time()
    arm, info = setup(v, eps, o)
    t1 = time.time()
    Ldec = [10.0 ** (-k) for k in range(1, 121) if 10.0 ** (-k) > 30 * eps]
    rows, profs, summ = walk_in(arm, o, rec_prof=Ldec)
    out = summarize(rows, summ, eps)
    out.update(secs_setup=round(t1 - t0, 1), secs_walk=round(time.time() - t1, 1), opts=o)
    print(json.dumps(out))
    if o['save']:
        tag = o['tag'] or f"in_v{v}_e{eps:g}_g{o['g']}_k{o['khop']}_{o['mode']}"
        np.savez(os.path.join(HERE, 'out', tag + '.npz'), rows=rows, cols=np.array(COLS),
                 prof_L=np.array([q[0] for q in profs]),
                 **{f'prof{i}': np.array(q[1:]) for i, q in enumerate(profs)}, summary=json.dumps(out))
