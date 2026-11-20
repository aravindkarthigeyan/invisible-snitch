# Referee report RG: claims G1–G6 (`referee/G-claims.md`)

Referee: independent adversarial referee (RG). I read `BRIEF.md` §1–2, `paper/main.tex`, `referee/G-claims.md`,
and `referee/E-claims.md` (only to check the exact wording of E3', which G2' cites). I did **not** read
`reports/G-1.md` or `code/G/`. Formulation unchanged: Harry's path is any 1-Lipschitz H with H(0)=0, ε ≥ 0, exact
capture for ε = 0. E1, E2/E3, E3c, E5 and E3' are treated as given. I flag every place where G uses them.

Scripts are in `code/referee/RG/` and run with `python <script>` from that folder (Python 3.12, numpy/scipy). Outputs
are in the `*.out` files next to them.

## Verdicts

| Claim | Verdict | One line |
|---|---|---|
| G1 (hull perimeter ≥ 2πd + 2vt before contact) | **OK** | Every step checks. The Danskin/Lipschitz regularity is handled correctly. Numerics: no violation, large margin. |
| G2 (ε = 0: T ≥ (1+2π)d/ν + 2vd/ν²) | **OK** | Correct deduction from G1 and E3c (used only in the weaker form T ≥ t + L/ν). All numbers reproduce. |
| G2' (ε > 0 bound) | **OK** | The covering argument at scale ε is correct and uses E3' exactly as E states it. The asymptotic claim with λ = dν^{-1/2} is right (slow convergence, see below). |
| G3 (measure-form catch rate) | **OK** | Correct. It uses E1 and P0 only in the stated form. It also reproves E3c, so G2 does not depend on E3c. |
| G4 (accounting inequality) | **OK** (the "Reading" overstates) | The inequality is proved. The "iff" in the Reading is only proved in the "only if" direction. |
| G5 (hull lemma after contact; needle condition) | **OK after two small fixes** | The main inequality is correct and numerically tight (equality occurs). **ERROR (harmless):** "P is 1-Lipschitz" is false; P is 2π-Lipschitz. **GAP (notational):** the width argument in (ii) uses D for both sup ρ and diam K. Fixes are below. |
| G6 (needle-time measure ≥ P(t₁)/(2ν)) | **OK** | Correct given G5. Only Lipschitz continuity of P is needed, not the false 1-Lipschitz constant. |

Nothing in G uses E1, E2/E3, E3c, E3' or E5 in a stronger form than stated.

---

## G1

**Step 1 (Harry inside K).** Correct. For s ≤ t < t\*, the map (α,s) ↦ S_α(s) − H(s) is continuous on circle × [0,t]
and nonzero. Continuity holds because the field is continuous in t and smooth in S away from H, and ρ is bounded below
on that compact set. So the degree of α ↦ r̂_α(t) is constant, equal to 1. A loop lying in an open half-plane that
misses p has winding number 0 about p, so H(t) ∈ K(t). In fact H(t) ∈ int K(t): a loop in a closed half-plane minus a
boundary point p also has winding number 0 about p. Hence ρ_α ≤ diam K.

**Step 2 (Danskin).** Correct. ∂_t S_α = v r̂_α is jointly continuous on circle × [0,t\*) and the circle is compact, so
the right derivative of g(θ,·) exists **everywhere** and equals the max over maximisers.

**Steps 3–4 (regularity).** Correct, and the a.e. issue is handled properly. The difference quotients of g(θ,·) are
bounded by v, so by dominated convergence D⁺(Per K)(t) = ∫ D⁺g dθ ≥ (v/D)∫f dθ = v Per/D at **every** t < t\*. Per K is
Lipschitz, hence absolutely continuous, and its a.e. derivative equals D⁺Per. So integration is legitimate.
∫H·e_θ dθ = 0, and D ≤ Per/2 holds for compact convex sets. Per K(0) = 2πd.

**Step 5.** A closed curve is at least as long as the perimeter of its convex hull. Γ(t) is an injective closed C¹ curve.

**Numerics** (`t1_G1.py`, N = 5000 candidates; the N = 2000 run is the convergence check). Paths tested at v = 0.3,
0.5, 0.8, 0.9, 0.95: stationary, straight, half speed, circles of radius 0.25/1/4, 60° zigzags (period 0.05 and 0.5),
back-and-forth (period 0.2), outward spiral, "turn late", three random piecewise-straight paths, and a random smooth
path. RK4 is used with steps aligned to the path knots and sub-stepping when ρ is small. A run stops at t_max = 1.5/ν,
or at ρ_min < 10⁻², or as soon as the sampled curve stops winding once around H. That last case happens on the
circle R = 4 and "turn late" paths: first contact occurs between samples, and G1 no longer applies.

Results (N = 5000; the N = 2000 run is the convergence check):
- No violation of Per ≥ Per_N(0) + 2vt. The sampled inscribed hull underestimates the true one, so this check is
  conservative.
- The smallest average rate min_t (Per(t) − 2π)/(vt) was **4.75** at both N, against the 2 that G1 claims.
- The smallest instantaneous rate R = Per'/v was 4.01 at N = 5000 and 3.81 at N = 2000. The minimum occurs just
  before contact on the circle R = 4 path, where the sampling is coarse, so this number is resolution-sensitive.
- R/(Per/D) ≥ 1 at every sample.
- The winding number was 1 at every sample used.

Caveat from a first version of the script, which I fixed: if contact is not detected, the sampled curve passes behind
Harry. Then "R < Per/D" (down to a ratio of 0.87) and winding ≠ 1 appear. That is post-contact, where G1 claims
nothing. It is not a counterexample.

**Spot check of the straight-run numbers** (`t4_bounds.py`, exact map, 1.2·10⁵ points log-spaced near α = 0):
L(d/ν) = 7.6817, 11.7249, 50.6784, 443.058 at v = 0.2, 0.5, 0.9, 0.99. These match the reported 7.68, 11.72, 50.68,
443.06. The hull perimeter equals L to all digits shown, so the straight-run wavefront at first contact is convex.

**Is 2v sharp? (not a defect, a remark).** The proof bounds R ≥ Per/D ≥ 2. As pure convex geometry this is
asymptotically sharp, even with H interior. Write f for the support function of K − H and ψ = arctan((ln f)'). Then
R = ∫cos ψ dθ, convexity is equivalent to ψ' ≥ −1 (upward jumps allowed), and closure is equivalent to ∫tan ψ = 0.
Taking ψ ≈ π/2 − δ, then one unit-slope descent, then ψ ≈ −π/2 + δ gives R → 2. In `t5_rate_inf.py`, built
log-spiral bodies give R = 4.10, 3.38, 3.02, 2.66 for δ = 0.6, 0.4, 0.3, 0.2, with aspect ratio up to 6·10³.
So proving a rate of 4v would need dynamics, not convex geometry. Numerically the simulated wavefronts had R ≳ 4:
the minimum was 4.01 at N = 5000 and 3.81 at N = 2000, both near contact, so this is weak evidence. The time-averaged
rate was always ≥ 4.75. **CONJECTURE (tentative):** before contact Per(t) ≥ 2πd + 4vt. That would turn G2 into
T ≥ (1+2π)d/ν + 4vd/ν². This is consistent with the straight run: 2π + 4vt₀ = 402.3 ≤ 443.1 at v = 0.99.

## G2

The deduction is correct. For t < d/ν ≤ t₁ we have U(t) = everything, so L(t) = length Γ(t) ≥ 2πd + 2vt by G1.
E3c is used only as T ≥ t + L(t)/ν, which is weaker than the stated T − t ≥ (ρ_min + L)/ν. G3a with J = (t,T]
reproves exactly this form independently. The right-hand side increases in t; let t ↑ d/ν.
Numbers reproduced (`t4_bounds.py`): 18.6, 39.8, 76.4, 252.8, 905.7, 20528.3, and E5: 19.8, 41.6, 75.2, 208.7, 582.0,
6383.2. The claim that the new bound wins for v ≥ 0.8 is correct. Consistency checks: the bound lies below every
simulated capture time in the paper table, and below the conditional Theorem-B time (v = 0.2: 9.7 vs 22.4).

## G2'

I checked each step, including the scale-ε covering.

- **Step 1.** t_s ≥ (d−ε)/ν by P0. For t < t_s every ρ > ε > 0, so G1 applies with t\* = t_s. No candidate has been
  seen before t.
- **Step 2.** The "E3'" used is exactly E's E3': |P−Q| ≤ ν|σ_P − σ_Q| + 2ε. Restarting at time t is legitimate,
  because both candidates are uncaught (ρ ≥ ε) on [t, σ_P], so E1 applies. ρ_Q(σ_Q) = ε needs d > ε. Hence
  diam A_i ≤ νδ + 2ε. This is the additive-2ε form, not a stronger one.
- **Step 3.** Consecutive nonempty classes give ℓ ≤ 2ε(k'−1) + ν(s_last − s_first) ≤ 2ε(k−1) + ν(T−t).
- **Step 4.** Γ(t) ⊂ c + B̄(D_δ), so K(t) ⊂ conv(c) + B̄(D_δ). Perimeter is monotone on convex sets, and Steiner gives
  +2πD_δ. Per conv(c) = ∫₀^π width ≤ ∫₀^π TV(c·e_θ) = 2ℓ. The k' = 1 case is trivial.
  Numerically, Per(conv c + B_r) ≤ 2ℓ + 2πr on 3000 random polylines (max excess −2.6·10⁻⁷).
- **Step 5.** The algebra is correct: k − 1 < (T−t)/δ, and λ = νδ ranges over (0,∞). The bound increases in t.
  If the bracket is negative the statement is still true, because T ≥ (d−ε)/ν.

**Asymptotics.** With λ = dν^{-1/2}, 2ε/λ = O(√ν) and πλ/(v(d−ε)/ν) = O(√ν), so T ≥ (1 − O(√ν)) v(d−ε)/ν². Correct,
but the constant is large. The ratio of the bound to v(d−ε)/ν² is 0.67, 0.89, 0.96 at v = 0.99, 0.999, 0.9999
(ε = 0.1). With the optimal λ it is 0.88, 0.95, 0.98. (Note for readers: λ = dν^{+1/2} would be wrong, since the
ratio → 0.) Against the paper's ε-sweep table, G2' is far below every simulated time; for example, 10.5 vs 214 at
v = 0.7, ε = 0.1. It is consistent but weak at moderate v.

## G3

- **Step 1.** U(t) is open by the paper's compactness Claim (Lemma limit, with H_N = H). τ is lower semicontinuous,
  hence Borel. F_t is C¹ on U(t): the field and its S-derivative are continuous in (t,S) where ρ > 0. F_t is injective
  by E1 (or by backward uniqueness).
- **Step 2.** E1 on [t, s] for s < τ(α), then s ↑ τ(α), gives |F_t(α) − F_t(α')| ≤ ρ_α'(τ(α)) ≤ ν(τ(α') − τ(α)).
  This is E2 in the given form. Equal catch times force F_t(α) = F_t(α'), so τ is injective on B. (Corollary: two
  candidates uncaught at a common time are never caught simultaneously.)
- **Step 3.** A ν-Lipschitz map on a subset of ℝ multiplies H¹ (outer measure) by at most ν, and H¹(τ(B)) ≤ |J|.
  No measurability of τ(B) is needed.
- **Step 4.** The area formula for an injective C¹ map on a countable union of compact arcs of U(t) is correct.
- **Step 5.** The dyadic left endpoints are non-decreasing in n and converge to τ(α) from below. |∂_αS| is
  non-decreasing (V), and ∂_αS is C¹ in t with |∂_αS| ≥ d > 0. So monotone convergence applies; the integrands are
  measurable step-function compositions. Then a → 0, b → ∞.
- **Step 6.** τ ∈ [d/ν, T].

Remark (not a defect): along a straight leg aimed at a target whose wavefront tangent is transversal, |∂_αS| grows like
ρ^{−v/ν}, so m = ∞ there. G3b therefore implies that, a.e. on the circle, catches must be "tangential". The discrete
chase is a finite set, so it gives no numerical test of G3.

## G4

The proof is correct. By (V), for α ∈ U(t), |∂_αS(α,t)| = |∂_αS(α,s)| + ∫_s^t (v/ρ)sin²φ|∂_αS|, and Tonelli applies.
G3a at time s with J = (s,t] bounds the part caught in (s,t]. Then E3c (or G3a again) gives the result. Values in
[0,∞] are fine.

**Overstatement in the "Reading":** "A path finishes in finite time iff it stretches the uncaught wavefront by a finite
total amount." Only "finite time ⇒ Str(s,t) ≤ ν(T−s) − L(s)" is proved. The converse is unproved. Fix: write "only if",
or label the converse CONJECTURE.

## G5

**Main inequality: OK.**
- Step 1: f ≥ 0 and P = ∫f.
- Step 2: the Hausdorff-distance argument is correct, including the candidate caught at τ ∈ (t,s]:
  |S_α(t) − H(s)| ≤ v(τ−t) + (s−τ) ≤ s−t. So g(θ,·) is 1-Lipschitz.
- Step 3: the maximising sequence stays uncaught for time > f/(2ν). The lower bound
  (r·e_θ − (1+v)h)/(D + (1+v)h) is positive for small h. This gives the **lower Dini** derivative D₊g ≥ vf/D at
  every t.
- Step 4: D₊g ≥ u·e_θ wherever H is differentiable.
- Step 5: Fatou applies (quotients ≥ −1), or Fubini as written. N(t) is exactly the normal cone at H. The arc integral
  is ≥ −2|u|cos(γ/2). Degenerate cases also work: K a segment with H at an end gives γ = 0 and an arc of length π;
  H in the relative interior gives a null cone.
- The step to ≥ 2v − 2cos(γ/2) ≥ −2ν uses P ≥ 2 diam K ≥ 2D.

**ERROR (harmless): "P is 1-Lipschitz on [0,T]".** Counterexample: Harry stationary. Then P(t) = 2π(d + vt), so
P' = 2πv > 1 for v > 1/(2π) (`t4_bounds.py`: P(1) − P(0) = 3.14 at v = 0.5). Step 2 proves that g(θ,·) is
1-Lipschitz, which gives **P 2π-Lipschitz**. Fix: replace "P is 1-Lipschitz" with "P is Lipschitz (constant 2π)".
Nothing downstream uses the constant: (i) and G6 only need absolute continuity and P' ≥ −2ν.

**GAP (notational) in (ii), width part.** The proof says "K contains a diameter segment [a,b] of length D", but D was
defined as sup_{U(t)} ρ_α, which can be smaller than diam K. Fix: run the quadrilateral argument with D_K := diam K. It
gives P ≥ 2√(D_K² + w²). Combined with P < 2D/v and D ≤ D_K:
w² < D²/v² − D_K² ≤ D²(1/v² − 1). So w/D < √(1−v²)/v as claimed, and also w/D_K < √(1−v²)/v. The rest of (ii) is
correct: the projections lie in [a,b] because |ca|, |cb| ≤ D_K; the quadrilateral is convex because the diagonals
cross inside [a,b]; ellipse minimisation and Jensen do the rest.

**Numerics.**
- `t2_G5_instant.py`, random finite configurations. The proof's steps 3–5 apply verbatim to finite sets of uncaught
  candidates.
  - 2·10⁵ random configurations: 1–8 candidates, Harry inside or outside, needle-like clusters, u aimed at the
    cluster, |u| = 1 or random. The minimum of (P' − bound)/max(1,|P'|) was +3.3·10⁻⁹. The vertex formula for P'
    agrees with finite differences to 1.9·10⁻⁶.
  - In all 48 389 configurations with P' < 0, both cos(γ/2) > v and w/D < √(1−v²)/v held (0 violations).
  - Nelder–Mead minimisation of the normalised slack (600 starts, n ≤ 5, v up to 0.97) reached −4.5·10⁻⁹. That is
    round-off at an equality configuration: equality holds for n = 1 with u = r̂.
  - Separately, a Nelder–Mead search over polygons with H interior found R = 3.24 < 4. This confirms that a rate of 4
    cannot come from convex geometry alone.
- `t3_G5_chase.py`, along exact-map discrete chases (N up to 1024, 12 samples per leg; v = 0.3, 0.5, 0.6, 0.7, 0.8),
  testing the instantaneous P'₊ (vertex formula) against vP/D − 2|u|cos(γ/2). The minimum of P' − bound was
  ≥ −4.4·10⁻¹⁶ (relative ≥ −3·10⁻¹⁶) in every run. Equality occurs: at the last leg, X = {H, S_j} and u = r̂, so
  P' = 2(v−1) = bound. Consequence (i) also holds with equality on the last leg. All P' < 0 samples satisfied
  cos(γ/2) > v and the needle-width bound (0 violations). At non-needle samples, min P' was ≥ 0.27 > 0.
  - For v ≥ 0.7 the chase blows up numerically (T_end up to 10⁶⁶). That is the known instability. Those runs are still
    legitimate finite-candidate paths, and the inequality held to relative 10⁻¹⁶. The negative values of
    (T−t) − P/(2ν) printed there are absolute round-off at that scale.

## G6

Correct given G5:
- At a non-needle time P' ≥ 0, in both branches.
- At a needle time P' ≥ −2ν.
- P(t₁) = −∫P' ≤ 2ν·|needle|.
- P(t₁) ≥ 2πd + 2vt₁ by G1, because P is continuous and K = conv Γ for t < t₁ (H ∈ conv Γ).

Numerically (`t3_G5_chase.py`), the needle-time measure was 15.1–15.5 (v = 0.3) and 36.9–39.4 (v = 0.5), against
P(t₁)/(2ν) = 6.19 and 11.72. P(t₁) = 8.66 and 11.72 are above the G1 values 7.14 and 8.28. About 60% of the chase
time has P' < 0, and those are all needle times.

## Summary of fixes to apply before the main document
1. G5 statement: "P is 1-Lipschitz" → "P is 2π-Lipschitz (g(θ,·) is 1-Lipschitz)".
2. G5 (ii) proof: use D_K = diam K for the diameter segment, then conclude w/D < √(1−v²)/v via D ≤ D_K (two lines).
3. G4 Reading: "iff" → "only if" (the converse is unproved).
4. Optional: state in G1 that the derivative bound holds for the right derivative at every t < t\* (Danskin plus
   dominated convergence), which is cleaner than "a.e.".

## Reproduce
```
cd code/referee/RG
python t1_G1.py 5000      # G1 on 16 paths x 5 speeds  (also: python t1_G1.py 2000)
python t2_G5_instant.py   # G5 on random/adversarial finite configurations; rate-4 question
python t3_G5_chase.py     # G5/G6 along exact discrete chases
python t4_bounds.py       # G2/G2'/E5 numbers, straight-run L, 1-Lipschitz counterexample, covering inequality
python t5_rate_inf.py     # convex bodies with H interior and Per'/v -> 2
```
