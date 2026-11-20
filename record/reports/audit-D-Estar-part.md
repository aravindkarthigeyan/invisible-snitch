# Audit D, part sec_Estar: paper/sec_Estar.tex against referee/Q1-claims-v1.md and the RQ1 referee fixes

Auditor: fork for section E* only. The paper was not edited.
Sources read in full: paper/sec_Estar.tex (788 lines), referee/Q1-claims.md (v2), the v1→v2 diff, reports/referee-RQ1-1.md,
reports/referee-RQ1-2.md, reports/Q4-1.md. Also read: paper/sec_E.tex (thm:End, cor:End, rem:E-B), the (S) clause of thm:R in
sec_B.tex, code/Q1/out/optimise.txt, and the sec_T3.tex lines that cite this section.
Code: `code/audit/D/Estar_check.py` (50-digit mpmath; imports `code/Q1/q1const.py` unchanged), output `code/audit/D/Estar_check.out`.

## 0. Method and overall result

1. **v1 → v2 (claims).** `diff` shows only the 11 changelog items: F1, F2, F3 of RQ1-1, the remarks after (c) and (d), the binding
   set, R rounding, ≥20-digit printing, the L4 note, the (C0) note and the simulation paragraph. No formula, constant or side
   condition changed. Each item matches what the referees asked for (exact fix texts F1–F3 of RQ1-1 §5 and fixes 1–3 of RQ1-2 §6
   are applied word for word).
2. **v2 → paper, statement by statement.** I compared every statement: the table of free parameters (ranges), all 33 derived
   constants, (S1*)–(S3*), (P0)–(P7), (Pc), Theorem End* (a)–(e), Corollary End* (C0)–(C6), Lemmas 4.1–4.3 (= Estar-duh, -gap, -int),
   Steps 0–5, the proofs of (b)–(e), the proof of the Corollary, and L1–L4. Apart from the renames in the file header (d→d_L, χ→χ_g,
   q→q_c, f→f_F, Ψ→Ψ_I, G→G_3, G(4.2(ii))→ḡ, θ→θ̄), **all hypotheses, constants, ranges and conclusions are identical.** I grepped the
   section for un-renamed symbols and found none (`d=1` on line 43 is the vision distance, as intended; `\BLs` is sec_B's L_s).
3. The deltas the typesetter added are listed below, each refereed.

## 1. Table of deltas

Main path = what sec_T3 uses (Theorem End* (a), (b), (d), (e), (CA*), (E-star*), Corollary End*, Lemmas Estar-duh/gap/int,
L1–L4).

| # | section | delta (paper vs claims v2 / referee fixes) | on main path? | verdict | exact fix text |
|---|---|---|---|---|---|
| 1 | sec_Estar, whole | Symbol renames d→d_L, χ→χ_g, q→q_c, f→f_F, Ψ→Ψ_I, G→G_3, G (4.2(ii))→ḡ, θ→θ̄; labels Estar-duh/gap/int, L1–L4 | yes | OK | none |
| 2 | lem:Estar-gap | "a time interval 𝒯" → "a set of times 𝒯" (a generalisation) | yes | OK | none (see note 2) |
| 3 | intro, l.34–35 | "Theorem thm:End is the special case γ ≤ 1/4 with the parameter values in the last column of Table tab:Estar-par, proved in Section sec:end with coarser constants" (in no claims file) | no | **FALSE as stated** (only (c) fails: with δ1 = 2 from the table, End*(c) gives K̃ ≤ 32.0003 + 10.89 U/R, which does not imply 17 + 19 U/R when U/R < 1.85); OK with δ1 := e^{2v/(1−v)} | Replace the sentence by: "With the values in the last column of Table~\ref{tab:Estar-par}, except $\delta_1:=e^{2v/(1-v)}$ in place of $2$, the side conditions \textup{(P0)}--\textup{(P7)}, \textup{(Pc)} hold under the hypotheses of Theorem~\ref{thm:End}, and Theorem~\ref{thm:Estar} gives the conclusions of Theorem~\ref{thm:End} (for (c): $\tilde K\le16.001+5.3\,U/R$ and $r_1\ge0.42R$); Theorem~\ref{thm:End} is proved in Section~\ref{sec:end} with coarser constants, and the proof below follows that proof step by step." Or, more simply: "The last column of Table~\ref{tab:Estar-par} gives the corresponding thresholds of Theorem~\ref{thm:End}, which is proved in Section~\ref{sec:end} with coarser constants; the proof below follows that proof step by step." |
| 4 | tab:Estar-unch | New rows not in claims §4.0: "Remark rem:E-B(2) (reflection)", "Proof of thm:End(b)", "Start value of near pairs …", "Family …" | no (proof bookkeeping) | OK with fix (rem:E-B(2) is not cited by any step of the proof; sec_T3 l.79–82 lists the items cited by the proof of End* and leaves (2) out) | In the row "Remark~\ref{rem:E-B}(2) (reflection), (4) (causality)" delete "(2) (reflection),". Or mark it "(2): scope only, not used in the proof". |
| 5 | rem:Estar-cd(1) | Adds "nor in the assembly of the main theorem" (from Q4-1, unrefereed) | no | OK (checked: sec_T3/sec_HTp never cite thm:Estar(c) or thm:R; sec_T3 l.850 lists them as not used) | none |
| 6 | rem:Estar-cd(1),(2) | Numbers 1.9·10⁴, μK̃ ≈ 1.11, C_TL m ≈ 2.67, (2/2.675)^{1/γ} ≈ 0.56 (refereed, RQ1-1 R1/R2) | no | OK (recomputed 19092.2, 1.1126, 2.6749, 0.5588) | none |
| 7 | rem:Estar-status, "What is not provided" | μK̃ = 0.77 and C_TL m = 0.91 at the chain's rounded parameters (Q4-1, unrefereed) | no | OK (recomputed from code/Q4/out/final.json with U = U_max = 6.29319: K̃ ≤ 12892, μK̃ = 0.7736, C_TL = 16.2574, C_TL m = 0.9124; (P0)–(P7), (Pc) hold there) | Optional: after "not refereed" add "; recomputed in audit D". |
| 8 | rem:Estar-status, Range | "(against 4.7·10⁻¹⁵ from Corollary cor:End)" (not in claims v2; from optimise.txt / Q1-1) | no | OK (recomputed: γ = 1/4, R = 5.28157·10⁻⁷, v0 = 4.71569·10⁻¹⁵) | none |
| 9 | rem:Estar-status, Range | "5.8–6.5·10⁻⁵ over the four data sets examined … reproduced by both referees" | no | OK with fix (RQ1-2 reproduced all four data sets; RQ1-1 reproduced only (1/2, 0.86, 1/40, 0.024, 6.5)) | Replace "(numerical: explicit inequalities in 50-digit arithmetic, reproduced by both referees)" by "(numerical: explicit inequalities in 50-digit arithmetic; the value for $(1/2,0.86,1/40,0.024,6.5)$ was reproduced by both referees, the four data sets by \texttt{referee-RQ1-2.md})". |
| 10 | rem:Estar-status, Ceiling | Ceiling paragraph (c_6 ≥ 2, C_A ≥ 6.75, K_f ≳ 5, D ≳ 5·10³, v ≲ 10⁻⁴). The claims label it "NUMERICAL, reports/Q1-1.md §3, not refereed"; **the paper drops that label** | no | OK with fix. The claim is true: with c_6 ≥ 2, κ1, d, χ ≥ 1, K_f ≥ (2+2δ1+κ1)/c_A ≥ 5, K_R ≥ 1, C_A ≥ min_q q^{1/2+γ}/(1−q^{−γ}) (= 6.75 at γ = 1/2, ≥ 5.39 for γ ≤ 0.99), I get D ≥ D_I + D_IIs ≥ 6.29·10³ for γ ∈ [0.05, 0.99] (larger for smaller γ), so (P6) forces v < 8.0·10⁻⁵ | Append to the paragraph: "(Heuristic bound from \texttt{Q1-1.md}, not refereed by RQ1-1/RQ1-2; audit D checks $D\ge D_{\mathrm I}+D_{\mathrm{IIs}}\ge6.2\cdot10^3$, hence $v<8.1\cdot10^{-5}$ from \textup{(P6)}, for every admissible parameter choice.)" |
| 11 | after lem:Estar-L4 | δ_tail < 2.3·10⁻⁸ at the unconstrained optimum; with δ_tail = 2·10⁻⁵, "the optimised range of v drops by less than 0.1% (numerical, not refereed)" | no (sec_T3 uses its own (PT), which is checked) | OK with fix (2.32344·10⁻⁸ confirmed. The δ_tail runs exist only for the data (1/2, 0.70, …) and (0.99, 4.25, …), not for the data of the "unconstrained optimum" in the same sentence. I re-verified both runs in 50 digits: all of (P0)–(P7_δ), (C0)–(C6) hold. Changes: −1.1·10⁻⁴ and +1.0·10⁻⁵, i.e. 0.011%. These are optimiser optima, not proven maxima) | Replace "the optimised range of $v$ drops by less than $0.1\%$ (numerical, not refereed)" by "the optimiser's $v$ for the data $(1/2,0.70,1/40,0.024,6.5)$ and $(0.99,4.25,1/40,0.024,6.5)$ changes by less than $0.1\%$ (numerical, local optimisation; not refereed)". |
| 12 | rem:Estar-status, Refereed | "The first report … located every implicit use of γ ≤ 1/4, K_f = 64, m = γ/50" | no | OK with fix (RQ1-1 lists the γ ≤ 1/4 uses; the search for K_f = 64, K_R = 32, m = γ/50 is RQ1-2 §2) | Replace "located every implicit use of $\gamma\le1/4$, $K_f=64$, $m=\gamma/50$ in the old proof and its replacement" by "located every implicit use of $\gamma\le1/4$ in the old proof and its replacement (the second report did the same for $K_f=64$, $K_R=32$, $m=\gamma/50$)". |
| 13 | rem:Estar-status, Refereed | Says the referees checked version 1 and lists the incorporated fixes. It does not say that the typeset text adds unrefereed material | no | OK with fix | Append: "The typeset text differs from version~2 of the claims only by notation (d→$\ESd$, χ→$\ESchi$, q→$\ESq$, f→$\ESf$, Ψ→$\ESPsi$, θ→$\bar\theta$, G→$G_3$, $\bar g$) and by the unrefereed remarks marked as such (the comparison with Theorem~\ref{thm:End}, the values from \texttt{Q4-1.md}, the ceiling, the $\delta_{\mathrm{tail}}$ cost)." |
| 14 | rem:Estar-status, near-pair paragraph | "(J1*) fails only far out of range (v = 5·10⁻²)" | no | OK with fix (the simulation tested only 5·10⁻⁵ … 5·10⁻²; it is evidence, not a statement) | Replace by "In the simulations (J1$\ESs$) was violated only at the largest tested value $v=5\cdot10^{-2}$." |
| 15 | rem:Estar-status, Use | "uses … Lemmas Estar-L1–L3 and (P7_δ) … (report Q4-1.md, interface check)": the source is unrefereed, and sec_T3 cites lem:Estar-L4 (l.135, 150, 176, 817, 829) | no | OK with fix | Replace "Lemmas~\ref{lem:Estar-L1}--\ref{lem:Estar-L3} and \textup{(P7$_\delta$)} (through a stronger condition of its own)" by "Lemmas~\ref{lem:Estar-L1}--\ref{lem:Estar-L4} (with \textup{(P7$_\delta$)} implied by its stronger condition (PT))", and "(report \texttt{Q4-1.md}, interface check)" by "(report \texttt{Q4-1.md}, interface check, not refereed; see Section~\ref{sec:T3})". |
| 16 | cor:Estar statement | Adds "with P(t_s)=x_{a_s}(t_s), b_E − a_s < 2π" explicitly | yes | OK (these are the standing setting of Construction C; claims v2 has them in §1) | none |
| 17 | proof of (c) | The covering of [a_j, b_E] is abbreviated: "last piece merged" leaves out the claims' explicit case "if 0 < U − u_{a_{j+1}} < ε/2, the single pair (a_j, b_E)" | no ((c) is unused) | OK (that case is a merge of the last piece) | Optional: after "last piece merged, label length $<3\varepsilon/2\le R$" add "; if $0<U-u_{a_{j+1}}<\varepsilon/2$ the single pair $(a_j,\EbE)$". |

## 2. Notes on the verdicts

**Note 2 (lem:Estar-gap with a set of times).** The proof needs only three facts. (a) Each leg contributes at most d_Lε of time; this
is true for any measurable subset of that leg. (b) The gaps attained on distinct legs differ by at least the sum of the
intermediate advances, which is ≥ ε/κ1 (Step 1(a)(α), including the first leg). Any subset of these gaps keeps that spacing.
(c) The monotonicity of h on the stated range. The argument never uses that 𝒯 is an interval. All applications (filters g ≥ g0,
the final segment {g ≤ ηR}, the near period) are covered. OK.

**Note 3 (special case).** At the table values (m = γ/50, s0 = 1/8, f = 3/8, κ1 = 9/8, c_A = 1/2, K_R = 32, K_f = K_ε = 64,
η = 1/2, q_c = 2, ν = 22v, d_L = A0 = 2), with γ = 0.01, …, 0.25, v = 2·10⁻¹¹γ² and vU/R = 2.5·10⁻⁷γ (the largest values that
thm:End allows; every condition is monotone in v and U/R):
- (ST*) is exactly (ST_γ).
- All of (P0)–(P7), (Pc) hold, for δ1 = 2 and also for δ1 = e^{2v/(1−v)}. c_amp ≤ 5.6 ≤ 22.
- Conclusions that match thm:End:
  - L_J ≤ 1.00000001 ≤ 1.01;
  - the advance range [8ε/9, ε] lies inside [ε/2, ε];
  - J − j_s ≤ 9U/(8ε) ≤ 2U/ε;
  - C_TL·γ ≤ 12.44 < 16.5 (8.66 as γ → 0), so (d) implies 0.33(λ_I/R)^γ;
  - c_0 = m²/2 = γ²/5000;
  - r_1 ≥ 0.413R ≥ R/8, and (S) is monotone in r_1.
- Only K̃ fails. With the tabulated δ1 = 2 the bound is 32.0003 + 10.89U/R. To imply thm:End's 17 + 19U/R it needs U/R ≥ 1.85.
- With δ1 = e^{2v/(1−v)} (admissible: δ1 ≥ 1 and (P1)), the bound is 16.0003 + 5.25U/R ≤ 17 + 19U/R. The "special case" then holds.

**Note 7.** The values 0.77 and 0.91 are recomputed exactly with Q1's formulas at Q4's rounded inputs. They are not refereed, but
they are correct and correctly labelled "not refereed" in the paper.

**Check (3): Status remark accuracy.**
- Correct as written:
  - "checked, in the form of version 1 of the claims, by two independent referees";
  - the list of incorporated corrections and "they change no constant and no side condition";
  - the simulation description: v = 5·10⁻⁵, 5·10⁻⁴, 5·10⁻³, U = 40R, 2560–5120 legs;
  - the binding set and the slacks;
  - 2vD_IIs ≈ 0.885 with 80% from II_β(g>0);
  - the R rounding;
  - "Neither report found a false claim or a gap".
- Inaccurate or incomplete:
  - the attribution in row 12;
  - "reproduced by both referees" for the four-data-set range (row 9);
  - the ceiling has lost its "not refereed" label (row 10);
  - the "Use" paragraph relies on unrefereed Q4-1 without saying so and omits L4 (row 15);
  - nothing discloses that the typeset text adds unrefereed material (row 13).
- RQ1-1's fix 8 (print parameters to ≥ 20 digits) is moot, because the paper prints no parameter vector.

**Nothing on the main path changed.** Theorem End* (a), (b), (d), (e), Corollary End*, the three auxiliary lemmas and L1–L4 are
typeset faithfully from v2. Their refereed proofs carry over unchanged.
