# Referee report SA — short paper, §1 (statements), §2, §3, §4 (end theorem)

Referee: independent, adversarial. Files read: `short/sec1.tex`, `sec2.tex`, `sec3.tex`, `sec4.tex`, `preamble.tex`,
`verify_constants.py` (function `core`, lines 349–443), then for comparison `paper/sec_T3.tex` 90–249, `paper/sec_Estar.tex`
76–135, `short/notes_W1.md`, `short/notes_W2.md`. The script was re-run (`ALL 207 CONDITIONS HOLD`; the regenerated
`appA_tables.tex` and `verify_constants.out` have the same byte length as before).

**Overall verdict.** Every proof in §2–§4 was checked line by line, standalone. I found **no FALSE statement and no GAP that
breaks the logic**. The end theorem (Thm 3.4) follows from §2–§4 as written, uniformly in ε, with no circularity. All numerical
conditions used in §§2–4 are either (P0)–(P7)/(PT) (all checked by the script, with formulas identical to Def 3.3) or are proved
inline. The fixes below are a sign error, two misstatements of strictness or scope, and a symbol (δ_t) that is used before it is
defined.

---

## 1. Verdicts per statement

### §1 (statements only)
| item | verdict |
|---|---|
| Problem set-up, candidate = maximal solution, caught/seen | OK |
| Thm 1.1 | OK as a statement. It is consistent with §3: seen at radius ε' ≤ ε implies seen at radius ε, and ε' ≤ ε_* matches the §§2–8 convention |
| Cor 1.2 | OK. Follows from Thm 1.1 + Lemma 2.11 with T = 10.13d and ε_N → 0. Minor: Lemma 2.11 gives H only on [0,T]; say "extended as a constant after T" |
| Rem 1.3 | OK. The script runs with `mp.dps = 50` |
| Outline paragraphs | OK. Consistent with §§2–4 |

### §2
| item | verdict |
|---|---|
| Lemma 2.2 (field) | OK. Checked: f ≤ 1, C¹ matching at ε, f/ρ − f′ = ρ/max(ρ,ε)², (iii), (iv) |
| Def 2.3, Lemma 2.4 (flow) | OK. The ψ_t formula and sign were verified |
| Lemma 2.5 (seen) | OK. It uses ρ_θ(0) = 1 > ε, which the §2 convention ε < 1 provides |
| Lemma 2.6 (separation) | OK. The mixed-field case was checked (whichever of p_a, p_b has modulus ≥ ε makes both values come from one monotone field). The boundary case c₀ = 2ε is handled correctly by perturbation |
| Def 2.7, Lemma 2.8 (static) | OK. (c): (2/K) sin(Kl/2) ≥ l − K²l³/24 gives N ≤ K l^{3/2}/√12. (d) needs c(a′,b′) > 0 and c(a,b) > 0, which every application has through (CA) |
| Lemma 2.9 (excess identities) | **OK with fix (sign)**. All identities and both far inequalities re-derived. The constants 1 + l/ρ_m + 2l²/ρ_m² and 2vl^{3/2}\|p_a\|N/ρ_m³ are exact. Sign slip: in this notation e^⊥·r_a = e×r_a = −(r_a×e). The proof says "r_a·e^⊥ = r_a×e = p_a" (line 188) and "\|r(s)·e^⊥\| = \|p_a+δ(s)\|" (line 194). Only \|p_a\| enters, so the bounds are unaffected. Replacement for line 188: "(note \|r_a·e^⊥\| = \|r_a×e\| = \|p_a\|)". Replacement for line 194: "\|e×r(s)\| = \|r(s)·e^⊥\| = \|δ(s) − p_a\| ≤ \|p_a\| + l^{1/2}N" |
| Lemma 2.10 (Duhamel) | OK. c > 0 propagates by Lemma 2.6(c), N_η is C¹, and α, β are continuous |
| Lemma 2.11 (compactness) | OK. Checked: the inequality \|y/\|y\| − z/\|z\|\| ≤ 2\|y−z\|/max, the Grönwall constant 8v/c, closedness and openness of I, the subsequence argument, and the openness of the uncaught set |

**Hypotheses added by the writers (c > 0, regular start curves).** Every application in §§3–4 meets them:
- Lemmas 2.8(d), 2.9 and 2.10 are applied only to pairs with ε/2 ≤ λ ≤ R. Such pairs are good, so (CA) gives c ≥ c_Aλ > 0.
- The pairs J₀, I₀, (a′,a), (a′,b), (a_{j+1},b) and (a,a+λ_s) all have λ ≥ ε/2 and λ ≤ R.
- The working front has \|∂_u x⁰\| ≡ 1.
- Lemma 2.9(v) needs ρ_m ≥ ε. Prop 4.2 proves it from (P2) at every τ.

### §3
| item | verdict |
|---|---|
| Def 3.1, Lemma 3.2 (chase) | OK. Checked: (1) the ρ and σ ODEs; (3) the factor e^{2μ}; (0) finiteness of legs before any T |
| Def 3.3 (parameters), (P0)–(P7) | OK. Each derived constant was compared with `core()`: all 30+ formulas agree, including T_I, T_α, T_β, k₀, D_IIs, D_IIl, B₅, I₅, X_far, L_J, θ̄ |
| Setting (H) | **OK with fix (δ_t used before it is defined)**. δ_t appears in (TW), (PT), (Imp) and Prop 4.4. It is not in the parameter tuple and is defined only in §5 (sec5.tex l.143). Replacement in (H), after "an excuse length W_e ≥ 0": "and a number δ_t ≥ 0 (in the application, δ_t = e^{v₀K_w} − 1 of §5)". Also add "(S1) and (S2) are hypotheses at time t_td" (the text implies this but never says it) |
| Thm 3.4 (end theorem) | **OK** (proof complete; see §2 of this report). Fix in (c): "at every t ≤ T_stop" should read "at every t ∈ [t_td, T_stop]" |
| Proof of (CA) | OK |
| Lemma 3.5 (legs) | OK. The induction in (ii) is correct. The pair (a_{j−1},U) is admissible because a_j > U − ε/2 > W_e, hence t_j ≥ t_W. 3κ/2 − 1 ≤ 1 uses κ ≤ 4/3 |
| Lemma 3.6 (gap–time integrals) | OK. Bases of non-final legs are spaced by at least ε/κ, and the disjoint-interval comparison is correct in both directions |
| Lemma 3.7 (distance) | OK. Uses c_A − 1/c₆ = c_Aδ₁/(1+δ₁). The second claim for w < ε/2 holds because y < ε/2 < c₆ε |
| Lemma 3.8 (tilts) | OK. One step, chains (A), (B), (C), and the constants C_A, C_B, C_TL = 2C_A + c_t(3) were all checked. The max(b, a_{j+1}) in the hypothesis is exactly what Prop 4.3(i) needs for I₀ = (β,β⁺). Only γ > 0 is used here (σ_q < ∞). The γ > 1/2 hypothesis enters §§3–4 only in Prop 4.4 (monotonicity of y^{2γ−1} in Lemma 3.6(ii)) |
| Lemma 3.9 (locality), incl. the "3.8(ii)" outline issue | **OK**. The writer's correction holds. For a tail pair at t′ = t_W the base a_{j(t_W)} = a_{j_W−1} < W_e would make (a_{j_W−1}, s) a bad pair. The fix (i), (ii) for t′ > t_W plus "use leg j_W+1, base a_{j_W} ≥ W_e" at t_W is legitimate for three reasons: P(t_W) = x_{a_{j_W}}(t_W); F_*(t_W) = F(t_W) contains the family of leg j_W+1; and (iv) gives a > a_{j_W}. Lemma 3.7 accepts t = t_j as a point of leg j+1. (iv) uses a_{j_W} ≤ a_{j_W−1} + ε < W_e + ε ≤ U − W_e − R |
| Locality principle (paragraph) | **OK with fix (wording)**. "and, of the pair itself, only its start data" is inaccurate. Props 4.2 and 4.4 use (J1) and (J2) of the pair itself at every τ ∈ [t_∘,t]. This is harmless, because the pair itself is one of the pairs of Lemma 3.9(i). Replacement: "...and, beyond the bounds of the pairs of Lemma 3.9(i) (which include (a,b) itself), only the start data of (a,b) at t_∘." |
| Lemma 3.10 (continuity scheme) | **OK with fix (strictness)**. Line 323 chooses δ with "≤ ½(1−θ̄)M²(ε/2)^{2γ}", but line 326 concludes "E(t) < ½M²λ^{1+2γ}"; with ≤ only ≤ follows. (J2) is non-strict, so ≤ suffices and the argument stands. Fix: replace "<½M²λ^{1+2γ}" on line 326 by "≤½M²λ^{1+2γ}" (or choose δ with strict inequality). The rest is correct: the bounds at τ* by left continuity; the tail pairs entering at τ* = t_W through (TW), (PT) and L_J ≥ 1; F_*(t) ⊂ F_*(τ*) on an interval free of leg starts; termination by Lemma 3.5(iv) + Lemma 3.2(0); t_W reached because a_J ≥ U − ε > W_e |

### §4
| item | verdict |
|---|---|
| Standing assumptions; t_∘, β, β⁺ | OK. For a tail pair at t_W, membership in the family of leg j_W+1 uses g_W ≥ K_fλ > ε ≥ a_{j_W+1} − a_{j_W}; checked |
| Lemma 4.1 (two integrals) | OK. Closed forms, z h₁ ≤ λ, ∫₀^{Kλ} h₁ = λ(2 + log K), G₃ all verified |
| Prop 4.2 (far) | OK. Checked: ρ_m ≥ c_ρg and ≥ c_RR, ≥ ε by (P2), ρ_m ≥ K_i l; amplification ≤ A₀(min(g(τ),K_RR)/ĝ)^ν by (P3), (P4); forcing in both regimes, with B_{2U}, B_{2η}, B₃ and C_p re-derived (r_f = 1 + 1/(K_f−2), λ(a′,b) ≤ R from η₁ ≤ K_f/(K_f+1)); the three Duhamel terms reproduce (P5) exactly (γ + ν < 1 is used in terms 2 and 3). Tail restart: N(t_∘) comes from (TW) with g(t_∘) = g_W, and the weight min(g_∘, K_RR, K_fλ)/ĝ is ≤ 1. Correct. Notation: "K_i" in "ρ_m(1+1/K_i)" is undefined; write "K_1 resp. K_2" |
| Prop 4.3 (near) | OK. Checked: start value (S2), Prop 4.2 at t_n, or (TW); Term I with ω(y), λ_y and the two regimes of y; the first piece needs c₆ε ≤ K_RR, which follows from (P2) and ε ≤ R/K_ε; T_I. Term II short case: offset k₀ for g = 0; for g > 0 the three sub-cases, including the J₀ case with ½κ^{1/2}(1+κC_TL²)^{1/2} ≤ C_TL (valid since κ ≤ 4/3 and C_TL ≥ c_t(3) ≥ √3); split, Fubini, H(x), T_α, T_β, D_IIs. Long case: D_IIl, using K_f + 1 ≤ K_R. Conclusion gives θ̄ |
| Prop 4.4 (length) | OK. Far, g > η₁R: X_far. Far, g ≤ η₁R: B₅; Lemma 3.6(ii) with γ > 1/2; only the first summand of I₅ is needed. Near: κT_Iλ. The additive and multiplicative combination gives (1+δ)L_J |
| §4.4 completion of Thm 3.4 | OK. (b) by Lemma 3.5 at t′ = T_stop and Lemma 3.2(2); (c) by Lemma 3.9(i) and Lemma 3.8; (d) is Lemma 3.7; (e) by Lemma 3.2(4) |

---

## 2. Global checks requested

- **First-failure closing argument and non-circularity.** Lemma 3.10 takes τ* as a supremum. §4 proves (Imp) on [t_td, t*] using only (J1), (J2) on [t_td, t*], plus (S1), (S2), (TW) and constants. (Imp) is strictly better than (J1), (J2) by (P6), (P7) and (PT), so the extension step goes through. The proviso is never assumed: T_def is the time up to which the chase is defined, and Lemma 3.5(iii) shows the proviso cannot fail at τ*. (TW) is a conditional hypothesis about the configuration at t_W, and nothing in §§3–4 uses it to reach t_W. This matches the record's structure (sec_T3, "No circularity"). Whether (TW) is verified in §8 without Thm 3.4 is outside my scope.
- **Uniformity in ε.** ε enters §§3–4 only through ε ≤ R/K_ε and ε/2 ≤ λ. Every constant in Def 3.3 is free of ε, v and U (v and U appear only through v₀ and U₀ in X_far, (P3)–(P7)). The δ of Lemma 3.10 depends on ε, but it is only a continuity device. Uniform: OK.
- **Script coverage.** `core()` checks every item of (P0)–(P7) (including γ > 1/2, γ + ν < 1, f_F < 1, κ ≤ 4/3, K_f ≥ 3, K_f + 1 ≤ K_R, K_ε ≥ 3/2, η₁ ≤ K_f/(K_f+1), q_c > 1, d_L, δ₁, A₀ ≥ 1) for both tuples. (PT) is checked as "(A5) (PT)", and ε_* ≤ R/K_ε as "(A6)". **Conditions used in §§2–4 that are not in the script, all proved inline or trivial:**
  - c₆ ≥ 2 and K_R ≥ 4, from (P0);
  - c_ρ > 0 and c_R > 0, from (P2);
  - δ₁ ≥ 1 > c_A/2;
  - κε/2 ≤ ε and (3/2)κ − 1 ≤ 1, from κ ≤ 4/3;
  - κ ≤ C_TL²(4 − κ²) and c_t(3) ≥ √3, proved inline in Prop 4.3 and correct;
  - η₁ ≤ K_R and the monotonicity of a_D, trivial;
  - L_J ≥ 1, trivial.

  **No condition used in §§2–4 is missing from the script.** The (H) conditions U ≤ U₀ and U ≥ 2W_e + R + ε are §8 matters (outside scope).
- **Record comparison** (sec_T3 Thm T3-E, sec_Estar Def/Steps). The single-proof form with t_∘ ∈ {t_td, t_W} and β(t_W) := a_{j_W} reproduces Part 1, Part 2, (F1)–(F4) and Table T3-reuse. No needed step was lost:
  - the start value of near pairs at a far→near switch is present;
  - the tail-pair restart as far pairs from (TW) is present;
  - the length start (1+δ_t)λ is present;
  - case (β) of Step 1(a) (pair (a_{j−1},U), shown admissible because t_j ≥ t_W) is present;
  - the record's (Pc) and conclusion (c) were not carried over and are not needed.

  The simplifications (Ψ_I, D_IIl without the ι-term, I₅) are valid under K_f + 1 ≤ K_R and γ > 1/2, and the script confirms their equality to 1e-45.

---

## 3. Exposition problems (brief)

1. δ_t is used in §3 before it is defined in §5 (fix above).
2. T_n (Def 3.3) is defined but never used in any proof. Drop it from Def 3.3 and Table A.1.
3. The second summand of I₅ is not needed (Prop 4.4 uses only the first). Either drop it or add one sentence saying it is slack.
4. Thm 3.4(c) gives no lower limit for the time range; Prop 4.2 writes "K_i" without defining it; Lemma 2.11 uses T for a time, while T is also the unit tangent.
5. The lead-in sentence of Lemma 3.6 states the spacing ε/κ as a fact. It should cite Lemma 3.5(i), (ii) explicitly (the proof does).
6. Leg-start conventions:
   - j(t_j) = j−1, while "t_j belongs to legs j and j+1".
   - The tail-pair convention β(t_W) = a_{j_W} is used in Lemmas 3.7 and 3.9.

   Both are correct but easy to misread. One sentence after the definition of j(t) would help: "statements 'in leg j+1' may be applied at t_j with base a_j or at t_j with base a_{j−1}; both are valid since P(t_j) = x_{a_j}(t_j)".
7. Prop 4.3, Term I: the step "ρ_s < y ⇒ w_s < (y+δ₁ε)/c_A" uses min(w_s, K_RR) < (y+δ₁ε)/c_A ≤ K_RR. Write this out.
8. §2's opening "External input" quotes Hartman as plain text. A bibliography entry is needed.
