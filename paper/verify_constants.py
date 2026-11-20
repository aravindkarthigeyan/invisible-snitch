"""verify_constants.py -- constants and side conditions of the paper
"A path fixed in advance that finds a slow fleeing point" (Appendix A).

Standalone: Python 3 with mpmath and numpy, 50 significant digits.  Run from the directory of this file:

    python -I verify_constants.py

Inputs are the PRINTED numbers of Appendix A (dict INPUTS below, exactly as printed).  The script
  1. computes certified upper bounds for the near-pair constant D' (Definition 4.x, Lemma "evaluation") of the main
     tuple p and the stage-A tuple p_A, by an outward-rounded evaluation of the cell scheme (constants in mpmath.iv,
     arrays in IEEE float64 rounded outward after every operation, sums of non-negative terms inflated by 1+1e-11),
     and checks that they do not exceed the printed values of D' used in (P6);
  2. evaluates the touch-down constants of Definition 7.1 at (vbar, eta, epsbar, xi1, lambda0, G_T), checks the side
     conditions (SC1)-(SC48) (and four further inequalities on this row), and checks that every touch-down constant used
     downstream is printed on the safe side of its exact value;
  3. evaluates the derived constants of the end theorem (Definition 3.3, with the function C of (S1G), Section 8) for
     the main tuple p (U0 = U_max) and the stage-A tuple p_A (gamma -> gamma_D, U0 = U_A), and checks (P0)-(P8) and
     (C1)-(C6);
  4. evaluates the assembly constants of Section 8.1 (heading Lemma 5.1, departure Theorem 5.2, (TS), T_0^sharp) and
     checks (A2)-(A7);
  5. checks further elementary inequalities;
  6. writes appA_tables.tex (Tables A.1-A.4) and verify_constants.out (full log: every condition with both sides and
     its relative slack, and all constants).
The downstream computations use the PRINTED (outward-rounded) touch-down constants and the PRINTED D', never the
exact values.  Exit status 0 iff every condition holds.  The final line is "ALL <n> CONDITIONS HOLD".
"""
import math
import os
import sys
import time
from collections import OrderedDict

import mpmath as mp
import numpy as np
from mpmath import iv

mp.mp.dps = 50
M = mp.mpf
sin, cos, tan, asin, acos = mp.sin, mp.cos, mp.tan, mp.asin, mp.acos
sqrt, pi, exp, log = mp.sqrt, mp.pi, mp.exp, mp.log
HERE = os.path.dirname(os.path.abspath(__file__))

# =====================================================================================================================
# Section 1. INPUTS: the printed numbers of Appendix A (strings exactly as printed).
# =====================================================================================================================
INPUT_SETS = OrderedDict()
INPUT_SETS['S1G'] = OrderedDict([
    ('v0', '5.8e-3'),
    ('epsS', '4e-11'),
    ('T0', '13.1'),
    ('vbar', '5.8e-3'),
    ('eta', '0.11639'),
    ('epsbar', '1e-3'),
    ('xi1', '1.16171'),
    ('lam0', '0.0337254'),
    ('GT', '0.030573'),
    ('T2', '3.77231'),
    ('Umax', '7.17768'),
    ('csep', '0.0276152'),
    ('kc', '0.951517'),
    ('cN', '3.41207'),
    ('muTb', '0.0172997'),
    ('mub', '0.00583384'),
    ('ap', '0.9827002'),
    ('thv', '1.153'),
    ('cT4', '1.12275'),
    ('czlo', '1.20086'),
    ('czhi', '1.67043'),
    ('cy', '0.697925'),
    ('WxL', '1.22122'),
    ('gam', '0.50164'),
    ('R', '0.00139765'),
    ('m', '0.142162'),
    ('s0', '0.276635'),
    ('kap', '1.2897'),
    ('cA', '0.997991'),
    ('KR', '9.21786'),
    ('Kf', '8.20966'),
    ('Keps', '137.074'),
    ('eta1', '0.887055'),
    ('qc', '2.30668'),
    ('dL', '1.0058339'),
    ('delta1', '1.0117361'),
    ('nu', '0.0107665'),
    ('A0', '1.129899'),
    ('fF', '0.500225'),
    ('gD', '0.535633'),
    ('omb', '0.421626'),
    ('ck', '1.01239'),
    ('d0fac', '0.251113'),
    ('Dp', '63.068'),
    ('DpA', '64.6357'),
])
USE_S1G = {'S1G': True}

# =====================================================================================================================
# condition bookkeeping
# =====================================================================================================================
CONDS = []   # (group, tex, left, rel, right)
I = {}


def cond(group, tex, left, rel, right):
    CONDS.append((group, tex, M(left), rel, M(right)))


def holds(left, rel, right):
    return {'<': left < right, '<=': left <= right, '>': left > right, '>=': left >= right}[rel]


def slack(left, rel, right):
    big, small = (right, left) if rel in ('<', '<=') else (left, right)
    if big == 0:
        return big - small
    return (big - small) / abs(big)


# =====================================================================================================================
# Section 2. touchdown(): Definition 7.1, (SC1)-(SC48), four further inequalities on the row, and W_x Lhat
# =====================================================================================================================
def touchdown(vbar, eta, eb, xi1, lam0, G):
    v = vbar
    mu = v / (1 - v)
    muT = 3 * v / (1 + v)
    K = OrderedDict()
    SC = []

    def sc(n, tex, left, rel, right):
        SC.append((('(SC%s)' % n) if n else '', tex, M(left), rel, M(right)))

    half = M(1) / 2
    t1b = 2 + mu
    gb = sqrt(1 - v * v) * ((1 + v) / (1 - v)) ** (v / 2)
    alo = acos(half + v)
    Da = pi / 3 - alo
    d1 = v * t1b + mu
    erho = v * t1b + Da + mu
    T2 = t1b + (sqrt(3) + erho) / (1 - v)
    ds = v * T2
    dP = max(mu, ds + Da)
    K.update(mub=mu, muTb=muT, t1b=t1b, gb=gb, alo=alo, Da=Da, d1=d1, erho=erho, T2=T2, ds=ds, dP=dP)
    W1 = lambda rho: exp(v * t1b / rho)
    om1 = lambda rho: v * t1b / (2 * rho)
    vk = lambda rho: (2 / rho + 1 / rho ** 2) * v * t1b * exp(2 * v * t1b / rho)
    rhomid = sin(half)
    karm = (1 + v) / (cos(half) - v) + 2 * v / (1 - v * v)
    darm = (1 + v) / ((1 - v) * (cos(half) - v)) + v / (1 - v * v)
    e1 = (2 - cos(half)) * (1 + tan(M(1) / 4) ** 2) + (1 + v) * tan(M(1) / 4) ** (1 - v)
    E1 = max(M(1), e1 / (1 - v))
    Warm = E1 ** v / (1 - v)
    kall = max(karm, 1 + vk(rhomid))
    Wall = max(Warm, W1(rhomid) * (pi / 2) ** (2 * v))
    K.update(rhomid=rhomid, karm=karm, darm=darm, e1=e1, E1=E1, Warm=Warm, kall=kall, Wall=Wall)
    thL = alo - eta
    thR = pi / 3 + eta
    R0 = lambda th: sqrt(5 - 4 * cos(th))
    s_ = lambda th: 2 * sin(th) / (5 - 4 * cos(th))
    RL, RR = R0(thL), R0(thR)
    rmin, rmax = RL - d1, RR + d1
    rhow = sin(thL)
    Ww, omw, vkw = W1(rhow), om1(rhow), vk(rhow)
    iotaw = 1 + v * t1b / sin(thL)
    qmin = sin(alo + eta / 2) / RR
    qmax = sin(pi / 3 - eta / 2) / RL
    ellmin = 4 * qmin / (1 + d1 / RL)
    ellmax = 2 * t1b * iotaw * qmax / (1 - d1 / RL)
    Lmin = 4 * sin(alo - eta / 2) / rmax ** 2
    Lmax = 2 * t1b * iotaw * sin(pi / 3 + eta / 2) / rmin ** 2
    m0 = max(abs(1 - 2 * cos(thL)), abs(1 - 2 * cos(thR))) / RL
    omp = asin(d1 / RL)
    angw = asin(m0) + omw + omp
    Amin, Amax = cos(angw), Ww
    blo = Lmin * (1 - eta ** 2 / 48) / 4
    bhi = Lmax / 4
    bbar = bhi * eta ** 2
    etau = tan(bbar / 2) / (bbar / 2) - 1
    beta2 = bhi * (1 + etau) / 2
    Chi = 2 * rmax * beta2 ** (1 - v)
    Clo = 2 * rmin * (blo / 2) / (1 + tan(bbar / 2) ** 2)
    aux = ellmax * bbar * eta / 2
    amin = Amin * cos(bbar) - aux
    amax = Amax * (1 + v) + aux
    LC = 2 * Lmax / Lmin + eta * Amax / rmin
    Llo = 2 * (cos(bbar) - v) * (Lmin / Lmax) * (1 - eta ** 2 / 32)
    S1 = ellmax * (rmax * amax * LC + (1 + v) * eta) / (2 * (1 - v * v) * rmin)
    K.update(thL=thL, thR=thR, RL=RL, RR=RR, rmin=rmin, rmax=rmax, rhow=rhow, Ww=Ww, omw=omw, vkw=vkw,
             iotaw=iotaw, qmin=qmin, qmax=qmax, ellmin=ellmin, ellmax=ellmax, Lmin=Lmin, Lmax=Lmax, m0=m0, omp=omp,
             angw=angw, Amin=Amin, Amax=Amax, blo=blo, bhi=bhi, bbar=bbar, etau=etau, beta2=beta2, Chi=Chi,
             Clo=Clo, aux=aux, amin=amin, amax=amax, LC=LC, Llo=Llo, S1=S1)
    hf = Amin - rmax * bhi ** 2 * eta ** 3 / 2
    rhoc = hf / (1 + v)
    Q = (1 + v) * rmax / hf
    yf = 2 * rmax * beta2
    Y1 = (ellmax / 2 + Amax * bhi * (1 + etau) * eta) / amin
    Ybar = Y1 * eta ** (1 - mu) * Q ** mu
    thf = max((1 + v) * Y1, v * yf / rhoc) / (1 - v - v * Ybar)
    Wf = amax * sqrt((1 + v + v * Ybar) ** 2 + ((1 + v) * Ybar + v) ** 2) / (1 - v * v)
    dfw = v / (3 * (1 - v) ** 2 * xi1)
    tauf = beta2 * Q ** (1 + mu)
    taufb = tauf * eta ** (1 - mu)
    rhou = ((1 + v) * Amax + dfw) / (1 - 2 * taufb ** 2)
    S2 = (2 * tauf + thf * Q ** mu) * (rhou * amax * LC + 1 + v) / ((1 - v * v) * rhoc)
    kf = Q ** mu * (1 + vkw + S1 * v) + S2 * v
    K.update(hf=hf, rhoc=rhoc, Q=Q, yf=yf, Y1=Y1, Ybar=Ybar, thf=thf, Wf=Wf, dfw=dfw, tauf=tauf, taufb=taufb,
             rhou=rhou, S2=S2, kf=kf)
    thv = Q ** mu * exp(mu) * (thf + mu * exp(2 * mu) * yf * xi1)
    Wv = Wf * exp(2 * mu)
    uv = Wv * xi1
    K.update(thv=thv, Wv=Wv, uv=uv)
    xim = Chi ** (-half)
    xip = (gb / Clo) ** (1 / (2 - 2 * v))
    xeb = xip * sqrt(eb)
    dtl = (1 + v) * v / (3 * (1 - v) * xim)
    ht = Amin - dtl
    hT = (1 + v) * Amax + rmax * bhi ** 2 * eta ** 3 / 2
    mtau = (2 * ht / Chi) * eta ** (-(1 - 2 * v))
    taut = mtau ** (1 / (1 + v))
    et = (1 + v) / (mtau * taut ** (1 - v))
    yc = 2 * (1 + et) * hT / (1 - v)
    yT = Chi ** (1 / (1 + v)) * max(M(1), yc) ** v
    Tt = (max(M(1), yc / Clo) * 2 / blo) ** v
    Y2 = Tt * ellmax / (2 * amin)
    Y2b = Y2 * eta ** (1 - muT)
    tht = Y2 + v * yT / ht
    zT = (hT + v * yT * eta ** (1 - muT)) / (1 - v)
    rhoT = zT * sqrt(1 + (yT * eta ** (1 - muT) / ht) ** 2)
    Wt = amax * sqrt((1 + v + v * Y2b) ** 2 + ((1 + v) * Y2b + v) ** 2) / (1 - v * v)
    S3 = (yT / ht + tht) * (rhoT * amax * LC + 1 + v) / ((1 - v * v) * ht)
    kt = Tt * (1 + vkw + S1 * v) + S3 * v
    xi2 = 1 / (3 * (1 - v) * Amin)
    ha = 1 - Amax / 2 - rmax * bhi ** 2 * eb ** 3 / 32
    Qa = (1 + v) * rmax / ha
    taua = beta2 * Qa ** (1 + mu) * eb ** (1 - mu) / 4
    K.update(xim=xim, xip=xip, xeb=xeb, dtl=dtl, ht=ht, hT=hT, mtau=mtau, taut=taut, et=et, yc=yc, yT=yT, Tt=Tt,
             Y2=Y2, Y2b=Y2b, tht=tht, zT=zT, rhoT=rhoT, Wt=Wt, S3=S3, kt=kt, xi2=xi2, ha=ha, Qa=Qa, taua=taua)
    ebeta = asin(erho / sqrt(3))
    bl = blo * eta ** 2
    yb = sin(bl)
    Hb = 3 + d1 + (1 + v) * (sqrt(3) + erho) / (1 - v)
    Tb = 2 * Hb / (yb * tan(bl / 2))
    Sb = (3 + v) / (2 * (1 - v) * yb)
    kb = Tb ** v * (kall + Sb * v) + Sb * v
    Wb = (1 + v) / (1 - v) * Tb ** v
    rB = M('0.005') + v * t1b
    rhoh = half - dP - rB - v * T2
    K.update(ebeta=ebeta, bl=bl, yb=yb, Hb=Hb, Tb=Tb, Sb=Sb, kb=kb, Wb=Wb, rB=rB, rhoh=rhoh)
    Wx = max(Wv, Wt, Wb * Wall)
    Umax = (Wv + Wt) * eta + Wb * Wall * (2 * pi - 2 * eta) / (1 - 2 * v)
    Lhat = (8 / lam0) ** (2 * v) / (1 - 2 * v)
    D0 = lam0 / (Wx * Lhat)
    csep = 2 * sin(D0 / 2)
    kc = min(cos(thv * D0 ** (1 - mu)), ht / Wt)
    kstar = max(kf * Wv ** mu, kt * Wt ** muT, kb)
    cfar = kstar / sqrt(12)
    cnear = thv * sqrt((12 * uv ** 2 + 6 * uv + 1) / (3 - 2 * mu))
    ctail = tht * sqrt(19 / (3 - 2 * muT))
    cN = max(cfar, cnear, ctail)
    cy = yT / ht ** 2
    cT4 = tht / ht
    K.update(Wx=Wx, Umax=Umax, Lhat=Lhat, D0=D0, csep=csep, kc=kc, kstar=kstar, cfar=cfar, cnear=cnear,
             ctail=ctail, cN=cN, cy=cy, cT4=cT4, czlo=ht * xim, czhi=zT * xip, WxL=Wx * Lhat)
    vb, eB = r'\vbar', r'\epsbar'
    sc(1, r'$\sqrt3-e_\rho>%s$' % eB, sqrt(3) - erho, '>', eb)
    sc(2, r'$\cos\frac12>%s$' % vb, cos(half), '>', v)
    sc(3, r'$\theta_L\ge\frac12$', thL, '>=', half)
    sc(4, r'$\theta_R\le\pi/2$', thR, '<=', pi / 2)
    sc(5, r'$\eta\le\pi/3$', eta, '<=', pi / 3)
    sc(6, r'$\cos\theta_L<4/5$', cos(thL), '<', M(4) / 5)
    sc(7, r'$\frac12\cot(\underline\alpha-\eta/2)<s(\theta_R)$', 1 / tan(alo - eta / 2) / 2, '<', s_(thR))
    sc(8, r'$d_1<R_L$', d1, '<', RL)
    sc(9, r'$\angle_{\mathrm w}<\pi/2$', angw, '<', pi / 2)
    sc(10, r'$\bar b<\pi/2$', bbar, '<', pi / 2)
    sc(11, r'$\beta_2<1$', beta2, '<', 1)
    sc(12, r'$b_{\mathrm{lo}}<2$', blo, '<', 2)
    sc(13, r'$\sa_{\min}>0$', amin, '>', 0)
    sc(14, r'$\cos\bar b>%s$' % vb, cos(bbar), '>', v)
    sc(15, r'$L_{\mathrm{lo}}>\eta\sA_{\max}/\sr_{\min}$', Llo, '>', eta * Amax / rmin)
    sc('16a', r'$h_{\mathrm f}>0$', hf, '>', 0)
    sc('16b', r'$h_{\mathrm f}\le1-%s^2$' % vb, hf, '<=', 1 - v * v)
    sc(17, r'$\rho_{\mathrm c}\xi_1>1$', rhoc * xi1, '>', 1)
    sc(18, r'$Q\ge1$', Q, '>=', 1)
    sc(19, r'$1-%s-%s\bar Y>0$' % (vb, vb), 1 - v - v * Ybar, '>', 0)
    sc(20, r'$1-2\bar\tau_{\mathrm f}^2>%s$' % vb, 1 - 2 * taufb ** 2, '>', v)
    sc(21, r'$C_{\mathrm{hi}}<1$', Chi, '<', 1)
    sc(22, r'$C_{\mathrm{lo}}\eta^2>%s\gb$' % eB, Clo * eta ** 2, '>', eb * gb)
    sc(23, r'$\gb>C_{\mathrm{lo}}$', gb, '>', Clo)
    sc(24, r'$\bar\xi_{\mathrm e}<\eta$', xeb, '<', eta)
    sc(25, r'$h_{\mathrm t}>0$', ht, '>', 0)
    sc(26, r'$m_\tau>1$', mtau, '>', 1)
    sc(27, r'$\xi_2%s\le\frac12$' % vb, xi2 * v, '<=', half)
    sc(28, r'$\xi_-\ge\frac12$', xim, '>=', half)
    sc(29, r'$h_{\mathrm a}>0$', ha, '>', 0)
    sc(30, r'$1-2\tau_{\mathrm a}^2>0$', 1 - 2 * taua ** 2, '>', 0)
    sc(31, r'$\sA_{\min}>4\tau_{\mathrm a}^2$', Amin, '>', 4 * taua ** 2)
    sc(32, r'$b_{\mathrm l}\le\pi/6-e_\beta$', bl, '<=', pi / 6 - ebeta)
    sc(33, r'$\pi/3+2e_\beta\le\pi-b_{\mathrm l}$', pi / 3 + 2 * ebeta, '<=', pi - bl)
    sc(34, r'$T_{\mathrm b}\ge1$', Tb, '>=', 1)
    sc(35, r'$%s\le\frac1{10}$' % vb, v, '<=', M(1) / 10)
    sc(36, r'$\rho_{\mathrm h}>0$', rhoh, '>', 0)
    sc('37a', r'$2\gb%s<\theta_L$' % eB, 2 * gb * eb, '<', thL)
    sc('37b', r'$\gb%s\le1$' % eB, gb * eb, '<=', 1)
    sc(38, r'$2-2d_{\mathrm s}\ge1$', 2 - 2 * ds, '>=', 1)
    sc(39, r'$2\lambda_0+\min(\bar\xi_{\mathrm e},\lambda_0)\le\eta$', 2 * lam0 + min(xeb, lam0), '<=', eta)
    sc(40, r'$2u_{\mathrm v}%s\le\eta$' % eB, 2 * uv * eb, '<=', eta)
    sc(41, r'$W_x\hat L\le2$', Wx * Lhat, '<=', 2)
    sc(42, r'$\Delta_0\le\eta$', D0, '<=', eta)
    sc(43, r'$c_{\mathrm{sep}}>2%s$' % eB, csep, '>', 2 * eb)
    sc(44, r'$\theta_{\mathrm v}\Delta_0^{1-\mub}\le\pi/2$', thv * D0 ** (1 - mu), '<=', pi / 2)
    sc(45, r'$k_*\lambda_0^{1-\muTb}\le\pi$', kstar * lam0 ** (1 - muT), '<=', pi)
    sc(46, r'$u_{\mathrm v}\ge\frac12$', uv, '>=', half)
    sc('47a', r'$G_{\mathrm T}>0$', G, '>', 0)
    sc('47b', r'$\bar\xi_{\mathrm e}+G_{\mathrm T}\le\eta$', xeb + G, '<=', eta)
    sc('48a', r'$z_{\mathrm T}\bar\xi_{\mathrm e}+%s<1$' % eB, zT * xeb + eb, '<', 1)
    sc('48b', r'$G_{\mathrm T}+z_{\mathrm T}\bar\xi_{\mathrm e}\le1$', G + zT * xeb, '<=', 1)
    # four further inequalities on the row (not used in the proofs; checked for completeness)
    sc('', r'$\lambda_0\le\frac14$', lam0, '<=', M(1) / 4)
    sc('', r'$\kc\ge\frac12$', kc, '>=', half)
    sc('', r'$c_N\lambda_0^{1-\muTb}\le1$', cN * lam0 ** (1 - muT), '<=', 1)
    sc('', r'$\vbar\le2\cdot10^{-2}$', v, '<=', M('0.02'))
    return K, SC


# touch-down constants used downstream: (key, INPUTS key, direction)
TD_USED = [('T2', 'T2', 'up'), ('Umax', 'Umax', 'up'), ('csep', 'csep', 'down'), ('kc', 'kc', 'down'),
           ('cN', 'cN', 'up'), ('muTb', 'muTb', 'up'), ('mub', 'mub', 'up'), ('thv', 'thv', 'up'),
           ('cT4', 'cT4', 'up'), ('czlo', 'czlo', 'down'), ('czhi', 'czhi', 'up'), ('cy', 'cy', 'up'),
           ('WxL', 'WxL', 'up')]


# =====================================================================================================================
# Section 3. tilt constants, far-pair integrals J_k, core(p, U0)  (Definition 3.3)
# =====================================================================================================================
def aD(K):
    return 1 + 1 / K + 2 / K ** 2


def aDs(K):
    """aD*(K) of Lemma 2.x (far inequality) and the Duhamel lemma"""
    return 1 + 1 / (pi * K) + 2 / (pi ** 2 * K ** 2)


def tiltc(gam, kap, cA, m, qc):
    """Definition 3.3: C_T = omega_* max(sigma_q s(q), s(2q/(q-1))), C_mu = 1 + kappa C_T^2."""
    sfun = lambda r: sqrt(kap) / cA * (r / 2 if r <= 2 else sqrt(r - 1))
    sq = 1 / (1 - qc ** (-gam))
    r2 = 2 * qc / (qc - 1)
    rstar = max(qc, r2)
    arg = 1 - m ** 2 * rstar / (4 * cA)
    CT = max(sq * sfun(qc), sfun(r2)) / sqrt(arg) if arg > 0 else M(10) ** 30
    return CT, 1 + kap * CT ** 2, rstar


def sin_piece_int(k, u, w, W, s, N):
    """UPPER bound (lower=True: LOWER bound) of int_u^w (2 sin(y/(2W)) - s)^{-k} dy, 0 <= u < w <= pi W; the integrand
    is positive and non-increasing, so the left- (right-) endpoint Riemann sum on ANY partition is an upper (lower)
    bound.  Partition geometric in the distance to u (the integrand is steepest at u): u + (w-u)*{0, 1e-8 ... 1}."""
    return _sin_sum(k, u, w, W, s, N, False)


def _sin_sum(k, u, w, W, s, N, lower):
    ratio = (M(10) ** 8) ** (M(1) / (N - 1))
    pts = [u] + [u + (w - u) * M(10) ** -8 * ratio ** i for i in range(N - 1)] + [w]
    tot = 0
    for a, b in zip(pts[:-1], pts[1:]):
        tot += (b - a) * (2 * sin((b if lower else a) / (2 * W)) - s) ** (-k)
    return tot


def rhoG_int(k, a, b, F, s, cl, W, yc, NS):
    """UPPER bound of int_a^b rho_G(y)^{-k} dy, rho_G = max(F, G) - s, G = min(cl y, 2 sin(1/2 min(pi, y/W))).
    yc = (yc_lo, yc_hi) brackets the crossing of the two branches: G = cl y on [0, yc_lo], G = sine branch on
    [yc_hi, inf).  Pieces: constant (F - s), linear, sine (Riemann upper sum), mixed bracket (Riemann upper sum)."""
    if b <= a:
        return 0
    ycl, ych = yc
    piW = pi * W
    yFl = F / cl                                           # cl y = F
    yFs = 2 * W * asin(F / 2) if F < 2 else piW            # sine branch = F
    pts = sorted(set([a, b] + [p for p in (ycl, ych, yFl, yFs, piW) if a < p < b]))
    tot = 0

    def Gpt(y):
        return min(cl * y, 2 * sin(min(pi, y / W) / 2))

    def f(y):
        return (max(F, Gpt(y)) - s) ** (-k)
    for u, w in zip(pts[:-1], pts[1:]):
        if w <= ycl:                                       # linear branch
            if cl * w <= F:
                tot += (w - u) * (F - s) ** (-k)
            elif cl * u >= F:
                if k == 1:
                    tot += log((cl * w - s) / (cl * u - s)) / cl
                else:
                    tot += (1 / (cl * u - s) - 1 / (cl * w - s)) / cl
            else:
                tot += (w - u) * f(u)                      # (not reached: yFl is a breakpoint)
        elif u >= ych:                                     # sine branch
            if u >= piW:
                tot += (w - u) * (max(F, M(2)) - s) ** (-k)
            elif 2 * sin(w / (2 * W)) <= F:
                tot += (w - u) * (F - s) ** (-k)
            elif 2 * sin(u / (2 * W)) >= F:
                tot += sin_piece_int(k, u, min(w, piW), W, s, NS)
                if w > piW:
                    tot += (w - piW) * (2 - s) ** (-k)
            else:
                tot += (w - u) * f(u)
        else:                                              # inside the bracket [yc_lo, yc_hi]: f is non-increasing
            n = 8
            h = (w - u) / n
            tot += sum(f(u + i * h) for i in range(n)) * h
    return tot


def yc_bracket(cl, W):
    """bracket of yc = sup{y: cl y <= 2 sin(1/2 min(pi, y/W))}; verified."""
    piW = pi * W
    if cl * W >= 1:                                        # cl y >= y/W >= 2 sin(y/(2W)): sine branch everywhere
        return (M(0), M(0))
    if cl * piW <= 2:                                      # linear branch up to 2/cl >= pi W
        y = 2 / cl
        return (y * (1 - M(10) ** -40), y * (1 + M(10) ** -40))
    lo, hi = M(0) + piW * M(10) ** -12, piW            # cl lo < 2 sin(lo/2W) (since cl W < 1), cl hi > 2
    for _ in range(170):
        mid = (lo + hi) / 2
        if cl * mid <= 2 * sin(mid / (2 * W)):
            lo = mid
        else:
            hi = mid
    assert cl * lo <= 2 * sin(lo / (2 * W)) and cl * hi >= 2 * sin(hi / (2 * W))
    return (lo, hi)


def Jints(U0, R, KR, cA, cR, dl1, Ke, dL, chig, S1G, td):
    """J_k(U0), k = 1, 2, of Definition 3.3: the minimum of chi_g U0 (c_R* R)^{-k} and
    2 d_L R/(K_eps (c_R*R)^k) + chi_g [int_{K_R R}^{max(K_R R, U0/2)} rho_C^{-k} + int_0^{U0/2} rho_C^{-k}]
    (rho_C = max(c_A K_R R, C) - delta_1 R/K_eps with the function C of Section 8: C(y) = min(c0' y, k_c y,
    2 sin(1/2 min(pi, y/(W_x Lhat))))); integrals bounded from above as in rhoG_int (an empty range gives 0)."""
    J1o = chig * U0 / (cR * R)
    J2o = chig * U0 / (cR * R) ** 2
    if not S1G:
        return J1o, J2o, OrderedDict(J1o=J1o, J2o=J2o)
    C0, ap, lam0, kc, W = td['cN'], td['ap'], td['lam0'], td['kc'], td['WxL']
    c0p = 1 - (C0 * lam0 ** ap) ** 2 / 2
    cl = min(c0p, kc)
    F = cA * KR * R
    s = dl1 * R / Ke
    yc = yc_bracket(cl, W)
    Y = U0 / 2
    NS = td.get('NS', 20000)
    J1g = 2 * dL / (Ke * cR) + chig * (rhoG_int(1, KR * R, Y, F, s, cl, W, yc, NS) + rhoG_int(1, 0, Y, F, s, cl, W, yc, NS))
    J2g = 2 * dL / (Ke * cR ** 2 * R) + chig * (rhoG_int(2, KR * R, Y, F, s, cl, W, yc, NS)
                                              + rhoG_int(2, 0, Y, F, s, cl, W, yc, NS))
    J1g = J1g * (1 + M(10) ** -30)          # absorbs 50-digit rounding of the closed forms / sums
    J2g = J2g * (1 + M(10) ** -30)
    return min(J1o, J1g), min(J2o, J2g), OrderedDict(J1o=J1o, J2o=J2o, J1g=J1g, J2g=J2g, c0p=c0p, cl=cl)


def B3prime(kap, crho, Kf, nu, gam, dL, chig, Cps, Car):
    """B_3' of Definition 3.3 (closed form of the integral)."""
    p = nu + gam - 2
    if Car * sqrt(Kf) < Cps:
        xs = (Cps / Car) ** 2
        ch = Car * sqrt(Kf)
        integral = Car * (xs ** (p + M(3) / 2) - Kf ** (p + M(3) / 2)) / (p + M(3) / 2) + Cps * xs ** (p + 1) / (-p - 1)
    else:
        ch = Cps
        integral = Cps * Kf ** (p + 1) / (-p - 1)
    return 2 * kap ** M(1.5) / (pi * crho ** 3) * Kf ** (-nu) * (2 * dL * Kf ** p * ch + chig * integral)


def core(gam, U0, v0, tag, Dp, S1G, td):
    R, m, s0, kap, cA = I['R'], I['m'], I['s0'], I['kap'], I['cA']
    KR, Kf, Ke, eta1, qc = I['KR'], I['Kf'], I['Keps'], I['eta1'], I['qc']
    dL, dl1, nu, A0, fF = I['dL'], I['delta1'], I['nu'], I['A0'], I['fF']
    D = OrderedDict()
    D['M'] = m * R ** (-gam)
    chig = kap * dL
    c6 = (1 + dl1) / cA
    CT, Cmu, rstar = tiltc(gam, kap, cA, m, qc)
    crho = cA - 2 * dl1 / Kf
    ceta = cA - dl1 / (Ke * eta1)
    cR = cA * KR - dl1 / Ke
    K1 = crho * Kf / kap
    K2 = cR / kap
    camp = aDs(K1) * chig / crho
    J1, J2, Jd = Jints(U0, R, KR, cA, cR, dl1, Ke, dL, chig, S1G, td)
    B2Up = 2 * kap ** M(1.5) * (1 + 1 / K2) / pi
    B2eta = 2 * kap ** M(1.5) * (1 + 1 / K1) * (chig / eta1 + dL / (Ke * eta1 ** 2)) / (pi * ceta ** 2)
    Cp = sqrt(kap) * (1 + 1 / Kf) ** (M(1) / 2 + gam) / sqrt(Kf) + kap * CT * (1 + 1 / Kf) ** gam
    CpV = sqrt(kap) * sqrt(Cmu) * (1 + 1 / Kf) ** (M(1) / 2 + gam)
    Cps = min(Cp, CpV)
    Car = kap ** M(1.5) * (1 + 1 / Kf) ** (M(1.5) + gam) / cA
    B3p = B3prime(kap, crho, Kf, nu, gam, dL, chig, Cps, Car)
    PsiI = 2 + log(Kf)
    TI = dL * (kap * c6 + 2) + c6 * chig * PsiI
    B5 = (1 / crho) * ((Cps + sqrt(kap) * Kf ** (-1 - gam) / pi) / crho + Kf ** (-gam)) ** 2
    I5 = chig * (eta1 + 1 / Ke) ** (2 * gam) / (2 * gam)
    Xfar = v0 * (J1 + (dL / (Ke * eta1) + chig * log(KR / eta1)) / ceta)
    LJ = exp(Xfar + B5 * I5 * v0 * m ** 2) + v0 * kap * TI
    thbar = fF ** 2 + 2 * v0 * Dp
    P4l = v0 * (2 * aDs(K1) * dL / (crho * Kf) + aDs(K2) * J1)
    P5 = A0 * (s0 + (KR / Kf) ** nu * v0 / m * (B2Up * R * J2 + B2eta) + B3p * v0)
    D.update(chig=chig, c6=c6, CT=CT, Cmu=Cmu, rstar=rstar, crho=crho, ceta=ceta, cR=cR, K1=K1, K2=K2, camp=camp,
             J1=J1, J2=J2, B2Up=B2Up, B2eta=B2eta, Cp=Cp, CpV=CpV, Cps=Cps, Car=Car, B3p=B3p, PsiI=PsiI, TI=TI,
             B5=B5, I5=I5, Xfar=Xfar, LJ=LJ, Dp=Dp, thbar=thbar, P4l=P4l, P5=P5)
    for k_, v_ in Jd.items():
        D['J_' + k_] = v_
    PsiI_gen = 2 + log(min(Kf, KR)) + max(Kf - KR, 0) / KR
    D['_simplification_ok'] = abs(PsiI_gen - PsiI) < M(10) ** -45 and Kf + 1 <= KR
    g = 'core'
    t = r'\,[%s]' % tag
    gs = r'\gamma' if tag == 'p' else r'\gD'
    cond(g, r'(P0) $\frac12<%s$' % gs + t, M(1) / 2, '<', gam)
    cond(g, r'(P0) $%s+\nu<1$' % gs + t, gam + nu, '<', 1)
    cond(g, r'(P0) $0<R$' + t, 0, '<', R)
    cond(g, r'(P0) $R\le1$' + t, R, '<=', 1)
    cond(g, r'(P0) $m>0$' + t, m, '>', 0)
    cond(g, r'(P0) $0<s_0$' + t, 0, '<', s0)
    cond(g, r'(P0) $s_0\le\fF$' + t, s0, '<=', fF)
    cond(g, r'(P0) $\fF<1$' + t, fF, '<', 1)
    cond(g, r'(P0) $1<\kappa$' + t, 1, '<', kap)
    cond(g, r'(P0) $\kappa\le4/3$' + t, kap, '<=', M(4) / 3)
    cond(g, r'(P0) $0<c_A$' + t, 0, '<', cA)
    cond(g, r'(P0) $c_A\le1$' + t, cA, '<=', 1)
    cond(g, r'(P0) $K_f\ge3$' + t, Kf, '>=', 3)
    cond(g, r'(P0) $K_f+1\le K_R$' + t, Kf + 1, '<=', KR)
    cond(g, r'(P0) $\Keps\ge2$' + t, Ke, '>=', 2)
    cond(g, r'(P0) $0<\eta_1$' + t, 0, '<', eta1)
    cond(g, r'(P0) $\eta_1\le K_f/(K_f+1)$' + t, eta1, '<=', Kf / (Kf + 1))
    cond(g, r'(P0) $\qc>1$' + t, qc, '>', 1)
    cond(g, r'(P0) $\nu\ge0$' + t, nu, '>=', 0)
    cond(g, r'(P0) $\dL\ge1$' + t, dL, '>=', 1)
    cond(g, r'(P0) $\delta_1\ge1$' + t, dl1, '>=', 1)
    cond(g, r'(P0) $A_0\ge1$' + t, A0, '>=', 1)
    cond(g, r'(P0) $0<\vz$' + t, 0, '<', v0)
    cond(g, r'(P0) $\vz<1$' + t, v0, '<', 1)
    cond(g, r'(P1) $1/(1-\vz)\le\dL$' + t, 1 / (1 - v0), '<=', dL)
    cond(g, r'(P1) $e^{2\vz/(1-\vz)}\le\delta_1$' + t, exp(2 * v0 / (1 - v0)), '<=', dl1)
    cond(g, r'(P2) $c_\rho^*K_f\ge2$' + t, crho * Kf, '>=', 2)
    cond(g, r'(P2) $c_R^*\Keps\ge1$' + t, cR * Ke, '>=', 1)
    cond(g, r'(P2) $c_6\le K_R\Keps$' + t, c6, '<=', KR * Ke)
    cond(g, r'(P2) $c_\eta>0$' + t, ceta, '>', 0)
    cond(g, r'(P3) $\camp\vz\le\nu$' + t, camp * v0, '<=', nu)
    cond(g, r'(P4)' + t, P4l, '<=', log(A0))
    cond(g, r'(P5)' + t, P5, '<=', fF)
    cond(g, r"(P6) $\bar\theta<1$" + t, thbar, '<', 1)
    cond(g, r'(P7) $\LJ(U_0)<\kappa$' + t, LJ, '<', kap)
    cond(g, r'(P8) $m^2r_*<4c_A$' + t, m ** 2 * rstar, '<', 4 * cA)
    cond('extra', r'$\Cmu\ge(1+2%s)\kappa/c_A$' % gs + t, Cmu, '>=', (1 + 2 * gam) * kap / cA)
    cond('extra', r'$%s\le c_A/\kappa$' % gs + t, gam, '<=', cA / kap)
    cond('extra', r'$K_f(2%s-1)\le3c_A/\kappa$' % gs + t, Kf * (2 * gam - 1), '<=', 3 * cA / kap)
    return D


def corollary(gam, ap, C0, lam0, csep, tag):
    R, m, s0, cA, KR, Kf, nu = I['R'], I['m'], I['s0'], I['cA'], I['KR'], I['Kf'], I['nu']
    g = 'cor'
    t = r'\,[%s]' % tag
    gs = r'\gamma' if tag == 'p' else r'\gD'
    cond(g, r'(C1) $R\le\lambda_0$' + t, R, '<=', lam0)
    cond(g, r'(C2)' + t, 1 - (C0 * min(KR * R, lam0) ** ap) ** 2 / 2, '>=', cA)
    if KR * R < lam0:
        cond(g, r'(C3)' + t, lam0 * (1 - (C0 * lam0 ** ap) ** 2 / 2), '>=', cA * KR * R)
    cond(g, r'(C4) $c_{\mathrm{sep}}%s\ge c_AK_RR$' % ('' if tag == 'p' else r'^{\mathrm A}') + t, csep, '>=',
         cA * KR * R)
    cond(g, r'(C5) $%s+\nu\le a^\prime$' % gs + t, gam + nu, '<=', ap)
    cond(g, r'(C6)' + t, C0 * R ** ap, '<=', s0 * m * (Kf / KR) ** nu)


# =====================================================================================================================
# Section 4. assembly(): Section 8.1, Lemma 5.1, Theorem 5.2
# =====================================================================================================================
def assembly(S1G, DP):
    v0, eps = I['v0'], I['epsS']
    R, m, s0, kap, cA, KR, Kf, Ke = I['R'], I['m'], I['s0'], I['kap'], I['cA'], I['KR'], I['Kf'], I['Keps']
    nu, dl1, gam, gD = I['nu'], I['delta1'], I['gam'], I['gD']
    T2, Umax, csep, kc, cN = I['T2'], I['Umax'], I['csep'], I['kc'], I['cN']
    muTb, mub, ap, thv, cT4, czlo, czhi, cy = I['muTb'], I['mub'], I['ap'], I['thv'], I['cT4'], I['czlo'], I['czhi'], I['cy']
    lam0, GT, epsbar, vbar = I['lam0'], I['GT'], I['epsbar'], I['vbar']
    omb, ck = I['omb'], I['ck']
    A = OrderedDict()
    zeta = sqrt(1 - omb ** 2) - v0
    etaN = aDs(M(4)) * v0 / zeta
    etaD = v0 / zeta
    We = cA * KR * R / kc
    delta0 = I['d0fac'] * R
    UA = We + delta0 + R
    UE = We + R
    Dbar = (kap * We + eps) / (1 - v0)
    z0max = czhi * sqrt(eps)
    Xs = UE + z0max + Dbar
    Gf = We + eps + delta0
    csepA = min(csep, kc * (1 - UA))
    th0 = cT4 * Xs ** (1 - muTb - gD)
    thy = cy * 2 ** (2 - muTb) * z0max ** (1 - muTb - gD)
    C0 = cN
    Tsharp = T2 + kap * Umax / (1 - v0)
    A.update(zeta=zeta, etaN=etaN, etaD=etaD, We=We, delta0=delta0, UA=UA, UE=UE, Dbar=Dbar, z0max=z0max, Xs=Xs,
             Gf=Gf, csepA=csepA, th0=th0, thy=thy, C0=C0)
    td = dict(cN=cN, ap=ap, lam0=lam0, kc=kc, WxL=I['WxL'], NS=I.get('_NS', 20000))
    Dm = core(gam, Umax, v0, 'p', DP['p'], S1G, td)
    corollary(gam, ap, C0, lam0, csep, 'p')
    DA = core(gD, UA, v0, r'p_{\mathrm A}', DP['pA'], S1G, td)
    corollary(gD, ap, C0, lam0, csepA, r'p_{\mathrm A}')
    CTA = DA['CT']                                         # the tilt constant C_T of p_A
    sigb = thv * Gf ** (1 - mub)
    thG = thv * Gf ** (1 - mub - gD)
    ksig = (1 + sigb / 2) / (1 - sigb ** 2 / 2)
    C3 = 2 * CTA
    ctau = 1 / (1 - m ** 2 / 2)
    rhos = cA * (R - delta0 - eps) - dl1 * eps
    Krot = kap / (1 - v0) * (2 * R / (cA * delta0) + (We + eps) / rhos)
    om0 = CTA * m * (delta0 / R) ** gD + ksig * sigb + v0 * Krot
    thh1 = (CTA * m * R ** (-gD) + 2 ** gD * ksig * thG
            + v0 * 4 * kap * C3 * m / (cA * (1 - v0)) * 2 ** gD * R ** (-gD))
    varth = ctau ** gD * max(thh1, om0 * delta0 ** (-gD))
    A.update(CTA=CTA, sigb=sigb, thG=thG, ksig=ksig, C3=C3, ctau=ctau, rhos=rhos, Krot=Krot, om0=om0, thh1=thh1,
             varth=varth)
    th0y = max(th0, thy)
    xc = (om0 / varth) ** (1 / gD)
    Lh = 1 / (2 * gD) + max(M(0), log((Dbar + eps) / xc))
    Th0 = th0 + v0 * th0y / zeta ** 2 + v0 * varth / (zeta ** 2 * (1 - etaD) * (gD - etaD))
    Thb = Th0 + th0y / zeta + varth / (zeta * (1 - etaD))
    Kw = (Th0 + th0y / zeta) ** 2 * Xs ** (2 * gD) / (gD * zeta) + 2 * om0 ** 2 * Lh / (zeta ** 3 * (1 - etaD) ** 2)
    dt = exp(v0 * Kw) - 1
    omT = Th0 * Xs ** gD
    omy = thy * Xs ** gD
    kD = ck * 4 * (1 + dt) / zeta
    Thp = (1 + omy + v0) * (1 + 1 / kD) ** gD * Th0 / (1 - omT ** 2 / 2) + th0y + varth / (1 - etaD)
    cn = sqrt(1 + dt) * kD ** gD / (gD * zeta)
    cbeta = 2 * (1 + dt) ** M(1.5) * kD ** (gD - 1) / (pi * zeta ** 3 * (1 - gD))
    Ktail = cn * Thb + cbeta * Thp
    TS = (1 + Dbar / (kD * R)) ** etaN * (C0 * R ** ap + v0 * Ktail * R ** gD)
    TSrhs = s0 * m * (Kf / KR) ** nu
    A.update(th0y=th0y, xc=xc, Lh=Lh, Th0=Th0, Thb=Thb, Kw=Kw, dt=dt, omT=omT, omy=omy, kD=kD, Thp=Thp, cn=cn,
             cbeta=cbeta, Ktail=Ktail, TS=TS, TSrhs=TSrhs, C0Ra=C0 * R ** ap, PT=(1 + dt) * Dm['LJ'], Tsharp=Tsharp)
    g = 'asm'
    cond(g, r'(A2) $1-\UA\ge\We$', 1 - UA, '>=', We)
    cond(g, r'(A3) $G_f\le G_{\mathrm T}$', Gf, '<=', GT)
    cond(g, r'(A3) $\epsS\le\delta_0$', eps, '<=', delta0)
    cond(g, r'(A3) $\delta_0\le R/2$', delta0, '<=', R / 2)
    cond(g, r'(A3) $\bar\sigma\le\frac12$', sigb, '<=', M(1) / 2)
    cond(g, r'(A3) $\rho_*\ge\epsS$', rhos, '>=', eps)
    cond(g, r'(A3) $m^2<2$', m ** 2, '<', 2)
    cond(g, r'(A3) $\gD\le1-\mub$', gD, '<=', 1 - mub)
    cond(g, r'(A3) $\UA\ge\We{+}2\epsS{+}\delta_0$', UA, '>=', We + 2 * eps + delta0)
    cond(g, r'(A3) $\kappa\le2$', kap, '<=', 2)
    cond(g, r'(A3) $K_R\ge1$', KR, '>=', 1)
    cond(g, r'(A4) $\zeta>0$', zeta, '>', 0)
    cond(g, r'(A4) $\bar\omega\le\frac12$', omb, '<=', M(1) / 2)
    cond(g, r'(A4) $c_k\ge1$', ck, '>=', 1)
    cond(g, r'(A4) $\theta_0X_*^{\gD}\le\bar\omega$', th0 * Xs ** gD, '<=', omb)
    cond(g, r'(A4) $\bar\omega_y\le\bar\omega$', omy, '<=', omb)
    cond(g, r'(A4) $\omega_0\le\bar\omega$', om0, '<=', omb)
    cond(g, r'(A4) $\omega_T\le\frac12$', omT, '<=', M(1) / 2)
    cond(g, r'(A4) $\etaD\le\gD/2$', etaD, '<=', gD / 2)
    cond(g, r'(A4) $\gD\le1-\muTb$', gD, '<=', 1 - muTb)
    cond(g, r'(A4) $\gD<1$', gD, '<', 1)
    cond(g, r'(A4) $\czlo\epsS^{1/(2-2\vz)}\ge\epsS/\zeta$', czlo * eps ** (1 / (2 - 2 * v0)), '>=', eps / zeta)
    cond(g, r'(A4) $\UE\le G_{\mathrm T}$', UE, '<=', GT)
    cond(g, r'(A5) $\gD\ge\gamma+\nu+\etaN$', gD, '>=', gam + nu + etaN)
    cond(g, r'(A5) $\gD+\nu\le a^\prime$', gD + nu, '<=', ap)
    cond(g, r'(A5) (TS)', TS, '<=', TSrhs)
    cond(g, r'(A5) $K_RR\le1-\UE-\We-\epsS$', KR * R, '<=', 1 - UE - We - eps)
    cond(g, r'(A5) (PT) $(1+\delta_t)\LJ(U_{\max})<\kappa$', (1 + dt) * Dm['LJ'], '<', kap)
    cond(g, r'(A6) $\vz\le\vbar$', v0, '<=', vbar)
    cond(g, r'(A6) $\epsS\le\epsbar$', eps, '<=', epsbar)
    cond(g, r'(A6) $\epsS\le R/\Keps$', eps, '<=', R / Ke)
    cond(g, r'(A6) $2\We+R+\epsS\le1$', 2 * We + R + eps, '<=', 1)
    cond(g, r'(A6) $K_RR<\lambda_0$', KR * R, '<', lam0)
    cond(g, r"(A6) $a^\prime\le1-\muTb$ (printed $\muTb$)", ap, '<=', 1 - muTb)
    cond(g, r'(A6) $\Tsharp\le13.1$', Tsharp, '<=', I['T0'])
    if S1G:   # the function C of (S1G): Lemma 7.x (global chords) and Lemma 8.x
        c0p = Dm['J_c0p']
        A['c0p'] = c0p
        cond(g, r"(A7) $c_0'>0$", c0p, '>', 0)
        cond(g, r'(A7) $8/\lambda_0\ge1$', 8 / lam0, '>=', 1)
    return A, Dm, DA


def extra_conditions(TD, A, Dm, DA):
    """Further elementary inequalities used in the proofs."""
    g = 'extra'
    kap, cA, Kf, KR, m, omb = I['kap'], I['cA'], I['Kf'], I['KR'], I['m'], I['omb']
    cond(g, r'$\frac32\kappa-1\le1$', M(3) / 2 * kap - 1, '<=', 1)
    cond(g, r'$c_A/2<1\le\delta_1$', cA / 2, '<', 1)
    cond(g, r'$c_\tau\ge1$', A['ctau'], '>=', 1)
    cond(g, r'$K_f<K_R$', Kf, '<', KR)
    cond(g, r'$\zeta\le1-\bar\omega^2/2$', A['zeta'], '<=', 1 - omb ** 2 / 2)
    cond(g, r'$\lambda_0<1$', I['lam0'], '<', 1)
    cond(g, r'$\zeta\le1$', A['zeta'], '<=', 1)
    cond(g, r'$m_0\le1$ ($\arcsin$ domain)', TD['m0'], '<=', 1)
    cond(g, r'$e_\rho/\sqrt3\le1$ ($\arcsin$ domain)', TD['erho'] / sqrt(3), '<=', 1)
    cond(g, r'$\pi/2+\eta<2$', pi / 2 + I['eta'], '<', 2)
    cond(g, r'$2\pi-2\eta>4$', 2 * pi - 2 * I['eta'], '>', 4)
    cond(g, r'$\vbar^2\le\frac12$', I['vbar'] ** 2, '<=', M(1) / 2)
    cond(g, r'$Q_{\mathrm a}\ge1$', TD['Qa'], '>=', 1)
    cond(g, r'$W_{\mathrm v}\ge1$', TD['Wv'], '>=', 1)
    cond(g, r'$W_{\mathrm t}\ge1$', TD['Wt'], '>=', 1)
    cond(g, r'$\eta\le1$', I['eta'], '<=', 1)
    cond(g, r'$\mathcal E_1\ge1$', TD['E1'], '>=', 1)
    cond(g, r'$\bar t_1<3$', TD['t1b'], '<', 3)
    cond(g, r'$\sA_{\max}<2$', TD['Amax'], '<', 2)
    cond(g, r'$h_{\mathrm t}\le1$', TD['ht'], '<=', 1)


# =====================================================================================================================
# Section 5. CERTIFIED D' (Section 4, Lemma "evaluation"), parametrised by INPUTS.
#   scalar constants (parameters as decimal strings, C_T, C_mu, C_V, C_1A, c6, P_0, bottom-cell closed forms, r^gamma)
#   in mpmath.iv (outward rounded), converted to float64 with one extra outward ulp; (1+y)^gamma via an iv-computed
#   increasing table; arrays in IEEE float64 with np.nextafter outward after every operation; sums of non-negative
#   terms inflated by (1 + 1e-11) >= 1 + gamma_n (Higham, Thm 3.1; n <= 5e4).  Cell scheme: proof of the Lemma.
# =====================================================================================================================
iv.prec = 80
INF = np.inf


def U(x):
    return np.nextafter(x, INF)


def Dn(x):
    return np.nextafter(x, -INF)


def fhi(J):
    return float(np.nextafter(float(J.b), INF))


def flo(J):
    return float(np.nextafter(float(J.a), -INF))


SUMF = 1.0 + 1e-11
NMAX = 50000


def usum(a):
    a = np.asarray(a, float)
    assert a.size <= NMAX and np.all(a >= 0)
    return float(U(U(np.sum(a)) * SUMF))


def udot(K, d):
    assert K.shape[1] <= NMAX and np.all(K >= 0) and np.all(d >= 0)
    return U(U(K @ d) * SUMF)


def imax(a, b):
    return iv.mpf([max(a.a, b.a), max(a.b, b.b)])


def min_iv(a, b):
    a = iv.mpf(a)
    b = iv.mpf(b)
    return iv.mpf([min(a.a, b.a), min(a.b, b.b)])


def CT_iv(P):
    """C_T in interval arithmetic."""
    g, kap, cA, m, qc = P['gam'], P['kap'], P['cA'], P['m'], P['qc']

    def s(r):
        f = iv.sqrt(kap) / cA
        if r.b <= 2:
            return f * r / 2
        if r.a >= 2:
            return f * iv.sqrt(r - 1)
        lo = f * iv.mpf(r.a) / 2
        hi = f * iv.sqrt(iv.mpf(r.b) - 1)
        return iv.mpf([lo.a, hi.b])
    r2 = 2 * qc / (qc - 1)
    rstar = imax(qc, r2)
    arg = 1 - m ** 2 * rstar / (4 * cA)
    assert arg.a > 0
    sq = 1 / (1 - qc ** (-g))
    return imax(sq * s(qc), s(r2)) / iv.sqrt(arg)


class Const:
    def __init__(self, Pstr, gam_str):
        P = {k: iv.mpf(v) for k, v in Pstr.items()}
        P['gam'] = iv.mpf(gam_str)
        self.P = P
        kap, cA, d1, dL = P['kap'], P['cA'], P['d1'], P['dL']
        CT = CT_iv(P)
        CA = CB = CT
        CTL = 2 * CT
        CmuA = 1 + kap * CA ** 2
        self.I = dict(CA=CA, CB=CB, CTL=CTL, CmuA=CmuA, C1A=iv.sqrt(kap * CmuA), CV=iv.sqrt(1 + kap * CB ** 2),
                      c6=(1 + d1) / cA, uc=1 / CmuA, dLp=3 * dL - 2, kmc=kap - cA, Kf1=P['Kf'] + 1,
                      k32_2cA=kap ** iv.mpf('1.5') / (2 * cA))
        self.I.update(P)
        for k, v in self.I.items():
            setattr(self, k + '_hi', fhi(v))
            setattr(self, k + '_lo', flo(v))
        self.h = 2.0 ** -15
        n = int((self.Kf_hi + 0.5) / self.h) + 2
        g = iv.mpf(P['gam'].b)
        hh = iv.mpf(self.h)
        tab = np.empty(n)
        for j in range(n):
            tab[j] = fhi((1 + iv.mpf(j) * hh) ** g)
        assert np.all(np.diff(tab) >= 0)
        self.powtab = tab

    def pow_u(self, z):
        y = U(np.asarray(z, float) - 1.0)
        j = np.maximum(np.ceil(y / self.h).astype(np.int64), 0)
        assert np.all(j < len(self.powtab))
        return self.powtab[j]


def budgets(c, s, thf):
    lam = np.maximum(s, thf / 2)
    Om_hi = np.minimum(1.0, U(c.CmuA_hi * lam)); Om_lo = np.minimum(1.0, Dn(c.CmuA_lo * lam))
    Q_hi = U(U(c.kap_hi * lam) * Om_hi); Q_lo = Dn(Dn(c.kap_lo * lam) * Om_lo)
    G_hi = U(np.sqrt(Q_hi)); G_lo = Dn(np.sqrt(np.maximum(Q_lo, 0)))
    return (Om_lo, Om_hi), (Q_lo, Q_hi), (G_lo, G_hi)


def budgets_c(c, s):
    return budgets(c, s, 0.0)


def ust(K, Phi):
    lo, hi = Phi
    d = np.maximum(U(hi[1:] - lo[:-1]), 0.0)
    return U(U(K[:, 0] * hi[0]) + udot(K[:, :-1], d))


def ell_ratio_u(ell):
    return U(ell / Dn(1.0 + ell))


def p_nochord(c, y, ell):
    L2 = U(c.CV_hi * U(np.sqrt(U(U(c.kap_hi * ell) * U(1.0 + y)))))
    fac = U(1.0 + U(U(c.kap_hi * ell) / c.cA_lo))
    S = U(U(fac * U(np.sqrt(U(c.kap_hi * ell_ratio_u(ell))))) * U(np.sqrt(U(1.0 + y))))
    return U(np.minimum(L2, S) * c.pow_u(U(1.0 + y)))


def pfrak(c, y, thf):
    y = np.asarray(y, float)
    ell = np.maximum(y, thf / 2)
    base = p_nochord(c, y, ell)
    chord = U(U(U(c.kap_hi * c.CTL_hi) * y) * c.pow_u(U(1.0 + y)))
    val = np.where(y >= thf / 2, np.minimum(base, chord), base)
    return np.where(y > 0, val, 0.0)


def pstar(c, z, thf):
    z = np.asarray(z, float)
    zz = np.maximum(z, 0.0)
    h = thf / 2
    left = p_nochord(c, np.minimum(zz, h), np.full_like(zz, h))
    right = pfrak(c, np.maximum(zz, h), thf)
    val = np.where(zz < h, left, np.maximum(left, right))
    return np.where(z > 0, val, 0.0)


def pL(c, y, thf):
    y = np.asarray(y, float)
    ell = np.maximum(y, thf / 2)
    fac = U(1.0 + U(U(c.kap_hi * ell) / c.cA_lo))
    inner = U(U(U(U(2.0 * c.kap_hi) * c.kmc_hi) * U(1.0 + y)) * ell_ratio_u(ell))
    val = U(fac * U(np.sqrt(inner)))
    return np.where(y > 0, val, 0.0)


def pLstar(c, z, thf):
    z = np.asarray(z, float)
    return np.where(z > 0, pL(c, np.maximum(z, 1e-300), thf), 0.0)


def P0_u(c, th):
    Ic = c.I
    t = iv.mpf(th)
    lam = lambda s: iv.mpf(max(s, th / 2))
    Gb = lambda s: iv.sqrt(Ic['kap'] * lam(s) * min_iv(1, Ic['CmuA'] * lam(s)))
    if th <= 1:
        return fhi(Gb(th))
    a1 = Ic['kap'] * Ic['CA'] * t ** (1 + Ic['gam'])
    a2 = iv.sqrt((Ic['kap'] * t - Ic['cA']) * Ic['CmuA'] * t ** (1 + 2 * Ic['gam']))
    a3 = Ic['k32_2cA'] * t ** (2 + Ic['gam'])
    alt = min(fhi(a1), fhi(a2), fhi(a3))
    return max(fhi(Gb(1.0)), alt)


def sgrid(lo, n):
    pts = [np.array([0.0, 1.0]), np.linspace(0, 1, n // 4)]
    if lo > 0:
        pts += [np.geomspace(max(lo, 1e-16), 1.0, n), np.array([lo])]
    s = np.unique(np.concatenate(pts))
    return s[(s >= 0) & (s <= 1)]


class Cell:
    def __init__(self, c, th_lo, th_hi, nx=500, ns=700, bottom=False, x1=1e-7):
        self.c, self.th_lo, self.th_hi, self.bottom, self.x1 = c, th_lo, th_hi, bottom, x1
        thb = th_hi
        d1th = U(c.d1_hi * th_hi)

        def den_lin(W):
            return Dn(Dn(c.cA_lo * W) - d1th)

        if bottom:
            def K1f(W):
                return U(1.0 / np.maximum(Dn(W / c.c6_hi), den_lin(W)))
        else:
            def K1f(W):
                return U(1.0 / np.maximum(th_lo, den_lin(W)))

        def M1f(W):
            return np.minimum(1.0, U(th_hi / np.maximum(th_hi, den_lin(W))))

        thf = th_hi
        xlo = x1 if bottom else float(Dn(th_lo / c.kap_hi))
        xend = c.Kf_hi
        extra = [] if bottom else [np.arange(1, 400) * xlo]
        xs = np.unique(np.concatenate([np.geomspace(xlo, xend, nx), np.linspace(xlo, xend, nx // 2), [xlo, xend]] + extra))
        xs = xs[(xs >= xlo) & (xs <= xend)]
        assert xs[0] == xlo and xs[-1] == xend
        xl, xr = xs[:-1], xs[1:]
        if bottom:
            s = sgrid(1e-15, ns); Om, Q, G = budgets_c(c, s)
        else:
            s = sgrid(thf / 2, ns); Om, Q, G = budgets(c, s, thf)
        assert s[0] == 0.0 and s[-1] == 1.0
        W = Dn(xl[:, None] + s[None, :])
        K1 = K1f(W); M1 = M1f(W); K2 = U(K1 * K1); MK = U(M1 * K1)

        def OmA_u(sig, t):
            return np.minimum(1.0, U(c.CmuA_hi * np.maximum(sig, t / 2)))

        c6th = U(c.c6_hi * th_hi)
        ind = xl < c6th
        IND_T = np.where(ind, OmA_u(U(c6th - xl), th_hi), 0.0)
        IND_H = np.where(ind, U(c.CmuA_hi * c.c6_hi), 0.0) if bottom else U(IND_T / th_lo)
        if bottom:
            Mx, Kx = M1f(xl), K1f(xl)
            a_om = U(c.CmuA_hi / 2)
            iH = U(U(U(a_om * Mx) + ust(K1, Om)) + IND_H)
            iT = U(U(U(min(1.0, U(c.CmuA_hi * thb / 2)) * Mx) + ust(M1, Om)) + IND_T)
            kc4 = U(U(c.kap_hi * c.CmuA_hi) / 4)
            qH = U(U(kc4 * U(Mx * Mx)) + ust(K2, Q))
            qT = U(U(U(kc4 * thb) * U(Mx * Mx)) + ust(MK, Q))
            ca = U(c.C1A_hi / 2)
            j2H = U(U(ca * U(Mx * Kx)) + ust(K2, G))
            j2T = U(U(ca * U(Mx * Mx)) + ust(MK, G))
            j1H = U(U(ca * Mx) + ust(K1, G))
            j1T = U(U(U(ca * thb) * Mx) + ust(M1, G))
        else:
            iH = U(ust(K1, Om) + IND_H); iT = U(ust(M1, Om) + IND_T)
            qH = ust(K2, Q); qT = ust(MK, Q)
            j2H = ust(K2, G); j2T = ust(MK, G)
            j1H = ust(K1, G); j1T = ust(M1, G)
        pf = pfrak(c, xr, thf)
        zs = xr if bottom else np.maximum(U(xr - Dn(th_lo / c.kap_hi)), 0.0)
        ps = pstar(c, zs, thf)
        Lf = U(0.5 * U(U(c.dL_hi * pf) + U(c.dLp_hi * ps)))
        LfL = U(U(0.5 * U(U(c.dL_hi * pL(c, xr, thf)) + U(c.dLp_hi * pLstar(c, zs, thf)))) / c.m_lo)
        self.linLH, self.linLT = U(LfL * j2H), U(LfL * j2T)
        self.xl, self.xr, self.dx = xl, xr, U(xr - xl)
        self.IH, self.IT = U(c.dL_hi * iH), U(c.dL_hi * iT)
        self.quadH, self.linH = U(U(c.dL_hi / 2) * qH), U(Lf * j2H)
        self.quadT, self.linT = U(U(c.dL_hi / 2) * qT), U(Lf * j2T)
        self.LH = U(U(c.dL_hi * j1H) / c.m_lo)
        self.LT = U(U(c.dL_hi * j1T) / c.m_lo)
        self.onex_g = c.pow_u(U(1.0 + xr))
        W0 = s[None, :]
        if bottom:
            M0 = M1f(W0); K0 = K1f(np.maximum(W0, 1e-300)); MK0 = U(M0 * K0); MK0[:, 0] = 0.0
            assert s[1] <= c.uc_lo
            i0 = U(U(min(1.0, U(c.CmuA_hi * thb / 2)) + ust(M0, Om)[0]) + OmA_u(c6th, thb))
            q0 = U(U(U(c.kap_hi * c.CmuA_hi / 4) * thb) + ust(MK0, Q)[0])
            q0 = U(q0 + U(U(U(U(2 * c.kap_hi) * c.CmuA_hi) * c.c6_hi) * s[1]))
            atomG = fhi(iv.sqrt(c.I['kap'] * iv.mpf(thb) / 2 * min_iv(1, c.I['CmuA'] * iv.mpf(thb) / 2)))
            lin0 = U(U(U(0.5 * c.dLp_hi) * c.C1A_hi) * U(atomG + ust(U(M0 * M0), G)[0]))
        else:
            M0 = M1f(W0); K0 = K1f(W0)
            i0 = U(ust(M0, Om)[0] + OmA_u(c6th, th_hi))
            q0 = ust(U(M0 * K0), Q)[0]
            lin0 = U(U(U(0.5 * c.dLp_hi) * P0_u(c, th_hi)) * ust(U(M0 * K0), G)[0])
        self.TH0 = float(U(U(U(c.dL_hi * i0) + U(U(c.dL_hi / 2) * q0)) + lin0))
        if bottom:
            self._crude()

    def _crude(self):
        c, Ic = self.c, self.c.I
        x1 = iv.mpf(self.x1)
        kap, Cmu, c6, C1A, CV, CTL, dL, dLp, gam, m = (Ic[k] for k in
                                                        ('kap', 'CmuA', 'c6', 'C1A', 'CV', 'CTL', 'dL', 'dLp', 'gam', 'm'))
        u = 1 / Cmu
        A_i, B_i = Cmu / 2 + Cmu * c6, Cmu * c6
        A_q, B_q = kap * Cmu / 4 + kap * c6 ** 2 / u, 2 * kap * Cmu * c6 ** 2
        cj2, dj2 = C1A * c6 * (iv.mpf('0.5') + c6), iv.sqrt(kap) * c6 ** 2 / 3 * u ** iv.mpf('-1.5')
        A_1, B_1 = C1A / 2 + c6 * iv.sqrt(kap) * u ** iv.mpf('-0.5'), C1A * c6
        g1 = (1 + x1) ** (gam + iv.mpf('0.5'))
        a_l, b_l = g1 * dL * kap * CTL / 2, g1 * dLp * CV * iv.sqrt(kap) / 2
        Lx1 = a_l * x1 + b_l * iv.sqrt(x1)
        lfc = dL * (1 + x1) ** gam / m
        il = x1 * iv.log(1 + u / x1) + u * iv.log(1 + x1 / u)
        lg = iv.log(1 + u / x1)
        I_cr = (dL * (A_i * x1 + B_i * il) + dL / 2 * (A_q * x1 + B_q * il) + a_l * cj2 * x1 + 2 * b_l * cj2 * iv.sqrt(x1)
                + Lx1 * dj2 * x1 + lfc * (A_1 * x1 + B_1 * il))
        Hx1 = (dL * (A_i + B_i * lg) + dL / 2 * (A_q + B_q * lg) + a_l * cj2 + b_l * cj2 / iv.sqrt(x1) + Lx1 * dj2
               + lfc * (A_1 + B_1 * lg))
        self.I_cr = fhi(I_cr)
        self.T_cr = fhi(kap * x1 * Hx1)

    def bound(self, r_lo=None, r_hi=None):
        c = self.c
        if r_lo is None:
            mode = np.zeros(len(self.xl), int)
            rs = INF
            rf = np.ones(len(self.xl))
        else:
            mode = np.where(self.xr <= Dn(r_lo - 1.0), 0, np.where(self.xl > U(r_hi - 1.0), 1, 2))
            rs = fhi(iv.mpf(r_hi) ** c.I['gam'])
            rf = np.minimum(rs, self.onex_g)

        def comb(Iv, quad, lin, L, linL):
            linS = np.minimum(lin, U(linL * rs)) if np.isfinite(rs) else lin
            Lv = np.minimum(U(L * rf), U(quad + U(linL * rf)))
            Sv = U(quad + linS)
            return U(Iv + np.where(mode == 0, Sv, np.where(mode == 1, Lv, np.maximum(Sv, Lv))))

        H = comb(self.IH, self.quadH, self.linH, self.LH, self.linLH)
        TH = comb(self.IT, self.quadT, self.linT, self.LT, self.linLT)
        Hst = np.maximum.accumulate(H[::-1])[::-1]
        THst = np.maximum.accumulate(TH[::-1])[::-1]
        kap = c.kap_hi
        if self.bottom:
            legs = U(max(self.T_cr, THst[0]) + U(kap * U(U(self.I_cr + U(self.x1 * Hst[0])) + usum(U(Hst * self.dx)))))
            return float(U(self.TH0 + legs))
        integ = U(THst[0] + U(kap * usum(U(Hst * self.dx))))
        kmax = int(math.ceil(U(U(c.kap_hi * c.Kf_hi) / self.th_lo))) - 1
        if kmax <= 40000:
            z0 = float(Dn(self.th_lo / c.kap_hi))
            z = Dn(np.arange(1, kmax + 1) * z0)
            idx = np.clip(np.searchsorted(self.xl, z, side='right') - 1, 0, len(self.xl) - 1)
            legs = min(usum(THst[idx]), float(integ))
        else:
            legs = float(integ)
        return float(U(self.TH0 + legs))


def cell_sup(c, cell, dr=0.05):
    best, arg = cell.bound(None, None), None
    rmin = max(1.0, float(Dn(c.Ke_lo * cell.th_lo)))
    r_end = c.Kf1_hi
    if rmin < r_end:
        r = rmin
        while r < r_end:
            r2 = min(r + dr, r_end)
            v = cell.bound(r, r2)
            if v > best:
                best, arg = v, (r, r2)
            r = r2
    return best, arg


def Dprime_cert(Pstr, gam_str, q=1.03, nx=500, ns=700, dr=0.05, th_b=1e-7):
    """certified upper bound of D' (Section 4) at the parameters Pstr (decimal strings), gamma = gam_str."""
    c = Const(Pstr, gam_str)
    out = []
    cb = Cell(c, 0.0, th_b, nx, ns, bottom=True)
    v, a = cell_sup(c, cb, dr)
    out.append((0.0, th_b, v, a))
    hi = th_b
    while hi < 2.0:
        lo, hi = hi, min(hi * q, 2.0)
        cl = Cell(c, lo, hi, nx, ns)
        v, a = cell_sup(c, cl, dr)
        out.append((lo, hi, v, a))
    assert out[-1][1] == 2.0
    worst = max(out, key=lambda t: t[2])
    return worst[2], worst, len(out), c


# =====================================================================================================================
# output helpers
# =====================================================================================================================
def tex_num(x, d=6, strip=False):
    x = M(x)
    if x == 0:
        return '0'
    s = mp.nstr(x, d, min_fixed=-3, max_fixed=7, strip_zeros=strip)
    if 'e' in s:
        mant, ex = s.split('e')
        if strip and mant.endswith('.0'):
            mant = mant[:-2]
        if mant == '1':
            return r'10^{%d}' % int(ex)
        return r'%s\cdot10^{%d}' % (mant, int(ex))
    if s.endswith('.0'):
        s = s[:-2]
    return s


def tex_slack(s):
    if s == 0:
        return '0'
    return tex_num(s, 2, strip=True)


def tex_input(key):
    """an input exactly as printed"""
    t = INPUTS[key]
    if 'e' in t:
        mant, ex = t.split('e')
        return r'%s\cdot10^{%d}' % (mant, int(ex)) if mant != '1' else r'10^{%d}' % int(ex)
    return t


def pair_rows(cells, ncols):
    """cells: list of tuples (strings); returns rows with ncols cells per row (padding with empties)."""
    width = len(cells[0]) if cells else 1
    rows = []
    for i in range(0, len(cells), ncols):
        chunk = list(cells[i:i + ncols])
        while len(chunk) < ncols:
            chunk.append(('',) * width)
        rows.append(' & '.join(' & '.join(c) for c in chunk) + r' \\')
    return rows


# =====================================================================================================================
# main
# =====================================================================================================================
INPUTS = INPUT_SETS['S1G']
S1G = USE_S1G['S1G']
TD_TEX = OrderedDict([('T2', r'T_2'), ('Umax', r'U_{\max}'), ('csep', r'c_{\mathrm{sep}}'), ('kc', r'\kc'),
                      ('cN', r'c_N'), ('muTb', r'\muTb'), ('mub', r'\mub'), ('thv', r'\theta_{\mathrm v}'),
                      ('cT4', r'c_{T4}=\theta_{\mathrm t}/h_{\mathrm t}'), ('czlo', r'\czlo=h_{\mathrm t}\xi_-'),
                      ('czhi', r'\czhi=z_{\mathrm T}\xi_+'), ('cy', r'c_y'), ('WxL', r'W_x\hat L')])


def main():
    global I
    I = {k: M(s) for k, s in INPUTS.items()}
    del CONDS[:]
    L = []
    out = L.append
    out('verify_constants.py -- 50-digit verification of the constants of Appendix A')
    out('INPUTS: ' + ', '.join('%s=%s' % kv for kv in INPUTS.items()))
    t0 = time.time()
    # ---------------- certified D' at both tuples ----------------
    Pstr = dict(kap=INPUTS['kap'], cA=INPUTS['cA'], m=INPUTS['m'], Kf=INPUTS['Kf'], Ke=INPUTS['Keps'],
                qc=INPUTS['qc'], dL=INPUTS['dL'], d1=INPUTS['delta1'])
    kw = dict(q=1.03, nx=500, ns=700, dr=0.05)
    DPc = {}
    for tup, gs in (('p', INPUTS['gam']), ('pA', INPUTS['gD'])):
        val, worst, ncell, cc = Dprime_cert(Pstr, gs, **kw)
        DPc[tup] = val
        out("certified D'(%s) <= %.6f   (gamma=%s, %d theta-cells, worst cell theta in [%.5g,%.5g], r-cell %s; "
            "C_T in [%s, %s]; grid %s)" % (tup, val, gs, ncell, worst[0], worst[1], worst[3],
                                          mp.nstr(cc.I['CA'].a, 12), mp.nstr(cc.I['CA'].b, 12), kw))
    out('D\' time %.0fs' % (time.time() - t0))
    cond('near', r"$D'$ certified $\le$ printed\,[p]", M(DPc['p']), '<=', I['Dp'])
    cond('near', r"$D'$ certified $\le$ printed\,[p_{\mathrm A}]", M(DPc['pA']), '<=', I['DpA'])
    # ---------------- touch-down ----------------
    TD, SC = touchdown(I['vbar'], I['eta'], I['epsbar'], I['xi1'], I['lam0'], I['GT'])
    for (n, tex, l, rel, r) in SC:
        CONDS.append(('td', (n + ' ' + tex).strip(), l, rel, r))
    for key, ikey, direction in TD_USED:
        ex, pr = TD[key], I[ikey]
        name = TD_TEX[key].split('=')[0]
        if direction == 'up':
            cond('out', r'$%s$ (up)' % name, pr, '>=', ex)
        else:
            cond('out', r'$%s$ (down)' % name, pr, '<=', ex)
    # ---------------- core and assembly ----------------
    A, Dm, DA = assembly(S1G, {'p': I['Dp'], 'pA': I['DpA']})
    extra_conditions(TD, A, Dm, DA)
    nfail = 0
    out('\n%-5s %-78s %-26s %-3s %-26s %s' % ('grp', 'condition', 'left', 'rel', 'right', 'rel.slack'))
    for (grp, tex, l, rel, r) in CONDS:
        ok = holds(l, rel, r)
        nfail += (not ok)
        out('%-5s %-78s %-26s %-3s %-26s %-10s %s' % (grp, tex[:78], mp.nstr(l, 18), rel, mp.nstr(r, 18),
                                                      mp.nstr(slack(l, rel, r), 3), 'OK' if ok else '*** FAIL ***'))
    if not (Dm['_simplification_ok'] and DA['_simplification_ok']):
        out('*** Psi_I simplification not valid ***')
        nfail += 1
    else:
        out('\nSimplified Psi_I agrees with the general formula to 1e-45 (K_f + 1 <= K_R): OK')
    out('\nTouch-down constants, exact (50 digits):')
    for k in TD:
        out('  %-8s %s' % (k, mp.nstr(TD[k], 25)))
    out('\nCore derived constants (main p | stage A p_A):')
    for k in Dm:
        if k.startswith('_'):
            continue
        out('  %-8s %-30s %s' % (k, mp.nstr(Dm[k], 20), mp.nstr(DA[k], 20) if k in DA else '-'))
    out('\nAssembly constants:')
    for k in A:
        out('  %-8s %s' % (k, mp.nstr(A[k], 20)))
    n = len(CONDS)
    smallest = sorted(((slack(l, rel, r), tex, grp) for (grp, tex, l, rel, r) in CONDS), key=lambda x: x[0])[:45]
    out('\nSmallest relative slacks:')
    for s, tex, grp in smallest:
        out('  %-12s %-5s %s' % (mp.nstr(s, 3), grp, tex))
    groups = []
    for c_ in CONDS:
        if c_[0] not in groups:
            groups.append(c_[0])
    out('\nCondition count by group: ' + ', '.join('%s %d' % (gname, sum(1 for c in CONDS if c[0] == gname))
                                                 for gname in groups))
    out('T_sharp = %s, certified D\'(p) = %.6f, D\'(p_A) = %.6f, time %.0fs'
        % (mp.nstr(A['Tsharp'], 10), DPc['p'], DPc['pA'], time.time() - t0))
    write_tables(TD, Dm, DA, A, DPc)
    if nfail:
        out('\n%d OF %d CONDITIONS FAIL' % (nfail, n))
    else:
        out('\nALL %d CONDITIONS HOLD' % n)
    text = '\n'.join(L) + '\n'
    with open(os.path.join(HERE, 'verify_constants.out'), 'w', encoding='utf-8') as f:
        f.write(text)
    print('\n'.join(L[-16:]))
    sys.exit(1 if nfail else 0)


# =====================================================================================================================
# Tables A.1-A.4
# =====================================================================================================================
CORE_NAMES = OrderedDict([
    ('M', r'M'), ('chig', r'\chig'), ('c6', r'c_6'), ('rstar', r'r_*'), ('CT', r'\CT'), ('Cmu', r'\Cmu'),
    ('crho', r'c_\rho^*'), ('ceta', r'c_\eta'), ('cR', r'c_R^*'), ('K1', r'K_1'), ('K2', r'K_2'), ('camp', r'\camp'),
    ('J1', r'J_1(U_0)'), ('J2', r'J_2(U_0)'), ('B2Up', r"B_{2U}'"), ('B2eta', r'B_{2\eta}^*'), ('Cp', r"C_p'"),
    ('CpV', r'C_p^V'), ('Cps', r'C_p^*'), ('Car', r'C_{\mathrm{ar}}'), ('B3p', r"B_3'"), ('PsiI', r'\PsiI'),
    ('TI', r'\TI'), ('B5', r'B_5^*'), ('I5', r'I_5'), ('Xfar', r'\Xfar(U_0)'), ('LJ', r'\LJ(U_0)'), ('Dp', r"D'"),
    ('thbar', r'\bar\theta')])

ASM_NAMES = OrderedDict([
    ('zeta', r'\zeta'), ('etaN', r'\etaN'), ('etaD', r'\etaD'), ('We', r'\We'), ('delta0', r'\delta_0'),
    ('UA', r'\UA'), ('UE', r'\UE'), ('Dbar', r'\Dbar'), ('z0max', r'z_0^{\max}'), ('Xs', r'X_*'), ('Gf', r'G_f'),
    ('csepA', r'c^{\mathrm A}_{\mathrm{sep}}'), ('th0', r'\theta_0'), ('thy', r'\theta_y'), ('C0', r'C_0'),
    ('c0p', r"c_0'"), ('CTA', r'\CT^{\mathrm A}'),
    ('sigb', r'\bar\sigma'), ('thG', r'\theta_G'), ('ksig', r'k_\sigma'), ('C3', r'C_3'), ('ctau', r'c_\tau'),
    ('rhos', r'\rho_*'), ('Krot', r'K_{\mathrm{rot}}'), ('om0', r'\omega_0'), ('thh1', r'\theta_{h1}'),
    ('varth', r'\vartheta_h'), ('th0y', r'\theta_{0y}'), ('xc', r'x_c'), ('Lh', r'L_h'), ('Th0', r'\Theta_0'),
    ('Thb', r'\Theta_b'), ('Kw', r'K_w'), ('dt', r'\delta_t'), ('omT', r'\omega_T'), ('omy', r'\bar\omega_y'),
    ('kD', r'\kD'), ('Thp', r'\Theta_{\mathrm p}'), ('cn', r'c_n'), ('cbeta', r'c_\beta'),
    ('Ktail', r'c_n\Theta_b+c_\beta\Theta_{\mathrm p}'), ('C0Ra', r'C_0R^{a^\prime}'), ('TS', r'\mathrm{(TS)}'),
    ('TSrhs', r's_0m(K_f/K_R)^\nu'), ('PT', r'(1+\delta_t)\LJ(U_{\max})'), ('Tsharp', r'\Tsharp')])

TD_NAMES = OrderedDict([
    ('Q', r'Q'), ('Amin', r'\sA_{\min}'), ('Amax', r'\sA_{\max}'), ('Wall', r'W_{\mathrm{all}}'), ('Wb', r'W_{\mathrm b}'),
    ('Wv', r'W_{\mathrm v}'), ('uv', r'u_{\mathrm v}'), ('Wt', r'W_{\mathrm t}'), ('Wx', r'W_x'), ('Lhat', r'\hat L'),
    ('D0', r'\Delta_0'), ('kstar', r'k_*'), ('cfar', r'c_{\mathrm{far}}'), ('cnear', r'c_{\mathrm{near}}'),
    ('ctail', r'c_{\mathrm{tail}}'), ('tht', r'\theta_{\mathrm t}'), ('ht', r'h_{\mathrm t}'), ('zT', r'z_{\mathrm T}'),
    ('yT', r'y_{\mathrm T}'), ('xim', r'\xi_-'), ('xip', r'\xi_+'), ('xeb', r'\bar\xi_{\mathrm e}'),
    ('Chi', r'C_{\mathrm{hi}}'), ('Clo', r'C_{\mathrm{lo}}')])
SLACK_SHOWN = M('0.002')   # Table A.4 lists the conditions with relative slack below this


def write_tables(TD, Dm, DA, A, DPc):
    L = []
    w = L.append
    w('% appA_tables.tex -- GENERATED by verify_constants.py. Do not edit by hand.')
    # ---------------- Table A.1 ----------------
    w(r'\begin{table}[!htbp]\centering\footnotesize\setlength{\tabcolsep}{3pt}')
    w(r'\begin{tabular}{@{}ll@{\hspace{9pt}}ll@{\hspace{9pt}}ll@{\hspace{9pt}}ll@{\hspace{9pt}}ll@{\hspace{9pt}}ll@{}}\toprule')
    w(r'\multicolumn{12}{@{}l}{\emph{Free parameters} (both tuples; $\pA$ differs from $p$ only by $\gamma\mapsto\gD$), '
      r'\emph{dependent quantities, rounded up,}}\\')
    w(r'\multicolumn{12}{@{}l}{and the values of $D^\prime$ used in (P6)}\\\midrule')
    free = [(r'\gamma', 'gam'), (r'R', 'R'), (r'm', 'm'), (r's_0', 's0'), (r'\kappa', 'kap'), (r'c_A', 'cA'),
            (r'K_R', 'KR'), (r'K_f', 'Kf'), (r'\Keps', 'Keps'), (r'\eta_1', 'eta1'), (r'\qc', 'qc'), (r'\gD', 'gD'),
            (r'\dL', 'dL'), (r'\delta_1', 'delta1'), (r'\nu', 'nu'), (r'A_0', 'A0'), (r'\fF', 'fF'),
            (r"D^\prime[p]", 'Dp'), (r"D^\prime[\pA]", 'DpA')]
    cells = [('$%s$' % t, '$%s$' % tex_input(k)) for t, k in free]
    L += pair_rows(cells, 6)
    w(r'\bottomrule\end{tabular}')
    w(r'\par\medskip')
    w(r'\begin{tabular}{@{}lll@{\hspace{12pt}}lll@{\hspace{12pt}}lll@{}}\toprule')
    w(r'constant & $p$ & $\pA$ & constant & $p$ & $\pA$ & constant & $p$ & $\pA$\\\midrule')
    cells = [('$%s$' % t, '$%s$' % tex_num(Dm[k]), '$%s$' % tex_num(DA[k])) for k, t in CORE_NAMES.items()]
    L += pair_rows(cells, 3)
    w(r'\bottomrule\end{tabular}')
    w(r'\caption{Parameters of the end theorem (Section~\ref{sec:end}) and derived constants for the main tuple $p$ '
      r'($U_0=U_{\max}$) and the stage-A tuple $\pA$ ($U_0=\UA$), at $\vz=%s$, with the touch-down constants of '
      r'Theorem~\ref{thm:touchdown} and the function $\Cfl$ of \eqref{eq:asm}. The certified bounds of '
      r'Lemma~\ref{lem:Ne} are $D^\prime\le%.4f$ $[p]$ and $D^\prime\le%.4f$ $[\pA]$ (rounded up); $D^\prime$ in the table is the '
      r'printed value used. Derived values to six digits; the check uses $50$ digits.}\label{tab:core}'
      % (tex_input('v0'), math.ceil(DPc['p'] * 1e4) / 1e4, math.ceil(DPc['pA'] * 1e4) / 1e4))
    w(r'\end{table}')
    # ---------------- Table A.2 ----------------
    w(r'\begin{table}[!htbp]\centering\footnotesize\setlength{\tabcolsep}{3pt}')
    w(r'\begin{tabular}{@{}ll@{\hspace{10pt}}ll@{\hspace{10pt}}ll@{\hspace{10pt}}ll@{}}\toprule')
    cells = [('$%s$' % TD_NAMES[k], '$%s$' % tex_num(TD[k])) for k in TD_NAMES]
    L += pair_rows(cells, 4)
    w(r'\bottomrule\end{tabular}')
    w(r'\par\medskip')
    w(r'\begin{tabular}{@{}ll@{\hspace{10pt}}ll@{\hspace{10pt}}ll@{}}\toprule')
    cells = [('$%s$' % TD_TEX[k].split('=')[0], r'$%s\to%s$' % (tex_num(TD[k], 8), tex_input(ik)))
             for k, ik, d in TD_USED]
    L += pair_rows(cells, 3)
    w(r'\bottomrule\end{tabular}')
    w(r'\caption{Constants of Definition~\ref{def:tdconst} at $\vbar=%s$, $\eta=%s$, $\epsbar=%s$, $\xi_1=%s$, '
      r'$\lambda_0=%s$, $G_{\mathrm T}=%s$ (six digits; the check uses $50$ digits). Top: the ingredients of the '
      r'constants of Theorem~\ref{thm:touchdown}; all %d constants of Definition~\ref{def:tdconst} are listed in '
      r'\texttt{verify\_constants.out}. Bottom: the constants used in Theorem~\ref{thm:touchdown}, '
      r'Lemma~\ref{lem:T2star} and afterwards, exact value $\to$ value used; $c_{\mathrm{sep}},\kc,\czlo$ are rounded '
      r'down, the others up.}\label{tab:td}'
      % (tex_input('vbar'), tex_input('eta'), tex_input('epsbar'), tex_input('xi1'), tex_input('lam0'),
         tex_input('GT'), len(TD)))
    w(r'\end{table}')
    # ---------------- Table A.3 ----------------
    w(r'\begin{table}[!htbp]\centering\footnotesize\setlength{\tabcolsep}{3pt}')
    w(r'\begin{tabular}{@{}ll@{\hspace{10pt}}ll@{\hspace{10pt}}ll@{\hspace{10pt}}ll@{}}\toprule')
    w(r'\multicolumn{8}{@{}l}{\emph{Free:} $\bar\omega=%s$, $c_k=%s$, $\delta_0=%s\,R$; and $\vz=%s$, '
      r'$\epsS=%s$, $a^\prime=%s$, $C_0=c_N$}\\\midrule' % (INPUTS['omb'], INPUTS['ck'], INPUTS['d0fac'],
                                                         tex_input('v0'), tex_input('epsS'), INPUTS['ap']))
    cells = [('$%s$' % t, '$%s$' % tex_num(A[k])) for k, t in ASM_NAMES.items()]
    L += pair_rows(cells, 4)
    w(r'\bottomrule\end{tabular}')
    w(r'\caption{Constants of the assembly (Section~\ref{sec:proof}, Lemma~\ref{lem:heading}, '
      r'Theorem~\ref{thm:departure}), at $(\vz,\epsS)$ with the touch-down constants as used.}\label{tab:asm}')
    w(r'\end{table}')
    # ---------------- Table A.4: the conditions with the smallest margins ----------------
    rows = sorted(((slack(l, rel, r), grp, tex, l, rel, r) for (grp, tex, l, rel, r) in CONDS), key=lambda x: x[0])
    tight = [x for x in rows if x[0] < SLACK_SHOWN]
    w(r'\begin{table}[!htbp]\centering\scriptsize\setlength{\tabcolsep}{2.5pt}\renewcommand{\arraystretch}{1.05}')
    spec = r'@{\hspace{10pt}}'.join([r'>{\raggedright\arraybackslash}p{96pt}rrr'] * 2)
    w(r'\begin{tabular}{@{}%s@{}}\toprule' % spec)
    w(' & '.join(['condition & left & right & slack'] * 2) + r'\\\midrule')
    cells = []
    for (sl, grp, tex, l, rel, r) in tight:
        tex = tex.replace(r'\,[p_{\mathrm A}]', r'\,[$\pA$]').replace(r'\,[p]', r'\,[$p$]')
        cells.append((tex, '$%s$' % tex_num(l, 5, strip=True), '$%s$' % tex_num(r, 5, strip=True),
                      '$%s$' % tex_slack(sl)))
    half = (len(cells) + 1) // 2
    left, right = cells[:half], cells[half:]
    while len(right) < len(left):
        right.append(('',) * 4)
    for a, b in zip(left, right):
        L.append(' & '.join(a + b) + r' \\')
    w(r'\bottomrule\end{tabular}')
    w(r'\caption{The %d side conditions (of %d) with relative slack below $%s$, in increasing order of slack (difference '
      r'of the two sides divided by the larger one; sides to five digits); $[p]$, $[\pA]$ indicate the tuple, and ``(up)'', '
      r'``(down)'' the outward rounding of a touch-down constant (exact value against value used). The script '
      r'checks all %d conditions in $50$-digit arithmetic and lists each of them, with both sides and its slack, in '
      r'\texttt{verify\_constants.out}.}\label{tab:side}' % (len(tight), len(CONDS), tex_num(SLACK_SHOWN, 2, strip=True),
                                                             len(CONDS)))
    w(r'\end{table}')
    with open(os.path.join(HERE, 'appA_tables.tex'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')


if __name__ == '__main__':
    main()
