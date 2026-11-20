"""
q1const.py -- the derived constants and side conditions of Theorem End* / Corollary End*
(referee/Q1-claims.md, final version).  One formula per line, in the order of Q1-claims.md §1-§3.

Backend-generic: pass  L = FloatLib()  (fast search) or  L = MpLib(dps)  (verification, mpmath).
All side conditions are returned as  (name, lhs, rhs, kind)  with kind in {'<=', '<'}; a condition holds iff lhs kind rhs.

Parameters (dict p):
  gam, R, m, s0, f, k1, cA, KR, Kf, Ke, eta, q, nu, d, dl1, A0      (Theorem End*, §1 of Q1-claims)
  U (=U_max), v
Corollary data (dict D): ap (a'), C0, lam0, csep
"""
import math
import mpmath


class FloatLib:
    def __init__(self):
        self.log, self.exp, self.sqrt = math.log, math.exp, math.sqrt
        self.one = 1.0

    def num(self, x):
        return float(x)


class MpLib:
    def __init__(self, dps=50):
        mpmath.mp.dps = dps
        self.log, self.exp, self.sqrt = mpmath.log, mpmath.exp, mpmath.sqrt
        self.one = mpmath.mpf(1)

    def num(self, x):
        return mpmath.mpf(x) if not isinstance(x, str) else mpmath.mpf(x)


def derived(p, L):
    """All derived constants of §1 of Q1-claims.md.  p must contain numbers of the backend."""
    o = L.one
    gam, R, m, k1, cA, KR, Kf, Ke, eta, q, d, dl1 = (p[k] for k in
        ('gam', 'R', 'm', 'k1', 'cA', 'KR', 'Kf', 'Ke', 'eta', 'q', 'd', 'dl1'))
    c = {}
    c['M'] = m * R ** (-gam)
    c['chi'] = k1 * d                                              # (E-1c*) constant
    c['c6'] = (1 + dl1) / cA                                        # (E-star*)
    ct = lambda r: (L.sqrt(k1) * r ** (o / 2 + gam) + m / 2) / cA  # one-step tilt constant
    c['ct'] = ct
    c['Sq'] = 1 / (1 - q ** (-gam))
    c['CA'] = c['Sq'] * ct(q)                                       # same left end
    c['CB'] = c['CA'] + ct(3 * o)                                   # same right end
    c['CTL'] = c['CA'] + c['CB']                                    # general
    c['CmuA'] = 1 + k1 * c['CA'] ** 2
    c['C1A'] = L.sqrt(k1 * c['CmuA'])
    c['crho'] = cA - (2 * dl1 + k1) / Kf
    c['cR'] = cA * KR - dl1 / Ke - k1
    c['K1'] = c['crho'] * Kf / k1
    c['K2'] = c['cR'] / k1
    c['a1'] = 1 + 1 / c['K1'] + 2 / c['K1'] ** 2
    c['a2'] = 1 + 1 / c['K2'] + 2 / c['K2'] ** 2
    c['camp'] = c['a1'] * c['chi'] / c['crho']                      # amplification exponent / v
    c['B2U'] = 2 * k1 ** (o * 3 / 2) * (1 + 1 / c['K2']) / c['cR'] ** 2
    c['B2e'] = 2 * k1 ** (o * 3 / 2) * (1 + 1 / c['K1']) / c['crho'] ** 2 * (c['chi'] / eta + d / (Ke * eta ** 2))
    c['rf'] = 1 + 1 / (Kf - 2)
    c['Cp'] = k1 * (ct(c['rf']) + c['CB'] * (1 + 1 / Kf) ** gam)
    c['B3'] = 2 * k1 ** (o * 3 / 2) * c['Cp'] / c['crho'] ** 3
    Kmin = Kf if Kf <= KR else KR
    c['Psi'] = 2 + L.log(Kmin) + (Kf - KR if Kf > KR else 0 * o) / KR
    c['tauI'] = d * (k1 * c['c6'] + 2) + c['c6'] * c['chi'] * c['Psi']
    c['tau_al'] = d / c['c6'] + c['chi'] * (2 + L.log(Kf))
    c['tau_be'] = 2 ** gam * (2 * d + c['chi'] * (o * 3 / 4 + (Kf ** gam - 1) / (2 * gam)))
    c['tau_n'] = c['chi'] * Kf + 2 * d
    c['k0'] = max(c['C1A'], k1 * 2 ** gam * c['CA'])
    c['iota'] = o if Kf + 1 > KR else 0 * o
    c['D_I'] = c['CmuA'] * c['tauI']
    c['D_IIs_al'] = c['c6'] ** 2 * c['C1A'] ** 2 * c['tau_al']
    c['D_IIs_be'] = 2 * c['c6'] ** 2 * k1 * c['CTL'] * c['C1A'] * c['tau_be']
    c['D_IIs_0'] = 4 * d * c['c6'] * c['C1A'] * c['k0']
    c['D_IIs'] = c['D_IIs_al'] + c['D_IIs_be'] + c['D_IIs_0']
    c['D_IIl'] = c['c6'] * (Kf + 1) ** gam / m * (c['C1A'] * c['tau_al'] + c['iota'] * L.sqrt(k1) * c['tau_n'] / KR)
    c['B5'] = (2 / c['crho']) * ((c['Cp'] + L.sqrt(k1) * Kf ** (-1 - gam)) ** 2 / c['crho'] ** 2 + Kf ** (-2 * gam))
    c['I5'] = c['chi'] * (eta + 1 / Ke) ** (2 * gam) / (2 * gam) + d * max(o, (2 / Kf) ** (1 - 2 * gam)) * Ke ** (-2 * gam)
    c['r1'] = R * (cA / k1 - dl1 / Ke)
    return c


def theorem_conditions(p, c, L, with_Pc=True):
    """Side conditions (P0)-(P7), (Pc) of Theorem End*.  Returns list of (name, lhs, rhs, kind)."""
    o = L.one
    v, U = p['v'], p['U']
    gam, R, m, s0, f, k1, cA, KR, Kf, Ke, eta, q, nu, d, dl1, A0 = (p[k] for k in
        ('gam', 'R', 'm', 's0', 'f', 'k1', 'cA', 'KR', 'Kf', 'Ke', 'eta', 'q', 'nu', 'd', 'dl1', 'A0'))
    chi, crho, cR = c['chi'], c['crho'], c['cR']
    out = []
    # (P0) ranges
    out += [('P0 gam>0', 0 * o, gam, '<'), ('P0 gam+nu<1', gam + nu, o, '<'), ('P0 R<=1', R, o, '<='),
            ('P0 R>0', 0 * o, R, '<'), ('P0 m>0', 0 * o, m, '<'), ('P0 s0>0', 0 * o, s0, '<'),
            ('P0 s0<=f', s0, f, '<='), ('P0 f<1', f, o, '<'), ('P0 k1>1', o, k1, '<'), ('P0 k1<=4/3', k1, 4 * o / 3, '<='),
            ('P0 cA>0', 0 * o, cA, '<'), ('P0 cA<=1', cA, o, '<='), ('P0 KR>=1', o, KR, '<='), ('P0 Kf>=3', 3 * o, Kf, '<='),
            ('P0 Ke>=3/2', 3 * o / 2, Ke, '<='), ('P0 eta>0', 0 * o, eta, '<'), ('P0 eta<=Kf/(Kf+1)', eta, Kf / (Kf + 1), '<='),
            ('P0 q>1', o, q, '<'), ('P0 nu>=0', 0 * o, nu, '<='), ('P0 A0>=1', o, A0, '<='), ('P0 v>0', 0 * o, v, '<'),
            ('P0 v<1', v, o, '<')]
    # (P1)
    out += [('P1 1/(1-v)<=d', 1 / (1 - v), d, '<='), ('P1 e^{2v/(1-v)}<=dl1', L.exp(2 * v / (1 - v)), dl1, '<=')]
    # (P2)
    out += [('P2 crho*Kf>=2', 2 * o, crho * Kf, '<='), ('P2 cR*Ke>=1', o, cR * Ke, '<='), ('P2 c6<=KR*Ke', c['c6'], KR * Ke, '<=')]
    # (P3)
    out += [('P3 camp*v<=nu', c['camp'] * v, nu, '<=')]
    # (P4)
    out += [('P4 log A0', v * (2 * c['a1'] * d / (crho * Kf) + c['a2'] * chi * U / (cR * R)), L.log(A0), '<=')]
    # (P5) far pairs
    mx = (KR / Kf) ** nu if KR > Kf else o
    T1 = s0
    T2 = mx * (v / m) * (c['B2U'] * chi * U / R + c['B2e'])
    T3 = c['B3'] * Kf ** (gam - 1) * (2 * d / Kf + chi / (1 - gam - nu)) * v
    out += [('P5 far', A0 * (T1 + T2 + T3), f, '<=')]
    # (P6) near pairs
    out += [('P6 near', f ** 2 + 2 * v * (c['D_I'] + max(c['D_IIs'], c['D_IIl'])), o, '<')]
    # (P7) length
    Xfar = v * (chi * U / (cR * R) + (d / (Ke * eta) + chi * L.log(KR / eta)) / crho)
    dtail = p.get('dtail', 0 * o)     # (P7_delta) of Lemma Q1.L3/L4; delta = 0 is (P7)
    out += [('P7 length', (1 + dtail) * L.exp(Xfar + c['B5'] * c['I5'] * v * m ** 2) + v * k1 * c['tauI'], k1, '<')]
    if with_Pc:
        out += [('Pc m^2<=1/2', m ** 2, o / 2, '<='), ('Pc r1>0', 0 * o, c['r1'], '<')]
    return out, dict(T1=T1, T2=T2, T3=T3, Xfar=Xfar)


def corollary_conditions(p, c, D, L):
    """(C1)-(C6) of Corollary End*."""
    o = L.one
    ap, C0, lam0, csep = D['ap'], D['C0'], D['lam0'], D['csep']
    R, KR, Kf, cA, gam, nu, s0, m = (p[k] for k in ('R', 'KR', 'Kf', 'cA', 'gam', 'nu', 's0', 'm'))
    KRR = KR * R
    mn = KRR if KRR < lam0 else lam0
    out = [('C0 C0*lam0^a<=1', C0 * lam0 ** ap, o, '<='),
           ('C1 R<=lam0', R, lam0, '<='),
           ('C2', cA, 1 - (C0 * mn ** ap) ** 2 / 2, '<=')]
    if KRR < lam0:
        out.append(('C3', cA * KRR, lam0 * (1 - (C0 * lam0 ** ap) ** 2 / 2), '<='))
    out += [('C4 csep>=cA*KR*R', cA * KRR, csep, '<='),
            ('C5 gam+nu<=a', gam + nu, ap, '<='),
            ('C6', C0 * R ** ap, s0 * m * (Kf / KR if Kf < KR else o) ** nu, '<=')]
    return out


def check(conds):
    """Return list of (name, lhs, rhs, kind, ok, slack) ; slack = rhs - lhs (for '<=','<')."""
    res = []
    for name, lhs, rhs, kind in conds:
        ok = (lhs <= rhs) if kind == '<=' else (lhs < rhs)
        res.append((name, lhs, rhs, kind, ok, rhs - lhs))
    return res
