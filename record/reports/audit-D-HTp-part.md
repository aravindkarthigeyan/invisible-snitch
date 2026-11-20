# audit-D, part HTp: `paper/sec_HTp.tex` against `referee/Q3-claims-v1.md` and the referee fixes

Sources compared: `paper/sec_HTp.tex` (1000 lines, read in full); `referee/Q3-claims-v1.md` §0–§10; `referee/Q3-claims.md` v2
(changelog C1–C8, U1–U3); `reports/referee-RQ3-1.md`; `reports/referee-RQ3-2.md`; `reports/Q3-1.md` §3; `code/Q3/constants.py`;
`code/Q3/out/table.txt`; `code/Q4/final.py` (header and `q3_chain` only).

Audit code (new, in `code/audit/D/`):
* `HTp_constants.py` (output `HTp_constants.out`). Every constant of def:HTp-const and every side condition (SC1)–(SC51), transcribed
  from the TeX alone. It is compared with `constants.chain` on the 13 table rows and on the row used downstream, and it checks the
  excluded combinations and the outward rounding in cor:HTp-used.
* `HTp_lam0_scan.py` (output `HTp_lam0_scan.out`). Checks whether any λ₀ satisfies (SC39) and (SC42) together at (2·10⁻², 0.1).
* `HTp_thv_limit.py` (output `HTp_thv_limit.out`). Computes θ_v as v̄ → 0 for several η.

## Overall result

* **The mathematics agrees with v1 plus the referee fixes.** Every lemma, theorem and corollary statement matches v1 plus
  C1–C4 (hypotheses, constants, ranges and conclusions). The 51 side conditions and every formula of def:HTp-const reproduce
  `constants.py`: the largest relative difference over 15 output constants and 13 rows is 4·10⁻⁵¹, and all SC booleans agree.
  The only changes are symbol renames (x→ξ, xe_lo/xe_hi→ξ₋/ξ₊, rΛ→ℓ, δ(t)→ω(t), and so on), which are recorded in the file header.
* **No GAP or FALSE on the main path.**
* **One FALSE statement off the main path** (intro, line 39–40): θ_v → 1 as v̄ → 0.
* **One inaccurate Status claim:** that `code/Q4/final.py` evaluates the row used downstream "independently". It imports the same
  `chain()`.
* The rest are small wording fixes.

## Table

| # | section / location | delta (vs v1 + referee fixes) | main path? | verdict | exact fix text |
|---|---|---|---|---|---|
| 1 | sec_HTp, all statements (Lemmas HTp-M … HTp-T1, thm:HTp, cor:HTp-table) | Transcription and renames. C1 ((SC51) in the hypothesis, cited at (T4′) and (T5′)), C2 (cites (SC39), (SC40)), C3 (η ≤ π/6) and C4 (STA_max < 1.6) are applied. | yes | OK | none |
| 2 | def:HTp-const, (SC1)–(SC50) | Formulas rewritten in TeX notation. | yes | OK (recomputed: rel. diff ≤ 4·10⁻⁵¹ against `chain()` on all 13 rows; SC booleans identical; the SC order equals the order of the `cond` keys) | none |
| 3 | (SC51) and its uses (thm:HTp proof l.831 and l.840; lem:HTp-M; cor:HTp-table; cor:HTp-used) | New side condition z_T ξ̄_e + ε̄ < 1 and G_T + z_T ξ̄_e ≤ 1 (fix C1 of RQ3-1). | yes | OK | none. It is needed: (T4′) needs u′+z₀ ≤ 1 for the exponent change 1−μ_T → 1−μ̄_T, and (T5′) needs z₀+ε < 1; z₀ ≤ z_T x_e ≤ z_T ξ̄_e. It is monotone in v̄ and ε̄ in the safe direction, so lem:HTp-M stays valid. It holds in all 13 rows (max 0.06661 and 0.21149; printed bounds 0.0667 and 0.2115 are correct) and at (6·10⁻⁵, 0.1): 0.0505094 and 0.0995094. It only adds a hypothesis that is true in every row used, so it breaks nothing. |
| 4 | cor:HTp-table, Table tab:HTp (13 rows) | Theorem applied per row. Rows and values equal `code/Q3/out/table.txt` and `reports/Q3-1.md` §3 (unchanged from v1). | yes (row v̄=2·10⁻², η=0.2 gives "every v ≤ 2·10⁻²") | OK | none. All 51 SC hold in every row (independent transcription). |
| 5 | text after cor:HTp-table (l.912–913) and rem:HTp-status (l.993) | Excluded combinations: (10⁻², 0.3) fails (SC21); (2·10⁻², 0.1) fails (SC42); v̄=3·10⁻² fails (SC42), and also (SC21) for η ≥ 0.2. | no | OK | none. Recomputed: (10⁻²,0.3) C_hi = 1.0322, only (SC21) fails. At (2·10⁻²,0.1) W_xL̂ = 2.024. (SC42) is independent of x₁ and G_T, and no λ₀ satisfies (SC39) and (SC42) together (the largest λ₀ with (SC39) is 0.0333; λ₀ = 0.05 passes (SC42) but fails (SC39)). RQ3-1 §4 found the same. At 3·10⁻²: η=0.1, 0.15 fail (42); η=0.2, 0.25 fail (21, 42); η=0.3 fails (21, 42, 49). |
| 6 | rem:HTp-status l.993–994 | "at v̄ = 5·10⁻² also (SC47) and (SC49) fail" | no | OK with fix | Replace with: "at $\HTvb=5\cdot10^{-2}$ also \HTSC{36}, \HTSC{47} and \HTSC{49} fail" (recomputed at η = 0.15 and 0.2: (SC21), (SC36), (SC42), (SC47), (SC49) fail). |
| 7 | Intro l.39–40 | "\|ψ\| ≤ θ_v ξ^{1−μ} with θ_v → 1 as v̄ → 0 (the true constant is 1)" | no | **FALSE** as written | Recomputed: θ_v(v̄→0) = 1.06936 at η=0.1, 1.0315 at η=0.05, 1.0059 at η=0.01. So θ_v → 1 only as (v̄, η) → 0. Replace with: "with $\theta_{\mathrm v}\to1$ as $(\HTvb,\eta)\to0$ ($\theta_{\mathrm v}=1.070$ at $\HTvb=10^{-6}$, $\eta=0.1$; the true constant is $1$)". (This matches Q3-1 §4 "ψ ≈ ξ" and rem:HTp-compare, "the factor ℓ_max/2 ≈ 1.03".) |
| 8 | lem:HTp-tilt (new separate statement) | Q2(c)'s last item, plus the tilt identity of rem:T1-tilt(i) stated with N_ψ, D_ψ | yes | OK | none. Re-derived: Ξ = a(1+iY_r) and (1−v²)q = Ξ − v e^{iβ} Ξ̄ give exactly D_ψ + iN_ψ. The bounds in (a) are those of v1 Q2(c). |
| 9 | lem:HTp-twotime (new separate statement) | Collects steps from the proofs of v1 Q3(d), Q5(c) and Q6(b) | yes | OK | none. Re-derived: (a) from eq:T1-k2 with w′/w″ ≤ 1 (w is non-decreasing, [B]); (b) from eq:T1-k with \|v+cos(φ−ψ)\| ≤ 1+v; (c) gives v(3+v)/(2(1−v)y), the same as v1 S_b; (d) \|Ξ″\| ≤ (τ″/τ′)^v\|Ξ′\|. Optional: add "($w$ is non-decreasing in time, Lemma~\ref{lem:B-1})" after "$w'/w''\le1$" in the proof of (a). |
| 10 | lem:HTp-M, last-but-one sentence (l.233–234) | New sentence (not in v1): "In ε, only ξ̄_e, C_z, h_a, τ_a and the conditions (SC1), (SC22), (SC37), (SC40), (SC44), (SC51) depend on ε̄" | yes (rule M) | OK with fix | The list is incomplete: ϑ₄ and ϑ_T (through ξ̄_e), and (SC24), (SC29)–(SC31), (SC39), (SC50), also depend on ε̄. All are monotone in the safe direction, so the conclusion stands. Replace with: "In $\varepsilon$, the constants depending on $\HTeb$ are $\HTxb$, $\vartheta_4$, $\vartheta_{\mathrm T}$, $C_z$, $h_{\mathrm a}$, $Q_{\mathrm a}$, $\tau_{\mathrm a}$, and the side conditions depending on $\HTeb$ are \HTSC1, \HTSC{22}, \HTSC{24}, \HTSC{29}--\HTSC{31}, \HTSC{37}, \HTSC{39}, \HTSC{40}, \HTSC{44}, \HTSC{50}, \HTSC{51}; all monotonically." |
| 11 | cor:HTp-used (row 6·10⁻⁵, 0.1) | New row, not in v1. Its constants are taken from v2 §9 "Column used downstream" (not refereed). | yes (feeds sec_T3) | OK | none. Recomputed in 50 digits from the TeX transcription: ALL 51 SC hold. Printed values are rounded outward: T₂ 3.73247 ≥ 3.7324640; U_max 6.29320 ≥ 6.2931948; c_sep 0.0330591 ≤ 0.03305915; κ₂ 0.988089 ≤ 0.98808912 (= h_t/W_t); c_N 2.72160 ≥ 2.7215935; ϑ_T 1.15397 ≥ 1.1539694; C_z 0.278412 ≥ 0.27841163; μ̄_T 1.79990e-4 ≥ 1.7998920e-4; μ̄ 6.00037e-5 ≥ 6.0003600e-5; θ_v 1.07003; c_T4 1.04263; h_tξ₋ 1.27025 ≤ 1.2702545; z_Tξ₊ 1.56563; c_y 0.619797. The (T1) data also check: a′ = 0.99982 ≤ 1−μ̄_T = 0.9998200108. Taking C₀ = 2.72160 ≥ c_Nλ₀^{1−μ̄_T−a′} = 2.7215934 is admissible, and 2.72160·0.0333^{0.99982} = 0.0906848 ≤ 0.0907. |
| 12 | cor:HTp-used proof l.939 | "(SC51) holds with z_Tξ̄_e+ε̄ = 0.050510 and G_T+z_Tξ̄_e = 0.099510" | no | OK with fix | The exact values are 0.0505094 and 0.0995094. Replace "$=0.050510$" with "$\le0.050510$" and "$=0.099510$" with "$\le0.099510$". |
| 13 | text l.909 | "With ε̄=10⁻⁶ the end x_e ≲ 1.9 ε^{1/2}" (v1 / Q3-1 had 1.7) | no | OK with fix | ξ₊ = 1.924 in the ε̄=10⁻⁶ row (10⁻³, 0.3). Replace with "$\TDxe\le1.93\,\varepsilon^{1/2}$". |
| 14 | rem:HTp-status, "Refereed" (l.965–967) | "Lemmas HTp-M–HTp-T1, Theorem HTp and Corollary HTp-table (as a statement about the rows of the table) were checked by two independent referees on version 1" | — | OK with fix | RQ3-1 was told not to read the table. It recomputed its own columns with its own x₁ and G (RQ3-1 §0: "I did not see the authors' table"; §4), so only RQ3-2 checked the 13 printed rows. Neither referee checked (SC51) on the printed rows: RQ3-2 checked (SC1)–(SC50); RQ3-1 checked i1, i2 on its own columns. The range HTp-M–HTp-T1 also includes HTp-tilt and HTp-twotime, which are listed as not refereed further down. Replace with: "Lemmas~\ref{lem:HTp-M}--\ref{lem:HTp-T1} (except as noted below) and Theorem~\ref{thm:HTp} were checked by two independent referees on version~1 of the claims file … Corollary~\ref{cor:HTp-table} was checked row by row for \HTSC1--\HTSC{50} by RQ3-2; RQ3-1 confirmed with its own parameter choices that the same $(\HTvb,\eta)$ admit all side conditions including \HTSC{51}; \HTSC{51} on the printed rows is checked by the author's code and by audit-D." |
| 15 | rem:HTp-status, RQ3-2 bullet (l.984–985) | "all side conditions hold" (on the 18 rows) | — | OK with fix | Replace with "\HTSC1--\HTSC{50} hold" (RQ3-2 §3 refereed v1, which had no (SC51)). |
| 16 | rem:HTp-status, "Not refereed" (l.989–990) | "the row 6·10⁻⁵ … (evaluated by the same code, and independently in code/Q4/final.py)" | — | **inaccurate** | `code/Q4/final.py` does `import constants as q3c` and calls `q3c.chain`; it only adds the (SC51) test. It is not independent. Replace with: "(evaluated by \texttt{code/Q3/constants.py}, which \texttt{code/Q4/final.py} calls unchanged, and independently, from the typeset formulas, by \texttt{code/audit/D/HTp\_constants.py})". |
| 17 | rem:HTp-status l.997 | "true bulk curvature ≈ 1.02 (RQ3-1, by ODE)" | no | OK with fix | RQ3-1 §1(2) says "≤ 1.015". Replace "$\approx1.02$" with "$\le1.015$". |
| 18 | file header l.5 (comment) | "Doubly refereed." | no (not typeset) | OK with fix | Replace with "Statements doubly refereed (v1); the row 6e-5 and lem:HTp-tilt/-twotime as statements are not; see rem:HTp-status." |
| 19 | rem:HTp-status RQ3-1 bullet (l.971–977) | Numbers: 54 values, 40 digits, v-set, 10⁻⁴¹, 10⁻⁴⁰, chords, row 10⁻⁶ | — | OK | none. Each number is in RQ3-1 (§§1–2, §5, file table). |
| 20 | rem:HTp-status RQ3-2 bullet (l.978–984) | 178 digits, 99 configurations, 7 sets, v ∈ {v̄, v̄/10, v̄/1000}, ε ≥ 10⁻⁶⁰, 27 000 pairs, margins 1.4 %, 4–5 %, 19 %, ≥ 25 %, 18 rows, 7·10⁻⁴ | — | OK | none. Each number is in RQ3-2 §§0–3. |
| 21 | rem:HTp-compare | Comparison with thm:HT. κ₂ = 0.9883 is printed, while the table has 0.9884 (exact 0.988407). | no | OK | Optional: print "$\kappa_2=0.9884$" for consistency with Table~\ref{tab:HTp}. 0.9883 is a valid, more conservative lower bound. |

## Notes

* **Main path (thm:HTp → cor:HTp-used → sec_T3).** Every hypothesis and conclusion matches v1 + C1–C4, and every constant was
  recomputed. Nothing on this path needs a mathematical change.
* **No change outside C1–C4.** I compared the statements of Lemmas Q1–Q7 and Theorem Q.H in v1 line by line with
  lem:HTp-run1 … lem:HTp-T1 and thm:HTp. No hypothesis was weakened, and no constant or range was changed except η ≤ π/6 (C3).
  The added items are all proved in place: "ρ₀ > ε" in lem:HTp-tang(b), "τ_b ≥ b/2" in (c), and "τ″ ≥ τ_b" in lem:HTp-twotime(a).
* **Downstream rounding (outside this section).** sec_T3 (tab:T3-const, l.651) prints μ̄_T = 1.79989·10⁻⁴. The exact value is
  1.7998920·10⁻⁴, so 1.79989 is rounded down, while μ̄_T is used as an upper constant. This concerns sec_T3, not sec_HTp; it is
  passed to the sec_T3 audit.
