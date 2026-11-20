## Notation
r = S − H, ρ = |r|, r̂ = r/ρ, r̂⊥ = r̂ rotated by +90°, u = H' (|u| ≤ 1), J = ∂_α S (H does not depend on α,
so ∂_α r = J). φ = angle between J and r̂. γ = polar angle of r (absolute bearing). κ := v/(1−v).
J_r := J·r̂ (radial part), J_t := J·r̂⊥ (transverse part).

## 1. Tangent-vector dynamics (all PROVED, elementary)

**Lemma C0 (PROVED; already in snitch_proved.tex Prop. 6 proof, restated).** For any path with |H'| ≤ 1 and any
candidate with ρ > 0 on the interval: J' = (v/ρ)(I − r̂r̂ᵀ)J, hence d|J|/dt = (v/ρ) sin²φ |J|, and
ρ ∂_α γ = J_t, so d|J|/dt = v |sin φ| |∂_α γ| ≤ v|∂_α γ|. Consequently
  |J(α,t)| ≤ |J(α,s)| + v ∫_s^t |∂_α γ(α,τ)| dτ   and   |J(α,t)| ≤ |J(α,s)| exp(v ∫_s^t dτ/ρ).

**Lemma C3 (PROVED). Componentwise form.** With J_r = J·r̂, J_t = J·r̂⊥, u_⊥ = u·r̂⊥:
  J_r' = −J_t u_⊥/ρ,     J_t' = (v J_t + J_r u_⊥)/ρ.
Proof: r̂' = ((v r̂ − u)·r̂⊥/ρ) r̂⊥ = −(u_⊥/ρ) r̂⊥ and r̂⊥' = (u_⊥/ρ) r̂; J'·r̂ = 0, J'·r̂⊥ = vJ_t/ρ. ∎
So the Snitch's own motion stretches only the transverse part; the radial part J_r changes only through Harry's
transverse velocity, and v does not enter its equation.

**Lemma C1 (PROVED). Exact head-on stretching law.** On a straight run with heading u, let a candidate lie on the
forward ray (β = 0) with ρ(t1) = ρ0. Then r̂ ≡ u, ρ(t) = ρ0 − (1−v)(t − t1), and
  J_r(t) = J_r(t1),   J_t(t) = J_t(t1) (ρ0/ρ(t))^κ,   κ = v/(1−v),
  tan φ(t) = tan φ(t1) (ρ0/ρ)^κ,   |J(t)|² = J_r(t1)² + J_t(t1)² (ρ0/ρ)^{2κ},
  ∫_{t1}^{t} v sin²φ/ρ dτ = ½ ln[cos²φ(t1) + sin²φ(t1)(ρ0/ρ)^{2κ}].
Proof: u_⊥ = 0 in Lemma C3, so J_r' = 0 and J_t' = vJ_t/ρ; with dt = −dρ/(1−v), d ln J_t/d ln ρ = −κ. ∎
On the backward ray (β = π) the same argument gives J_t ∝ ρ^{v/(1+v)}.
*Answer to the brief's question:* the exponent is exactly κ = v/(1−v), not reduced by the angular factor.
sin²φ only delays the onset: d ln|J| / d ln(ρ0/ρ) = κ sin²φ, and sin²φ = tan²φ/(1+tan²φ) → 1 because tan φ itself
grows like (ρ0/ρ)^κ. The only exception is J_t(t1) = 0 exactly (J radial), when |J| is constant.

**Corollary C2 (PROVED). The literal author condition fails at every head-on catch, in particular at t0.**
In the first straight run, α = 0 is on the forward ray with J(0,0) = (0, d) purely transverse, so
|∂_α S(0,t)| = d (d/(d − (1−v)t))^κ → ∞ as t → t0 = d/(1−v). The same holds at every catch of the discrete chase
whose target has J_t ≠ 0 at the start of its leg. Hence "|∂_αS(θ(t),t)| ≤ C(1+t)" is false at t = t0 for every
v ∈ (0,1) (this agrees with stream I's observation). More generally:

**Proposition C4 (PROVED). Finite stretch at the caught point forces radial (tangential-sweep) capture.**
Let |H'| ≤ 1 and let candidate α be caught at t_c (ρ(t) → 0 as t ↑ t_c, ρ > 0 before). If
limsup_{t↑t_c} |J(α,t)| < ∞ then ∫^{t_c} sin²φ(t) dt/(t_c − t) < ∞; in particular liminf_{t↑t_c} |sin φ| = 0.
If instead sin²φ ≥ m > 0 on [s, t_c), then |J(α,t)| ≥ |J(α,s)| ((t_c − s)/(t_c − t))^{κ m} → ∞.
Proof: ρ' = v − u·r̂ ≥ −(1−v) (Prop. 3), so ρ(t) ≤ (1−v)(t_c − t). Then
ln|J(t)| − ln|J(s)| = v∫_s^t sin²φ/ρ ≥ (v/(1−v)) ∫_s^t sin²φ dτ/(t_c − τ). ∎
So any sweep for which the author's quantity is finite must catch each direction with the wavefront tangent
pointing at Harry, i.e. Harry moves along the one-sided tangent of Γ (the author's ε = 0 system).

## 2. What growth of the stretch actually suffices (the author's ODE, done exactly)

The author's ε = 0 system (refs/Epsilon_zero_results.txt, eq. (5); our normalisation) is H(t) = S(θ(t),t),
θ' = (1−v)/|∂_αS(θ(t),t)|. If |∂_αS(θ,t)| ≤ C(1+t) then θ(t) − θ(t0) ≥ ((1−v)/C) ln((1+t)/(1+t0)), so θ reaches 2π by
T ≤ (1+t0) e^{2πC/(1−v)} − 1: **linear growth does give finite time** (exponentially large in C/(1−v)); the divergence
of ∫dt/(1+t) is what makes it work. The sharp version of this implication is Osgood-type, stated here for the
well-defined discrete chase (no regularity assumptions needed):

**Theorem C5 (PROVED). Discrete form of the author's condition.** Discrete chase of snitch_proved.tex §4 on
0 = α_0 < … < α_{N−1} < 2π; t_j = catch time of S_j (t_0 = d/(1−v)); for j ≤ N−2 let ℓ_j = |S_{j+1}(t_j) − H(t_j)|,
Δ_j = α_{j+1} − α_j and Q_j = ℓ_j/Δ_j (the discrete stretch at the caught point).
(i) t_{j+1} − t_j = ℓ_j/(1−v), hence t_{N−1} = t_0 + (1−v)^{−1} Σ_j Q_j Δ_j exactly.
(ii) Let f : [t_0,∞) → (0,∞) be nondecreasing, F(t) = ∫_{t_0}^t ds/f(s), and w_j ≥ 0 with Q_j ≤ f(t_j) w_j for all j.
Then F(t_{N−1}) ≤ (1−v)^{−1} Σ_j w_j Δ_j.
(iii) Hence if, for nested direction sets with dense union, Σ_j w_jΔ_j ≤ M for all N and F(∞) > M/(1−v), every chase
ends by T* = F^{−1}(M/(1−v)), and by Lemma 4 (compactness) there is a path with |H'| ≤ 1 (speed ≤ 1, not exactly 1)
catching every direction exactly (ε = 0) by T*.
Author's case f = C(1+t), w ≡ 1, M = 2π: T* = (1+t_0) e^{2πC/(1−v)} − 1.
Proof. (i) is Lemma 2 of the tex (the chase of S_{j+1} takes |S_{j+1}−H|/(1−v)). (ii) Since f is nondecreasing,
F(t_{j+1}) − F(t_j) = ∫_{t_j}^{t_{j+1}} ds/f(s) ≤ (t_{j+1}−t_j)/f(t_j) = Q_jΔ_j/((1−v)f(t_j)) ≤ w_jΔ_j/(1−v); sum over j.
(iii) F is continuous strictly increasing, so t_{N−1} ≤ T*; apply Lemma 4. ∎

**Remark C5a (sharpness; PROVED for the model recursion).** Among pointwise bounds Q ≤ f(t) (w ≡ 1), the condition
F(∞) > 2π/(1−v) cannot be weakened: the extremal recursion t_{j+1} = t_j + f(t_j)Δ/(1−v) converges as Δ → 0 to
dt/dα = f(t)/(1−v), which reaches t = ∞ at α = (1−v)F(∞). So for f = C(1+t)^p: any p ≤ 1 works for every C
(log factors allowed, e.g. f = C(1+t)ln(e+t)); p > 1 works only if C < (1−v)(1+t_0)^{1−p}/(2π(p−1)).
The author's linear bound is therefore exactly the borderline power, but (i) shows the condition is nothing more
than a local-in-time way of bounding Σ Q_jΔ_j = (1−v)(t_{N−1} − t_0).

**Proposition C5b (PROVED). The unweighted condition (w ≡ 1) is false uniformly in N, for every v.**
By Prop. 4 of the tex (proof), at t_0 a candidate α ∈ (0,π) has C = d g(α) ~ d 2^v α^{1−v} and bearing → θ*, so
ρ(α,t_0) = C/g(β) ≍ α^{1−v} as α → 0. Hence Q_0 = ρ(α_1,t_0)/α_1 ≍ α_1^{−v} → ∞ as the mesh is refined:
sup_j Q_j/(1+t_j) → ∞. So any correct statement must carry an integrable weight, at least w(α) ≳ α^{−v} near α = 0.
(This is the discrete counterpart of Corollary C2 and of stream I's remark; it is harmless because α^{−v} ∈ L¹.)
Starting the clock at some t_1 > t_0 does not repair the pointwise version: see §4 (end-point exponent).
**The right substitute** is therefore (ii)–(iii) with w ∈ L¹: Q(θ) ≤ f(t) w(θ), ∫ 1/f = ∞, w(θ) = θ^{−v} + (2π−θ)^{−p₁}
with p₁ < 1 (numerically p₁ ≈ 2v/(1+v), §4), uniformly in N. Numerically (§4) this holds for v ≤ 0.5 with
f = 0.4(1+t). It is equivalent in strength to a uniform bound on Σ Q_jΔ_j, i.e. on the capture time itself.

## 5. ε > 0: the residence-time ingredient

**Lemma C8 (PROVED). Stretch is controlled by angular crowding.** For any path with |H'| ≤ 1 and any candidate with
ρ > 0 on [s,t] (γ = bearing of S_α from H, u_⊥ = H'·r̂⊥):
  ∂_tγ = −u_⊥/ρ,  ρ ∂_αγ = J_t,  J_r' = −J_t u_⊥/ρ,
  |J_r(t)| ≤ |J_r(s)| + ∫_s^t |∂_αγ| |u_⊥| dτ ≤ |J_r(s)| + ∫_s^t |∂_αγ| dτ,   |J(t)| ≤ |J(s)| + v ∫_s^t |∂_αγ| dτ.
In particular, if |∂_αγ(α,τ)| ≤ K(α) for τ ≤ t then |J(α,t)| ≤ |J(α,0)| + vK(α)t and |J_r(α,t)| ≤ |J_r(α,0)| + K(α)t.
Exact straight-step identities (used in the code): over a straight run, ∫dt/ρ = Δ ln tan(|β|/2) and
∫|u_⊥|/ρ dt = Δ|β| (= the bearing swept); for the head-on target ∫dt/ρ = ln(ρ_0/ρ_1)/(1−v).
Proof: r̂' = −(u_⊥/ρ)r̂⊥ gives ∂_tγ; ∂_α r = J gives ρ∂_αγ = J·r̂⊥; the rest is Lemmas C0, C3 and |u_⊥| ≤ 1.
On a straight run db/dt = sin b/ρ = |u_⊥|/ρ and d ln tan(b/2)/db = 1/sin b. ∎
*Relation to the trawler lead (stream I).* For a static observer (Harry fixed) each direction keeps its bearing,
|∂_αγ| ≡ 1 and C8 gives |J| ≤ d + vt, which is exactly the trawler / author's toy front (|∂_αS| = vt + O(1)). So
"comparison with a trawler front" is the hypothesis K ≡ 1 in C8: Harry never sees the unseen directions more crowded
in bearing than a static observer would. C8 is the precise form of that comparison; it needs no t_1 > t_0 shift but it
does need a weight in α near both ends (K(α) ≳ α^{−v}, (2π−α)^{−2v/(1+v)}), by §2 and §4.

**Proposition C9 (PROVED). Greedy ε-sweep, Osgood form.** Greedy ε-sweep on directions α_0 = 0 < … < α_{N−1}:
step k starts at t_k with target θ_k = first unseen direction; Harry runs straight at it for τ_k = (ρ_k − ε)/(1−v)
(ρ_k = |S_{θ_k}(t_k) − H(t_k)|), after which it is seen; all directions with min distance ≤ ε during the step are
marked seen. Let Q_k = |S_{θ_k}(t_k) − S_{θ_{k−1}}(t_k)|/(θ_k − θ_{k−1}) for k ≥ 1. Then θ_k is strictly increasing,
τ_k ≤ Q_k(θ_k − θ_{k−1})/(1−v), and if Q_k ≤ f(t_k) w_k with f nondecreasing, F = ∫_{t_1} ds/f, then
F(T) ≤ (1−v)^{−1} Σ_k w_k(θ_k − θ_{k−1}), T = end of the sweep, t_1 = (d−ε)/(1−v).
Proof: at t_k the previous target θ_{k−1} is at distance exactly ε from H (the head-on step ends when it reaches ε),
so ρ_k ≤ ε + Q_k(θ_k − θ_{k−1}). The target of step k is seen at its end and all directions below it were seen
before, so θ_{k+1} > θ_k. Then argue as in Theorem C5(ii). ∎
(For a statement about *all* directions with ε > 0 one still needs the Lemma-4-type limit with "seen" in place of
"caught"; I have not written that out, so it is not claimed.)

**What residence bound would close the ε > 0 argument, and how far each version gets.**
(R1) *Total exposure.* E_α(t) := ∫_0^t dτ/ρ_α ≤ b + (c/(1−v)) ln(1 + t/ε) for every α, for all t up to the first
step start t_k with θ_k ≥ α (so that it applies to the arcs [θ_{k−1}, θ_k] used in C9). By Lemma C0,
|J| ≤ d e^{vb}(1+t/ε)^{cκ}; with the chord bounded by ∫|J|dα this gives a finite ε-sweep when cκ ≤ 1 (PROVED as an
implication). c = 1 is one head-on approach at the maximal closing rate from the largest possible distance; then
cκ ≤ 1 ⇔ v ≤ 1/2 — this is the exact content of the brief's "exponent v/(1−v) ≤ 1 iff v ≤ 1/2" heuristic. But
NUMERICALLY (residence.py, greedy, N = 2000/4000, ε = 0.1/0.05/0.025) the per-candidate constants at the moment of
being seen, c_α = (1−v)E_α/ln((1+(1+v)t)/ε), have median 1.02, 0.97, 0.91, 0.88, 0.82 but maximum 2.08, 1.82, 1.55,
1.38, 1.22 for v = 0.2, 0.35, 0.5, 0.6, 0.7; so cκ ≤ 1 holds only up to v ≈ 0.35. (R1) is also hopeless for ε → 0
(bound ∝ ε^{−cκ}). Reason: E counts the stretching of J_t, which the sweep does not need (Lemma C3, §4(1)).
(R2) *Angular density (trawler comparison).* |∂_αγ(α,τ)| ≤ K w(α) for every α and τ ≤ (first t_k with θ_k ≥ α) (w as in §2). By C8,
|J(α,t)| ≤ d + vKw(α)t and |J_r| ≤ d + Kw(α)t: the weighted author condition with f linear, uniformly in ε.
Combined with C5/C9 this would give exact capture (ε = 0, via Lemma 4) / an ε-sweep, for every v for which (R2)
holds along a stable sweep. NUMERICAL test: see the table below. (R2) is a statement about how fast directions can
crowd in bearing near Harry; proving it requires control of the curvature of Γ near Harry, i.e. of the steering
(§3), which is where the real difficulty sits.

