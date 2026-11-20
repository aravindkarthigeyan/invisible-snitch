# Referee report R9-tilt-1: sharper tilt lemma and the near-pair constant D

Object: `referee/R9-tilt-claims.md` (Lemma S, Lemma T, Lemma G′, Lemma O, Lemma P, Prop 4.3′, §§7–9), against the base text
`r9/base_short/` (sec2 Lemma `lem:static`, sec3 Def 3.3, `lem:legs`, `lem:gapint`, `lem:dist`, `lem:tilt`, `lem:local`, sec4
Props 4.2–4.4, sec5, sec8, appA). `reports/R9-tilt.md` and `r9/tilt/` were not read. My own code and logs:
`code/referee/R9tilt_1/` (`constants.py/.out`, `split_sup.py/.out`, `split_cellbound.py/.out`, `lemmaS_tests.py/.out`,
`lemmaT_static.py/.out`, `chain_combinatorics.py/.out`).

**Overall verdict: OK with fixes.** I re-derived every step. I found no gap and no false statement. All constants reproduce:
C_T = 2.91086, C_μ = 9.60815, and D = 544.912 (drop-in). The fixes below are textual or bookkeeping. None of them changes a constant
that binds.

---------------------------------------------------------------------------------------------------------------------
## 1. Verdicts per claim

| # | Claim | Verdict |
|---|---|---|
| 0 | New constants and side conditions (T1)–(T4); two old "extra" conditions removed | OK with fixes (F5, F6) |
| 1 | Lemma S (i) split identity/bound, (ii), (iii) | OK |
| 2 | Lemma T (o) one step | OK (cosmetic F1) |
| 2 | Lemma T (i) chain, C_T for all sub-arc positions | OK with fix (F2: ratio range) |
| 2 | Lemma T (ii) (E-μ′), L² and L¹, capped by N(I)² | OK |
| 3 | Lemma G′ | OK |
| 4 | Lemma O (O1), (O2), (O3) | OK (F7: final-leg remark inherited from the base text) |
| 5 | Lemma P (P1)–(P5) | OK with fix (F3: the step in the (P1) proof for Φ_l) |
| 6 | Prop 4.3′ (6.1 Term I, 6.2 short, 6.3 long drop-in, 6.4 split) | OK |
| 7 | Prop 4.2′ / 4.4 with C_p′, B₃′, B₅′ | OK |
| 8 | Theorem `thm:end`(c), §5 | OK with fix (F4) |
| 9 | Values (C_T, C_μ, D_I′, D_IIs′, D_IIl′, D_IIl″, D, C_p′, B₃′, B₅′, C_T^A) | OK. All reproduced (table in §4) |
| 10 | Sanity checks | Consistent with my own independent tests (§3) |
| — | Coverage of every use of C_A, C_B, C_TL, C_μA, C_1A, k₀ in §§3–4 (and beyond) | OK. Every use is covered (§2) |

---------------------------------------------------------------------------------------------------------------------
## 2. Re-derivations (what I checked, step by step)

### Lemma S (static split tilt). OK
(i) V_J×e_I = ∫_J(T−e_I)×e_I, and |(T−e_I)×e_I| ≤ |T−e_I|. Cauchy–Schwarz gives Z² ≤ l(J)∫_J|T−e_I|². Since V_I×e_I = 0, also
V_J×e_I = −V_{I∖J}×e_I. If J is interior, the complement is two arcs and Cauchy–Schwarz runs over their union, so
Z² ≤ l_c∫_{I∖J}|T−e_I|². Adding Z²/l(J) and Z²/l_c and using ∫_I|T−e_I|² = N(I)² (static(b), c(I) > 0) gives the claim.
Regularity is used only for l_c > 0 when J ≠ I. Piecewise C¹ is fine, because static(b) only uses ∫T ds = x_b − x_a.
(ii) The identity |d|²(1−|d|²/4) = sin²θ = Z²/c(J)² is exact. c(J)|d|² ≤ V_{e_I}(J) ≤ V_{e_I}(I) = N(I)² follows from static(b)
plus additivity and non-negativity. Under N(I)² < 4c(J) the stated bound follows, and it needs |d| < 2, which holds.
(iii) Both identities hold, and the last form is the triangle inequality. The last form also holds when J shares the left end
(L = (β,b)); it is not used that way.

### Lemma T (o). OK
Z² ≤ N(I)² f(l(J)), where f(ℓ) = ℓ(1−ℓ/l(I)) increases in l(I) and l(I) ≤ κλ_I. Maximizing over 0 < ℓ ≤ κλ_J gives κλ_Jρ̃(ρ),
with ρ̃ as stated. Then (J2), and (CA) with λ_J ≤ R ≤ K_RR, give Z/c(J) ≤ s(ρ)Mλ_I^γ. s is continuous at 2 (value κ^{1/2}/c_A) and
increasing. Next, N(I)²/(4c(J)) ≤ (Mλ_I^γ)²ρ/(4c_A) ≤ m²r/(4c_A) < 1. Text: "For pairs J ⊂ I of that family, J ⊂ I" repeats
"J ⊂ I" (F1).

### Lemma T (i). OK with F2
Case A, chain I_k = (α_k, α_k+λ_k), α_k = min(a′, b−λ_k). I checked (1)–(3) by hand. The membership argument "b − λ_k ≥
a + λ_I(1−1/q) ≥ a_j + ε ≥ a_{j+1}" uses a_{j+1} − a_j ≤ l_{t_j}(a_j,a_{j+1}) ≤ ε, which holds for final legs too.
Case B: λ_I < εq/(q−1) and λ_J ≥ ε/2 give ratio < 2q/(q−1) ≤ r_*. The cases are exhaustive: the complement of Case A is
a < a_{j+1} (so a = a_j), a′ ≠ a and λ_I(1−1/q) < ε.
Exact test (`chain_combinatorics.py`, Fraction arithmetic, κ = 4/3 the worst case, 678 107 Case-A and 8 498 Case-B instances):
I_0 = I, every link is a family pair, J ⊂ I_k ⊂ I, nesting, link ratios in [1,q], and the Case-B ratio < 2q/(q−1).
**0 failures.**
Summation: Σ_{k<K} q^{−kγ} < σ_q and ω_q ≤ ω_*, so C_T = ω_*·max(σ_q s(q), s(2q/(q−1))) is correct.
**F2.** In step (4), λ(I_{K−1})/λ_J lies in [1,q], not [1,q): equality q occurs when λ_K = λ_J exactly. This is harmless, because
(o) is applied with r = q.

### Lemma T (ii) (E-μ′). OK
J = (a, a+λ_s) is a family pair, since λ_s ≤ λ (s ≤ b and ε/2 ≤ λ). Then N(J)² + c(J)|e_J−e|² ≤ M²λ_s^{1+2γ} + κλ_sC_T²M²λ^{2γ} ≤
C_μM²λ^{2γ}λ_s. The cap ∫_a^s ≤ N(I)² ≤ M²λ^{1+2γ} holds. The L¹ bound follows by Cauchy–Schwarz with l(a,s) ≤ l(J) ≤ κλ_s.
The linear form of the old (E-μ) still follows, with C_1A := (κC_μ)^{1/2} = 3.124 (old value 6.57). So any reference to the
old (E-μ) remains valid.

### Lemma G′. OK
On 𝒯 every gap value g_i is ≥ ε/κ, so each interval [g_i − ε/κ, g_i] lies in [0,∞). The intervals are disjoint, because distinct
legs have gaps that differ by ≥ ε/κ. Each value is taken on one leg, for a time ≤ d_Lε. On the uses: g > 0 forces a ≥ β⁺, so
g ≥ β⁺ − β ≥ ε/κ. That uses the non-final-leg advance; in the final leg no family pair has a ≥ a_{j+1} = U.

### Lemma O. OK
(O1) I′ = (a′,b) is a family pair contained in [β, max(b,β⁺)]. The case g′ < ε/2 only arises for a′ = β⁺. There
L ⊂ L₀ = (β⁺, β⁺+ε/2) ⊂ I′, and l(L) ≤ κε/2 ≤ κg because g ≥ ε/κ ≥ ε/2. yz/(y+z) is monotone. Hence Y ≤ (1 + κg/(c_Aλ))
κ^{1/2}M(g+λ)^γ(gλ)^{1/2}, as claimed.
(O2) With β⁺ ≤ b, λ_u ≤ min(ε,λ) and min(C_μ min(ξ,1), 1) = min(C_μξ, 1) because C_μ ≥ 1. With β⁺ > b, AM–GM gives
l(J)l_c/l(I₀) ≤ l(I₀)/4, and κε·Mε^{1/2+γ}(κε)^{1/2}/(2c_Aλ) = (κ^{3/2}/(2c_A))ξ^{2+γ}Mλ^{1+γ}.
(O3) g′ ≥ g − ε ≥ (K_f−2)λ ≥ ε/2, and λ(I′) ≤ η₁R(1+1/K_f) ≤ R by (P0). The (iii) last form, (i), T(i) and c(L) ≤ κg′ give C_p′.
**F7 (inherited, not new).** In the final leg (t = t_j = T_stop) the pair I₀ = (β,β⁺) need not be a family pair. There,
however, P = x_β = x_a, so p_a = 0. The base proof (sec4 l. 150) has the same silent point. One sentence would close it.

### Lemma P. OK with F3
The closed forms of Φ_α, Φ_l, Φ_β agree with quadrature to 2·10⁻³¹ at 8 points per profile. The (P3) closed forms are exact
(error ≤ 10⁻³⁰). (P2): max ratio 0.999997. (P4): I re-derived (log P)′ ≤ (1+γ)/(x + c_A/κ), using c_A/κ ≤ 1, and the three
pieces need exactly (T2), (T3), (T4). A grid check (4 000 points) confirms that B is non-increasing on (0,K_f].
**F3.** In (P1), on w = Cz ≤ 1 the text says "C^{−1/2}w(2−log w) − w/C ≤ 2C^{−1/2} − 1/C, since w ↦ w(2−log w) increases".
That step does not follow as written, because −w/C decreases in w. Replace it with: "the whole function has derivative
C^{−1/2}(1−log w) − 1/C ≥ C^{−1/2} − 1/C ≥ 0, so its maximum is at w = 1, namely 2C^{−1/2} − 1/C = 1 − (1−C^{−1/2})² ≤ 1."
The conclusion is unchanged.

### Prop 4.3′. OK
- (F′): u_y − a ≤ min(λ, y−g), ε/2 ≤ min(λ,y) because y ≥ c₆ε ≥ 2ε, and C_μ ≥ 1. Checked.
- 6.1: λ_y ≥ ε/2, so λ_{a+λ_y} = λ_y ≤ min(λ, c₆y). The substitution z = C_μc₆y gives the factor C_μc₆ h₁(C_μc₆ρ̄).
  zh₁ ≤ λ, and ∫_0^{C_μK_fλ}h₁ = λ(2 + log K_f + log C_μ). Total T_I + c₆χ log C_μ. Checked.
- 6.2: Tonelli with Φ = c₆²/max(w,c₆ε)² ≥ D⁻², the inner bounds F(u_y)²/2 and F(u_y), and scaling y = λη. Checked.
  The II_α time integral uses (P1) and (P3). The g = 0 leg: both subcases are checked, including F(b)² ≤ lN² ≤ κM²λ^{2+2γ}
  and ξ ≤ 2. The g > 0 part uses (O1), Φ_β(y₀/λ) ≤ Φ_β(x), (P4) and Lemma G′. Checked.
- 6.3: |q| ≤ ρ/max(ρ,ε)² ≤ 1/D, w_s < (K_f+1)R ≤ K_RR, profile Φ_l, and 1/(Mλ^γ) < (K_f+1)^γ/m. Checked.
- 6.4: on 𝒯₁, g + λ ≤ R gives w_s < R and makes (O1) available. The cut indicator keeps h non-increasing, μ − 1 < K_f, and
  the g = 0 leg lies in 𝒯₁. On 𝒯₂ the long-case bound holds unconditionally, gapint(i) with g₀ = (μ−1)λ applies, and
  1/(Mλ^γ) = μ^γ/m. Checked. Both 𝒯₁ and 𝒯₂ carry their own boundary term d_L/c₆, which is correct.

### Coverage of the old constants (every occurrence, `grep`)
| Location | Old use | Covered by |
|---|---|---|
| sec3 l.70–71 (Def 3.3) | c_t, C_A, C_B, C_TL, C_μA, C_1A | C_T, C_μ. c_t is no longer used anywhere: C_p′ has no c_t(r_f), and r_f is also unused |
| sec3 l.76 | r_f, C_p, B₃ | C_p′, B₃′ ((O3)) |
| sec3 l.77–81 | T_a, T_b, k₀, D_I, D_IIs, D_IIl | D_I′, D_IIs′, D_IIl′(″). T_a, T_b, k₀ unused (delete). Ψ_I, T_I still used (T_I in D_I′ and L_J) |
| sec3 l.82 | B₅ | B₅′ |
| sec3 l.88 | θ̄ | new D |
| sec3 l.145–146 | thm:end(c) with C_TL/C_A/C_B | C_T for all J ⊂ I (Lemma T(i) plus the unchanged §4 completion, l.245–247) |
| sec3 l.237–269 | lem:tilt (i), (ii), eq:Emu | Lemma T (i), (ii) (keep the label `eq:Emu`, since sec4 l.225 cites it) |
| sec4 l.39, 74–84 | C_p via c_t(r_f), C_B (Prop far) | (O3) |
| sec4 l.102–105, (P5) | B₃ | B₃′ |
| sec4 l.113–199 | C_μA, C_1A, k₀, C_A (β⁺ > b), C_A + C_B, C_TL, and the inequality κ ≤ C_TL²(4−κ²) with C_TL ≥ c_t(3) ≥ √3 | Prop 4.3′ (the whole proof is replaced) |
| sec4 l.217–222 (Prop length) | C_p, B₅ | C_p′, B₅′. The near part uses (J1) only (κT_I), unchanged |
| sec4 l.246 | lem:tilt(i) | Lemma T(i) |
| sec5 l.19–28, 51, 73, 101, 107; sec8 l.8 | C_A^A, C_B^A, C₃ | see F4 |
| appA l.18, appA_tables | κ ≤ C_TL²(4−κ²) and the table entries | see F5 |

Removed conditions: "κ ≤ C_TL²(4−κ²)" and "c_t(3) ≥ √3" occur only at sec4 l.161–162 (and in the appA/verify "extra" list).
Prop 4.3′ no longer uses them. **Confirmed.** The old (P0)–(P7) conditions all remain. The changed constants enter
(P5) (B₃′ < B₃), (P6) (θ̄ 0.897 → 0.084), and (P7) (B₅′ < B₅). All three move in the safe direction.

Old constants reproduced from the INPUTS line: D_I 485.642, D_IIs 6837.12, D_IIl 2960.78, D = 7322.76, θ̄ = 0.897490, C_p 12.6407,
B₃ 413.253, B₅ 5162.04. These match verify_constants.out, which confirms my reading of the inputs.

---------------------------------------------------------------------------------------------------------------------
## 3. Numerical tests of the identity and the lemma

**Lemma S at high precision** (`lemmaS_tests.py`, mpmath at 50 digits). Piecewise-linear curves are computed exactly. Smooth
Fourier curves use arclength by mp.quad. Large-tilt classes are spirals and hairpins (a reversal of π − 0.05). J is a left,
right or interior sub-arc. Pairs where I is straight to round-off are excluded: there every quantity is pure noise, as found
on a first run that reported spurious ratios like 1.5 and 22 for exactly straight I.
In total I tested 6 483 pairs from 24 polygons (gentle, rough, spiral, hairpin) and 12 smooth curves (scales 0.05 to 3).
- The identities hold to round-off: the (ii) identity |d|²(1−|d|²/4) = Z²/c(J)² has error ≤ 1.7·10⁻⁵⁰, |V_I×e_J| = (c(I)/c(J))Z
  has error ≤ 4.6·10⁻⁵⁰, and |V_L×e_J| = |V_I×e_J| has error ≤ 5.3·10⁻⁵⁰.
- Worst ratios: S(i) 0.9903; S(ii) 0.99999999629, on the 4 535 pairs with N(I)² < 4c(J); c(J)|d|²/V_{e_I}(J) = 1.0, attained for
  straight J; V_{e_I}(J)/N(I)² 0.99999998; S(iii) (1+c(L)/c(J))-form 0.9999999995; last form 0.9999999995 (right end) and
  0.999999998 (left end). **0 violations.**
- Hypothesis of (ii): in 1 948 pairs (spirals, hairpins) N(I)² ≥ 4c(J). There the plain Z/c(J) underestimates |d| by up to a
  factor 1 289 (a near-reversed sub-chord). So the hypothesis of (ii) is genuinely needed. Lemma T supplies it through (T1).

**Lemma T, O static adversarial test** (`lemmaT_static.py`). Curves on a 48-label grid with stretch w ≥ 1, ε = 4, R = 48, base
0 and next base from the chase rule. κ, M and c_A are taken as the exact sup/inf over the family. So (J1), (J2) and (CA) hold
by construction, and every claimed inequality must then hold. Curve classes: smooth, rough self-similar (amplitude ∝ scale^γ),
single corner, kink at the base. There were 17 random curves satisfying (T1), plus hill-climbing on each target ratio.
Worst LHS/RHS:
T(o) 0.954, T(i) 0.448, T(ii)-L² 1.000000000001 (equality up to round-off: s = b and I is the M-extremal pair), T(ii)-L¹ 0.9987,
(O1) 0.949, (O3) 0.331. The empirical sup of |e_J − e_I|/(Mλ_I^γ) was 1.55, against C_T ≈ 2.9–3. **No violation.** The one-step
bound (o) is nearly sharp (0.95); the chain constant has about a factor 2 of slack.

---------------------------------------------------------------------------------------------------------------------
## 4. Constants (independent recomputation, `constants.py` → `constants.out`, mpmath at 30 digits)

Inputs as printed in the INPUTS line of `r9/base_short/verify_constants.out` (main tuple p; p_A uses γ_D = 0.614666).

| constant | claims | referee (p) | referee (p_A) |
|---|---|---|---|
| s(q), s(2q/(q−1)), r_* | — | 1.04096, 1.72017, 3.88984 | same |
| ω_* | — | 1.0015409 | same |
| C_T | 2.9109 (p), 2.9094 (p_A) | **2.910857** | 2.909356 |
| C_μ | 9.6082 | 9.608152 | 9.599274 |
| D_I′ | 16.034 | 16.0343 | 16.0324 |
| Π_α | 19.37 | 19.3667 | 19.3628 |
| S₀ | ≤ 0.22896 | 0.228706 (argmax ξ ≈ 0.104, refined grid) | 0.228698 |
| Π₀ | 1.876 | 1.87375 (with S₀ = 0.228706) | 1.87369 |
| ∫₀^{K_f}B | ≤ 8.2305 (quad 8.2256) | quad 8.225584 | 8.227354 |
| Π_β | 68.51 | 68.465 (quad) | 68.480 |
| D_IIs′ | 89.75 | 89.706 (quad values) | 89.716 |
| T_l | — | 4.860733 | 4.860581 |
| D_IIl′ | 528.88 | **528.8775** | 529.2405 |
| D (drop-in) | 544.91 | **544.9118** | 545.2729 |
| D_IIl″ | 182.20 | sup on a fine grid 181.500 (at μ ≈ 1.019); cell-wise monotone upper bound 181.741 | 181.47 (coarse) |
| D (split) | 198.23 | 197.53 (grid), ≤ 197.78 (cell bound) | ≈ 197.5 |
| Λ(1) | 175.3 | 175.296 | 175.290 |
| C_p′, B₃′, B₅′ | 3.855, 126.03, 493.5 | 3.85490, 126.026, 493.545 | 3.85347, 125.979, 493.175 |
| θ̄ (drop-in) | — | 0.084148 | 0.084191 |
| (T1) m²r_*/(4c_A) | 0.0031 | 0.0030747 < 1 | same |
| (T2) C_μ vs (1+2γ)κ/c_A | 9.61 ≥ 2.27 | 9.6082 ≥ 2.2729 | 9.5993 ≥ 2.2737 |
| (T3) γ vs c_A/κ | 0.614 ≤ 0.980 | 0.614267 ≤ 0.980466 | 0.614666 ≤ 0.980466 |
| (T4) K_f(2γ−1) vs 3c_A/κ | 1.15 ≤ 2.94 | 1.15087 ≤ 2.94140 | 1.15489 ≤ 2.94140 |
| q = 2.42: C_T, C_μ, D | 2.8822, 9.4397, 544.56 | 2.88224, 9.43975, 544.559 | — |
| G1 closed-form bound ∫₀^{1/C}B | Π_β = 70.31 | 2.08542 (vs quad 1.86603), Π_β = 70.30 | — |

Every claimed value is either reproduced (to 4–5 digits) or is an upper bound slightly above my quadrature or grid value. That
holds for S₀, ∫B, Π₀, Π_β, D_IIs′ and D_IIl″, which is consistent with the claimed rigorous upper sums. D_IIs′ and D_IIl″ do not
bind the drop-in D. For D_IIl″, a uniform grid of 800 cells is too coarse near μ = 1: S(μ) has slope ≈ 480 there, because
B ~ C^{1/2}x^{−1/2} and Φ_α ~ C log. My uniform-cell bound was 185.2. A geometric mesh starting at 10⁻⁵ gives 181.74 ≤ 182.20.
A rigorous evaluation of the sup must refine near μ = 1. I could not see their script, so I only flag this; my mesh confirms
the printed number is safe.

---------------------------------------------------------------------------------------------------------------------
## 5. Fixes (exact text)

**F1** (Lemma T(o), statement). Replace "For pairs J ⊂ I of that family, J ⊂ I, with λ_I ≤ rλ_J" by "For pairs J ⊂ I of that
family with λ_I ≤ rλ_J".

**F2** (Lemma T(i), step (4)). Replace "λ(I_{K−1})/λ_J ∈ [1, q)" by "λ(I_{K−1})/λ_J ∈ [1, q]".

**F3** (Lemma P (P1)). Replace "and C^{−1/2}w(2 − log w) − w/C ≤ 2C^{−1/2} − 1/C ≤ 1, since w ↦ w(2−log w) increases on (0,1]" by
"and C^{−1/2}w(2 − log w) − w/C ≤ 2C^{−1/2} − 1/C = 1 − (1 − C^{−1/2})² ≤ 1, since the left side has derivative
C^{−1/2}(1 − log w) − 1/C ≥ C^{−1/2} − 1/C ≥ 0 on (0,1]".

**F4** (§5, §8). Two options.
(a) Minimal and safe: leave §5 and its numbers unchanged. Its statements stay true, because the new `thm:end`(c) gives
|e_J − e_I| ≤ C_T^A m(λ_I/R)^{γ_D} with C_T^A = 2.909 ≤ C_A^A = 6.392 ≤ C_B^A. In that case §8 l.8 must keep a definition of
C_A^A, C_B^A, since Def 3.3 will no longer define them. Text for sec8 l.8: "C_A^A := σ_q c_t(q_c) and C_B^A := C_A^A + c_t(3),
computed for p_A, with c_t(r) := (κ^{1/2}r^{1/2+γ_D} + m/2)/c_A. These are upper bounds for C_T^A, so Theorem `thm:end`(c)
gives the tilt bounds used in §5 with these constants." This is mere bookkeeping.
(b) Replace them by C_T^A as the claims propose. Then C₃ := 2C_T^A suffices: both chains in Step 3 have two links, each
≤ C_T^Aκ_W. The claimed 3C_T^A is valid but loose. Option (b) changes ω₀, θ_h1, ϑ_h, x_c, L_h, Θ_0, Θ_b, K_w and Θ_p, which
feed (A3), (A4), (D3) and later sections. Not all of these are monotone in the tilt constants (x_c = (ω₀/ϑ_h)^{1/γ_D}), so
verify_constants.py must be rerun. I did not do this. Option (a) needs no rerun.

**F5** (Appendix A / verify_constants.py). Add the conditions (T1)–(T4) for p and p_A. Drop the two "extra" conditions
κ ≤ C_TL²(4−κ²) and c_t(3) ≥ √3 (four lines), and remove the first of these from the example list in appA l.18. Update the
counts "201" and "24 further". Print C_T, C_μ, C_p′, B₃′, B₅′, D_I′, Π_α, Π₀, Π_β, T_l, D_IIl′ (and D_IIl″ if used) in
Table core. Delete T_a, T_b, k₀, C_1A, r_f, c_t from the main tuple tables, unless F4(a) keeps c_t for p_A.

**F6** (Def 3.3 text). Add S₀, ∫B and D_IIl″ with an explicit statement of how the script bounds them from above. Use monotone
cells (B is non-increasing by (P4)). Near μ = 1, use a geometric mesh, or use the G1 closed form on [0,1/C]. Alternatively, state θ̄
with the drop-in D_IIl′ only. That needs only closed forms: D_I′, Π_α, D_IIl′ are explicit, and Π₀ and Π_β can use the G1 bound
plus any upper bound for S₀. This is simplest, because D_IIl′ binds anyway.

**F7** (Lemma O (O2), or Prop 4.3′ 6.2, first line of "II_β, g = 0"). Add: "If the leg is final, then τ = T_stop = t_j and
P = x_β = x_a, so p_a = 0; we may therefore assume the leg is non-final, so β⁺ − β ∈ [ε/κ, ε]."

Editorial (no verdict impact): after the rewrite, Lemma `lem:int` is used only for h₁. The parts h₃, G₃ and the function H of the
old proof can be deleted.

---------------------------------------------------------------------------------------------------------------------
## 6. Final assessment
Lemma S, Lemma T (one constant C_T for every sub-arc position), Lemma G′, Lemma O, Lemma P and Prop 4.3′ are correct. The new
L²/L¹ bounds (E-μ′) hold with the cap N(I)² and with every auxiliary pair a family pair. Every use of C_A, C_B, C_TL, C_μA,
C_1A and k₀ in §§3–4 is covered. §5 and §8 need F4. (T1)–(T4) hold for p and p_A with large slack, and the two old conditions are
indeed no longer used. D drops from 7322.76 to 544.91 (drop-in) or about 197.8 (split), and θ̄ from 0.897 to 0.084.
