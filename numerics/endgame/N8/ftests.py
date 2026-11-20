"""N8: quantitative tests of the structural claims F1-F4 of L-7 with the deep-scale E-centred simulator (code/N7/n7.py).
Usage: python ftests.py F1|F2|F3gen|DaR [v ...]"""
import sys, os, math, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'N7'))
import n7, inward, alt


def ray_chain(v, eps, omega, s, g=1.02, L=0.3, kappa=0.0, sign=1.0):
    """arc (curvature kappa; straight if 0) starting at tip-distance eps from Harry's initial position T = origin, tangent +x;
    Harry departs straight in the direction -(cos omega, sign sin omega) for the distance s.  Returns arm (E-centred) and r."""
    d0 = 1e-4 * eps ** (1 + 1.5 * v)
    ds = [0.0, d0]
    while eps + ds[-1] < L: ds.append(ds[-1] * g)
    ds = np.array(ds); ds[-1] = L - eps; s_ = eps + ds
    if kappa == 0:
        Y = np.stack([ds, 0 * ds], 1); XE = np.array([eps, 0.0])
    else:
        k = kappa; amp = (2 / k) * np.sin(k * ds / 2)
        Y = np.stack([amp * np.cos(k * (s_ + eps) / 2), amp * np.sin(k * (s_ + eps) / 2)], 1)
        XE = np.array([math.sin(k * eps) / k, (1 - math.cos(k * eps)) / k])
    arm = n7.Arm(v, eps, Y, -XE)
    u = -np.array([math.cos(omega), sign * math.sin(omega)])
    arm.move_geom(u, s, 0.02)
    return arm, ds


def tangents(arm):
    X = arm.Y[:arm.n]; d = np.diff(X, axis=0); dl = np.hypot(d[:, 0], d[:, 1])
    return np.unwrap(np.arctan2(d[:, 1], d[:, 0])), np.cumsum(dl) - 0.5 * dl


def at(x, xs, ys):
    return float(np.interp(math.log(x), np.log(xs), ys))


if __name__ == '__main__':
    what = sys.argv[1]; vs = [float(x) for x in sys.argv[2:]] or [0.3, 0.2, 0.1, 0.05]
    eps = 1e-40
    if what == 'F1':
        print("F1: straight ray left behind at wedge omega (collinear departure at tilt omega), s = 1, eps = 1e-40.")
        print("    rotation of the tangent at t-0 tip distance r, divided by omega; P6c law: tan(rot) ~ c (s/r)^{v/(1+v)}")
        for v in vs:
            for om in (1e-4, 1e-3, 1e-2, 1e-1, 2 * math.asin(v)):
                arm, ds = ray_chain(v, eps, om, 1.0)
                psi, sig = tangents(arm); r0 = np.sqrt(ds[1:] * ds[:-1]) + eps
                rot = psi - 0.0
                row = "  ".join(f"r={r:.0e}: {abs(at(r, r0[1:], rot[1:]))/om:9.3f}" for r in (1e-2, 1e-4, 1e-8, 1e-16, 1e-32))
                e1 = math.log(abs(math.tan(at(1e-6, r0[1:], rot[1:])) / math.tan(at(1e-3, r0[1:], rot[1:])))) / math.log(1e3)
                print(f"v={v} omega={om:.3e}: rot/omega at {row}   | exponent of tan(rot) between r=1e-3 and 1e-6: {e1:.4f} (v/(1+v)={v/(1+v):.4f})"
                      f"  rot at r=1e-36: {abs(at(1e-36, r0[1:], rot[1:])):.4f} rad")
    elif what == 'F2':
        print("F2: straight arc PERPENDICULAR to Harry's departure (transversal departure from the tip), height D = 1, eps = 1e-40.")
        print("    rotation of the tangent at current tip distance y: measured | lead: v(1 - y/sqrt(y^2+D^2)) | exact-integral law v(1+v)(y/(2(1+v)D))^v")
        for v in vs:
            arm, ds = ray_chain(v, eps, math.pi / 2, 1.0)
            psi, sig = tangents(arm)
            # distance from the tip measured perpendicular to Harry's line = along the arc
            for y in (1e-1, 1e-2, 1e-4, 1e-8, 1e-16, 1e-24, 1e-32):
                m = abs(at(y, sig[1:], psi[1:]))
                print(f"v={v} y={y:.0e}: rotation {m:.5f} | {v*(1-y/math.hypot(y,1)):.5f} | {v*(1+v)*(y/(2*(1+v)))**v:.5f}")
            j = np.searchsorted(sig, 1e-10); k = np.searchsorted(sig, 1e-20)
            print(f"   local exponent a' of the rotation between y=1e-20 and 1e-10: {math.log(abs(psi[j]/psi[k]))/math.log(sig[j]/sig[k]):.4f} (v={v})")
    elif what == 'F3gen':
        print("F3 (generic): arc of curvature 1 left TANGENTIALLY from its tip (Harry at tip distance eps on the arc, departs along the")
        print("    backward tangent, s = 0.3): tilt of the tangent relative to the tangent at the tip, local exponent a'; eps = 1e-40")
        for v in vs:
            arm, ds = ray_chain(v, eps, 0.0, 0.3, kappa=1.0)
            psi, sig = tangents(arm); dev = np.abs(psi - psi[0])
            out = []
            for r in (1e-30, 1e-20, 1e-10, 1e-6, 1e-3):
                i = np.searchsorted(sig, r); j = np.searchsorted(sig, 3 * r)
                out.append(f"r={r:.0e}: tilt {dev[i]:.2e}, a'={math.log(dev[j]/dev[i])/math.log(sig[j]/sig[i]):.4f}")
            print(f"v={v}: " + "; ".join(out) + f"   (1/(1+v) = {1/(1+v):.4f}, mu = {v/(1-v):.4f})")
    elif what == 'DaR':
        print("D-a, right tip E_R: Harry walks the LEFT arm outward for t_0-radius D0 (straight, time D0/(1-v)), turns, runs straight at")
        print("    E_R and walks the right arm OUTWARD with rule C.  sup over the outward walk while W < D0 (hooked region): |Q|, bearing of")
        print("    the far end of the 0.2-arm, K~; tangent turn of the arm at arrival between tip and r = D0")
        for v in vs:
            for D0 in (0.05,):
                for e in (1e-6, 1e-12, 1e-24, 1e-36):
                    o = inward.parse(['rec=2'])
                    al, rho0, Y, p0 = n7.arm_nodes_t0(v, e, 0.2, 1.02)
                    arm = n7.Arm(v, e, Y, p0)
                    thst = math.acos(-v); u0 = np.array([math.cos(thst), math.sin(thst)])
                    arm.move_geom(u0, D0 / (1 - v), 0.02)
                    while True:                                   # straight back at E_R (re-aimed against round-off)
                        D = math.hypot(*arm.p)
                        if D <= 4 * e:
                            arm.move(-arm.p / D, n7.close_time(D, v, e), 0.02); break
                        arm.move(-arm.p / D, 0.5 * D / (1 - v), 0.02)
                    arm.p[:] = 0; arm.pc[:] = 0
                    psi, sig = tangents(arm)
                    turn = abs(at(D0, sig[1:], psi[1:]) - psi[1])
                    Qarr = np.abs(np.gradient(psi[5:], np.log(sig[5:])))
                    m = (sig[5:] > 4 * e) & (sig[5:] < D0)
                    rows, summ = alt.walk_out(arm, o)
                    W = rows[:, 0]; w = (W > 16 * e) & (W < D0)
                    print(f"v={v} D0={D0} eps={e:g}: at arrival: turn(tip..D0)={turn:.4f} rad, sup|Q|={Qarr[m].max():.4f}; outward walk: sup|Q|={rows[w,6].max():.4f} "
                          f"sup bearing={np.abs(rows[w,2]).max():.4f} sup K~={rows[w,4].max():.5f} T/L0={summ['T_over_L0']:.4f}", flush=True)
