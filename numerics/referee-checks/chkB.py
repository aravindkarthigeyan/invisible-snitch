"""High-precision check of Appendix B claims using the exact straight-run integrals.
Design T, d=1.  Run 1: P(t)=t.  Run 2: P(t)=t1+(t-t1) n, n=e^{i beta*}.
"""
import sys
from mpmath import mp, mpf, mpc, cos, sin, tan, atan, acos, exp, log, sqrt, pi, arg, quad, fabs, findroot

mp.dps = 130

def g(beta, v):
    return sin(beta) / tan(beta/2)**v

def gmax(v):
    return g(acos(v), v)

def solve_tau(C, h, v):
    """Solve h = C/2[(1+v)tau^{v-1} - (1-v)tau^{1+v}] for tau>0 (monotone decreasing)."""
    if h > 0:
        u0 = log(((1+v)*C/(2*h)))/(1-v)
    else:
        u0 = log(2*(-h)/((1-v)*C))/(1+v)
    u = u0
    for _ in range(200):
        e1 = exp((v-1)*u); e2 = exp((1+v)*u)
        H = C/2*((1+v)*e1 - (1-v)*e2) - h
        dH = C/2*((1+v)*(v-1)*e1 - (1-v)*(1+v)*e2)
        du = H/dH
        u -= du
        if fabs(du) < mpf(10)**(-mp.dps+10):
            break
    return exp(u)

def pos_from(C, tau, v):
    z = C/2*(tau**(v-1) - tau**(v+1)); y = C*tau**v
    return mpc(z, y)

class Design:
    def __init__(s, v, eps):
        s.v = v = mpf(v); s.eps = eps = mpf(eps)
        s.mu = v/(1-v)
        s.t1 = 2 + s.mu
        s.alpha0 = acos(v + 1/s.t1)
        p0 = s.S1(s.alpha0) - s.t1
        s.rho0 = abs(p0); s.bstar = arg(p0); s.n = exp(mpc(0, 1)*s.bstar)
        s.ta = s.t1 + (s.rho0 - eps)/(1-v)
        s.ttd = s.ta + eps*quad(lambda sg: 1/(1 - v*sg*(2-sg)), [0, 1])
        s.tc = s.t1 + s.rho0/(1-v)
        s.Ptd = s.t1 + (s.ttd - s.t1)*s.n
        s.gm = gmax(v)

    def S1(s, a):
        """True candidate a (0<a<pi) at t1, absolute coords. Lower half by conjugation."""
        v = s.v
        conj = False
        a = a % (2*pi)
        if a > pi:
            a = 2*pi - a; conj = True
        C = g(a, v)
        h1 = cos(a) + v - (1-v*v)*s.t1
        tau = solve_tau(C, h1, v)
        r = pos_from(C, tau, v)
        if conj: r = r.conjugate()
        return s.t1 + r

    def run2(s, th, t):
        """Run-2 frame position r at time t, plus C2,h2(t1), b."""
        v = s.v
        p = (s.S1(th) - s.t1) / s.n
        r1 = abs(p); b = arg(p)
        assert 0 < b < pi, (th, b)
        C2 = r1*g(b, v); h21 = r1*(cos(b) + v)
        ht = h21 - (1-v*v)*(t - s.t1)
        tau = solve_tau(C2, ht, v)
        return pos_from(C2, tau, v), C2, h21, b, r1

    def minrho_run2(s, th):
        v = s.v
        r, C2, h21, b, r1 = s.run2(th, s.ttd)
        btd = arg(r)
        bv = acos(v)
        if b <= bv <= btd:
            return C2/s.gm
        return min(r1, abs(r))

    def tangent_td(s, th, rel=mpf(10)**-25):
        h = rel*abs(th - s.alpha0)
        rp = s.run2(th+h, s.ttd)[0]; rm = s.run2(th-h, s.ttd)[0]
        q = (rp - rm)/(2*h)
        return q  # in heading frame

def run(v, eps, out):
    D = Design(v, eps)
    v = D.v; eps = D.eps; mu = D.mu; muT = 3*v/(1+v)
    pr = lambda *a: print(*a, file=out, flush=True)
    pr(f"\n=== v={float(v)}, eps={mp.nstr(eps,3)} ===")
    pr("alpha0-pi/3 =", mp.nstr(D.alpha0 - pi/3, 5), " rho0=", mp.nstr(D.rho0, 8), " beta*-5pi/6=", mp.nstr(D.bstar-5*pi/6, 5),
       " ttd=", mp.nstr(D.ttd, 10), " omega(ttd)/(v eps/3(1-v)^2)=", mp.nstr((D.tc-D.ttd)/(v*eps/(3*(1-v)**2)), 6))
    # tail: xi_e from C(alpha0 - xi) = eps*gmax
    def Ctail(xi):
        return D.run2(D.alpha0 - xi, D.ttd)[1]
    target = eps*D.gm
    # bisection in log xi
    lo, hi = log(eps/10), log(mpf('0.1'))
    for _ in range(400):
        mid = (lo+hi)/2
        if Ctail(exp(mid)) < target: lo = mid
        else: hi = mid
        if hi-lo < mpf(10)**-30: break
    xie = exp(lo)
    pr("xi_e =", mp.nstr(xie, 6), " xi_e/eps^{1/(2-2v)} =", mp.nstr(xie/eps**(1/(2-2*v)), 6), " xi_e/eps=", mp.nstr(xie/eps, 4))
    # seen set on tail side: min rho over run 2 (true candidate); run 1 has rho>=1/3 there
    for fac in ['1e-6', '0.01', '0.3', '0.7', '0.99', '0.999999', '1.000001', '1.01', '1.5', '3']:
        xi = xie*mpf(fac)
        if xi >= mpf('0.1'): continue
        mr = D.minrho_run2(D.alpha0 - xi)
        pr(f"  tail xi={fac}*xi_e : minrho/eps = {mp.nstr(mr/eps, 8)}  seen={mr <= eps}")
    for fac in ['1e-3', '0.1', '0.4', '0.5', '1', '3', '10']:
        xi = eps*mpf(fac)
        mr = D.minrho_run2(D.alpha0 - xi)
        pr(f"  tail xi={fac}*eps : minrho/eps = {mp.nstr(mr/eps, 8)}  seen={mr <= eps}")
    # forward side: minrho
    for fac in ['0.5', '0.9', '1', '1.2', '2', '4', '10']:
        xi = eps*mpf(fac)
        mr = D.minrho_run2(D.alpha0 + xi)
        pr(f"  fwd  xi={fac}*eps : minrho/eps = {mp.nstr(mr/eps, 8)}  seen={mr <= eps}")
    # (T5): tail end
    rE = D.run2(D.alpha0 - xie, D.ttd)[0]   # heading frame: x0(U)-P(ttd)
    z0 = -rE.real; y0 = -rE.imag
    pr("T5: z0 =", mp.nstr(z0, 6), " z0/eps^{1/(2-2v)}=", mp.nstr(z0/eps**(1/(2-2*v)), 6), " z0/xi_e=", mp.nstr(z0/xie, 6),
       " y0 =", mp.nstr(y0, 5), " |y0|/z0^{2-muT}=", mp.nstr(abs(y0)/z0**(2-muT), 6), " z0/eps=", mp.nstr(z0/eps, 4))
    # forward tilt psi(ttd) vs xi^{1-mu}, true labels (xi >= ~3 eps)
    pr("  forward tilt: xi, psi, |psi|/xi^{1-mu}, |q|")
    for xi in [mpf(10)**k for k in range(-1, int(mp.log10(eps))-1, -3)] + [3*eps, 10*eps]:
        if xi < 3*eps: continue
        q = D.tangent_td(D.alpha0 + xi)
        psi = arg(q)
        pr(f"   xi={mp.nstr(xi,3):>10}  psi={mp.nstr(psi,5):>12}  ratio={mp.nstr(abs(psi)/xi**(1-mu),5):>10}  w={mp.nstr(abs(q),6)}")
    pr("  tail tilt: xi, psi, |psi|/xi^{1-muT}, w")
    for xi in [mpf(10)**k for k in range(-1, int(mp.log10(xie)), -3)] + [2*xie, xie*mpf('1.0001')]:
        if xi < xie: continue
        q = D.tangent_td(D.alpha0 - xi)
        psi = arg(q)
        pr(f"   xi={mp.nstr(xi,3):>10}  psi={mp.nstr(psi,5):>12}  ratio={mp.nstr(abs(psi)/xi**(1-muT),5):>10}  w={mp.nstr(abs(q),6)}")
    # (T2) wrap pairs, endpoint a = 0 (Harry) or forward true label; b tail label.
    # arclength from label to end approximated by summing chords on a geometric grid.
    def arclen(th_from_xi, xi_lo, xi_hi, npts=300):
        L = mpf(0); prev = None
        for k in range(npts+1):
            xi = xi_lo*(xi_hi/xi_lo)**(mpf(k)/npts)
            x = th_from_xi(xi)
            if prev is not None: L += abs(x - prev)
            prev = x
        return L
    xtail = lambda xi: D.run2(D.alpha0 - xi, D.ttd)[0]
    xfwd = lambda xi: D.run2(D.alpha0 + xi, D.ttd)[0]
    pr("  T2 wrap pairs: chord/(u_a+u'_b)")
    worst = mpf(10)
    for xa in [None, 10*eps, mpf(10)**-6, mpf('0.01'), mpf('0.05')]:
        for xbf in ['1.001', '2', '10', '1e3']:
            xb = xie*mpf(xbf)
            if xb > mpf('0.05') or (xa is not None and xa < 3*eps): continue
            ub = arclen(xtail, xie, xb) if xb > xie else mpf(0)
            if xa is None:
                ua = mpf(0); Xa = mpc(0, 0)
            else:
                # arclength from Harry: virtual part ~ chord from 0 to label 3eps, then true
                ua = abs(xfwd(3*eps)) + arclen(xfwd, 3*eps, xa)
                Xa = xfwd(xa)
            Xb = xtail(xb)
            ch = abs(Xa - Xb)
            rat = ch/(ua+ub) if ua+ub > 0 else None
            if rat is not None: worst = min(worst, rat)
            pr(f"   xa={mp.nstr(xa,3) if xa is not None else 'Harry':>8}  xb={xbf}*xi_e  chord={mp.nstr(ch,5)}  ua+u'b={mp.nstr(ua+ub,5)}  ratio={mp.nstr(rat,5) if rat else '-'}")
    pr("  min ratio:", mp.nstr(worst, 5))
    # tangency identity check at one label
    th = D.alpha0 + mpf('0.03'); hh = mpf(10)**-30
    bfun = lambda t: arg((D.S1(t) - D.t1)/D.n)
    db = (bfun(th+hh) - bfun(th-hh))/(2*hh)
    p1 = D.S1(th) - D.t1
    rho1 = abs(p1); beta1 = arg(p1)
    Lam = 2*D.t1*sin(beta1)*sin((th+D.alpha0)/2)/(rho1*sin(th))
    pr("  tangency identity: db/dtheta =", mp.nstr(db, 15), "  Lambda*sin((th-a0)/2) =", mp.nstr(Lam*sin((th-D.alpha0)/2), 15))
    return D, xie

if __name__ == "__main__":
    out = sys.stdout
    for v in ['0.01', '0.04']:
        for eps in ['1e-4', '1e-12', '1e-30']:
            run(v, eps, out)
