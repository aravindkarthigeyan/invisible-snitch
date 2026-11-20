"""N7 Task 4: alternative endgames at depth.  NUMERICAL models.

  python alt.py gen v eps omega [kappa0 sign key=value...]
      "generic last end": a circular arc (curvature kappa0, default 1) left behind by Harry at its end T (unseen part
      from arclength eps), straight departure at wedge angle omega to the backward tangent (omega = 0: tangential =
      strategy (b) 'eat the left arm first, turn around'; omega = 2 arcsin v: the corner; omega = pi/2: perpendicular
      = a reversed walk leaving the front sideways), far detour, return to the outer end, inward walk with rule C.
  python alt.py out v eps phiZ [D0 key=value...]
      P6f's reversed walk on the real arm (phases (i), (ii) of inward.py): from the entry, run to the staging point
      Z = E + D0 R(phiZ) a (a = unit chord E -> top), run straight at E, walk the arm OUTWARD with rule C.
"""
import sys, os, math, json, time
import numpy as np
import n7, inward

HERE = os.path.dirname(os.path.abspath(__file__))


def goto_rel(arm, Z, cstep=0.05):
    """Harry runs (unit speed, 3 straight pieces, re-aimed because E drifts) to the E-centred point Z."""
    for it in range(3):
        dd = Z - arm.p; T = math.hypot(*dd)
        if T < 1e-9: break
        arm.move(dd / T, T * (0.9 if it < 2 else 1.0), cstep)


def gen(v, eps, omega, kappa0=1.0, sign=1.0, o=None, Larm=0.2, s1=0.3):
    g = o['g']
    d0 = 1e-4 * eps ** (1 + 1.5 * v)
    ds = [0.0, d0]
    while eps + ds[-1] < Larm: ds.append(ds[-1] * g)
    ds = np.array(ds); ds[-1] = Larm - eps
    s = eps + ds                                              # arclength from T
    k = kappa0
    amp = (2 / k) * np.sin(k * ds / 2)
    Y = np.stack([amp * np.cos(k * (s + eps) / 2), amp * np.sin(k * (s + eps) / 2)], 1)
    XE = np.array([math.sin(k * eps) / k, (1 - math.cos(k * eps)) / k])
    arm = n7.Arm(v, eps, Y, -XE); arm.noise = o['noise']
    u = -np.array([math.cos(omega), sign * math.sin(omega)])
    arm.move_geom(u, s1, o['cdep'])
    n = arm.n
    for wp in ((-0.15, -0.45), (Larm + 0.35, -0.35)):
        a = arm.Y[n - 1] / math.hypot(*arm.Y[n - 1]); nn = np.array([-a[1], a[0]])
        goto_rel(arm, wp[0] * a + wp[1] * nn)
    tt = arm.Y[n - 1] - arm.Y[n - 4]; tt /= math.hypot(*tt)
    goto_rel(arm, arm.Y[n - 1] + 0.2 * tt)
    rows, profs, summ = inward.walk_in(arm, o, rec_prof=[])
    return rows, summ


def diag_out(arm, ib, kt, u, W, eps):
    """outward walk: base = node ib (Harry), remaining arc = nodes ib..n-1; sigma = W + arclength from the base."""
    n = arm.n; X = arm.Y[ib:n]; p = arm.p
    d = np.diff(X, axis=0); ds = np.hypot(d[:, 0], d[:, 1]); s = np.concatenate([[0.0], np.cumsum(ds)])
    r = X[1:] - p; rho = np.hypot(r[:, 0], r[:, 1])
    beta = np.arctan2(u[0] * r[:, 1] - u[1] * r[:, 0], u[0] * r[:, 0] + u[1] * r[:, 1])
    out = dict(W=W, R=s[-1], bend=beta[-1], B=max(0.0, beta.max()) - min(0.0, beta.min()))
    mid = 0.5 * (X[1:] + X[:-1]) - p; rm = np.hypot(mid[:, 0], mid[:, 1]); T = d / ds[:, None]
    sphi = (T[:, 0] * mid[:, 1] - T[:, 1] * mid[:, 0]) / rm
    ok = (rm >= eps) & (np.arange(len(rm)) >= kt - ib)
    out['K'] = float((sphi[ok] ** 2 / rm[ok] * ds[ok]).sum())
    psi = np.unwrap(np.arctan2(d[:, 1], d[:, 0])); sm = W + 0.5 * (s[1:] + s[:-1])
    out['span'] = float(np.ptp(psi))
    ls = np.log(sm); grid = np.arange(ls[0], ls[-1], 0.02); Q = 0.0
    if len(grid) > 16:
        pg = np.interp(grid, ls, psi); w = 13
        Q = float(np.abs((pg[w:] - pg[:-w]) / (0.02 * w)).max())
    out['Q'] = Q
    out['heading'] = math.atan2(u[1], u[0])
    return out


def walk_out(arm, o):
    v, eps = arm.v, arm.eps
    # refine the part next to E for true eps-legs
    s = arm.arclen(); m = int(np.searchsorted(s, 80 * eps)) + 2
    X = arm.Y[:m] + arm.C[:m]; sq = [0.0]
    for i in range(1, m):
        k = max(1, int(math.ceil((s[i] - s[i - 1]) / (eps / 4))))
        sq.extend([s[i - 1] + (s[i] - s[i - 1]) * a / k for a in range(1, k)]); sq.append(s[i])
    Xn = n7.interp_arc(X, s[:m], np.array(sq))
    Xn = Xn[np.concatenate([[True], np.hypot(*np.diff(Xn, axis=0).T) > 0])]
    arm.Y = np.ascontiguousarray(np.vstack([Xn, arm.Y[m:arm.n]])); arm.C = np.zeros_like(arm.Y); arm.n = len(arm.Y)
    ib = 0; W = 0.0; rows = []; taus = []; j = 0; L0 = arm.arclen()[-1]
    while True:
        n = arm.n
        d = np.diff(arm.Y[ib:n], axis=0); sl = np.concatenate([[0.0], np.cumsum(np.hypot(d[:, 0], d[:, 1]))])
        R = sl[-1]
        if R <= eps: break
        if W < 64 * eps:
            k = int(np.searchsorted(sl, eps, side='right')) - 1            # sl[k] <= eps < sl[k+1]
            w_ = (eps - sl[k]) / (sl[k + 1] - sl[k])
            tg = arm.Y[ib + k] + w_ * (arm.Y[ib + k + 1] - arm.Y[ib + k])
            kt = ib + k; arm.Y[kt] = tg; arm.C[kt] = 0; step = eps
        else:
            kt = min(ib + o['khop'], n - 1); step = sl[kt - ib]
        r = arm.Y[kt] - arm.p; u = r / math.hypot(*r)
        if j % o['rec'] == 0 and n - ib > 6:
            dg = diag_out(arm, ib, kt, u, W, eps); rows.append([dg[c] for c in ('W', 'R', 'bend', 'B', 'K', 'span', 'Q', 'heading')])
        uu, tau, r0, mis = arm.leg(kt, o['nsub']); taus.append(tau)
        ib = kt; W += step; j += 1
    rows = np.array(rows)
    return rows, dict(v=v, eps=eps, L0=L0, T=float(np.sum(taus)), T_over_L0=float(np.sum(taus) / L0), legs=j)


def out(v, eps, phiZ, D0, o):
    arm, info = inward.setup(v, eps, o)
    n = arm.n
    a = arm.Y[n - 1] / math.hypot(*arm.Y[n - 1])
    c, s_ = math.cos(phiZ), math.sin(phiZ)
    Z = D0 * np.array([c * a[0] - s_ * a[1], s_ * a[0] + c * a[1]])        # E-centred staging point (E drifts slowly)
    # psi at entry, for the record
    d = np.diff(arm.Y[:n], axis=0); psi = np.unwrap(np.arctan2(d[:, 1], d[:, 0]))
    turn = psi[min(5, n - 2)] - math.atan2(a[1], a[0])
    goto_rel(arm, Z)
    # straight at E until it is met
    # (pursuit of a radially fleeing target is a straight line; re-aiming every halving only removes round-off)
    while True:
        D = math.hypot(*arm.p)
        if D <= 4 * eps:
            arm.move(-arm.p / D, n7.close_time(D, v, eps), 0.02); break
        arm.move(-arm.p / D, 0.5 * D / (1 - v), 0.02)
    res = math.hypot(*arm.p) / eps
    arm.p[:] = 0; arm.pc[:] = 0
    d = np.diff(arm.Y[:n], axis=0); psi2 = np.unwrap(np.arctan2(d[:, 1], d[:, 0]))
    rows, summ = walk_out(arm, o)
    summ.update(inner_turn_at_entry=float(turn), residual_over_eps=res, span_arrive=float(np.ptp(psi2)))
    return rows, summ


if __name__ == '__main__':
    mode = sys.argv[1]; v = float(sys.argv[2]); eps = float(sys.argv[3])
    pos = [a for a in sys.argv[4:] if '=' not in a]; o = inward.parse([a for a in sys.argv[4:] if '=' in a])
    t0 = time.time()
    if mode == 'gen':
        omega = float(pos[0]) if pos[0] != 'corner' else 2 * math.asin(v)
        kappa0 = float(pos[1]) if len(pos) > 1 else 1.0; sign = float(pos[2]) if len(pos) > 2 else 1.0
        rows, summ = gen(v, eps, omega, kappa0, sign, o)
        outd = inward.summarize(rows, summ, eps); outd.update(omega=omega, kappa0=kappa0, sign=sign, secs=round(time.time() - t0, 1))
        print(json.dumps(outd))
        tag = o['tag'] or f"gen_v{v}_e{eps:g}_om{pos[0]}_k{kappa0}_s{sign:g}"
        np.savez(os.path.join(HERE, 'out', tag + '.npz'), rows=rows, cols=np.array(inward.COLS), summary=json.dumps(outd),
                 prof_L=np.zeros(0))
    else:
        phiZ = float(pos[0]) * math.pi / 180; D0 = float(pos[1]) if len(pos) > 1 else 0.1
        rows, summ = out(v, eps, phiZ, D0, o)
        Wc, R = rows[:, 0], rows[:, 1]
        inner = (R > 0.5 * summ['L0']) & (Wc > 16 * eps)                     # base in the inner half (as P6f)
        summ.update(phiZ_deg=float(pos[0]), D0=D0, supQ=float(rows[inner, 6].max()), sup_bend=float(np.abs(rows[inner, 2]).max()),
                    sup_B=float(rows[inner, 3].max()), sup_K=float(rows[inner, 4].max()), sup_span=float(rows[inner, 5].max()),
                    supQ_all=float(rows[:, 6].max()), secs=round(time.time() - t0, 1))
        deep = (Wc > 16 * eps) & (Wc < 1e-3)
        if deep.any():
            summ.update(deep_supQ=float(rows[deep, 6].max()), deep_bend=float(np.abs(rows[deep, 2]).max()),
                        deep_B=float(rows[deep, 3].max()), deep_K=float(rows[deep, 4].max()))
        print(json.dumps(summ))
        tag = o['tag'] or f"out_v{v}_e{eps:g}_phi{pos[0]}"
        np.savez(os.path.join(HERE, 'out', tag + '.npz'), rows=rows, summary=json.dumps(summ))
