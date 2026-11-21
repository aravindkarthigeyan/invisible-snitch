# Audit of the revision `human_backup_preRev/` → `human/` (audit-human-rev)

Scope: every `.tex` file and changed figure script/PDF diffed (word level) against the backup; every renamed symbol
grepped (old and new) across `main1–7.tex`, `appA–C.tex`; new mathematics refereed line by line; both referee reports
(`referee-human-1.md`, `referee-human-2.md`) checked item by item; Fig. 2 and Fig. 5 numbers re-measured with the
project's own `figs/snitchsim.py`; one independent build.

Unchanged files: `preamble.tex`, `snitch_human.tex`, `_wrapC_Hdepart.tex`, `fig_hook/limit/problem.py`,
`snitchsim.py`, and the PDFs of Figs. 1, 2, 3, 5, 8. Changed: `main1–7`, `appA–C`, `fig_designT.py` (docstring only),
`fig_timeline.py` (docstring only), `fig_touchdown.py` + `fig_touchdown.pdf` (labels only).

## Verdict

**Revision faithful and correct.** Every referee fix is applied, and applied correctly. Every rename is complete, with
no old symbol left over. The moves and cuts leave no dangling references, and the Lock order m → λ0 → R → v0 → ε*
is intact. The new mathematics (Lemma A.7, the B.5(a) ranges, the new (T0) proof, the new k1 argument in B.4(b)) is
correct. The build is clean, and the shipped PDF matches the sources exactly.

Five small blemishes remain. None of them affects correctness. Exact fixes are in §7.

## 1. Build

`pdflatex -interaction=nonstopmode -jobname=audit_build -output-directory=<scratchpad>/build snitch_human.tex`, run
three times from `human/`:

- 0 errors;
- no undefined or multiply defined references;
- no overfull boxes;
- **42 pages**.

The only warnings are 6 hyperref "Token not allowed in a PDF string". The pre-revision log has the same 6.

`pdftotext` of my build and of `human/snitch_human.pdf` are **identical**, so the shipped PDF is current.

## 2. Referee fixes: checklist

| Item | Applied? | Check |
|---|---|---|
| R1 F1 / R2 B1 (T0) | ✓ | Thm 5.1 now reads "…; for u∈𝒢 the direction Θ(u) is seen by t_td or u is true;" (R1's exact text). The proof is rewritten (§4.3 below). b_e is now "boundary direction of the sliver seen", and the cut-off set is (b_e, α0). |
| R1 F2 | ✓ | B.8(c): corr = (1+v)/((1−v)τ²−(1+v)) ≤ 1. I re-derived it by eliminating 𝒞/\|h\| from Lemma B.2(c): it is exact. |
| R1 F3 | ✓ | ω0 uses C_rot·v0. main6 says O(v0). The non-circularity remark in C.1 is valid (§4.5). |
| R1 F4 | ✓ | Setting (H) says "with cut b_c = U". main6 says Stage A is the chase on x⁰\|[0,U_A]. App. C Steps 1–2 say the (T2) estimate uses the full-front U. |
| R1 F5 | ✓ | B.4(b): y ≥ sin α, so ρ² ≥ 1. |
| R1 F6 | ✓ | B.5(a) "Ranges" (refereed in §4.2). |
| R1 F7 / R2 B2 | ✓ | K_*λ_*^{7/8} ≤ π. v_T ≤ 1/23 gives μ_T ≤ 1/8, and λ_* ≤ η/8 < 1, so K_*λ^{1−μ_T} ≤ K_*λ_*^{7/8} ≤ π. (T1) case 3 now cites this. |
| R1 F8 / R2 C1 | ✓ | C.1: "λ0 ≤ λ_* and C_tdλ0^{γ*} ≤ 1". ε_T and c_sep are "fixed once λ0 is fixed". "Shrinking λ0" is gone. |
| R1 F9 | ✓ | Lock item (4): C_tdε*^{1/2} ≤ R; ε* depends "on λ0 and R only"; z0 ≥ 2ε holds uniformly in v ≤ 1/23. Item (3) lists the caps 1/53, 1/300, R/10, mR/C1, 3/(16C*), R/(2·10⁴). |
| R1 minor: C1 clash / R2 C2 | ✓ | App. C constant renamed C_TW everywhere (5 occurrences). C1 of (A.farfinal) is kept, and the Lock's "mR/C_1" correctly refers to it. |
| R1 minor: A.2(a2) j=0 | not applied | The reason is **valid**: Setting (H) assumes only U ≤ 8, and Stage A has U = U_A ≤ ½, so "U ≥ 1" is not available in general. |
| R1 note: Thm 4.2(e) | kept | Harmless. Accepted. |
| R2 B3 | ✓ | "+η³ξ" dropped, with the sign remark. Range 2 is still correct: −½ξ + vε ≤ 0 since C0 ≥ 2. |
| R2 B4 | ✓ | The new Conventions paragraph is accurate, and the single exception (2ε_T < c_sep(λ0)) is the right one. |
| R2 C3 | ✓ | (D3) now says "in particular D+ε ≤ 1, as z0 ≥ 2ε". Check: (D3) gives U_E+z0+D ≤ (8C_D)^{−4/3} ≤ 1/16. (C.hint) cites (D3). |
| R2 M1 | ✓ | "relative bendiness … decays only like δ^{v/(1+v)} … far more slowly than δ^γ". This matches R2's analysis. |
| R2 M2 | ✓ | "v ≈ 0.05" removed. |
| R2 M3 | ✓ | "(for v ≤ v0 the proof gives 15)". |
| R2 M4 | ✓ | Closedness of I: \|S̃′\| = v gives a continuous extension to sup I. Correct. |
| R2 Fig. 1, 2, 3, 5, 6, 8 | ✓ | See §5. |
| R2 readability 1–10, §3.2, §3.3, §3.5 | ✓ | As listed in CHANGES §2. The two partial ones (items 2 and 4) are justified in CHANGES §3. |

**CHANGES §3 ("not applied") assessed.**
- R2's exponent 1/2 versus 7/8: both are valid. 7/8 needs μ_T ≤ 1/8, which is now enforced in the B Conventions.
- Fig. 2 at "66°": my recomputation agrees with the reviser, not with R2 (§5).
- The Fig. 2 snapshot and the uncut label set: optional, and covered by a caption caveat.
- Thm 4.2 not restated: keeping the formal statement unchanged is reasonable.
- λ0 not fixed inside Thm 5.1: consistent with R1 F8.

All of these reasons are acceptable.

## 3. Renames: grep results (old symbol left over / collision)

| Old → new | Old left over? | New collides? |
|---|---|---|
| C (conserved) → 𝒞 (main5, appB) | none (every `C(`, `∂C`, `log C`, `C/g_max`, `Cτ` checked; the remaining C are generic constants) | no. **Source blemish:** `\mathcal \mathcal C` at appB l.50 and l.382 (renders correctly) |
| C1 (App C) → C_TW | none | no |
| β(τ), β⁺ → ā, ā⁺ (appA) | none | mild: main1 Notation uses \bar a for the complex conjugate (a·b := Re(āb)). In App A, a is a real label, so there is no real ambiguity. Optional. |
| α, β, β_f, α*_D, C_β → 𝒜, ℬ, 𝒜*, C_ℬ | none (`\alpha`, `\beta` in main3/4/6, appA, appC are only angles) | no (\mathcal A/\mathcal B appear nowhere else) |
| A.6 ξ, θ → ζ, ϑ | none (`\xi`, `\theta` are absent from appA; \bar\theta = 5/8 is a separate, older constant) | no |
| ϑ(ρ) → 𝗊(ρ) | none | no |
| ω (1−2m²)^{−1/2} → c_m; ω̃ → 𝓛 | none (`\omega` absent from appA) | no |
| ω(t) moved to App B | the main text has no ω(t); App B defines it before first use (Design T frames paragraph) | no |
| η (regularisation) → ι | none (`\eta` now occurs only in appB, as the window half-width) | no |
| η1 → c_off; η_N → ν_D | none | no |
| m(θ) → 𝔪(θ); E → K_E; 𝒯 → 𝒦 | none (𝒯 in appA is the Toolkit leg-time set, as intended) | no |
| D(s) → ρ̂_s; w_s → Δ_s | none (D( in main3 is the chord difference, and in main6/appC it is the departure duration) | Δ in App B ((T2), Lemma B.10) is a different, appendix-local quantity. Acceptable. |
| a′ (=7/8) → γ_* | none in appC (a′ in appA is a label, as intended) | no |
| ν′ → ϖ; q_c removed | none (q_c was never used) | no |

## 4. New mathematics, refereed

**4.1 Lemma A.7 (layer cake): correct.**
- For ψ ≥ 0 non-increasing on [0,1], each set {ψ > u} is ∅, [0,σ_u) or [0,σ_u].
- Its ϖ-measure is at most ϖ([0,σ_u]) ≤ Φ(σ_u), which is the measure of the same set under μ = Φ(0)δ₀ + Φ′dσ.
- Integrating over u gives ∫ψ dϖ ≤ ∫ψ dμ.
- The uses in Terms I, II_a and II_b (kernels non-increasing in σ, and Φ as stated) are unchanged.

**4.2 Lemma B.5(a), proof of the ranges: correct.**
- For θ ∈ (0,π), β stays in (0,π), and h1 < 0 gives cos β1 < −v. So β1 ∈ (π/2,π), and 𝔟 = β1 − β* < π − β*.
- By the identity, ∂θβ1 has the sign of (cos α0 − cos θ), that is, of θ − α0. With 𝔟(α0) = 0 this gives 𝔟 ≥ 0.
- The mirror labels give 2π − β1 − β* ∈ (π−β*, 2π−2β*].
- The displayed bracket was verified by expanding: h1(cosθ−v) + sin²θ = (1+2v−v³) − (2+v−v²)cosθ = (1+v)[(1+v−v²) − (2−v)cosθ] = (1−v²)t1(cos α0 − cos θ), using (1−v²)t1 = (1+v)(2−v) and cos α0 = (1+v−v²)/(2−v).

**4.3 New (T0) proof: correct.** It covers four cases:
- u ∉ 𝒢 ⇒ true (B.4(e)).
- Θ = 2π: caught on Run 1.
- Θ = α0: ρ(t_a) = ε.
- Θ in the open window: either seen, or ρ > ε on [0,t_td], in which case virtual = true and u is true.

Every direction other than (b_e, α0) equals some Θ(u), and (b_e, α0) is seen by B.8(b). This proves both clauses of
(T0) as now worded. The parenthetical "need not be seen" is consistent with R1's and R2's counterexample.

**4.4 New k1 argument in B.4(b) (it replaces the k_t formula and the Grönwall step): correct.**
- 𝔖(0) = 0 for every α ∈ (0,π), since 𝔞∂log𝒞 = −(cos α − v) cancels the bracket at φ = −π/2, ψ = α + π/2.
- (log τ)′ = β′/sin β = 1/ρ ≤ 3, so (τ1/τα)^v ∈ [1, e^{9v}].
- \|𝔖1\| = O(v), from ρ1 ∈ [1/3, 7] and w1 ≥ 1.
- α = π follows by continuity.

**Slip:** "\|𝔞∂_α log𝒞\| ≤ 1" is false for α close to π, where it equals \|cos α − v\| → 1+v. The bound 1+v gives the
same O(v) conclusion. The cut k_t formula is referenced nowhere else (grep: only B.4(b) cites Lemma B.3(a), and only for
w_t and ψ_t).

**4.5 ω0 / v0 non-circularity (C.1): correct.**
- ω0 enters the departure proof only through h_H ≤ ¼, through polynomials, and through ω0²log⁺(C_H/ω0)/γ (bounded on (0,¼]).
- C_H uses ω0 only through ω0 ≤ ¼ (Step 4, case Λ > δ0).
- The dependence of v0 on ω0 is therefore effectively absolute.

**4.6 Other new text checked:**
- B.3(c) displayed identity with J time-independent: matches the proof.
- §6 exponent paragraph: γ+ν+ν_D ≤ γ_D ⇔ ν_D ≤ 1/24, and 2𝒜*(4)/53 = 0.0412 ✓.
- C_T formula in Thm 4.2(c): 6.104 and 5.572 ✓.
- Family-exclusion sentence (a non-final leg has l(a_j,a_{j+1}) = ε, so interior first points are within ε) ✓.
- ξ1 sentence before Thm 5.1 matches B.6(d) ✓.

## 5. Moves and cuts

**Parameter Lock.**
- §1 keeps only "Locked numbers", with roles. Each gloss is consistent with its use (c_off·R = offset threshold, d_L, κ, δ1, …).
- The four-item Lock now sits in §6, after W_e, δ0, U_A and U_E are defined.
- Its references are to earlier results (Thm 4.2(c), Thm 5.1, Lemma A.4) or are names only (Lemma 6.1 "below", (R1)–(R5) in App. C.1).

**Order.**
- m (locked) → λ0 (λ_*, C_td absolute) → c_sep(λ0), ε_T(λ0) → R (R1–R5; uses λ0, c_sep, G_T, C_td) → v0 (m, R, C_H(R), ω0, the caps) → ε* (λ0, R).
- No step uses a later choice.
- The label `par:lock` moved without breaking anything (0 undefined references).

**Cuts.**
- No remaining references to "Shrinking λ0", `rem:B-statement`, k_t, q_c or "Why straight runs help".
- After the duplicate §2 opening was cut, "front", "seen" and "candidate" are still defined in §1 (main1 l.19–31, 64).
- The deleted prose before Table 1 is replaced by a pointer to the table.
- App. A.1 and App. C.1 point to the "Where ε enters" paragraph, which is indeed the last paragraph of §4 (main4 l.134).
- The deleted parameter lists in A.1 and C.1 are replaced by "locked numbers of Section 1".
- Definitions moved before Thm 5.1 (ξ1, b_e, ξ_e, g_max) are consistent with B.6(d) and B.8(a).

## 6. Figures

**Fig. 2.** I recomputed with `snitchsim.simulate(v=0.1, eps=0.02, walk=False)`:
- P(t_td) = 0.3285 + 1.1014i, \|P\| = 1.149, polar angle **73.39°**;
- α0 = **54.99°**;
- n̂ = 148.3°;
- t_td = 4.207.

The caption ("about 0.33+1.10i, at polar angle about 73°; α0 ≈ 55°") is right, and so is the CHANGES §3 note. R2's
"66°" does not reproduce. The "close variant" caveat is accurate (it matches the docstring).

**Fig. 5.** I reran a scratch copy of `fig_timeline.py` (ε = 0.01). The relative change at the end of the near phase is
1.72 % (λ = 0.02) and 0.36 % (λ = 0.1), so "at most two percent" is correct. The ε = 0.01 versus 0.02 note and the
"arclength ≈ 1.1λ" note are correct (docstring updated).

**Fig. 6.** It was regenerated. The PDF text shows "tail end x0(U)" and "z0 ≍ ε^{1/(2−2v)}", which matches the caption
and the script diff (labels only).

**Fig. 3.** Caption versus `fig_hook.py`:
- (a) is a ray at angle 2 arcsin v to the backward direction, ending at Harry ✓;
- (b) is the parabola y = s²/2, with z0 = 0.03 ✓.

**Figs. 1 and 8.** The caption clauses agree with R2's observations.

**Fig. 9.** The braces K1 = (a_{i+1},a_j) and K2 = (a_{i+1},b) match the C.3 Step 3 definitions.

## 7. Remaining blemishes (none affects correctness): exact fixes

1. **main5.tex l.55–56.** The parenthetical describes 𝒞/g_max but is attached to g_max. Replace "where
   $\gmax:=\max\frg$ (the minimum of $\rho=\mathcal C/\frg(\beta)$ on a run)" with "where $\gmax:=\max\frg$ (so
   $\mathcal C/\gmax$ is the minimum of $\rho=\mathcal C/\frg(\beta)$ on a run)".
2. **appB.tex l.161 (Lemma B.4(b)).** Replace "$|\fra\,\partial_\alpha\log\mathcal C|\le1$" with
   "$|\fra\,\partial_\alpha\log\mathcal C|=|\cos\alpha-v|\le1+v$".
3. **appB.tex l.50 and l.382.** Replace `\mathcal \mathcal C` with `\mathcal C` (rename artefact; the output is unaffected).
4. **main6.tex, Lock item (2) (optional).** "depending only on $m$ and on the constants of Theorem 5.1" → "depending only
   on $m$, $\lambda_0$ and the constants of Theorem 5.1". (R1) and (R2) use λ0 and c_sep(λ0) explicitly.
5. **appA.tex (optional).** \bar a (base) shares its glyph with the complex conjugate of main1's Notation. Harmless,
   since labels are real. If wanted, rename to $a_\flat$ or $\underline a$.
