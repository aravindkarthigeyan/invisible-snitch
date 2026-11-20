"""verify_constants.py -- constants and side conditions of the paper
"A path fixed in advance that finds a slow fleeing point" (Appendix A).

Standalone: Python 3 and mpmath only, 50 significant digits.  Run from the directory of this file:

    python -I verify_constants.py

Inputs are the PRINTED numbers of Appendix A (dict INPUTS below, exactly as printed).  The script
  1. evaluates the touch-down constants of Definition 7.1 at (vbar, eta, epsbar, xi1, lambda0, G_T) and checks the
     side conditions (SC1)-(SC48), and checks that every touch-down constant used downstream (Theorem 7.12) is printed
     on the safe side of its exact value;
  2. evaluates the derived constants of the end theorem (Section 3, "Parameters") for the main tuple p (U0 = U_max)
     and the stage-A tuple p_A (gamma -> gamma_D, U0 = U_A), and checks (P0)-(P7) and (C1)-(C6);
  3. evaluates the assembly constants of Section 8.1 (heading Lemma 5.1, departure Theorem 5.2, (TS), T_0^sharp) and
     checks (A2)-(A6);
  4. checks further elementary inequalities used in the proofs;
  5. writes appA_tables.tex (Tables A.1-A.4; Table A.4 lists only the conditions with the smallest margins) and
     verify_constants.out (full log, with every condition, both sides and its relative slack, and all constants).
The downstream computations (2, 3) use the PRINTED (outward-rounded) touch-down constants, never the exact ones.
Exit status 0 iff every condition holds.  The final line is "ALL <n> CONDITIONS HOLD".
"""
import os
import sys
from collections import OrderedDict

import mpmath as mp

mp.mp.dps = 50
M = mp.mpf
sin, cos, tan, asin, acos = mp.sin, mp.cos, mp.tan, mp.asin, mp.acos
sqrt, pi, exp, log = mp.sqrt, mp.pi, mp.exp, mp.log
HERE = os.path.dirname(os.path.abspath(__file__))

# =====================================================================================================================
# Section 1. INPUTS: the printed numbers of Appendix A (strings exactly as printed)
# =====================================================================================================================
INPUTS = OrderedDict([
    # main theorem
    ('v0', '6e-5'), ('epsS', '4e-11'), ('T0', '10.13'),
    # touch-down parameters
    ('vbar', '6e-5'), ('eta', '0.1'), ('epsbar', '1e-3'), ('xi1', '1.007'), ('lam0', '0.0333'), ('GT', '0.05'),
    # touch-down constants used downstream (Theorem 7.12; outward rounded)
    ('T2', '3.73247'), ('Umax', '6.29320'), ('csep', '0.0330591'), ('kc', '0.988089'), ('cN', '2.72160'),
    ('muTb', '1.79990e-4'), ('mub', '6.00037e-5'), ('ap', '0.99982'), ('thv', '1.07003'), ('cT4', '1.04263'),
    ('czlo', '1.27025'), ('czhi', '1.56563'), ('cy', '0.619797'),
    # core free parameters (both tuples except gamma)
    ('gam', '0.614267'), ('R', '0.001014'), ('m', '0.0561202'), ('s0', '0.0543222'), ('kap', '1.01594'),
    ('cA', '0.996095'), ('KR', '31.9496'), ('Kf', '5.03588'), ('Keps', '999.98'), ('eta1', '0.834088'),
    ('qc', '2.05829'),
    # dependent quantities, rounded up (inputs)
    ('dL', '1.0000602'), ('delta1', '1.0001202'), ('nu', '3.10668e-4'), ('A0', '1.01292'), ('fF', '0.136962'),
    ('gD', '0.614666'),
    # assembly free parameters (delta0 = d0fac * R)
    ('omb', '0.338254'), ('ck', '1.21399'), ('d0fac', '0.149785'),
])
I = {k: M(s) for k, s in INPUTS.items()}

# =====================================================================================================================
# condition bookkeeping
# =====================================================================================================================
CONDS = []   # (group, tex, left, rel, right)


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
# Section 2. touchdown(): Definition 7.1 and (SC1)-(SC51)
# =====================================================================================================================
def touchdown(vbar, eta, eb, xi1, lam0, G):
    v = vbar
    mu = v / (1 - v)                     # \bar\mu
    muT = 3 * v / (1 + v)                # \bar\mu_T
    K = OrderedDict()
    SC = []

    def sc(n, tex, left, rel, right):
        SC.append(('(SC%s)' % n, tex, M(left), rel, M(right)))

    half = M(1) / 2
    # basic
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
    # run 1
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
    # window
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
    # forward arc
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
    # virtual labels
    thv = Q ** mu * exp(mu) * (thf + mu * exp(2 * mu) * yf * xi1)
    Wv = Wf * exp(2 * mu)
    uv = Wv * xi1
    K.update(thv=thv, Wv=Wv, uv=uv)
    # tail
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
    # bulk and hole
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
    # assembly
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
             ctail=ctail, cN=cN, cy=cy, cT4=cT4, czlo=ht * xim, czhi=zT * xip)

    # ---- side conditions (SC1)-(SC51), in the order of Definition 7.1 ----
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
    # (the record's lambda_0 <= 1/4, kappa_c >= 1/2 and c_N lambda_0^{1-muTb} <= 1 are used in no proof; removed)
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
    return K, SC


# TeX names of the constants of Definition 7.1 (renames of the short paper)
TD_NAMES = OrderedDict([
    ('t1b', r'\bar t_1'), ('gb', r'\gb'), ('alo', r'\underline\alpha'), ('Da', r'\Delta_{\mathrm a}'), ('d1', r'd_1'),
    ('erho', r'e_\rho'), ('T2', r'T_2'), ('ds', r'd_{\mathrm s}'), ('dP', r'd_P'), ('rhomid', r'\rho_{\mathrm{mid}}'),
    ('karm', r'k_{\mathrm{arm}}'), ('darm', r'd_{\mathrm{arm}}'), ('e1', r'e_1'), ('E1', r'\mathcal E_1'),
    ('Warm', r'W_{\mathrm{arm}}'), ('kall', r'k_{\mathrm{all}}'), ('Wall', r'W_{\mathrm{all}}'),
    ('thL', r'\theta_L'), ('thR', r'\theta_R'), ('RL', r'R_L'), ('RR', r'R_R'), ('rmin', r'\sr_{\min}'),
    ('rmax', r'\sr_{\max}'), ('rhow', r'\rho_{\mathrm w}'), ('Ww', r'W_{\mathrm w}'), ('omw', r'\omega_{\mathrm w}'),
    ('vkw', r'\vk_{\mathrm w}'), ('iotaw', r'\iota_{\mathrm w}'), ('qmin', r'q_{\min}'), ('qmax', r'q_{\max}'),
    ('ellmin', r'\ell_{\min}'), ('ellmax', r'\ell_{\max}'), ('Lmin', r'\Lambda_{\min}'), ('Lmax', r'\Lambda_{\max}'),
    ('m0', r'm_0'), ('omp', r'\omega_{\mathrm p}'), ('angw', r'\angle_{\mathrm w}'), ('Amin', r'\sA_{\min}'),
    ('Amax', r'\sA_{\max}'), ('blo', r'b_{\mathrm{lo}}'), ('bhi', r'b_{\mathrm{hi}}'), ('bbar', r'\bar b'),
    ('etau', r'e_\tau'), ('beta2', r'\beta_2'), ('Chi', r'C_{\mathrm{hi}}'), ('Clo', r'C_{\mathrm{lo}}'),
    ('aux', r'\mathrm{aux}'), ('amin', r'\sa_{\min}'), ('amax', r'\sa_{\max}'), ('LC', r'L_C'),
    ('Llo', r'L_{\mathrm{lo}}'), ('S1', r'S_1'), ('hf', r'h_{\mathrm f}'), ('rhoc', r'\rho_{\mathrm c}'), ('Q', r'Q'),
    ('yf', r'y_{\mathrm f}'), ('Y1', r'Y_1'), ('Ybar', r'\bar Y'), ('thf', r'\theta_{\mathrm f}'),
    ('Wf', r'W_{\mathrm f}'), ('dfw', r'\delta_{\mathrm{fw}}'), ('tauf', r'\tau_{\mathrm f}'),
    ('taufb', r'\bar\tau_{\mathrm f}'), ('rhou', r'\rho_{\mathrm u}'), ('S2', r'S_2'), ('kf', r'k_{\mathrm f}'),
    ('thv', r'\theta_{\mathrm v}'), ('Wv', r'W_{\mathrm v}'), ('uv', r'u_{\mathrm v}'), ('xim', r'\xi_-'),
    ('xip', r'\xi_+'), ('xeb', r'\bar\xi_{\mathrm e}'), ('dtl', r'\delta_{\mathrm{tl}}'), ('ht', r'h_{\mathrm t}'),
    ('hT', r'h_{\mathrm T}'), ('mtau', r'm_\tau'), ('taut', r'\tau_{\mathrm t}'), ('et', r'e_{\mathrm t}'),
    ('yc', r'y_{\mathrm c}'), ('yT', r'y_{\mathrm T}'), ('Tt', r'T_{\mathrm t}'), ('Y2', r'Y_2'),
    ('Y2b', r'\bar Y_2'), ('tht', r'\theta_{\mathrm t}'), ('zT', r'z_{\mathrm T}'), ('rhoT', r'\rho_{\mathrm T}'),
    ('Wt', r'W_{\mathrm t}'), ('S3', r'S_3'), ('kt', r'k_{\mathrm t}'), ('xi2', r'\xi_2'), ('ha', r'h_{\mathrm a}'),
    ('Qa', r'Q_{\mathrm a}'), ('taua', r'\tau_{\mathrm a}'), ('ebeta', r'e_\beta'), ('bl', r'b_{\mathrm l}'),
    ('yb', r'y_{\mathrm b}'), ('Hb', r'H_{\mathrm b}'), ('Tb', r'T_{\mathrm b}'), ('Sb', r'S_{\mathrm b}'),
    ('kb', r'k_{\mathrm b}'), ('Wb', r'W_{\mathrm b}'), ('rB', r'r_{\mathrm B}'), ('rhoh', r'\rho_{\mathrm h}'),
    ('Wx', r'W_x'), ('Umax', r'U_{\max}'), ('Lhat', r'\hat L'), ('D0', r'\Delta_0'), ('csep', r'c_{\mathrm{sep}}'),
    ('kc', r'\kc'), ('kstar', r'k_*'), ('cfar', r'c_{\mathrm{far}}'), ('cnear', r'c_{\mathrm{near}}'),
    ('ctail', r'c_{\mathrm{tail}}'), ('cN', r'c_N'), ('cy', r'c_y'), ('cT4', r'c_{T4}'),
])

# the touch-down constants used downstream: (key of Def 7.1 dict, key of INPUTS, TeX, direction)
TD_USED = [('T2', 'T2', r'T_2', 'up'), ('Umax', 'Umax', r'U_{\max}', 'up'),
           ('csep', 'csep', r'c_{\mathrm{sep}}', 'down'), ('kc', 'kc', r'\kc', 'down'), ('cN', 'cN', r'c_N', 'up'),
           ('muTb', 'muTb', r'\muTb', 'up'), ('mub', 'mub', r'\mub', 'up'), ('thv', 'thv', r'\theta_{\mathrm v}', 'up'),
           ('cT4', 'cT4', r'c_{T4}=\theta_{\mathrm t}/h_{\mathrm t}', 'up'),
           ('czlo', 'czlo', r'\czlo=h_{\mathrm t}\xi_-', 'down'),
           ('czhi', 'czhi', r'\czhi=z_{\mathrm T}\xi_+', 'up'), ('cy', 'cy', r'c_y', 'up')]


# the touch-down constants printed in Table A.2 (ingredients of the constants of Theorem 7.12); all are in the log
TD_SHOW = ['Q', 'Amin', 'Amax', 'Wall', 'Wb', 'Wv', 'uv', 'Wt', 'Wx', 'Lhat', 'D0', 'kstar', 'cfar', 'cnear', 'ctail',
           'tht', 'ht', 'zT', 'yT', 'xim', 'xip', 'xeb', 'Chi', 'Clo']
SLACK_SHOWN = M('0.002')   # Table A.4 lists the conditions with relative slack below this


# =====================================================================================================================
# Section 3. core(p, U0) and corollary(...): Section 3 "Parameters", (P0)-(P7), (C0)-(C6)
# =====================================================================================================================
def aD(K):
    return 1 + 1 / K + 2 / K ** 2


def core(gam, U0, v0, tag):
    R, m, s0, kap, cA = I['R'], I['m'], I['s0'], I['kap'], I['cA']
    KR, Kf, Ke, eta1, qc = I['KR'], I['Kf'], I['Keps'], I['eta1'], I['qc']
    dL, dl1, nu, A0, fF = I['dL'], I['delta1'], I['nu'], I['A0'], I['fF']
    D = OrderedDict()
    D['M'] = m * R ** (-gam)
    chig = kap * dL
    c6 = (1 + dl1) / cA
    ct = lambda r: (sqrt(kap) * r ** (M(1) / 2 + gam) + m / 2) / cA
    sq = 1 / (1 - qc ** (-gam))
    CA = sq * ct(qc)
    CB = CA + ct(M(3))
    CTL = CA + CB
    CmuA = 1 + kap * CA ** 2
    C1A = sqrt(kap * CmuA)
    crho = cA - (2 * dl1 + kap) / Kf
    cR = cA * KR - dl1 / Ke - kap
    K1 = crho * Kf / kap
    K2 = cR / kap
    camp = aD(K1) * chig / crho
    B2U = 2 * kap ** M(1.5) * (1 + 1 / K2) / cR ** 2
    B2eta = 2 * kap ** M(1.5) * (1 + 1 / K1) / crho ** 2 * (chig / eta1 + dL / (Ke * eta1 ** 2))
    rf = 1 + 1 / (Kf - 2)
    Cp = kap * (ct(rf) + CB * (1 + 1 / Kf) ** gam)
    B3 = 2 * kap ** M(1.5) * Cp / crho ** 3
    PsiI = 2 + log(Kf)
    TI = dL * (kap * c6 + 2) + c6 * chig * PsiI
    Ta = dL / c6 + chig * (2 + log(Kf))
    Tb = 2 ** gam * (2 * dL + chig * (M(3) / 4 + (Kf ** gam - 1) / (2 * gam)))
    k0 = max(C1A, kap * 2 ** gam * CA)
    DI = CmuA * TI
    DIIs = c6 ** 2 * C1A ** 2 * Ta + 2 * c6 ** 2 * kap * CTL * C1A * Tb + 4 * dL * c6 * C1A * k0
    DIIl = c6 * (Kf + 1) ** gam * C1A * Ta / m
    B5 = 2 / crho * ((Cp + sqrt(kap) * Kf ** (-1 - gam)) ** 2 / crho ** 2 + Kf ** (-2 * gam))
    # Proposition 4.4 needs only chi_g (eta_1 R + eps/kappa)^{2 gamma}/(2 gamma) <= I_5 R^{2 gamma}; the record's second
    # summand d_L (K_f/2)^{2 gamma - 1} K_eps^{-2 gamma} was slack and is dropped (this only decreases L_J).
    I5 = chig * (eta1 + 1 / Ke) ** (2 * gam) / (2 * gam)
    Xfar = v0 * (chig * U0 / (cR * R) + (dL / (Ke * eta1) + chig * log(KR / eta1)) / crho)
    LJexp = exp(Xfar + B5 * I5 * v0 * m ** 2)
    LJ = LJexp + v0 * kap * TI
    thbar = fF ** 2 + 2 * v0 * (DI + max(DIIs, DIIl))
    D.update(chig=chig, c6=c6, sq=sq, CA=CA, CB=CB, CTL=CTL, CmuA=CmuA, C1A=C1A, crho=crho, cR=cR, K1=K1, K2=K2,
             camp=camp, B2U=B2U, B2eta=B2eta, rf=rf, Cp=Cp, B3=B3, PsiI=PsiI, TI=TI, Ta=Ta, Tb=Tb, k0=k0,
             DI=DI, DIIs=DIIs, DIIl=DIIl, B5=B5, I5=I5, Xfar=Xfar, LJ=LJ, thbar=thbar, LJexp=LJexp)
    # general (unsimplified) formulas, to confirm the simplified Psi_I and D_IIl do not change any value on the branch
    # gamma > 1/2, K_f + 1 <= K_R (T_n enters only through the iota-term, which vanishes on this branch)
    PsiI_gen = 2 + log(min(Kf, KR)) + max(Kf - KR, 0) / KR
    iota = 1 if Kf + 1 > KR else 0
    Tn = chig * Kf + 2 * dL
    DIIl_gen = c6 * (Kf + 1) ** gam / m * (C1A * Ta + iota * sqrt(kap) * Tn / KR)
    tol = M(10) ** -45
    D['_simplification_ok'] = (abs(PsiI_gen - PsiI) < tol and abs(DIIl_gen - DIIl) < tol * DIIl
                               and gam > M(1) / 2 and Kf + 1 <= KR)

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
    cond(g, r'(P0) $\Keps\ge3/2$' + t, Ke, '>=', M(3) / 2)
    cond(g, r'(P0) $0<\eta_1$' + t, 0, '<', eta1)
    cond(g, r'(P0) $\eta_1\le K_f/(K_f+1)$' + t, eta1, '<=', Kf / (Kf + 1))
    cond(g, r'(P0) $\qc>1$' + t, qc, '>', 1)
    cond(g, r'(P0) $\nu\ge0$' + t, nu, '>=', 0)
    cond(g, r'(P0) $\dL\ge1$' + t, dL, '>=', 1)
    cond(g, r'(P0) $\delta_1\ge1$' + t, dl1, '>=', 1)
    cond(g, r'(P0) $A_0\ge1$' + t, A0, '>=', 1)
    cond(g, r'(P0) $0<\vz<1$' + t, v0, '<', 1)
    cond(g, r'(P1) $1/(1-\vz)\le\dL$' + t, 1 / (1 - v0), '<=', dL)
    cond(g, r'(P1) $e^{2\vz/(1-\vz)}\le\delta_1$' + t, exp(2 * v0 / (1 - v0)), '<=', dl1)
    cond(g, r'(P2) $c_\rho K_f\ge2$' + t, crho * Kf, '>=', 2)
    cond(g, r'(P2) $c_R\Keps\ge1$' + t, cR * Ke, '>=', 1)
    cond(g, r'(P2) $c_6\le K_R\Keps$' + t, c6, '<=', KR * Ke)
    cond(g, r'(P3) $\camp\vz\le\nu$' + t, camp * v0, '<=', nu)
    cond(g, r'(P4)' + t, v0 * (2 * aD(K1) * dL / (crho * Kf) + aD(K2) * chig * U0 / (cR * R)), '<=', log(A0))
    P5 = A0 * (s0 + (KR / Kf) ** nu * v0 / m * (B2U * chig * U0 / R + B2eta)
               + B3 * Kf ** (gam - 1) * (2 * dL / Kf + chig / (1 - gam - nu)) * v0)
    cond(g, r'(P5)' + t, P5, '<=', fF)
    cond(g, r'(P6) $\bar\theta<1$' + t, thbar, '<', 1)
    cond(g, r'(P7) $L_J(U_0)<\kappa$' + t, LJ, '<', kap)
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
# Section 4. assembly(): Section 8.1, Lemma 5.1, Theorem 5.2; (A2)-(A6), (TS), T_0^sharp
# =====================================================================================================================
def assembly():
    v0, eps = I['v0'], I['epsS']
    R, m, s0, kap, cA, KR, Kf, Ke = I['R'], I['m'], I['s0'], I['kap'], I['cA'], I['KR'], I['Kf'], I['Keps']
    nu, dl1, gam, gD = I['nu'], I['delta1'], I['gam'], I['gD']
    T2, Umax, csep, kc, cN = I['T2'], I['Umax'], I['csep'], I['kc'], I['cN']
    muTb, mub, ap, thv, cT4, czlo, czhi, cy = I['muTb'], I['mub'], I['ap'], I['thv'], I['cT4'], I['czlo'], I['czhi'], I['cy']
    lam0, GT, epsbar, vbar = I['lam0'], I['GT'], I['epsbar'], I['vbar']
    omb, ck = I['omb'], I['ck']
    A = OrderedDict()
    zeta = sqrt(1 - omb ** 2) - v0
    etaN = M('1.375') * v0 / zeta
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
    # the two core tuples
    Dm = core(gam, Umax, v0, 'p')
    corollary(gam, ap, C0, lam0, csep, 'p')
    DA = core(gD, UA, v0, r'p_{\mathrm A}')
    corollary(gD, ap, C0, lam0, csepA, r'p_{\mathrm A}')
    # heading (Lemma 5.1)
    sigb = thv * Gf ** (1 - mub)
    thG = thv * Gf ** (1 - mub - gD)
    ksig = (1 + sigb / 2) / (1 - sigb ** 2 / 2)
    C3 = 2 * DA['CB'] + DA['CA']
    ctau = 1 / (1 - m ** 2 / 2)
    rhos = cA * (R - delta0 - eps) - dl1 * eps
    Krot = kap / (1 - v0) * (2 * R / (cA * delta0) + (We + eps) / rhos)
    om0 = DA['CA'] * m * (delta0 / R) ** gD + ksig * sigb + v0 * Krot
    thh1 = (DA['CA'] * m * R ** (-gD) + 2 ** gD * ksig * thG
            + v0 * 4 * kap * C3 * m / (cA * (1 - v0)) * 2 ** gD * R ** (-gD))
    varth = ctau ** gD * max(thh1, om0 * delta0 ** (-gD))
    A.update(sigb=sigb, thG=thG, ksig=ksig, C3=C3, ctau=ctau, rhos=rhos, Krot=Krot, om0=om0, thh1=thh1, varth=varth)
    # departure (Theorem 5.2), gamma = gamma_D
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
    cbeta = 2 * (1 + dt) ** M(1.5) * kD ** (gD - 1) / (zeta ** 3 * (1 - gD))
    Ktail = cn * Thb + cbeta * Thp
    TS = (1 + Dbar / (kD * R)) ** etaN * (C0 * R ** ap + v0 * Ktail * R ** gD)
    TSrhs = s0 * m * (Kf / KR) ** nu
    A.update(th0y=th0y, xc=xc, Lh=Lh, Th0=Th0, Thb=Thb, Kw=Kw, dt=dt, omT=omT, omy=omy, kD=kD, Thp=Thp, cn=cn,
             cbeta=cbeta, Ktail=Ktail, TS=TS, TSrhs=TSrhs, C0Ra=C0 * R ** ap, PT=(1 + dt) * Dm['LJ'],
             Tsharp=Tsharp)
    # ---- side conditions ----
    g = 'asm'
    # (A2) extra
    cond(g, r'(A2) $1-\UA\ge\We$', 1 - UA, '>=', We)
    # (A3) heading
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
    # (A4) departure
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
    # (k_D >= 4(1+delta_t)/zeta, used in Theorem 5.2(v), is k_D = c_k 4(1+delta_t)/zeta with c_k >= 1, checked above)
    # (A5) tail start
    cond(g, r'(A5) $\gD\ge\gamma+\nu+\etaN$', gD, '>=', gam + nu + etaN)
    cond(g, r'(A5) $\gD+\nu\le a^\prime$', gD + nu, '<=', ap)
    cond(g, r'(A5) (TS)', TS, '<=', TSrhs)
    cond(g, r'(A5) $K_RR\le1-\UE-\We-\epsS$', KR * R, '<=', 1 - UE - We - eps)
    cond(g, r'(A5) (PT)', (1 + dt) * Dm['LJ'], '<', kap)
    # (A6) and touch-down range
    cond(g, r'(A6) $\vz\le\vbar$', v0, '<=', vbar)
    cond(g, r'(A6) $\epsS\le\epsbar$', eps, '<=', epsbar)
    cond(g, r'(A6) $\epsS\le R/\Keps$', eps, '<=', R / Ke)
    cond(g, r'(A6) $2\We+R+\epsS\le1$', 2 * We + R + eps, '<=', 1)
    cond(g, r'(A6) $K_RR<\lambda_0$', KR * R, '<', lam0)
    cond(g, r"(A6) $a^\prime\le1-\muTb$ (printed $\muTb$)", ap, '<=', 1 - muTb)
    cond(g, r'(A6) $\Tsharp\le10.13$', Tsharp, '<=', I['T0'])
    return A, Dm, DA


# =====================================================================================================================
# notes of the other writers (merged conditions)
# =====================================================================================================================
def extra_conditions(TD, A, Dm, DA):
    """Further inequalities used in the proofs without being listed side conditions (reported in short/notes_W2..W4.md,
    and two used in Section 7.3).  W1 reported none."""
    g = 'extra'
    kap, cA, Kf, KR, m, omb = I['kap'], I['cA'], I['Kf'], I['KR'], I['m'], I['omb']
    # Sections 3-4 (W2)
    cond(g, r'$\kappa\le\CTL^2(4-\kappa^2)$\,[$p$]', kap, '<=', Dm['CTL'] ** 2 * (4 - kap ** 2))
    cond(g, r'$\kappa\le\CTL^2(4-\kappa^2)$\,[$\pA$]', kap, '<=', DA['CTL'] ** 2 * (4 - kap ** 2))
    cond(g, r'$\frac32\kappa-1\le1$', M(3) / 2 * kap - 1, '<=', 1)
    ct3 = lambda gam: (sqrt(kap) * M(3) ** (M(1) / 2 + gam) + m / 2) / cA
    cond(g, r'$c_t(3)\ge\sqrt3$\,[$p$]', ct3(I['gam']), '>=', sqrt(3))
    cond(g, r'$c_t(3)\ge\sqrt3$\,[$\pA$]', ct3(I['gD']), '>=', sqrt(3))
    cond(g, r'$c_A/2<1\le\delta_1$', cA / 2, '<', 1)
    # Sections 5 and 8 (W3)
    cond(g, r'$c_\tau\ge1$', A['ctau'], '>=', 1)
    cond(g, r'$K_f<K_R$', Kf, '<', KR)
    cond(g, r'$\zeta\le1-\bar\omega^2/2$', A['zeta'], '<=', 1 - omb ** 2 / 2)
    cond(g, r'$\lambda_0<1$', I['lam0'], '<', 1)
    cond(g, r'$\zeta\le1$', A['zeta'], '<=', 1)
    # Section 7 (W4, W5)
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


def main():
    log_lines = []
    out = log_lines.append
    out('verify_constants.py -- 50-digit verification of the constants of Appendix A')
    out('INPUTS: ' + ', '.join('%s=%s' % kv for kv in INPUTS.items()))

    # ---------------- touch-down ----------------
    TD, SC = touchdown(I['vbar'], I['eta'], I['epsbar'], I['xi1'], I['lam0'], I['GT'])
    for (n, tex, l, rel, r) in SC:
        CONDS.append(('td', n + ' ' + tex, l, rel, r))
    # outwardness of the constants used downstream
    for key, ikey, tex, direction in TD_USED:
        ex, pr = TD[key], I[ikey]
        if direction == 'up':
            cond('out', r'$%s$ (up)' % tex.split('=')[0], pr, '>=', ex)
        else:
            cond('out', r'$%s$ (down)' % tex.split('=')[0], pr, '<=', ex)

    # ---------------- core and assembly ----------------
    A, Dm, DA = assembly()
    extra_conditions(TD, A, Dm, DA)

    # ---------------- evaluation ----------------
    nfail = 0
    out('\n%-4s %-70s %-28s %-3s %-28s %s' % ('grp', 'condition', 'left', 'rel', 'right', 'rel.slack'))
    for (grp, tex, l, rel, r) in CONDS:
        ok = holds(l, rel, r)
        nfail += (not ok)
        out('%-4s %-70s %-28s %-3s %-28s %-10s %s' % (grp, tex[:70], mp.nstr(l, 20), rel, mp.nstr(r, 20),
                                                      mp.nstr(slack(l, rel, r), 3), 'OK' if ok else '*** FAIL ***'))
    if not (Dm['_simplification_ok'] and DA['_simplification_ok']):
        out('*** the simplified core formulas differ from the general formulas ***')
        nfail += 1
    else:
        out('\nSimplified Psi_I, D_IIl agree with the general formulas to 1e-45 (gamma > 1/2, K_f + 1 <= K_R): OK')

    out('\nTouch-down constants, exact (50 digits):')
    for k in TD_NAMES:
        out('  %-8s %s' % (k, mp.nstr(TD[k], 25)))
    out('\nCore derived constants (main p | stage A p_A):')
    for k in Dm:
        if k.startswith('_'):
            continue
        out('  %-8s %-30s %s' % (k, mp.nstr(Dm[k], 20), mp.nstr(DA[k], 20)))
    out('\nAssembly constants:')
    for k in A:
        out('  %-8s %s' % (k, mp.nstr(A[k], 20)))

    n = len(CONDS)
    smallest = sorted(((slack(l, rel, r), tex, grp) for (grp, tex, l, rel, r) in CONDS), key=lambda x: x[0])[:25]
    out('\nSmallest relative slacks:')
    for s, tex, grp in smallest:
        out('  %-12s %s %s' % (mp.nstr(s, 3), grp, tex))
    out('\nCondition count by group: ' + ', '.join('%s %d' % (gname, sum(1 for c in CONDS if c[0] == gname))
                                                 for gname in ('td', 'out', 'core', 'cor', 'asm', 'extra')))

    write_tables(TD, Dm, DA, A)

    if nfail:
        out('\n%d OF %d CONDITIONS FAIL' % (nfail, n))
    else:
        out('\nALL %d CONDITIONS HOLD' % n)
    text = '\n'.join(log_lines) + '\n'
    with open(os.path.join(HERE, 'verify_constants.out'), 'w', encoding='utf-8') as f:
        f.write(text)
    print('\n'.join(log_lines[-14:]))
    sys.exit(1 if nfail else 0)


# =====================================================================================================================
# Tables A.1-A.4
# =====================================================================================================================
CORE_NAMES = OrderedDict([
    ('M', r'M'), ('chig', r'\chig'), ('c6', r'c_6'), ('sq', r'\sigma_q'), ('CA', r'C_A'), ('CB', r'C_B'),
    ('CTL', r'\CTL'), ('CmuA', r'\CmuA'), ('C1A', r'\ConeA'), ('crho', r'c_\rho'), ('cR', r'c_R'), ('K1', r'K_1'),
    ('K2', r'K_2'), ('camp', r'\camp'), ('B2U', r'B_{2U}'), ('B2eta', r'B_{2\eta}'), ('rf', r'r_f'), ('Cp', r'C_p'),
    ('B3', r'B_3'), ('PsiI', r'\PsiI'), ('TI', r'\TI'), ('Ta', r'\Ta'), ('Tb', r'\Tb'),
    ('k0', r'k_0'), ('DI', r'\DI'), ('DIIs', r'\DIIs'), ('DIIl', r'\DIIl'), ('B5', r'B_5'), ('I5', r'I_5'),
    ('Xfar', r'\Xfar(U_0)'), ('LJ', r'\LJ(U_0)'), ('thbar', r'\bar\theta')])

ASM_NAMES = OrderedDict([
    ('zeta', r'\zeta'), ('etaN', r'\etaN'), ('etaD', r'\etaD'), ('We', r'\We'), ('delta0', r'\delta_0'),
    ('UA', r'\UA'), ('UE', r'\UE'), ('Dbar', r'\Dbar'), ('z0max', r'z_0^{\max}'), ('Xs', r'X_*'), ('Gf', r'G_f'),
    ('csepA', r'c^{\mathrm A}_{\mathrm{sep}}'), ('th0', r'\theta_0'), ('thy', r'\theta_y'), ('C0', r'C_0'),
    ('sigb', r'\bar\sigma'), ('thG', r'\theta_G'), ('ksig', r'k_\sigma'), ('C3', r'C_3'), ('ctau', r'c_\tau'),
    ('rhos', r'\rho_*'), ('Krot', r'K_{\mathrm{rot}}'), ('om0', r'\omega_0'), ('thh1', r'\theta_{h1}'),
    ('varth', r'\vartheta_h'), ('th0y', r'\theta_{0y}'), ('xc', r'x_c'), ('Lh', r'L_h'), ('Th0', r'\Theta_0'),
    ('Thb', r'\Theta_b'), ('Kw', r'K_w'), ('dt', r'\delta_t'), ('omT', r'\omega_T'), ('omy', r'\bar\omega_y'),
    ('kD', r'\kD'), ('Thp', r'\Theta_{\mathrm p}'), ('cn', r'c_n'), ('cbeta', r'c_\beta'),
    ('Ktail', r'c_n\Theta_b+c_\beta\Theta_{\mathrm p}'), ('C0Ra', r'C_0R^{a^\prime}'), ('TS', r'\mathrm{(TS)}'),
    ('TSrhs', r's_0m(K_f/K_R)^\nu'), ('PT', r'(1+\delta_t)\LJ(U_{\max})'), ('Tsharp', r'\Tsharp')])


def write_tables(TD, Dm, DA, A):
    L = []
    w = L.append
    w('% appA_tables.tex -- GENERATED by verify_constants.py. Do not edit by hand.')
    # ---------------- Table A.1 ----------------
    w(r'\begin{table}[!htbp]\centering\footnotesize\setlength{\tabcolsep}{3pt}')
    w(r'\begin{tabular}{@{}ll@{\hspace{9pt}}ll@{\hspace{9pt}}ll@{\hspace{9pt}}ll@{\hspace{9pt}}ll@{\hspace{9pt}}ll@{}}\toprule')
    w(r'\multicolumn{12}{@{}l}{\emph{Free parameters} (both tuples; $\pA$ differs from $p$ only by $\gamma\mapsto\gD$), and '
      r'\emph{dependent quantities, rounded up}}\\\midrule')
    free = [(r'\gamma', 'gam'), (r'R', 'R'), (r'm', 'm'), (r's_0', 's0'), (r'\kappa', 'kap'), (r'c_A', 'cA'),
            (r'K_R', 'KR'), (r'K_f', 'Kf'), (r'\Keps', 'Keps'), (r'\eta_1', 'eta1'), (r'\qc', 'qc'), (r'\gD', 'gD'),
            (r'\dL', 'dL'), (r'\delta_1', 'delta1'), (r'\nu', 'nu'), (r'A_0', 'A0'), (r'\fF', 'fF')]
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
      r'($U_0=U_{\max}$) and the stage-A tuple $\pA$ ($U_0=\UA$), at $\vz=6\cdot10^{-5}$ with the touch-down constants of '
      r'Theorem~\ref{thm:touchdown}. Derived values to six digits; the check uses $50$ digits.}\label{tab:core}')
    w(r'\end{table}')
    # ---------------- Table A.2 ----------------
    w(r'\begin{table}[!htbp]\centering\footnotesize\setlength{\tabcolsep}{3pt}')
    w(r'\begin{tabular}{@{}ll@{\hspace{10pt}}ll@{\hspace{10pt}}ll@{\hspace{10pt}}ll@{}}\toprule')
    cells = [('$%s$' % TD_NAMES[k], '$%s$' % tex_num(TD[k])) for k in TD_SHOW]
    L += pair_rows(cells, 4)
    w(r'\bottomrule\end{tabular}')
    w(r'\par\medskip')
    w(r'\begin{tabular}{@{}ll@{\hspace{10pt}}ll@{\hspace{10pt}}ll@{}}\toprule')
    cells = [('$%s$' % tex.split('=')[0], r'$%s\to%s$' % (tex_num(TD[k], 8), tex_input(ik)))
             for k, ik, tex, d in TD_USED]
    L += pair_rows(cells, 3)
    w(r'\bottomrule\end{tabular}')
    w(r'\caption{Constants of Definition~\ref{def:tdconst} at $\vbar=6\cdot10^{-5}$, $\eta=0.1$, $\epsbar=10^{-3}$, '
      r'$\xi_1=1.007$, $\lambda_0=0.0333$, $G_{\mathrm T}=0.05$ (six digits; the check uses $50$ digits). Top: the '
      r'ingredients of the constants of Theorem~\ref{thm:touchdown}; all %d constants of Definition~\ref{def:tdconst} are '
      r'listed in \texttt{verify\_constants.out}. Bottom: the constants used in Theorem~\ref{thm:touchdown} and afterwards, '
      r'exact value $\to$ value used; $c_{\mathrm{sep}},\kc,\czlo$ are rounded down, the others up.}\label{tab:td}'
      % len(TD_NAMES))
    w(r'\end{table}')
    # ---------------- Table A.3 ----------------
    w(r'\begin{table}[!htbp]\centering\footnotesize\setlength{\tabcolsep}{3pt}')
    w(r'\begin{tabular}{@{}ll@{\hspace{10pt}}ll@{\hspace{10pt}}ll@{\hspace{10pt}}ll@{}}\toprule')
    w(r'\multicolumn{8}{@{}l}{\emph{Free:} $\bar\omega=%s$, $c_k=%s$, $\delta_0=%s\,R$; and $\vz=6\cdot10^{-5}$, '
      r'$\epsS=4\cdot10^{-11}$, $a^\prime=0.99982$, $C_0=c_N$}\\\midrule' % (INPUTS['omb'], INPUTS['ck'], INPUTS['d0fac']))
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
