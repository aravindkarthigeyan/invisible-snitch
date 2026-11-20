# Referee report R9-far-2 (second, adversarial referee) on `referee/R9-far-claims.md`

Scope: F1–F9 of `referee/R9-far-claims.md`, read against `r9/base_short/` sec2–sec8. The doubly refereed R-tilt
(`referee/R9-tilt-claims.md`) and R-near are assumed. I did not read `reports/referee-R9-far-1.md`, `reports/R9-far.md` or
`r9/far/`. My code and outputs are in `code/referee/R9far_2/`:

| script | what it does | output |
|---|---|---|
| `consts.py` | rebuilds every new constant from the formulas as stated in the claims (base tuple, v0 = 6e-5); touch-down constants (Def 7.1) at other v̄ | `consts.out` |
| `lemmaE_attack.py` | tries to break Lemma E* on adversarial arcs, then Nelder–Mead maximisation of the two ratios | `lemmaE_attack.out` |
| `touchdown_chords.py v ε` | the curve x^∘ of design T from the exact conserved quantities (C, h, h′ = −(1−v²)) in mpmath (66–126 digits), with the forward ghost labels as virtual candidates (RK4 on [t_a,t_dd]); checks T2*, (S1G) and the proof steps over all pairs | `touchdown_chords.out`, `td_*.out` |
| `sim_far.py` | the greedy chase (Def 3.1) started from x^∘ (smooth, or with multiscale roughness that brings (S2) to 0.80–0.81 of saturation); measures Lemma (J), Prop F*(i)/(iii), Lemma Du* in situ, and far-pair and length growth | `sim_*.out`, `simM_*.out`, `*.json` |
| (inline) | touch-down side conditions at v̄ = 4.146e-3 | `sc_retune.out` |

## Verdicts

| claim | verdict |
|---|---|
| F1 Lemma E* | **OK** |
| F2 Lemma Du* + drop-in in Thm 5.2(v) | **OK** |
| F3 Lemma 3.6(iv) | **OK** |
| F4 Lemma T2* | **OK** |
| F5 (S1G), start addendum, Lemma 3.7(iii) | **OK with fixes** (bookkeeping only; text below) |
| F6 Prop F* incl. Lemma (J) | **OK** |
| F7 Prop L* | **OK** |
| F8 constants and side conditions | **OK with fixes** (two misprinted table values, no effect on any condition) |
| F9 joint point v0 = 4.146e-3 | **not verified.** The vector is in a file I may not read. One precondition is missing (see F9). |

I found no counterexample. Every inequality I could stress held. The tightest margins were 1.00015 for T2* at v = 6e-5 and
1.006 for Prop F*(iii) in the simulation.

---------------------------------------------------------------------------------------------------------------------

## F1 Lemma E* — OK

**Proof.** I checked every step.
- **Step 0.** The arc distance alone gives A = Π/ρ and q = Q(r) on the arc. The convex hull is never needed.
- **Derivative bounds on Q.** ∂_{y2}Q = −y1(y1²−2y2²)/|y|⁵, with |z(3z²−2)| ≤ 1. ∂_{y1}Q = −y2(y2²−2y1²)/|y|⁵, with |y2²−2y1²| ≤ 2|y|².
- **Steps 1–2.** δ(0) = δ(l) = 0, ∫ς² ≤ ∫|T−e|² = N², and Wirtinger's inequality with the sharp constant (l/π)² all apply.
- **Step 3.** The integration by parts is legitimate. G = Q(r(σ)) − Q(r(0)) is C¹ because r ≠ 0 on the arc, and dr/dσ = T at fixed t.
- **Step 4.** y2 = r_a·e^⊥ + δ, with |r_a·e^⊥| = |p_a|. The three Cauchy–Schwarz and Wirtinger bounds give exactly
  lN²/(πρ*²) + 2|p_a|l^{3/2}N/(πρ*³) + 2l²N²/(π²ρ*³).
- **Step 5.** Same as Lemma 2.6(ii).
- **Step 6.** |e×r| = |r_a·e^⊥ + δ|, and Minkowski in L²(ds) gives (b).
- **Corollaries.** (a) and (b) imply the old Lemma 2.6(v). The right-hand sides decrease in ρ, ρ* ≥ ρ_m, and (x+y)² ≤ 2x² + 2y².

**Attempts to break it** (`lemmaE_attack.out`; v = 1 and A = Π/ρ, so the statement is purely geometric):
- 11 432 arcs. These include random multi-mode tangents with amplitudes up to 6 rad, hairpins (a turn of ≈π over widths
  down to 0.01 l), spirals and circles with up to 4π of total turning, and S-curves.
- P was placed in the hull, on the chord line, at normal offsets down to 40 grid steps from the arc, and near the end points.
- Maximum ratios: 0.979 for (a) and 0.968 for (b).
- Nelder–Mead maximisation over 6 tangent modes plus the position of P (40 starts each) converges to ratio 0.999999 for
  (a) and 1.000000 for (b). It gets there only in the degenerate limit: P on the chord line, ρ* ≈ 7·10⁶ l, and N → 0,
  where the leading term vN²/ρ* is attained.
- So the lemma is sharp but not violated. No non-convex arc, curl-back or P inside a hook comes near 1.

## F2 Lemma Du* — OK

- The Grönwall argument goes through verbatim. α and β are continuous because ρ* is continuous and ≥ ε.
- **Drop-in for Thm 5.2(v)** (sec5 l.236–250). Only "ρ_m ≥ ζ(g̃+τ) ≥ 4l, ρ_m ≥ ε" and β are used there.
  - Since ρ* ≥ ρ_m and α*(ρ) = (v/ρ)(1 + l/(πρ) + 2l²/(π²ρ²)) decreases in ρ, α* ≤ aD*(4)v/ρ_m ≤ η_N/(g̃+τ′) with
    η_N = aD*(4)v0/ζ.
  - β* ≤ β/π with the same |p_a| bound, so c_β gains the factor 1/π.
- No other user of Lemma 2.7 or 2.6(v) exists (grep: sec4 l.51, 86, 217; sec5 l.238–246; sec8 l.13).
- η_N also enters (A5) and (TS) in sec8. The change only helps, as the claims say.

## F3 Lemma 3.6(iv) — OK

- The lower group uses the intervals [g_i − ε/κ, g_i] ⊂ (g_0, Y/2], where H is non-increasing.
- The upper group uses [g_i, g_i + ε/κ] ⊂ [Y/2, Y], since g_i + ε/κ ≤ g_{i−1} ≤ Y and H is non-decreasing there.
- The intervals are disjoint across the two groups, and there are two exceptional values. The constant is χ_g = κd_L.

## F4 Lemma T2* — OK (numerically stressed with the exact touch-down state)

**Proof.** I checked every step.
- Case A: Δ̃ ∈ [Δ0, π] and c_sep > 2ε̄, then Lemma 7.9(c).
- Pointwise bound w ≤ W_x(2/|θ|_∘)^{2v}, from the proof of Lemma 7.10. It holds for every label ≠ 2π, including the forward and tail zones, because (2/|θ|_∘)^{2v} ≥ 1 on I_η.
- Arc bound for Δ′ ≥ Δ0: (4/Δ′)^{2v} ≤ (8/λ0)^{2v} by (SC41), and (8/λ0)^{2v}/(1−2v) ≤ L̂ for v ≤ v̄.
- The two label sets of d_c lie in [Θ_b, Θ_a + 2π] and are disjoint, because Θ_b ≤ 2π + b_e < 2π + α0 ≤ 2π + Θ_a.
- Case B is the proven (T2).

**Computation** (`touchdown_chords.py`).
- **Exact front.**
  - Run 1 and run 2 were computed in closed form from C = ρ sg(β) and h = ρ(cos β + v), with h(t) = h(t1) − (1−v²)(t−t1)
    and a safeguarded Newton solve for τ.
  - t_dd = t1 + (ρ0−ε)/(1−v) + ε∫dσ/(1−vσ(2−σ)), and the end label b_e = α0 − ξ_e is solved from C(b_e) = ε g_max.
  - The hole at 2π (Z_s) is resolved by labels geometric down to |α − 2π| = 1e-14 on both sides.
  - The tail is resolved geometrically down to ξ − ξ_e = 1e-9·η, and the forward zone down to ξ = ξ1ε/12.
  - The ghost labels ξ < ξ1ε are the virtual candidates: true state at t_a, then RK4 of x′ = vF(x − P) on [t_a, t_dd].
- **Pairs.** About 3 800 labels give about 7.2·10⁶ pairs per run. Across-hole pairs (Θ_a < 2π < Θ_b) and wrap pairs
  (u_a < 0.05 and U − u_b < 0.05, the X0 side against the E_Y side) are reported separately.
- **Constants.** W_x, L̂, k_c, c_N and Δ0 are Definition 7.1 evaluated at v̄ := v.
- **Results:** minimum of chord / (claimed bound) over all pairs with λ > λ0.

| v \ ε | 1e-3 | 1e-6 | 1e-12 | 1e-30 |
|---|---|---|---|---|
| 6e-5 | 1.00027 (wrap 1.475) | 1.00016 (wrap 1.026) | 1.00015 (wrap 1.0117) | 1.00015 (wrap 1.0117) |
| 1e-3 | 1.00333 (wrap 1.508) | 1.00280 (wrap 1.050) | 1.00278 (wrap 1.036) | 1.00278 (wrap 1.036) |
| 4e-3 | 1.0271 (wrap 1.666) | 1.0252 (wrap 1.166) | 1.0252 (wrap 1.150) | 1.0252 (wrap 1.150) |
| 5e-3 | 1.0392 (wrap 1.723) | 1.0369 (wrap 1.208) | 1.0368 (wrap 1.191) | 1.0368 (wrap 1.191) |

How to read the table:
- **Tightest pairs.** The global minimum is always at an almost antipodal pair (λ ≈ d_c ≈ π), often across the hole. There
  the bound is 2 sin(π/(2W_xL̂)) ≈ 2 and the chord is ≈ 2.0002. So T2* is essentially sharp at v = 6e-5, and the slack
  comes from W_xL̂ > 1.
- **Wrap pairs.** These are governed by (T2): min c/(k_c d_c) = 1.012 to 1.09.
- **Proof steps, checked separately:**
  - Case A, Lemma 7.9(c): c/2sin(Δ̃/2) ≥ 1.00005.
  - Case A, step (i): W_xL̂Δ/λ ≥ 1.0066.
  - Case A, step (ii): W_xL̂(2π−Δ)/d_c ≥ 1.014.
  - Δ/Δ0 ≥ 1.007 for λ > λ0.
  - Case B: c/(k_c d_c) ≥ 1.012.
- **Stretch constant.** The actual max w/(2/|θ|)^{2v} is 1.0004 to 1.014, against W_x = 1.006 to 1.117. U ≤ U_max in every run.
- **Global ratio.** The bare chord-to-arc ratio c/min(λ, d_c) over all pairs with λ ≥ ε/2 has minimum 0.6363, at the
  antipodal pairs (2/π). It is correctly captured by the sine branch of 𝒢 and not by a linear branch.

## F5 (S1G), addendum to Lemma 8.2, Lemma 3.7(iii) — OK with fixes

**Mathematics.** All three steps are correct.
- For λ ≤ λ0: φ(λ) ≥ c0′λ, with K_RR < λ0 from (A6).
- For λ > λ0: T2* with d_c ≥ y.
- Stage A: a + U_A − b ≤ a + U − b and 𝒢 is non-decreasing.
- Lemma 3.7(iii): the chords are non-decreasing in t, and |P − x_β| ≤ δ1ε.

**Numerics.** On the exact x^∘, c ≥ 𝒢(min(λ, d_c)) holds for every pair with λ > K_RR, at every (v, ε) above. The
minimum ratio equals the T2* column, and the wrap and across-hole subsets are ≥ 1.0117.

**Fixes (bookkeeping).** Prop F*(iii) now uses start data of pairs other than (a, b), namely (S1G) for the pairs
(a_{j(τ)}, s), s ∈ [a, b]. The locality principle (sec3 l.293–297) has to say so:
- Add to the locality principle, after "…of Lemma~\ref{lem:local}(ii) (through Lemma~\ref{lem:dist})": "and, under (S1G),
  the hypothesis (S1G) at $\ttd$ for these pairs $(a_{j(t')},s)$ (through Lemma~\ref{lem:dist}(iii))".
- Theorem 3.4(d) (sec3 l.147–148): append "and, under (S1G), if $s-a_j>K_RR$:
  $\rho_s(t)\ge\max(c_AK_RR,\mathcal G(\min(s-a_j,a_j+U-s)))-\delta_1\eps$".
- Prop 8.3: in Step 1 and Step 6, cite the addendum next to Lemma 8.2 where (S1) and (S2) are concluded: "and (S1G) by the
  addendum".

## F6 Proposition F* — OK

**Proof.** I checked every step.
- **Distance (i)–(iii).** w_s ≥ g; min(w_s, β + U − s) ≥ min(g, U − λ − g); (P2*) gives ρ* ≥ ε; K_1 and K_2 bound l, and the
  hull loss is gone.
- **Lemma (J).**
  - H = ρ_G(min(g, Y−g))^{−k} has the required unimodality, including the extension ρ_G(y) = ρ_G(0) for y < 0.
  - g ≤ Y on 𝒯_3 (g ≤ a ≤ U − λ; tail pairs g ≤ g_W ≤ a), and the substitution y = Y − g is valid.
  - The first entry uses T_B = χ_gU.
- **Forcing for g > η1R.** |p_a| ≤ ρ_a ≤ ρ* + l.
- **The three |p_a| bounds.**
  - Bound 2 uses V_e(a′,a) ≤ V_e(a′,b) = N(a′,b)² + c(a′,b)|e_{a′b} − e|², with the same-right-end tilt C_B → C_T.
  - Bound 3 uses (x_b − x_a)×e = 0, c(a,b)u×e = ∫_a^b u×(T−u), V_u(a,b) ≤ V_u(a′,b) = N(a′,b)², and (CA) c(a,b) ≥ c_Aλ.
- **Third term.** h is non-increasing because ν + γ − 3/2 < 0. Φ is non-increasing. The closed form of ∫x^pĈ agrees
  with direct quadrature (5.29109 both ways).

**Constants rebuilt independently** (`consts.out`, base tuple, C_T = 2.91086):

| | claimed | rebuilt |
|---|---|---|
| c_ρ* | 0.5989 | 0.59890 |
| c_η | 0.9949 | 0.99490 |
| c_R* | 31.82 | 31.824 |
| K_1 | 2.97 | 2.9687 |
| K_2 | 31.3 | 31.325 |
| aD*(K_1) | 1.130 | 1.1302 |
| c_amp* | 1.917 | 1.9174 |
| J_1, (S1) / (S1G) | 198.1 / 10.9 | 198.141 / 10.892 |
| J_2, (S1) / (S1G) | 6140 / 95.7 | 6140.23 / 95.728 |
| B_2η* | 1.074 | 1.0738 |
| C_p^V | 3.823 [12.32] | 3.8230 [12.324] |
| C_p* | 3.823 | 3.8230 |
| B_3′ | 18.5 | 18.492 |
| B_5* | 77.1 | 77.057 |
| X_far*, (S1) / (S1G) | 0.0121 / 0.00088 | 0.012112 / 0.000877 |
| (P4*) | — | 0.01206 ≤ log A_0 = 0.01284 under (S1); 0.00071 under (S1G) |
| (P5*) | — | 0.0618 (S1) / 0.0574 (S1G) ≤ 𝔣 = 0.137 |
| (P3*) | — | 1.15e-4 ≤ ν = 3.11e-4 |

Two printed values differ; both are under F8.

**Simulation** (`sim_far.py`; four smooth and four rough runs).
- **Setup.**
  - The greedy chase runs from the exact touch-down curve at v = 1e-3 and 4e-3 (ε = 1e-3, h = ε/4, about 24 500 nodes, about
    6 150 legs, RK4).
  - The front is cut at U − 1.2K_RR/k_c, so that every pair is good.
  - The synthetic tuple has R = 0.02, K_R = 5, K_f = 4, K_ε = 20, η1 = 0.8, m = 0.15 for the rough runs, with κ and c_A
    measured.
  - Multiscale roughness on scales down to 4h brings the (S2) ratio to 0.80–0.81 at start.
  - 600 far pairs are tracked (λ = R/2 and R).
- **Results** (identical to 4 digits across seeds and with/without roughness):
  - **Lemma (J):** max ∫_{𝒯_3}ρ*^{−1} / J_1 = 0.797 (v = 1e-3) and 0.729 (4e-3). Max ∫ρ*^{−2} / J_2 = 0.495 and 0.428,
    using the (S1G) entry. The (S1) entry is about 9 times looser.
  - **Prop F*(iii):** min ρ*/ρ_G(min(g, U−λ−g)) = 1.0061 and 1.0152. This bound is tight; it is attained by pairs whose arc
    faces the base across the loop.
  - **Prop F*(i):** min ρ*/(c_ρ*g) = 2.02.
  - **Lemma Du* in situ:** max N(t)/(the Duhamel majorant from the measured α, β*) = 0.999999 ≤ 1.
  - **Far-pair N:** max over the far period of N/(Mλ^{1/2+γ}) is 0.0437 against 0.0437 at start. The growth is 0.03%,
    far below the A_0 and forcing allowance.

## F7 Proposition L* — OK

- (log l)′ ≤ v/ρ* uses l′ = v∫sin²φ/ρ ≤ vl/ρ*. Lemma (J) with k = 1 handles 𝒯_3, and Lemma 3.6(i) handles η1R < g ≤ K_RR
  with c_η.
- The B_5* computation is correct: E*(b) divided by l; N/l^{1/2} ≤ Mλ^γ ≤ K_f^{−γ}Mg^γ; l^{1/2}N ≤ κ^{1/2}Mλ^{1+γ}.
- The near part is unchanged.
- **Simulation check.** max over pairs of [log(l_end/l_∘) − v(∫_{𝒯_3}1/ρ* + ∫_{η1R<g≤K_RR}1/ρ*)] ≤ 0. Total far log-growth is
  0.0020 / 0.0080, against the bound v[J_1 + …] = 0.0107 / 0.0461.

## F8 constants — OK with fixes

Two values in the table of Section 3 are misprinted. Neither changes any condition.
- **C_ar.** κ^{3/2}(1+1/K_f)^{3/2+γ}/c_A = 1.02401 · 1.46659 / 0.996095 = **1.5077, not 1.53**. B_3′ = 18.49 is consistent
  with 1.5077, so only the printed entry is wrong. Replace "1.53" by "1.508".
- **B_2U′RJ_2.** With B_2U′ = 0.672713, R = 0.001014 and J_2 as printed, B_2U′RJ_2 = **4.188 (S1) / 0.0653 (S1G), not
  4.13 / 0.064**. Replace both. (P5*) still holds: 0.0618 / 0.0574 ≤ 0.137.

The side conditions (P2★)–(P7★) are correctly derived from F1–F7.

## F9 joint point — not verified; one missing precondition

The vector lives in `reports/R9-far.md` §5.2, which I was not allowed to read. One independent remark follows.

The far claims (Section 3, last bullet, and F8) say "T2* needs only (SC41)–(SC44), already checked". That was checked
at v̄ = 6e-5 only. A joint point v0 = 4.146e-3 needs Theorem 7.12 at v̄ ≥ 4.146e-3, because (A6) requires v0 ≤ v̄. At
v̄ = 4.146e-3 with the current fixed data (ξ1 = 1.007, G_T = 0.05), two side conditions fail (`sc_retune.out`):
- **(SC17):** ρ_cξ1 = 0.9952, which is not > 1.
- **(SC47b):** ξ̄_e + G_T = 0.10026, which is not ≤ η = 0.1.

Both are repaired by ξ1 = 1.05 and G_T = 0.04, and then all SC1–SC48 hold. (SC41)–(SC44) hold with margin: W_xL̂ = 1.156,
Δ0 = 0.0288, c_sep = 0.0288, θ_vΔ0^{1−μ̄} = 0.0326.

Two downstream conditions change with these values:
- c_sep falls from 0.03306 to 0.02880, so (C4) needs c_AK_RR ≤ 0.0288. The base tuple has 0.03227.
- G_T = 0.04 tightens (A3) G_f ≤ G_T and (A4) U_E ≤ G_T.

Requested text for the F8 bullet: "(S1G) uses the touch-down constants W_x, L̂, k_c, c_N, λ0 at the v̄ of the joint point;
Theorem 7.12 must be re-verified at that v̄ (with v̄ = 4.146e-3: ξ1 = 1.007 → 1.05 and G_T = 0.05 → 0.04 are needed for
(SC17), (SC47b)), and (C4), (A3), (A4) re-checked with the new c_sep, G_T."

The joint-point claim should be read as conditional on that re-verification.
