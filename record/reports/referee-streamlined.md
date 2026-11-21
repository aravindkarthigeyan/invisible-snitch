# Referee report: `streamlined_snitch_proof.tex` (15 pp.)

Reviewed: `streamlined_snitch_proof.tex`, a user-supplied streamlined outline of the proof.
Compared against: `short/` (sec1–sec8, sec7a/b, appA; Def 3.3 side conditions (P0)–(P8); page numbers from `snitch.aux`).
Scratch check of the locked constants: scratchpad `chk.py` (computes c6, c_ρ*, K1, C_T, C_μ, ω0's first term).

## Verdict

**(C): the outline is correct, but the text leaves out substantial arguments. It also contains one false step, which a one-line parameter change repairs.**

- The architecture is ours, compressed faithfully: Design T, then the touch-down front, then a heading/departure stage A with an excuse length, then the end theorem by continuity, using far pairs (Duhamel), near pairs and length. The quantifier order m → R → v0 → ε* has no circularity.
- **The near-pair proposition is a valid, hand-checkable replacement for the computer-certified D′.** This is the paper's real simplification, and it works because v0 is no longer explicit.
- **One step is false with the locked parameters.** With c_A = 1/2, δ1 = 2 and K_f = 10, the far-pair claim "ρ_arc ≥ ε" does not follow (§E1). This breaks Prop. "Far pairs" (and the far-pair part of "Length") as written, for the pairs with λ ∈ [ε/2, 0.6ε) and gap g ∈ [K_fλ, 6ε). Setting δ1 = 5/4, or K_f = 20 with K_R = 21, repairs it with no other change.
- **It is not a stand-alone complete proof.** The touch-down theorem (our §§6–7, pp. 27–42, with 48 side conditions), the heading lemma and departure theorem (our §5, pp. 22–27), and the locality bookkeeping of the end theorem (our Lemma 3.9) appear as asserted "≍ / ≲ / perturbing from v = 0" estimates. I checked each one and found nothing false or ε-dependent in them; the ε-uniformity is genuinely visible in the structure (see §4). They are, however, nontrivial to write out. Read alone, the text is a correct and well-organised roadmap whose hard estimates must be taken on trust or from our 50-page paper.

---

## 1. Section-by-section

Legend: (a) routine, constants clearly ε-free; (b) true but needs a nontrivial omitted argument; (c) doubtful or false.

### §1. Statement and Parameter Lock
- The statement is implied by ours, so it is true.
- The Lock is a valid order (see §5). It omits the requirements v0 ≤ v_T and ε* ≤ ε_T, and the absolute cap on v0 that gives a′ ≥ 7/8 before R is chosen. These are implicit in "small". **(a)**

### §2. Virtual fronts
- Lemmas F, vflow, seen, chords, excess, split tilt, Eprime(i)–(iv) and Duhamel are complete or near-verbatim copies of our §2. **(a)**
  - I checked f/ρ − f′ = ρ/max(ρ,ε)², the bound in F(iii), and Lemma excess(c).
  - In the mixed-field case of chords(b), the field at the far point is the same under both laws, so monotonicity holds. Correct.
- The far inequality (iv) is our v2 form, using the arc minimum ρ̲ (sec2 Lemma 2.10(v)).
- Compactness: the final deduction (first hitting times t_N → t*, then a contradiction through the claim) is compressed to one sentence. The "uncaught set is open" step is correct. **(a)**

### §3. Chase and end theorem
- Lemma chase: as ours. **(a)**
- Setting (H) has no (S1G). This is legitimate here: with a non-explicit v0, the flat bound ρ ≥ c_R*R on {g > K_R R} costs only O_R(v).
- Small slip: (H) says δ_t = O(v), but the application gives O_R(v). **(a)**
- Lemma toolkit:
  - (a) Legs: the step with κ = 5/4 < 4/3 is checked (3κ/2 − 1 = 7/8).
  - (b) and (c): as ours.
  - (d) Dyadic tilts: the chain construction is only sketched (our Lemma 3.8, about 1 page). **(a/b)**
- Continuity scheme: as ours. **(a)**
- The opening of §4 states admissibility of all family pairs in [a_j, max(b, a_{j+1})] without proof. This is our Lemma 3.9 (locality), half a page, including the convention that t_W belongs to leg j_W + 1 for tail pairs. **(a)**

### §4.1 Far pairs — contains error E1
- **E1 is a false step; see §2.**
- Apart from E1, the proof is correct:
  - Amplification: ∫α ≤ O_R(v) + Cv log(ratio), and A0 = 2 absorbs it.
  - Forcing with g > η1R, and with g ≤ η1R. In the second case |p_a| ≤ CMg^{1+γ} via V_e(I′) ≤ C_μ M²(g+λ)^{1+2γ}, and I′ is a family pair because (1 + 1/K_f)η1R ≤ R.
  - Three-term combination: the first term uses (S2)'s min(1, K_fλ/min(a, K_R R))^ν factor exactly as we do.
  - Third term: γ + ν = 17/24 < 1, and 1/(1−γ−ν) = 24/7.
- Constants are O_{m,R}(v) and ε-free. **(a)**

### §4.2 Near pairs — correct (details in §3)

### §4.3 Length
- Correct apart from the same ρ̲ ≥ ε issue in the "Far, g ≤ η1R" bullet (E1).
- The other bullets can use l′ ≤ v∫a* directly; a* ≤ 2/D costs only a factor 2. **(a)**

### §5. Heading and departure (our §5, pp. 22–27, about 5 pages; here about 1.5 pages)
- **Heading lemma.** Steps 1–4 match our proof.
  - Step 3 (rotation: close and far cases, durations) is compressed from about 1 page. **(b, routine)**
  - **Slip E2:** h_H := C_H·min((t+ε)^{γ_D}, ω0) with C_H = C_H(R). This makes h_H ≤ C_H·ω0, which need not be ≤ 1/4, but (D2) needs h_H ≤ 1/4. It should read min(C_H(t+ε)^{γ_D}, ω0), as in ours.
  - **E3:** "ω0 ≤ 1/4 for small R, v0" is not justified as stated. The first term C_T^A·m·(δ0/R)^{γ_D} has δ0/R = 1/4 fixed, so it does not shrink with R or v0. It is small only through m. With the locked values it equals 5.572 × 0.1 × 4^{−3/4} = 0.197 < 1/4, which is true but tight and not shown. A smaller δ0 also fixes it. **(b, true)**
- **Departure theorem.** Items (i)–(iv) are correct in outline.
  - ε-uniformity of (iii) needs the (t+ε)^{γ_D} branch of h_H. The ω0 branch alone gives ∫ω0²/(t+ε) ~ log(1/ε). The text says "integrating … gives O_R(v)", which is true via that branch but leaves the step implicit.
  - The variation-of-constants details in (ii) are omitted (ours: 2.5 pages). **(b)**

### §6. Design T and touch-down (our §§6–7, pp. 27–42)
- Prop. integrals, Lemma τ-relations and Lemma transport are copied from our §6 with proofs sketched. **(a)**
- Theorem "Front at touch-down" is about 1.5 pages, against our pp. 30–42. See §4 for the ε-uniformity audit. **(b) throughout; nothing (c).**

### §7. Assembly
- Steps 1–4 match our §8.
  - "(T1) gives (S1)" for λ ≤ λ0 needs c = λ − N²/2 ≥ c_A·min(λ, K_R R). That requires C²λ0^{2a′} small, our conditions (C2) and (C3) with a concavity argument (Lemma 8.1). This is not stated but is achievable, because λ0 can be shrunk (then c_sep becomes λ0-dependent but stays absolute). **(a/b)**
- The (TW) computation in Step 3 is correct. It uses a′ ≥ 7/8 > γ_D = 3/4 > γ + ν + η_N = 17/24 + O(v), and C^{η_N} → 1.
- T_stop ≤ 4 + (5/4)·8·(11/10) = 15 holds.

## 2. Parameter check (locked values against our (P0)–(P8), (C·), (A·))

| Condition | Value | Status |
|---|---|---|
| (P0) γ > 1/2; γ+ν < 1 | 2/3; 17/24 (γ_D: 19/24) | OK |
| (P0) 1 < κ ≤ 4/3; K_f ≥ 3; K_f+1 ≤ K_R | 5/4; 10; 11 ≤ 12 | OK |
| (P0) η1 ≤ K_f/(K_f+1); K_ε ≥ 2; s0 ≤ f_F < 1 | 0.5 ≤ 0.909; 10; 1/8 ≤ 1/2 | OK |
| (P1) 1/(1−v0) ≤ d_L, e^{2μ} ≤ δ1 | small v0 | OK |
| **(P2) c_ρ* K_f ≥ 2** | **c_ρ* = 1/10, c_ρ* K_f = 1** | **FAILS (E1)** |
| (P2) c_R* K_ε ≥ 1; c6 ≤ K_R K_ε; c_η > 0 | 58; 6 ≤ 120; 0.1 | OK |
| (P3)–(P5), (P7) | O(v) margins; A0 s0 = 1/4 < 1/2 | OK for small v0 |
| (P6) θ̄ < 1 | 5/8 | OK |
| (P8) m² r* < 4c_A | 0.04 < 2 | OK |
| c6 = (1+δ1)/c_A | 6 | OK |
| K1 = c_ρ* K_f/κ | 4/5 | Harmless. Only α_D*(K1) = 1.71 and |p_a| ≤ ρ̲(1+1/K) use it; no step needs K1 large. |
| Dropping κ/K_f from c_ρ | – | Justified. The v2 far inequality uses ρ̲ = min over the arc, and toolkit(c) bounds every ρ_s with w_s ≥ g (our CHANGES_v2: the old c_ρ was deleted). |
| (S2) factor min(1, K_fλ/min(a, K_R R))^ν | present | OK; absorbs (g(t∘)/ĝ)^ν exactly as ours |
| (S2) from (T1) | C R^{a′} ≤ ½ s0 m (K_f/K_R)^ν | OK (our Lemma 8.1) |
| a′ ≥ 7/8 > γ_D > γ+ν+η_N | 0.875 > 0.75 > 0.708+O(v) | OK; margin 1/24 |
| κ = 5/4 margin | (1+δ_t)(1+O_R(v)) < 5/4; 3κ/2−1 < 1 | OK |
| ω0 ≤ 1/4 (D2) | 0.197 + O(R) + O_R(v) | True, but only via m (E3) |
| C_T(γ), C_T(γ_D); C_μ | 6.10, 5.57; 47.6, 39.8 | finite, ε-free |

**E1 in detail.**
- Lemma toolkit(c) gives ρ_s ≥ c_A·min(w_s, K_R R) − δ1ε.
- A far pair has g ≥ K_fλ ≥ 5ε. At g = 5ε this gives only ρ̲ ≥ 2.5ε − 2ε = **ε/2**. You need g ≥ c6·ε = 6ε to get ρ̲ ≥ ε.
- So the sentence "In both regimes ρ̲ ≥ ε, so Lemma Duhamel applies" is false as derived. Lemma Eprime(iv) needs A = Π/ρ on the whole arc.
- The affected pairs have λ ∈ [ε/2, 0.6ε) and g ∈ [K_fλ, 6ε).
- **Repair.** Take δ1 = 5/4. This is admissible: e^{2μ} ≤ 5/4 for v ≤ 0.1. Then c_ρ* = 1/4, c_ρ* K_f = 5/2, c6 = 4.5 and c_η = 1/4. Alternatively take K_f = 20 and K_R = 21. Nothing else changes qualitatively.

## 3. Near-pair proposition (replacement for the certified D′)

I re-derived every display. **It is correct and complete.**

- **Envelope.** D(s) ≥ λ·max(θ, (x+σ)/c6) ≥ λ(x+σ+θ)/(2c6). This needs w_s ≤ (K_f+1)λ ≤ K_R R. Also a* ≤ 2/D.
- **Budgets.** Ω ≤ C_μ m_λ² λ(σ+θ) and G ≤ (κC_μ)^{1/2} m_λ λ(σ+θ), from (E-μ) with λ_σ ≤ σ+θ.
- **Term I.** ≤ 4c6C_μ v m_λ² H1(x), with H1(x) = 1 + log(1 + 1/(x+θ)). The atom is included.
- **Term II, long-type (g+λ > R).** Then r_λ < K_f + 1, so 1 ≤ (K_f+1)^γ m_λ/m. Using |q| ≤ 1/D gives C·v·m_λ²·H1/m. Valid; C_* depends on m only.
- **Term II, short-type.**
  - II_a ≤ 4c6²κC_μ v m_λ² H1: here θ²/(x+θ)² ≤ 1 and (σ+θ)/(x+σ+θ)² ≤ 1/(x+σ+θ).
  - II_b ≤ 8c6²(κC_μ)^{1/2} v m_λ |p_a|/(λ(x+θ)).
  - Case g > 0: I′ = (a′, b) is a family pair with Λ ≤ g+λ ≤ R (the text writes "(1+K_f)λ ≤ R", which is a typo; short-type is what gives it). Also l(a′, a) ≤ κλ(x+θ), with the g′ < ε/2 case handled through (a′, a′+ε/2). So Y ≲ m_λ λ(x+θ)^{1/2} and H2 = (x+θ)^{−1/2}.
  - Case g = 0: always short-type. If β⁺ ≤ b, then Y ≤ κ^{1/2} m_λ λ. If β⁺ > b, then θ > 1 and the tilt in I0 = (β, β⁺) gives Y ≤ 2^{1+γ}κC_T m_λ λ. In both cases II_b ≲ v m_λ²/θ.
  - Tail pairs are near only after t_W, which is covered. A final, unwalked leg has P = x_β, so p_a = 0.
- **Sum over legs.**
  - The g = 0 leg contributes d_L θλ(H1(0) + 1/θ) = O(λ), since θ log(1+1/θ) ≤ 1 and θ ≤ 2.
  - The positive-gap legs, spaced by at least θ/κ, contribute at most θH(θ/κ) + κ∫_0^{K_f} H, with θH1(θ/κ) ≤ 3, θH2 ≤ √2, ∫H1 ≤ K_f + ∫_0^{K_f} log(1 + 1/x) dx < ∞ and ∫H2 ≤ 2√(K_f+2).
- **C_\*.** It is an explicit finite polynomial in c6, C_μ(m), κ, K_f, d_L and 1/m, independent of ε, λ, R and v. The text never writes it out, but doing so is mechanical. The cut leg, tail pairs, the g = 0 leg, β⁺ > b and long pairs are all covered. **(a)**
- Start value E(t_n) ≤ ½f_F²m_λ²λ follows from Prop. far, (S2) or (TW), and θ̄ = 5/8 then requires v0 < 3/(16C_\*).

## 4. Touch-down theorem: ε-uniformity audit

**Run 1 and the Run-2 data at t1 do not depend on ε at all.** These are frr, frb, frA, fra, frc, Λ, C, ∂log C and S(t1), and they depend smoothly on (θ, v) on I_η, where ρ ≥ sin θ > 0.8 in Run 1.

ε enters only through the following, and the text tracks each correctly:
- t_td − t_a = ε(1 + O(v)) and ω(t_td) = O(vε);
- the virtual window ξ < ξ1ε;
- ξ_e ≍ ε^{1/(2−2v)};
- the seen ranges [C0vε, ξ_e] and (0, ε/2].

The exponents ξ^{2−2v}, ξ^{−μ}, ξ^{1−μ_T} and ξ^{−μ_T} come with uniform constants: powers c^{μ}, c^{1−v} → O(1).

So the hidden constants are ε-free. What the text omits is the proof that they are finite and have the right signs. Each claim below is true (our proof covers it) but is not derived here:

- **Window data** (our Lemma 7.4(c,d), about 2 pp.): bounds on frA and Λ; the tail-side sign ∂_θ log C < 0 on [α0 − η, α0), which gives uniqueness of b_e; |S(t1)| ≲ v; and |τ_b^v ∂C| ≲ ξ.
- **Forward arc** (our Lemma 7.5, about 1 p.): D_ψ > 0, fra ≥ fra_min > 0, and "τ ≪ 1 ⇒ cos β > v". With η fixed at 0.1 these are numerical facts at v = 0, not consequences of smallness.
- **Virtual labels** (our Lemma 7.6): the Grönwall additive term vy/ε ≲ ξ1·v·ξ^{1−μ} uses ξ < ξ1ε, which is unstated. ψ(α0, t_td) = 0 comes by a limit.
- **Tail** (our Lemma 7.7, about 2 pp.): τ > 1 and the refined τ^{1+v} ≍ |h|/C; frA_max < 2 for the (0, ε/2] range.
- **Arm, hole and bulk** (our Lemmas 7.3(c) and 7.8, about 3 pp.), and **regularity and length** (our Lemma 7.10).
- "U = 2π + O(v)" is unproved but not load-bearing; only 1 ≤ U ≤ 8 is used.
- **(T1)**: the three-case analysis is reproduced correctly.
- **(T2)**: the endpoint Z_s (a limit) needs our Lemma 7.8(c) case split. **(a)**

In total about 12 pages of ours become 1.5 pages. A strong reader could reconstruct them, but it is real work.

## 5. Corollary and quantifier order

- The compactness corollary is correct: D_N dyadic, ε_N = 2^{−N}ε*, and T̄ = T0 is independent of N.
- Order of choices:
  - m is fixed first; C_T, C_μ and C_\* depend only on m.
  - R depends on m and the absolute touch-down constants. Its conditions are R ≤ λ0, U_A ≤ G_T, c_sep ≥ 6R and C R^{7/8} ≤ ½s0 m(K_f/K_R)^ν. The last uses a′ ≥ 7/8, which needs only the absolute cap v ≤ v_T, μ_T ≤ 1/8.
  - v0 depends on (m, R) through C_H(R), δ_t = O_R(v), O_{m,R}(v), C_\*(m), c_amp and η_N < 1/24.
  - ε* depends on (R, v0): ε* ≤ R/10, ε* ≤ ε_T, and z0 ≥ 2ε through ε^{1/(2−2v)} ≥ ε^{1/(2−2v0)}.
- No constant chosen earlier depends on a later one. **No circularity.**

## 6. Answers to the specific questions

| Question | Answer |
|---|---|
| Is every lemma proved? | No. See the (b) items: touch-down (≈ our pp. 30–42), heading/departure (≈ our pp. 22–27), locality (our Lemma 3.9), dyadic chain (our Lemma 3.8), start-chord lemma (our Lemma 8.1). |
| Doubtful or false items? | Only E1 (false as derived; repair: δ1 = 5/4) and the E2 notational slip. E3 is true but unjustified as worded. |
| Is the near pair a valid replacement? | Yes: complete case analysis, finite ε-independent integrals, explicit C_\*(m). |
| Corollary and logic | Correct; no circularity. |
| Overall | **(C)**: correct outline with substantial omitted arguments, plus one parameter error that is easy to fix. |
| Stand-alone valid proof? | No. It is a sound, honest roadmap, but it relies on our §§5–7 for the touch-down and departure estimates. After E1 and E2 are fixed, it could become a complete qualitative proof by expanding §§5–6 to about 10–12 pages. Computer assistance would still be unnecessary, because the near-pair bound and all touch-down facts are hand-checkable when v0 is not explicit. |
