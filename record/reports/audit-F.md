# Audit F: short/ (v2) against short_v1/ and the round-9 refereed claims

**Objects compared.**
- `short/` (version 2) against `short_v1/` (version 1). Every `.tex` file was diffed with CRLF stripped.
- Sources: `referee/R9-tilt-claims.md`, `r9/near/prop_near.tex` and `referee/R9-far-claims.md`.
- Referee reports: `reports/referee-R9-{tilt,near,far}-{1,2}.md`.
- Optimisation sources: `reports/R9-opt.md`, `r9/opt/verify_v2.py` and `r9/opt/inputs_S1G_final.json`.
- The integrator's change log: `short/CHANGES_v2.md`.

**Classes.**
- (a) Transcription of a refereed claim, including its referee fix. Checked for fidelity.
- (b) Adaptation, i.e. new text. I refereed it myself.
- (c) Unrelated or accidental change.

**Verdicts:** OK / fix / GAP / FALSE.

## 0. Summary

- **No GAP and no FALSE item.** Every transcription matches its refereed source in hypotheses, constants, exponents, conclusions and steps. Each step was checked line by line.
- **Two small fixes are needed.**
  - **F-A.** The assembly-condition range is stale. It reads (A1)–(A6), although the proof now uses (A7) through Lemma 8.2.
  - **F-B.** Lemma 3.8(i), step (4), states the ratio range (1,q]. This is false in the trivial case J = I.
- **One citation to check:** F-C, [Higham, Thm 3.1].
- **One optional cosmetic point:** F-D.
- **Renames.** Renames A1–A20 are applied consistently. A grep for every deleted or renamed symbol finds no stale use with the old meaning:
  - `c_t`, `C_A`/`C_B` as tilt constants, `\CTL`, `\CmuA`, `\ConeA`;
  - bare `c_ρ`, `c_R`, `B_2U`, `B_3`, `B_5`, `C_p`, and `ρ_m` outside its definition;
  - `D_I`, `T_α`, `k_0`, `h_3`, `G_3`, `lem:Ns`, `s_τ`, μ := Mλ^γ, and r := R/λ.
- **Build.** The PDF is newer than every source. There are no `??` and no undefined or multiply-defined references.
- **Verifier.** `python -I verify_constants.py` was run on a copy in the scratchpad, so `short/` was not touched. It took 99 s, exited with status 0 and ended with **`ALL 218 CONDITIONS HOLD`**.
  - The regenerated `appA_tables.tex` is byte-identical to `short/appA_tables.tex`, apart from CRLF.
  - All 217 machine-parsable condition rows (left value, relation, right value) are numerically identical to `r9/opt/verify_v2_S1G.out`. The 218th row, the near D′(p_A) row, only fails to parse because its label is truncated in the v2 log; its value 64.63563 is the same.
- **Headline numbers.** The abstract, Theorem 1.1, Corollary 1.2, (A6), the proof of Corollary 1.2, Appendix A and the PDF text all say v0 = 5.8·10⁻³ and T0 = 13.1. No stale "10.13" or "6·10⁻⁵" remains in any `.tex` file or in the PDF.

## 1. Change table

| § / file | change | class | verdict | fix text (if needed) |
|---|---|---|---|---|
| preamble | `\vz` comment; `\aD` → α*_D; delete `\CTL \CmuA \ConeA \Ta \Tb \DI \DIIs \DIIl`; `\camp`, `\Xfar`, `\LJ` get stars; new `\CT \Cmu \rhoarc \Cfl \vv` | (b) | OK. Macro deletion means any stale use would fail to compile, and the build is clean. Starring `\LJ` applies far-1 F7(c) everywhere at once. | — |
| snitch.tex | Abstract: v ≤ 5.8·10⁻³ and time 13.1d; a clause on certification of the supremum constant D′; bibliography gains [HLP] and [Higham] | (a) numbers from opt; (b) clause | OK | — |
| sec1 | Thm 1.1 and Cor 1.2 numbers | (a) opt | OK | — |
| sec1 | Remark 1.3 rewritten (D′ certified; near-tight conditions); outline phrases | (b) | OK. This is commentary, not mathematics, and consistent with opt §0 and §6. | — |
| sec2 | Chord vector **v**_K and new Lemma 2.9 (split tilt) | (a) tilt §1 Lemma S | OK. (i)–(iii) are verbatim, with V → **v** (A3). Near's Lemma S is the special case used, as claimed. | — |
| sec2 | Lemma 2.10(v): arc distance ρ̲; bounds (a), (b); proof via δ, Wirtinger [HLP], integration by parts, Minkowski | (a) far §2.1 E* | OK. Constants π, π² and ρ̲^{-2}, ρ̲^{-3} match. Steps 0–6 are condensed but none is dropped. The remark ρ̲ ≥ ρ_m is kept. | — |
| sec2 | Lemma 2.11 Duhamel: α, β with π; α*_D(K) = 1 + 1/(πK) + 2/(πK)²; ρ̲ continuous | (a) far §2.2 Du* | OK | — |
| sec3 Def 3.3 | Tilt constants s(r), ω_r, r_*, C_T, C_μ | (a) tilt §0 | OK. Formulas are identical, and match `tiltc` and `CT_iv` in the script. | — |
| sec3 Def 3.3 | Far constants c*_ρ, c_η, c*_R, K_1, K_2, c*_amp, B′_2U, B*_2η, C′_p, C_p^V, C*_p, C_ar, Ĉ, B′_3 (with closed form), B*_5, ρ_𝒞, J_k^𝒞, J_k, X*_far, L*_J | (a) far §3 + tilt §0 (C′_p) + far-1 F6 | OK. Each formula was compared symbol by symbol with far §3 and with the script. The upper limit max(K_RR, U0/2) is far-1 F6. The range p̂ ∈ (−3/2, −1) follows from (P0). | — |
| sec3 Def 3.3 | Deleted c_t, C_A, C_B, C_TL, C_μA, C_1A, r_f, C_p, B_3, T_α, T_β, k_0, D_I, D_IIs, D_IIl; kept Ψ_I and T_I | (a) tilt-1 F5 / near-1,2 F1 / far-1 F7(a) | OK. No remaining use. | — |
| sec3 Def 3.3 | θ̄ := f_F² + 2v0D′ (Def 4.3) | (a) near-1/2 F3 | OK | — |
| sec3 Def 3.3 | (P0) K_ε ≥ 2; (P2)–(P5), (P7) starred forms; (P8) m²r_* < 4c_A | (a) near (N1), far §3, tilt (T1) | OK | — |
| sec3 Def 3.3 | (P2) adds c_η > 0 | (b) | OK. It is needed: Prop 4.2(ii), B*_2η and Prop 4.12 divide by c_η. The far claims omitted it. The script checks it for both tuples. | — |
| sec3 Def 3.3 | Remarks: ρ_𝒞 ≥ c*_R R > 0; J_k non-decreasing in U0; ω_r defined and increasing on [1, r_*] by (P8) | (b) | OK. Each is immediate. Monotonicity in U0 is used in the amplification step, as in far §2.6. | — |
| sec3 (H) | 𝒞 becomes a datum of the setting, with side conditions on (p, U0, 𝒞); new (S1G); "(S1), (S1G), (S2) at t_td" | (a) far §2.5 + (b) A7 | OK. With 𝒞 ≡ 0, (S1G) is void, ρ_𝒞 ≡ c*_R R and the second entry of J_k still bounds the integral. So making 𝒞 global loses nothing. | — |
| sec3 Thm 3.4(c) | One constant C_T for all J ⊂ I | (a) tilt §8 | OK. The completion in §4.4(c) is unchanged and cites Lemma 3.8(i). | — |
| sec3 Thm 3.4(d) | (S1G) clause | (a) far-2 F5 | OK. The completion's "(d) is Lemma 3.7" covers it via 3.7(iii). | — |
| sec3 Lemma 3.5(i) | "K_ε ≥ 3/2" → "K_ε ≥ 2" | (b) | OK. It only cites (P0). | — |
| sec3 Lemma 3.6(iv) | Unimodal gap–time bound, with the empty-range convention | (a) far §2.3 + far-1 F3 | OK, verbatim. | — |
| sec3 Lemma 3.7 | Split into (i)/(ii); new (iii); proof notes c(a_j,s;t) ≥ c(a_j,s;t_td) | (a) far §2.5 | OK. The max with c_A K_RR in (iii) comes from (i) with w > K_RR. | — |
| sec3 Lemma 3.8 | (o), (i) Cases A/B, (ii) (E-μ) with L² cap and L¹ form | (a) tilt §2 + tilt-1 F1, F2/tilt-2 F1 | (o) and (ii) are OK and verbatim. In (i), "(T1)" became "(P8)", and the added "(a_{j+1} − a_j ≤ l ≤ ε, as w ≥ 1)" is tilt-1's own justification. **(i) step (4) needs a fix: F-B.** | **F-B** below |
| sec3 locality principle | Adds "(S1G) at t_td only for these pairs (a_{j(t′)}, s)" | (a) far-2 F5 | OK | — |
| sec4 standing assumptions | Definition of ρ̲ | (b) | OK | — |
| sec4 Lemma 4.1 | Reduced to h_1 | (a) tilt-1 editorial | OK. h_3 and G_3 are unused. | — |
| sec4 Prop 4.2 | (i)–(iv); distance via Lemma 3.7(i), (iii); claim = Lemma (J); amplification; forcing with π; bounds (1)–(3); third term Φ(K_f) | (a) far §2.6 F*, Lemma (J) + tilt §4 (O3) inline (A9) + far-1 F6 | OK. I re-derived bounds (1)–(3): (1) gives C′_p exactly, (2) gives C_p^V, (3) gives C_ar. Also re-derived: β_f, the J_2 and B*_2η regimes, Φ non-increasing, and B′_3. A7 (dropping "under (S1G)" in (iii)) and A8 (g ≤ a ≤ Y for every pair) are correct. | — |
| sec4 Def 4.3 | D′, with the A11 specialisations C_V → C_μ^{1/2}, C* → 2C_T, C_A → C_T, C_μA → C_μ; P0 for θ ≤ 1 written as Ḡ(θ) | (a) near "Changes to Def 3.3" + (b) A11, A13 | OK. Each specialisation is valid under Lemma 3.8(i)/(ii): every tilt C_A or C_B is bounded by C_T, and C_μA = 1 + κC_T² = C_μ. The script's `Const` uses exactly CA = CB = CT, CTL = 2CT, C1A = (κC_μ)^{1/2}. | — |
| sec4 Lemmas 4.4–4.6, 4.9 | Near's Lemmas D, B, L, Σ | (a) | OK, apart from renames (m_λ, r_λ, ν′). Lemma 4.5 cites Lemma 3.8(ii) directly. | — |
| sec4 Lemma 4.7 | Near's Lemma O, routes 1–3, (ii), (iii)(a)–(c) with C_T/C_μ | (a) + near-2 wording fix + (b) final-leg sentence (tilt-1 F7 / tilt-2 F2 relocated, A12) | OK. I recomputed every 𝔭 entry and P0 branch. (iii)(c) uses only the first identity of Lemma 2.9(iii), which needs no shared end, so it is correct with J sharing the left end of I_0. The final-leg sentence is correct: the final leg is the single instant T_stop and P = x_β = x_a there. It is also redundant, since ϖ ≡ 0. | — |
| sec4 Lemma 4.8 | Near's Lemma A (σ, ρ → d₋, d₊) | (a) | OK | — |
| sec4 Prop 4.10 | Near's Prop 4.3″ | (a) | OK. The start value adds "≤ ½f_F²", which is the old step. | — |
| sec4 Lemma 4.11 | D′ ≤ 63.068 (p) and ≤ 64.6357 (p_A); cell scheme; "Arithmetic" paragraph | (a) near Lemma E + near-1 F4, F5 + (b) A14 | OK. 63.067903 ≤ 63.06791 ≤ 63.068 and 64.635629 ≤ 64.63563 ≤ 64.6357 (script). **Citation: F-C.** | F-C |
| sec4 Prop 4.12 | Far regimes with J_1, c_η, B*_5; "Near" paragraph inlined | (a) far §2.7 L* + near-1/2 F2 + far-1 F7(b) | OK. I re-derived B*_5 and the near increment vκT_Iλ. The far-1 F7(b) form c6ρ̄ ≥ max(c6ε, g) follows from Lemma 3.7(ii), since g < K_fλ ≤ K_RR. | — |
| sec4 §4.4 | "every use of (S1G) …" | (a) far-2 F5 | OK | — |
| sec5 | δ0 = 0.251113R; C_T^A replaces C_A^A and C_B^A; C3 := 2C_T^A | (a) opt + tilt-1 F4(b) / tilt-2 R1 | OK. Step 3 has two links per chain, so 2C_T^A κ_W = s is exact. (The claims' 3C_T^A was loose.) | — |
| sec5 | c_β gains 1/π; Thm 5.2(v) uses ρ̲ ≥ min z_s ≥ ζ(g̃+τ) | (a) far §2.2 drop-in + (b) A20 | OK. ρ_s ≥ z_s pointwise, so the arc version follows from the same bound. | — |
| sec6 | η = 0.11639 | (a) opt | OK. No other numeric use of η = 0.1 remains (grep). | — |
| sec7a | Fixed data v̄, η, ξ1, λ0, G_T | (a) opt (`inputs_S1G_final.json`) | OK. These match the JSON exactly. | — |
| sec7b Thm 7.12 | v ≤ 5.8·10⁻³ and printed constants | (a) opt | OK. They match the inputs and the 'out' rows. | — |
| sec7b Lemma 7.13 | Global chords, W_xL̂ ≤ 1.22122 | (a) far §2.4 T2* + (b) A15 | OK. The references are correctly remapped. The step (4/Δ′)^{2v} ≤ max(1, 4/Δ0)^{2v} ≤ (8/λ0)^{2v} is valid. 8/λ0 ≥ 1 and λ0 < 1 are both checked. | — |
| sec8 (8.1) | C_T^A defined; c0′; 𝒞(y); W_xL̂ | (a) far §2.5 + tilt-1 F4(b) | OK | — |
| sec8 (A1), (A2) | (P0)–(P8) for (p, U_max, 𝒞) and (p_A, U_A, 𝒞) | (a) | OK | — |
| sec8 (A6), (A7) | T♯ ≤ 13.1; new (A7): c0′ > 0 and 8/λ0 ≥ 1 | (a) opt + (b) A16 | OK as conditions. **The label and the proof still say "(A1)–(A6)": F-A.** | **F-A** |
| sec8 Lemma 8.2 | (S1G) at touch-down for any 0 < Ū ≤ U; printed κ_c and W_xL̂ are safe | (a) far §2.5 addendum + (b) generalisation | OK. d_c = a + U − b ≥ a + Ū − b ≥ y, and 𝒞 is non-decreasing. A smaller κ_c or a larger W_xL̂ only lowers 𝒞, because the sine is increasing on [0, π]. λ > K_RR ≥ ε/2 gives c ≥ φ(λ) ≥ c0′λ. | — |
| sec8 Prop 8.3 | Steps 1 and 6 cite Lemma 8.2; (P0)–(P8); coverage table; T̄ = 13.1 | (a) far-2 F5 | OK, apart from F-A. | F-A |
| appA | Inputs, script description, 218 = 2 + 56 + 13 + 72 + 12 + 37 + 26, J_k bounding, runtime, slack summary; C_TL example removed | (b) + tilt-1 F5 | OK. The counts match the run: 36 per tuple in core, and extra = 20 + 6. The slack statement checks: 32 conditions below 2·10⁻³, the next at 2.01·10⁻³, and (C2) and K_f + 1 ≤ K_R at 8.9·10⁻⁴. | — |
| appA_tables, verify_constants.py | Regenerated / ported | (b) | OK. The tables are identical to my run, and the condition values are identical to verify_v2. | — |

No class (c) (accidental or unrelated) change was found.

## 2. Referee fixes (each once, or justified)

| fix | status |
|---|---|
| tilt-1 F1 | Applied once (Lemma 3.8(o)). |
| tilt-1 F2 / tilt-2 F1 | Applied once as "(1,q]". The text is false for J = I (see F-B). |
| tilt-1 F3 | **Not applicable, and the justification is verified.** Lemma P (Φ_α, Φ_l, Φ_β, B) is absent from v2 (grep). It served only Prop 4.3′, which near's Prop 4.10 replaces. |
| tilt-1 F4(b) / tilt-2 R1 | Applied once (sec5, sec8). |
| tilt-1 F5 | Applied. (T1) is (P8); (T2)–(T4) are in 'extra'; the two old extras and the appA example are gone; C_T, C_μ, C′_p, B′_3, B*_5 are in Table A.1. The Π- and T_l-entries concern Prop 4.3′ and are not applicable. |
| tilt-1 F6 | **Not applicable, and the justification is verified.** S_0, ∫B and D_IIl″ are absent from v2. θ̄ uses D′. |
| tilt-1 F7 / tilt-2 F2 | Applied once, relocated to Lemma 4.7(iii) (A12). This is valid. |
| tilt-1 editorial | Applied (Lemma 4.1). |
| tilt-2 R2 (optional) | Not applied. This is acceptable. |
| near-1/2 F1, F2, F3; near-1 F4, F5; near-2 wording fix | Each applied once. |
| near-2 F4 | Superseded by near-1 F5, since the bound is now certified. Correctly omitted. |
| far-1 F3, F6, F7(a)(b)(c) | Each applied once. F7(c) is applied via the macro, and the lemma is correctly identified as 3.10. |
| far-2 F5 | Applied in all three requested places. |
| far-2 F8 | **Justification verified.** The values 1.53, 4.13, 0.064, 1.508, 4.188 and 0.0653 occur nowhere in v2. All v2 constants are computed by the script from the formulas. |
| far-2 F9 | Applied in substance. The whole touch-down row is re-verified at v̄ = v0 = 5.8·10⁻³, together with (C4) and (A3)/(A4) at the new c_sep and G_T. |

## 3. (T2)–(T4) and script coverage

- **(T2)–(T4).** C_μ ≥ (1+2γ)κ/c_A, γ ≤ c_A/κ and K_f(2γ−1) ≤ 3c_A/κ appear only in `verify_constants.py` (lines 551–553, group 'extra') and in the appA sentence saying the proofs do not use them.
  - I grepped every `.tex` file for c_A/κ, (1+2γ), 2γ−1, B(x), Φ_β, Φ_l and Lemma P. Nothing in any proof matches.
  - The labels (T1)–(T4) in v2 are Theorem 7.12's own items, which are unrelated.
  - In the claims, they were used only by Lemma P (P4), which is not in v2. **The claim holds.** Keeping the 6 checks is harmless (U1).
- **Coverage.** Every numeric condition that a v2 proof uses is checked:
  - (P0)–(P8) for both tuples, including K_ε ≥ 2, K_f ≥ 3, K_f + 1 ≤ K_R, η1 ≤ K_f/(K_f+1), γ + ν < 1, κ ≤ 4/3 (which gives 1.03κ < 2 in Lemma 4.11) and c_η > 0;
  - (P1) v ≤ 1 − 1/d_L (Lemma 4.8);
  - the certified D′ ≤ printed (2);
  - (SC41)–(SC44) and λ0 < 1 (Lemma 7.13);
  - (A7) (Lemma 8.2);
  - W_xL̂ (up), κ_c (down) and the other outward roundings;
  - (C1)–(C6) and (A2)–(A6).
- **Facts that need no check.** a′ > 0 (used in c0′) follows from (C5). K_RR ≥ ε/2 follows from (A6).
- **Run.** The verifier ends with `ALL 218 CONDITIONS HOLD` and exit status 0.

## 4. Exact fix texts

**F-A (sec8.tex, two places).** The proof of Proposition 8.3 uses Lemma 8.2, which assumes (A7).
- Line 38: replace `\namedlabel{hyp:A}{(A1)--(A6)}` by `\namedlabel{hyp:A}{(A1)--(A7)}`.
- Line 104: replace "We use the conditions (A1)--(A6)." by "We use the conditions (A1)--(A7)."

**F-B (sec3.tex, Lemma 3.8(i)).** When J = I, K = 1 and the ratio is 1, which is not in (1,q]. The changelog's argument "λ_{K−1} > λ_J" needs J ≠ I.
- After "(i) Let $J=(a',b')\subset I$," insert "If $J=I$ there is nothing to prove, so let $J\ne I$;".
- Alternatively, replace "$\lambda(I_{K-1})/\lambda_J\in(1,q]$" by "$\lambda(I_{K-1})/\lambda_J\in[1,q]$", which is tilt-1 F2's text.
- Only "≤ q" is used, so no conclusion changes.

**F-C (sec4.tex l.358, check only).** I could not confirm that "\cite[Thm.~3.1]{Higham}" (inherited from near-1) is the right locator in Higham, 2nd ed. The standard bound is Lemma 3.1 (|θ_n| ≤ γ_n) together with the recursive-summation bound of §4.2. Suggested text: "\cite[Lemma~3.1 and \S4.2]{Higham}". The inequality itself holds: γ_{5·10⁴} ≈ 5.6·10⁻¹² < 10⁻¹¹.

**F-D (optional, cosmetic).** In the proof of Lemma 3.8(o), the local "ρ := λ_I/λ_J" (inherited from tilt §2) shadows the distance ρ. It is harmless because it is local. It could be renamed, e.g. "$\varrho_0:=\lambda_I/\lambda_J$" with ρ̃ becoming ϱ̃. Not required.
