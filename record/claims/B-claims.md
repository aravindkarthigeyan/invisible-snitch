## 3. Lemma B1 (PROVED): rate identity for Psi_lambda
Setting: the discrete chase of Section 4, chasing S_j, j <= N. Let rho_N = |S_N - H|, and let beta_N in (-pi, pi]
be the bearing of S_N from Harry's heading u (u = direction to S_j). Let W be as in Lemma 2 of the tex. Fix
lambda in [0,1) and set Psi = Phi - lambda rho_N.

**Lemma B1.** (a) `(1-lambda) Phi <= Psi <= Phi`. (b) Psi is continuous in t on [t0, end of chase].
(c) On each open leg, `Psi' = -(1-lambda)(1-v) + v W - lambda(1 - cos beta_N)`.

*Proof.* (a) Phi is the length of a polyline from H to S_N, so Phi >= |S_N - H| = rho_N >= 0.
(b) Phi is continuous (Lemma 2). rho_N is continuous because H(t) and S_N(t) are, and S_N is caught only at the end.
(c) By Lemma 2, Phi' = -(1-v) + vW. By (eq. polar), which holds for any constant heading, rho_N' = v - cos beta_N.
Hence Psi' = -(1-v) + vW - lambda v + lambda cos beta_N = -(1-lambda)(1-v) + vW - lambda(1 - cos beta_N).
When j = N we have Phi = rho_N, W = 0 (empty sum) and beta_N = 0, and the formula gives -(1-lambda)(1-v), which is
correct. []

*Degenerate case (remark, not used later).* If some S_i with i > j lies on the forward ray closer than S_j, it is
caught during the leg. Deleting it from the polyline does not increase Phi (triangle inequality). If i = N, rho_N
jumps from 0 up to rho_{N-1}, so Psi jumps down. Lemma 2 of the tex tacitly assumes this does not occur; the proof
above inherits that convention.

## 5. Conditional theorem (PROVED, conditional on (K))
Define, for 0 <= lambda < 1,
`m(v,lambda) = min_{0<=x<=pi} [ (1-lambda)(1-v) + lambda(1 - cos x) - v x ]`.
Closed form: if lambda <= v, m = m_pi := (1-lambda)(1-v) + 2 lambda - v pi. If lambda > v,
m = min(m_pi, m_int), where m_int = (1-lambda)(1-v) + lambda - sqrt(lambda^2 - v^2) - v arcsin(v/lambda).
The critical point x1 = arcsin(v/lambda) is the only interior local minimum, since the second derivative there is
lambda cos x1 > 0. This was checked against brute force on 2e6 grid points (`thr_exact.py`).

Hypothesis **(K)** (with constant w0 = 0.3): for every finite direction set containing 0 (it suffices to take the
dyadic ones), at every time of the discrete chase, `W <= max(|beta_N|, w0)`.

**Theorem B2.** Assume (K). Let v < v1, where v1 = 0.474752638033... is the unique v with max_lambda m(v,lambda) = 0
(it solves m_pi = m_int = 0, with lambda* = ((pi+1)v1 - 1)/(1+v1) = 0.65518...). Choose lambda with m(v,lambda) > 0.
Put c = min( m(v,lambda), (1-lambda)(1-v) - v w0 ), which is > 0. Then there is a path with |H'| <= 1 that catches
every candidate (eps = 0) by time
`T = d/(1-v) + 2 pi d / ((1-v) c)`.

*Proof.* By Lemma B1(c), on each leg Psi' = -(1-lambda)(1-v) + vW - lambda(1 - cos beta_N).
Case W <= |beta_N|: with x = |beta_N| in [0,pi], Psi' <= -[(1-lambda)(1-v) + lambda(1 - cos x) - v x] <= -m.
Case W <= w0: since 1 - cos beta_N >= 0, Psi' <= -(1-lambda)(1-v) + v w0.
So Psi' <= -c on every open leg. Psi is continuous (B1(b)), so Psi(t) <= Psi(t0) - c(t - t0) as long as the chase
runs. By B1(a), Psi >= 0, and Psi(t0) <= Phi(t0) <= 2 pi d/(1-v) (Lemma 3). Hence every discrete chase ends by T.
Apply the compactness Lemma 4 to nested dyadic sets.
Positivity of c: m > 0 by choice. For the second term, since w0 = 0.3, it suffices that
(1-lambda)(1-v)/v > 0.3 for the lambda used. At the optimal lambda this quantity decreases in v and equals 0.381 at
v1, so taking the optimal lambda gives c > 0 for all v < v1. In any case c is defined as the minimum, and the
theorem only needs c > 0. []

Numbers (optimal lambda, d = 1, from `thr_exact.py`): v = 0.2415: lambda = 0.333, m = 0.414, T <= 21.4;
v = 0.3: 0.414, 0.296, T <= 31.8; v = 0.35: 0.483, 0.203, 49.3; v = 0.4: 0.552, 0.116, 91.8;
v = 0.45: 0.621, 0.037, 313; v = 0.47: 0.649, 0.0069, 1713. Empirically lambda_opt ~ 1.38 v.

Remarks.
* (K) is implied by (H') "bearings of S_j, ..., S_N are non-decreasing in chase order, with total A <= pi", because
  W <= A (Lemma 2) and then A = |beta_N|. (H') implies (H).
* **Status of (K): CONJECTURE, strongly supported (NUMERICAL).** In every run (v in {0.2, ..., 0.5}, N up to 6400)
  the inequality W <= |beta_N| fails only in the end phase, and there W <= 0.011. The largest excess
  W - |beta_N| is 0.0076, 0.0090, 0.0106 at v = 0.5 for N = 1600, 3200, 6400, growing slowly with N. So (K) with
  w0 = 0.3 holds with a factor of about 30 to spare.
* (H') itself is **false** in simulation: bearings stop being monotone in the end phase. The non-monotone stretch
  grows with N: it starts with 29/68/150 candidates left at v = 0.5, N = 200/400/800, and max A there is
  0.18/0.24/0.29. The backtracking A - |beta_N| reaches 0.12 at N = 6400. That is why (K) is stated with the
  escape clause W <= w0 rather than as monotonicity.

**Prop B3 (PROVED): the argument of Theorem B2 is sharp at v1.** For every x in (0, pi] there are polyline states
with W -> x and |beta_N| = x: S_j at (r, 0), then S_{j+1}, ..., S_N on the circle of radius r about H at bearings
k x/n. Every triangle H S_k S_{k+1} is isosceles, so W = 2n sin(x/(2n)) -> x. For these states Psi' tends to
-[(1-lambda)(1-v) + lambda(1 - cos x) - v x]. So for v >= v1, (K) together with Lemma B1 cannot give a negative
rate for any lambda. []

**Prop B4 (PROVED): (H) alone cannot certify Phi + kappa rho_N beyond 1/(1+pi).** Let kappa be any real number.
(a) Same states as in B3 with x = pi: A = pi and W -> pi; with beta_N = pi, rho_N' = 1 + v, so the rate tends to
-(1-v) + v pi + kappa(1+v).
(b) Zig-zag states: S_j at (r,0), then vertices alternating between bearings delta and 0 at radii r(1 + k eta),
with n = floor(pi/delta) segments. Then A <= pi. As eta -> 0 each triangle tends to isosceles with apex angle
delta, so W -> 2n sin(delta/2) -> pi as delta -> 0. Also cos beta_N -> 1, so rho_N' -> -(1-v), and the rate tends
to -(1-v) + v pi - kappa(1-v).
Both families satisfy (H). Hence sup over (H)-states of (Phi + kappa rho_N)' >= -(1-v) + v pi for every kappa,
which is >= 0 when v >= 1/(1+pi). (These are abstract states; they need not occur in a chase.) []

## 7. The discrete chase changes behaviour at v = 1/2 (NUMERICAL + model PROVED + link CONJECTURE)
* T(v), N = 200/400/800: 37.0/37.5/37.9 at v = 0.46, 45.2/45.9/46.5 at 0.5, 55.8/58.6/60.5 at 0.51, 73/77/80 at 0.52,
  180/197/211 at 0.55. At v = 0.6 the times are 4.7e4, 1.3e9 and 3e19. There is a sharp kink at exactly 1/2
  (`tscan.py`).
* This is not rounding error. At v = 0.55, N = 200, relative noise up to 1e-10 per step changes T by < 1e-3
  (`noise_test.py`).
* Mechanism: a period-2 zigzag of Harry's turning angles. At v = 0.55 the alternating component grows by about
  1.6, 1.57, 1.54, 1.51, 1.49, 1.45 per leg from the first legs, then saturates with turns alternating +-1.47 rad
  for the rest of the chase. At v = 0.5 a small alternation (turns 0.030/0.002) persists without growing. At
  v = 0.45 it decays to 3e-4 (`zigprint.py`, `zigcmp.py`).
* **Linearised model.** Take candidates equally spaced by l on a straight radial line ahead of Harry, with small
  bearing deviations E_m of the m-th one from the current heading. During a leg, a small bearing scales as
  rho^{-q} with q = 1/(1-v) (from rho beta' = sin beta and rho' = v - cos beta). So at the catch
  E -> ((m+1)/m)^q E, and the turn is delta = 2^q E_2. Unrolling gives
  `delta_{n+1} = - sum_{k>=0} (k+2)^q delta_{n-k}`.
  The derivation is a heuristic linearisation (**CONJECTURE** that it governs the chase).
* **Prop B5 (PROVED, about the model).** With delta_0 = 1 and zero history, the generating function is
  D(z) = sum delta_n z^n = z / Li_{-q}(z), where Li_{-q}(z) = sum_{n>=1} n^q z^n.
  If 2 < q < 4 (1/2 < v < 3/4), Li_{-q} has a zero z0 in (-1,0), so limsup |delta_n|^{1/n} >= 1/|z0| > 1: the
  zigzag grows exponentially, at a rate independent of the step size.
  If q = 2 (v = 1/2), D = (1-z)^3/(1+z), so delta_n tends to a bounded, non-decaying period-2 oscillation.
  *Proof.* From the recursion, D - 1 = -z G(z) D with G(z) = sum_k (k+2)^q z^k, and
  1 + z G(z) = sum_{m>=0} (m+1)^q z^m = Li_{-q}(z)/z. For q not an integer, Li_{-q} continues analytically to
  C \ [1, inf), and Li_{-q}(-1) = -eta(-q) = (2^{1+q} - 1) zeta(-q). On (-4,-2), zeta has no zeros (its trivial
  zeros are -2 and -4) and zeta(-3) = 1/120 > 0, so zeta(-q) > 0 and Li_{-q}(-1) > 0. Near 0,
  Li_{-q}(-x) = -x + O(x^2) < 0, so there is a zero in (-1,0). It is a pole of D because the numerator z is
  nonzero there. For q = 2, Li_{-2}(z) = z(1+z)/(1-z)^3. []
  Numerically: model growth 1.071, 1.148, 1.231, 1.421, 2.078, 5.276 at v = 0.51, 0.52, 0.53, 0.55, 0.6, 0.7.
  For v <= 0.5 the recursion decays or is marginal (`zigzag_lin.py`). Measured in the chase: 1.11 at v = 0.51;
  1.45-1.6 in the earliest legs at v = 0.55.
* Consequence (**CONJECTURE**): the Section-4 discrete chase is the wrong strategy above v = 1/2. No functional can
  decrease uniformly along it with a bound uniform in N much beyond 1/2, and "ideally up to 1/2" is the natural
  ceiling for this stream. Above 1/2 a smoothed chase is needed, e.g. one that aims ahead of the next candidate,
  or the eps-sweep.

