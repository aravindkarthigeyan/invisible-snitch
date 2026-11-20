# Referee report R9-tilt-2 (second, independent referee)

Object: `referee/R9-tilt-claims.md`, read in full, against `r9/base_short/` sec2–sec4 and the uses in sec5.
Not read: `reports/referee-R9-tilt-1.md`, `reports/R9-tilt.md`, `r9/tilt/`.
Code and outputs: `code/referee/R9tilt_2/`:
- `constants.py` → `constants.out`: all constants, old and new, for p, for p with q = 2.42, and for p_A.
- `intB_upper.py` → `intB_upper.out`: rigorous upper bounds for ∫B and S₀.
- `tilt_opt.py`, `tilt_small.py` → `tilt_small.out`, and `tilt_geo.py` → `tilt_geo.out`: adversarial convex optimisation for Lemma T(i).
- `l2_opt.py` → `l2_opt_n60.out`: adversarial search for Lemma T(ii).

## Verdict summary

| Claim | Verdict |
|---|---|
| §0 New constants, side conditions (T1)–(T4) | OK. All four hold for p and for p_A. |
| §1 Lemma S (i)–(iii) | OK |
| §2 Lemma T (o) | OK |
| §2 Lemma T (i), one constant C_T | OK with one typo fix (F1) |
| §2 Lemma T (ii), L²/L¹ capped by N(I)² | OK |
| §3 Lemma G′ | OK |
| §4 Lemma O (O1)–(O3) | OK with one sentence added (F2) |
| §5 Lemma P (P1)–(P5) | OK |
| §6 Prop 4.3′ (6.1–6.4), coverage of all near pairs and times | OK |
| §7 Prop 4.2′/4.4 (C_p′, B₃′, B₅′) | OK |
| §8 thm:end(c), §5 replacements | OK. Optional remark R1. |
| §9 Values | OK. Every value reproduced; D_IIl″ = 182.20 is a valid but slightly loose upper bound (exact sup ≈ 181.50). |
| §10 Sanity checks | Not re-run. They are replaced by the stronger adversarial optimisation below, which finds no violation. |
| §11 Caveats G1–G3 | OK |

No GAP and no FALSE item was found.

## 1. Attempt to break the tilt lemma

**Model.** I = (0,1) in labels, R = λ_I = 1, M = 1. The tangent angle ψ is piecewise constant. To leading order in the amplitude:
- N(K)² = ∫_K(ψ − ψ̄_K)²
- angle(e_K) = ψ̄_K
- |e_J − e_I|/(Mλ_I^γ) → ψ̄_J − ψ̄_I

The hypothesis is imposed only on family pairs inside I: label length ≥ ε/2 and first point 0 (= a_j) or ≥ a₁ (= a_{j+1}). With a₁ = ε, the region (0, ε) is unconstrained except through pairs that start at 0. With a₁ = 0, every sub-pair is constrained.

Maximising a linear functional over an intersection of ellipsoids is a convex SOCP. So, for the discretised problem, the optimum found is the **global** maximum. I used Clarabel with cutting planes, iterated until no admissible constraint was violated, and then rescaled to exact feasibility. The optimiser was rebuilt as an exact polygon with amplitude M = m, from which the true N, e and c were computed. The exact ratios agree with the linear ones to 10⁻³, and c/l ≥ 0.998 > c_A.

In this limit (stretch w = 1, m → 0) the lemma's constant is C_T^lin = max(σ_q s(q), s(2q/(q−1))) with κ = c_A = 1, which gives 2.872. The constant as stated is C_T = 2.9109.

| setting | max of \|e_J − e_I\|/(Mλ_I^γ) found |
|---|---|
| uniform grid n = 60, ε = 0.05–0.067, J searched over positions and lengths | 2.07–2.16 |
| uniform n = 60, ε = 1/30 (J at either end, a₁ ∈ {0, ε}) | 2.257 |
| geometric grid, J = (0,δ), ε/2 = δ: δ = 10⁻² / 10⁻³ / 10⁻⁴ / 10⁻⁵ | 2.297 / 2.399 / 2.423 / 2.431 (δ = 10⁻⁶ came out lower, 2.25–2.36. That is solver ill-conditioning, a sub-optimal but feasible point, so it is not evidence either way.) |
| same, with the grid refined ×2 | stable to within 0.003 |

The worst case is a small J at one end of I, with constraints active at every scale. The supremum increases with the number of scales, roughly like T_∞ − Aδ^γ, and extrapolates to **T_∞ ≈ 2.44**. That is about 85% of C_T^lin and 84% of C_T.

So C_T cannot be beaten in the regime that dominates, and it is not wildly pessimistic either: about 16% slack. Two variations cannot close that gap:
- **Stretch.** Admissible stretch (∫_K w ≤ κλ_K at scales ≥ ε/2) changes the picture only at relative order κ − 1 ≈ 1.6%. The factor κ^{1/2}/c_A in s(·) already accounts for it.
- **Base region.** The unconstrained base region a₁ = ε gave nothing larger than a₁ = 0.

The empirical maxima reported in the claims (0.95–1.63) were therefore far from adversarial. That does not matter for correctness, but §10 should not be read as evidence of sharpness.

**L² bound, Lemma T(ii).** I used successive-linearisation ascent (each step an SOCP, so the objective increases monotonically), with 5 starts per case, and also an a-priori upper estimate (s^{1+2γ} + s·T*(s)²)/min(C_μ s, 1). For s ∈ [ε, 0.4λ] the worst ratio of ∫_a^s|T−e|² to the bound was 0.45–0.57, and the upper estimate was ≤ 0.63. As s → λ the ratio tends to 1 by construction: the cap is N(I)², which is attained. No violation. The L¹ bound follows from the L² bound by Cauchy–Schwarz and needs no separate test.

## 2. Proofs checked line by line, and the near-pair estimate rebuilt

**Lemma S.**
- (i) Both Cauchy–Schwarz estimates hold. Adding them uses 1/l(J) + 1/l_c = l(I)/(l(J)l_c). Correct, also when the complement has two arcs.
- (ii) The identity |d|²(1 − |d|²/4) = sin²θ holds. From c(J)|d|² ≤ V_{e_I}(I) = N(I)² we get 1 − |d|²/4 ≥ 1 − N(I)²/(4c(J)). This gives the bound directly, with no ambiguity about which root is taken.
- (iii) Correct.

**Lemma T(o).**
- The maximisation of ℓ(1 − ℓ/(κλ_I)) over ℓ ≤ κλ_J is correct, as is ρρ̃(ρ) ∈ {ρ²/4, ρ − 1}.
- (CA) is used with min(λ_J, K_RR) = λ_J.
- N(I)²/(4c(J)) ≤ m²r/(4c_A) < 1 follows from (T1).

**Lemma T(i).**
- In case A, the chain I_k = (α_k, α_k + λ_k) is nested and lies between J and I.
- α_0 = a, so I_0 = I.
- First points are admissible in all three sub-cases. When a = a_j and λ_I(1 − 1/q) ≥ ε, we have b − λ_k ≥ a_j + ε ≥ a_{j+1}, because a_{j+1} − a_j ≤ l ≤ ε since w ≥ 1.
- The case split is exhaustive: a ≥ a_{j+1}; or a = a_j with a′ = a; or a = a_j, a′ > a, split by λ_I(1 − 1/q) ≥ ε versus < ε.
- In case B, λ_J ≥ ε/2 gives a ratio < 2q/(q − 1) ≤ r_*.

**Lemma T(ii).** J = (a, a+λ_s) ⊂ I because ε/2 ≤ λ. The bound c(J) ≤ l(J) ≤ κλ_s holds, and the cap ∫_a^s ≤ N(I)² is trivial. Correct.

**Lemma G′.** g ≥ ε/κ puts every interval [g_i − ε/κ, g_i] inside [0, ∞). Correct.

**Lemma O.**
- (O1):
  - L₀ ⊂ I′ needs ε/2 ≤ λ, and l(L) ≤ κε/2 ≤ κg needs g ≥ ε/κ > ε/2. Both hold.
  - N(I′) needs g′ + λ ≤ R. This holds in the short case and on 𝒯₁.
  - The final formula is checked.
- (O2) and (O3): checked.

**Prop 4.3′.** I rederived each displayed bound independently. Each matches.
- (F′): u_y − a ≤ y − g, and y ≥ c₆ε ≥ ε/2.
- Tonelli with Φ(s) = ∫2c₆²y⁻³: the inner integrals are ≤ F(u_y)²/2 and ≤ F(u_y).
- The scalings give Φ_α, Φ_β (factor λ^{γ−1}) and Φ_l.
- 6.1: the substitution z = C_μc₆y gives C_μc₆h₁(·), and ∫₀^{C_μK_fλ}h₁ = λ(2 + log(C_μK_f)), so D_I′ = T_I + c₆χ log C_μ.
- The g = 0 leg gives Π₀, in both sub-cases β⁺ ≤ b and β⁺ > b.
- B(x) for g > 0, with the time integral through G′ and (P4).
- 6.3: |q| ≤ ρ/D² ≤ 1/D, giving D_IIl′.
- 6.4: since 1/(Mλ^γ) = μ^γ/m, the Λ factor is exact. The double counting at g = (μ − 1)λ only over-estimates.

Closed forms:
- The closed forms of Φ_α, Φ_l, Φ_β agree with quadrature to 10⁻⁴⁰.
- The (P3) identities agree to 10⁻⁴⁰.
- (P1) and (P4) were checked analytically. B is non-increasing on a 200 000-point grid for both tuples.

**Coverage, item (3).**
- Every near time lies in (t_n, t] with g < K_fλ.
- The short/long split depends only on λ.
- In the short case, g = 0 is handled by (O2) and g > 0 by (O1); g′ < ε/2 is handled through L₀.
- The long case is covered by the drop-in form (no (O1)) or by 𝒯₁ ∪ 𝒯₂.
- Tail pairs are far at t_W, so their near times are > t_W, where FamS = Fam.
- The final leg contributes one instant, of measure zero, and there p_a = 0.
- Pairs with b = U need nothing new.

No bound is used outside its hypotheses:
- (O1) is used only when g + λ ≤ R.
- (F)/(F′) involve only the pair (a,b) and its left-end sub-pairs.
- Lemma dist is used with w_s ≤ K_RR in both cases.

**sec5 replacements.** Every use is J ⊂ I sharing an end: Step 1; K₁ ⊂ K₂ and K₃ ⊂ K₄ share the left end; I ⊂ K₂ and I ⊂ K₄ share the right end; the i = j − 1 pairs. So C_T^A covers all of them. All occurrences are upper bounds, so the smaller constants only help.

## 3. Constants, independent (40 digits; ∫B and S₀ by rigorous upper sums)

| quantity | claims | this referee |
|---|---|---|
| C_T / C_μ | 2.9109 / 9.6082 | 2.910857 / 9.608152 |
| C_T^A (γ_D) | 2.9094 | 2.909356 |
| D_I′ | 16.034 | 16.0343 |
| Π_α / Π₀ / S₀ | 19.37 / 1.876 / ≤ 0.22896 | 19.3667 / 1.8765 / S₀ ∈ [0.228706, 0.228739] |
| ∫₀^{K_f}B | ≤ 8.2305 (quad 8.2256) | ≤ 8.225884 (geometric upper sum), quad 8.225584 |
| Π_β / D_IIs′ | 68.51 / 89.75 | 68.507 (from 8.2305) / 89.75 |
| Π_β coarse (G1) | 70.31 | 70.291 (consistent; the claim rounds up) |
| D_IIl′ / Λ(1) | 528.88 / 175.3 | 528.8775 / 175.2960 |
| D_IIl″ | 182.20 | sup = 181.503 at μ ≈ 1.019 (the claim is a valid upper bound) |
| **D drop-in / split** | **544.91 / 198.23** | **544.912 / 197.54** |
| q = 2.42: C_T, C_μ, D′, D″ | 2.8822, 9.4397, 544.56, 198.05 | 2.88224, 9.43975, 544.559, 197.35 |
| C_p′ / B₃′ / B₅′ | 3.855 / 126.03 / 493.5 | 3.8549 / 126.026 / 493.545 |
| old D (DI + DIIs) | 7322.76 | 7322.759 |
| θ̄ old → new (drop-in / split) | — | 0.8975 → 0.0841 / 0.0425 |

Side conditions (T1)–(T4), checked for p and for p_A:

| condition | p | p_A |
|---|---|---|
| (T1) | 0.00307 < 1 | 0.00307 < 1 |
| (T2) | 9.608 ≥ 2.273 | 9.599 ≥ 2.274 |
| (T3) | 0.614 ≤ 0.980 | 0.615 ≤ 0.980 |
| (T4) | 1.151 ≤ 2.941 | 1.155 ≤ 2.941 |

They must be added to Appendix A and to verify_constants for **both** tuples, since stage A needs (P6) for p_A, and hence D for p_A.

## 4. Fixes (exact text)

**F1** (§2, Lemma T(i), Case A, item (4)). Replace "λ(I_{K−1})/λ_J ∈ [1, q)" with "λ(I_{K−1})/λ_J ∈ (1, q]". The proof uses only "≤ q", so nothing else changes.

**F2** (§4, Lemma O (O2), case β⁺ > b). Insert before "then I₀ := (β,β⁺)": "If the leg is final, τ = T_stop and P = x_β = x_a, so p_a = 0. Otherwise". The bound λ_{I₀} ∈ [ε/κ, ε] needs a non-final leg (Lemma legs(i)). The final leg is a single instant, so it does not affect any time integral either.

**R1** (optional, §8). C₃ := 2C_B^A + C_A^A could become 2C_T^A instead of 3C_T^A: each of the two sums in Step 3(α) has two terms. 3C_T^A is valid as stated.

**R2** (optional, §9/§10). State D_IIl″ = 181.51 (it is now 182.20) if a tighter value is wanted. Add one sentence saying that the adversarial maximum of the tilt ratio is about 2.44 (about 84% of C_T), so that §10's 0.95–1.63 is not read as sharpness evidence.
