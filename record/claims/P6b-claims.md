# P6b-claims — statements and proofs of the PROVED claims of stream P6b (order route)

Nothing here proves the round-6 goal. All four claims are either unconditional lemmas or **conditional** reductions;
the hypotheses (N) and (S_γ) below are NOT proved. Formulation unchanged: d = 1, Harry speed ≤ 1, path fixed in advance,
S' = v(S − H)/|S − H|, vision radius ε ∈ (0,1). No strengthening.

Notation (paper/main.tex, paper/sec_D3.tex). r = S − H, ρ = |r|, r̂ = r/ρ, θ = polar angle of r. For a C² family
α ↦ S_α(t): T = ∂_αS, τ = angle of T, φ = τ − θ (angle from r̂ to T), κ = ∂_ατ/|T| (signed curvature; κ = +1 on the
initial circle), and

  w := ∂_αθ   (the α-derivative of the bearing; it does not depend on the heading used to measure bearings).

Chase LG0, α*(t), α_e(t), U(t), the remaining arc 𝒜(t) = {S_α(t): α ∈ [α*(t), α_e(t)]}, Λ, Ψ = ρ_{α*} + Λ, order (O),
t_0 = 1/(1−v): exactly as in paper/sec_D3.tex §"The ordered phase" (Proposition D3.2). On a leg, β = θ − ω, ω the
heading angle.

Regularity used throughout: if ρ > 0 on J × [0, t] for a compact α-interval J, then ρ is bounded below there, the field
v(x − H(s))/|x − H(s)| is C^∞ in x near the trajectories and continuous in s, so (α, s) ↦ S_α(s) is C^∞ in α with all
α-derivatives continuous in (α, s) (and C¹ in s on each leg), and T ≠ 0 (Lemma A3.2 of reports/A-3.md).

---------------------------------------------------------------------------------------------------------------------

## Lemma P6b.1 (the bearing derivative). PROVED

Let ρ > 0 on J × [t_1, t_2]. Then
 (i)  w = |T| sin φ / ρ = (r × T)/ρ²   (× = planar cross product);
 (ii) on a unit-speed straight run with heading angle ω (β = θ − ω):  ∂_t θ = sin β/ρ  and
      ∂_t w = |T| sin(φ − β)/ρ²;
 (iii) at a point where sin φ = 0 (so cos φ = ±1):  ∂_α w = cos φ · |T|² κ / ρ.

*Proof.* (i) θ = arg r, ∂_α r = T, so ∂_αθ = (r × T)/ρ² and r × T = ρ|T| sin φ.
(ii) r' = v r̂ − u with u = (cos ω, sin ω); ∂_tθ = (r × r')/ρ² = −(r × u)/ρ² = −ρ sin(ω − θ)/ρ² = sin β/ρ. All quantities
are smooth in α, so ∂_t w = ∂_α(sin β/ρ) = cos β · w/ρ − sin β · ∂_αρ/ρ², and ∂_αρ = r̂·T = |T| cos φ; with (i),
∂_t w = |T|(sin φ cos β − cos φ sin β)/ρ².
(iii) ∂_α w = (r × ∂_αT)/ρ² + (T × T)/ρ² − 2(r × T)(r·T)/ρ⁴ = (r × ∂_αT)/ρ² at a point with r × T = 0. Write
∂_αT = (∂_α|T|) T̂ + |T|²κ N̂ (N̂ = T̂ rotated by +90°). There r̂ = cos φ · T̂, so r × T̂ = 0 and r × N̂ = ρ cos φ. ∎

Numerical check (code/P6b/test_identities.py, finite differences on random arcs and runs): relative errors
2·10⁻⁶ (i), 8·10⁻⁶ (ii), 1.3·10⁻⁵ (iii).

---------------------------------------------------------------------------------------------------------------------

## Proposition P6b.2 (order can only be lost through a radial tangency at an inflection or at the far end). PROVED

Call α ∈ [α*(t), α_e(t)] a **bad point at time t** if sin φ(α, t) = 0 (the tangent line of the arc at S_α(t) passes
through Harry) and, in addition, either κ(α, t) = 0 or α = α_e(t). At a switch time the arc of the leg that ends is meant.
Let T_1 > t_0 and assume

  **(N)** at every time t ∈ [t_0, T_1] of LG0 at which U(t) ≠ ∅ there is no bad point.

Then (O) holds at every t ∈ [t_0, T_1] with U(t) ≠ ∅. Consequently (Proposition D3.2(d), whose proof is local in time)
no point of the arc is caught on [t_0, T_1], K ≤ π there, and for t_0 ≤ t ≤ T_1:
Ψ(t) ≤ Ψ(t_0) − (1 − v(1+π))(t − t_0), Ψ(t_0) ≤ 2π/(1 − v).

*Proof.* Legs are finite in number before T_1 (Prop. D6(a)). We prove by induction over legs the statement
  (I_j): at the start t_s of leg j, (O) holds and sin φ(α*, t_s) > 0 (i.e. w(α*, t_s) > 0).
*Base.* At t_0, by Proposition "Bearings stay ordered" of main.tex (with c = −1; see the proof of Lemma A1), h/C is a
C¹ function of α ∈ (0, 2π)∖{π} with derivative of the sign of −(1+v)(1 − cos α) ≠ 0, and k' ≠ 0, so w > 0 there; (O)
at t_0 is D3.2(a). The first target lies in (0, 2π). If it equals π, w(π, t_0) ≥ 0 by (O), and w(π, t_0) = 0 would make
π an interior minimum of w ≥ 0 unless π = α_e (then U = ∅): then ∂_αw = 0, so κ = 0 by P6b.1(iii): a bad point,
excluded by (N).
*Within a leg* [t_s, t_e], t_e ≤ T_1 (or the leg truncated at T_1), assume (I_j). Let
s* := sup{s ∈ [t_s, t_e] : (O) holds on [t_s, s]}. While (O) holds no arc point is caught (only the target has bearing 0,
Proposition "ray"), and the arc at a later time is a subset of the arc at an earlier time (α_e non-increasing), so
ρ > 0 on [α*, α_e(s*)] × [0, s*] and, by compactness and continuity, on a slightly longer time interval; the regularity
statement applies.
 Step 1: β(·, s*) is non-decreasing on J* := [α*, α_e(s*)] with values in [0, π] (limit of (O) at times s ↑ s*; if
 s* = t_s it is (O) at t_s). Hence w(·, s*) ≥ 0 on J*.
 Step 2: β(·, s*) is strictly increasing. Otherwise β(·, s*) is constant on some [P, Q] ⊂ J*, P < Q, so w = 0 and
 ∂_αw = 0 on (P, Q); by P6b.1(i),(iii) every α ∈ (P, Q) has sin φ = 0 and κ = 0: a bad point. So (O) holds at s*.
 Step 3: s* = t_e. Suppose s* < t_e. Then there are s_n ↓ s* at which (O) fails. On the leg, bearings in (0, π) stay in
 (0, π), the target stays at 0 and a point at π stays at π (Lemma A2 of main.tex), so, (O) holding at s*, all bearings of
 arc points lie in [0, π] at s_n; hence failure means: there are P_n < Q_n in [α*, α_e(s_n)] ⊂ J* with
 β(P_n, s_n) ≥ β(Q_n, s_n). By the mean value theorem there is ξ_n ∈ [P_n, Q_n] with w(ξ_n, s_n) ≤ 0. Pass to a
 subsequence P_n → P, Q_n → Q, P ≤ Q in J*. If P < Q then β(P, s*) ≥ β(Q, s*), contradicting Step 2. So ξ_n → α_0 := P = Q,
 and w(α_0, s*) ≤ 0 by continuity; with Step 1, w(α_0, s*) = 0, so sin φ(α_0, s*) = 0.
  - α_0 = α_e(s*): bad point. Excluded.
  - α* < α_0 < α_e(s*): α_0 is an interior minimum of w(·, s*) ≥ 0, so ∂_αw(α_0, s*) = 0 and κ(α_0, s*) = 0 by
    P6b.1(iii): bad point. Excluded.
  - α_0 = α* (< α_e(s*)): the target stays on the forward ray, θ(α*, ·) is constant on the leg, so by Lemma A3.2
    φ* := φ(α*, ·) solves φ*' = (v/2ρ*) sin 2φ*, ρ* ≥ ε/2. The solution through sin φ* = 0 is constant, so by uniqueness
    sin φ*(s*) = 0 would force sin φ*(t_s) = 0, contradicting (I_j).
 So s* = t_e, and (O) holds on the whole leg (Step 2 at s* = t_e).
*Switch.* If U(t_e) ≠ ∅, (O) holds at the start of leg j+1 by D3.2(c). The new target α** = inf U(t_e) satisfies
α* < α** ≤ α_e(t_e); if α** = α_e(t_e) then U(t_e) ⊂ (α**, α**] = ∅, excluded. So α** is an interior point of the old
arc, where w(·, t_e) ≥ 0 (w does not depend on the heading). If w(α**, t_e) = 0 it is an interior minimum, so
∂_αw = 0, κ = 0, sin φ = 0: a bad point at time t_e. Excluded. So (I_{j+1}) holds.
The consequences are D3.2(d) applied on [t_0, T_1] (its proof uses (O) only up to the time considered). ∎

*Remarks (not needed for the proof).* (1) At an interior first failure the tangent points away from Harry: cos φ = +1.
Indeed by P6b.1(ii) at sin φ = 0, ∂_t w = −cos φ |T| sin β/ρ², and β ∈ (0, π); with cos φ = −1 one would get w < 0 just
before s*. This is Lemma A4 of main.tex ("the closer point overtakes") in differential form. (2) In particular: if the
arc is strictly locally convex (κ > 0 on [α*, α_e]) and the tangent at the far end is never radial, order is never lost.
Geometrically: order is first lost when Harry crosses the tangent line at an inflection point of the remaining arc (or
the tangent line at its far end).

---------------------------------------------------------------------------------------------------------------------

## Lemma P6b.3 (far-field convexity). PROVED

Let H be any path with |H'| ≤ 1 and let a direction α have ρ > 0 on [0, t] (and its neighbours too). Put
J_1 := ∫_0^t ds/ρ_α(s), J_2 := ∫_0^t ds/ρ_α(s)². Then, with κ_0 = κ(α, 0) (= 1 for the initial circle),

  κ(α, t) ≥ e^{−2vJ_1} κ_0 − v e^{vJ_1} J_2.

In particular κ(α, t) > 0 whenever v e^{3vJ_1} J_2 < κ_0: an inflection point of the front can only sit at a direction
with J_2 ≥ e^{−3vJ_1}/v.

*Proof.* Lemma A3.2 (reports/A-3.md, refereed): ∂_tκ = aκ − b with a = (v/ρ)(cos 2φ − sin²φ) = (v/ρ)(1 − 3 sin²φ)
∈ [−2v/ρ, v/ρ] and b = (v/ρ²) sin φ (3cos²φ − 1). With x = sin φ ∈ [−1, 1], |x(2 − 3x²)| ≤ 1 (the critical values are
±(4/9)√2 ≈ ±0.63 at x² = 2/9 and ∓1 at x = ±1), so |b| ≤ v/ρ². With A(s) = ∫_0^s a,
κ(t) = e^{A(t)}κ_0 − ∫_0^t e^{A(t)−A(s)} b(s) ds, A(t) ≥ −2vJ_1, A(t) − A(s) ≤ vJ_1. ∎

Numerical check (test_identities.py, 30 random piecewise-straight paths): max(lower bound − κ) = −6.5·10⁻³ ≤ 0.

---------------------------------------------------------------------------------------------------------------------

## Lemma P6b.4 (hull perimeter for the ε-chase). PROVED

For LG0 and t ≥ t_0 with U(t) ≠ ∅ let V(t) := cl U(t) ∪ {α*(t)} (compact), X(t) := {S_α(t) : α ∈ V(t)},
P(t) := perimeter of conv({H(t)} ∪ X(t)) (twice the length for a segment), and B(t) ∈ [0, π] the opening of the smallest
closed sector with apex H(t) containing X(t) (B := π if there is none of opening < π). Let
G(B) := −(1 + cos B) + v(π + B) (increasing on [0, π]). Then:
 (a) V(t) is non-increasing in t, and ρ_α ≥ ε/2 on [0, t] for α ∈ V(t);
 (b) if t < t' and B(s) ≤ γ for all s ∈ [t, t'], then P(t') ≤ P(t) + G(γ)(t' − t); always P(t') ≤ P(t) + 2πv(t' − t);
 (c) P(t) > 2ε while U(t) ≠ ∅, and P(t) ≤ 2Ψ(t) whenever ρ > 0 on [α*(t), α_e(t)] × [0, t].

*Proof.* (a) U is non-increasing and open. For α ∈ cl U(t), ρ_α ≥ ε on [0, t] by continuity (as in Prop. D6(a)). The
target of leg j is α*_j = inf U(t_j) ∈ cl U(t_j), has ρ ≥ ε up to t_j and ρ ≥ ε/2 during the leg. For t in leg j,
V(t) ⊂ cl U(t_j) ⊂ V(t_j^−), and inside a leg V(t) = cl U(t) ∪ {α*_j} is non-increasing.
(b) It is enough to treat t < t' in one leg (then add over legs; G(γ)-bounds and 2πv-bounds are additive, and (a) makes
the family monotone across switches because the argument below only uses V(t') ⊂ V(s) for s ≤ t'). Let F ⊂ V(t') be
finite with α*_j ∈ F and P_F(s) the perimeter of conv({H(s)} ∪ {S_α(s): α ∈ F}). On [t, t'] all points of F have
ρ ≥ ε/2 > 0 and Harry moves with constant unit velocity pointing at S_{α*_j}, a point of F. The proof of Lemma A3.4
(main.tex Lemma "Hull perimeter"; no point is removed here) gives: P_F is Lipschitz and P_F' ≤ G(B_F) a.e., where B_F is
the sector opening of F. Since F ⊂ V(s), B_F(s) ≤ B(s) ≤ γ, and G is increasing (G' = sin B + v > 0), so
P_F(t') ≤ P_F(t) + G(γ)(t' − t) ≤ P(t) + G(γ)(t' − t) (hull perimeter is monotone under inclusion of convex sets). The
perimeter of the convex hull of a compact set is the supremum over its finite subsets (Cauchy's formula and monotone
convergence of support functions along an increasing sequence of finite subsets with dense union). Take the supremum
over F. The second bound is γ = π.
(c) Some α ∈ U(t) has ρ_α > ε, and P ≥ 2 diam ≥ 2ρ_α. conv({H} ∪ X) lies in the convex hull of the curve formed by the
segment from H to S_{α*} followed by the arc 𝒜(t) (as V(t) ⊂ [α*, α_e(t)]), of length Ψ(t); the perimeter of the convex
hull of a rectifiable curve is at most twice its length (Cauchy: width ≤ total variation of the projection). ∎

---------------------------------------------------------------------------------------------------------------------

## Theorem P6b.5 (two-phase conditional reduction). PROVED (conditional on (N) and (S_γ); neither is proved)

Let v(1 + π) < 1 and γ ∈ [0, π] with c_γ := 1 + cos γ − v(π + γ) > 0. Suppose that for LG0 there is t_1 ≥ t_0 with
  **(N)** on [t_0, t_1] (no bad point, Proposition P6b.2), and
  **(S_γ)** for every t ≥ t_1 with U(t) ≠ ∅: X(t) lies in a closed sector with apex H(t) and opening ≤ γ.
Then every direction is seen by

  T ≤ t_0 + (2π/(1 − v)) / min{ 1 − v(1 + π), c_γ/2 },

a bound independent of ε. (For γ ≤ π/2 and v ≤ 0.1: T ≤ 1.12 + 6.99/0.264 ≤ 27.6.)

*Proof.* By P6b.2, Ψ(t_1) ≤ Ψ(t_0) − m(t_1 − t_0), m := 1 − v(1+π), Ψ(t_0) ≤ 2π/(1−v), and ρ > 0 on the arc up to t_1.
By P6b.4(b),(c), for t ≥ t_1 with U(t) ≠ ∅: 2ε < P(t) ≤ P(t_1) − c_γ(t − t_1) ≤ 2Ψ(t_1) − c_γ(t − t_1). So U = ∅ by
t_1 + 2Ψ(t_1)/c_γ ≤ t_1 + 2(Ψ(t_0) − m(t_1 − t_0))/c_γ ≤ t_0 + Ψ(t_0)/min{m, c_γ/2}. ∎
