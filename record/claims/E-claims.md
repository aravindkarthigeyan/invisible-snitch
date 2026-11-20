## 2. Statements and proofs

**Conventions.**
- H is 1-Lipschitz on [0, T] with H(0) = 0. A *candidate* is any initial point P ≠ H(0) of the plane; the circle |P| = d is the actual problem.
- S_P(t) solves (1) of snitch_proved.tex. Write r_P = S_P − H, ρ_P = |r_P| and r̂_P = r_P/ρ_P.
- The vector field (S, t) ↦ v(S − H(t))/|S − H(t)| is C^∞ in S on {S ≠ H(t)} and continuous in (S, t). So S_P exists, is unique and is C¹ while ρ_P > 0. It depends C¹ on the initial point (Hartman, *ODEs*, Thm V.3.1), and the derivative solves the variational equation.
- S_P is v-Lipschitz, so it extends continuously to the end of its maximal interval. The *capture time* τ(P) is the first time with S_P(τ) = H(τ), if one exists.
- **(P0)** Along any path, ρ_P is absolutely continuous while positive, with ρ_P' = v − r̂_P·H' ≥ −(1 − v) a.e.

### Lemma E1 (non-expansion: the time-reversed flow is a contraction). PROVED.
Let P ≠ Q, and suppose ρ_P, ρ_Q > 0 on an interval I. Then on I

  d/dt |S_P − S_Q| = v (ρ_P + ρ_Q)(1 − cos ψ) / |S_P − S_Q| ≥ 0,

where ψ is the angle between r_P and r_Q, the angle P–Harry–Q. In particular |S_P(t) − S_Q(t)| is non-decreasing, and stays ≥ |P − Q|.

*Proof.* S_P(t) = S_Q(t) at some t ∈ I is impossible, because forward uniqueness would then make the two trajectories equal back to time 0. So f = |S_P − S_Q| > 0 is C¹, and f' = v(r̂_P − r̂_Q)·(S_P − S_Q)/f = v(r̂_P − r̂_Q)·(r_P − r_Q)/f. Expanding with r_P = ρ_P r̂_P and r_Q = ρ_Q r̂_Q gives (r̂_P − r̂_Q)·(r_P − r_Q) = ρ_P + ρ_Q − (ρ_P + ρ_Q) r̂_P·r̂_Q = (ρ_P + ρ_Q)(1 − cos ψ). ∎

This is the monotonicity of the gradient r ↦ r/|r| of the convex function |r|. Note that H' does not enter.

### Corollary E2 (unique release; separated capture times). PROVED.
If P ≠ Q are both caught, with τ(P) ≤ τ(Q), then

  τ(Q) − τ(P) ≥ |P − Q| / (1 − v).

In particular two distinct candidates are never caught at the same instant, under any path. The same holds from any start time t ≤ τ(P), with |P − Q| replaced by |S_P(t) − S_Q(t)|.

*Proof.* On [t, τ(P)) both ρ_P and ρ_Q are positive. By E1 and continuity, ρ_Q(τ(P)) = |S_Q(τ(P)) − S_P(τ(P))| ≥ |S_P(t) − S_Q(t)|. By (P0), ρ_Q decreases at rate at most 1 − v until it reaches 0 at τ(Q). ∎

**Reconciliation with the reversed picture (task item 1).**
- *The picture.* Reverse time, s = T − t. Each candidate becomes a hound with dŜ/ds = −v r̂, a pure pursuer of speed v. A capture at time τ is a release from H(τ).
- *Is the release direction free?* The singular point r = 0 is a *repeller* in forward time: a Snitch placed on Harry can flee in any direction. In reversed time it is an *attractor*.
- *No: one hound per release time.* By E1 run backwards, two reversed solutions that both start at r = 0 at the same reversed time have non-increasing mutual distance, which starts at 0. So they coincide. **Each release time releases at most one hound, and its direction is forced.**
- *The forced direction.* If Harry runs straight just before τ, the hound leaves along −H', directly behind reversed Harry. In forward time that is capture on the forward ray, which is exactly Prop 3.
- *Where the "one-parameter family" comes from.* It is the forward-time emission family: continuations of a candidate after it has been caught, which do not matter for the game.
- *Consequence.* No single capture time catches an arc (E2).

### Theorem E3 (the catch curve is (1−v)-Lipschitz). PROVED.
Fix t ∈ [0, T]. Let K_t be the set of candidates that are uncaught at time t and caught by time T, and put X_t(P) = S_P(t) for P ∈ K_t. Then there is a (1−v)-Lipschitz curve c_t : [t, T] → ℝ² with

  c_t(t) = H(t),  c_t(τ(P)) = X_t(P) for all P ∈ K_t.

Consequently:
- **(a)** X_t(K_t) lies on a rectifiable curve that starts at H(t) and has length ≤ (1 − v)(T − t). In particular H¹(X_t(K_t)) ≤ (1 − v)(T − t).
- **(b) Zero area for every path.** For any 1-Lipschitz path on [0, ∞), the set of starting points P ∈ ℝ² that are ever caught is a countable union of sets of finite H¹-measure (take t = 0 and T = 1, 2, …). So it has Lebesgue measure 0. This generalises Prop 8 of snitch_proved.tex, which was proved only for locally finitely many straight pieces.
- **(c) Remaining-time bound.** If every direction is caught by time T, then for every t,
  T − t ≥ ℓ_t / (1 − v),
  where ℓ_t is the infimum of lengths of curves that start at H(t) and pass through every point of the closure of the set of current positions of uncaught candidates. Before first contact, Γ(t) is a C¹ Jordan curve not containing H(t), and then
  T − t ≥ (ρ_min(t) + L(t)) / (1 − v),  where ρ_min(t) = dist(H(t), Γ(t)) and L(t) = length(Γ(t)).
- **(d)** In particular (at t = 0): T ≥ (1 + 2π) d / (1 − v).

*Proof.*
1. *Definition.* Define c on E = {t} ∪ {τ(P) : P ∈ K_t}. By E2 (started at time t), τ is injective on K_t, so c is well defined.
2. *Lipschitz bound between two captures.* For P, Q ∈ K_t with τ(P) < τ(Q), E1 on [t, τ(P)] and then (P0) give |X_t(P) − X_t(Q)| ≤ |S_P(τ(P)) − S_Q(τ(P))| = ρ_Q(τ(P)) ≤ (1 − v)(τ(Q) − τ(P)).
3. *Lipschitz bound from the start point.* By (P0), |X_t(P) − H(t)| = ρ_P(t) ≤ (1 − v)(τ(P) − t).
4. *Extension to [t, T].* So c is (1−v)-Lipschitz on E. It extends to the closure of E by uniform continuity, and then to [t, T] by linear interpolation on each complementary open interval, constant after the last point. The constant is preserved: for x < y, split [x, y] at the nearest points of the closure of E and use the triangle inequality.
5. *(a), (b), (d).* For (a), use H¹(image) ≤ length. (b) follows from (a). (d) is (c) at t = 0, where ρ_min = d and L = 2πd.
6. *(c).* The image of c_t is closed and contains every current position of an uncaught candidate, since all of them are caught by T. Before contact, let t' be the first time at which c_t meets Γ(t). The piece of c_t on [t, t'] has length ≥ |c_t(t') − H(t)| ≥ ρ_min(t). The image of [t', T] contains Γ(t), so that piece has length ≥ H¹(Γ(t)) = L(t). ∎

### Corollary E4 (catch-rate bound; the author's condition is necessary in integrated form).
**Status.** Inequality (E4a) is PROVED under its hypotheses. (E4b) is PROVED assuming that ∂_αS extends continuously to the caught point (the regularity assumption, labelled as such).

Suppose the directions are caught in a non-decreasing, absolutely continuous order α(τ), with α(t₀) = 0 and α(T) = 2π.

**(E4a)** For every τ < τ' in the capture range, writing α₀ = α(τ) and α₁ = α(τ'),
  |S_{α₁}(τ) − S_{α₀}(τ)| ≤ (1 − v)(τ' − τ).
This is Thm E3 started at time τ, together with S_{α₀}(τ) = H(τ).

**(E4b)** Assume ∂_αS(·, τ) extends continuously to α(τ), where α(·) is differentiable. Then
  |∂_αS(α(τ), τ)| · α'(τ) ≤ 1 − v,  and so  2π ≤ (1 − v) ∫_{t₀}^{T} dτ / |∂_αS(α(τ), τ)|.

*Proof of (E4b).* Divide (E4a) by τ' − τ and let τ' ↓ τ. Then integrate α' ≤ (1 − v)/|∂_αS|. ∎

**Reading.** The author's sufficient condition |∂_αS(θ(t), t)| ≤ C(1 + t) is essentially the right one. If the stretch at the caught point grows so fast that ∫ dτ/|∂_αS| converges, that order cannot finish. If it grows at most linearly, the integral diverges and E4 is no obstruction.

### Theorem E5 (universal lower bound on capture time, ε = 0). PROVED.
If a path with |H'| ≤ 1 catches every direction on the circle of radius d by time T, then

  **T ≥ d/(1 − v) + 2πd/(1 − v)^{3/2}.**

*Comparisons.*
- This is strictly larger than (1 + 2π)d/(1 − v), the bound E3(d).
- It is below the conditional time of Theorem B. As v → 0, T_B = (1 + 2π)d + O(v), and the bound E5 equals (1 + 2π)d + O(v) too. The first-order terms are T_B: (1 + 4π + 2π²)vd, and E5: (1 + 3π)vd. So Theorem B would be sharp to leading order.
- Numerically (section 3), the greedy sweep takes about 6d/(1 − v)³. The lower-bound exponent 3/2 and this exponent 3 bracket the truth.

*Proof.*
1. *No contact before t₁.* Let t₁ = d/(1 − v). By (P0), every candidate has ρ(t) ≥ d − (1 − v)t > 0 for t < t₁. So no candidate is caught before t₁, and Γ(t) is a C¹ closed curve, the image of α ↦ S(α, t), with ρ_min(t) ≥ d − (1 − v)t.
2. *Winding.* The map (α, s) ↦ S(α, s) − H(s) is continuous and non-zero on circle × [0, t]. So the winding number of Γ(t) about H(t) is 1, as it is at s = 0.
3. *Length derivative.* The variational equation gives ∂_t ∂_αS = (v/ρ)(I − r̂r̂ᵀ) ∂_αS (Prop 6(2) of snitch_proved.tex; H' does not appear). Hence ∂_t|∂_αS| = (v/ρ) sin²φ |∂_αS|, where φ is the angle between ∂_αS and r̂. The integrand is continuous on [0, 2π] × [0, t] because ρ ≥ ρ_min > 0. Therefore L(t) = ∫|∂_αS| dα is C¹, with
  L' = v ∫ sin²φ |∂_αS| / ρ dα.
4. *Bearing variation.* Let β be a continuous lift of arg(S − H) in α. Then ρ|∂_αβ| = |sin φ| |∂_αS|. By step 2, ∫ |sin φ| |∂_αS| / ρ dα = ∫ |∂_αβ| dα ≥ 2π.
5. *Cauchy–Schwarz.* Using also ∫ |∂_αS| / ρ dα ≤ L/ρ_min,
  4π² ≤ (∫ sin²φ |∂_αS|/ρ)(∫ |∂_αS|/ρ) ≤ (L'/v)(L/ρ_min).
  So (L²)' ≥ 8π² v ρ_min(t) ≥ 8π² v (d − (1 − v)t) on [0, t₁).
6. *Integrate.* From L(0) = 2πd, for t < t₁,
  L(t)² ≥ 4π²d² + 8π²v (dt − (1 − v)t²/2),
  which tends to 4π²d²(1 + v/(1 − v)) = 4π²d²/(1 − v) as t ↑ t₁.
7. *Conclude.* By E3(c) and ρ_min(t) ≥ d − (1 − v)t, for every t < t₁,
  T ≥ t + (d − (1 − v)t + L(t))/(1 − v) = d/(1 − v) + L(t)/(1 − v).
  Let t ↑ t₁. ∎

**Remarks.**
- Only pre-contact stretching is used. Any lower bound on stretching after contact would add to this.
- The ε > 0 analogue is not claimed. E2 and E3 have ε > 0 versions with an additive error 2ε (see E3'), but step 7 needs a covering argument at scale ε that I have not done.

### E3' (ε > 0 version of the separation). PROVED.
Let τ(P) be the first time with ρ_P ≤ ε. Then |P − Q| ≤ (1 − v)|τ(P) − τ(Q)| + 2ε.

*Proof.* Say τ(P) ≤ τ(Q). By E1, |P − Q| ≤ |S_P(τ(P)) − S_Q(τ(P))| ≤ ε + ρ_Q(τ(P)) ≤ ε + ε + (1 − v)(τ(Q) − τ(P)). ∎

**Corollary (ε > 0 lower bound).** Every δ > 0 with D := (1 − v)δ + 2ε < d gives

  T ≥ (d − ε)/(1 − v) + δ(π / arcsin(D/(2d)) − 1).

*Proof.*
1. *Start.* Every sighting time is ≥ t_ε := (d − ε)/(1 − v).
2. *Cover in time.* Cover [t_ε, T] by k ≤ (T − t_ε)/δ + 1 intervals of length δ.
3. *Each interval sees little.* By E3', the directions seen during one interval form a set of diameter ≤ D on the circle. Since D < d, such a set lies in an arc of angle 2 arcsin(D/(2d)).
4. *Count.* The arcs must cover 2π, so k · 2 arcsin(D/(2d)) ≥ 2π. ∎

As ε → 0 and then δ → 0, this recovers (1 + 2π)d/(1 − v).

### Proposition E7 (a log spiral from its centre catches at most one direction). PROVED.
Let a > 0 and b ∈ ℝ with a² + b² = 1, and put

  H(t) = (a t)^{1 + i b/a}  (complex notation), H(0) = 0.

This is the unit-speed log spiral emanating from 0: |H'| = |a + ib| = 1. Then at most one point of the whole plane is caught at any given time. The set of all initial points that are ever caught lies on a single log spiral {μ_c P₁ : c ∈ ℝ}, where μ_c = e^{(a+ib)c}. In particular **at most one direction on the circle |P| = d is ever caught.**

*Proof.*
1. *Equivariance.* Put λ = |μ_c| = e^{ac}. Then H(λt) = μ_c H(t). The Snitch equation is invariant under rotation and under scaling space and time by the same factor. So if S is a trajectory, then S̃(t) := μ_c S(t/λ) is a trajectory. If S is caught at τ, then S̃ is caught at λτ, and S̃(0) = μ_c S(0).
2. *Uniqueness per time.* Let P₁ be caught at τ₁ and P₂ at τ₂, and choose c with λτ₁ = τ₂. Then μ_c P₁ is caught at τ₂. By E2 only one point is caught at τ₂, so P₂ = μ_c P₁.
3. *Meeting the circle.* |μ_c P₁| = e^{ac}|P₁| is strictly monotone in c, so the spiral {μ_c P₁} meets |P| = d at most once. ∎

This sharpens the brief's "countably many" for spirals started from their centre.

**Autonomous-frame version.** In z = S/H with logarithmic time, the dynamics are autonomous. The set of z that eventually reach z = 1 is exactly one orbit, because by E2 at most one point is caught per time, and by autonomy the point caught at τ₁ + s is the time-shift of the one caught at τ₁. So:
- *No homoclinic loop helps.* A homoclinic loop or invariant curve through z = 1 consists of points that never reach z = 1, except the single stable orbit.
- *Orbits leaving z = 1* correspond to candidates that were at Harry's position earlier, so they were already caught.

**Remark (shape Γ, then spiral). Assessment, not a theorem.**
- For *any* final phase [t_s, T] of *any* strategy, the uncaught candidates at time t_s must lie on the catch curve c_{t_s}([t_s, T]) of Thm E3.
- That curve is determined by the future path alone, because the reversed hound released at τ depends only on H on [t_s, τ].
- For a self-similar final phase this curve is one fixed orbit (rescaled). So "shape Γ, then spiral" means: drive the remaining wavefront *exactly* onto a prescribed curve.
- The original problem is the special case "drive it onto the empty set", and nothing about the spiral makes the shaping easier. I found no mechanism by which a self-similar phase attracts Γ onto its stable orbit. By E1, z-distances contract at rate at most a (the scaling rate). For ε > 0 that exactly matches the shrinking of the vision disc in z, so self-similar funnelling is at best marginal (heuristic).

### Lemma E8 (crossing lemma). PROVED.
Suppose Harry runs straight for time τ, and a candidate has ρ = ρ₀ at the start and is not caught during the run. Then, whatever its bearing,

  ρ(τ) ≥ (1 + v)τ − (1 + v)ρ₀/(1 − v).

*Proof.* By Prop 1, h = ρ(cos β + v) satisfies h(τ) = h(0) − (1 − v²)τ for every bearing, including 0 and π. Also h(0) ≤ (1 + v)ρ₀. Since cos β + v ≥ −(1 − v), we have h ≥ −(1 − v)ρ, so

  ρ(τ) ≥ −h(τ)/(1 − v) ≥ ((1 − v²)τ − (1 + v)ρ₀)/(1 − v). ∎

**Corollary E8' (cost of an excursion).** Suppose Harry is within g of an uncaught candidate Q at time t, and then runs straight for time τ (for example, to catch a far candidate), **without catching Q during that run**. Then, whatever the path afterwards,

  τ(Q) ≥ t + 2τ/(1 − v) − (1 + v)g/(1 − v)².

*Proof.* Combine E8 with (P0). ∎

So a straight excursion of length τ that leaves a neighbour behind costs at least 2τ/(1 − v) before that neighbour can be caught. A candidate left behind recedes as if it were directly behind Harry, at rate (1 + v). Compounding gives the factor (1 + v)/(1 − v) per crossing that the numerics show (section 4). I have not turned that into a theorem for the alternating order, because it needs control of the neighbour gaps g, which also grow (by E1).

**Consequences for task item 3 (non-contiguous orders, leaving and re-entering Γ).**
- *Bisection orders.* By E3, a strategy that catches all directions by time T catches them along a catch curve of length ≤ (1 − v)T − d. For the dyadic bisection order on N = 2^k directions, the polyline of initial positions in catch order has length ≥ Σ_{j=1}^{k−1} (2^j − 1)·2d sin(π/2^j). Each term is ≥ 2d and tends to 2πd, because within dyadic level j + 1 the 2^j new points are visited in increasing angle. So by E2 the chase time is ≥ (d + Σ_j (2^j − 1)·2d sin(π/2^j))/(1 − v) ≥ (d + 2d(k − 1))/(1 − v) → ∞. **Bisection orders admit no N-uniform time bound, so Lemma 4 (compactness) can never be applied to them.** (PROVED.)
- *Leaving and re-entering Γ.* Time spent off Γ catches nothing. Skipping ahead along Γ by a chord χ costs ≥ χ/(1 − v) (E2), which is as much as catching the skipped arc at perfect efficiency. The skipped arc must then be caught later, at extra cost ≥ χ/(1 − v) again, plus the E8' penalty if the legs are straight. So re-entering helps only if the stretch where Harry rejoins is much smaller than where he left. I found no mechanism that guarantees this.

