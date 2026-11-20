# Referee report RD3b (second, independent referee of `referee/D3-claims.md`)

Read: `referee/D3-claims.md`, `paper/main.tex` (and its `\input` file `paper/sec_D1.tex`, for Lemma D3 and Prop. D6).
Not read: `reports/referee-RD3a.md`, `reports/D3-1.md`, `code/D3`. Own code: `code/referee/D3b/`
(`constants.py` exact recomputation of Lemma W6; `sim_W.py` direct simulation of strategy W; `sim_LG0.py` test of (O)).

Problem statement as given (H(0)=0, |H'| ≤ 1, path fixed in advance depending on v, d, ε only; S' = v(S−H)/|S−H|;
win iff every α is seen) is used unchanged by both claims. D3.1 even gives speed exactly 1.

## Summary of verdicts

| Claim | Verdict |
|---|---|
| Lemma W1 (stretch) | OK |
| Lemma W2 (straight run) | OK |
| Lemma W3 (a)(b)(c) | OK |
| Lemma W4 (chords) | OK |
| Lemma W5 (layer cake) | OK |
| Elementary inequalities (W = 2π/3 etc.) | OK |
| Lemma W6 (constants) | OK with a wording fix (T_c) |
| Theorem D3.1 (induction, path, covering) | OK (two optional clarifications) |
| D3.2 (a) | OK |
| D3.2 (b) | OK with fix (which arc the end-of-leg hypothesis refers to) |
| D3.2 (c) | OK |
| D3.2 (d) | OK as a conditional reduction (minor clarification of α*(t)); hypothesis (O) numerically true at v = 0.1, numerically violated late in the chase at v = 0.2, 0.24 |

No claim is FALSE; no GAP that affects a conclusion.

## 1. Theorem D3.1

### 1.1 Logical structure (focus 1)

Dependency graph: W3(a) ← Lemma D3 (sec_D1) [re-checked]; W3(b) ← Prop 2.1, Lemma 2.2, Lemma A2; W3(c) ← Lemma A2;
W4 ← Lemma E1; W1 ← variational equation (Prop 3.3(2)); W5 elementary; W6 arithmetic. Theorem: base (H₁) ← W3(b), W2, W5;
(H_k) ⇒ Γ_k C¹ with 1 ≤ |∂Γ_k| ≤ M ← W1 + (C3); (H_k) ⇒ c_k ≤ ε ← W3(a) (k=1), (C1) + induction c_{k−1} ≤ ε;
(H_k) ⇒ (H_{k+1}) ← W2, W4 at each τ_j (j ≤ k, legitimate by (H_j)(i)), W5, counting facts (which use only |∂Γ_j| ≤ M for j ≤ k).
No lemma uses a later one; no cycles.

Bootstrap: the induction is genuinely on windows, with (H_k) a statement about [0, τ_k] only. In the step, the only quantity
on (τ_k, τ_{k+1}] that is needed a priori is that S_θ exists (ρ_θ > 0); the lower bounds used (|S_θ(s) − S_θ(τ_k)| ≤ v(s−τ_k),
Lemma W4 *at time τ_k*, Harry's position on the connector/walk) hold for as long as S_θ exists, and give ρ_θ ≥ ρ_* > 0;
the first-zero time argument then closes. This is correct and non-circular: the Lipschitz bound M for Γ_k is derived from
(H_k)(ii) at τ_k and is never assumed on the interval being controlled. The c_k ≤ ε step uses S_{b_k} on [τ_{k−1}, τ_k],
covered by (H_k)(i) as stated. Counting facts (number of windows ≤ 1 + 2πM/ℓ, Σℓ_j ≤ 2πM, τ_j ≤ T_*) use (H_j) for j ≤ k only.
Termination: each non-final window consumes ≥ ℓ/M + η of θ, so finitely many windows.

### 1.2 Regularity of the front (focus 2) and the path (focus 3)

* Γ_k is **not** "the current front" and not the unseen set: it is the frozen snapshot θ ↦ S_θ(τ_k) on the full parameter
  interval [b_k, 2π−δ₁], seen or not. Nothing is removed, so there is no arc-structure problem. (H_k)(i) gives ρ_θ ≥ ρ_* > 0
  on [0, τ_k] for every θ of the interval, which is exactly what W1 needs; by openness (continuous dependence, as in the Claim of
  Lemma 5.1) this persists on an open neighbourhood, so Γ_k is C¹ on the closed interval.
* Injectivity of Γ_k is not needed and not claimed (it does hold, by backward uniqueness / Lemma E1, but is irrelevant);
  |∂_θΓ_k| ≥ 1 makes arclength a C¹ strictly increasing function of θ, so the unit-speed walk is well defined, C¹, and θ
  increases along it. Rectifiable: length ≤ M·(2π).
* Harry passing through or near the front: Harry walks over *past* positions S_θ'(τ_k); directions θ' being walked, or
  skipped, may later be caught, but they are never used again (all later windows use θ ≥ b_{k+1}). Directions still in use
  have ρ ≥ ρ_* throughout (the step). So no candidate whose trajectory is needed is ever caught.
* Path: depends only on (v, ε) (Γ_k is computed from H on [0, τ_k]); continuous at junctions (connector ends at Γ_k(b_k), walk
  ends at Γ_k(a_{k+1}) = X_{k+1}); piecewise C¹ with speed exactly 1; finite. Fixed in advance, independent of α. OK.

### 1.3 Cited results within hypotheses (focus 4)

* Lemma E1 (W4): any path, ρ_P, ρ_Q > 0 on [0, t] — supplied by (H_k)(i) at each use. OK.
* Stretching formula (W1): needs ρ > 0 on [0, t] for θ in an open interval — supplied as above. The F in W1 is continuous in
  (t, x) because H is continuous; C¹ dependence on initial data holds for such F (Hartman, Thm V.3.1). OK.
* Prop 2.1 / Lemma A2 / Lemma A4 / Prop 2.3: used only on straight runs (Phase 1, connectors in W2/W3), with ρ > 0. OK.
* Lemma D3 (sec_D1) under v ≤ 1/2, ε < 1: re-derived line by line: 1−cos α ≤ α²/2 ≤ 0.045ε² ≤ ε/4 (ε ≤ 1);
  h(t_ε) = (1+v)ε/2 − (1−cos α) ≥ (1+v)ε/4; g(α) ≤ 2^v α^{1−v} ≤ √2·0.3ε < (√3/4)ε; β_c = arccos((1−v)/2) ∈ (π/3, arccos(1/4)]
  ⊂ (π/3, π/2), so sin β_c ≥ √3/2, tan(β_c/2) ≤ 1, g(β_c) ≥ √3/2; hence β(t_ε) ≤ β_c and ρ(t_ε) ≤ ε. Includes α = δ₁, so
  c₁ ≤ ε. OK. (A0) is not otherwise used.
* W2: x' = v r̂·u − 1 ≤ −(1−v); {ρ < r} ⊂ {|x| < r}. OK. W5: ∫ds/ρ = ∫₀^∞ m(r) r^{−2} dr; correct three-piece bound. OK.
* W: half-length of {chord < x} is 2 arcsin(x/2); arcsin y ≤ (π/3)y on [0, 1/2] (arcsin y / y increasing); measure ≤ (2π/3)x. OK.

### 1.4 Step-by-step checks of 1.4 (all OK)

* Connector k ≥ 2: θ − b_k ≥ b_{k+1} − b_k ≥ ℓ/M + η (window k non-final ⇒ walk length exactly ℓ, |∂Γ_k| ≤ M) and
  b_k ≥ δ₁ + ℓ/M + η, θ ≤ 2π − δ₁ give dist(θ, b_k) ≥ ℓ/M + η (the min with π is harmless). ρ ≥ chord − c_k − v c_k. OK.
* Connector 1, lower half: the segment from (t_ε, 0) to S_{δ₁}(t_ε) has ordinate ≥ 0 (W3(c)); y_θ(s) ≤ y_θ(t_ε) + v c₁ ≤
  −sin δ₁ + vε. OK.
* Walk: θ − θ' ∈ [η, 2π − 2δ₁] since θ' ≤ a_{k+1} = b_{k+1} − η and θ' ≥ b_k ≥ δ₁. OK.
* m(r): Phase 1 by W2; walks: the θ'-sets of different windows are disjoint and time = ∫_E |∂Γ_j| ≤ M|E|; connectors j ≥ 2:
  the arc {chord(θ,·) < x} meets [δ₁, 2π−δ₁] in ≤ 2 intervals, points ℓ/M apart, so ≤ 2 + |arc| M/ℓ points; each ≤ ε long.
  Sum = A r + B exactly as defined (εM/ℓ = Mv/λ). Requires r + (1+v)ε ≤ 1 for r ≤ R: (C0). OK.
* c_k ≤ ε (k ≥ 2): v(c_{k−1} + ℓ) + Mη ≤ (v + λ + Mκ)ε. OK.
* Covering: [−δ₁, δ₁] (Phase 1), [b_k, a_{k+1}] (walked: ρ(s_θ) ≤ v(c_k + ℓ) ≤ (v+λ)ε), [a_{k+1}, b_{k+1} ∧ (2π−δ₁)]
  (skipped: ≤ (v+λ+Mκ)ε at τ_{k+1}), consecutive since b₁ = δ₁. If θ is caught earlier it is seen anyway. OK.

### 1.5 Constants (Lemma W6), recomputed (`code/referee/D3b/constants.py`, 30 digits)

f ≥ 0.889806; g_max(0.015) = 1.0001125; ρ₁/ε ≥ 0.299921; ρ_w/ε ≥ 0.1749565; ρ_c/ε ≥ 0.399711; ρ_l/ε ≥ 0.251902;
A_c = 9.256120; b_c = 4.679181; log 3/A_c = 0.1186904; constant in the J-bound 7.36720. All as printed.
v_W(0.1) = 0.011732, v_W(10⁻²) = 9.5001·10⁻³, v_W(10⁻⁶) = 5.3951·10⁻³, v_W(10⁻¹²) = 3.2735·10⁻³. As printed.
Direct evaluation with the exact formulas (no Taylor bounds) at v = v_W(ε) for 400 values ε ∈ [10⁻²¹, 0.1], and at
v = c·v_W(ε) for c ∈ {0.999, 0.9, 0.5, 0.1, 0.01}: (C0)–(C3) and T_* ≤ 22.8 hold everywhere; max vJ_*/log 3 = 0.918 (at ε = 0.1).
So the monotonicity-in-v claim is at least numerically confirmed on the range used.

**Fix (wording only).** "T_* ≤ T_c = 22.7923 (values at v = v_c, ε = 0.1)": the value 22.7923 is
1/(1−v_c) + 2πM + 0.1 + 2πMv_c/λ, i.e. it uses t_ε ≤ 1/(1−v) together with ε ≤ 0.1; the actual value at v = v_c, ε = 0.1
is 22.7415. Replace by: "T_* ≤ T_c := 1/(1−v_c) + 2πM + 0.1 + 2πMv_c/λ = 22.7923 (using t_ε ≤ 1/(1−v) and ε ≤ 0.1)".
The conclusion is unchanged (it is an upper bound).

### 1.6 Direct simulation of strategy W (`sim_W.py`, RK4, grid of directions; evidence only)

| ε | v | windows | end time | max c_k/ε | min_k (min ρ on front)/ε | max v∫ds/ρ | max ∂Γ | unseen |
|---|---|---|---|---|---|---|---|---|
| 0.1 | 0.01173 | 8 | 7.45 | 0.578 | 0.396 | 0.131 | 1.063 | 0 |
| 0.01 | 0.0095 | 60 | 7.46 | 0.584 | 0.397 | 0.180 | 1.073 | 0 |
| 0.001 | 0.00798 | 496 | 7.44 | 0.600 | 0.398 | 0.195 | 1.079 | 0 |

(Grids N = 2·10⁴, 10⁵, 6·10⁴; dt = 0.002, 0.002, 5·10⁻⁴. A first ε = 0.001 run with dt = 0.004 > 2ε reported "unseen"
directions; that was a sampling artefact (sightings checked only at step ends) and disappears at dt = 5·10⁻⁴.
Raw output in `code/referee/D3b/W_eps*.txt`.)

(ρ_*/ε ≈ 0.178, J-budget log 3 = 1.10, M = 3, T bound 22.8: the theorem's margins are large, as expected of a worst-case proof.)

### 1.7 Optional clarifications (not errors)

1. In 1.1 say explicitly that Γ_k is defined on the whole θ-interval, including directions already seen (this is what makes
   the front a C¹ curve with no holes); a reader might otherwise think seen directions are removed.
2. In "Step (H_k) ⇒ (H_{k+1})", the continuity argument could be one sentence: "let σ be the supremum of s ≤ τ_{k+1} with
   S_θ defined and ρ_θ > 0 on [τ_k, s]; the bounds below hold on [τ_k, σ) and give ρ_θ ≥ ρ_* there, so σ = τ_{k+1}."

**Verdict D3.1: OK** (with the T_c wording fix).

## 2. Proposition D3.2

Prop. D6(a) is cited for LG, while LG0 starts with exact capture at t₀; its proof (closedness of the seen set by continuous
dependence; ρ_{α*} ≥ ε at a switch; leg ≥ ε/(2(1−v))) applies verbatim to LG0, including at t₀. Say so.

**(a) OK.** For every α ∈ (0, π), Lemma A1's per-direction argument (h(t₀) < 0 < C, bracket (1+v)(1−cos α) > 0) gives
θ(α) ∈ (θ*, π) strictly increasing; α = π on the backward ray; reflection. Shift by θ(α*) > θ*: values in
[0, 2π − 2θ*) = [0, 2 arccos v) ⊂ [0, π). Correct.

**(b) OK with fix.** The pairwise argument is right: on a leg, every arc point other than the target has bearing in (0, π]
at the start (by (O)), so none is caught (Prop 2.3) and (0, π), {π}, {0} are invariant (Lemma A2); for P < Q with bearings
in (0, π), k(β_P) − k(β_Q) is affine (Lemma A4), > 0 at the start (strictness, k strictly decreasing), ≥ 0 at the end,
hence > 0 strictly inside. I checked the affine formula against Prop 2.1: h/C − (1−v²)s/C. Correct.
The gap is in *which* pairs the end-of-leg hypothesis covers. The arc is [α*, α_e(t)] with α_e(t) = sup U(t)
non-increasing, and it can decrease inside a leg. If "arc points" means points of the arc at the end of the leg, then a pair
(P, Q) with α_e(t_end) < Q ≤ α_e(t) is not covered: nothing prevents its order from being already reversed at an interior
time t at which Q is still in the arc, so the conclusion "(O) at every interior time" does not follow from the hypothesis
as literally stated. (Logical gap in the formulation only; not used by (d), which assumes (O) directly.) Replacement text:

> (b) … Hence if (O) holds at the start t_s of a leg, and β(P, t_e) ≤ β(Q, t_e) for all α* ≤ P < Q ≤ α_e(t_s)
> (pairs of the arc **at the start** of the leg), then (O) holds at every t ∈ (t_s, t_e) on [α*, α_e(t)].

Also state that α*(t) denotes the target of the current leg (constant on a leg), not inf U(t), which increases inside the
leg once the target is seen. (With inf U(t) the statement of (O) is still true but (d)'s formula ρ'_{α*} = −(1−v) is not.)
Note: (b) is a *criterion*, not a proof of order; by itself it gives nothing about the end of a leg, and the end-of-leg
hypothesis is weak, whereas (c) needs strict order at the end. Since (d) assumes (O) at all times, this is consistent; but
the chain (a) → (b) → (c) proves (O) only if strict order at every leg end is verified separately.

**(c) OK.** At a switch positions are continuous; with strict (O) at t_e (old heading), α** > α* has old bearing
b ∈ (0, π]; the new heading is the direction to S_{α**}, so new bearings are β_old − b ∈ [0, π − b], strictly increasing on
[α**, α_e(t_e)]. Nothing is caught at the switch (only α* is at bearing 0, at distance ε/2). This is Lemma A3(b) with strict
order. "(as a limit)" only means that the old-heading bearings at t_e are the limits from inside the leg (continuity) and
can be deleted.

**(d) OK as a conditional reduction.** Checked: under (O), arc points at a leg start lie off the forward ray except the
target, and arcs shrink, so every point of the arc at time t has ρ > 0 on [0, t]; C¹ dependence on an open neighbourhood
(openness of {ρ > 0 on [0,t]}) covers the endpoints. L_I' = v∫_I sin²φ |∂S|/ρ ≤ v∫_I |∂_αβ| = v(β(α_e(t₂)) − 0) ≤ vπ
uses ρ|∂_αβ| = |sin φ||∂S| (Prop 3.3(2)) and monotonicity of β(·, t) on I ⊂ [α*, α_e(t)]; Λ(t₁) ≥ L_I(t₁) handles downward
jumps of α_e. Switches: Λ_old = |arc(α*, α**)| + Λ_new at the same instant, ≥ ρ_{α**} − ε/2 + Λ_new. Start:
Ψ(t₀) ≤ L(t₀) = lim_{t↑t₀} L(t) by monotone convergence (|∂_αS| non-decreasing in t), ≤ 2π + 2πv t₀ = 2π/(1−v). Then
time after t₀ ≤ (2π/(1−v) − ε/2)/(1 − v(1+π)) ≤ the stated bound. Correct.

Is the hypothesis ever true? (Evidence only, `sim_LG0.py`, grid of directions, RK4.) ε = 0.1: (O) held at every step for
v = 0.1 (N = 4000) and for ε = 0.05, v = 0.1 (N = 6000); for v = 0.2 (N = 4000 and 8000) and v = 0.24 (N = 4000) it fails
late in the chase (t ≈ 12.66 of 12.89 at v = 0.2; t ≈ 14.04 of 14.82 at v = 0.24): arc points with bearing −1.4·10⁻³
(v = 0.2, unchanged under N doubling) and −1.3·10⁻² (v = 0.24). So (d) is not vacuous for small v, but its hypothesis
appears false near the top of its range v < 1/(1+π); this mirrors the end-phase failure of (H) for the discrete chase.
Not proved either way.

## 3. Files

* `code/referee/D3b/constants.py` — exact recomputation of Lemma W6 and a grid check of (C0)–(C3), T_* ≤ 22.8.
* `code/referee/D3b/sim_W.py` — simulation of strategy W.
* `code/referee/D3b/sim_LG0.py` — test of (O) along LG0.
