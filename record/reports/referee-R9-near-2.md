# Referee report R9-near-2 (second, independent referee)

Object: `referee/R9-near-claims.md`, i.e. the drop-in Proposition 4.3'' in `r9/near/prop_near.tex` and the evaluation
`r9/near/near_const.py` / `near_const.out`. Base: `r9/base_short/` (sec2–sec4). R-tilt Lemma T (C_T = 2.9108574,
C_μ = 9.608152) assumed as instructed. I did not read `reports/R9-near.md` or the other referee's report.

Order of work: I first rebuilt the near-pair estimate from sec2 (Lemma excess(iii), field(iii)), sec3 (dist, legs, gapint,
local, chase(1), sep(c)) and Lemma T, before opening `prop_near.tex` (the claims file is only a table; the lead then confirmed
that `prop_near.tex` and `near_const.py` are the object under review). I then checked the proof line by line, wrote an
independent evaluator of 𝒟(θ,r) from the TeX definitions alone, and ran adversarial simulations.

## Summary verdict

**The factor-209 improvement is real.** I found no mathematical error in Proposition 4.3''. My own reconstruction of the
near-pair increment has the same structure:
E′ ≤ v∫a*|T−e|² + v∫|ϑ||q|, with |q| ≤ |p|/D², D ≥ λφ_θ, |p| ≤ G + |p_a|, layer-cake against the Lemma T(ii) budgets, and
per-leg averaging of |p_a| along P ∈ [x_β, x_β⁺]. Each step has the stated direction and the stated range of validity. An
independent evaluation of 𝒟 confirms that it stays below the printed cell bounds, with a margin of 1–2%.

The gaps are editorial or bookkeeping, not mathematical. (1) The "Changes to Definition 3.3" delete T_I, but T_I is still used
by Proposition 4.4 (length) and by L_J. (2) Proposition 4.4's near paragraph cites "Term I of Proposition 4.3", which this
replacement removes. (3) D′ is evaluated only at the main tuple p, and the stage-A tuple p_A also needs it.

The rigour of the double-precision evaluation is a non-issue at the current v₀. (P6) needs only D′ < (1−f_F²)/(2v₀) ≈ 8177,
and the bound is 35.

| # | verdict |
|---|---|
| N-D | OK |
| N-B | OK |
| N-L | OK |
| N-S | OK |
| N-O | OK (one wording fix) |
| N-A | OK |
| N-Σ | OK |
| N-P | OK with fixes (definition bookkeeping, see F1–F3) |
| N-E | OK with fixes (p_A value; statement of rigour). Both 34.99 (R-tilt) and 42.40 (Definition 3.3) confirmed independently |
| N-X | Confirmed independently (my own code, not `check_independent.py`) |
| N-Sim | Confirmed and strengthened: J2-saturated adversarial data give at most ≈1.5, far below the bound |

## 1. Rebuild and term-by-term comparison

Notation as in `prop_near.tex`: μ = Mλ^γ, θ = ε/λ ∈ (0,2], r = R/λ, x = g/λ, σ = (s−a)/λ.

**Distance (N-D).** Lemma dist with base β gives D(s) = max(ρ_s, ε) ≥ max(ε, c_A min(w_s, K_RR) − δ₁ε). Here
w_s ≤ g+λ < (K_f+1)λ ≤ (K_f+1)R ≤ K_RR, so the min is w_s. The hypothesis of Lemma dist holds at every s ∈ [a,b] by
Lemma local(ii), for body and tail pairs alike. a*(ρ) = 1/ρ for ρ ≥ ε, and a*(ρ) = 2/ε = 1/D + 1/ε for ρ < ε. ρ < ε forces
c_Aw − δ₁ε < ε, i.e. w < c₆ε. **OK.**

This is where much of the gain comes from. The old bound max(w, c₆ε)/c₆ loses a factor up to c_Ac₆ = 1+δ₁ ≈ 2 in D, so up to
4 in D⁻² (Remark R1 is correct). The bound covers the cases w < ε/2 (where only D ≥ ε is used) and pairs at the base, g = 0.

**Budgets (N-B).** Ω(σ) ≤ M²λ^{2γ} min(C_μλ_s, λ) = μ²λ Ω̄(σ) is Lemma T(ii), together with N(a,b)² ≤ M²λ^{1+2γ}. The pair
(a, a+λ_s) is a family pair: its first point a is that of the family pair (a,b), and its length lies in [ε/2, λ] since θ ≤ 2.
It lies in [β, max(b, β⁺)], so (J1) holds for it and l(a,s) ≤ κλ_s. Cauchy–Schwarz gives G ≤ ∫|T−e| ≤ μλ(κλ_σΩ̄)^{1/2}, and
|ϑ| ≤ |T−e|. **OK.**

**Layer cake (N-L).** All kernels are non-increasing in σ: φ_θ is non-decreasing, and the indicator is that of an initial
segment. Each ν([0,σ]) is dominated by Φ(σ) including the atom Φ(0) = F(θ/2). The proof via {ψ > t} = [0,σ_t) or [0,σ_t] is
correct, including the left-limit case. **OK.**

**Term I.** I ≤ (v/λ)∫ψ_I dΩ ≤ vμ²𝔦(x). **OK.**

**Term II, offset route.** p(s) = (x_s − x_a)×e + p_a and |(x_s−x_a)×e| = |∫ϑ| ≤ G(σ). Then
∫|ϑ|G ψ₂ ds = ∫ψ₂ d(G²/2), with ν([0,σ]) = G(σ)²/2 ≤ μ²λ²Q̄/2, and |p_a|∫ψ₂ dG ≤ |p_a| μλ 𝔧₂. **OK.**
The 1/D route uses |q| ≤ |r×e|/D² ≤ ρ/D² ≤ 1/D, so II ≤ vμ𝔧₁ = vμ²(r^γ/m)𝔧₁. **OK.**

**Offsets (N-O).** p_a is affine in P = (1−s)x_β + s x_β⁺, so |p_a| ≤ (1−s)Y_β + sY_β⁺ exactly.
- **Route 1.** Uses ∫_{I′}|T−e|² = N(I′)² + c(I′)|e_{I′}−e|² ≤ (1+κC_B²)M²Λ^{1+2γ}. The tilt step is same-right-end, J ⊂ I′,
  both family pairs because Λ ≤ g+λ ≤ R at short-type times.
- **Route 2.** Lemma S with the monotone map (u,v) ↦ uv/(u+v).
- **Route 3.** L = (a′,a) is a family pair when g′ ≥ ε/2; same left end as I′.

  All three routes check, including the ℓ = max(y, θ/2) bookkeeping for g′ < ε/2: L ⊂ (a′, a′+ε/2) ⊂ I′, since ε/2 ≤ λ.
- **(ii), the tilt-free long route.** This is the decisive new ingredient, and it is correct.
  - (a′,b) is good: for a′ = β by local(ii); for a′ = β⁺, body pairs have U−b ≥ W_e and tail pairs have β ≥ a_{jW} ≥ W_e.
  - Λ ∈ [ε/2, K_RR), so (CA) gives c(I′) ≥ c_AΛ.
  - l(I′) ≤ κΛ by covering I′ with ⌈Λ/R⌉ equal pieces of length in (R/2, R]. Each piece starts at a′ or at a point ≥ a′+R/2.
    By (N1), R/2 ≥ K_εε/2 ≥ ε ≥ β⁺−β, so each start is β or ≥ β⁺. Every piece is therefore a pair of the leg's family inside
    [β, b], hence admissible by local(i), and (J1) applies to it.
  - So N(I′)² ≤ 2(κ−c_A)Λ. No (J2) and no tilt bound is needed, so pairs with g+λ > R are covered. This was the case that
    previously forced the 1/D route and dominated D (Λ(1) = 175 in R-tilt).
- **(iii).** All three alternatives for β⁺ > b check: (a) tilt with the same left end, at scale λ_{I₀} ≤ ε; (b) Cauchy–Schwarz on
  (b, β⁺) with l(I₀) − l(J) ≤ κε − c_Aλ; (c) Lemma S. Ḡ(min(θ,1)) covers β⁺ ≤ b, since β⁺ − β ≤ ε and β⁺ − a ≤ λ.
- **(iv).** Correct.

Wording fix: in (ii), "If g′ > R, cover L…" should also say that when ε/2 ≤ g′ ≤ R but Λ > R, I′ is covered in the same way.
The text says "the same covering gives l(I′) ≤ κΛ", which is correct but implicit for this sub-case.

**Leg averages (N-A).** I re-derived both bounds.
- s = σ/(σ+ρ), and σ+ρ = c(β,β⁺;τ) ≥ c₀ by chord monotonicity (the three points are collinear by chase(1)).
- 1−s ≤ ρ/c₀ ≤ 1 − (1−v)τ′/c₀, which integrates to c₀/(2(1−v)) ≤ d_Lε/2.
- s ≤ min(1, (1+v)τ′/c₀), and the leg duration satisfies c₀ ≤ T ≤ c₀/(1−v), since |ρ′| ≤ 1. This gives
  ∫s ≤ c₀(1+3v)/(2(1−v²)) ≤ (3d_L−2)ε/2, using v ≤ 1 − 1/d_L.

The per-leg bound needs Y_β and Y_β⁺ bounds that are uniform over the leg, and they are: the type and the gap are constant on a
leg, and λ and μ are fixed. **OK.**

**Leg sums (N-Σ).**
- There is at most one g = 0 leg, and it is the last: after it a < β, so the pair leaves the family.
- Gaps g ≥ ε/κ are spaced by ε/κ, so z_k ≥ kθ/κ and n ≤ ⌈κK_f/θ⌉ − 1.
- The non-increasing envelope H* makes the discrete sum and the integral form valid.

**OK.** This is conservative: H at long-type x near K_f propagates leftward through H*, so D′ could be reduced further. This
does not affect validity.

**Assembly (N-P).** Duration per leg is ≤ d_Lε = d_Lθλ. Per leg the proof takes the minimum of bounds each valid on the
whole leg, and the conversion λ = μλ·r^γ/m is right. The start value E(t_n) ≤ ½f_F²M²λ^{1+2γ} comes from Proposition 4.2 or
(TW) at a leg start, or from (S2) at t_td. Tail pairs are far at t_W, so the near phase starts later.

Cases checked:
- pairs at the base (g = 0, H₀; always short-type);
- pairs at the cut and the final leg (P is constant after T_stop, and t ≤ T_stop);
- the ε-disc (the indicator term of a*, and w < ε/2);
- tail pairs (local(ii) and good-ness, start after t_W);
- long pairs with g+λ > R (route (ii));
- the full range θ ∈ (0,2], r ≥ max(1, K_εθ): r = R/λ and ε ≤ R/K_ε, so this is exactly the admissible set, not a smaller one.

Mathematics **OK**, with the bookkeeping fixes below.

### Fixes required (exact text)

- **F1.** In "Changes to Definition 3.3", replace "Delete T_I, T_α, T_β, k₀, D_I, D_IIs, D_IIl (and Ψ_I if unused elsewhere: it
  is still used in Proposition~\ref{prop:length})" by:
  "Delete T_α, T_β, k₀, D_I, D_IIs, D_IIl. **Keep Ψ_I and T_I**: they are used in Proposition~\ref{prop:length} and in
  L_J(U_0) = exp(…) + v₀κT_I." (sec3.tex l.88 and sec4.tex l.204/227 use T_I.)
- **F2.** Proposition~\ref{prop:length}, *Near* paragraph: it says "As in Term I of Proposition~\ref{prop:near}…". After the
  replacement, that argument (the set {ρ_s < y} lies in (a, a+λ_y), λ_y ≤ min(λ, c₆y); the ω(ε)/ε piece only when g < c₆ε;
  gapint(i),(iii)) is no longer in the text. Either keep the old Term-I paragraph as a lemma, or restate it inside
  Proposition~\ref{prop:length} with ω̃ in place of ω. Otherwise the length proposition cites a deleted argument.
- **F3.** Add (N1) K_ε ≥ 2 to (P0) and to `verify_constants.py` (both tuples; it holds, K_ε = 999.98). Add θ̄ := f_F² + 2v₀D′
  with D′ evaluated for **each** tuple. Stage A (p_A, γ_D = 0.614666, C_T^A = 2.9094) is also an instance of the end theorem,
  so (P6) must be checked there with D′(p_A). I ran `near_const.py` unchanged except for γ = 0.614666 and C_T = 2.9094. It
  gives D′(p_A) ≤ **35.001** (R-tilt) and ≤ **42.413** (Definition 3.3). These are slightly above the p-values, so Lemma E
  should print both, or the single value 35.01.
- **F4** (statement). Lemma E should read "D′ ≤ 34.99 (double precision; not interval arithmetic)". It should add that (P6)
  only needs D′ < (1−f_F²)/(2v₀) = 8.18·10³, so the conclusion is insensitive to rounding by more than two orders of
  magnitude. If v₀ is later raised towards the (P6) threshold of 1.4·10⁻², interval arithmetic becomes necessary.

## 2. Hunting list (each checked, none found)

| suspicion | finding |
|---|---|
| term dropped | E′ ≤ I + II with q̄ = 0 is Lemma excess(iii). Both atoms (Φ(0)) and the a*-indicator are kept, and every L¹/L² budget includes the atom. |
| inequality in wrong direction | Kernels are taken at the left end of σ-cells and x-cells (non-increasing), and increasing factors at the right end. θ/φ_θ is non-decreasing in θ, which I verified: θ/max(θ, c_Aw−δ₁θ) = min(1, θ/(c_Aw−δ₁θ)⁺). 1/φ is not monotone in θ, and the code correctly uses 1/max(θ_l, c_Aw−δ₁θ_h). |
| short-pair bound used for long pairs | 𝔭 (routes 1–3) is used only where x ≤ r_l − 1. Ambiguous r-cells take the max of the short and long forms. 𝔭_L is valid at all times. |
| wrong time interval | All integrals are over (t_n, t], leg by leg. The per-leg minimum is over bounds valid on the whole leg. |
| missing case | Base (g = 0), cut/final leg, ε-disc, tail pairs, λ > ε (θ > 1, β⁺ > b) are all covered (§1). |
| sup over too small a set | The set {0 < θ ≤ 2, r ≥ max(1, K_εθ)} is exactly the admissible set. Cells cover r ≥ K_f+1 (short only, 𝔭_L dropped: conservative). The bottom cell (0, 10⁻⁷] uses θ-free kernels; I re-derived its closed-form majorants of 𝔦, 𝔮, 𝔧₁, 𝔧₂, 𝔭 (all correct) and the monotonicity of zH̃(z) used for θH*(θ/κ). |
| implicit parameter range | Needs (N1); uses K_f + 1 ≤ K_R (P0), κ ≤ 4/3 (θ/κ ≥ θ/2), v ≤ 1 − 1/d_L (P1). All are stated or in (P0)–(P2). |
| code vs. definition | `pfrak` uses C* = CTL = 2C_T and requires y ≥ θ_h/2 for the chord route (stricter, so conservative). `pstar` is the correct running max; 𝔭 can drop at y = θ/2 when the chord route becomes available, and the code handles this. P₀ and Ḡ match. The discrete sum uses k·θ_l/κ and THst at the largest grid point ≤ z (conservative). The integral form THst[0] + κΣHst·dx is valid. |

## 3. Numerics

### 3a. Independent evaluation of 𝒟(θ,r)

Script: `scratch/dprime_indep.py`, written from the TeX only. It uses composite Gauss–Legendre in σ with breakpoints at
θ/2, 1/C_μ and c₆θ − x, exact Stieltjes atoms, a dense x-grid with an envelope for H*, and the exact discrete sum (or the
envelope at the grid point below kθ/κ when k* > 3000). This is a point evaluation, not a bound, so it should lie slightly
below the cell bounds.

| (θ, r) | mine | near_const cell bound |
|---|---|---|
| (0.00562, 5.63) (worst cell) | 34.26 | 34.99 |
| (10⁻⁶, 5) | 32.87 | 33.23 (bottom-adjacent cells) |
| (10⁻³, 5) | 33.25 | 33.6 |
| θ ≥ 0.035 (short only) | ≤ 25.7 | 26.2 |

I scanned 210 points in the new constants: θ ∈ [10⁻⁶, 2], 30 values; r ∈ {r_min, r_min+0.03, 2, 3, 4, 4.5, 5, 5.5, 5.8, 6.0,
6.03, 6.1, 6.5, 8}, restricted to r ≥ r_min = max(1, K_εθ).
- **Maximum** of 𝒟: 34.15 at θ = 4.8·10⁻³, r = 5 (34.26 at the claimed worst point).
- **Minimum** of 𝒟: 17.8, at r just above K_f+1, where only short-type times occur.
- **Old constants** (Definition 3.3): 140 points, maximum 40.30 (θ = 4.5·10⁻³, r = 5), against the bound 42.40.

Every value of mine lies below the corresponding cell bound. The location of the maximum agrees with near_const: long-type,
θ ≈ 5·10⁻³ near the constraint r = K_εθ, and r ≈ 5–6. Conclusion: the claimed values 34.99 and 42.40 are upper bounds
for 𝒟 that are tight to about 2–5%. This independent check confirms N-X.

### 3b. Adversarial simulation of Construction C

Script: `scratch/sim_adv.py`, adapted from `code/referee/Q1_2/sim.py`. Settings: main tuple, K_ε = 20 (U = 10R) and
K_ε = 100 (U = 4R), h = 0.2ε, v ∈ {10⁻⁴, 10⁻³, 10⁻²}, bend ±1 (bend tuned to saturate (S1)/(CA)). Measured:
Deff = max over tracked near pairs of ΔE/(vM²λ^{1+2γ}).

Start data are adversarial for the proposition's own hypotheses, not just (S2). The roughness amplitude was tuned so that
N ≈ 0.95·Mλ^{1/2+γ}, i.e. (J2) is 95% saturated at t_td (S2-ratio 17.5, i.e. 17.5·s₀ = 0.95), instead of the s₀ = 0.054 of (S2). Three
front shapes were used:
- (multi) multiscale sinusoids;
- (zig) multiscale plus a strong square-wave tangent at period 2ε;
- (kink) multiscale square waves, i.e. corners at every scale.

Deff = max ΔE/(vM²λ^{1+2γ}) over 31 282 (K_ε=20) or 63 433 (K_ε=100) near pairs:

| start data | v = 10⁻⁴ | 10⁻³ | 10⁻² | J2 max during run |
|---|---|---|---|---|
| (S2)-saturated multi, K_ε=20 | 0.0036 | 0.0036 | 0.0039 | 0.057 |
| (J2) 95% multi, K_ε=20, bend ±1 | 1.30 / 1.32 | 1.28 / 1.31 | 1.42 / 1.45 | 0.99 |
| (J2) 95% zig, K_ε=20 | 1.35 / 1.35 | 1.35 / 1.35 | 1.52 / 1.45 | 1.02 |
| (J2) 95% kink, K_ε=20 | 0.99 / 1.00 | 0.99 / 1.00 | 1.20 / 1.20 | 0.98 |
| (J2) 95% multi, K_ε=100 | 1.30 | – | 1.56 | 1.00 |
| (J2) 95% kink, K_ε=100 | 0.95 | – | 1.34 | 1.04 |

The largest measured value is 1.56, or 4.5% of D′ = 34.99 and below the minimum 17.8 of 𝒟 over the admissible set. CA ≥ 1.0035
and J1 ≤ 1.0034 throughout.

Every value lies far below the bound: 𝒟(θ,r) ≥ 17.8 on the whole admissible set, and D′(K_ε=20) ≤ 45.8. The (J2)-saturated
fronts raise the measured constant about 400-fold over the (S2)-saturated runs (0.0036, which reproduces N-Sim). At v = 10⁻²,
(J2) itself is slightly exceeded (ratio up to 1.02), and the measured increase still stays at ≈3% of the bound. No violation.

## 4. Rigour of the D′ evaluation (task 4)

- The cell method is a valid upper-bound scheme. I checked every monotonicity used (§2) and the bottom-cell majorants.
- Floating point is uncontrolled. The quantities involved are sums of order 10⁴ positive terms in double precision; relative
  rounding error is ≲ 10⁻¹², against a cell over-estimate of 1–2%.
- Since (P6) has slack ×230 (D′ needed < 8177), the rounding issue cannot change any conclusion of the paper at v₀ = 6·10⁻⁵.
- Verdict **OK with fix F4**: state the precision honestly. Interval arithmetic would only be needed if v₀ were pushed to
  within a factor of about 2 of 1.4·10⁻².

## 5. Is the factor 209 real?

Yes, and most of it does **not** come from the unrefereed tilt lemma.

- **The near-pair machinery alone.** With the Definition 3.3 tilt constants (C_μA = 42.5, C* = C_TL = 16.3), the new
  proposition gives D′ ≤ 42.40, against 7322.76. That is ×173 with refereed ingredients only. My independent scan of the old
  constants is in §3a.
- **R-tilt's constants.** They add only ×1.21 (42.40 → 34.99).

The gain comes from four ingredients:
- the exact two-regime distance (up to ×4 on D⁻² terms);
- the leg average of |p_a| (×½ on Y_β, and Y_β⁺ evaluated at the next gap);
- L² budgets used directly (𝔦, 𝔮), in place of products of L¹ bounds C_1A²;
- the tilt-free long route (ii), which removes the 1/D long term that previously dominated (D_IIl = 2961).

The old D_IIs, which contained C_TL·C_1A·T_β products, was the largest piece (6837) and is gone entirely.

**Consequence.** The claim's dependence on R-tilt Lemma T only concerns the last ×1.2. If Lemma T fails at referee, the paper
can use D′ ≤ 42.40.
