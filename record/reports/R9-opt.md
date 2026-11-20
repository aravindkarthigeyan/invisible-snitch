# R9-opt: certified final constant after the three refinements (tilt, near, far/length)

Stream Opt, round 9. Script `r9/opt/verify_v2.py` checks every condition. It is self-contained (mpmath, numpy), works in
50-digit arithmetic at the PRINTED inputs, exits non-zero on failure and prints all margins. Its logs are
`r9/opt/verify_v2_S1G.out`, `r9/opt/verify_v2_S1.out` and `r9/opt/verify_v2_all.txt` (`EXIT 0`). The search tools are
`opt_v2.py` (float optimiser with a D′ model), `freeze_v2.py` (final stage with D′ frozen), `finalize_v2.py` (safe
rounding plus certification) and `patch_inputs.py`. The cross-checks are `cmp_J.py`, `xcheck_Q3.py` and
`xcheck_far_row.py`.

## 0. Result

| | **with (S1G) / Lemma T2\*** | **without (S1G)** (fallback if T2\* fails refereeing) |
|---|---|---|
| certified **v0** | **5.8·10⁻³** | **2.3·10⁻³** |
| T0 (T♯ = T₂ + κU_max/(1−v0) ≤ T0) | **13.1** (T♯ = 13.0834) | **12.6** (T♯ = 12.5769) |
| ε* (ε_S) | 4·10⁻¹¹ | 4·10⁻¹¹ |
| certified D′(p), D′(p_A) | 63.0679, 64.6356 (printed 63.068, 64.6357) | 144.3302, 147.1774 (printed 144.331, 147.178) |
| conditions | **218, all hold** | **216, all hold** (the 2 (S1G) conditions are dropped) |

Compared with R9-far §5.2 (4.146e-3, not verified): v0 rises by 40%. It rises because D′ was iterated to consistency
(the true D′ is ≈ 63–65, not the 98.7 that was used) and because the optimiser re-chose η, ξ₁, λ₀ and G_T.

**Binding conditions (S1G set).** By design, the derived quantities sit at their limits, with relative slack ≤ 2e-6:
(P1) d_L, δ₁; (P3\*) ν; (P4\*) A₀; (P5\*) s₀; (P6) f_F with the certified D′(p_A); the outward roundings; and
v0 = v̄. The genuinely binding parameter conditions are:

| condition | relative margin |
|---|---|
| (C2) [p], [p_A] | 8.9e-4 |
| K_f + 1 ≤ K_R | 8.9e-4 |
| (PT) (1+δ_t)L_J\*(U_max) < κ | 1.8e-3 (1.28741 < 1.2897) |
| c_A ≤ 1 | 2.0e-3 |
| ω₀ ≤ ω̄ (A4) | 2.6e-3 |
| ½ < γ | 3.3e-3 |
| η₁ ≤ K_f/(K_f+1) | 4.9e-3 |
| (P7\*) [p] | 1.6e-2 |
| (TS) | 2.0e-2 |

(P6) is binding through f_F: θ̄ = f_F² + 2v0D′(p_A) = 1 − 8.3e-7.

**Binding conditions (S1-only set).**

| condition | relative margin |
|---|---|
| (SC17) ρ_cξ₁ > 1 | 7.2e-5 |
| (PT) | 7.5e-5 |
| (C4) c_sep ≥ c_AK_RR | 9.2e-5 |
| κ ≤ 4/3 | 1.1e-4 |
| (3/2)κ − 1 ≤ 1 | 2.2e-4 |
| ω₀ ≤ ω̄ | 5.0e-4 |
| (TS) | 9.5e-4 |
| (SC39) | 1.2e-3 |

The S1-only set also has P1/P3–P6 saturated by construction. Without (S1G), (PT)/(P7\*) caps v0 at about 2.33e-3:
J₁ = χ_gU₀/(c_R\*R) = 91.8 forces κ → 4/3.

## 1. Final parameter tables (strings exactly as printed in `verify_v2.py`)

**Set S1G (v0 = 5.8e-3).**

| group | values |
|---|---|
| main | v0 5.8e-3, ε_S 4e-11, T0 13.1 |
| touch-down row (thm:HTp, D₁ = 1) | v̄ 5.8e-3, η 0.11639, ε̄ 1e-3, ξ₁ 1.16171, λ₀ 0.0337254, G_T 0.030573 |
| touch-down constants (outward) | T₂ 3.77231↑, U_max 7.17768↑, c_sep 0.0276152↓, k_c 0.951517↓, c_N 3.41207↑, μ̄_T 0.0172997↑, μ̄ 0.00583384↑, a′ 0.9827002, θ_v 1.153↑, c_T4 1.12275↑, c_z,lo 1.20086↓, c_z,hi 1.67043↑, c_y 0.697925↑, W_xL̂ 1.22122↑ |
| core | γ 0.50164, R 0.00139765, m 0.142162, s₀ 0.276635, κ 1.2897, c_A 0.997991, K_R 9.21786, K_f 8.20966, K_ε 137.074, η₁ 0.887055, q_c 2.30668 |
| dependent (safe side) | d_L 1.0058339, δ₁ 1.0117361, ν 0.0107665, A₀ 1.129899, f_F 0.500225, γ_D 0.535633 |
| assembly | ω̄ 0.421626, c_k 1.01239, δ₀ = 0.251113 R |
| near (certified, printed upper bounds) | D′ 63.068, D′_A 64.6357 |

Derived values (p | p_A):

| constant | p | p_A |
|---|---|---|
| C_T | 3.8325 | 3.6370 |
| C_μ | 19.94 | |
| c_ρ\* | 0.7515 | |
| c_η | 0.9897 | |
| c_R\* | 9.192 | |
| c_amp\* | 1.8563 | |
| J₁ | 19.745 | 0.772 |
| J₂ | 392.26 | 60.10 |
| B₂U′ | 1.0632 | |
| B₂η\* | 1.694 | |
| C_p′ | 5.681 | |
| C_p^V | 5.690 | |
| C_ar | 1.847 | |
| B₃′ | 12.60 | |
| B₅\* | 83.62 | |
| T_I | 15.36 | |
| X_far\* | 0.1324 | |
| L_J\* | 1.26945 | 1.14736 |

Assembly values: δ_t = 0.014153, η_N = 0.0070313, W_e = 0.013513, (TS) 0.038507 ≤ 0.039278.

**Set S1 (no (S1G), v0 = 2.3e-3).**

| group | values |
|---|---|
| main | v0 2.3e-3, ε_S 4e-11, T0 12.6 |
| touch-down row | v̄ 2.3e-3, η 0.276456, ε̄ 1e-3, ξ₁ 1.07839, λ₀ 0.108217, G_T 0.143406 |
| touch-down constants | T₂ 3.74794, U_max 6.60721, c_sep 0.0964115, k_c 0.864827, c_N 3.84813, μ̄_T 0.00688417, μ̄ 0.00230531, a′ 0.9931158, θ_v 1.33693, c_T4 1.28857, c_z,lo 0.985192, c_z,hi 1.91821, c_y 1.03227, W_xL̂ 1.12202 |
| core | γ 0.544297, R 0.00376374, m 0.129265, s₀ 0.330381, κ 1.33319, c_A 0.908052, K_R 28.2071, K_f 17.4401, K_ε 20.9351, η₁ 0.906661, q_c 2.3314 |
| dependent | d_L 1.0023054, δ₁ 1.0046213, ν 0.00400271, A₀ 1.239866, f_F 0.568314, γ_D 0.557637 |
| assembly | ω̄ 0.49256, c_k 1.16311, δ₀ = 0.126548 R |
| near | D′ 144.331, D′_A 147.178 |

Derived values: J₁ = 91.756, J₂ = 953.59, L_J\* = 1.31364, δ_t = 0.014804.

## 2. Conditions and their sources

Counts: S1G set 218 (near 2, td 56, out 13, core 78, cor 12, asm 37, extra 20); S1 set 216 (asm 35).

| group | conditions | source |
|---|---|---|
| td (56) | (SC1)–(SC48) of the short paper's Def 7.1 (52 lines incl. a/b items), plus the record's HTSC41 λ₀ ≤ ¼, HTSC46 κ₂ ≥ ½, HTSC49 c_Nλ₀^{1−μ̄_T} ≤ 1, and v̄ ≤ 2e-2 | `paper/sec_HTp.tex` thm:HTp (= HTSC1–51) at the new row; `r9/base_short` sec7 |
| out (13) | outward rounding of T₂, U_max, c_sep, k_c, c_N, μ̄_T, μ̄, θ_v, c_T4, c_z,lo, c_z,hi, c_y, and **W_xL̂** (new, used by 𝒢) | base; W_xL̂ for Lemma T2\* (`referee/R9-far-claims.md` §2.4–2.5) |
| core (P0), (P1), (P2) c₆ ≤ K_RK_ε | unchanged base (P0)/(P1), except **(N1) K_ε ≥ 2**, which replaces K_ε ≥ 3/2 | base; (N1): `r9/near/prop_near.tex` l.45, `reports/referee-R9-near-1.md` F3 |
| core (P2\*) c_ρ\*K_f ≥ 2, c_R\*K_ε ≥ 1, c_η > 0; (P3\*); (P4\*); (P5\*); (P7\*) | new far-pair/length formulas (aD\*, J₁, J₂, B₂U′, B₂η\*, C_p\* = min(C_p′, C_p^V), C_ar, Ĉ, B₃′, B₅\*, X_far\*, L_J\*) | `referee/R9-far-claims.md` §2.6–2.7, §3 (UNDER REFEREEING; proofs passed by referee-R9-far-1 and -2) |
| core (P6) θ̄ = f_F² + 2v0D′ < 1 | D′ certified (`near` group) for both tuples | `r9/near/prop_near.tex` (Lemma E boxed D′); certification: port of `code/referee/R9near_1/cert_Dprime.py`; `referee-R9-near-1.md` F3/F4, `-2.md` F3 |
| core (T1)–(T4), both tuples | C_T, C_μ, C_p′ | `referee/R9-tilt-claims.md` §0; `reports/referee-R9-tilt-1.md` F5, `-2.md` §3 |
| near (2) | certified D′(p) ≤ printed D′, D′(p_A) ≤ printed D′_A | as above |
| cor (C1)–(C6) | unchanged | base `r9/base_short` sec3 |
| asm (A2)–(A6), (TS), (PT) | η_N = aD\*(4)v0/ζ and c_β/π (Lemma Du\* drop-in); stage-A tilts C_A^A = C_B^A = C_T^A, C₃ = 2C_T^A (option F4(b)); (PT) with L_J\* | base sec5/sec8; `referee/R9-far-claims.md` §2.2; `reports/referee-R9-tilt-1.md` F4(b), `-2.md` R1 |
| asm (S1G) (2, S1G set only) | c₀′ = 1 − ½(C₀λ₀^{a′})² > 0, 8/λ₀ ≥ 1 | `referee/R9-far-claims.md` §2.4 (Lemma T2\*), §2.5 |
| extra (20) | base "extra" list minus κ ≤ C_TL²(4−κ²) and c_t(3) ≥ √3 | base; deletions per `referee/R9-tilt-claims.md` §0, `referee-R9-tilt-1.md` F5 |

Interface fixes applied:
- T_I and Ψ_I are kept: they are used in L_J\* (`referee-R9-near-1.md` F1, `referee-R9-far-1.md` F7(a)).
- L_J\* is used wherever the text says L_J, i.e. in Lemma 3.9 (Imp), the §4 standing assumptions and (A1)/(A5)
  (`referee-R9-far-1.md` F7(c)). Numerically these are the (P7\*) and (PT) checks above.
- The upper limit in (3.1) is max(K_RR, U₀/2) (`referee-R9-far-1.md` F6). It is implemented as "empty range ⇒ 0".
- referee-R9-far-2 F5: the locality principle, Thm 3.4(d) and Prop 8.3 Steps 1 and 6 must cite (S1G). This is text
  only and has no numeric effect.

## 3. Certification details

- **D′ (R-near Lemma E).** This is a port of the referee's certified evaluator, parametrised by the printed strings.
  - Scalars are evaluated in mpmath.iv, including C_T and C_μ computed from the R-tilt formula in interval arithmetic
    (not a rounded input).
  - Arrays use float64 with an outward ulp after every operation.
  - Sums are inflated by (1 + 1e-11).
  - The (1+y)^γ table is extended to K_f.
  - Grid: q = 1.03, n_x = 500, n_s = 700, dr = 0.05, 570 θ-cells.
  - S1G set: the worst cell for p is θ ∈ [0.0254, 0.0261], r ∈ [3.48, 3.53] (long-type). For p_A it is
    θ ∈ [1.74, 1.79] (short-type).
- **J₁, J₂ (Lemma (J)).** The bounds are rigorous upper bounds.
  - Closed forms are used on the constant piece and on the linear branch of ρ_G, with a verified bracket of the branch
    crossing.
  - On the sine branch I use left-endpoint Riemann sums: the integrand is non-increasing, so any partition gives an
    upper bound. The partition is geometric in the distance to the start of the piece, with 20 000 cells.
  - A factor (1 + 1e-30) covers the 50-digit rounding.
- **Touch-down row.** Every constant is recomputed at the printed (v̄, η, ε̄, ξ₁, λ₀, G_T).
  - `xcheck_Q3.py` reproduces the record's `code/Q3/constants.py` chain() (D₁ = 1) to 50 digits for T₂, U_max, c_sep,
    κ₂, c_N, θ_v, c_T4, c_y, W_x, L̂, ξ±, z_T, h_t, μ̄_T, μ̄.
  - chain() reports "ALL OK (50)" plus HTSC51 for both final rows.

## 4. The J₁/J₂ discrepancy (referee-R9-far-1 F9)

At the R9-far §5.2 vector (v0 = 4.14578e-3, `r9/opt/cmp_J.py`):

| evaluation | J₁ | J₂ |
|---|---|---|
| `r9/far/far_opt.py` (`_Jints`) | 28.212 | 11 353.8 |
| referee `code/referee/R9far_1/recompute.py` (mp.quad) | 28.411 | 12 634.4 |
| verify_v2, rigorous **upper** bound (20 000 cells) | **28.4208** | **12 638.0** |
| same partition, rigorous **lower** bound (right endpoints) | 28.4001 | 12 630.6 |

So the true values lie in [28.400, 28.421] and [12 630.6, 12 638.0]. The referee's values are correct, and the formula
as written is what verify_v2 implements. far_opt.py differs for this reason: after the plateau ρ_G = c_AK_RR − δ₁R/K_ε
(which ends at y ≈ 4.2e-4), ρ_G grows on the sine branch from ≈ 3.5e-4 to 2 over [4.2e-4, πW_xL̂ ≈ 3.65]. far_opt
integrates that whole piece with one 96-node Gauss–Legendre rule (times 1.001). The integrand (2 sin(y/2W) − s)^{−k}
varies on the scale 4e-4 at the left end, which that rule does not resolve, so it underestimates: by 0.7% for k = 1
and 10% for k = 2. With the formula-faithful values, the R-far point fails (P4\*), (P5\*) and (PT), as the referee
found.

A plain mp.quad without a breakpoint at the kink 2W asin(F/2) also gives a wrong J₁ (28.665, i.e. +0.9%). Only a
bracketed bound is reliable here. All numbers in this report use the rigorous upper bounds.

## 5. referee-R9-far-2 items

- **F8 misprints** (C_ar 1.508, B₂U′RJ₂ 4.188/0.0653 at the base point): verify_v2 computes every constant from the
  formulas and uses no table value.
- **F9 (touch-down row).** The full row (SC1)–(SC48) plus the record's extra conditions is part of the checked set and
  of the joint optimisation. η, ξ₁, λ₀ and G_T are free variables of the optimiser. Lemma T2\*'s preconditions
  (SC41)–(SC44) are included, as are (C4) with the new c_sep and (A3)/(A4) with the new G_T.
  - The failures the referee reports, (SC17) ρ_cξ₁ = 0.9952 and (SC47b) 0.10026 > η, are for the BASE row data
    (ξ₁ = 1.007, η = 0.1, G_T = 0.05) at v̄ = 4.146e-3. At R-far's re-optimised row (ξ₁ 2.42695, η 0.131449,
    G_T 4.16e-4), all HTSC1–51 hold: ρ_cξ₁ = 2.385 and ξ̄_e + G_T = 0.0523 ≤ 0.1314 (`xcheck_far_row.py`).
  - At the final rows the closest touch-down margins are (SC17) 7.2e-5 (S1 set) and (SC39) 1.2e-3 (S1 set). In the
    S1G set, every SC has margin ≥ 1e-2.
  - (C4) holds with c_sep = 0.0276 ≥ c_AK_RR = 0.0129 (S1G set), and with 0.0964 ≥ 0.0964 (S1 set, margin 9.2e-5).

## 6. How v0 was obtained (NUMERICAL search; the certificate is §3)

1. **Float optimiser** (`opt_v2.py`). It is exactly the same condition functions exec'd in float, with the J sums
   vectorised on the same partition. It optimises 18 free parameters (γ, R, m, κ, c_A, K_R, K_f, K_ε, η₁, q_c,
   γ_D slack, ω̄, c_k, δ₀/R, ξ₁, η, λ₀, G_T) by bisection in v0. The derived quantities are saturated: d_L, δ₁, ν, A₀,
   f_F = √(1−2v0 max D′), and s₀ from (P5\*) for both tuples. D′ for both tuples is a log-linear model fitted with
   `r9/near/near_const.py` (fine resolution for the level, quick resolution for the slopes) inside a trust region.
   After each run D′ is recomputed and the model is re-centred.
2. **Iterations to D′ consistency (S1G).**

   | step | v_max | D′ max at the result (model) |
   |---|---|---|
   | start (R9-far point) | 4.10e-3 | — |
   | | 4.78e-3 | 65.6 |
   | | 5.57e-3 | 71.7 vs model 64.6: rejected; the stage-A γ_D offset fixed in the model |
   | | 5.738e-3 | 64.41 ≤ 65.31 (consistent) |
   | | 5.727e-3 | — |
   | | 5.871e-3 | inconsistent |
   | | **5.807e-3** | 64.57 ≤ 64.81 (consistent) |

   Each consistent result was certified, and then `freeze_v2.py` re-optimised the remaining parameters with the D′
   parameters frozen at the certified printed values. In that run γ_D ≤ its certified value and v0 ≤ the certified v0
   (D′ is increasing in both), so D′ is exactly conservative.
   - With D′ frozen at the 5.738e-3 point, v_max = 5.689e-3 (certified at 5.6e-3, 218/218;
     `verify_v2_S1G_5p6.out`, `inputs_S1G_5p6.json`).
   - With D′ frozen at the 5.807e-3 point, it is feasible at v0 = 5.8e-3 → **final** (`inputs_S1G_final.json`).
   - D′ moves by about 1% per 0.01 in κ − c_A, and the D′(κ, c_A) surface is non-smooth: the worst cell switches between
     long-type θ ≈ 0.025 and short-type θ ≈ 1.8. 5.9e-3 was not reached. The 2-digit answer 5.8e-3 is within 1.5% of
     the best float value found (5.807e-3).
3. **S1 set.** The iterations gave 1.97e-3, 2.16e-3, 2.30e-3, 2.33e-3 and 2.35e-3, but the D′ model was poor:
   D′ ≈ 134–147 at κ − c_A ≈ 0.42, and the K_f slope is unstable. The 2.33e-3 point was certified (D′ 144.3/147.2),
   then frozen and re-optimised. It is feasible at 2.3e-3 and infeasible beyond the certified v0, where (PT)/κ ≤ 4/3
   bind. **Final: 2.3e-3** (`inputs_S1_final.json`).

## 7. Caveats

- **R-far is under refereeing.** Both reports so far pass all proofs. Every far/length condition (P2\*)–(P5\*),
  (P7\*), (PT), η_N, c_β/π and J_k comes from `referee/R9-far-claims.md`. If R-far failed, neither number would stand:
  the S1 set still uses E\*, Du\*, F\* and L\*.
- **The S1G number additionally needs Lemma T2\*,** the (S1G) addendum to Lemma 8.2, Lemma 3.7(iii) and Lemma 3.6(iv).
  If T2\* fails, the certified fallback is 2.3e-3.
- **F4 choice.** Stage A uses option (b): C_T^A for C_A^A and C_B^A, and C₃ = 2C_T^A. Both tilt referees endorse
  this (the claims file's 3C_T^A is valid but looser). The text of §5/§8 must be changed accordingly.
- **What "rigorous" rests on.** The certificate rests on IEEE-754 round-to-nearest for float64 + − × ÷ √ (D′ arrays),
  on mpmath.iv, and on 50-digit mpmath elsewhere (as in the base script). The search itself is float and uncertified.
  It does not matter, because every condition is re-checked at the printed values.
- **v0 = v̄.** v0 is printed equal to v̄, so (A6) v0 ≤ v̄ holds with equality, by construction.
