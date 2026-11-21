"""Lemma B-virtual: tangent of the virtual front at t_td for labels alpha0+xi, 0<xi<xi1*eps.
Exact true data at t_a (mpmath), then the regularised flow on [t_a,t_td] in scaled variables R=r/eps, s=(t-t_a)/eps
(heading frame, P fixed at 0 moving with velocity 1):  R' = v F1(R) - (1,0),  Q' = v DF1(R) Q,  F1 = F at eps=1.
"""
import sys
sys.path.insert(0, '.')
from chkB import Design
from mpmath import mp, mpf, arg, quad
import numpy as np

def F1(R):
    rho = np.hypot(*R)
    s = (2 - rho) if rho <= 1 else 1/rho
    return s*R

def DF1(R):
    rho = np.hypot(*R)
    if rho <= 1:
        return (2 - rho)*np.eye(2) - (np.outer(R, R)/rho if rho > 0 else 0)
    rh = R/rho
    return (np.eye(2) - np.outer(rh, rh))/rho

def rhs(Y, v):
    R = Y[:2]; Q = Y[2:]
    return np.concatenate([v*F1(R) - np.array([1.0, 0.0]), v*DF1(R) @ Q])

def integrate(R0, Q0, v, S, n=40000):
    Y = np.concatenate([R0, Q0]); h = S/n
    for _ in range(n):
        k1 = rhs(Y, v); k2 = rhs(Y + h/2*k1, v); k3 = rhs(Y + h/2*k2, v); k4 = rhs(Y + h*k3, v)
        Y = Y + h/6*(k1 + 2*k2 + 2*k3 + k4)
    return Y

for vs in ['0.01', '0.04']:
    for es in ['1e-12', '1e-30']:
        D = Design(vs, es); v = float(D.v); mu = float(D.mu)
        S = float((D.ttd - D.ta)/D.eps)
        print(f"v={vs} eps={es}  S=(ttd-ta)/eps={S:.6f}")
        for fac in ['0.001', '0.01', '0.1', '0.5', '1', '2', '4']:
            xi = D.eps*mpf(fac)
            th = D.alpha0 + xi
            r = D.run2(th, D.ta)[0]
            h = xi*mpf(10)**-25
            q = (D.run2(th+h, D.ta)[0] - D.run2(th-h, D.ta)[0])/(2*h)
            R0 = np.array([float(r.real/D.eps), float(r.imag/D.eps)])
            Q0 = np.array([float(q.real), float(q.imag)])
            Y = integrate(R0, Q0, v, S)
            psi_a = float(arg(q)); psi_td = np.arctan2(Y[3], Y[2])
            xif = float(xi)
            print(f"  xi={fac}*eps  psi(t_a)={psi_a:.4e}  psi(t_td)={psi_td:.4e}  |psi_td|/xi^(1-mu)={abs(psi_td)/xif**(1-mu):.4f}"
                  f"  w_td={np.hypot(Y[2],Y[3]):.4f}  |R(t_td)|={np.hypot(Y[0],Y[1]):.3e}")
