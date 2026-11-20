# Referee report SB — short paper `short/snitch.tex`: §1 statements, §§5–8, Appendix A, `verify_constants.py`

Second referee. Scope: §1 (statements), §5 (heading, departure), §6 (straight runs, design T), §7 (touch-down front), §8
(assembly, Theorem 1.1, Corollary 1.2), Appendix A and the script. I read the text standalone first and checked every proof
line by line. After that I compared §7 against `paper/sec_HTp.tex` and `paper/sec_T1.tex`, and §5/§8 against `paper/sec_T3.tex`
and `paper/sec_Estar.tex`, using the notes `short/notes_W3.md`–`notes_W5.md`. I did not read `reports/referee-SA.md`.

## Overall verdict

**Correct, with local fixes.** I found no statement that is false and no gap that affects any theorem.

- Two displayed inequalities in §7 are false as written, but their conclusions are true:
  - the length chain in Lemma 7.10;
  - the |z| sandwich in Lemma 7.8(b).
- One bound in Prop. 6.1 is proved only for v² ≤ ½, but stated for every v.
- The classification of constants in Lemma 7.2 (monotonicity) is incomplete.
- Exact replacement text for all four is given below.

**The script:**
- It is self-contained: Python 3 and mpmath only, no imports from `code/`.
- I ran a copy of it in a scratch directory. It printed `ALL 207 CONDITIONS HOLD` and exited with status 0.
- Its outputs `appA_tables.tex` and `verify_constants.out` are byte-identical to the files in `short/`.
- Its inputs equal the printed numbers: Theorem 7.12's constants, a′ = 0.99982, Table A.1 and Table A.3.

**The transcription:** I compared it statement by statement. Def. 7.1 and (SC1)–(SC51) are identical to the record after
renaming. Every heading constant, departure constant and eq. (8.1) entry also matches the record. No exponent changed, and no
symbol is used with its old meaning. The deviations I found are listed under "Comparison with the record".

## Verdicts per statement

### §1
| statement | verdict |
|---|---|
| Thm 1.1 | OK. Matches Prop. 8.2 and the scaling proof. The path depends only on (v, ε, d), and |H′| ≤ 1. Every direction is seen by T₀♯d ≤ 10.13d, where T₀♯ = 10.12637. |
| Cor 1.2 | OK. The hypotheses of Lemma 2.11 are checked in §8 (nested dyadic directions, ε_N = 2^{-N}ε\* → 0, common T = 10.13). |
| Rem 1.3 | OK. The sentence about v ≈ 10⁻⁴ and "simulations" is unsupported but harmless. |
| Outline, line 74 | **Fix.** "its last point lies a distance at most of order ε^{1/2} **ahead of** the pursuer" is wrong. By (T5), x⁰(U) = P(t_td) − z₀n̂ − y₀n̂^⊥ with z₀ > 0, so it lies **behind** P (§5 says "just behind P"). Replace "ahead of the pursuer at $\ttd$" with "behind the pursuer at $\ttd$". |

### §5
| statement | verdict |
|---|---|
| Heading constants (5.1) | OK. They match the record's lem:T3-H specialised to γ₁ = γ_h = γ_D; ρ\* is an admissible fixed choice. |
| Lemma 5.1 (heading) | OK. I checked every step: λ_I ∈ [ε, δ₀] and I in the family; the k_σ bound; the close case (pairs K₁–K₄ in the family, ψ⋆); the far case via Thm 3.3(d) and ρ\* ≥ ε\*; durations; the rotation bound; the sum; and the time bound via (J2) and c_τ. Exposition: ρ′ denotes a distance in Step 3 but the derivative in "Time". |
| (D0)–(D3), constants (5.2) | OK. They match the record. The record's X\* ≥ U_E + z₀ + D̄ is replaced by z₀ ≤ z₀^max, which §8 Step 4 proves. |
| Thm 5.2 (departure) (i)–(v) | OK. I checked every exponent: ζX bounds; Grönwall for y (eq. 5.3); δ via δ_ϖ; K_w including the split at x_c; and both phases of (v), with Lemma 2.9 applied for K = 4 and the β-integral giving c_β. The §2 hypotheses are available: c > 0 by the chord bound (v), and ρ_m ≥ ζz₀ ≥ ε. |

### §6
| statement | verdict |
|---|---|
| Prop 6.1 | **OK with fix.** The statement (and "valid for every v ∈ (0,1)") claims ĝ_max ≤ e^{v²}, but the proof ends "≤ v² for v² ≤ ½". Replace `$\phi(v):=\log\gmax=\frac12[\dots]=\sum_{n\ge1}\frac{v^{2n}}{2n(2n-1)}\le\frac{v^2}{2(1-v^2)}\le v^2$ for $v^2\le\frac12$` with `$\log\gmax=\frac12[(1+v)\log(1+v)+(1-v)\log(1-v)]=\sum_{n\ge1}\frac{v^{2n}}{2n(2n-1)}\le v^2\sum_{n\ge1}\frac1{2n(2n-1)}=v^2\log2\le v^2$`. This also removes the clash of φ(v) with the angle φ. |
| Lemma 6.2 (true front) | OK. I verified the w, ψ and k evolution laws directly. |
| Lemma 6.3 | OK. |
| Lemma 6.4 (transport) (a)–(e) | OK. I re-derived k w³ = q × ∂_θq including the ∂_β L⁻¹ term, the 𝔖 formula, the two-time formula and both 𝔖 bounds. |
| Def 6.5, run-1/run-2 data, (6.2), (6.3) | **OK with fix (wording).** Eq. (6.2) is stated "for a label with 0 < 𝗯 < π", but the proof of Lemma 7.6 applies it to α₀, where 𝗯 = 0. The identity holds whenever ρ > 0 on run 2. Replace "a label with $0<\sbb<\pi$ has in run 2" with "every label whose true candidate has $\rho>0$ on run 2 (including $\alpha_0$, for $t<\tc$) has". |

### §7
| statement | verdict |
|---|---|
| Def 7.1, (SC1)–(SC51) | OK. Identical to def:HTp-const and its side conditions after the rename map. |
| Lemma 7.2 (monotonicity) | **OK with fix.** See (a)–(c) below the table. |
| Lemma 7.3 (run 1) (a)–(e) | OK. I checked α_s ≤ 2ĝ_b ε, the middle bounds by Grönwall, and the arm bounds: k_arm, d_arm, W_arm and y ≤ 2𝓔₁τ_α^{(1−v)/(1+v)}. |
| Lemma 7.4 (tangency) (a)–(d) | OK. I checked the ∂_θβ₁ identity, α₀ ∈ [α̲, π/3], the bound on t_c − t_td, and all window bounds: q̃ decreasing, the cot bounds, L_lo, 𝔖 ≤ S₁v. |
| Lemma 7.5 (forward arc) | OK. |
| Lemma 7.6 (virtual labels) | OK. This includes the Grönwall step on [t_a, t_td] and the case ξ = 0. |
| Lemma 7.7 (tail) | OK. Exposition: the y-step `$y=C\tau^v=C(\tau^{1+v})^{v/(1+v)}\le C_{\mathrm{hi}}^{1/(1+v)}\dots$` skips a step. Better: `$y=C^{1/(1+v)}(C\tau^{1+v})^{v/(1+v)}$, and $C\tau^{1+v}\le y_{\mathrm c}\xi$ by the bound on $\tau$, so $y\le C_{\mathrm{hi}}^{1/(1+v)}\xi^{(2-2v)/(1+v)}(y_{\mathrm c}\xi)^{v/(1+v)}\le\dots$`. |
| Lemma 7.8 (bulk, hole, chords) | **OK with fix in (b).** "so $(1-v)|z|\le|h_1|\le(1-v)|z|+vy$" is false whenever y > 0. Since z = h₁ − vρ₁ < 0, we have |h₁| = |z| − vρ₁ and |z| ≤ ρ₁ ≤ |z| + y. Replace it with "so $|h_1|\le(1-v)|z|\le|h_1|+vy$, hence $0\le|z|-(1+v)\le(1-\cos\alpha+vy)/(1-v)$". The conclusion and everything after it are unchanged. |
| Def 7.9, ghost set | OK. |
| Lemma 7.10 (length) | **OK with fix.** "$W_{\mathrm b}W_{\mathrm{all}}(2\pi/(1-2v)-2\eta)\le W_{\mathrm b}W_{\mathrm{all}}(2\pi-2\eta)/(1-2v)$" is false (2η/(1−2v) > 2η). The claim U ≤ U_max is still true. Replace the sentence "Now $\int_0^{2\pi}\dots$, and $U\le U_{\max}$." with: "The bulk labels form an arc of length $2\pi-2\eta>4$; by the arc bound proved below, its contribution is at most $W_{\mathrm b}W_{\mathrm{all}}(2\pi-2\eta)\bigl(4/(2\pi-2\eta)\bigr)^{2v}/(1-2v)\le W_{\mathrm b}W_{\mathrm{all}}(2\pi-2\eta)/(1-2v)$; with $W_{\mathrm v}\eta$ and $W_{\mathrm t}\eta$ for the forward and tail zones, $U\le U_{\max}$." The arc-bound sentence should then move up. |
| Lemma 7.11 (N bound) | OK. All three cases are exhaustive; I checked the forms 12u_v² + 6u_v + 1 and 3³ − 2³ = 19, and Kλ ≤ π. |
| Thm 7.12 (T0)–(T5) | OK. I checked the outward roundings with the script. (T5) only gives z₀ ≤ c_zhi ε^{1/2} where the record has ε^{1/(2−2v)}; this is weaker but sufficient. (T1) and (T3) state only the barred exponents; also sufficient. |

Fixes for Lemma 7.2 (monotonicity):
- (a) **The lower-constant list is incomplete.** θ_L = α̲ − η, R_L = R₀(θ_L) and q_min decrease in v, so they are lower constants. I confirmed this numerically by evaluating Def. 7.1 at six values of v ∈ [10⁻⁷, 6·10⁻⁵] and four values of ε. Every other constant is monotone as stated. Every use of these three constants is as a lower bound, so the proofs are unaffected. Add "$\theta_L$, $R_L$, $q_{\min}$," to the list of lower constants.
- (b) **Rule (2) wrongly covers Δ₀^{1−μ}.** Rule (2) assumes a base that does not decrease in v, but Δ₀ is a lower constant. κ_c and (SC45) are used only as numbers: in (T2), ξ < Δ₀ refers to the fixed Δ₀. Delete "$\Delta_0^{1-\mu}$," from rule (2) and add after the rules: "$\kc$ and \hyptag{SC45} enter the proofs only as fixed numbers, so no monotonicity is needed for $\Delta_0^{1-\mu}$."
- (c) **A hypothesis was dropped.** The record lemma assumes (SC1)–(SC51), and the proof uses (SC1), (SC8)–(SC12), (SC18), (SC21), (SC23) and (SC26). Add "Assume \hyptag{SC1}--\hyptag{SC51}." to the statement.

### §8
| statement | verdict |
|---|---|
| (8.1), (C0)–(C6), (A1)–(A6) | **OK with fix.** See (a)–(b) below the table. |
| Lemma 8.1 (start data) | OK. The (S2) chain and the concave case split are correct; it uses (C1)–(C6) but not (C0). |
| Prop 8.2 Steps 1–7 | OK. See the paragraph below the table. |
| Proof of Thm 1.1 | OK. |
| Proof of Cor 1.2 | OK. |
| Coverage (Table 8.1) | OK. |

Fixes for (8.1), (C0)–(C6) and (A1)–(A6):
- (a) **The script checks "v₀ ≤ v̄" as an (A6) item, but the text of (A6) does not list it.** It is needed for Thm 7.12 to apply. Add "$\vz\le\vbar$," at the start of (A6).
- (b) **A record condition was dropped silently.** The record's ε\* ≤ (R/(100c_zhi))² (`sec_T3.tex:536`) is dropped without comment. No short-paper proof uses it, so this is harmless.

Prop 8.2, as checked:
- Step 1: pairs with λ > λ₀ in [0, U_A] get c ≥ c_sep^A from (T2), because a + U − b ≥ 1 − U_A.
- Step 2: there is no circularity. P_A's end theorem is independent of P's, and P = P_A on [0, t_W] by Lemma 3.2(4).
- Step 4:
  - (D0): the bound on y₀ uses 1 − μ̄_T − γ_D ≥ 0.
  - (D1): uses (T4) with s + z₀ ≤ X\*.
  - (D2): uses h_H ≤ ω₀ ≤ ½.
  - The monotonicity of ε^{1/(2−2v)}/ε holds in both variables.
- Step 5: the (TW) ratio exponents are a′ − η_N − γ − ν ≥ 0 and γ_D − η_N − γ − ν ≥ 0.
- Step 6: κ_c W_e = c_A K_R R holds by definition.
- The §2 hypotheses (c > 0, regular start curves: x⁰ has unit speed, the departure arc too, the virtual candidates start on the circle) hold everywhere they are used.

## Numerical conditions versus the script

I listed every numerical inequality used in §§5–8 and grepped the script for each one.

**Used but not checked by the script.** All are trivially true, but strictly they are unverified:
- ζ ≤ 1 (Thm 5.2(i), z₀ + ζ(s+τ) ≥ ζX);
- m₀ ≤ 1 and e_ρ/√3 ≤ 1 (arcsin domains in Def. 7.1; they are 0.109 and 1.4·10⁻⁴);
- π/2 + η < 2 (Lemma 7.10);
- 2π − 2η > 4 (needed only with my fix of Lemma 7.10);
- s/(1 − s²/2) ≤ 2s for s ≤ 1 (ψ⋆ in Lemma 5.1).

Every listed side condition is checked.

**Checked by the script but not in the text as stated:**
- "(A6) v₀ ≤ v̄" is not in the (A6) text (see above).
- "(P0) 0 < v₀ < 1" is not in the (P0) text.
- "(A3) G_f ≤ U_A − ε\*" duplicates "U_A ≥ W_e + 2ε\* + δ₀".
- "(A4) 1 + γ_D ≤ 2 − μ̄_T" duplicates γ_D ≤ 1 − μ̄_T.
- "(A4) k_D ≥ 4(1+δ_t)/ζ" is not in (A4); it is automatic from c_k ≥ 1.
- a′ ≤ 1 − μ̄_T is checked twice, under "out" and under "extra".

No check has the wrong direction or a different constant. I verified every formula in `touchdown()`, `core()`, `corollary()` and `assembly()` against Def. 7.1, Def. 3.2, (5.1), (5.2) and (8.1). Examples: η_N uses α_D(4) = 1.375, and θ_h1 = 2^{γ_D+2}v₀κC₃m/(c_A(1−v₀)R^{γ_D}).

**Stated but never used in any proof:** (C0), (SC41) λ₀ ≤ ¼, (SC46) κ_c ≥ ½, (SC49), X\* ≤ 1, z₀^max ≤ 1. (A3) "U_A ≥ W_e + 2ε\* + δ₀" is used: it gives G_f ≤ U_A in Lemma 5.1.

The four reference-value warnings in `verify_constants.out` (B_{2U}, σ̄, Θ₀, δ_t) come from 4-digit record values and from the outward-rounded θ_v. They are expected.

## Comparison with the record (after the standalone reading)

- **§7 against sec_HTp/sec_T1:** no changed formula, exponent, sign, factor or inequality direction in Def. 7.1, (SC1)–(SC51) or any lemma. The deviations are:
  - The weakened (T1), (T3), (T5) (harmless).
  - The dropped (SC) hypothesis of Lemma 7.2 (fix above).
  - Eq. (6.2) restricted to 0 < 𝗯 < π but used at α₀ (fix above).
  - 𝗯 ∈ [0, π/2) instead of the record's [0, π) (stronger, proved).
  - A_max < 2 instead of < 1.6 (correct, since e^{0.3/sin ½} ≈ 1.87).
- **§5/§8 against sec_T3/sec_Estar:** every constant and condition matches or is a valid specialisation (θ_h1, ρ\*, L_h with ε\*, all departure constants at v₀). Dropped items: ε\* ≤ (R/(100c_zhi))² (unused) and v₀ ≤ v̄ from the side-condition list (see above).

## Exposition (brief)

1. §1, line 74: "ahead" should be "behind" (see above).
2. θ_v in Theorem 7.12, §5 and Table A.2 is written with an italic v, which reads as the speed; Def. 7.1 writes θ_{\mathrm v}. Use θ_{\mathrm v} throughout.
3. Other notation clashes:
   - Lemma 5.1 uses ρ′ for a distance (Step 3) and a derivative ("Time"); rename the distance, e.g. ϱ.
   - Prop 6.1 uses φ(v) (fixed above).
   - Thm 5.2(iii) uses d := T − û next to the distance d.
   - Step 5 of Prop 8.2 uses K, which clashes with the K of Lemma 2.9.
4. §5, opening paragraph: δ₀ is called both a number "of (8.1)" (where it is not defined) and a free parameter. Keep only "free parameter δ₀ = 0.149785R (Table A.3)".
5. Lemma 7.8(c): the case split θ = π / θ ≠ π is unmotivated. One sentence would help: Lemma 2.6(b) needs ≥ 2ε for each approximating α, and the limit gives the bound.
6. Thm 7.12 could state the sharper (T1), (T3) and (T5) with μ, μ_T and ε^{1/(2−2v)}. They are proved, and doing so costs nothing.

## How Appendix A could be shortened without loss

1. **Table A.2:** print only the about 25 constants that enter Theorem 7.12, the side conditions with slack below 10⁻² and the eq. (8.1) inputs. The other ~100 values are reproducible from Def. 7.1 and already sit in the log.
2. **Table A.4:** drop the trivial (P0) positivity and range rows (0 < R, m > 0, 0 < c_A, ν ≥ 0, …) and the trivially true (SC2), (SC5), (SC35), (SC50a), v̄² ≤ ½, η ≤ 1, 𝓔₁ ≥ 1 (true by definition). State in one sentence that they hold.
3. **Duplicates:** remove the duplicate checks (G_f ≤ U_A − ε\*, 1 + γ_D ≤ 2 − μ̄_T, a′ ≤ 1 − μ̄_T twice, k_D ≥ 4(1+δ_t)/ζ).
4. **Unused conditions:** remove (C0), (SC41), (SC46), (SC49), X\* ≤ 1 and z₀^max ≤ 1 from the paper and the script.
5. **Merge the (P) blocks:** merge the "(P0)–(P7) same for p and p_A" block with the per-tuple blocks into one two-column table (p | p_A). This saves about a third of a page.
6. **The margins paragraph** in appA.tex (smallest margins) repeats the slack column. It could be reduced to one sentence: "the smallest relative slacks are 0 (v₀ = v̄), 10⁻⁸ (a′) and < 10⁻⁵ for conditions defining rounded inputs".
7. **The `REFERENCE` dictionary** in the script compares against the record and only produces warnings. Removing it, and the corresponding log block, makes the script independent of the record.
