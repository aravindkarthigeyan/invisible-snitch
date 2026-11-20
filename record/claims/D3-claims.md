# D3 claims for independent refereeing (round 5, stream D3)

Only PROVED statements, with complete proofs. Notation as in `paper/main.tex`: d = 1, Harry H(t), H(0) = 0, |H'| ≤ 1;
candidate θ starts at e^{iθ} and obeys S' = v (S − H)/|S − H|; r = S − H, ρ = |r|. "Seen" = ρ ≤ ε at some time.
chord(θ, θ') := |e^{iθ} − e^{iθ'}| = 2 sin(dist(θ, θ')/2), dist = angular distance on the circle (∈ [0, π]).
Results used from the paper: Prop. 2.1 (integrals C, h on a straight run), Lemma 2.2 (g, k), Prop. 2.3 (ray),
Prop. 3.3(2) (stretching formula), Lemma A2 (half-plane persistence), Lemma E1 (candidates never approach each other),
Lemma D3 of `paper/sec_D1.tex` (re-checked below for v ≤ 1/2). The arithmetic is in `code/D3/constants.py`.

---------------------------------------------------------------------------------------------------------------------

## Claim 1 (Theorem D3.1). PROVED

**Statement.** Let 0 < ε ≤ 0.1 and

    v ≤ v_W(ε) := 0.115 / (log(1/ε) + 7.5).

Then there is an explicit path of speed exactly 1 along which every candidate is seen, by time T ≤ 22.8.

(For ε ≤ 0.1, v_W(ε) ≤ 0.0118. Examples: v_W(10^{-2}) = 9.50·10^{-3}, v_W(10^{-6}) = 5.40·10^{-3},
v_W(10^{-12}) = 3.27·10^{-3}. Theorem A allows ε/(1+2π); Theorem D1 allows ≈ (ε/log(1/ε))^{1/2} capped at 10^{-4}.)

### 1.1 Parameters and the path (strategy W)

λ = 0.1, κ = 0.29, M = 3, R = 0.85. Put

    δ₁ := (0.3 ε)^{1/(1−v)},   ℓ := λε/v (walk length),   η := κε (skip),   t_ε := (1 − ε/2)/(1 − v).

* **Phase 1.** H(s) = (s, 0) for 0 ≤ s ≤ τ₁ := t_ε. X₁ := H(τ₁), b₁ := δ₁.
* **Window k (k ≥ 1)**, given τ_k, X_k = H(τ_k) and b_k < 2π − δ₁:
  * Γ_k(θ) := S_θ(τ_k) for θ ∈ [b_k, 2π − δ₁] (computable from the path on [0, τ_k]).
  * Connector k: straight unit-speed run from X_k to Γ_k(b_k); its length is c_k.
  * Walk k: unit-speed walk along Γ_k starting at θ = b_k, for arclength ℓ or until θ = 2π − δ₁, whichever comes
    first; the stop parameter is a_{k+1}, the length walked ℓ_k ≤ ℓ, τ_{k+1} := τ_k + c_k + ℓ_k,
    X_{k+1} := Γ_k(a_{k+1}) = H(τ_{k+1}).
  * If a_{k+1} = 2π − δ₁, or b_{k+1} := a_{k+1} + η ≥ 2π − δ₁, the construction stops (Harry then moves in any
    unit-speed way); otherwise go to window k + 1.

Walk k is well defined once Γ_k is C¹ with |∂_θΓ_k| ≥ 1 (proved below): then arclength is a C¹ increasing function of
θ, and θ increases along the walk. The path is continuous at all junctions and has speed exactly 1.

### 1.2 Lemmas

**Lemma W1 (stretch).** Let I be an open interval of directions and t > 0 with ρ_θ > 0 on [0, t] for all θ ∈ I. Then
θ ↦ S_θ(t) is C¹ on I and

    1 ≤ |∂_θ S_θ(t)| ≤ exp( v ∫_0^t ds/ρ_θ(s) ).

*Proof.* F(t, x) = v (x − H(t))/|x − H(t)| is continuous on the open set {x ≠ H(t)} and C¹ in x there with
∂_xF = (v/ρ)(I − r̂r̂ᵀ) continuous; hence solutions are C¹ in the initial point and ∂_θS solves the variational equation
∂_t ∂_θS = (v/ρ)(I − r̂r̂ᵀ)∂_θS. So ∂_t |∂_θS| = (v/ρ) sin²φ |∂_θS| with φ the angle between ∂_θS and r̂
(Prop. 3.3(2)), and |∂_θ e^{iθ}| = 1. Integrate: |∂_θS(t)| = exp(∫ v sin²φ/ρ) ∈ [1, exp(v∫ds/ρ)]. ∎

**Lemma W2 (straight run).** During a straight unit-speed run of Harry, any candidate with ρ > 0 throughout satisfies
|{s : ρ(s) < r}| ≤ 2r/(1 − v) for every r > 0.

*Proof.* With heading u let x := r·u. Then x' = v r̂·u − 1 ≤ −(1 − v), so x is strictly decreasing with slope
≤ −(1 − v); and ρ < r implies |x| < r, a set of times of measure ≤ 2r/(1 − v). ∎

**Lemma W3 (phase 1).** Let 0 < ε ≤ 0.1 and v ≤ 1/2. During Phase 1:
(a) every θ with dist(θ, 0) ≤ δ₁ has ρ_θ(t_ε) ≤ ε (so it is seen); in particular c₁ = ρ_{δ₁}(t_ε) ≤ ε;
(b) for θ ∈ [δ₁, 2π − δ₁] and s ∈ [0, t_ε]: ρ_θ(s) ≥ ρ₁ := min(1, g(δ₁)/g_max), where g_max = max g = g(arccos v);
(c) for θ ∈ (π, 2π) the ordinate y_θ(s) of S_θ(s) is negative and non-increasing on [0, t_ε]; for θ ∈ (0, π) it is
positive and non-decreasing.

*Proof.* (a) is Lemma D3 of sec_D1.tex, whose proof uses (A0) only through v ≤ 1/2 and ε < 1: it uses
α ≤ δ₁ ≤ 0.3ε, α^{1−v} ≤ 0.3ε, 1 − cos α ≤ ε/4, 2^v ≤ √2, √2·0.3 < √3/4, and β_c = arccos((1−v)/2) ∈ (π/3, π/2)
with sin β_c ≥ √3/2, tan(β_c/2) ≤ 1, all valid for v ≤ 1/2; its conclusion is ρ(t_ε) ≤ ε for 0 < α ≤ δ₁ (and ε/2 for α = 0);
α < 0 by reflection.
(b) For θ ∈ (0, π) the bearing stays in (0, π) (Lemma A2), so C = ρ g(β) is constant (Prop. 2.1), equal to g(θ)
(initially ρ = 1, β = θ). Hence ρ ≥ g(θ)/g_max. If θ ∈ [δ₁, arccos v], g(θ) ≥ g(δ₁) since g'/g = (cos β − v)/sin β ≥ 0
there. If θ ∈ [arccos v, π), β ≥ θ ≥ arccos v throughout (β increases), so ρ' = v − cos β ≥ 0 and ρ ≥ 1. θ = π stays on
the backward ray, ρ increasing. θ ∈ (π, 2π − δ₁] by reflection.
(c) y' = v y/ρ on the run (Harry has ordinate 0); y never vanishes for θ ∉ {0, π} (Lemma A2). ∎

**Lemma W4 (chords).** If ρ_θ, ρ_{θ'} > 0 on [0, t], then |S_θ(t) − S_{θ'}(t)| ≥ chord(θ, θ').

*Proof.* Lemma E1. ∎

**Lemma W5 (layer cake).** If ρ ≥ ρ_* > 0 on [0, τ], m(r) := |{s ≤ τ : ρ(s) < r}| ≤ A r + B for ρ_* ≤ r ≤ R, and
τ ≤ T, then ∫_0^τ ds/ρ ≤ A log(R/ρ_*) + B/ρ_* + T/R.

*Proof.* ∫_0^τ ds/ρ = ∫_0^∞ |{1/ρ > y}| dy = ∫_0^∞ m(r) r^{−2} dr; m = 0 on (0, ρ_*), m ≤ Ar + B on [ρ_*, R],
m ≤ T on (R, ∞). ∎

**Elementary inequalities used.** For 0 ≤ x ≤ 1: the set {θ' : chord(θ, θ') < x} is an arc of half-length
2 arcsin(x/2) ≤ (π/3)x, hence of measure ≤ W x with W := 2π/3 (arcsin y ≤ (π/3)y on [0, 1/2], convexity).
2 sin(x/2) ≥ (2/π) x on [0, π]; 2 sin(x/2) ≥ x(1 − x²/24) and sin x ≥ x(1 − x²/6) for x ≥ 0.

### 1.3 The constants

Let ρ_* := min(ρ₁, ρ_w, ρ_c, ρ_l) with

    ρ_w := chord(min(η, 2δ₁)) − (λ + v)ε,   ρ_c := chord(min(ℓ/M + η, π)) − (1 + v)ε,   ρ_l := sin δ₁ − vε,

(chord(x) := 2 sin(x/2)), and

    A := 2/(1−v) + W M (1 + v/λ),   B := W M (λ + v) ε + 3ε + W M v (1 + v) ε/λ,
    T_* := t_ε + 2πM + ε + 2πM v/λ,   J_* := A log(R/ρ_*) + B/ρ_* + T_*/R.

**Conditions.** (C1) v + λ + Mκ ≤ 1; (C2) ρ_* > 0; (C3) v J_* ≤ log M; (C0) R + (1+v)ε ≤ 1, R ≥ ρ_*, v ≤ 1/2.

**Lemma W6.** If 0 < ε ≤ 0.1 and v ≤ v_W(ε), then (C0)–(C3) hold, and T_* ≤ 22.8.

*Proof.* v ≤ 0.115/(log 10 + 7.5) < 0.0118 ≤ v_c := 0.015. Since 7.5 ≥ log(1/0.3),
v log(1/(0.3ε)) ≤ 0.115, so f := (0.3ε)^{v/(1−v)} ≥ exp(−0.115/0.985) ≥ 0.8898, and δ₁ = 0.3εf ∈ [0.2669ε, 0.03];
note δ₁^{1−v} = 0.3ε exactly. Then (all bounds monotone in v, worst case v = v_c; `constants.py`):
* g(δ₁) ≥ δ₁(1 − δ₁²/6)/(δ₁/2 (1 + δ₁²/8))^v ≥ 2^v δ₁^{1−v}(1 − δ₁²/6)(1 + δ₁²/8)^{−v} ≥ 0.3ε(1 − 0.03²/6)
  (using tan y ≤ y(1 + y²/2) for y ≤ 0.1 and 2^v(1+δ₁²/8)^{−v} ≥ 1); g_max = (1−v²)^{1/2}((1+v)/(1−v))^{v/2}
  ≤ g_max(v_c) ≤ 1.0002. So ρ₁ ≥ 0.29995ε/1.00012 ≥ 0.2999ε.
* ρ_w ≥ [min(κ, 0.6f)(1 − 0.06²/24) − λ − v_c] ε = [0.29·0.99985 − 0.115] ε ≥ 0.17495 ε.
* ℓ/M + η ≥ λε/(v_c M), so ρ_c ≥ [min((2/π)λ/(v_c M), 2/ε) − (1 + v_c)] ε ≥ 0.3997 ε.
* ρ_l ≥ [0.3f(1 − 0.03²/6) − v_c] ε ≥ 0.2519 ε.
Hence ρ_* ≥ r_* ε with r_* = 0.17495. (C1): 0.015 + 0.1 + 0.87 = 0.985. (C0): 0.85 + 1.015·0.1 < 1.
With A ≤ A_c = 9.2562, B ≤ b_c ε, b_c = 4.6792, T_* ≤ T_c = 22.7923 (values at v = v_c, ε = 0.1):
J_* ≤ A_c [log(1/ε) + log(R/r_*) + (b_c/r_* + T_c/R)/A_c] = A_c [log(1/ε) + 7.3671...]. So v J_* ≤ log 3 holds if
v ≤ (log 3/A_c)/(log(1/ε) + 7.3671), and log 3/A_c = 0.11869 ≥ 0.115, 7.5 ≥ 7.3671. ∎

### 1.4 Proof of Theorem D3.1

Assume (C0)–(C3) and write M = 3 = e^{μ}, so (C3) reads vJ_* ≤ μ. For k ≥ 1 let (H_k) be:

(H_k) windows 1, …, k − 1 have been performed with c_j ≤ ε, b_k < 2π − δ₁ is defined, and for every
θ ∈ [b_k, 2π − δ₁]: (i) ρ_θ(s) ≥ ρ_* for s ∈ [0, τ_k]; (ii) ∫_0^{τ_k} ds/ρ_θ ≤ J_*.

By Lemma W1 (applied on a slightly larger open interval, where ρ > 0 by continuity and compactness), (H_k) gives:
Γ_k is C¹ with 1 ≤ |∂_θΓ_k| ≤ e^{vJ_*} ≤ M on [b_k, 2π − δ₁], so window k is well defined.

**Base.** (H₁): Lemma W3(b) gives ρ ≥ ρ₁ ≥ ρ_* on [0, t_ε]; Lemma W2 gives m(r) ≤ 2r/(1−v) ≤ A r, so (ii) by Lemma W5.

**Counting facts (valid while (H_j) holds for j ≤ k).** The walked θ-ranges [b_j, a_{j+1}] are disjoint subsets of
[δ₁, 2π − δ₁]; walking time over a set E of θ' is ∫_E |∂Γ_j| ≤ M|E|. A non-final walk has length exactly ℓ, so
a_{j+1} − b_j ≥ ℓ/M and b_{j+1} − b_j ≥ ℓ/M + η. Hence the number of windows is at most 1 + 2πM/ℓ, Σℓ_j ≤ 2πM,
Σ c_j ≤ ε(1 + 2πMv/(λε)), and every τ_j ≤ T_*.

**Step (H_k) ⇒ c_k ≤ ε.** k = 1: Lemma W3(a). k ≥ 2: X_k = S_{a_k}(τ_{k−1}), so
c_k ≤ |S_{b_k}(τ_k) − S_{b_k}(τ_{k−1})| + |S_{b_k}(τ_{k−1}) − S_{a_k}(τ_{k−1})| ≤ v(c_{k−1} + ℓ) + Mη
≤ (v + λ + Mκ) ε ≤ ε by (C1); the second term is an arc of Γ_{k−1} over [a_k, b_k] ⊂ [b_{k−1}, 2π − δ₁]
(and S_{b_k} is defined on [τ_{k−1}, τ_k] by (H_k)(i)).

**Step (H_k) ⇒ (H_{k+1})** (when window k + 1 exists). Fix θ ∈ [b_{k+1}, 2π − δ₁] ⊂ [b_k, 2π − δ₁]. On [0, τ_k],
(i) is (H_k)(i). On [τ_k, τ_{k+1}], as long as ρ_θ > 0 (a continuity argument then shows it stays ≥ ρ_* > 0 up to τ_{k+1}):

* *Connector k*, s ∈ [τ_k, τ_k + c_k]: |H(s) − Γ_k(b_k)| ≤ c_k and |S_θ(s) − S_θ(τ_k)| ≤ v c_k, so by Lemma W4
  at τ_k (both θ, b_k satisfy (H_k)(i)): ρ_θ(s) ≥ chord(θ, b_k) − (1+v)c_k. Here θ − b_k ≥ ℓ/M + η. If k ≥ 2 also
  2π − (θ − b_k) ≥ 2δ₁ + ℓ/M + η, so dist(θ, b_k) ≥ min(ℓ/M + η, π) and ρ_θ ≥ ρ_c. If k = 1 and
  dist(θ, b₁) < min(ℓ/M + η, π), then dist = 2π − θ + δ₁, so θ ∈ (π + δ₁, 2π − δ₁]; the connector-1 segment has
  ordinate ≥ 0 (its end S_{δ₁}(t_ε) has positive ordinate, Lemma W3(c)), and y_θ(t_ε) ≤ sin θ ≤ −sin δ₁, so
  ρ_θ(s) ≥ −y_θ(s) ≥ sin δ₁ − v c₁ ≥ ρ_l.
* *Walk k*, s ∈ [τ_k + c_k, τ_{k+1}]: H(s) = S_{θ'}(τ_k) with θ' ∈ [b_k, a_{k+1}], and s − τ_k ≤ c_k + ℓ, so
  ρ_θ(s) ≥ chord(θ, θ') − v(c_k + ℓ) ≥ chord(θ, θ') − (λ + v)ε. Here θ − θ' ≥ η and 2π − (θ − θ') ≥ 2δ₁, so
  ρ_θ(s) ≥ ρ_w.

So (i) holds on [0, τ_{k+1}]. For (ii) bound m(r) := |{s ≤ τ_{k+1} : ρ_θ(s) < r}| for ρ_* ≤ r ≤ R, by the same
estimates applied to every earlier window j ≤ k (each uses Lemma W4 at τ_j, legitimate by (H_j)(i)):
* Phase 1: ≤ 2r/(1−v) (Lemma W2).
* Walks: ρ_θ(s) < r forces chord(θ, θ'(s)) < r + (λ+v)ε ≤ 1, so θ'(s) lies in an arc of measure ≤ W(r + (λ+v)ε);
  each θ' is walked at most once, at speed |∂Γ_j| ≤ M: total ≤ W M (r + (λ+v)ε).
* Connectors j ≥ 2: contribute only if chord(θ, b_j) < r + (1+v)ε ≤ 1, i.e. b_j in an arc of measure
  ≤ W(r + (1+v)ε) (meeting [δ₁, 2π − δ₁] in at most two intervals); the b_j are ℓ/M apart, so at most
  2 + W(r + (1+v)ε)M/ℓ of them, each of duration ≤ ε. Connector 1: duration ≤ ε.
Total: m(r) ≤ A r + B with A, B as in 1.3 (use ε M/ℓ = Mv/λ). Also m(r) = 0 for r < ρ_*, and τ_{k+1} ≤ T_*. Lemma W5
gives (ii). This proves (H_{k+1}).

**Everything is seen.** dist(θ, 0) ≤ δ₁: Lemma W3(a). θ ∈ [b_k, a_{k+1}] (walked in window k): Harry is at
Γ_k(θ) = S_θ(τ_k) at a time s_θ ∈ [τ_k, τ_{k+1}]; if θ were unseen up to s_θ then ρ_θ > 0 there and
ρ_θ(s_θ) = |S_θ(s_θ) − S_θ(τ_k)| ≤ v(c_k + ℓ) ≤ (v + λ)ε ≤ ε, a contradiction. θ ∈ [a_{k+1}, b_{k+1}] (skipped):
at τ_{k+1}, H = S_{a_{k+1}}(τ_k), so if unseen, ρ_θ(τ_{k+1}) ≤ v(c_k + ℓ) + M(θ − a_{k+1}) ≤ (v + λ + Mκ)ε ≤ ε,
a contradiction (θ ∈ [b_k, 2π − δ₁], so |∂Γ_k| ≤ M on [a_{k+1}, θ]). These sets cover the circle; the number of windows
is finite, and the last one ends by T_* ≤ 22.8. ∎

---------------------------------------------------------------------------------------------------------------------

## Claim 2 (ordered phase of the ε-chase). PROVED (a)–(c); (d) is a conditional theorem, PROVED as a reduction

**Chase LG0.** Harry runs along +x up to t₀ = 1/(1−v) (catching candidate 0 exactly). Then repeatedly: U(t) := set of
directions in (0, 2π) unseen up to t (open, Prop. D6(a)); target α* := inf U, end α_e := sup U; run straight at
S_{α*} until ρ_{α*} = ε/2; repeat while U ≠ ∅. Remaining arc 𝒜(t) := {S_α(t) : α ∈ [α*(t), α_e(t)]};
bearings β(α, t) ∈ (−π, π] measured from the current heading (β(α*) = 0).

**(O) at time t:** β(·, t) is strictly increasing on [α*(t), α_e(t)] with values in [0, π].

(a) (O) holds at t₀.
(b) On one leg, for two candidates P, Q with bearings in (0, π) on the whole leg, k(β_P(s)) − k(β_Q(s)) is affine in
the leg time s. Hence if (O) holds at the start of a leg, and the bearing order of every pair of arc points is
(weakly) correct at the end of the leg, then (O) holds at every interior time of the leg.
(c) If (O) holds at the end time of a leg (as a limit) and U ≠ ∅, it holds at the start of the next leg.
(d) Suppose (O) holds at every t ≥ t₀ of LG0 and v(1 + π) < 1. Then every candidate is seen by
T ≤ t₀ + 2π/((1 − v)(1 − v(1 + π))).

*Proof.* (a) At t₀ the bearings θ(α) of S_α(t₀) from the initial heading are strictly increasing on (0, 2π) with values
in (θ*, 2π − θ*), cos θ* = −v (Lemma A1, whose proof is for one direction at a time and applies to every α ∈ (0, 2π)).
From the new heading (towards S_{α*}) the bearings are θ(α) − θ(α*) ∈ [0, 2π − 2θ*) ⊂ [0, π), strictly increasing.
(b) The affine formula is Lemma A4 (Prop. 2.1: C constant, h decreasing at rate 1 − v²). Bearings in (0, π) stay in
(0, π), the forward and backward rays are invariant (Lemma A2). An affine function that is > 0 at s = 0 and ≥ 0 at the
end is > 0 in between; k is strictly decreasing. A point at bearing 0 at the start other than the target is excluded by
strictness; a point at bearing π at the start stays at π and every other point stays below π.
(c) At the switch the new target α** > α* has old bearing b ∈ [0, π]; new bearings are old ones minus b, strictly
increasing on [α**, α_e] ⊂ [α*, α_e] with values in [0, π − b].
(d) Under (O) the only arc point at bearing 0 is the target, so no arc point is caught (Prop. 2.3), ρ is continuous and
positive on the compact set {(α, s): α ∈ [α*, α_e(t₁)], s ∈ [t₁, t₂]} for any interval [t₁, t₂] inside a leg, hence
bounded below; by Lemma W1-type smoothness L_I(t) := ∫_I |∂_αS(α, t)| dα is C¹ on [t₁, t₂] for I = [α*, α_e(t₂)], with
L_I' = v ∫_I sin²φ ρ^{−1}|∂_αS| dα ≤ v ∫_I |∂_αβ| dα = v(β(α_e(t₂)) − 0) ≤ vπ, using sin²φ|∂_αS|/ρ ≤ |∂_αβ| (Prop.
3.3(2)) and (O) at time t on I ⊂ [α*, α_e(t)] (α_e is non-increasing). Since Λ(t₂) = L_I(t₂) and L_I(t₁) ≤ Λ(t₁),
Λ(t₂) − Λ(t₁) ≤ vπ(t₂ − t₁). With ρ_{α*}' = −(1−v), Ψ := ρ_{α*} + Λ satisfies Ψ(t₂) − Ψ(t₁) ≤ −(1 − v(1+π))(t₂ − t₁)
inside legs, and Ψ does not increase at switches (Prop. D6(b): Ψ_old = ε/2 + |arc(α*, α**)| + Λ_new ≥ ρ_{α**} + Λ_new).
Every leg lasts at least ε/(2(1−v)) (Prop. D6(a)), so there are finitely many legs before any finite time, and Ψ ≥ ε/2
while legs run. Finally Ψ(t₀) ≤ lim_{t↑t₀} L(t) ≤ 2π/(1−v) (Prop. 3.3(2); the arc from S_0 to S_{α*} bounds ρ_{α*}). ∎

