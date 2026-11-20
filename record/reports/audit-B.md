# Audit B — unrefereed deltas in the typeset sections sec_T1, sec_T2, sec_E, sec_B, sec_ST

Date: 2026-11-19. Auditor B. Nothing under `paper/`, `referee/` or the referee reports was edited.

## 0. Result

* **No FALSE statement and no GAP was found in any delta.** Every delta on the path to `thm:Main` re-derives; the
  constants of `thm:Main` (v₀ = 4·10⁻⁵¹, T₀ = 19.69, vision radius min(ε, 2·10⁻⁴⁴)) were recomputed independently and
  every side condition holds with the rounded values actually stated.
* **Text fixes needed: 13** (table, verdict "OK with fix"). None changes a theorem. Three are on the main path
  (T2-1, T2-2, E-1) and all three are wording, not mathematics.
* **All five Status remarks overstate the refereeing** (§3). The reports were written against earlier versions of the
  claims; the passages changed afterwards were seen by one referee or none. The worst single sentence is the last one
  of `rem:E-status` ("the start data are not yet proved in this paper"), which contradicts `thm:HT`/`thm:Main`.
* `rem:B-relaxed` and `cor:E-T` are **confirmed NOT used** by `thm:Main`, directly or transitively (grep over
  main.tex, sec_T1, sec_T2, sec_E, sec_ST; sec_T2 l.793–795 and l.839–841 say so and are right).

How the work was done. sec_T1 and sec_T2 (main path) were audited by me line against line with the claims files, with a
numeric-token diff of tex against claims (`code/audit/numdiff.py`) and a word diff of the claims versions
(`code/audit/worddiff.py`). sec_E, sec_B, sec_ST were audited by three independent sub-auditors under my brief; I
spot-checked their quotations of the tex (Status remarks, sec_B l.119, l.540, l.684–693, sec_E Step 3) and they are
accurate. What was **not** re-derived is listed in §4.

A point of method that matters for §3: for sec_T1 and sec_T2 most "known deltas" are not typesetter inventions. They are
already in the final claims file (P8a v3 changelog items 1, 10, 11; P8b v2 changelog item 8), which the referees never
saw — they refereed P8a v2 and P8b v1. So the unrefereed set is "claims vN−1 → tex", not only "claims vN → tex".

## 1. Table of deltas

Verdicts: OK / OK with fix / GAP / FALSE. "Main path" = used in the proof of `thm:Main` (or `cor:Exact`).

### sec_T1 (← P8a-claims v3 ← v2; RP8a-1, RP8a-2). Whole section is on the main path through `thm:HT`.

| # | Statement (line) | Delta | Main path | Verdict | Fix |
|---|---|---|---|---|---|
| T1-1 | `lem:T1-tail`(b) proof, l.660–664 | v2: "h(t_s) ≤ −0.994x + 3.4·10⁻⁷ε ≤ 0 for x ≥ 0.35vε" (false for v < 9.8·10⁻⁷, i.e. almost the whole range). Now (1−v²)ω(t_s) ≤ (1+v)vε/(3(1−v)) ≤ 0.3334vε ≤ 0.994·0.35vε | yes | **OK**. (1+v)/(3(1−v)) ≤ 0.33334 for v ≤ 10⁻⁶; 0.994·0.35 = 0.3479 ≥ 0.3334. h ≤ 0 ⇒ cos β ≤ −v, minimum C/g_max ≤ ε passed in run 2 (cos b > v at t₁ since b ≤ 0.0034). The two ranges [0.35vε, ξ_e] and (0, ε/2] cover (0, ξ_e]. Second range re-derived too (0.49ε, 3.74/ε, 0.3127, 0.0491, ε − 0.89ξ). RP8a-1 l.87 computes the same threshold 0.3354vε | — |
| T1-2 | `lem:T1-tang`(b), l.393–394, 443–445 | "0 < t_c − t_s" strict (v2: "0 ≤"); `lem:T1-hole`(a) correspondingly drops the case "t_s = t₂" | yes (u = 0 is a ghost label; 𝒢 ⊂ [0,U)) | **OK**. f(σ) = (σ/ε)(2 − σ/ε) < 1 on [0,ε), integrand v(1−f)/((1−v)(1−vf)) > 0; ∫₀^ε(1−f) = ε/3 | — |
| T1-3 | `lem:T1-run1`(d), l.337–347 | new proof, θ_s ≤ 0.51vε (v2: vε, proof gave 1.2vε) | yes, weakly (only through y_s in `lem:T1-edges`, itself not used by `thm:HT`) | **OK**. y_s^{1+v} = εg_max(2(1+v))^v[B₁B₂]^v exactly; B₁ ≤ 1 + 2.205ε²/(1−v²) ≤ 1 + 0.0023ε; B₂ ≤ 1 + 1.000001ε/(2(1−v)) ≤ 1 + 0.5001ε; product ≤ 1 + 0.5025ε; Bernoulli with exponent v/(1+v) < 1 | — |
| T1-4 | `lem:T1-elem`, l.84–97 | new lemma: (a) = `lem:ST-D0`(c) and (b) = N² ≤ ∫\|T−û\|² of `lem:E-facts`(b), for arbitrary C¹ unit-speed curves | yes ((T1), far and near case) | **OK**. (a): \|ψ(s) − ψ_m\| ≤ K\|s − l/2\| ≤ π/2, c ≥ ∫cos(K\|s−l/2\|) = (2/K)sin(Kl/2) ≥ l − K²l³/24. (b): \|γ′−û\|² = 2(1 − γ′·û). Both proofs complete as written | — |
| T1-5 | `rem:T1-assembly`(4), l.1119–1122 | D₁ remark reworded: "the *method* of `lem:T1-run1`(d)", "with h₁ = cos α + v − (1−v²)t₁" | no (D₁ = 1 fixed) | **OK**, and more accurate than v3: for general D₁ the formula of (d) changes (|h₁| = (1−v²)D₁ + 1 − cos α). (a): h₁ = cos α − 1 − (1−v²)D₁ < 0 for all D₁ > 0. `lem:T1-tang`(a): the identity h₁(cos θ − v) + sin²θ = (1−v²)(1 − t₁(cos θ − v)) holds for every t₁ | — |
| T1-6 | `lem:T1-tang`(b) l.394–395; `lem:T1-bulk`(a) l.726 | added "and so has every true candidate while it exists"; "The same holds for its true candidate" | yes (`lem:T1-hole`(c)) | **OK** (speed v; same proof). v3 had this inside the proof of Lemma 11(c) | — |
| T1-7 | `lem:T1-bulk`(c) proof, l.760 | added "an interval of length < 0.02 is contained in an interval of length 0.02 of the same arc" | yes ((T2), eq. T1-len) | **OK** (both arcs are longer than 0.02) | — |
| T1-8 | Notation renames (header l.8–17) | x → ξ, t₂ → t_c, δ(t) → ω(t), x_θ → q, S → L, a, c → 𝖺, 𝖼, etc. | — | **OK**, consistent throughout. Numeric-token diff tex/claims: no constant differs | — |
| T1-9 | Mandated fixes R1 F1–F6, M1; R2 F1–F4 | — | — | all applied, each once (2.66414; cos b − v chain; 4.9063; 2.002003; sign at E∓; α = π; 𝒢 ⊂ [0,U)) | — |
| T1-10 | `rem:T1-status`, l.1126–1136 | see §3 | — | **OK with fix** | §3 |

### sec_T2 (← P8b-claims v2 ← v1; RP8b-1, RP8b-2). Whole section is on the main path.

| # | Statement (line) | Delta | Main path | Verdict | Fix |
|---|---|---|---|---|---|
| T2-1 | Table `tab:T2-const`, `thm:Main` proof, eq. (T2-const) | all final constants recomputed with the refereed (H_T) constants (ϑ_T = 3.3, U_max = 6.5, T₂ = 3.74). **No referee computed these numbers**: RP8b-1 §4 tabulates the N8 set and the interim set (v₀ = 1.61·10⁻⁵¹); only RP8a-1 l.179 has T₀ = 19.69 | yes | **OK**. Independent recomputation (`code/audit/secT2_constants.py`, 80 digits, not importing the authors' script): R_A = 5.2816·10⁻⁷, M_A = 0.18547, ϑ_h = 16.704, W = 1.9113·10⁻¹¹, C_I = 25.368, Λ_I = 4.7783·10⁻¹³, c_I = 2.1237·10⁻¹³, R_B = 2.0713·10⁻⁴², v₀ = 4.1426·10⁻⁵¹, ε_* = 2.1966·10⁻⁴⁴, T₀ = 19.69; binding entries as stated. All 16 groups of side conditions used in `lem:T2-StA`, `prop:T2-I`, `prop:T2-cond` hold **with v = 4·10⁻⁵¹, ε = 2·10⁻⁴⁴**. **Fix (caption only):** `final_constants.py` checks (4.1·10⁻⁵¹, 2.1·10⁻⁴⁴) and (10⁻⁵¹, 10⁻⁴⁴), not the values the caption names | Caption l.750: replace "with the rounded values $v=4\cdot10^{-51}$, $\varepsilon=2\cdot10^{-44}$" by "with the exact values, with $(4.1\cdot10^{-51},2.1\cdot10^{-44})$ and with $(10^{-51},10^{-44})$; the conditions are monotone in $(v,\varepsilon)$, so they hold for $(4\cdot10^{-51},2\cdot10^{-44})$" — or add that pair to the script |
| T2-2 | `lem:T2-W`(d) proof, l.116–121 | not a typesetter delta (in v1), but wrong as typeset: "The proofs of thm:End and cor:End cite Section sec:bulk only through Lemmas …". The typeset proof of `thm:End` also imports, by reference, computations from the proof of `thm:Bulk`: eq. (B-1c) and (B-star) "with the same proof" (sec_E l.205, 213), the Step 3 forcing bound β ≤ 408vλ^{3/2}/R² (l.282), the Step 4 times 264λ / 272λ / 536λ (l.330, 402). `rem:T2-budget`(4) likewise says thm:Bulk is "not used" | yes | **OK with fix**. I read the four imported passages (sec_B l.440–447, 515–522, 547–549, 623–627): they use only l ≤ 2λ, \|p_a\| ≤ ρ_m + l, the bounds on ρ_m, gap spacing ≥ ε/2 and leg duration ≤ 2ε — static geometry and facts available on a working front — so the conclusion of (d) stands | l.116–118: after "Lemma~\ref{lem:B-C}(0),(2),(3),(4)" insert ", the elementary computations of Steps~1(c),(d), 3 and~4 of the proof of Theorem~\ref{thm:Bulk} that are quoted there (they use only the geometry of a pair, the spacing of the gaps and the duration of a leg)". l.794–795: "Theorem~\ref{thm:Bulk}" → "the statement of Theorem~\ref{thm:Bulk} (three computations of its proof are quoted in the proof of Theorem~\ref{thm:End})" |
| T2-3 | `thm:Main`, l.702–731 | restated unconditionally; path run "for the vision radius min(ε, 2·10⁻⁴⁴)" (claims: min(ε, ε_*), ε_* = 2.1966·10⁻⁴⁴; that device is in v1 and was refereed, RP8b-1 §4) | yes | **OK**. With ε″ := min(ε, 2·10⁻⁴⁴) ≤ ε_* ≤ ε_T and v ≤ 4·10⁻⁵¹ ≤ v₀ ≤ v_T: `thm:HT` gives (H_T) at (v, ε″); the proof of `prop:T2-cond` (case "ε ≤ ε_*") gives every true candidate within ε″ ≤ ε by T_stop ≤ T₀. True candidates do not depend on the vision radius. For ε between 2·10⁻⁴⁴ and ε_* the path differs from the one named in `prop:T2-cond`, which is harmless and is said in the proof (l.726–728). Scaling in d checked | — |
| T2-4 | `prop:T2-cond`, l.670–700 | new statement (claims: Theorem P8.M); adds "T_stop ≤ t_td + 2.1W + 2.25U_max/(1−v) ≤ T₀" | yes | **OK**. 2·(9/8)U_max = 2.25U_max; 3.74 + 4·10⁻¹¹ + 14.625/(1−v) ≤ 19.69. cor:End as typeset (sec_E l.511–527) is invoked with exactly its hypotheses in both stages (U_max/2 resp. (9/8)U_max in the role of its U_max; γ, R formulas agree; c_I/16 = Λ_I/36) | — |
| T2-5 | `lem:T2-H` setting and Step 3, l.444, 484, 510 | "v ≤ 2·10⁻¹¹γ₁² ≤ 10⁻⁴" stated; "Step 3 empty for j = j_s" (R1-F7) | yes | **OK**. v ≤ 2·10⁻¹¹γ² is a hypothesis of `thm:End` as typeset (sec_E l.139). 8.04·2^{1/4}·10⁻⁴ = 9.6·10⁻⁴ ≤ 10⁻³. For j = j_s: Λ = ε, I has label length ε, J ⊂ I, t_j = t_s, nothing to rotate | — |
| T2-6 | `prop:T2-I`, case (P), l.626–634 | new intermediate constant 1.0005 and "1.0005·1.0001^{3/2} ≤ 1.001" (claims: 1.001 twice, "constants rounded up") | yes | **OK**, and tighter than the source. e^{14.44v}·131.25 ≤ 1.0005·132; enlarged pair: N(a,b) ≤ N(enlarged) (`lem:E-facts`(a)), ε/2 ≤ λ^I, l_{t_I}(enlarged) ≤ 1.0001λ^I | — |
| T2-7 | l.207, 617–619 | "W ≤ R_A/2 ≤ c_sep/32 and W ≤ 10⁻⁴" (claims: W ≤ R_A ≤ c_sep/16) | yes | **OK** for all admissible (H_T) constants: W ≤ R_A·10^{−1/γ_*}/2.1 ≤ R_A·10⁻⁴/2.1 | — |
| T2-8 | `lem:T2-StA` (new lemma = "Stage A" + "(a)" + "Departure of the tail" of the proof of P8.I) | restructuring; statements (a)–(d) made explicit | yes | **OK**; every numbered hypothesis of `lem:T2-H` and (Q0)–(Q4) checked numerically and symbolically (a_* ≤ 4.11W) | — |
| T2-9 | `hyp:HT` vs `thm:HT` | interface | yes | **OK**: (T0)–(T5), the definition of true/ghost label and all twelve constants agree verbatim; ranges a′ ≤ 1, λ₀ ≤ 1/4, c_sep ≤ 1, γ_T ≤ 1/4, G_T ≤ 1, T₂, U_max ≥ 1 hold | — |
| T2-10 | `cor:Exact`, l.754–775 | ε_N := 2^{−N}·2·10⁻⁴⁴ (claims: 2^{−N}ε_*); hypotheses of `lem:A41` listed one by one | yes | **OK** against `lem:A41` as typeset (main.tex l.238–242) | — |
| T2-11 | Renames (D0)…(D3) → (Q0)…(Q4), 𝔡 → 𝔭, Θ → Θ₀ etc.; `thm:T2-D` and `lem:T2-A` | — | yes | **OK**: numeric-token diff shows no constant of §§2–4 changed; statements compared. Proof of `thm:T2-D` not re-derived (§4) | — |
| T2-12 | Mandated fixes R1 F1–F7, R2 F1–F5 | — | — | all applied (proviso in W(c),(d); 𝒢 ⊂ [0,U); D₁ = 1; (9/8)U_max; H(0) = 0) | — |
| T2-13 | `rem:T2-status`, l.798–818 | see §3 | — | **OK with fix** | §3 |

### sec_E (← P7-claims v2 ← v1; RP7-1, RP7-2)

| # | Statement (line) | Delta | Main path | Verdict | Fix |
|---|---|---|---|---|---|
| E-1 | `rem:E-B`(4), l.487–492 (causality) | new (RP7-2 F3/F10 only); cited at sec_T2 l.450, 569 | **yes** | **OK with fix**: the claim is immediate, but its justification is an assertion about the whole proof | Replace "Every step of the continuity argument … any prefix of the construction. Hence," by "Let $\tilde P$ equal $P$ on $[0,t_j]$ and continue the construction after $t_j$. The candidates at times $\le t_j$ are the same for $P$ and $\tilde P$, and Theorem~\ref{thm:End} applies to $\tilde P$. Hence," |
| E-2 | Family at switching times, l.131–136 | 𝔉(t_j) := family of leg j (RP7-2 F1 only) | yes | **OK**; every use checked | — |
| E-3 | Step 3, l.273–317 | ĝ₂ = min(g₂, 32R), case g₂ > 32R (RP7-1 F1 only) | yes | **OK** (346, 5.47, 0.0408, 1.4·10⁻⁸ recomputed; 16R − R/32 − 2R = 13.97R) | — |
| E-4 | Arguments quoted from the proof of `thm:Bulk`, l.205, 213, 282, 330, 402 | already so in v1; both referees saw that form | yes | **OK**: same hypotheses and constants available in sec_E (389.9 ≤ 390, 0.04, 264λ, 270.9λ, 534.9λ). See T2-2 for the consequence in sec_T2 | — |
| E-5 | Step 4, l.338–341, 387 | log⁺(λ/6ρ̄) ≤ log⁺(λ/g̃) written out | yes | **OK** | — |
| E-6 | `cor:End`, l.511–539 | quantifiers, U_max, leg-start hypothesis | yes | **OK**; (S1)–(S3) re-derived | — |
| E-7 | `cor:E-T`, l.837–900 | time-dependent ρ₀(t): U_Γ ≤ min ρ₀/5, v∫dt/ρ₀ ≤ 1/200, bound 2.8·v∫dt/ρ₀²·λ₁^{3/2}; also v ≤ γ₁/14, a′ = γ₁/2 | **no** | **OK**. 1.03e^{1/200} ≤ 1.036, 1.036/5 ≤ 1/4 (hypothesis of `lem:E-far` pointwise in t); 2.9·0.96·1.007 = 2.803; 2.6·1.036^{3/2} = 2.742 ≤ 2.8. 2·10⁵ random parameter sets, 0 failures | — |
| E-8 | `prop:E-trans`(iii), l.926–931 | upper bound only if vμ < 1; lower bound only if also 2ζ^{1−v} ≤ 1 | no (never referenced) | **OK** (sufficient, not necessary; 1.6·10⁵ grid points, 0 violations) | — |
| E-9 | `lem:E-H`, l.805–806 | "holds as soon as U_E + D ≤ R₁·20^{−1/γ₁}" | no | **OK** (the old "reads" was wrong; exact threshold 19.2^{−1/γ₁}) | — |
| E-10 | `thm:End`(c) proof, l.455–466 | splitting of [a_j, b_E] made explicit | no (sec_T2 l.794) | **OK with fix**: a piece of length R merged with a remainder < ε/2 exceeds R | "have label lengths in $[\varepsilon/2,R]$, a last piece …" → "have label length $\varepsilon$, a last piece shorter than $\varepsilon/2$ being merged with its predecessor (label length $<3\varepsilon/2\le R$)" |
| E-11 | `rem:E-restart`(2), l.557 | clause "as long as U − u_{a_j} ≥ ε/2" of v2 dropped | no | **OK with fix** | append ", again for $U-u_{a_j}\ge\varepsilon/2$" |
| E-12 | Intro l.31 | "shows that some loss is real" without the qualifier of `prop:E-depsharp` | no | **OK with fix** | "shows that the chord tilts from the end do lose an exponent $v/(1+v)$" |
| E-13 | `thm:E-dep` (M₀ ≤ ϑ₀ hypothesis), `rem:E-D2`, `rem:E-restart`(1),(3), `rem:E-B`(1) | new or reworded after the reports | no | **OK** (6.04, 104.9 ≤ 106, 8.2/e, exponents 2.25/3.25 ≤ 3.3) | — |
| E-14 | `rem:E-status`, l.982–1020 | see §3 | — | **OK with fix** (one sentence false) | §3 |

### sec_B (← P6a-claims v4 ← v3; RP6a-1, RP6a-2 — both written against v2, which is not in the repository)

| # | Statement (line) | Delta | Main path | Verdict | Fix |
|---|---|---|---|---|---|
| B-1 | Step 3 forcing, l.515–521 | R1's text, recomputed: 390, 0.04, 408 | **yes**, by reference from sec_E l.282 | **OK**: 2·2^{3/2}·(14/13)·64 = 389.888; 2/13.96875 = 0.1432 ≤ 0.144; 2·2^{3/2}·1.144/13.9² = 0.0335 | — |
| B-2 | Step 3 ρ_m chain, l.497–506 | restructured | sec_E has its own copy | **OK** | — |
| B-3 | Step 1(c) proof of (B-1c), l.446–447; Step 4 times, l.547–549, 623–627; `lem:B-C`(0), l.260, 275 | typesetter additions / "two legs" fix / R2-F1 text | **yes** (sec_E l.205, 330, 402; sec_T2 l.86, 112) | **OK** (256λ + 4ε ≤ 264λ; 264 + 8/e + 4 = 270.94; w ≤ e^{2vT/ε}) | — |
| B-4 | Sentence after `lem:B-1`, l.119–120 | "Parts (ii)–(iv) are not used below" | (ii), (iii) are used at sec_T1 l.63, sec_T2 l.81, 330, sec_ST l.197 | **OK with fix** (true only inside sec_B) | "Parts (ii)--(iv) are not used in this section; (ii) and (iii) are used in later sections." |
| B-5 | `rem:B-relaxed`, l.674–694, main claim | unrefereed: `thm:Bulk`, its consequence and `cor:M` under (W1)–(W3) | **no** (sec_E l.470–477 cites it for comparison only; `thm:End` has its own hypotheses and proof) | **OK**: (ST) enters the proof only through (CA) at t_s, the start of (I1)/(I2), the start value of near pairs, N(t_s) in Step 3 and ε ≤ R/64; exponent 44v = 2ν; (ST) ⇒ (W1)–(W3) | — |
| B-6 | `rem:B-relaxed`, parenthesis l.684–686 | uses (min(g_s,32R)/g₂)^ν also for g₂ > 32R | no | **OK with fix** | "$A_0(\min(g_{\mathrm s},32R)/\hat g_2)^\nu N(\Bts)\le2\cdot\frac M8\lambda^{3/4}\bigl(\min(\min(g_{\mathrm s},32R),64\lambda)/\hat g_2\bigr)^\nu\le\frac M4\lambda^{3/4}$, $\hat g_2:=\min(g_2,32R)$" |
| B-7 | `rem:B-relaxed`, last sentence l.692–693 | "both reports only suggest …" | no | **OK with fix** (inaccurate: only R2 §4(2) suggests that start; R1 §7 suggests "(IC1) for ε/2 ≤ λ ≤ 32R plus (CA)") | "…; the second report (\S4(2)) suggests only the start `$E\le M^2\lambda^{3/2}/128$ for family pairs, plus \eqref{eq:B-CA}' (without the gap factor of (W2)), and the first (\S7) only `(IC1) for $\varepsilon/2\le\lambda\le32R$, plus \eqref{eq:B-CA}'." |
| B-8 | Step 3 amplification display l.510–513 and Result l.535 | not a delta; the text's derivation covers only g₂ ≤ 32R, the Result uses it for all g₂ ≥ 64λ | no (sec_E l.273–280 has the corrected form) | **OK with fix** (final bound unaffected) | use sec_E's wording with $\hat g_2:=\min(g_2,32R)$; in the Result write $(32R/\hat g_2)^\nu\le\max(1,R/(2\lambda))^\nu\le(R/\lambda)^\nu$ |
| B-9 | Step 3, l.540 | not a delta; rounding slip both referees missed: 6.07·64^{−3/4} = 0.26826 > 0.268 | no | **OK with fix** (downstream 1.33·10⁵·0.2683 ≤ 3.6·10⁴ still holds) | "$g_2^{-3/4}(1/16+6)=6.0625\,g_2^{-3/4}\le6.0625\,(64\lambda)^{-3/4}\le0.268\,\lambda^{-3/4}$" |
| B-10 | 42.12, 90.94 (Step 2); 218.12 ≤ 219 (Step 4 merged insert, l.596–605); Step 5 arithmetic; `rem:B-B`(4); `cor:M` restructured; scope of `thm:Bulk` (R2-F3); (IC1) range | reconciler's choices and post-report text | no | **OK** (6.7/(1 − 2^{−1/4}) = 42.1109; 183.414·2^{1/4} = 218.12; 5.70105 ≤ 5.702; 5015.8 ≤ 5016; 1/((1−v)·0.49) ≤ 2.1) | — |
| B-11 | `rem:B-status`, l.746–750 | see §3 | — | **OK with fix** | §3 |

### sec_ST (← P6d-claims and Claim 1 of P6c-claims; RP6d-1 covers Claim 1 (a)–(g), RP6d-2 covers (a),(b),(e),(f),(g))

| # | Statement (line) | Delta | Main path | Verdict | Fix |
|---|---|---|---|---|---|
| ST-1 | `lem:ST-D0`(a), l.186–200 | one added line (Γ\|sin φ cos φ\| ≤ \|p\|/m_ε²) | **yes** (sec_T1 l.706, `lem:T1-virt`); stated for any 1-Lipschitz path, so the use matches | **OK** | — |
| ST-2 | `lem:ST-D3` preliminary, l.381–387 | α_s ≤ 2.1ε moved here from Theorem D item 1 (now under D3's hypotheses only) | no | **OK**; the move repairs a silent use in the source | — |
| ST-3 | `lem:ST-front`(g) proof, l.152–156 | proof without part (d) | no | **OK** (identity checked to 10⁻³¹) | optional: add "and β is continuous at π" |
| ST-4 | `lem:ST-D2` statement, l.324–334 | stated for the true front; new sentence on the virtual front | no | **OK** (tested also for α_s > δ/2: min ratio 1.04) | — |
| ST-5 | `rem:ST-more`(3), l.588–590 | new remark | no | **OK** | — |
| ST-6 | `lem:ST-front`(e), l.90 | "every virtual field" — the proof needs the field Lipschitz | no (sec_T1 re-proves its own version) | **OK with fix** | "of \emph{every} virtual field that equals" → "of \emph{every} Lipschitz field that equals" |
| ST-7 | `lem:ST-D1` "Virtual front" paragraph; `lem:ST-D0`(b) Gronwall line; `cor:ST` (T) per leg; parentheticals in `thm:ST` | post-report text | no | **OK** (all constants recomputed: 2.171, 1.0886, 3.59, 204.1, 1.0010297, 15.4911) | optional: move the numerical sentence l.513–514 out of the theorem environment |
| ST-8 | `rem:ST-status`, l.593–598 | see §3 | — | **OK with fix** | §3 |

## 2. What `thm:Main` actually uses from the older sections

* sec_B: lemmas B-V, B-VC(a),(b) (and (c) via its proof), B-1(i)–(iii), B-2, B-3(a),(c),(d),(e), B-4, B-C(0),(2),(3),(4);
  and, **by reference from the proof of `thm:End`**, four computations inside the proof of `thm:Bulk` (B-1, B-3 above).
  Not used: the statements of `thm:Bulk`, `thm:R`, `cor:M`, and `rem:B-relaxed`.
* sec_E: `lem:E-facts`, `thm:End`(a),(b),(d) with (E-CA), (E-star), `rem:E-B`(4), `cor:End` (twice). Not used: `cor:E-T`,
  `thm:E-dep`, `lem:E-H`, `rem:E-restart`, `thm:End`(c), `prop:E-trans`, `rem:E-D2`.
* sec_ST: only `lem:ST-D0`(a). Everything else sec_T1 needs from there is notation or re-proved (`lem:T1-elem`).
* There is no place where a bulk-type theorem is invoked with a start satisfying only relaxed conditions.

## 3. Accuracy of the Status remarks

**`rem:T1-status`.** Accurate that both verdicts are "OK with text fixes". Three inaccuracies:
1. "checked by two independent referees" is true of P8a v2. The proof of `lem:T1-run1`(d), the repaired step of
   `lem:T1-tail`(b), the strictness in `lem:T1-tang`(b) and `lem:T1-elem` were written afterwards (items T1-1 to T1-4).
2. "One further rounding slip … (the threshold 0.35vε)" understates it: the inequality in the v2 proof was false for
   v < 9.8·10⁻⁷. The statement was unaffected.
3. "Lemma T1-elem … both referees re-proved them" is wrong: RP8a-1 l.212–213 re-proved both facts; RP8a-2 l.5–6
   took them "as cited".
   Fix text, l.1133–1136: "One step of the proof of Lemma~\ref{lem:T1-tail}(b) (the range $\xi\ge0.35\,v\varepsilon$) used an
   inequality that fails for $v<9.8\cdot10^{-7}$; it was repaired after the reports (the first report contains the correct
   computation), and the statement is unchanged. Lemma~\ref{lem:T1-elem} restates two facts of Sections~\ref{sec:start}
   and~\ref{sec:end} for arbitrary $C^1$ curves; the first referee re-proved them. These repairs, the new proof of
   Lemma~\ref{lem:T1-run1}(d) and the strict inequality in Lemma~\ref{lem:T1-tang}(b) were not re-read by the referees;
   they were checked in a later audit."

**`rem:T2-status`.** "found the chain correct, no false statement and no gap", "none changes a constant": accurate.
Inaccurate: "Both recomputed all derived constants" — they recomputed the formulas with the N8 and interim constant
sets; the final numbers of Table `tab:T2-const` were computed by the authors' script only (now also by this audit).
"Every link of the chain was checked by two independent referees" needs the caveat that each section contains
post-report passages. Fix text, l.816–818: replace "Both recomputed all derived constants." by "Both recomputed the
derived constants from the formulas \eqref{eq:T2-const}, with the interim touch-down constants then available; the final
values of Table~\ref{tab:T2-const} were computed after the reports and re-computed independently in a later audit. In
every section some passages were written after the reports (they are listed in the Status remarks of the sections); these
were checked in that audit, not by the referees."

**`rem:E-status`.** Simulation paragraphs match the reports. Three defects:
1. "none changes a constant of a theorem": `cor:E-T` changed (v ≤ γ₁/14, a′ = γ₁/2) and `prop:E-trans`(iii) was false
   as first written for v ≥ 0.618 (RP7-1 F9).
2. "Neither found … a gap in a proof": RP7-1 F6 found an inequality used in the wrong direction in `thm:E-dep`(iii).
3. **Last sentence is false for the present paper**: "the start data are not yet proved in this paper" contradicts
   `thm:HT` and `thm:Main`.
   Fix, first paragraph: "…were checked, in the form of version 1 of the claims, by two independent referees. Neither found
   a false conclusion or a gap affecting a conclusion. Their corrections are incorporated; they changed no numerical
   constant of Theorem~\ref{thm:End}, Corollary~\ref{cor:End}, Lemma~\ref{lem:E-far} or Theorem~\ref{thm:E-dep}(i)--(v), but
   they did change Corollary~\ref{cor:E-T} ($v\le\gamma_1/14$, $a'=\gamma_1/2$), restrict Proposition~\ref{prop:E-trans}(iii),
   and repair one step of the proof of Theorem~\ref{thm:E-dep}(iii). The time-dependent form of Corollary~\ref{cor:E-T},
   Remarks~\ref{rem:E-D2}, \ref{rem:E-restart}(1),(3), \ref{rem:E-B}(4) and this remark were written afterwards, each on the
   suggestion of one referee, and were not re-read by the referees."
   Fix, last sentence: "It is used in Section~\ref{sec:main} for the start of Section~\ref{sec:touch};
   Theorem~\ref{thm:Main} uses only Lemma~\ref{lem:E-facts}, Theorem~\ref{thm:End}(a),(b),(d) with \eqref{eq:E-CA},
   \eqref{eq:E-star}, Remark~\ref{rem:E-B}(4) and Corollary~\ref{cor:End}."

**`rem:B-status`.** "the one exception is Remark B-relaxed" is too strong. Not seen by either referee in the typeset
form: Step 3 as rewritten with the new constants, the merged Step 4 insert, 42.12, the Step 5 arithmetic, `rem:B-B`(4),
the restructured `cor:M`. One referee's own text, never seen by the other: `lem:B-C`(0), the scope of `thm:Bulk`, the
(IC1) range. Also omitted: each referee found one gap (R1: Step 4 Term II; R2: last leg of `thm:Bulk`). R2's leg-5
value at ε = 5·10⁻³ is 0.020, not 0.019.
   Fix: "…were checked by two independent referees in an earlier version; neither found a false proved statement, each
   found one gap (Step 4, Term II, case $b<a_{j+1}$; the last leg of Theorem~\ref{thm:Bulk}), and all corrections are
   incorporated. The corrected passages (Lemma~\ref{lem:B-C}(0), the scope of Theorem~\ref{thm:Bulk}, the rewritten Step 3
   and its constants, the added case in Step 4, the arithmetic of Steps 2 and 5, Remark~\ref{rem:B-B}(4), the wording of
   Corollary~\ref{cor:M}) were written after the reports and re-checked only in a later audit;
   Remark~\ref{rem:B-relaxed} was added afterwards and is covered by no report."

**`rem:ST-status`.** Accurate about the reports and the numerical paragraphs. Overstates in one respect: the proof of
`lem:ST-front`(g), the "Virtual front" paragraph of `lem:ST-D1`, the last sentence of `lem:ST-D2`, the preliminary of
`lem:ST-D3`, the per-leg (T) in `cor:ST` and `rem:ST-more`(3) were seen by neither referee in this form.
   Fix, insert after "…are incorporated.": "A few passages were changed in typesetting and were seen by neither referee
   in this form (the proof of Lemma~\ref{lem:ST-front}(g), the paragraph `Virtual front' in the proof of
   Lemma~\ref{lem:ST-D1}, the last sentence of Lemma~\ref{lem:ST-D2}, the preliminary of the proof of
   Lemma~\ref{lem:ST-D3}, the wording of (T) in Corollary~\ref{cor:ST}, Remark~\ref{rem:ST-more}(3)); they were checked in a
   separate audit."

## 4. Not verified

* sec_T1 and sec_T2: passages that are identical (up to notation) to the refereed claims v2 / v1 were compared, not
  re-derived — in particular the proofs of `lem:T1-coord`–`lem:T1-second`, `lem:T1-tang`(c), `lem:T1-fwd`,
  `lem:T1-tail`(c),(d), `lem:T1-virt`, `lem:T1-edges`, `lem:T1-hole`, `thm:T2-D` and `lem:T2-H` Steps 1–2. Their
  constants agree token by token with the claims.
* sec_E: Step 2, Step 5 and `thm:E-dep`(ii),(v) beyond their constants; the proofs of the sec_B lemmas; the referees'
  code. The simulation of `lem:E-far` with varying ρ₀ (145 admissible runs, no violation) is evidence, not proof.
* sec_B: the reports were written against P6a v2, which is not in the repository; comparison was against v3 and v4.
  The kink heuristic in `rem:B-relaxed` (E_kink ≈ Θ²ε) is a heuristic and was checked only for consistency.
* sec_ST: `lem:ST-D3` was checked on paper only, not simulated; the referees' simulations were not re-run.
* No end-to-end simulation was run in this audit; none can reach v ≤ 4·10⁻⁵¹ in any case.

## 5. Scripts (all in `code/audit/`)

`numdiff.py` (numeric-token diff tex vs claims), `worddiff.py` (word diff of claims versions),
`secT2_constants.py` (independent constants and side conditions of sec_T2, prints "RESULT ALL OK"),
`secE_constants.py`, `secE_trans.py`, `secE_far.py`, `secB_constants.py`, `secB_random_tests.py`,
`secST_check.py` (+ `secST_check.out`).
