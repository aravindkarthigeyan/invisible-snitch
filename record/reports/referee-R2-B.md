# Second referee report R2-B: the conditional exact-capture chain (Section "The angle hypothesis")

Scope: `paper/main.tex`, Section `sec:angle` (Lemmas A1--A4, Prop A9, Lemma B1, Theorem B2, Lemma A2.1 = `lem:A21`,
Theorem A2.3 = `thm:A23`, Lemma A3.4 = `lem:A34`, Theorem A3.5 = `thm:A35`), with the dependencies in Sections 2--5
(Prop `prop:integrals`, Lemma `lem:k`, Props `prop:ray`, `prop:V`, `prop:order`, `prop:length`, Lemmas `lem:phi`, `lem:start`,
`lem:limit`, Theorem `thm:B`). Setting: epsilon = 0, |H'| <= 1, path fixed in advance, v < 1.
Verdicts were written before reading any existing referee report.

Code: `code/referee/R2B/mvals.py` (v1, lambda*, time bounds, gamma_H, the 0.2928 threshold),
`code/referee/R2B/propA9.py` (independent 60-digit recomputation of Prop A9 with the exact straight-run maps).

## Summary of verdicts

| Claim | Verdict |
|---|---|
| Lemma A1 (first instant) | OK |
| Lemma A2 (half-plane persistence) | OK |
| Lemma A3 (ordered phase) | OK |
| Lemma A4 (how order is lost) | OK |
| Prop A9 ((H) fails for a finite set) | OK (reproduced to all printed digits; my check is not interval-certified) |
| Lemma B1 (Psi = Phi - lambda rho_N) | OK |
| Theorem B2 (capture for v < v1 under (K)) | OK with a cosmetic fix |
| Numerical constants v1, lambda*, 0.5348, 16.9d / 37.6d | OK |
| Lemma A2.1 (cone facts) | OK |
| Theorem A2.3 (end-phase reduction) | OK with a cosmetic fix |
| Lemma A3.4 (hull perimeter) | OK |
| Theorem A3.5 (sector condition) | OK |
| Remarks (0.2928 threshold, gamma_H, 2 sqrt(pi v)) | OK |
| Passage discrete chases -> one path (Lemma 4) | OK |
| Conditional results labelled as conditional | OK |

No GAP and no FALSE claim found.

## Detailed checks

### Dependencies (Sections 2--5)
* `lem:phi`: d|S_j-H|/dt = -(1-v); d|S_{i+1}-S_i|/dt = v(rhat_{i+1}-rhat_i).e = v(cos b_i + cos c_i); b+c = pi-a gives
  2 sin(a/2) cos((b-c)/2) <= 2 sin(a/2) <= a. Degenerate (collinear) triangles contribute 0 or the right value. Accidental deletion
  of an interior point replaces two edges by one (triangle inequality: downward jump). Correct.
* `lem:start`: the open polyline H(t0)=S_0, S_1, ..., S_N is the closed inscribed polygon minus one edge; vertices are in curve
  order, so perimeter <= L(t) <= 2 pi d + 2 pi v t0 = 2 pi d/(1-v). Correct.
* `lem:limit`: Arzela--Ascoli, the Lipschitz constant 8v/c of (S,H) -> v(S-H)/|S-H| on {|S-H| >= c/4} (from
  |x/|x|-y/|y|| <= 2|x-y|/|x|), Gronwall bound (e(0) + (8v/c) T ||H_N-H||) e^{8vT/c}, the open-closed continuation argument,
  and the final openness of the uncaught set are all correct. The discrete chase H_N, extended by staying put after T_end, is
  1-Lipschitz on [0,T] and catches every direction of D_N (as target or accidentally), so the lemma applies exactly as used.

### Lemma A1
At t0, c = v - (1-v^2) t0/d = -1, so h = -d(1-cos alpha) < 0 and the bracket of `prop:order` is (1+v)(1-cos alpha) > 0 on (0,pi):
bearings k^{-1}(h/C) are strictly increasing in (theta*, pi). Reflection handles (pi, 2pi); alpha = pi stays on the backward ray.
Length of (theta*, 2pi-theta*) is 2pi - 2 arccos(-v) = 2 arccos v < pi. Hence beta_i = theta_i - theta_1 in [0, pi): ordered,
unsigned angles telescope, A(t0) = theta_N - theta_1. No candidate other than alpha = 0 is at H(t0) (`prop:ray`). OK.

### Lemma A2
Rays invariant (relative velocity parallel to r); on (0,pi), C > 0 constant, h strictly decreasing, k a decreasing bijection
(0,pi) -> R, so beta increases and never reaches 0 or pi; no capture by `prop:ray`. OK.

### Lemma A3
(a) bearings in [0,pi], unsigned consecutive angles are differences, A = beta_N <= pi, W <= A. (b) new bearings beta_i - beta_{j+1}
in [0, pi - beta_{j+1}], non-decreasing. At the end of leg j no other candidate is at H (distinct candidates never coincide),
so bearings extend continuously to the switch. Deleting bearing-0 points keeps order. (c) Within a leg, bearings in [0,pi]
stay in [0,pi] (A2), so no wrap-around at +-pi; order is closed; switches preserve order by (b). OK.

### Lemma A4
k(beta_P) - k(beta_Q) = h_P/C_P - h_Q/C_Q with h linear of slope -(1-v^2): affine. Identically zero would force equal bearing and
equal C, hence equal rho, i.e. coincident candidates: impossible. A + to - change needs C_P < C_Q, and at the tie C = rho g(b)
gives rho_P < rho_Q. The infimum argument: the failure set is relatively open within a leg (order closed, bearings continuous),
so s* is ordered and the reversing pair (pigeonhole over finitely many pairs, no deletions in a short interval after s*) is tied
at s*; ties on the rays never separate, so the tie is in (0,pi). Pair (j, j+1) cannot reverse since beta_{j+1} >= 0 = beta_j.
OK.

### Prop A9
Independent recomputation (`propA9.py`, 60 digits, exact maps of `prop:integrals`, bisection for k^{-1}):
A = 3.29145272139670365444..., A - pi = 0.14986... The bearings of S_1..S_6 relative to u_1 at that instant are
0, 0.9401, 0.8597, 3.1143, 3.1220, 3.1305 (mod 2pi): S_2 has overtaken S_3, as the mechanism remark says. All non-target bearings
are far from 0, so no accidental catch. Agreement with the printed enclosure to all 15 printed digits.
This contradicts (H) only for a non-dyadic set, and (H) is now stated for one family; the paper says so. OK.

### Lemma B1
Psi' = Phi' - lambda rho_N' = -(1-v) + vW - lambda(v - cos beta_N) = -(1-lambda)(1-v) + vW - lambda(1 - cos beta_N): algebra checked.
0 <= rho_N <= Phi gives the sandwich. Jumps: normal switch (target j < N(t)) leaves Phi and rho_N continuous; accidental catch
of an interior point lowers Phi; accidental catch of S_N lowers Phi by rho_{N-1} and raises rho_N from 0 to rho_{N-1}, so
Delta Psi = -(1+lambda) rho_{N-1} < 0. Final catch: Psi -> 0. OK.

### Theorem B2
Case W <= |beta_N| = x in [0,pi]: Psi' <= -f(x) <= -m. Case W <= w0: Psi' <= -(1-lambda)(1-v) + v w0 (dropping
-lambda(1-cos beta_N) <= 0). Hence Psi' <= -c(lambda); Psi >= (1-lambda)Phi > 0 while any candidate remains;
T_end <= t0 + Psi(t0)/c <= d/(1-v) + 2 pi d/((1-v) c). Lemma 4 concludes. Correct, and the conclusion for a given lambda with
c(lambda) > 0 holds for every v (v < v1 is only needed for c(lambda*) > 0).

Constants (recomputed, `mvals.py`). For lambda > v, f(x) = (1-lambda)(1-v) + lambda(1-cos x) - vx has local min at
x1 = arcsin(v/lambda), local max at pi - x1, and f'(0) = -v < 0, so m = min(f(x1), f(pi)) (= f(pi) if lambda <= v); validated
against a 4001-point grid on 200 random (v, lambda). f(pi) increases in lambda and f(x1) decreases near the optimum, so
max_lambda m is attained where f(x1) = f(pi); solving {f(x1) = f(pi) = 0} at 50 digits:

* v1 = 0.47475263829074210294519137953364301340...
* lambda* = 0.65518244479100280522464616276685729628...

Both agree with the paper's digits. max_lambda m(v1 -+ 1e-20, .) = +-1.45e-20 (sign change confirmed). Uniqueness of the root:
dm/dv <= -(1-lambda) < 0 for every lambda < 1, and the maximiser stays away from lambda = 1 (m <= (1-lambda)(1-v)), so
max_lambda m is strictly decreasing in v. Threshold (1-lambda*)(1-v) = 0.3 v at v = 0.534752...: paper's 0.5348 OK.
T at v = 0.2: 37.6356 d with lambda*, 16.8680 d with optimal lambda (~0.276): paper's 37.6d and 16.9d OK.

Cosmetic fix (W undefined at catch instants): in (K) replace
"at every time $t\ge t_0$ of the discrete chase," by
"at every time $t\ge t_0$ of the discrete chase other than a catch time,".

### Lemma A2.1
(a) angular distance on the circle is subadditive along the polyline. (b) from A2. (c) for the maximiser i at time s,
rho_i' = v - cos beta_i <= v - cos gamma on (s1, s); i is present on [s1, s]; deletions only remove a point at distance 0.
(d) triangle inequality. OK.

### Theorem A2.3
Ordered phase: W <= beta_N (A3(a)), so Psi' <= -m and Psi(t_f) <= Psi(t0) - m(t_f - t0). End phase: (i) 0 < D(t) <=
D(t_f) - (cos gamma - v)(t - t_f) by A2.1(c) chained across legs (D does not jump up at switches), (ii) Phi' <= -(1-v-vK).
Then T_end - t_f <= Phi(t_f)/c_E <= Psi(t_f)/((1-lambda)c_E) and the combination with mu = min{m, (1-lambda)c_E}
gives T_end - t0 <= Psi(t0)/mu. If order is never lost, t_f = T_end and Psi(T_end) = 0, consistent. M_1, M_2 > 0 because
v < v1 gives some lambda < 1 with m > 0; the sup is attained (continuous in lambda, -> <= 0 as lambda -> 1) and in any case
T_end <= inf over lambda of the bounds. Hypotheses are used exactly as stated, only on [t_f, T_end). OK.
Sample: with K = 0.45 at v = 0.2 the bound of (ii) is 16.868 d (m binds), so "essentially that of Theorem B2" is exact here.

Cosmetic fix (bearings are double-valued at switch instants): in (E_gamma) replace
"at every $t\in[t_f,T_{\rm end})$ every remaining candidate" by
"at every $t\in[t_f,T_{\rm end})$ off the catch times, every remaining candidate".

### Lemma A3.4
Cauchy: P = int_0^{2pi} h(theta,t) dtheta = int_0^pi width. For a.e. theta a unique vertex maximises, Danskin + dominated
convergence give P'^+ = sum_V int_{normal cone} <V', theta> = sum_V 2 sin(eps_V/2) <V', n_V>. Candidate vertex: <= v eps_V.
H vertex: interior angle = B_H (H is a vertex iff the candidates lie in a sector of opening < pi), u lies in that sector at angle
x <= B_H/2 from -n_H, contribution -2 cos(B_H/2) cos x <= -(1 + cos B_H); candidates give <= v(2pi - (pi - B_H)) = v(pi + B_H).
H not a vertex forces B_H = pi and the bound 2 pi v holds. P <= 2 Phi via width <= sum of |projected edges| and
int_0^pi |e . theta| = 2|e|; P >= 2 diam >= 2 max rho_i. Removal of a candidate at H leaves the hull unchanged, so P is Lipschitz
across catches. OK.

### Theorem A3.5
The bound -(1+cos B) + v(pi + B) has derivative sin B + v > 0, so B_H <= gamma gives P' <= -c_H; P >= 2 rho_j > 0 until the end;
T_end - t_f <= P(t_f)/c_H <= 2 Phi(t_f)/c_H <= 2 Psi(t_f)/((1-lambda) c_H); combine as in A2.3 with mu = min{m, (1-lambda)c_H/2}. OK.

Remark checks: "sector implies (E_gamma)" is right (u points at a candidate in the sector). The 0.2928 threshold: comparing
cos gamma - v with c_H/2 reduces to g(gamma) = cos gamma - 1 + v(pi + gamma - 2) >= 0, g concave on [0, pi/2], g(0) > 0, and
g(arccos v) >= 0 iff v(pi + arccos v) >= 1 + v, root 0.2928061625 (computed); at that v also gamma_H = arccos v, so for
v >= 0.2928 the A3.5 range of gamma lies inside the A2.3(i) range. gamma_H(0.1) = 2.0701 (paper 2.07);
pi - gamma_H ~ 2 sqrt(pi v) from 1 + cos(pi - delta) ~ delta^2/2 = 2 pi v. OK.

### Conditional labelling
Theorems `thm:B`, `thm:B2`, `thm:A23`, `thm:A35` all carry "Conditional"/"conditional" in their titles and state their
hypotheses ((H), (K), (E_gamma)/(E_K), sector) inside the theorem. The remarks mark numerical support as NUMERICAL;
Section "What is not proved" item 1 lists all four as conditional and the abstract says so. That (H) and (K) are end-phase
hypotheses is justified by Lemma A3(c) (they hold automatically while ordered). OK.

### Remarks not fully verified (outside the logical chain, no verdict)
"The cone condition fails for some well-separated non-dyadic sets" (after A2.3) and "with (H) alone no functional
Phi + kappa rho_N can be certified beyond 1/(1+pi)" (after B2) are not proved in the paper. The second is easily confirmed
(states with W ~ pi and beta_N ~ pi, resp. beta_N ~ 0, defeat kappa >= 0, resp. kappa < 0); the first should cite the code or
report that shows it.

## Comparison with earlier reports (read after the verdicts above were written)
* referee-RB flagged (1) Lemma B1 continuity at an accidental catch of S_N and (2) Theorem B2's positivity argument and a wrong
  10th decimal of v1. In the current text both are fixed: B1 states and proves the downward jump, B2 uses lambda = lambda* with an
  analytic positivity argument, and the printed v1 = 0.47475263829... agrees with my 50-digit value. No disagreement.
* referee-RA/RA2/RA3 report presentational gaps (base case of A3, definition of t_f, B_H discontinuous at catches); the current
  text defines t_f, states A3(c) with its base case, and A3.4 only uses P (continuous), not B_H. No disagreement.
