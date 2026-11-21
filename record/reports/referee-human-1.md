# Referee report: `human/snitch_human.pdf` read as a stand-alone paper (referee-human-1)

Reviewed: `human/snitch_human.tex`, `preamble.tex`, `main1.tex`–`main7.tex`, `appA.tex`, `appB.tex`, `appC.tex` (42 pp.).
Method: I read every statement and proof myself, line by line, and redid the computations by hand. Only after that did I
compare with `short/sec3–sec5, sec8` and with `reports/referee-streamlined.md`, to locate omitted steps.
Numerical check: scratchpad script `chk.py`. It recomputes c6, c_ρ*, c_R*, χ_g, α_D*(2), α_D*(4), C_T, C_μ, C_p, C_β, C1, C2,
C_*, C4, the "16" and "12.57" bounds, the length inequality at C3 = 2·10⁴, ω0's first term, μ/μ_T/e^{2μ} at v = 1/23,
η_N at v = 1/53, the T_stop arithmetic, ρ_* = R/5, and the close-case duration factor.

## Verdict

**The paper is a complete and correct stand-alone proof of Theorem 1.1 and Corollary 1.2, subject to the textual fixes
listed below. None of them needs a new idea.**

- No step is false where it is used.
- Two statements are false as literally worded:
  - (T0)'s clause "whose directions are seen by t_td" (F1);
  - the inequality for the correction term in Lemma B.7(c) (F2).
  In both cases the proofs establish what is actually used.
- Several statements need a one-line addition (F3–F9).
- The earlier referee findings are resolved:
  - **E1** is resolved: δ1 = 5/4 gives c_ρ*K_f = 5/2 ≥ 2, and the far-pair step at g = 5ε is now correct.
  - **E2** is resolved: h_H = min(C_H(t+ε)^{γ_D}, ω0).
  - **E3** is resolved: ω0 ≤ 1/4 via m = 1/10; the first term is 0.19699.
  - **The 17 pages of "only asserted" arguments** are now proved in the appendices. These are locality, the tilt chain,
    the start chords, heading Step 3, departure (ii)–(iv), and the touch-down window, virtual, tail, hole and curve
    lemmas. I could verify each one from the text alone.
- **ε-uniformity.** I found no O(·), ≲, ≍ or "small v0/R" whose constant depends on ε. Every such constant depends only
  on the following:
  - Appendix A: the locked numbers (with m). C_* is an explicit polynomial; its value is ≈ 1.1·10⁷.
  - Appendix B: η alone, plus ξ1(η).
  - Appendix C: C_td, κ_c, G_T, c_sep(λ0), C_D, C_H(R), and the absolute ratio W_e/R = 6/κ_c.
- **Where ε enters.** It enters only in the ways the text announces:
  - λ ≥ ε/2;
  - ε ≤ R/10;
  - leg duration versus base advance;
  - ω(t_td) ≤ vε, the virtual strip ξ < ξ1ε, and ξ_e ≍ ε^{1/(2−2v)};
  - the explicitly bounded integral ∫h_H²/(t+ε).
- **The order m → λ0 → R → v0 → ε\* has no circularity.** Details are in §4.

## 1. Findings (in order of weight)

**F1 (FALSE as worded; harmless): Theorem 5.1 (T0), and the proof in App. B.9.**
- **The text.** It defines 𝒢 as the labels with Θ = 2π or Θ ∈ [α0, α0+ξ1ε), "whose directions are seen by t_td".
- **Counterexample.** Take θ = α0+ξ with roughly 1.1ε < ξ < ξ1ε (ξ1 = 2/c_ρ ≈ 4).
  - Lemma B.5(a),(d) give ρ_θ(t) ≥ c_ρ(ξ+ω), and ρ_θ is decreasing on [t1, t_td].
  - So min ρ = ρ(t_td) = h/(cos β+v) = (1+O(η+v))ξ + O(vε) > ε.
  - Hence that direction is *not* seen by t_td.
- **What the proof shows instead.** An unseen direction in the strip keeps ρ > ε, so its true and virtual candidates
  agree, and its label is *true*. The clause that is actually used is "every θ is seen by t_td or carried by a true
  label". That clause is correct, and it is all that Prop. 6.3 Step 7 and Table 1 use.
- **Fix.** Replace "…, whose directions are seen by t_td;" with: "…; for u ∈ 𝒢 the direction Θ(u) is seen by t_td or u
  is true;".
- **Related wording slips (also harmless):**
  - main5 calls b_e "the last tail direction that was not seen". In fact b_e *is* seen, with ρ_min = C(b_e)/g_max = ε
    exactly, since h(t_td) < 0 forces the crossing of cos β = v. Say instead "the boundary direction of the seen sliver".
  - main5 says the seen labels "[b_e, α0]" are cut off. Υ keeps b_e, so the cut-off set is (b_e, α0).

**F2 (FALSE inequality; conclusion true): Lemma B.7(c), the line "The correction … is ≤ (1+v)/((1−v)τ²) ≤ 1".**
- **The text.** From τ^{1+v} ≥ 2|h|/((1−v)C) one gets an *upper* bound on |h|/C, so the stated inequality points the
  wrong way.
- **The exact value.** Eliminating C/|h| gives corr = (1+v)/((1−v)τ² − (1+v)). This is slightly *larger* than the
  stated bound.
- **Why the conclusion survives.** τ^{1+v} ≥ cη^{−1/2} is already established, so τ² ≥ 2(1+v)/(1−v) for small η, and
  corr ≤ 1 still holds.
- **Fix.** "corr = (1+v)/((1−v)τ²−(1+v)) ≤ 1 since τ is large".

**F3 (OK with fix): Lemma 6.1 (heading), statement versus proof.**
- **The text.** The lemma says ω0 is "independent of v". The proof defines ω0 := C_T m(δ0/R)^{γ_D} + 3C_td(W_e+δ0)^{7/8}
  + C_rot·v, which depends on v.
- **Fix.** Define ω0 with C_rot·v0 in place of C_rot·v. Since v ≤ v0, every bound still holds. The departure theorem
  then receives a genuinely v-independent ω0, and its "v0 depending only on C_D, C_H, ω0" is literally right.

**F4 (OK with fix): the cut b_c in Definition 4.1 versus Setting (H) and Theorem 4.2.**
- **The text.** Definition 4.1 allows a cut b_c < U. However, several steps silently assume b_c = U:
  - Lemma A.2(a2): "a final leg has U − a_j ≤ l(a_j,U) ≤ ε";
  - Lemma A.6: "the final leg has a_J ≥ U − ε > W_e";
  - Theorem 4.2(b): the intervals [a_j, a_{j+1}] cover [0,U].
- **The application is consistent with b_c = U.** Prop. 6.3 Step 1 takes the working front x⁰|_{[0,U_A]}, so U := U_A
  for Stage A. Only the (T2) estimate there uses the full-front U, which is legitimate because chords do not depend on
  the cut. main6, however, says "chase on x⁰ cut at U_A".
- **Fix.** Add "with b_c = U" to Setting (H). In §6, say that Stage A is the chase on the working front x⁰|_{[0,U_A]}.

**F5 (OK with fix): Lemma B.2(b) (Run 1, middle), α ∈ [π/2, π].**
- **The text.** It says "X − t ≤ cos α ≤ 0 … so ρ ≥ 1". This bound alone gives only ρ ≥ |cos α|, which is 0 at π/2.
- **Fix.** Add "and y ≥ sin α (y non-decreasing), so ρ² ≥ cos²α + sin²α".

**F6 (OK with fix): Lemma B.3(a), the range claims for b.**
- **The text.** It states "upper half b ∈ [0, π−β*), lower half b ∈ (π−β*, 2π−2β*]" without proof. These ranges feed
  Lemma B.2(e) (existence of candidates) and Lemma B.8(a) (y ≥ c).
- **A two-line proof.**
  - β1 ∈ (π/2, π), because h1 < 0 gives cos β1 < −v. This yields b < π−β*.
  - The double zero gives b ≥ 0, hence β1 ≥ β*.
  - Mirror labels have b = 2π − β1 − β* ∈ (π−β*, 2π−2β*].
- **Fix.** Add this.

**F7 (OK with fix): the choice of λ* in App. B.9.**
- **The text.** It requires "K_*λ_*^{1−μ_T} ≤ π" with λ_* absolute. As written this depends on v.
- **Fix.** Write K_*λ_*^{7/8} ≤ π. This suffices, since μ_T ≤ 1/8 and λ ≤ 1.

**F8 (OK with fix): App. C.1, the choice of λ0.**
- **The text.** It says "fix λ0 … with C_td λ0^{a′} ≤ 1", but also needs λ0 ≤ λ_*.
- **Fix.** Add "λ0 ≤ λ_*". The paragraph "Shrinking λ0" is then unnecessary: Theorem 5.1 already quantifies over every
  λ0 ∈ (0, λ_*].

**F9 (OK with fix): the Parameter Lock (main1), item (4).**
- **The text.** It omits ε_* ≤ (R/C_td)², which App. C.1 uses to get z0 ≤ R. The Lock also says ε_* depends on
  "R and v0". In fact ε_* depends on λ0 (through ε_T) and on R; the condition z0 ≥ 2ε is uniform for v ≤ 1/23.
- **Fix.** Add "C_td ε_*^{1/2} ≤ R" to item (4). Item (3) correctly says "finitely many" conditions; for completeness
  it could cite the extra caps 1/53, 1/300, R/10, mR/C1, 3/(16C_*) and R/(2·10⁴).

Minor typographical points, not affecting correctness:
- Lemma A.2(a2): the "j = 0" case of the induction is vacuous, because U ≥ 1.
- App. C uses the name C1 for 1 + D̄/(10R), which clashes with C1 of (A.farfinal).

## 2. Statement-by-statement verdicts

### Main text
| Statement | Verdict | Notes |
|---|---|---|
| §1 problem set-up, local existence and limit at catch | OK | |
| Thm 1.1 (main) | OK | Follows from Prop 6.3 by scaling (end of §6); d·ε̂ = ε′ is checked. |
| Cor 1.2 | OK | Follows from Lemma 7.1; the dyadic D_N are nested. |
| Parameter Lock | OK with fix (F9) | m²r_* = 0.04 < 2 = 4c_A ✓; A0s0 = 1/4 ✓; e^{2μ} ≤ δ1 ✓. |
| Def 2.1 (Design T) | OK | |
| Def 3.1, Lemma 3.2 (F) | OK | I checked f/ρ − f′ = ρ/max(ρ,ε)², eigenvalues, (iii) and (iv). |
| Def 3.3, Lemma 3.4 (vflow) | OK | The sign of ψ_t is checked (T^⊥·r̂ = sin φ). |
| Lemma 3.5 (seen) | OK | |
| Lemma 3.6 (chords) | OK | Mixed case: at the far point both laws coincide. Boundary case by perturbation (needs X_b away from P on the compact interval, which holds). |
| Def 3.7, Lemma 3.8 (excess) | OK | (c): c ≥ (2/K)sin(Kl/2) ≥ l − K²l³/24. |
| Lemma 3.9 (split tilt) | OK | The identity \|d\|²(1−\|d\|²/4) = \|e_J×e_I\|² is checked. |
| Lemma 3.10 (E′) | OK | I recomputed ∂Q bounds (\|∂_{y2}Q\| ≤ \|y\|⁻², max 1 at y2 = 0), the integration by parts, Wirtinger, and the l′ bound. |
| Lemma 3.11 (Duhamel) | OK | |
| Def 4.1 (chase) | OK with fix (F4) | |
| Setting (H) | OK with fix (F4) | "Every pair with λ ≤ R is good" ✓. |
| Thm 4.2 (end) | OK | Proved in App A; (a)–(e) match Lemmas A.1–A.9 and Props A.7–A.9. |
| §5 conserved quantities | OK | |
| Thm 5.1 (touch-down) | (T0) FALSE as worded (F1); (T1)–(T5) OK | The used content of (T0) is proved. |
| Assembly lengths W_e, δ0, U_A, U_E | OK | κ_cW_e = 6R. |
| Lemma 6.1 (heading) | OK with fix (F3) | |
| Thm 6.2 (departure) | OK | Hypotheses and conclusions match App C.4 exactly, including (D3). |
| Prop 6.3 (conditional) | OK | Steps 1–7 of App C.5 are checked; T_stop ≤ 4 + 11 = 15. |
| Table 1 (coverage) | OK | |
| Lemma 7.1 (compactness) | OK | Gronwall constant 8v/c ✓; I closed and open ✓; "uncaught set open" ✓. |

### Appendix A (end theorem)
| Statement | Verdict | Notes |
|---|---|---|
| Conventions, (A.V0) | OK | e^{2/9} = 1.2488 < 1.25. |
| Lemma A.1 (chase basics) (0)–(4) | OK | Collinearity via the ray ODEs ρ′ = −1+vf(ρ) and σ′ = 1+vf(σ) ✓. |
| Lemma A.2 (toolkit): (CA), (c), (a1)–(a4), (b)(i)–(iii) | OK (F4 for (a2)) | c_A − 1/c6 = 5/18 = c_Aδ1/(1+δ1) ✓; 3κ/2 − 1 = 7/8 ✓; admissibility of (a_j,s) and (a_{j−1},U) ✓. |
| Lemma A.3 (locality) (i)–(iii) | OK | The t_W convention is consistent. |
| Lemma A.4 (tilt chain) | OK | s(ρ) = ρ/2 or √(ρ−1) ✓; N²/(4c) ≤ m²r/2 ✓. Case A/B is exhaustive (a family pair has a = a_j or a ≥ a_{j+1}). C_T = 6.1041 / 5.5718 ✓; C_μ = 47.58 / 39.81 ✓. |
| Lemma A.5 (continuity scheme) | OK | The uniform margin 9/8 and the passage to τ* are fine; τ* < ∞ via (a4). |
| Prop A.6 (far) | OK | E1 fixed: g/4 ≥ 5ε/4 ≥ ε. α_D*(2) = 1.2098 ≤ 5/4; 5v/R + 2v ≤ 0.507 < log 2; 12.5v ≤ ν; 1.6 + 192 ≤ 194; C_p = 8.62 < 9; C_β = 490.8 < 513; third-term factor 12.57 / 16 ≤ 16; C1 = 6.6·10⁴ < 7·10⁴. |
| Prop A.7 (near) | OK | Envelope, budgets, layer cake, terms I, II_long, II_a and II_b (g > 0, g = 0, β⁺ > b) are re-derived; leg sums; ∫H1 = 13.35 < 14, ∫H2 = 6.32 < 7; C_* ≈ 1.13·10⁷ (finite, ε-free). |
| Prop A.8 (length) | OK | 20·8/47 < 4; 0.4 + 2.5·log 24 = 8.35 < 9; κc6 + 1 = 6.625 < 7; C4 = 80.5 < 81; at C3 = 2·10⁴ the bound is 1.078 ≤ 1.125 ✓. |
| Proof of Thm 4.2 | OK | |

### Appendix B (touch-down)
| Statement | Verdict | Notes |
|---|---|---|
| Prop B.1 (integrals), g_max | OK | |
| Lemma B.2 (τ-relations) | OK | |
| Lemma B.3 (transport) (a)–(c) | OK | I verified k_t and the identity kw³ = τ^vJ/(1−v²) − w³𝔖 term by term (∂_θL⁻¹ gives the (v + cos(φ−ψ)) part; the a·c·∂τ^v part gives the ρ𝔞∂log C/w² part); both 𝔖 bounds ✓. |
| Design-T frames, (B.run1), (B.run2h), (B.run2tau) | OK | |
| Lemma B.4 (Run 1) (a)–(e) | OK (F5 for (b)) | 𝔖(0) = 0 ✓; 𝒯 ≤ E^v τ_α^{−2v/(1+v)} ✓; y ≲ α^{(1−v)/(1+v)} ✓. |
| Lemma B.5 (window) (a) | OK with fix (F6) | Tangency identity re-derived; bracket = (1−v²)t1(cos α0 − cos θ) ✓. |
| (b) timing | OK | cos α0 − 1/2 = v(3−2v)/(2(2−v)) ✓; ∫(1−f) = ε/3 ✓. |
| (c) window data | OK | Perturbative and ε-free; τ_b^v∂C identity ✓; tail sign ξ∂log C ≤ −1 ✓. |
| Lemma B.6 (forward) (a)–(e) | OK | |
| Lemma B.7 (virtual) | OK | Gronwall on [t_a, t_td] uses ξ < ξ1ε twice, as stated; ψ(α0) = 0 ✓. |
| Lemma B.8 (tail) (a), (b), (d) | OK | The three ranges cover [b_e, α0] once C0v ≤ 1/2. |
| Lemma B.8 (tail) (c) | OK with fix (F2) | y ≍ ξ^{2−μ_T} exponent ✓. |
| Lemma B.9 (bulk, hole, chords) | OK | Foot of the perpendicular (5+i√3)/4, distance 1/2 ✓; mirror tangent e^{i(π/2−δ)} ✓; Z_s case split ✓. |
| Lemma B.10 (curve) (a)–(d) | OK | |
| Proof of Thm 5.1: constants | OK with fix (F7) | |
| (T0) | see F1 | |
| (T1) | OK | The three cases are exhaustive; Case 3 uses Lemma 3.8(c). |
| (T2) | OK | Non-wrap via chords incl. Z_s; wrap (Δ > 2π−Δ0) via z_a ≥ u_a/2, z_b ≤ −(c/C_w)u′_b. |
| (T3)–(T5) | OK | |

### Appendix C (departure and assembly)
| Statement | Verdict | Notes |
|---|---|---|
| C.1 conventions, (R1)–(R5), ε_* | OK (F8, F9) | ε^{1/(2−2v)}/ε = ε^{−0.477} ≥ ε^{−9/20} ✓. |
| Lemma C.1 (start chords) | OK | a′ = 7/8 ≥ γ_D + ν = 19/24 ✓. |
| Proof of Lemma 6.1 | OK (F3) | ρ_* = ½(3/4 − 1/10)R − R/8 = R/5 ✓; close-case durations 1.485R ≤ 3R/2 ✓; 0.19699 + 1/40 + 1/40 < 1/4 ✓; Λ ≤ 2(t+ε) ✓. |
| Proof of Thm 6.2 (i) | OK | √(15/16) = 0.968. |
| Proof of Thm 6.2 (ii) | OK | d·Aû sign ✓; 1/(γ−2v) ≤ 2 ✓. |
| Proof of Thm 6.2 (iii) | OK | (C.hint) is ε-free. |
| Proof of Thm 6.2 (iv) | OK | ρ̲ ≥ 5λ ≥ 4l ✓; α_D*(4) = 1.092 ✓; \|p_a\| bound ✓. |
| Proof of Prop 6.3, Steps 1–7 | OK | Stage-A (S1) via U − U_A ≥ 1/2 and κ_c/2 ≥ 6R ✓; common legs by induction ✓; D ≤ D̄ ✓; (D0) with (9/4)C_td ≤ C_D ✓; g_W ≥ K_RR ✓; η_N(1/53) = 0.0412 ≤ 1/24 ✓; TW ratio ≤ 2·(1/4+1/4) ✓. |

## 3. The five targeted checks

**(1) Hidden ε in O(·), ≲, ≍ and "small v0/R".** None found.
- App B fixes η first and makes every c, C depend on η only. The smallness of ε there is uniform in v ≤ v_T, for
  example Cε^{2−2μ} < 1/2 and C(α0−ε/2) < ε.
- Every O_R(v) in App C is v × (a polynomial in C_D, C_H, ω0, X_* ≤ 1, 1/γ_D, 1/(1−γ_D)).
- The single dangerous integral ∫dt/(t+ε) is defused by the (t+ε)^{γ_D} branch of h_H.

**(2) Quantifier order.** The order is
m → (η, v_T, λ_*, absolute touch-down constants) → λ0 (≤ λ_*, C_tdλ0^{7/8} ≤ 1) → c_sep(λ0), ε_T(λ0) → R (R1–R5) →
C_H(R), C_rot, ω0 → v0 (App A caps, the departure v0(C_D, C_H, ω0), 1/23, 1/53, v_T, δ_t ≤ 1/16, O_R(v) ≤ ¼s0m(K_f/K_R)^ν,
C1^{η_N} ≤ 2) → ε_* (ε_T(λ0), R/10, (R/C_td)², z0 ≥ 2ε).
- No constant is used before it is chosen.
- C_D = 4C_td+1 is fixed before R, and (R5) uses only C_D, not C_H.
- The heading lemma needs Theorem 4.2 for Stage A, which needs only (R1)–(R3) and v0(m,R).
- No step of Stage A uses the whole-front theorem. (TW) is obtained from Stage A plus departure, before the whole-front
  end theorem is applied.

**(3) Interfaces.** Each main-text statement matches what its appendix proves, except:
- (T0)'s wording (F1);
- ω0's v-dependence (F3);
- the implicit b_c = U (F4).

Every appendix uses only labels that are available: lem:F, vflow, seen, chords, excess, splittilt, Eprime, duhamel,
chase, toolkit, locality, tiltchain, startchord, and the touch-down items. Theorem 4.2(e) (causality) is stated but
never needed; Step 2 of Prop 6.3 uses Lemma A.1(4) directly.

**(4) Parameters.** Every claimed number is reproduced by `chk.py`:
- c6 = 9/2, c_ρ* = 1/4, K1 = 2 (ρ̲ ≥ 2l), c_R* = 47/8;
- C_T = 6.104 / 5.572, C_μ < 48, C_p < 9, C_β < 513, C1 < 7·10⁴;
- ω0's first term = 0.19699 < 0.198.

Every condition that uses γ = 2/3, γ_D = 3/4, ν = 1/24, κ = 5/4, c_A = 1/2, δ1 = 5/4, K_f = 10, K_R = 12, s0 = 1/8,
A0 = 2, f_F = 1/2, η1 = 1/2, K_ε = 10, d_L = 2 and m = 1/10 holds. In particular:
- γ + ν < 1 for both exponents;
- (1+1/K_f)η1R ≤ 0.55R < R;
- K_f + 1 ≤ K_R;
- κ < 4/3;
- f_F² ≤ θ̄ = 5/8 and s0² ≤ θ̄;
- 17/16 ≤ 9/8.

**(5) Case analyses.**
- **Near pairs.** Long and short type; within short type g > 0 (including g′ < ε/2) and g = 0 (including the final
  leg and β⁺ > b); the start value (far before, or near from t_td; tail pairs are far at t_W). Complete.
- **Touch-down seen set.** It covers [−α_s, α_s] (Run 1), [b_e, α0] (three ranges), and the virtual strip (seen or
  true, per F1). Complete.
- **The hole.** Z_s, Γ_s C¹ with a Lipschitz tangent, and chords through Z_s by one-sided limits with the θ_b = π split.
  Complete.
- **Wrap pairs in (T2).** Δ ≤ 2π−Δ0 or Δ > 2π−Δ0, and in the second case both ends lie in the forward or tail zone
  with the stated signs. Complete.
- **(T1).** The three cases are exhaustive.

**(6) Corollary.** OK.
- Arzelà–Ascoli is applied correctly.
- The claim's Gronwall constant is correct.
- The first-hitting-time contradiction is correct.
- The step "the uncaught set is open and misses a dense set" is correct.

## 4. Comparison with `short/` (done after the independent reading)
- The rewrite drops (S1G) and the explicit constant tables. This is legitimate, because the flat bound ρ̲ ≥ (47/8)R on
  {g > K_RR} costs only O_R(v) once v0 is not explicit.
- The near-pair proposition replaces the computer-certified D′ with an explicit finite C_*.
- The heading and departure proofs follow `short/sec5` step by step, with constants replaced by C(R) or O_R(v). I found
  no step of `short` that the rewrite omits and needs.
- The start-chord lemma removes the concavity argument of `short/sec8` by normalising C_tdλ0^{7/8} ≤ 1. This is valid.

**Overall: a complete and correct stand-alone proof once F1–F9 (wording and one-line additions) are made. There are no
gaps that need new mathematics.**
