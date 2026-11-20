# Audit E — end-to-end audit of the short paper, version 2

Object: `short/snitch.tex` with `sec1`–`sec8`, `sec7a`, `sec7b`, `appA` (+ `appA_tables.tex`), `short/snitch.pdf` (49 pp),
`short/verify_constants.py` (218 conditions), `short/CHANGES_v2.md`.
Claim: v ≤ v0 = 5.8·10⁻³, every direction seen by 13.1 d for every ε ∈ (0,d); exact capture (Corollary 1.2) by compactness.
The paper was not edited. New audit code is in `code/audit/E/`.

## Verdict: **CHAIN CLOSED**

Every new or replaced statement gets exactly what it needs at every place where it is used. All renames are applied
consistently, and no stale symbol is left. The constants are consistent from Def 3.3 through Def 4.3, Props 4.2, 4.10
and 4.12, §5 (C₃ = 2C_T^A), the touch-down row and Appendix A.

The first-failure argument of Lemma 3.10 closes with the new propositions. (S1G) is proved in §7–§8 (Lemma 7.13 and
Lemma 8.2) before the only places where the end theorem is applied (Prop 8.3 Steps 1 and 6). In §3–§4 it is a
hypothesis of Setting (H), so it creates no forward dependency.

I independently recomputed every derived constant and checked every stated side condition at the printed values,
including a new certified interval/outward-rounded bound for D′. Every condition holds:
- **D′(p) ≤ 63.04545** (printed value 63.068);
- **D′(p_A) ≤ 64.47140** (printed value 64.6357).

So (P6) holds with the printed values and also with the audit's independent bounds. The audit found no mathematical gap.

There are 3 editorial suggestions, all optional, in §6 below.

---------------------------------------------------------------------------------------------------------------------
## 1. Interface table (new or replaced statement → every use)

| statement (v2) | used in | what the use needs | provided? |
|---|---|---|---|
| **Lemma 2.9** (split tilt) (i) Z² ≤ N(I)² l(J) l_c/l(I); (ii) tilt from Z when N(I)² < 4c(J); (iii) \|v_I×e_J\| = (c(I)/c(J))Z; for J sharing the right end of I: \|v_L×e_J\| ≤ (1+c(L)/c(J))Z, ≤ Z + c(L)\|e_I−e_J\| | Lemma 3.8(o) | (i), (ii) with J ⊊ I, c(J) > 0 (by (CA)), N(I)²/(4c(J)) ≤ m²r/(4c_A) < 1 | yes; J ≠ I is assumed explicitly; (P8) gives r < 4c_A/m² |
| | Prop 4.2 bound (1) | (iii) last form + (i); J = (a,b) shares the right end of I′ = (a′,b); J ≠ I′ | yes: g′ ≥ g − ε ≥ (K_f−1)λ > 0 |
| | Lemma 4.7 route 2, (ii) | (i) and (iii) middle form; g′ > 0 | yes, as stated in (i), (ii) |
| | Lemma 4.7(iii)(c) | (iii) first form + (i), with J sharing the **left** end of I₀; the first form needs no shared end | yes |
| **Lemma 2.10(v)** (far inequality with the arc distance ρ̲ = min_s ρ_s ≥ ρ_m) | Lemma 2.11 | ρ̲ ≥ ε, c > 0 | yes |
| | Prop 4.12 "Far, g ≤ η₁R" | length form; ρ̲ ≥ ε | yes, by Prop 4.2(i) and (P2) |
| **Lemma 2.11** (Duhamel; α, β with π-factors; α*_D(K) = 1+1/(πK)+2/(πK)²) | Prop 4.2 | ρ̲ ≥ ε on [t∘,t]; c(t∘) > 0; ρ̲ ≥ K₁l (g ≤ K_RR) and ρ̲ ≥ K₂l (g > K_RR) | yes: (P2) gives c_ρ\*g ≥ ε and c_R\*R ≥ ε; (J1) gives the K-bounds |
| | Thm 5.2(v), phase 2 | ρ̲ ≥ ζ(g̃+τ) ≥ 4l, ρ̲ ≥ ζz₀ ≥ ε; c > 0 | yes: k_D ≥ 4(1+δ_t)/ζ since c_k ≥ 1; (D0); c ≥ (1−ω_T²/2)l |
| | Thm 5.2 constants | η_N = α*_D(4)v0/ζ; c_β carries 1/π, matching β = 2vl^{3/2}\|p_a\|/(πρ̲³) | consistent (eq. 8.1, eq. 5.3) |
| **Def 3.3** (new tilt/far constants; (P0) K_ε ≥ 2; (P2) c_η > 0; (P3)–(P5), (P7) new forms; (P8) m²r\* < 4c_A; θ̄ = f_F² + 2v0D′) | Lemma 3.5(i), Lemma 4.7 | K_ε ≥ 2 (ε/2 ≤ R; R/2 ≥ ε) | yes |
| | Lemma 3.8 | (P8) for r = q and r = 2q/(q−1) ≤ r\* | yes |
| | Prop 4.2 | K₁, K₂, c\*_amp, B′_2U, B\*_2η, C′_p, C_p^V, Ĉ, B′₃; (P3), (P4), (P5) | re-derived term by term; matches |
| | Prop 4.12 | J₁, X\*_far, B\*₅ (with C_p\* ≥ Ĉ), I₅, T_I = d_L(κc₆+2)+c₆χ_gΨ_I; (P7)/(PT) | re-derived; matches |
| | Prop 4.10, Lemma 3.10 | θ̄ = f_F² + 2v0D′, (P6) | yes |
| **Setting (H)**: datum 𝒞, hypothesis (S1G) | Lemma 3.7(iii), Thm 3.4(d), locality principle, Prop 4.2(iii) and its claim | (S1G) for the pairs (β(τ), s), s ∈ [a,b], with λ = s−β > K_RR; 𝒞 non-decreasing | yes; the min(w, β+U−s) ≥ min(g, U−λ−g) step is checked |
| **Thm 3.4(c)** \|e_J−e_I\| ≤ C_T m(λ_I/R)^γ | Lemma 5.1 Step 1, Step 3(α) | J ⊂ I family pairs; C₃ := 2C_T^A covers both chains I⊂K₂⊃K₁ and I⊂K₄⊃K₃ | yes (option F4(b)) |
| **Thm 3.4(d)** (S1G) clause | not used outside §4 (Lemma 5.1 uses only the first form) | — | — |
| **Lemma 3.6(iv)** | claim in the proof of Prop 4.2 | g ∈ (g₀,Y] on 𝒯₃ (g ≤ a ≤ U−λ = Y, g > K_RR); H unimodal and ≤ (c_R\*R)^{-k} | yes |
| **Lemma 3.7(iii)** | Prop 4.2(iii) | the hypothesis of Lemma 3.7 (U−s ≥ W_e or a_j ≥ W_e) | yes, by Lemma 3.9(ii) |
| **Lemma 3.8** (o), (i), (ii) (C_T, C_μ; (E-μ) with the L¹ form) | Lemma 4.5 (budgets) | (ii) with λ_s = max(s−a, ε/2) | yes |
| | Prop 4.2 (1)–(3), Lemma 4.7 | (i) for J ⊂ I′, L ⊂ I′, J ⊂ I₀ (all family pairs of the leg, λ ≤ R) | yes |
| **Def 4.3** (D′ with C_T, C_μ, 2C_T, C₁ = (κC_μ)^{1/2}) | Lemmas 4.6–4.9, Prop 4.10 | the entries of 𝔭 equal routes 1/2/3 of Lemma 4.7; 𝔭_L equals (ii); P₀ equals (iii)(a)–(c); H_r, S_r, L_r, H₀ equal the one-leg bound; k\*, sum and integral form equal Lemma 4.9 | re-derived symbol by symbol; matches |
| **Lemma 4.7(iii)** final-leg sentence | Lemma 4.8, Prop 4.10 (leg with g = 0) | ϖ ≡ 0 on a final leg | yes |
| **Lemma 4.11** (63.068 / 64.6357) | (P6) in (A1), (A2) | certified bounds ≤ printed values | yes: the script gives 63.067903 and 64.635630; the audit gives 63.045443 and 64.471393 |
| **Prop 4.12** (length; L\*_J) | Lemma 3.10 (Imp), (PT), (P7) | l ≤ (1+δ)L\*_J λ < κλ | yes |
| **§4.4** (completion) | Lemma 3.10 | (Imp) at every t ≤ t\*, with strict (P6), (P7), (PT) | yes; first-failure argument unchanged |
| **§5**: δ0 = 0.251113R, C_T^A, C₃ = 2C_T^A, c_β with 1/π, ρ̲ in Thm 5.2(v) | Prop 8.3 Steps 3–5, (A3)–(A5) | (A3): ρ\* ≥ ε\*, δ0 ≤ R/2, ε\* ≤ δ0, … | all hold |
| **Def 7.1 / Thm 7.12 at the new row** (v̄ = 5.8e-3, η = 0.11639, ξ₁ = 1.16171, λ₀ = 0.0337254, G_T = 0.030573) | Lemmas 8.1, 8.2; Prop 8.3 | (T0)–(T5) with the printed constants, rounded on the safe side | yes: 120/120 constants agree with the script to 10⁻²²; (SC1)–(SC48) hold |
| **Lemma 7.13** (global chords; W_xL̂ ≤ 1.22122) | Lemma 8.2 (λ > λ₀) | λ > λ₀ ⇒ Δ > Δ₀; (SC41)–(SC43); λ₀ < 1; arc-bound reuse; d_c ≥ a+Ū−b ≥ y | yes |
| **Lemma 8.2** ((S1G) at touch-down, any Ū ≤ U) | Prop 8.3 Step 1 (Ū = U_A), Step 6 (Ū = U) | λ ≤ λ₀ branch: c ≥ φ(λ) ≥ c₀′λ (needs λ > K_RR ≥ ε/2, (T1), a′ ≤ 1−μ̄_T); λ > λ₀ branch: Lemma 7.13; printed κ_c ≤ exact, printed W_xL̂ ≥ exact; (A7) | yes |
| **eq. (8.1)** c₀′, 𝒞, W_e = c_AK_RR/κ_c | Steps 1 and 6; J_k^𝒞 | κ_cW_e = c_AK_RR ≤ c_sep (C4); 𝒞 ≥ 0, non-decreasing | yes. At these numbers 𝒞(y) = 2 sin(½min(π, y/W_xL̂)), because 1/W_xL̂ = 0.819 < κ_c < c₀′ |
| **(A1)–(A7)** | Prop 8.3, Thm 1.1 | — | all hold (§3 below) |

**Renames.** I searched for ρ\*/ρ_m, 𝒢, L_J, (T1), C_A, C_B, C_TL, c_t, T_α, D_I, and old v0/T0 values.
- ρ_\* now appears only as the heading constant of §5.
- ρ_m appears only in the remark of Lemma 2.10(v) (ρ̲ ≥ ρ_m).
- 𝒢 (`\Ghost`) appears only in Def 7.9 and (T0).
- Every (T1)/(T2) is Thm 7.12's.
- `\LJ` prints L\*_J everywhere.
- The deleted macros are gone.

**Statements of v0 and T0.** The abstract, Thm 1.1, Cor 1.2, Thm 7.12, (A6), the proofs in §8.3, Appendix A and the tables
all say v0 = 5.8·10⁻³ and 13.1 (T♯ = 13.0834 ≤ 13.1). The proof of Cor 1.2 uses T̄ = 13.1.

## 2. Touch-down row (task 2)

At the printed row, with my independent transcription of Def 7.1, all of (SC1)–(SC48) hold. The two conditions the
earlier referee flagged at v̄ ≈ 4e-3 are comfortable at the row the paper actually uses:
- (SC17): ρ_c ξ₁ = 1.14222 > 1 (slack 0.125);
- (SC47b): ξ̄_e + G_T = 0.081998 ≤ η = 0.11639 (slack 0.295).

Lemma 7.13's preconditions hold:
- λ₀ < 1;
- 8/λ₀ = 237.2 ≥ 1;
- W_xL̂ = 1.2212199 ≤ 2 (SC41);
- Δ₀ = 0.0276162 ≤ η (SC42);
- c_sep = 0.0276153 > 2ε̄ (SC43).

The printed W_xL̂ = 1.22122 is an upper bound (exact value 1.22121991). The 13 printed touch-down constants are each on the
safe side of the exact value. The smallest margin is 7.6·10⁻⁸ (W_xL̂).

The later constraints on the touch-down data also hold:
- G_f = 0.01386 ≤ G_T;
- U_E = 0.01491 ≤ G_T;
- K_RR = 0.01288 < λ₀;
- U_A = 0.01526 ≤ 1 − W_e.

## 3. Constants check (task 3)

Code:
- `code/audit/E/audit_E_constants.py` (50 digits, written from the TeX only). Output in `audit_E_constants.out`, values in
  `audit_E_values.json`.
- `code/audit/E/audit_E_Dprime.py` (certified D′). Output in `Dprime_E.json` and `Dprime_E.out`.
- `code/audit/E/audit_E_Dprime_direct.py` (a non-rigorous direct evaluation of 𝒟(θ,r), used only for validation).

Result: **250 conditions, 0 failures.** They are:
- the 52 (SC) inequalities;
- 23 facts that §6–7 use in passing;
- 14 printed-constant checks;
- (P0)–(P8) for p and p_A (2×36);
- 11 facts that §3–4 use in passing, ×2;
- (C1)–(C6) ×2;
- (A2)–(A7) (37);
- 14 facts that §5/§8 use in passing;
- the 4 D′ / (P6) checks with the audit bounds.

Comparison with `verify_constants.py`:
- **Touch-down:** all 120 listed constants of Def 7.1 agree to 10⁻²².
- **Tuple, assembly and heading/departure constants:** they agree to all printed digits, for example:
  - C_T = 3.8325474581 (p), 3.6369518582 (p_A);
  - C_μ = 19.9436553 (p), 18.0594021 (p_A);
  - B′₃ = 12.59888 (p), 13.91851 (p_A);
  - B\*₅ = 83.62400 (p);
  - TS = 0.0385065278;
  - K_w = 2.42299697;
  - δ_t = 0.0141525954;
  - T♯ = 13.0833680326.

  The closed form of the B′₃ integral in Def 3.3 agrees with quadrature to 25 digits.
- **J_k(U_max)** is the only difference. The audit uses adaptive quadrature at 50 digits:

  | | script | audit (quadrature) |
  |---|---|---|
  | J₁ | 19.745314 | 19.739229 |
  | J₂ | 392.25649 | 392.14403 |

  This difference is expected: the script bounds the sine piece from above by left Riemann sums, as Appendix A says.
  Because of it, the script's (P4)[p], (P5)[p], (P7)[p] and (PT) are slightly conservative:

  | condition | script | audit (exact) | bound |
  |---|---|---|---|
  | (P4)[p] | 0.12212812 | 0.12209111 | ≤ log A₀ = 0.12212825 |
  | (P5)[p] | 0.50022495 | 0.50021724 | ≤ 0.500225 |
  | L\*_J | 1.2694465 | 1.2694057 | — |
  | (PT) | 1.2874124 | 1.2873711 | < κ |

  Every condition holds either way. For p_A (U_0 = U_A) the J_k values agree exactly: the only nonempty integral is the
  constant piece.

**Certified D′ (independent).** The construction follows Def 4.3 and the cell scheme of Lemma 4.11:
- Scalars (C_T, C_μ, c₆, P₀, r^γ, closed forms) are computed in python-flint arb balls at 200 bits.
- Arrays are float64, with a `nextafter` after each operation (4 ulps after log and pow).
- Stieltjes upper sums are written in Abel form, so they are monotone in the kernel and in the integrator.
- Sums are inflated by 1+10⁻⁹.
- θ-cells use ratio 1.03, with adaptive 4-way refinement of the cells above (printed − 0.02).
- r-cells have width 0.05, plus the regime r ≥ K_f+1.
- The bottom cell θ ≤ 10⁻⁷ uses my own closed-form majorants on x ≤ 10⁻⁶.

Results:
- **D′(p) ≤ 63.0454428.** The worst cell is θ ∈ [0.02464, 0.02538], r ∈ [3.377, 3.427].
- **D′(p_A) ≤ 64.4713928.** The worst cell is θ ∈ [0.03215, 0.03311], r ∈ [4.407, 4.457]. The first pass gave 64.64374 at
  θ ∈ [1.7386, 1.7907]; refining that cell brings it below 64.47.
- Both bounds are ≤ the printed values. With them, θ̄(p) = 0.981552 and θ̄(p_A) = 0.998093 < 1.

Validation:
- The direct 𝒟 values must not exceed the certified bound of any small cell containing them. I checked 14 (θ, r) points for
  p and p_A, at θ ∈ {10⁻⁵, 0.002, 0.025, 0.0326, 0.05, 0.3, 1.76}. At every point the direct value is below the certified
  sup over a cell of ratio 1.001 (dr = 0.01). For example, at p_A, θ = 0.0326 the direct value is 61.81 and the bound is
  62.24; at θ = 1.76 they are 61.76 and 62.18. So the implementation dominates the definition, and the gap shrinks as the
  cell shrinks.
- Direct values near the worst cells: about 60.5 for p and about 61.8 for p_A.

So the true sup is roughly 61.8 for p_A and 60.5 for p. The printed certified values (63.068 and 64.6357) are about 4%
above these, and about 2.5 of D′ is available in principle. Certifying D′ more finely would gain about 2v0·2.5 ≈ 0.03 in
θ̄(p_A).

I also reviewed the script's own D′ code (`Cell`, `ust`, `pfrak`, `pstar`, `_crude`):
- The upper RS sum in standard form is valid even where the computed kernel is not exactly monotone. The chain is
  integral ≤ S(ψ_θ, Φ_θ) ≤ S(ψ_θ, Φ_{θh}) ≤ S(ψ^up, Φ_{θh}), using Φ_θ ≤ Φ_{θh} pointwise.
- The bottom-cell bound T_cr = κx₁H(x₁) is valid because y·H^maj(y) is increasing.
- 𝔭\* handles y < θ/2 (where the chord entry is absent) correctly.

I found no rigour defect.

## 4. Side conditions: paper vs script

**Stated in the paper but not checked by the script as a separate line:** none that matters. Each item below is implied by
a checked condition or holds trivially:
- c₆ ≥ 2 and K_R ≥ 4 (§3, after Def 3.3): implied by (P0).
- p̂ ∈ (−3/2,−1) (Def 3.3): implied by (P0).
- d₁/R_L ≤ 1 (arcsin in Def 7.1): implied by (SC8).
- ξ₁ε̄ ≤ η/2 (Lemma 7.9): derived from (SC40).
- G_f ≤ U_A (Lemma 5.1): implied by (A3).
- k_D ≥ 4(1+δ_t)/ζ (Thm 5.2(v)): implied by c_k ≥ 1.
- U_A − W_e = δ0+R (Prop 8.3 Step 2): an identity.
- κ_cW_e = c_AK_RR (Step 6): an identity.
- The arguments of cot in (SC7) and of cos in κ_c lie in range: trivially.
- The monotonicity of 𝔭 in x (on x ≥ θ_l/κ ≥ θ_h/2, which needs θ_h/θ_l < 2/κ = 1.55): a property of the D′ scheme,
  not a stated condition; see fix E1.

The audit script checks all of these explicitly (groups `td-text`, `core-text`, `asm-text`).

**Checked by the script with no corresponding stated condition** (harmless; Appendix A says so):
- the 6 tilt inequalities (T2)–(T4) (C_μ ≥ (1+2γ)κ/c_A, γ ≤ c_A/κ, K_f(2γ−1) ≤ 3c_A/κ), for p and p_A;
- the 4 touch-down extras λ₀ ≤ ¼, κ_c ≥ ½, c_Nλ₀^{1−μ̄_T} ≤ 1, v̄ ≤ 2·10⁻²;
- in the "elementary" group, v̄² ≤ ½ and η ≤ 1, for which I found no use in the text (the others correspond to statements
  in the proofs).

## 5. Task 4 (end statements)

- **Every direction:**
  - (T0) covers directions seen during [0,t_td] and the ghost set.
  - Prop 8.3 Step 6 with Thm 3.4(b) covers true labels by T_stop.
  - In Lemma 3.2(2), "seen" means \|S−P\| ≤ ε at some time. Direction 0 is caught at 1/(1−v).
- **Path fixed in advance:**
  - Design T depends only on (v,ε); the label α₀ and n̂ come from run 1.
  - Each leg is determined by x⁰ and the earlier path (Lemma 3.2(4)).
  - Thm 1.1 scales with ε′ = min(ε, ε\*d).
- **Speed ≤ 1:** the path is unit-speed runs, then legs (Lemma 3.2(0)), then constant.
- **T₀ = 13.1:** T_stop ≤ t_td + κU/(1−v) ≤ T₂ + κU_max/(1−v0) = 13.08337 ≤ 13.1 (A6).
- **Corollary:** Lemma 2.13 is applied with D_N = dyadic directions, ε_N = 2^{−N}ε\* and T̄ = 13.1, which does not depend
  on N. The scaling to d = 1 is exact.

## 6. Fixes (all optional, editorial)

**E1. Lemma 4.11 proof, "Integrals".** After "…and the increasing factors (𝔭, 𝔭\*, 𝔭_L, 𝔭_L\*, (1+x)^γ) at x_{i+1}", insert:

> (on the range $x\ge\theta_l/\kappa$ used, $x\ge\theta_h/2$ since $\theta_h/\theta_l\le1.03<2/\kappa$, so all three entries of
> $\mathfrak p$ are present and $\mathfrak p$ is increasing there; $\mathfrak p^*$, $\mathfrak p_L$, $\mathfrak p_L^*$ are
> increasing everywhere)

Reason: across y = θ/2, 𝔭 jumps *down* (the chord entry 2κC_T y appears), so "increasing factor" needs this range
remark.

**E2. Appendix A, the sentence listing the 20 elementary inequalities.** Optionally add after "…in Lemma~\ref{lem:len})":

> ; two of them, $\vbar^2\le\frac12$ and $\eta\le1$, are recorded for completeness only

**E3. Theorem 5.2 proof (iii).** $\mathfrak p:=1-T\cdot\uhat$ reuses the symbol of Definition 4.3. Optionally rename it to
$\mathfrak d$ (local to that paragraph).

No change is needed for the mathematics, the constants, the tables or the script.
