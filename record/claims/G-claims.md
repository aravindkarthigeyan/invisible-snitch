## 2. Statements and proofs

**Conventions.** As in E-1 section 2. H is 1-Lipschitz, u = H' (exists a.e., |u| <= 1). For a candidate
alpha: S_alpha, r_alpha = S_alpha - H, rho_alpha = |r_alpha|, rhat = r/rho. The field
(S,t) -> v (S - H(t))/|S - H(t)| is continuous, and C^infinity in S away from H(t), so trajectories are
unique and C^1 while rho > 0 and depend C^1 on alpha. Capture time tau(alpha) in (0, infinity]
(epsilon = 0); sighting time sigma(alpha) = first t with rho <= epsilon (epsilon > 0).
U(t) = {alpha : tau(alpha) > t} is the set of uncaught directions. It is open (Lemma 4 of
snitch_proved.tex, "Claim"), so tau is lower semicontinuous, hence Borel. Facts used:
- (P0) rho_alpha is absolutely continuous while positive, with rho_alpha' = v - u.rhat >= -nu a.e.
  Hence rho_alpha(t) >= d - nu t, and no capture happens before d/nu. Also |r'| <= 1 + v.
- (V) Variational equation (Prop 6(2) of snitch_proved.tex; H' does not appear):
  d/dt d_alpha S = (v/rho)(I - rhat rhat^T) d_alpha S. So |d_alpha S(alpha, t)| = d exp( int_0^t (v/rho) sin^2 phi ds ),
  where phi is the angle between d_alpha S and rhat. In particular |d_alpha S| is non-decreasing in t.
- (E1) For alpha != alpha' both uncaught on [t1, t2], |S_alpha - S_alpha'| is non-decreasing there:
  d/dt |S_1 - S_2|^2 = 2v (rho_1 + rho_2)(1 - cos psi), with psi the angle at Harry. [E-1, Lemma E1.]
- (E3c) If every direction is caught by time T, then T >= t + L(t)/nu for every t, where
  L(t) = H^1({S_alpha(t) : alpha in U(t)}) = int_{U(t)} |d_alpha S(alpha,t)| d alpha. [E-1, Thm E3(c). It is
  also the case J = (t, T] of G3 below.]

### Theorem G1 (hull growth before first contact). PROVED.
Let t_* be any time such that rho_alpha(t) > 0 for all alpha and all t < t_*. Examples: the first capture
time, or for epsilon > 0 the first sighting time. For t < t_*, let K(t) be the convex hull of the
wavefront Gamma(t) = {S_alpha(t)}. Then

    Per K(t) >= 2 pi d + 2 v t,   and therefore   L(t) = length Gamma(t) >= 2 pi d + 2 v t.

*Proof.*
1. *Harry is inside K.* For s <= t < t_* the map (alpha, s) -> S_alpha(s) - H(s) is continuous and nonzero on
   circle x [0, t]. So the winding number of Gamma(t) about H(t) is 1, as at s = 0. A closed curve with
   nonzero winding number about a point p cannot lie in an open half-plane missing p, so H(t) is in K(t).
   Hence rho_alpha(t) <= diam K(t) for every alpha.
2. *Support function.* Let g(theta, t) = max_alpha S_alpha(t).e_theta, with e_theta = (cos theta, sin theta).
   By Cauchy's formula, Per K(t) = int_0^{2 pi} g(theta, t) d theta. Each S_alpha is C^1 in t with
   d/dt S_alpha = v rhat_alpha. This is jointly continuous in (alpha, t) on circle x [0, t_*), since rho > 0
   there, and the circle is compact. By Danskin's theorem the right derivative exists and equals
   D^+ g(theta, t) = max over maximisers alpha of v rhat_alpha.e_theta.
3. *Lower bound.* For a maximiser alpha, r_alpha.e_theta = g(theta,t) - H(t).e_theta =: f(theta,t) >= 0 by step 1.
   So v rhat_alpha.e_theta = v f / rho_alpha >= v f / D(t), where D(t) = diam K(t).
4. *Integrate in theta.* g(theta, .) is v-Lipschitz, so Per K is Lipschitz and, for a.e. t,
   (Per K)' = int d_t g d theta >= (v/D) int f d theta = (v/D)(Per K - int H.e_theta d theta) = v Per K / D.
   For a compact convex set D <= Per/2, so (Per K)' >= 2v a.e. Also Per K(0) = 2 pi d.
5. A closed curve is at least as long as the perimeter of its convex hull. QED

### Corollary G2 (lower bound, epsilon = 0). PROVED.
If a path with |H'| <= 1 catches every direction by time T, then

    T >= (1 + 2 pi) d / nu + 2 v d / nu^2,     as well as (E5)  T >= d/nu + 2 pi d / nu^{3/2}.

*Proof.* By (P0) the first capture time t_1 is >= d/nu. For t < d/nu, (E3c) and G1 give
T >= t + (2 pi d + 2 v t)/nu. Let t increase to d/nu. QED

Numbers (d = 1; E5 in brackets): v = 0.5: 18.6 [19.8]; v = 0.7: 39.8 [41.6]; v = 0.8: 76.4 [75.2];
v = 0.9: 252.8 [208.7]; v = 0.95: 905.7 [582.0]; v = 0.99: 20,528 [6,383]. The new bound wins for
v >= 0.8 and grows like 2/nu^2 instead of 2 pi/nu^{3/2}.

For the straight first run the true value L(d/nu) is 7.68, 11.72, 18.59, 26.86, 50.68, 96.43, 443.06 at
v = 0.2, 0.5, 0.7, 0.8, 0.9, 0.95, 0.99. These are NUMERICAL (`code/G/first_run_length.py`: exact map, polyline
with 8e4 points log-spaced near alpha = 0; the change under doubling is < 2e-7). So L nu/(2 pi) = 0.98 ... 0.71:
the first-contact length is of order 1/nu, and G1 shows that order 1/nu is forced (2v/nu forced, about 4.4/nu
achieved by the straight run at v = 0.99).

### Corollary G2' (lower bound, epsilon > 0). PROVED.
Let 0 < epsilon < d. If every direction is seen by time T, then for every lambda > 0

    T >= (d - epsilon)/nu + [ pi d + v (d - epsilon)/nu - pi lambda - 2 pi epsilon ] / ( nu (1 + 2 epsilon/lambda) ).

With lambda = d nu^{-1/2} this gives T >= (1 - O(sqrt nu)) v (d - epsilon)/nu^2 as v -> 1, for fixed epsilon/d.
So seeing everything also takes time of order 1/(1 - v)^2. (E-1's epsilon > 0 corollary is of order 1/nu.)

*Proof.*
1. Let t_s >= (d - epsilon)/nu be the first sighting time (P0), and fix t < t_s. By G1, Per K(t) >= 2 pi d + 2 v t.
2. Fix delta > 0 and split [t, T] into k = ceil((T - t)/delta) intervals I_i of length delta. Let A_i be the set
   of positions at time t of the candidates first seen during I_i. By E3' (run from time t instead of 0, which
   E1 on [t, sigma] permits), diam A_i <= nu delta + 2 epsilon =: D_delta.
3. In each nonempty A_i pick a point p_i, belonging to a candidate with sighting time s_i. Taken in increasing i,
   consecutive points satisfy |p_i - p_j| <= 2 epsilon + nu (s_j - s_i) (E3' again). So the polyline c through
   them has length ell <= 2 epsilon (k - 1) + nu (T - t).
4. Every point of Gamma(t) lies in some A_i, hence within D_delta of c. So K(t) is contained in
   conv(c) + B(0, D_delta). By monotonicity of perimeter and Steiner's formula,
   Per K(t) <= Per conv(c) + 2 pi D_delta <= 2 ell + 2 pi D_delta.
   Here Per conv(c) = int_0^pi width_theta(c) d theta <= int_0^pi TV(c.e_theta) d theta = 2 ell (Cauchy-Crofton).
5. Combine, using k - 1 < (T - t)/delta and lambda := nu delta:
   pi d + v t <= nu (T - t)(1 + 2 epsilon/lambda) + pi lambda + 2 pi epsilon.
   The resulting lower bound on T increases with t; let t increase to (d - epsilon)/nu, which is <= t_s. QED

Remark. The factor 2 lost against G2 is genuine for this method. With epsilon > 0 a thin loop can be seen by
a path along one of its two strands; step 4 is sharp for segments.

### Theorem G3 (catch rate, unconditional measure form). PROVED.
For every t >= 0 and every Borel set J in (t, infinity),

    int_{tau^{-1}(J)} |d_alpha S(alpha, t)| d alpha  <=  nu |J|.                                (G3a)

Let m(alpha) := lim_{s increasing to tau(alpha)} |d_alpha S(alpha, s)|, in [d, infinity], be the stretch just before
capture. The limit exists by (V). Then

    int_{tau^{-1}(J)} m(alpha) d alpha  <=  nu |J|   for every Borel J in (0, infinity).          (G3b)

In particular, if every direction is caught by T, then T >= d/nu + (1/nu) int_0^{2 pi} m(alpha) d alpha.

This is E-1's Corollary E4(b) ("alpha'(tau) |d_alpha S| <= 1 - v") without its hypotheses: no monotone or
absolutely continuous catch order, and no continuity of d_alpha S at the caught point.

*Proof.*
1. On the open set U(t), the map F_t(alpha) = S_alpha(t) is C^1, and it is injective by E1. Let B = tau^{-1}(J),
   a Borel subset of U(t).
2. Take alpha, alpha' in B with tau(alpha) <= tau(alpha'). By E1 on [t, tau(alpha)) and then (P0),
   |F_t(alpha) - F_t(alpha')| <= |H(tau(alpha)) - S_alpha'(tau(alpha))| = rho_alpha'(tau(alpha)) <= nu (tau(alpha') - tau(alpha)).
   So tau is injective on B, and the map tau(alpha) -> F_t(alpha) from tau(B) onto F_t(B) is nu-Lipschitz.
3. A Lipschitz map multiplies one-dimensional Hausdorff measure by at most its constant:
   H^1(F_t(B)) <= nu H^1(tau(B)) <= nu |J|.
4. By the area formula for the injective C^1 map F_t (applied on compact pieces of U(t)),
   H^1(F_t(B)) = int_B |d_alpha S(alpha,t)| d alpha. This is (G3a).
5. For (G3b), first let J lie in (a, b] with a >= 0; recall tau > 0 always. For n >= 1 split (a, b] into 2^n
   dyadic intervals (t_k, t_{k+1}]. Apply (G3a) at time t_k to J intersected with (t_k, t_{k+1}], and sum:
   int_{tau^{-1}(J)} |d_alpha S(alpha, t_{k(alpha), n})| d alpha <= nu |J|,
   where t_{k(alpha),n} is the left end of the dyadic interval containing tau(alpha). As n grows,
   t_{k(alpha),n} increases to tau(alpha), staying strictly below it. |d_alpha S| is non-decreasing in time (V),
   so monotone convergence gives (G3b) for J in (a, b]. Let a -> 0 and b -> infinity.
6. For full capture by T, tau takes values in [d/nu, T] by (P0), and m >= d. QED

### Proposition G4 (stretching costs time: accounting inequality). PROVED.
Suppose every direction is caught by T. For s < t < T let

    Str(s, t) = int_s^t int_{U(t)} (v/rho_alpha(r)) sin^2 phi_alpha(r) |d_alpha S(alpha, r)| d alpha dr,

the total amount by which the part of the wavefront still uncaught at time t was stretched during [s, t]. Then

    T >= s + ( L(s) + Str(s, t) ) / nu    for all s < t < T.

In words: after time s Harry needs L(s)/nu to eat what is there, plus 1/nu for every unit of length by which
the uncaught wavefront is later stretched.

*Proof.* By (V), L(t) = int_{U(t)} |d_alpha S(alpha,t)| = int_{U(t)} |d_alpha S(alpha, s)| + Str(s,t). By (G3a) at
time s with J = (s, t], the part of L(s) caught during (s, t] has length
int_{U(s) \ U(t)} |d_alpha S(alpha,s)| <= nu (t - s). So L(t) >= L(s) - nu (t - s) + Str(s, t). Insert this
into T >= t + L(t)/nu (E3c). QED

*Reading.* A path finishes in finite time iff it stretches the uncaught wavefront by a finite total amount.
An impossibility proof for v near 1 is therefore exactly a proof that every path that catches everything
must stretch the uncaught wavefront by an infinite total amount. Before contact stretching is forced: by G1,
the hull perimeter grows at rate >= 2v. After contact it is not forced pointwise: a straight radial segment
ahead of Harry is eaten with zero stretching (Prop 3: the whole forward ray is caught, with phi = 0 on it).

### Lemma G5 (hull lemma after contact; the needle condition). PROVED.
Let X(t) = {H(t)} union {S_alpha(t) : alpha in U(t)}, K(t) = conv X(t), P(t) = Per K(t), and
D(t) = sup_{alpha in U(t)} rho_alpha(t); assume U(t) is nonempty. If H(t) is an extreme point of K(t) with a
nondegenerate normal cone, let gamma(t) in [0, pi) be the interior angle of K(t) there. Otherwise put
cos(gamma/2) := 0. Then P is 1-Lipschitz on [0, T] (with P(T) = 0 if everything is caught by T), and for a.e. t

    P'(t) >= v P(t)/D(t) - 2 |H'(t)| cos(gamma(t)/2)  >=  2 v - 2 cos(gamma(t)/2)  >=  -2 nu.

Consequences:
- (i) T - t >= P(t)/(2 nu) for full capture by T.
- (ii) **Needle condition.** At a.e. time at which P'(t) < 0, two things hold. First, cos(gamma/2) > v, so the
  uncaught set lies in a cone at Harry of opening < 2 arccos v, about 2 sqrt(2 nu). Second, P < (2/v) D, so
  K is a needle: its minimal width w satisfies w/D < sqrt(1 - v^2)/v, about sqrt(2 nu).

*Proof.*
1. *Support function.* Let g(theta, t) = sup_{x in X(t)} x.e_theta and f = g - H.e_theta >= 0. So
   f(theta,t) = max(0, sup_{U(t)} r_alpha(t).e_theta), and P(t) = int g d theta = int f d theta.
2. *g is 1-Lipschitz in t.* Let s > t. A candidate uncaught at s moved at most v(s - t). One caught at
   tau in (t, s] was at H(tau) then, and H(s) is within s - tau of H(tau). H(s) is within s - t of H(t). So each
   point of X(t) is within s - t of a point of X(s), and vice versa. If all are caught by T, X(T) = {H(T)}.
3. *Directions with f(theta,t) > 0.* Take alpha_n in U(t) with S_{alpha_n}(t).e_theta -> g(theta,t). For large n,
   r_{alpha_n}(t).e_theta >= f/2, so rho_{alpha_n}(t) >= f/2, and by (P0) alpha_n stays uncaught for time >= f/(2 nu).
   For 0 < h < f/(2 nu) and r in [t, t+h] we have r_{alpha_n}(r).e_theta >= r_{alpha_n}(t).e_theta - (1+v)(r - t) and
   rho_{alpha_n}(r) <= D(t) + (1+v)h. Hence
   g(theta, t+h) >= S_{alpha_n}(t+h).e_theta >= S_{alpha_n}(t).e_theta + v h (r_{alpha_n}(t).e_theta - (1+v)h)/(D(t) + (1+v)h).
   Let n -> infinity, divide by h, and let h -> 0: D_+ g(theta, t) >= v f(theta,t)/D(t).
4. *Directions with f(theta,t) = 0.* Then g(theta,t) = H(t).e_theta and g(theta, t+h) >= H(t+h).e_theta. So
   D_+ g(theta,t) >= u(t).e_theta wherever H is differentiable.
5. *Integrate.* By step 2 and Fubini, for a.e. t the derivative d_t g(theta,t) exists for a.e. theta, and
   P'(t) = int d_t g d theta. Let N(t) = {theta : f(theta,t) = 0}; this is the normal cone of K(t) at H(t). Then
   P' >= (v/D) int_{not N} f d theta + int_N u.e_theta d theta = v P/D + int_N u.e_theta d theta.
   If H is a vertex with angle gamma, N is an arc of length pi - gamma, and
   int_N u.e_theta >= -2|u| sin((pi - gamma)/2) = -2|u| cos(gamma/2). Otherwise N is null.
   Finally D <= diam K <= P/2.
6. (i) P decreases at rate at most 2 nu, and P(T) = 0.
   (ii) If P' < 0 then 2 cos(gamma/2) > v P/D >= 2v, and v P/D < 2. For the width: K contains a diameter
   segment [a, b] of length D. In the direction normal to it, K has width >= w, so it contains points c, c' on
   the two support lines parallel to [a, b], at heights h1, h2 >= 0 on either side of the line ab, with
   h1 + h2 >= w. Since |ca|, |cb|, |c'a|, |c'b| <= D, the projections of c and c' onto the line ab lie in
   [a, b], so a, c, b, c' is a convex quadrilateral inside K and P >= |ac| + |cb| + |bc'| + |c'a|.
   Now |ac| + |cb| >= sqrt(D^2 + 4 h1^2), and likewise for c'. By convexity of h -> sqrt(D^2 + 4h^2),
   P >= 2 sqrt(D^2 + (h1 + h2)^2) >= 2 sqrt(D^2 + w^2). So P < 2D/v gives w/D < sqrt(1/v^2 - 1). QED

*Reading.* Before contact gamma = pi, and G5 reduces to G1. Right after a straight first run catches alpha = 0,
the uncaught set fills exactly the cone of opening 2(pi - theta*) = 2 arccos v at Harry (Prop 5 of
snitch_proved.tex: the bearings fill (theta*, 2 pi - theta*)). That is the borderline case of (ii). So for v
near 1, Harry can make progress in this measure only while the remaining wavefront is a needle of relative
width O(sqrt nu) pointing at him.

### Corollary G6 (time forced into needle configurations). PROVED.
Call t a *needle time* if cos(gamma(t)/2) > v and P(t) < 2 D(t)/v (notation of G5). If a path catches every
direction by T, and t_1 >= d/nu is its first capture time, then

    | { t in (t_1, T) : t is a needle time } |  >=  P(t_1)/(2 nu)  >=  (pi d + v t_1)/nu  >=  pi d/nu + v d/nu^2.

*Proof.* At a.e. non-needle time, G5 gives P' >= 0: if cos(gamma/2) <= v then P' >= vP/D - 2 cos(gamma/2) >= 2v - 2v;
if P >= 2D/v then P' >= 2 - 2 cos(gamma/2) >= 0. At needle times P' >= -2 nu. P is Lipschitz with P(T) = 0, so
P(t_1) = -int_{t_1}^T P' <= 2 nu |needle times|. Finally P is continuous and, for t < t_1, K(t) = conv Gamma(t)
because H(t) is in conv Gamma(t) (G1 step 1); so P(t_1) >= 2 pi d + 2 v t_1 by G1. QED

So an impossibility proof near v = 1 would follow from showing that a path cannot keep the uncaught
wavefront inside a cone of opening 2 arccos v at Harry, as a needle of width ratio < sqrt(1 - v^2)/v, for a
total time of pi d/nu + v d/nu^2. This is the sharpest form of "a quantity Harry cannot overcome" I found;
whether it is overcome is exactly the open question (section 3 shows the greedy sweep does overcome it for
v <= 0.75).

