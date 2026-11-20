"""Q3: constants of the touch-down theorem (design T) as explicit functions of
      vbar  (upper bound for v),  eta (half-width of the local window I_eta around alpha0),
      epsbar (upper bound for eps), x1 (threshold: forward labels x >= x1 eps are true up to t_s), lam0, D1.
Every quantity is the formula of referee/Q3-claims.md with the same name (section numbers in comments).
In every formula v stands for vbar; each formula is monotone in v in the safe direction (see Q3-claims §0, rule (M)).
chain() returns (K, cond): the constants and the SIDE CONDITIONS (all must be True for the proof to apply).
D1 != 1 is supported for NUMERICAL exploration only (Q3-claims proves D1 = 1); c := 1 + D1.
mpmath, 50 digits; printed values are rounded outward (up for upper bounds, down for lower bounds).
Usage:  python constants.py                 -> main table
        python constants.py vbar eta [epsbar] [D1]  -> full listing"""
import sys, mpmath as mp
mp.mp.dps = 50
M = mp.mpf
sin, cos, tan, asin, acos, atan, sqrt, pi, exp, log = mp.sin, mp.cos, mp.tan, mp.asin, mp.acos, mp.atan, mp.sqrt, mp.pi, mp.exp, mp.log


def chain(vbar, eta='0.1', epsbar='1e-3', x1=None, lam0=None, D1='1', G=None):
    v = M(vbar); eta = M(eta); eb = M(epsbar); D1 = M(D1); c = 1 + D1
    K = {}; cond = {}
    # ---- §0 basic -------------------------------------------------------------------------------------------------
    mu = v / (1 - v); muT = 3 * v / (1 + v)
    t1 = 1 / (1 - v) + D1                                  # = 2 + mu for D1 = 1
    gb = sqrt(1 - v * v) * ((1 + v) / (1 - v)) ** (v / 2)  # g_max(vbar) (g_max is increasing in v)
    a_c = acos(1 / c)                                      # pi/3 for D1 = 1
    a_lo = acos(1 / c + v)                                 # lower bound for alpha0
    Da = a_c - a_lo
    d1 = v * t1 + mu
    e_rho = v * t1 + Da + mu
    rho_c0 = sqrt(c * c - 1)                               # sqrt(3)
    cond['rho0 > epsbar'] = rho_c0 - e_rho > eb
    T2 = t1 + (rho_c0 + e_rho) / (1 - v)
    d_s = v * T2
    d_P = max(mu, d_s + Da)
    # ---- §1 run 1 ---------------------------------------------------------------------------------------------------
    W1 = lambda rho: exp(v * t1 / rho)
    om1 = lambda rho: v * t1 / (2 * rho)
    ka1 = lambda rho: (2 / rho + 1 / rho ** 2) * v * t1 * exp(2 * v * t1 / rho)
    rho_m = sin(M(1) / 2)
    cond['cos(1/2) > vbar'] = cos(M(1) / 2) > v
    rho1_min = (1 + v) * D1                               # rho_1 >= |h_1|/(1-v) >= (1+v) D1
    k_arm = (1 + v) / (cos(M(1) / 2) - v) + v / (1 - v * v) + v / ((1 - v) * rho1_min)
    d_arm = (1 + v) / ((1 - v) * (cos(M(1) / 2) - v)) + v / ((1 - v) * rho1_min)
    h1max = 1 - cos(M(1) / 2) + D1
    e1 = h1max * (1 + tan(M(1) / 4) ** 2) + (1 + v) * tan(M(1) / 4) ** (1 - v)
    E1 = max(M(1), e1 / (1 - v))
    W_arm = E1 ** v / (1 - v)
    k_all = max(k_arm, 1 + ka1(rho_m))
    W_all = max(W_arm, W1(rho_m) * (pi / 2) ** (2 * v))
    # ---- §2 the window I_eta at t1 ----------------------------------------------------------------------------------
    thL = a_lo - eta; thR = a_c + eta
    cond['thL >= 1/2'] = thL >= M(1) / 2
    cond['thR <= pi/2'] = thR <= pi / 2
    cond['eta <= pi/3'] = eta <= pi / 3
    cond['s decreasing: cos thL < 2c/(1+c^2)'] = cos(thL) < 2 * c / (1 + c * c)
    R0 = lambda th: sqrt(1 + c * c - 2 * c * cos(th))     # |e^{i th} - c|
    sfun = lambda th: c * sin(th) / R0(th) ** 2
    cond['q decreasing: cot(a_lo - eta/2)/2 < s(thR)'] = (1 / tan(a_lo - eta / 2)) / 2 < sfun(thR)
    RL = R0(thL); RR = R0(thR)
    cond['d1 < RL'] = d1 < RL
    r_min = RL - d1; r_max = RR + d1
    rho_w = sin(thL)
    W_w = W1(rho_w); om_w = om1(rho_w); ka_w = ka1(rho_w)
    iota = 1 + v * t1 / sin(thL)
    q_min = sin(a_lo + eta / 2) / RR; q_max = sin(a_c - eta / 2) / RL
    rL_min = 2 * c * q_min / (1 + d1 / RL); rL_max = 2 * t1 * iota * q_max / (1 - d1 / RL)
    L_min = 2 * c * sin(a_lo - eta / 2) / r_max ** 2; L_max = 2 * t1 * iota * sin(a_c + eta / 2) / r_min ** 2
    m0 = max(abs(c * cos(thL) - 1), abs(c * cos(thR) - 1)) / RL
    om_p = asin(d1 / RL)
    ang = asin(m0) + om_w + om_p
    cond['ang < pi/2'] = ang < pi / 2
    A_min = cos(ang); A_max = W_w
    b_lo = L_min * (1 - eta ** 2 / 48) / 4; b_hi = L_max / 4
    bbar = b_hi * eta ** 2
    cond['bbar < pi/2'] = bbar < pi / 2
    e_tau = tan(bbar / 2) / (bbar / 2) - 1
    beta2 = b_hi * (1 + e_tau) / 2
    cond['beta2 < 1'] = beta2 < 1
    C_hi = 2 * r_max * beta2 ** (1 - v)
    C_lo = 2 * r_min * (b_lo / 2) / (1 + tan(bbar / 2) ** 2)
    cond['b_lo < 2'] = b_lo < 2
    aux = rL_max * bbar * eta / 2
    a_min = A_min * cos(bbar) - aux; a_max = A_max * (1 + v) + aux
    cond['a_min > 0'] = a_min > 0
    cond['cos bbar > vbar'] = cos(bbar) > v
    L_C = 2 * L_max / L_min + eta * A_max / r_min
    L_lo = 2 * (cos(bbar) - v) * (L_min / L_max) * (1 - eta ** 2 / 32)
    cond['tail monotone: L_lo > eta A_max/r_min'] = L_lo > eta * A_max / r_min
    S1 = rL_max / (2 * (1 - v * v) * r_min) * (r_max * a_max * L_C + (1 + v) * eta)
    # ---- §3 forward arc ----------------------------------------------------------------------------------------------
    h_f = A_min - r_max * b_hi ** 2 * eta ** 3 / 2
    cond['0 < h_f <= 1 - vbar^2'] = 0 < h_f <= 1 - v * v
    rho_c = h_f / (1 + v)
    if x1 is None:
        x1 = mp.ceil(M('1.0001') / rho_c * 1000) / 1000
    x1 = M(x1)
    cond['rho_c x1 > 1'] = rho_c * x1 > 1
    Q = (1 + v) * r_max / h_f
    cond['Q >= 1'] = Q >= 1
    y_f = 2 * r_max * beta2
    Y1 = (rL_max / 2 + A_max * b_hi * (1 + e_tau) * eta) / a_min
    Ybar = Y1 * eta ** (1 - mu) * Q ** mu
    den_f = 1 - v - v * Ybar
    cond['den_f > 0'] = den_f > 0
    th_f = max((1 + v) * Y1, v * y_f / rho_c) / den_f
    W_f = a_max * sqrt((1 + v + v * Ybar) ** 2 + ((1 + v) * Ybar + v) ** 2) / (1 - v * v)
    del1 = v / (3 * (1 - v) ** 2 * x1)
    tau_f = beta2 * Q ** (1 + mu)
    tauf_bar = tau_f * eta ** (1 - mu)
    cond['1 - 2 tauf_bar^2 > vbar'] = 1 - 2 * tauf_bar ** 2 > v
    rho_u = ((1 + v) * A_max + del1) / (1 - 2 * tauf_bar ** 2)
    S2 = (2 * tau_f + th_f * Q ** mu) / ((1 - v * v) * rho_c) * (rho_u * a_max * L_C + 1 + v)
    K_f = Q ** mu * (1 + ka_w + S1 * v) + S2 * v
    # ---- §4 virtual labels next to X0 ---------------------------------------------------------------------------------
    th_v = Q ** mu * exp(mu) * (th_f + mu * exp(2 * mu) * y_f * x1)
    W_v = W_f * exp(2 * mu)
    u1 = W_v * x1
    # ---- §5 tail and end ----------------------------------------------------------------------------------------------
    cond['C_hi < 1'] = C_hi < 1
    cond['C_lo eta^2 > epsbar gb'] = C_lo * eta ** 2 > eb * gb
    cond['gb > C_lo'] = gb > C_lo
    xe_lo = C_hi ** (-M(1) / 2)
    xe_hi = (gb / C_lo) ** (1 / (2 - 2 * v))
    xe_bar = xe_hi * sqrt(eb)
    cond['xe_bar < eta'] = xe_bar < eta
    del2 = (1 + v) * v / (3 * (1 - v) * xe_lo)
    h_t = A_min - del2
    cond['h_t > 0'] = h_t > 0
    h_T = (1 + v) * A_max + r_max * b_hi ** 2 * eta ** 3 / 2
    m_tau = (2 * h_t / C_hi) * eta ** (-(1 - 2 * v))
    cond['m_tau > 1'] = m_tau > 1
    tau_t = m_tau ** (1 / (1 + v))
    e_t = (1 + v) / (m_tau * tau_t ** (1 - v))
    y_c = 2 * (1 + e_t) * h_T / (1 - v)
    y_T = C_hi ** (1 / (1 + v)) * max(M(1), y_c) ** v
    T_t = (max(M(1), y_c / C_lo) * 2 / b_lo) ** v
    Y2 = T_t * rL_max / (2 * a_min)
    Y2bar = Y2 * eta ** (1 - muT)
    th_t = Y2 + v * y_T / h_t
    z_T = (h_T + v * y_T * eta ** (1 - muT)) / (1 - v)
    rho_T = z_T * sqrt(1 + (y_T * eta ** (1 - muT) / h_t) ** 2)
    W_t = a_max * sqrt((1 + v + v * Y2bar) ** 2 + ((1 + v) * Y2bar + v) ** 2) / (1 - v * v)
    S3 = (y_T / h_t + th_t) / ((1 - v * v) * h_t) * (rho_T * a_max * L_C + 1 + v)
    K_t = T_t * (1 + ka_w + S1 * v) + S3 * v
    # seen in run 2
    x2 = 1 / (3 * (1 - v) * A_min)
    cond['x2 vbar <= 1/2'] = x2 * v <= M(1) / 2
    cond['xe_lo >= 1/2'] = xe_lo >= M(1) / 2
    h_a = 1 - A_max / 2 - r_max * b_hi ** 2 * eb ** 3 / 32
    cond['h_a > 0'] = h_a > 0
    Q_a = (1 + v) * r_max / h_a
    tau_a = beta2 * Q_a ** (1 + mu) * eb ** (1 - mu) / 4
    cond['1 - 2 tau_a^2 > 0'] = 1 - 2 * tau_a ** 2 > 0
    cond['A_min > 4 tau_a^2'] = A_min > 4 * tau_a ** 2
    # ---- §6 bulk and hole -----------------------------------------------------------------------------------------------
    e_beta = asin(e_rho / rho_c0)
    bl = b_lo * eta ** 2
    psi_c = asin(1 / c)                                    # pi/6 for D1 = 1: pi - beta* (unperturbed)
    cond['bl <= psi_c - e_beta'] = bl <= psi_c - e_beta
    cond['2 psi_c + 2 e_beta <= pi - bl'] = 2 * psi_c + 2 * e_beta <= pi - bl
    y_b = min(M(1), D1) * sin(bl)
    H_b = 1 + c + d1 + (1 + v) * (rho_c0 + e_rho) / (1 - v)
    T_b = 2 * H_b / (y_b * tan(bl / 2))
    S_b = (3 + v) / (2 * (1 - v) * y_b)
    K_b = T_b ** v * (k_all + S_b * v) + S_b * v
    W_b = (1 + v) / (1 - v) * T_b ** v
    cond['T_b >= 1'] = T_b >= 1
    cond['vbar <= 1/10'] = v <= M(1) / 10
    r_B = M('0.005') + v * t1                              # radius of the ball around 1 containing Gamma_1
    rho_h = (1 - 1 / c) - d_P - r_B - v * T2
    cond['rho_h > 0'] = rho_h > 0
    cond['alpha_s <= 2 gb epsbar < thL, gb epsbar <= 1'] = 2 * gb * eb < thL and gb * eb <= 1
    # ---- §7 assembly ------------------------------------------------------------------------------------------------------
    W_x = max(W_v, W_t, W_b * W_all)
    U_max = (W_v + W_t) * eta + W_b * W_all * (2 * pi - 2 * eta) / (1 - 2 * v)
    cond['U >= 1: 2 - 2 d_s >= 1'] = 2 - 2 * d_s >= 1
    if lam0 is None:
        lam0 = min(eta / 3 if xe_bar >= eta / 3 else (eta - xe_bar) / 2, M(1) / 4)
        lam0 = mp.floor(lam0 * 10000) / 10000
    lam0 = M(lam0)
    cond['2 lam0 + min(xe_bar, lam0) <= eta'] = 2 * lam0 + min(xe_bar, lam0) <= eta
    cond['2 u1 epsbar <= eta'] = 2 * u1 * eb <= eta
    cond['lam0 <= 1/4'] = lam0 <= M(1) / 4
    Lhat = (8 / lam0) ** (2 * v) / (1 - 2 * v)
    cond['W_x Lhat <= 2'] = W_x * Lhat <= 2
    Delta0 = lam0 / (W_x * Lhat)
    cond['Delta0 <= eta'] = Delta0 <= eta
    c_sep = 2 * sin(Delta0 / 2)
    cond['c_sep > 2 epsbar'] = c_sep > 2 * eb
    kap2 = min(cos(th_v * Delta0 ** (1 - mu)), h_t / W_t)
    cond['th_v Delta0^(1-mu) <= pi/2'] = th_v * Delta0 ** (1 - mu) <= pi / 2
    cond['kappa2 >= 1/2'] = kap2 >= M(1) / 2
    K_star = max(K_f * W_v ** mu, K_t * W_t ** muT, K_b)
    cond['K_star lam0^(1-muT) <= pi'] = K_star * lam0 ** (1 - muT) <= pi
    c_far = K_star / sqrt(12)
    c_near = th_v * sqrt((12 * u1 ** 2 + 6 * u1 + 1) / (3 - 2 * mu))
    cond['u1 >= 1/2'] = u1 >= M(1) / 2
    c_tail = th_t * sqrt(19 / (3 - 2 * muT))
    c_N = max(c_far, c_near, c_tail)
    cond['c_N lam0^(1-muT) <= 1'] = c_N * lam0 ** (1 - muT) <= 1
    if G is None:
        G = min(eta / 2, eta - xe_bar)
        G = mp.floor(G * 10000) / 10000
    G = M(G)
    cond['0 < G, xe_bar + G <= eta'] = G > 0 and xe_bar + G <= eta
    th3 = th_v * G ** (M(3) / 4 - mu)
    th4 = th_t * (xe_bar + G) ** (M(1) / 2 - muT) * (2 ** (M(1) / 4) * sqrt(xe_hi) + G ** (M(1) / 4))
    c_y = y_T / h_t ** 2
    th5 = c_y * max(M(1), z_T * xe_hi) * 2 ** (M(1) / 4)
    theta_T = max(th3, th4, th5)
    C_z = z_T * xe_hi * eb ** (M(1) / 4)
    c_T4 = th_t / h_t
    loc = dict(locals())
    for k_ in list(loc):
        if k_ in ('K', 'cond', 'k_', 'W1', 'om1', 'ka1', 'R0', 'sfun'):
            continue
        val = loc[k_]
        if isinstance(val, (mp.mpf, int)):
            K[k_] = val
    K['C0'] = lambda ap: c_N * lam0 ** (1 - muT - M(ap))
    return K, cond


def up(x, d=4):
    x = M(x)
    if x == 0: return '0'
    s = mp.mpf(10) ** (mp.floor(mp.log10(abs(x))) - d + 1)
    return mp.nstr(mp.ceil(x / s * (1 + M(10) ** -15)) * s, d + 2)


def dn(x, d=4):
    x = M(x)
    if x == 0: return '0'
    s = mp.mpf(10) ** (mp.floor(mp.log10(abs(x))) - d + 1)
    return mp.nstr(mp.floor(x / s * (1 - M(10) ** -15)) * s, d + 2)


ROWS = [('T2', 'T2', up), ('U_max', 'U_max', up), ('lam0', 'lam0', lambda x: mp.nstr(x, 6)), ('c_sep', 'c_sep', dn), ('kappa2', 'kap2', dn),
        ('c_N', 'c_N', up), ('c_near', 'c_near', up), ('c_far', 'c_far', up), ('c_tail', 'c_tail', up),
        ('th_v', 'th_v', up), ('th_t', 'th_t', up), ('T4coef', 'c_T4', up), ('c_y', 'c_y', up),
        ('theta_T', 'theta_T', up), ('G_T', 'G', lambda x: mp.nstr(x, 6)), ('C_z', 'C_z', up), ('zcoef', None, up),
        ('K_f', 'K_f', up), ('K_t', 'K_t', up), ('K_b', 'K_b', up), ('W_x', 'W_x', up), ('x1', 'x1', lambda x: mp.nstr(x, 6)), ('u1', 'u1', up),
        ('xe_lo', 'xe_lo', dn), ('xe_hi', 'xe_hi', up), ('A_min', 'A_min', dn), ('h_t', 'h_t', dn), ('z_T', 'z_T', up)]


def table(cases):
    res = [chain(*c) for c in cases]
    out = ['%-9s' % 'vbar' + ''.join('%11s' % c[0] for c in cases),
           '%-9s' % 'eta' + ''.join('%11s' % c[1] for c in cases),
           '%-9s' % 'epsbar' + ''.join('%11s' % (c[2] if len(c) > 2 else '1e-3') for c in cases)]
    for nm, key, f in ROWS:
        if key is None:
            out.append('%-9s' % nm + ''.join('%11s' % f(K['z_T'] * K['xe_hi']) for K, _ in res))
        else:
            out.append('%-9s' % nm + ''.join('%11s' % f(K[key]) for K, _ in res))
    out.append('%-9s' % "a'max" + ''.join('%11s' % dn(1 - K['muT'], 7) for K, _ in res))
    for ap in ('0.5', '0.9', None):
        out.append('%-9s' % ('C0(%s)' % (ap or 'max')) + ''.join('%11s' % up(K['C0'](ap if ap else 1 - K['muT'])) for K, _ in res))
    for (K, cond), c in zip(res, cases):
        bad = [k_ for k_, ok in cond.items() if not ok]
        out.append(str(c) + ' side conditions: ' + ('ALL OK (%d)' % len(cond) if not bad else 'FAILED: ' + '; '.join(bad)))
    return '\n'.join(out)


CASES = [('1e-6', '0.1'), ('1e-5', '0.1'), ('1e-4', '0.1'), ('1e-3', '0.1'), ('1e-2', '0.1'),
         ('1e-6', '0.2'), ('1e-5', '0.2'), ('1e-4', '0.2'), ('1e-3', '0.2'), ('1e-2', '0.2'), ('2e-2', '0.2'), ('1e-6', '0.3'), ('1e-3', '0.3')]

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        args = sys.argv[1:]
        K, cond = chain(args[0], args[1], args[2] if len(args) > 2 else '1e-3', D1=args[3] if len(args) > 3 else '1')
        for k_, val in K.items():
            if callable(val): continue
            print(f"  {k_:12s} = {mp.nstr(val, 12)}")
        bad = [c_ for c_, ok in cond.items() if not ok]
        print('  side conditions:', 'ALL OK (%d)' % len(cond) if not bad else 'FAILED: ' + '; '.join(bad))
    else:
        t = table(CASES) + '\n\n' + table([('1e-6', '0.2', '1e-6'), ('1e-4', '0.2', '1e-6'), ('1e-3', '0.2', '1e-6'),
                                           ('1e-2', '0.2', '1e-6'), ('1e-3', '0.3', '1e-6')])
        print(t)
        import os
        os.makedirs('out', exist_ok=True)
        open('out/table.txt', 'w').write(t + '\n')
