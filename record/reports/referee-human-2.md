# Referee report 2 (adversarial) on `human/snitch_human.pdf`

Scope: (1) try to break the proof where it is most likely to be wrong: Appendix B (touch-down), the far-pair step of
Appendix A at the smallest far gap, and the smallness hypotheses of Appendix C; (2) check every figure against its
caption and the mathematics; (3) readability for an analyst who does not know the project. I did not read
`reports/referee-human-1.md`. The PDF builds cleanly (42 pp., no undefined or multiply defined references).

**Verdict.** I found **no FALSE step and no GAP** in the parts I attacked. The perturbative Appendix B holds up, both
by hand and in a high-precision check down to ε = 1e-30. Every "for v ≤ v_T small" in Appendix B has a v-threshold
that does not depend on ε, and every "for small ε" has an ε-threshold that does not depend on v. The far-pair step
with δ₁ = 5/4 is correct, as is its arithmetic. The departure and heading arguments are correct. I list one
**FALSE statement in a theorem** (wording only; the proof is right), about ten **fixes**, five figure defects (one
caption is false), and a readability list.

---

## 1. Correctness

### 1.1 Appendix B: numerical stress test (mpmath, 130 digits)

Method. I used the paper's own exact straight-run integrals (C = ρ𝔤(β) constant, h decreasing at rate 1−v²). With
them I computed exactly the true candidates at t₁ (Run 1) and at t_td (Run 2) for v ∈ {0.01, 0.04} and
ε ∈ {1e-4, 1e-12, 1e-30}. Label derivatives come from central differences with step 10⁻²⁵ξ. For the virtual labels
ξ < ξ₁ε, I took the exact true data at t_a and integrated the regularised flow on [t_a, t_td] in the scaled variables
r/ε and (t−t_a)/ε. In those variables the problem does not depend on ε. I used RK4 with 4·10⁴ steps for (r, ∂_θr).
Scripts: `numerics/referee-checks/chkB.py` and `numerics/referee-checks/chkB_virtual.py` (outputs not kept).

| Claim (App. B / Thm 5.1) | What I checked | Result |
|---|---|---|
| Tangency identity, Lemma B.5(a) | ∂_θ𝔟 against Λ(θ) sin((θ−α₀)/2) at θ = α₀+0.03 | equal to 15 digits (v = .01, .04) |
| Timing, Lemma B.5(b) | α₀−π/3 ∈ [−2v, 0]; ω(t_td)·3(1−v)²/(vε) | −0.87v and −0.87v; ratio 0.994 and 0.976 (≤ 1 ✓) |
| ξ_e ≍ ε^{1/(2−2v)}, Lemma B.8(a) | ξ_e/ε^{1/(2−2v)} | 1.398 (v=.01), 1.349 (v=.04), **the same for ε = 1e-4, 1e-12, 1e-30** |
| Seen set [b_e, α₀], Lemma B.8(b) | min over [0,t_td] of ρ(true)/ε, for ξ = f·ξ_e and ξ = f·ε | seen ⟺ ξ ≤ ξ_e (threshold sharp: 0.999999ξ_e seen, 1.000001ξ_e not). The range ξ ≤ ε/2 is seen with ρ/ε ≤ 1e-5, and ≤ 1e-28 at ε = 1e-30 |
| (T5) z₀ ≍ ε^{1/(2−2v)}, \|y₀\| ≲ z₀^{2−μ_T} | z₀/ε^{1/(2−2v)}, \|y₀\|/z₀^{2−μ_T} | 1.438 / 0.494 (v=.01), 1.512 / 0.479 (v=.04), the same for every ε; z₀ ≥ 2ε holds by a wide margin |
| Forward-arc tilt, Lemma B.6(c) and (T3) | \|ψ(t_td)\|/ξ^{1−μ}, ξ from 0.1 down to 3ε | 1.0025 (v=.01), 1.0094 (v=.04) at every ξ and every ε. The exponent 1−μ is sharp |
| Virtual labels, Lemma B.7 | \|ψ(t_td)\|/ξ^{1−μ} for ξ ∈ [10⁻³ε, 4ε] | 0.79–1.01, identical for ε = 1e-12 and 1e-30. w(t_td) ≤ 1.08 |
| Tail tilt, Lemma B.8(c) and (T4) | \|ψ\|/ξ^{1−μ_T}, ξ ∈ [ξ_e, 0.1] | 0.998–1.000. The exponent 1−μ_T is sharp, and ψ < 0 as claimed |
| (T2) for wrap pairs | chord/(u_a + U − u_b) for a ∈ {Harry, forward labels} × b ∈ tail labels | min 0.9999 (κ_c ≤ ½ suffices), uniform in ε |

All of these match the paper, uniformly in ε. The ratios are the same to 4–5 digits from ε = 1e-4 to ε = 1e-30, which
is exactly the claimed ε-independence. One numerical observation shows that a theorem statement is false as worded
(B1 below).

### 1.2 Appendix B: findings

- **B1 (FALSE as stated, fix wording).** Thm 5.1 (T0): "*where 𝒢 is the set of labels with Θ(u)=2π or
  Θ(u)∈[α₀,α₀+ξ₁ε), whose directions are seen by t_td*". The forward window labels with ξ ≳ ε are **not** seen by t_td.
  Numerically, min ρ/ε = 1.012 at ξ = ε and 2.02 at ξ = 2ε. The window extends to ξ₁ε, and ξ₁ = 2/c_ρ ≥ 2 because
  ρ(t_td) ≈ 1.01ξ. The proof of (T0) in §B.8 handles this correctly ("an unseen true candidate keeps ρ>ε, so it equals
  the virtual one"), and Step 7 of App. C only needs "seen or carried by a true label". Fix: "...whose directions are
  seen by t_td or are carried by the label u itself (virtual = true while ρ > ε)". Alternatively, drop the window from
  𝒢 except for the label α₀.
- **B2 (fix).** §B.8 (proof of Thm 5.1), choice of constants: "*Choose λ_* … absolute with … K_*λ_*^{1−μ_T} ≤ π*". This depends on v
  through μ_T. Write K_*λ_*^{1/2} ≤ π (since μ_T ≤ ½), which implies the condition for all v ≤ v_T.
- **B3 (cosmetic).** Lemma B.8(b), range 2: "*h(t_td) ≤ −½ξ + η³ξ + vε*". The term −𝔯(1−cos𝔟) is ≤ 0, so +η³ξ is a
  harmless over-estimate. Drop it.
- **B4 (OK, worth one sentence).** Every threshold is ε-free. The v-thresholds are C₀v ≤ ½ with C₀ = 3 absolute (range
  2), v < 1−2C²η (forward arc), and μ ≤ 1/9. The ε-thresholds are C·ε^{2−2μ} < ½ (range 3), C(α₀−η) > εg_max,
  ξ_e ≤ η/4, ξ_e ≥ ε/2 and 2ε_T < c_sep, all with v ≤ 1/4. I suggest adding this list as one line after the
  Conventions of App. B, because "for small v" and "for small ε" alternate within single proofs.
- **B5 (OK).** I checked by hand: Prop. B.1 and Lemma B.2; Lemma B.3(b) (L, singular values 1±v); Run 1(c), including
  𝒯 ≤ (1+Cv)(2/α)^{2v}; the tangency derivation; window (c); forward (a)–(e); virtual (the Grönwall step and its use of
  ξ < ξ₁ε twice); tail (a)–(d) (the exponent algebra y ≍ ξ^{(2−v)/(1+v)} = ξ^{2−μ_T} and τ/τ_𝔟 ≲ ξ^{−3/(1+v)} are
  right); bulk (lower-half range 𝔟 ≤ 2π−2β* holds because β₁ ≥ β* on the upper half); hole; the T1 case split; and
  T2–T5.

### 1.3 Appendix A: the far-pair step at the smallest far gap (g = K_fλ = 5ε, δ₁ = 5/4)

**OK.** This is the step that was previously false. Step 1: with ε ≤ 2λ ≤ 2g/K_f = g/5, the bound gives
ρ̲ ≥ c_A g − δ₁ε ≥ g/2 − g/4 = g/4 ≥ 5ε/4 ≥ ε. It also gives ρ̲ ≥ (5/2)λ ≥ 2l, which uses l ≤ κλ = (5/4)λ exactly.

I re-derived the remaining links:
- Lemma A.1(3): |P−x_{a_j}| ≤ δ₁ε needs e^{2μ} ≤ 5/4. At v = 1/10 this is e^{2/9} = 1.2488, a 0.1 % margin; App. C caps
  v ≤ 1/23 anyway.
- Toolkit (c): the good pair (a_j, s) and the case w < ε/2.
- α*_D(2) = 1.21 ≤ 5/4.
- The amplification bound: 5v/R + 2v < log 2 and (25/2)v ≤ ν for v ≤ min(1/300, R/10).
- The offset bound: g' ≥ g−ε ≥ 4ε ≥ ε/2, so L and I' are family pairs. C_p = (κC_μ)^{1/2}(1.1)^{1/2+γ} = 8.73 < 9.
- C_β = 512.5 < 513, the "16λ^{γ−1}" bound, and C₁ = 68768 < 7·10⁴.

Also checked: Lemma 3.10(iv) (|∂_{y₂}Q| ≤ |y|⁻² holds, with maximum 1 at φ = 0), C_T < 6.11 and 5.58, and C_μ < 48.
The near-pair and length propositions do not depend on ε, as claimed. I did not re-derive every constant there; that
is the first referee's task.

### 1.4 Appendix C: departure smallness and heading

**OK.** Points I checked:
- Departure (i)–(iv): the expansion of d·AT, |q_û| ≤ |y|/ρ², and the variation-of-constants integrals
  (∫X⁻² ≤ X₀⁻¹ and ∫X^{γ−1−2v} ≤ 2X^{γ−2v} since γ−2v ≥ ½).
- The integral ∫h_H²/(𝔱+ε) ≤ C(R): it needs D+ε ≤ 1, which follows from (D3) because C_D ≥ 1 gives X_* ≤ 1/16. Say
  so explicitly.
- Phase 1 of (iv), which uses N' ≤ v‖AT‖ and so has no singular amplification, and the phase split at k_Dλ.
- Heading: the far case ρ_* = R/5 (again δ₁ = 5/4); the close case with K₁…K₄; the durations (κ/(1−v) ≤ 11/8); and
  ω₀: C_T m 4^{−3/4} = 0.197 ≤ 1/5.
- (R1)–(R5) and the ε_* conditions: ε^{1/(2−2v)}/ε ≥ ε^{−9/20} for v ≤ 1/23 is correct (the exponent is −21/44).
- Step 5, the (TW) ratio.

Fixes:
- **C1 (fix).** App. C Conventions call v_T, ε_T, λ₀, G_T, c_sep, κ_c "*the absolute constants of Theorem 5.1*". But
  ε_T and c_sep depend on λ₀, which is fixed only in the next paragraph. Say "fixed once λ₀ is fixed below".
- **C2 (fix).** Name clash: C₁ is the far-pair constant in (A.farfinal) and also "C₁ := 1 + D̄/(10R)" in C.5. Rename one.
- **C3 (cosmetic).** In the statement of Theorem 6.2, add "(in particular D+ε ≤ 1)" after (D3), since (C.hint) uses it.

### 1.5 Main text

- **M1 (fix, overstatement).** §2: "*Its bendiness is of the same order on every scale, which is exactly what the
  bootstrap forbids.*" The exact integrals (y = Cτ^v, τ^{1+v} ∝ t) show what happens at the corner end. At scale δ the
  arm is the graph x ∝ y^{1+v}: its direction tends to the **perpendicular** of Harry's path (visible in Fig. 3(a),
  where the 10⁻⁶ curve is almost vertical). The relative bendiness therefore decays like δ^{v/(1+v)}, not "the same on
  every scale". It is still forbidden, because the bootstrap needs decay like δ^{γ} with γ = 2/3 ≫ v. Suggested text:
  "its bendiness decays only like λ^{1/2+O(v)}, far more slowly than the λ^{1/2+γ} that the bootstrap requires".
- **M2 (fix).** §7: "*the method itself … is expected to break down somewhere around v ≈ 0.05*" is unsupported. Give a
  reason or delete it.
- **M3 (fix).** Fig. 2 caption: "*the bound in the proof is 15*". The proof says nothing at v = 0.1. Write "(the proof,
  for v ≤ v₀, gives 15)".
- **M4 (OK).** Lemma 7.1 (compactness): the closedness of I uses |S̃'| = v to extend to the endpoint. That holds, but it
  is worth half a sentence.

---

## 2. Figures

I rendered all six PDFs and read all six scripts in `human/figs/`.

- **Fig. 2, Design T (`fig_designT.py`, v=0.1, ε=0.02). Matches, with caveats.** Run 1 through the front is visible:
  in (a) Harry is just at or over the front at t = 1.25, and (b) shows the run-1 segment to x = t₁ ≈ 2.11 and the
  turn. To make "straight through" clearer, take snapshot (a) at t ≈ 1.8. In (c) the touch-down is tangential. It sits
  at about 66°, not at e^{iπ/3}, because v = 0.1 moves the front; the text's "e^{iπ/3}" is the v = 0 statement, which
  is consistent. The walk in (d)–(f) is correct, counter-clockwise from α₀, and the finish time 13.73 agrees with
  Fig. 8.
  - Caveat: `snitchsim.simulate` walks the **whole virtual front**. That includes the already-seen sliver [b_e, α₀) and
    the virtual labels near direction 0. The proof instead cuts the front at b_e and uses true candidates plus Z_s. So
    the figure shows a close variant of the path of Theorem 1.1, not that path exactly. Say so in a docstring or a
    caption phrase, or cut the label set at b_e.
  - See also M3.
- **Fig. 3, hook (`fig_hook.py`, v=0.2). Honest in substance, but the caption oversells.** The dynamics are the true
  field (DOP853, rtol 1e-12). Panel (a) uses the scale invariance r·Z(T/r) correctly, and the interpolation error is
  negligible. But:
  - (i) both initial arms are **models**, not Design T fronts: (a) is a ray at angle 2 arcsin v starting *exactly at
    Harry* (the ε = 0 idealisation of a corner), and (b) is the parabola y = s²/2 with its end 0.03 behind Harry. The
    caption should say "model arms".
  - (ii) In (b), fine-scale straightness is automatic, because the end is at positive distance from Harry and the
    curve is analytic there. In (a), the end sits at Harry. The comparison is fair only as ε → 0 with z₀ ≍ ε^{1/2} ≫ ε;
    one sentence would say this.
  - (iii) The hook converges to the perpendicular direction (see M1). "the finer the zoom, the more it has turned" is
    true, but it turns toward a limit.
  - (iv) "*only at scale 1 does one see the round shape of the whole front*": the arm is a 1.5-long parabola, not the
    whole front. Replace with "the curvature of the arm".
- **Fig. 5, timeline (`fig_timeline.py`). Caption FALSE as written.** "*during the simulated walk of Figure 2 (v=0.1,
  ε=0.01)*": Fig. 2 uses ε = 0.02, and this script uses ε = 0.01. Fix either one.
  - "pair of length λ = 0.02 / 0.1" is the **angular label length**. Arclength at t_td is about 1.1λ, though the
    far/near test in the script correctly uses arclength.
  - The docstring says it plots "N/λ^{3/2}"; it plots 100(N/N_td − 1).
  - "moves by a percent or two": the right panel moves about 0.4 %. Say "at most two percent".
- **Fig. 6, touch-down (`fig_touchdown.py`, v=0.1, ε=0.01). Correct.** The tail end E is above the heading line on the
  same side as the front, consistent with (T5) (y₀ < 0 in the paper's sign convention, which my numerics also give).
  Both arcs are tangent to n̂ at their ends. The band has width 2ε. The bracket says "≈ε^{1/2}" but shows about 0.13,
  which is ≈1.7ε^{1/(2−2v)}. Consider labelling it ≍ε^{1/(2−2v)}.
- **Fig. 1, problem (`fig_problem.py`, v=0.25).** The fronts in (b) are computed with the **regularised** field at
  ε = 0.04, so they are closed curves through direction 0. The true front has a caught candidate there (§3 says "the
  front of real candidates tears"). The "direction 0: caught" pointer lands on the dashed t = 0 circle. Either use the
  true field and show the hole, or add "(regularised candidates, §3)" to the caption.
- **Fig. 8, limit (`fig_limit.py`). Correct**, and consistent with Fig. 2 (13.67–13.73). "it shrinks with ε" holds on
  the whole except for end-of-walk spikes, which come from different final legs. One clause in the caption could say
  so.
- **TikZ Figs. 4, 7 and 9.** These agree with the definitions (K_f = 10 near/far; ρ_s ≥ ½(s+z₀+𝔱) is Theorem 6.2(i)).

---

## 3. Readability

### 3.1 The ten hardest places, with concrete simplifications

1. **The Parameter Lock box (§1, p. 2).** At first reading it refers to C_T, ω₀, δ₀, R, λ₀, λ_*, v_T, ε_T(λ₀), r_*,
   the "geometric tilt condition", A₀s₀ < f_F and "the tail end at touch-down", none of which is defined yet. *Fix:* in
   §1 keep only the list of numbers and the sentence "the order of choices m → λ₀ → R → v₀ → ε_* is explained in §6".
   Move items (1)–(4) to the start of §6 or to App. C.1, which already repeats them.
2. **Setting (H) (§4).** It stacks body, tail and good pairs, ℱ versus ℱ_*, j_W, t_W, and the weights
   min(1, K_fλ/min(a,K_RR))^ν in (S2) and (TW) without motivation. *Fix:* state Theorem 4.2 first with W_e = 0, then add
   the excused tail as a remark. Explain in one sentence that the ν-weight pays for the logarithmic amplification
   ∫v dt/g (this is said only later, in "Far pairs").
3. **Why the family is {a = a_j or a ≥ a_{j+1}}.** This is never explained. Add: "pairs starting strictly inside the
   current leg are already within ε of Harry and hence seen".
4. **The statement of Theorem 5.1.** It has a three-kind label assembly, Θ, 𝒢, Z_s, and a two-level constant hierarchy
   (λ₀-dependent c_sep and ε_T, absolute v_T, ξ₁, G_T, κ_c, C_td). App. C then immediately fixes λ₀ by
   C_tdλ₀^{7/8} ≤ 1. *Fix:* fix λ₀ inside the theorem. This deletes the "Shrinking λ₀" paragraph of C.1 and Remark B.11.
5. **Lemma B.3(c) (the transport of curvature with 𝔖).** It appears with no explanation of where 𝔖 comes from. Add one
   displayed line: kw³ = q×∂_θq = τ^vJ/(1−v²) − w³𝔖, with J time-independent.
6. **Lemma B.5(a), the tangency identity.** The derivation is compressed into three sentences. Give the intermediate
   identity (1−v²)ρ₁∂_θβ₁ = sinβ₁[h₁(cosθ−v)+sin²θ]/sinθ as a display, and say why the bracket vanishes exactly at α₀.
7. **The near-pair proof (App. A.6).** It combines the layer cake, the budgets Ω and G, H₁ and H₂, θ = ε/λ and ξ = g/λ.
   *Fix:* introduce the two dimensionless variables in a displayed line with their ranges, and isolate the layer-cake
   inequality as a numbered lemma.
8. **Heading Lemma, Step 3 (C.3).** The close and far cases with K₁…K₄ are hard to picture. The figure helps, but
   K₁…K₄ are not drawn. Label K₁ and K₂ in Fig. 9.
9. **Why two exponents γ = 2/3 and γ_D = 3/4.** The main text never says why. The reason, hidden in C.5, is that (TW)
   needs γ + ν + η_N ≤ γ_D, so the main walk must use a smaller exponent than the departure and heading. One sentence
   in §6 would do.
10. **Proposition 6.3, Step 2 (common legs and causality).** Two chases (Stage A cut at U_A, and the real walk cut at U)
    coincide until t_W. *Fix:* say in §6, before Lemma 6.1, that "Stage A is a bookkeeping device: the path is the same,
    only the cut differs".

### 3.2 Notation used before its definition

- μ_T (§1 Notation): its meaning appears in §5.
- M, R, γ in "Mλ^γ = m(λ/R)^γ" (§3.2): defined in §4.
- K_f, the gap g, legs and x_{a_j} in Fig. 4 (§3): defined in §4.
- t_a, t_td and ω(t) in Definition 2.1. ω(t) is never used in the main text; move it to App. B.
- C_T (Theorem 4.2(c)): its formula is only in App. A.1.
- ξ₁, b_e and ξ_e in Theorem 5.1: "defined in Appendix B". Give one-line definitions in §5.
- In the Parameter Lock: ω₀, δ₀, λ₀, λ_*, v_T, ε_T and r_* (see item 1 above).

### 3.3 Overloaded symbols (each has two or more unrelated meanings)

- β: polar angle; β* (heading); the base β(τ) in App. A; the Duhamel forcing β.
- C: a generic constant; the conserved quantity ρ𝔤(β); C₁ in App. A and C₁ in App. C.
- ξ: label offset (App. B); g/λ (App. A.6).
- θ: direction; ε/λ (App. A.6).
- ω: t_c − t; ω₀; (1−2m²)^{−1/2} in Lemma A.4.
- η: window half-width; η₁; η_N; regularisation parameters in Lemmas 3.6 and 3.11.
- m: the locked number; the stretch majorant m(θ) in (B.stretch).
- E: excess; the tail end "E" in Fig. 6; the constant E in Run 1(c).
- D: max(ρ,ε) in A.6; the departure duration.
- a′: a label in App. A; the number 7/8 in App. C.
- 𝒯: the leg-time set in the Toolkit; (τ₁/τ_α)^v in Run 1(c).

Renaming the App. A.6 variables (ξ→x, θ→ϑ_ε) and the App. B stretch majorant (m→𝔪) would remove the worst clashes.

### 3.4 Can §§1–7 be read without the appendices?

As an **architecture**, yes. §§1–7 (16 pp.) state every result precisely, prove the calculus lemmas of §3 in full, and
prove the main theorem from Proposition 6.3 and the corollary. Table 1 makes the logical coverage auditable. As a
**proof**, no. The four load-bearing results (Thms 4.2, 5.1 and 6.2, Lemma 6.1, Prop 6.3) are proved only in the
appendices, about 20 pp. A reader who stops at §7 cannot check that ε-independence survives the near-pair estimate or
the touch-down window. Those are exactly the delicate points, and the main text only asserts them in "Where ε enters".

### 3.5 Cuts that lose no completeness (≈2–3 pp.)

- **The "ε enters only…" paragraph appears three times** (§4, App. A.1, App. C.1). Keep the one in §4 and refer to it
  from the others.
- **Prose before Table 1.** The four-step paragraph after Proposition 6.3 duplicates Table 1 and the proof in C.5.
  Keep the table.
- **λ₀ machinery.** Fixing λ₀ in Theorem 5.1 (item 4) removes the "Shrinking λ₀" paragraph, Remark B.11, and the λ₀
  clauses of the Parameter Lock.
- **Lemma B.3(a), k_t formula.** It is used only for the middle labels in Run 1(b). Run 1(b) can use Lemma B.3(c) from
  t = 0, where 𝔖(0) = 0, exactly as Run 1(c) does. That deletes the k_t formula and one Grönwall argument.
- **The Parameter Lock box** shrinks to two lines (item 1).
- **"Why straight runs help" (§2, last paragraph).** It repeats the opening of §5; merge them.
- **The parenthetical about tracking C_T (C.3).** "A reader who prefers not to track C_T numerically…" can go once
  0.197 < 1/5 is stated.

---

### Summary of required changes

- FALSE wording: (T0) "whose directions are seen" (B1); Fig. 5 caption ε = 0.01 versus Fig. 2's ε = 0.02.
- Fix: B2, C1, C2, M1 (hook bendiness wording), M2, M3.
- Fix figures: Fig. 3 caption (model arms; ε = 0 idealisation; "whole front"); Fig. 1(b) regularised front; Fig. 2
  (simulated path walks the uncut virtual front; "bound in the proof").
- No GAP found. The Appendix B claims are confirmed numerically to ε = 1e-30, with constants that do not depend on ε
  to 4–5 digits.
