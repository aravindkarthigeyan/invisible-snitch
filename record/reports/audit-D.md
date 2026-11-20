# Audit D: do the typeset sections sec_Estar, sec_HTp and sec_T3 contain only refereed mathematics?

Auditor: audit D. **The paper was not edited.**

Detailed per-section working (full tables, notes and recomputations) is in two files:
- `reports/audit-D-Estar-part.md` (17 rows)
- `reports/audit-D-HTp-part.md` (21 rows)

This file contains the combined table, the full audit of sec_T3, and the status-remark checks.

Code, all in `code/audit/D/`, 50-digit mpmath, run with `python -I`:

| script | output | what it does |
|---|---|---|
| `Estar_check.py` | `Estar_check.out` | Recomputes the E\* deltas. |
| `HTp_constants.py`, `HTp_lam0_scan.py`, `HTp_thv_limit.py` | `.out` files of the same names | Rewrites def:HTp-const and (SC1)–(SC51) from the TeX, then checks the 13 rows, the excluded combinations and cor:HTp-used. |
| `T3_assembly.py` | `T3_assembly.out` | Recomputes every assembly constant of tab:T3-const and every assembly side condition of tab:T3-side. It starts from the *printed* inputs and uses the formulas *as typeset*, with no code from Q2 or Q4. |
| `T3_core.py` | `T3_core.out` | Recomputes the core rows (P1)–(P7) and (C2)–(C6), for the main application and for stage A, and L_J, C_A^A, C_B^A. It uses the refereed formulas of `code/Q1/q1const.py`. |

## 0. Summary

- **Main path (FALSE or GAP): none.** On the path cor:HTp-used → thm:Estar/cor:Estar/L1–L4 → lem:T3-W, thm:T3-E, lem:T3-H, thm:T3-D, prop:T3-cond → thm:Main2/cor:Exact2:
  - every delta is OK or OK with a textual fix;
  - every constant printed in tab:T3-const and tab:T3-side was reproduced independently. All 114 conditions hold, both at the printed nearest values and with the outward-rounded touch-down values.
- **lem:T3-W (new, refereed here in full): OK with fix.** The mathematics is correct. The citation list in its proof is incomplete:
  - the pieces of the proof of thm:End that are reused verbatim are missing, though they are covered by lem:T2-W(d);
  - Remark E-B(4) needs one sentence of justification;
  - the proviso must be stated with (CA\*) of good pairs, not with (S1\*), for use inside thm:T3-E.
- **Restating Q2.E′ for End\* instead of the old core is valid.** I checked every point that the RQ2 referees checked with the old core (§2, item T3 below).
- **ψ: OK.** Version 1's ψ = min(1, x/(1−x²/2)) is *negative* for x > √2, which is a defect in the version that both RQ2 referees passed. At the chain values x = C₃κ_W reaches about 1.47. Q4's (A4) wording is false on (√3−1, 1]. The typeset definition is correct, and no constant changes.
- **FALSE, off the main path (2 rows):**
  - sec_Estar intro: "thm:End is the γ ≤ 1/4 special case". It is true only with δ₁ := e^{2v/(1−v)} instead of the table's 2.
  - sec_HTp intro: "θ_v → 1 as v̄ → 0". At η = 0.1 the limit is 1.069.
- **Inaccurate status remarks (fix texts in the table):**
  - rem:T3-status opens with "Each piece of the chain … was checked by two independent referees". Its own table and its last sentence contradict this: lem:T3-W, the End\* version of the assembly, the 6·10⁻⁵ touch-down row, (SC51) and the final constants are unrefereed.
  - rem:T3-status presents the core ceiling without a "not refereed" label.
  - rem:T3-status says the core tilt "enters only through ω₀ ≤ ω̄"; this is wrong.
  - rem:HTp-status calls `final.py` an "independent" evaluation, and overstates what RQ3-1 checked.
  - rem:Estar-status has attribution errors: "reproduced by both referees", and the search for K_f = 64 is credited to the wrong report.
- **Note on the brief.** lem:T3-W is not in v1. It *is* in Q2-claims v2 §1.1, as the paragraph "Working fronts (core = End\*)", which is unrefereed. It was refereed here.

## 1. Combined table

Verdicts: OK / OK with fix / GAP / FALSE. "Main?" means the delta is on the logical path to thm:Main2.

### sec_T3 (full audit in §2)

| # | section | delta | main? | verdict | exact fix text |
|---|---|---|---|---|---|
| T1 | sec_T3 | Notation: t_w→t_W, j_w→j_W, η→η₁ (core), η→η_D (departure); labels T3-\*; d=1 except thm:Main2 | yes | OK | none |
| T2 | lem:T3-W (new; in Q2-claims v2 §1.1 only, unrefereed) | Working-front version of End\*/Cor End\* with the proviso | yes | **OK with fix** (no mathematical gap; §2.1) | In the proof replace "cites, besides its own auxiliary lemmas (…), only Lemmas" by "cites, besides its own auxiliary lemmas (…) and the pieces of the proof of Theorem~\ref{thm:End} used verbatim (Table~\ref{tab:Estar-unch}: the continuity scheme, the start value of near pairs, the proof of Theorem~\ref{thm:End}(b), which hold on a working front by Lemma~\ref{lem:T2-W}(d)), only Lemmas". After "with Lemma~\ref{lem:B-C}(3) replaced by ($3'$)" add "; Remark~\ref{rem:E-B}(4) holds because $x(\cdot,t)$ is determined by $x^0$ and $P|_{[\Mtw,t]}$". Replace "so that (J1$^*$) holds at $t_j$" by "so that (J1$^*$) holds at $t_j$ (by continuity if $t_j=t^*$)". At the end add: "The proviso uses (S1$^*$) only through \eqref{eq:Estar-CA} for the pair $(a_j,a_{j+1})$ (label length $\le\varepsilon\le R$); so it holds whenever \eqref{eq:Estar-CA} holds for the family pairs, as in Theorem~\ref{thm:T3-E}, where (CA$'$) gives it." |
| T3 | thm:T3-E | Stated and proved for End\*; RQ2 refereed it with the old core (RQ2-2 §6(b) proposed stating it for the old core) | yes | **OK** (each old-core step re-checked with End\*, §2.2) | Optional, in rem:T3-status after "have not been refereed": "(audit D, \texttt{reports/audit-D.md}, checked them)". |
| T4 | thm:T3-E (PT), (F3) | LHS(P7) := L_J with the final X (A1); (PT) ⇒ (P7_δ) | yes | OK. (1+δ)L_J ≥ (1+δ)e^{X+…} + vκ₁τ_I | none |
| T5 | (F4), Part 1 | (a_j, a_{j+1}) added (A2); shown to be a body pair | yes | OK (u′_{a_{j+1}} ≥ U−W−ε ≥ W) | none |
| T6 | Part 1 end | Pairs of F(t_W) with first point a_{j_W−1} are body pairs; the gap of a tail pair at t_W is g_W (RQ2-2 §2.2) | yes | OK. This is the convention of L3(2) (g_w := g(t_w)). In the assembly min(g_W, K_RR) = K_RR under either convention | none |
| T7 | Step 0 | New justification of the case w_s < ε/2: "(e′) is negative (δ₁ ≥ 1 > c_A/2)" | yes | OK (c_A w_s − δ₁ε < (c_A/2 − δ₁)ε < 0) | none |
| T8 | tab:T3-reuse (new) | Reuse table of the steps of End\* | yes (expository) | OK (consistent with L1–L4 and with the proof) | none |
| T9 | tab:T3-cover | Coverage table from RQ2-2 §2, adapted (as v2 §1.4) | yes | OK | none |
| T10 | lem:T3-H, Step 3 | ψ := min(1, x/(1−x²/2)) on [0,1], 1 on (1,∞) | yes | **OK.** For x ≤ 1: 1−x²/2 ≥ 1/2, so ψ ≤ 2x, and |e×r̂| ≤ x/(1−x²/2) from the two displayed bounds (e·e′ = 1−|e−e′|²/2). For x > 1, ψ = 1 ≥ |e×r̂|. K_rot uses ψ ≤ 1 and θ_{h1} uses ψ ≤ 2x. v1's ψ < 0 for x > √2 (defect missed by RQ2-1/2; at the chain values x reaches about 1.47). Q4's (A4) wording ψ := x/(1−x²/2) on [0,1] gives ψ(0.9) = 1.51 > min(1, 1.8) = 1, so its claim ψ ≤ min(1,2x) is false on (√3−1, 1]. The typeset definition avoids both problems | none |
| T11 | lem:T3-H setting | G_f becomes a parameter with W+ε+δ₀ ≤ G_f ≤ U_A−ε (v1: G_f := W+ε+δ₀). ρ_\* becomes any value with ε ≤ ρ_\* ≤ c_{A1}(R₁−δ₀−ε)−δ₁ε (v1: equality). ε ≤ δ₀ (F-H/M2) | yes | OK. The proof uses only u_b < W+δ₀ ≤ G_f ≤ U_A and ρ_a, ρ_b ≥ c_{A1}(R₁−δ₀−ε)−δ₁ε ≥ ρ_\*. This makes the constants computed at ε_\* valid for every ε ≤ ε_\* | none |
| T12 | thm:T3-D | Duration D and bound D̄, all constants computed with D̄; (D3) X_\* ≥ U_E+z₀+D̄ (F-D/M1); new sentence "No constant depends on ε except through D̄+ε in L_h" | yes | OK (D enters the proof only through τ ≤ D ≤ D̄, X_s ≤ X_\* and ∫_0^D ≤ ∫ up to D̄+ε in L_h) | none |
| T13 | hyp:T3-HT, Step 4 | [HT′] data (T1′)–(T5′) and the conversions θ₀ = c_T4X_\*^{1−μ̄_T−γ_D}, θ_y = c_y2^{2−μ̄_T}(z₀^max)^{1−μ̄_T−γ_D} | yes | OK (exponents ≥ 0, z₀ ≤ z₀^max, ε ≤ z₀, U_E ≤ G_T, u′+z₀ ≤ X_\*) | none |
| T14 | eq:T3-const | γ_D ≥ γ+ν+η_N (rounded up; v1 had equality); stage A: same R, m, A₀, f, ν (Q4); c_sep^A; D̄, G_f, z₀^max with ε_\* | yes | OK. P1–P3 do not depend on γ (c_ρ, c_R, c_6, c_amp do not involve γ), so the table's "(P0)–(P3) same for stage A" is right | none |
| T15 | Side conditions (i)–(vi) | Compared with v2 §4.2: all present. "1+γ_D ≤ 2−μ̄_T" (table) is the same as γ_D ≤ 1−μ̄_T in (iv) | yes | OK | none |
| T16 | prop:T3-cond, Steps 1–7 | Q2.M proof with the RQ2 fixes, End\* via lem:T3-W, [HT′] | yes | OK (§2.3) | none |
| T17 | prop:T3-cond, Monotonicity | Constants of lem:T3-H and thm:T3-D taken at (v₀, ε_\*) and applied at (v, ε) | yes | OK (every lemma hypothesis is one-sided in ε, v; k fixed at its v₀ value still satisfies k ≥ 4(1+δ_t(v))/ζ(v)) | none |
| T18 | tab:T3-const, tab:T3-side, Margins | Q4's constants (unrefereed numerics) | yes | **OK** (recomputed: all agree to the printed digits; PT 1.0142971, slack 0.162%; P7 0.164%; TS 3.01154·10⁻³ vs 3.04682·10⁻³, 1.16%; P6 10.3%; C2 1.3·10⁻⁵; P2 1.7·10⁻⁵; P5 slack 9.5·10⁻⁷ at nearest U_max, 7.8·10⁻⁷ at outward U_max; T₀ = 10.12635–10.12637 ≤ 10.13). All 114 conditions also hold with the outward T₂, C₀, U_max and a′ = 0.99982 | Optional: in tab:T3-const print "$\bar\mu_{\mathrm T}$ & $1.799892\cdot10^{-4}$" (1.79989 is rounded *down*; harmless because the caption says "rounded to nearest" and the check uses exact values). |
| T19 | thm:Main2, cor:Exact2 | New theorem with Q4's constants | yes | OK (scaling and lem:A41 as in thm:Main/cor:Exact) | none |
| T20 | intro, (3) | "this costs about forty orders of magnitude" (unrefereed) | no | OK with fix (4.1·10⁻⁵¹ vs 4.7·10⁻¹⁵ is 36 orders, RQ2-1 §5) | Replace "about forty orders of magnitude" by "about $36$ orders of magnitude ($v_0\approx4\cdot10^{-51}$ against $4.7\cdot10^{-15}$ for the same core and data)". |
| T21 | rem:T3-status, first sentence | "Each piece of the chain … was checked by two independent referees" | no | **Inaccurate** (contradicted by its own table row "Q4-1.md (not a referee report)" and by its last sentence; lem:T3-W, cor:HTp-used and (SC51) were not refereed) | Replace by: "The pieces of the chain behind Theorem~\ref{thm:Main2} and their refereeing status are as follows (reports in the project archive):" and add a table row "Lemma~\ref{lem:T3-W}; the End$^*$ form of Theorem~\ref{thm:T3-E}; Corollary~\ref{cor:HTp-used} (the column $\bar v=6\cdot10^{-5}$) and (SC51) & not refereed (audit D)". |
| T22 | rem:T3-status table, HTp row | "Theorem HTp (touch-down data, with (SC51) added): RQ3-1, RQ3-2" | no | OK with fix ((SC51) was added after the reports; RQ3-1 never saw the printed rows) | Replace the row text by "Theorem~\ref{thm:HTp} (version~1 statements; (SC51) added after the reports at RQ3-1's request, not itself re-refereed)". |
| T23 | rem:T3-status, Constants | "a ceiling argument for the core shows that the method cannot go much beyond v ≈ 10⁻⁴" (Q1-1 numerics, unrefereed) | no | OK with fix (the claim is true: D ≥ 6.2·10³, so v < 8.1·10⁻⁵ by (P6); see the E\* part, row 10) | Replace "a ceiling argument for the core shows" by "a ceiling argument for the core (numerical, not refereed; checked in audit D) indicates". |
| T24 | rem:T3-status, Constants | "the tilt bound of the core enters only through ω₀ ≤ ω̄ in Lemma T3-H" | no | **Inaccurate** (C_{A1}, C_{B1} also enter θ_{h1}, hence ϑ_h, Θ₀, K_w, Θ_b, Θ_p and (TS)) | Replace by "the tilt constants of stage~A enter only Lemma~\ref{lem:T3-H}, through $\omega_0$ and $\vartheta_h$ (and from there the constants of Theorem~\ref{thm:T3-D}); no smallness of $\ETL m$ is used, since $\psi\le\min(1,2x)$ for all $x\ge0$". |
| T25 | rem:T3-status, refereeing paragraph | Lists the incorporated fixes, but not that v1's ψ was defective and passed by both referees | no | OK with fix | After "so that $\psi\le\min(1,2x)$ holds)" add "; the definition in version~1, read by both referees, was negative for $x>\sqrt2$". |
| T26 | header comment (not typeset) | "applies … RQ2-2 ((M1),(M2),2.2,5.3,6)" | no | OK with fix (5.3 is moot for this chain; 6(b) was not applied) | "… RQ2-2 ((M1),(M2),2.2; 5.3 moot here; 6(a) as rem:T3-status; 6(b) not applied: Q2.E′ stated for End\*)". |

### sec_Estar (details in `audit-D-Estar-part.md`)

| # | section | delta | main? | verdict | exact fix text |
|---|---|---|---|---|---|
| E1 | whole | Renames d→d_L, χ→χ_g, q→q_c, f→f_F, Ψ→Ψ_I, G→G_3, ḡ, θ→θ̄ | yes | OK | none |
| E2 | lem:Estar-gap | "time interval" → "set of times" | yes | OK (the proof uses only per-leg duration and gap spacing) | none |
| E3 | intro | "Theorem thm:End is the special case γ ≤ 1/4 …" | no | **FALSE as stated**. With δ₁ = 2, K̃ ≤ 32+10.9U/R, which does not imply 17+19U/R when U/R < 1.85. True with δ₁ = e^{2v/(1−v)}: K̃ ≤ 16.0003+5.25U/R | "The last column of Table~\ref{tab:Estar-par} gives the corresponding thresholds of Theorem~\ref{thm:End}, which is proved in Section~\ref{sec:end} with coarser constants; the proof below follows that proof step by step." (A long variant is in the part file.) |
| E4 | tab:Estar-unch | Row "Remark E-B(2) (reflection)" (no step cites it) | no | OK with fix | Delete "(2) (reflection),". |
| E5–E8 | rem:Estar-cd, rem:Estar-status | 1.9·10⁴, 1.11, 2.67, 0.56; 0.77, 0.91 (Q4, unrefereed); 4.7·10⁻¹⁵ | no | OK (recomputed: 19092, 1.1126, 2.6749, 0.5588; 0.7736, 0.9124; 4.7157·10⁻¹⁵) | Optional: "; recomputed in audit D" after "not refereed". |
| E9 | rem:Estar-status | "reproduced by both referees" (four data sets) | no | OK with fix (RQ1-1 reproduced one set, RQ1-2 all four) | "(numerical: explicit inequalities in 50-digit arithmetic; the value for $(1/2,0.86,1/40,0.024,6.5)$ was reproduced by both referees, the four data sets by \texttt{referee-RQ1-2.md})". |
| E10 | rem:Estar-status, ceiling | Label "not refereed" dropped | no | OK with fix (true: D ≥ 6.2·10³, v < 8.1·10⁻⁵) | Append "(Heuristic bound from \texttt{Q1-1.md}, not refereed by RQ1-1/RQ1-2; audit D checks $D\ge D_{\mathrm I}+D_{\mathrm{IIs}}\ge6.2\cdot10^3$, hence $v<8.1\cdot10^{-5}$ from \textup{(P6)}, for every admissible parameter choice.)" |
| E11 | after lem:Estar-L4 | δ_tail < 2.3·10⁻⁸; "drops by less than 0.1%" | no | OK with fix (2.32·10⁻⁸ confirmed; the 0.1% runs are for other data sets, and the actual change is 0.011%) | Replace by "the optimiser's $v$ for the data $(1/2,0.70,1/40,0.024,6.5)$ and $(0.99,4.25,1/40,0.024,6.5)$ changes by less than $0.1\%$ (numerical, local optimisation; not refereed)". |
| E12 | rem:Estar-status | Search for K_f = 64, m = γ/50 credited to RQ1-1 | no | OK with fix | "located every implicit use of $\gamma\le1/4$ in the old proof and its replacement (the second report did the same for $K_f=64$, $K_R=32$, $m=\gamma/50$)". |
| E13 | rem:Estar-status | Does not say that the typeset text adds unrefereed remarks | no | OK with fix | Append "The typeset text differs from version~2 of the claims only by notation and by the unrefereed remarks marked as such (the comparison with Theorem~\ref{thm:End}, the values from \texttt{Q4-1.md}, the ceiling, the $\delta_{\mathrm{tail}}$ cost)." |
| E14 | rem:Estar-status | "(J1\*) fails only far out of range (v = 5·10⁻²)" | no | OK with fix | "In the simulations (J1$^*$) was violated only at the largest tested value $v=5\cdot10^{-2}$." |
| E15 | rem:Estar-status, Use | Relies on unrefereed Q4-1; omits L4 | no | OK with fix | "Lemmas~\ref{lem:Estar-L1}--\ref{lem:Estar-L4} (with \textup{(P7$_\delta$)} implied by its stronger condition (PT))" and "(report \texttt{Q4-1.md}, interface check, not refereed; see Section~\ref{sec:main2})". |
| E16 | cor:Estar | Setting P(t_s) = x_{a_s}(t_s), b_E − a_s < 2π made explicit | yes | OK | none |
| E17 | proof of (c) | Covering of [a_j, b_E] abbreviated | no | OK | Optional: "; if $0<U-u_{a_{j+1}}<\varepsilon/2$ the single pair $(a_j,\EbE)$". |

### sec_HTp (details in `audit-D-HTp-part.md`)

| # | section | delta | main? | verdict | exact fix text |
|---|---|---|---|---|---|
| H1 | all statements | Transcription and renames, with RQ3 fixes C1–C4 | yes | OK | none |
| H2 | def:HTp-const, (SC1)–(SC50) | TeX rewrite of the formulas | yes | OK (rewritten from the TeX: matches `chain()` to 4·10⁻⁵¹ on all 13 rows) | none |
| H3 | (SC51) | Added (fix C1) | yes | OK (needed for (T4′), (T5′); safe-direction monotone; holds in every row and at 6·10⁻⁵) | none |
| H4 | cor:HTp-table | Per-row statement, 13 rows | yes | OK (all 51 SC hold in every row) | none |
| H5 | text, rem:HTp-status | Excluded (10⁻², 0.3) fails SC21; (2·10⁻², 0.1) fails SC42 | no | OK (confirmed: no λ₀ satisfies SC39 and SC42 together) | none |
| H6 | rem:HTp-status | At 5·10⁻²: "(SC47), (SC49) fail" | no | OK with fix | "also \HTSC{36}, \HTSC{47} and \HTSC{49} fail". |
| H7 | intro | "θ_v → 1 as v̄ → 0" | no | **FALSE** (1.069 at η = 0.1) | "with $\theta_{\mathrm v}\to1$ as $(\HTvb,\eta)\to0$ ($\theta_{\mathrm v}=1.070$ at $\HTvb=10^{-6}$, $\eta=0.1$; the true constant is $1$)". |
| H8–H9 | lem:HTp-tilt, lem:HTp-twotime | Split out of v1 proofs | yes | OK (re-derived) | Optional: "($w$ is non-decreasing in time, Lemma~\ref{lem:B-1})". |
| H10 | lem:HTp-M | List of ε̄-dependent items incomplete | yes | OK with fix | The full replacement text is in the HTp part, row 10. |
| H11 | cor:HTp-used | Row v̄ = 6·10⁻⁵, η = 0.1, rounded outward (unrefereed) | yes | OK (all 51 SC hold; every value rounded outward; a′ = 0.99982 and C₀ = 2.72160 admissible) | none |
| H12 | cor:HTp-used proof | "(SC51) … = 0.050510, = 0.099510" | no | OK with fix | "$\le0.050510$", "$\le0.099510$". |
| H13 | text | "x_e ≲ 1.9ε^{1/2}" | no | OK with fix | "$\TDxe\le1.93\,\varepsilon^{1/2}$". |
| H14–H15 | rem:HTp-status | "checked by two independent referees" for cor:HTp-table; "all side conditions hold" | no | OK with fix (only RQ3-2 checked the printed rows, and only SC1–SC50) | The full replacement text is in the HTp part, rows 14 and 15. |
| H16 | rem:HTp-status | "independently in code/Q4/final.py" | no | **Inaccurate** (final.py imports the same `chain()`) | "(evaluated by \texttt{code/Q3/constants.py}, which \texttt{code/Q4/final.py} calls unchanged, and independently, from the typeset formulas, by \texttt{code/audit/D/HTp\_constants.py})". |
| H17 | rem:HTp-status | "≈ 1.02 (RQ3-1)" | no | OK with fix | "$\le1.015$". |
| H18 | header comment | "Doubly refereed" | no | OK with fix | "Statements doubly refereed (v1); the row 6e-5 and lem:HTp-tilt/-twotime as statements are not; see rem:HTp-status." |
| H19–H21 | rem:HTp-status numbers; rem:HTp-compare | Report figures; κ₂ = 0.9883 vs 0.9884 | no | OK | Optional: print "0.9884". |

## 2. sec_T3: audit notes

### 2.1 lem:T3-W (new): proof refereed in full

**Claim.** Thm/Cor End\* hold for Construction C on a working front, with "seen" replaced by "direction of every true label seen", and without P(0) = 0 or b_E − a_s < 2π. Under (S1\*), legs are defined.

**Check.**

1. *What the End\* proof cites.* I compared lem:T3-W's list with Table tab:Estar-unch and every `\ref` in sec_Estar.
   - All cited section-B and section-E items are in T2-W(a) or (c): B-V (static), B-VC(a),(b), B-1(i), B-2, B-3 (all parts), B-4, E-facts, B-C(0),(2),(4).
   - B-C(3) is replaced by (3′), and B-VC(c) ("seen") by T2-W(b).
   - lem:Estar-duh uses B-3(c) only. Its mention of B-3(e) is a comparison, not a use.
   - lem:Estar-gap needs leg duration ≤ d_Lε. This follows from B-C(2) (closing speed ≥ 1−v) and (P1).
   - *Missing from the list:* the pieces of the proof of thm:End that are reused verbatim (continuity scheme, start value of near pairs, proof of thm:End(b), and for (c) the Claim of thm:R). These are exactly what T2-W(d) already transfers to working fronts, so there is no gap, but the proof must say so.
   - Remark E-B(4) is not part of T2-W(a),(c). It holds trivially, since the front is the flow of x⁰ under P.
   - Remark E-B(2) is not used.
2. *Hypotheses P(0) = 0 and b_E − a_s < 2π.* In sec_E/sec_Estar they serve only B-VC(c) and c > 0 (tab:Estar-unch: "(c): P(0)=0"). This is correct.
3. *Cor End\*.* Its proof (lines 646–669) is static at t_s, using (E1), (E2), (C0)–(C6) and l = λ. It adds nothing that depends on the front. Correct.
4. *Proviso.*
   - Step 1(a) uses (J1\*) at t_j for (a_j, s_j), (a_j, a_{j+1}) and (a_{j−1}, b_E). This is Lemma L2(ii).
   - a_{j+1} is defined by maximality *before* the leg direction is needed, so the argument is not circular.
   - The advance lies in [ε/κ₁, ε] ⊂ [ε/2, R], since κ₁ ≤ 4/3 and ε ≤ R/K_ε ≤ 2R/3 by (P0).
   - Then c(a_j, a_{j+1}; t_j) ≥ c(…; t_s) ≥ c_A min(λ, K_RR) > 0, by chord monotonicity (T2-W(a)).
   - When t_j = t\*, (J1\*) at t_j holds by continuity; the proof should say this.
   - In thm:T3-E only (S1′) for good pairs is assumed. (a_j, a_{j+1}) has λ ≤ R, so it is good, and (CA′) supplies exactly what the proviso uses. This holds in Part 2 as well; Part 1 says it explicitly, Part 2 does not. Fix T2 adds the sentence.

**Verdict: OK with fix (T2).**

### 2.2 thm:T3-E with End\* in place of the old core

These are the points where the RQ2 referees used old-core specifics; I re-checked each with End\*.

| # | point | check with End\* |
|---|---|---|
| a | Advance ≥ ε/2 | Becomes ≥ ε/κ₁ ≥ 3ε/4 ≥ ε/2. Part 1 ("λ ≥ ε/κ₁ ≥ ε/2, good, c > 0") holds. |
| b | Far iff g ≥ 64λ | Becomes K_fλ. (TW) and Step 5 use K_f; g_W ≥ max(K_f, K_R)R ≥ K_fλ. |
| c | (F1)(i),(ii) window and long pairs (a_{j(τ)}, s) | Same as L1 and L2(i). The goodness argument is unchanged: u′_s ≥ u′_b ≥ W in Part 1, base ≥ W in Part 2. |
| d | (F4) | L2(ii) adds (a_i, a_{i+1}). It is a body pair in Part 1, since u′_{a_{j+1}} ≥ U−W−ε ≥ W. |
| e | (F2) far restart | Identical to L3(2), with the first term A₀(min(g_w,K_RR,K_fλ)/ĝ₂)^ν s₀Mλ^{1/2+γ}. lem:Estar-gap on a *set* of times (row E2) makes the forcing integrals over [t_W, t] legitimate. |
| f | (F3) | L3(2)/L4 with (P7_δ). (PT) ⇒ (P7_δ), because (1+δ)L_J ≥ (1+δ)e^{X+B₅I₅vm²} + vκ₁τ_I. |
| g | Strict start bounds at t_W | N ≤ s₀M… < M… because s₀ ≤ f < 1; the far bound fM… also holds. l ≤ (1+δ_T)λ < κ₁λ because L_J ≥ 1 and (PT). |
| h | Tail pair becomes near | "Step 4 starts from Step 3" (L3(2) proof). Only once, since gaps are non-increasing. |
| i | (b′) | The proof of End\*(b), with (3′) via lem:T3-W. |

No step relied on γ ≤ 1/4, m = γ/50, C_TL·m ≤ 0.33 or the fixed 1.00001/1.01. **Verdict: OK.**

### 2.3 prop:T3-cond / thm:Main2 against v1 Q2.M plus the fixes

- **Steps 1–7** match v2 §4.4. Steps 2, 4 and 5 now use the actual D = t_W − t_td and the bound D̄ (F-D/M1). ε ≤ δ₀ is in (iii) (F-H/M2).
- **Stage A.** U_A = 0.03383 > λ₀ = 0.0333. Unlike the old constants, (E2) is not vacuous here. The text covers it via c_sep^A = min(c_sep, κ₂(1−U_A)) = 0.0330591 ≥ c_AK_RR = 0.0322704 (C4 for stage A, slack 2.4%).
- **Step 5.** g_W ≥ (U−U_E) − (W+ε) ≥ max(K_f,K_R)R. Both exponents are ≥ 0:
  - a′ − η_N − γ − ν ≥ γ_D − η_N − γ − ν ≥ 0, from γ_D ≥ γ + ν + η_N and γ_D + ν ≤ a′;
  - η_N at v ≤ v₀ is ≤ its v₀ value, and R/λ ≥ 1.
- **Recomputation (T3_assembly.out, T3_core.out).** Every printed assembly and core value is reproduced:
  - W 0.0326594, U_A 0.0338253, U_E 0.0336734, D̄ 0.033182, X_\* 0.0668653, G_f 0.0328113, z₀^max 9.90185·10⁻⁶;
  - σ̄ 0.035116, ρ_\* 8.58751·10⁻⁴, K_rot 52.2591, ω₀ 0.150567, ϑ_h 33.5157;
  - Θ₀ 0.371550, ω_T 0.0704545, K_w 0.373653, δ_t 2.24194·10⁻⁵, k 5.16057, Θ_b 36.3820, Θ_p 34.3033, c_n 4.74078, c_β 3.30993, K 286.021;
  - (TS) 3.01154·10⁻³ ≤ 3.04682·10⁻³;
  - L_J 1.0142744, C_A^A 6.39227, C_B^A 9.86365.
  - Every side condition of tab:T3-side holds with the printed slacks.
  - (The last digits of ε_\*-dependent quantities agree to rounding. ε_\* = 4·10⁻¹¹ ≤ (R/(100c_zhi))² = 4.19·10⁻¹¹.)

## 3. Accuracy of the Status remarks

**rem:T3-status.**
- *Accurate:*
  - the table rows for the core and for "this section … with the old core";
  - "both found no false statement and no gap";
  - the list of incorporated RQ2 corrections ((F-A) is moot for End\*; RQ2-2 §5.3 is moot for this chain);
  - the list of incorporated Q4 amendments;
  - "This substitution, the typeset text … have not been refereed";
  - the margins (0.16%, 1.2%, 10.3%).
- *Inaccurate:*
  - the opening sentence (T21);
  - the HTp row ((SC51) and the 6·10⁻⁵ column are unrefereed; T22);
  - the ceiling presented as fact (T23);
  - "only through ω₀ ≤ ω̄" (T24).
- *Omissions:* lem:T3-W is not named as unrefereed (fixed by T21), and the ψ history (T25).

**rem:Estar-status.**
- *Accurate:* "version 1, two independent referees", the fix list and the simulation figures.
- *Inaccurate:* E9, E10, E12, E13, E15.

**rem:HTp-status.**
- *Inaccurate:*
  - "independently in final.py" (H16);
  - "checked by two independent referees" for the printed table (H14);
  - "all side conditions" (H15);
  - "≈1.02" (H17).
