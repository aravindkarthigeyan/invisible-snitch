# Referee report RQ2-1 on referee/Q2-claims.md (version 1)

Referee: independent, adversarial. Read in full: referee/Q2-claims.md; paper/sec_E.tex (thm:End statement and full proof,
lines 140-469; cor:End; Remark E-B(4); Remark E-restart); paper/sec_B.tex (Lemmas B-V, B-VC, B-1, B-2, B-3, B-4, B-C);
paper/sec_T2.tex (working fronts, lem:T2-W, hyp:HT, eq:T2-const, prop:T2-cond, thm:Main, cor:Exact); paper/sec_T1.tex
(thm:HT including "sharper forms actually proved", and the parts of its proof that give (T3)-(T5) in sharp form).
NOT read: reports/Q2-1.md and code/Q2 (as instructed). Own script: `code/referee/Q2_1/constants.py`
(mpmath, 50 digits).

Scope: everything was checked for **core = old** (thm:End/cor:End, refereed). Claims for core = End\* depend on Q1's
unrefereed Theorem End\* and on (F1)-(F4) being re-confirmed for End\*; I did not assess those. The Q3 touch-down data
(§4.1, second paragraph) are provisional by the authors' own statement and were not assessed.

## Summary of verdicts

| item | verdict |
|---|---|
| §1.2 (F1) locality | OK |
| §1.2 (F2) far pairs with later start | OK |
| §1.2 (F3) length with later start | OK |
| §1.2 (F4) Step 1(a) | OK |
| Thm Q2.E′ Step 0 / goodness | OK |
| Thm Q2.E′ Part 1 (body family closed) | OK |
| Thm Q2.E′ Part 2 (tail pairs enter as far pairs at t_w) | OK |
| Thm Q2.E′ no circularity | OK |
| Lemma Q2.H (heading) | OK with fix (F-H) |
| Theorem Q2.D (departure) | OK |
| Q2.M §4.1 conversion of touch-down data | OK |
| Q2.M §4.4 steps 1-7 | OK with fixes (F-D), (F-A) |
| constants v0 = 4.7e-15 / 9.7e-13, side conditions | OK (recomputed independently) |
| sanity 4.14e-51 | OK (reproduced) |
| every direction seen / fixed in advance / speed / time / Cor Q2.X | OK |
| core = End\* | conditional, not assessed |

No FALSE statement and no GAP found for core = old.

## 1. Theorem Q2.E′ against the proof of thm:End

I went through Steps 1-5 and the closing argument of thm:End (sec_E 167-440) and listed, for each step, every pair whose
family bounds are used, every pair whose (E-CA) is used, and every label at which (E-star) is used.

* **Closing argument (lines 175-180).** Uses only |E′| ≤ (4v/ε)l, l′ ≤ (2v/ε)l per pair, F(t) ⊂ F(t\*), and Lemma B-C(0).
  Holds verbatim for the shrinking body family F_b(t) (Part 1) and for the full family on [t_w, T_end] (Part 2).
* **Step 1(a).** (α) uses (J1) at t_j for (a_j, s), u_s = u_{a_j}+ε/2; (β) uses (J1) at t_j for (a_{j-1}, E). In Part 1,
  (a_j,s) has u′_s ≥ U − W₁ − ε/2 ≥ W₁ (body), (β) cannot occur (u_{a_j} < W₁ < U − ε/2), and the leg is not final
  (final would need U − u_{a_j} ≤ ε). Correct. (b) leg count, T_B = 4U+2: fine for the whole run since every leg advances
  ≥ ε/2 in both parts. (c) eq:E-1c needs only the leg spacing: fine. (d) eq:E-star at s uses (E-CA) for (a_j, s) only:
  this is exactly Step 0 / (e′).
* **Step 2 (tilt lemma).** Sub-arcs (A) (a′, b_k) with b_k ≤ b, (B) (a′_k, b), (C) (a_{j+1}, b) ⊂ (a_j, b); (E-CA) for J₁
  (length ≤ R, hence good). All inside [a_j, b]: body if b is body. Correct.
* **Step 3 (far).** ρ_m bound uses (E-star) at a only (hull ⊂ B(x_a, l)); forcing for g ≤ R/2 uses (a′,a), (a,b), (a′,b),
  a′ ∈ {a_j, a_{j+1}}: right ends a or b. The start time enters only through N(t_s), g_s and the left end of the integrals;
  A₀ uses T_B, which bounds any sub-interval. (F2) is exact: with N(t_w) ≤ s₀Mλ^{1/2+γ}min(1,64λ/min(g_w,32R))^ν the
  "First term" computation gives ≤ (M/4)λ^{1/2+γ} in both sub-cases g₂ ≤ 32R and g₂ > 32R.
* **Step 4 (near).** Start value: Step 3 at the time the pair becomes near, or (S2) at t_s; sub-arcs J_y ⊂ (a,b),
  J₀ ⊂ (a′,b) with a′ = a_{j+1}, and I = (a_j, a_{j+1}) when a_{j+1} > b (body in Part 1 because u′_{a_{j+1}} ≥ U−W₁−ε ≥ W₁);
  (E-star) at s ∈ [a,b] (Term I, Term II, w_s > 32R). Near time ≤ 264λ uses only eq:E-1c. Correct.
* **Step 5 (length).** l(t) ≤ l(t′)·exp(far growth) + near increase, the near increase 3618vλ being absolute (computed
  from (J1) of J_y). With l(t_w) ≤ (1+δ_T)λ: l ≤ (1+δ_T)·1.00001λ ≤ 1.01λ under (PT). Correct.

Hence (F1)-(F4) are true statements about the refereed proof. Part 1: for (a,b) ∈ F_b(t) every pair used is a body pair,
every (E-star) label s has u′_s ≥ W₁ (so (a_j,s) is good and (CA′) applies), start data are (S2′) and l = λ. Part 2: body
pairs inherit their [t_s, t_w] history from Part 1; tail pairs are far at t_w (g_w ≥ K_fλ, and gaps are non-increasing),
enter Step 3 with start t_w and the exact far-pair start bound of (TW), become near at most once and then use Step 4 with
the Step 3 start value; (E-star) at all labels for t > t_w because u_{a_j} ≥ W₁. Strict bounds at t_w (body: (Imp);
tail: s₀ < 1 and 1+δ_T < 9/8) start the continuity argument. No pair is restarted in mid near-phase: a tail pair is far on
[t_w, t_n) and never far again; a body pair is never restarted. Every family pair is good (λ ≤ R < U − 2W₁), and bad pairs
are used nowhere (the only use of (E-CA) for long pairs is (a_j, s) in Step 1(d), which is good in both parts).
Every tail pair of F(t), t ≥ t_w, is in F(t_w) (families shrink) and is covered by (TW).

No circularity: Part 1 does not use (TW); (TW) is derived from Q2.H + Q2.D, which use stage A (a separate application of
thm:End via cor:End on [0, U_A]) and touch-down data, never Q2.E′.

## 2. Lemma Q2.H

Checked line by line. Lemma B-C(2) gives P = x_{a_{i+1}} − ρ′û_{i+1} with û_{i+1} = e_{(a_i,a_{i+1})}(t) (collinearity
in that order). Close case: K₁..K₄, I are stage-A family pairs at t (first point a_i or ≥ a_{i+1}, lengths in
[ε/κ_adv, R₁]); the two tilt chains give ≤ (C_A+C_B)κ_W ≤ C₃κ_W; |e_I × r̂| ≤ x/(1−x²/2); c_I ≥ c_{A1}λ_I. Far case:
(E-star) relative to base a_i, F = r̂, |e_I′| ≤ v/ρ\*. Durations, the close-case count and K_rot, the three-term sum, the
Hölder form for Λ ≤ δ₀, and the time lower bound (closing speed ≤ 1, c ≥ (1 − m₁²/2)λ from (J2)) are correct.

**(F-H) fix.** The proof uses λ_I = min(Λ, δ₀) ∈ [ε, δ₀], i.e. δ₀ ≥ ε. Add "ε ≤ δ₀" to the hypotheses of Lemma Q2.H and
to the side conditions "H" of §4.2 (it holds with a huge margin: δ₀ = R/2, ε ≤ ε\* ≈ 1e-17 resp. 5e-13).

## 3. Theorem Q2.D

Checked every inequality. (i) z′ ≥ −v + (1−h²)^{1/2} ≥ ζ needs no bootstrap; z_s(0) ≥ z₀ + (1−ω̄²/2)u_s.
(ii) Gronwall with (X(τ)/X(τ′))^η and h non-decreasing. (iii) ∂_t𝔭 = v[(T−û)·AT − (T·AT)𝔭] is an identity; both parts of
(∗) integrate as stated (η < γ). (iv) T·AT = sin²φ/ρ, the split at x_c gives ω₀²L_h. (v) Phase 1 via Lemma B-3(b) and
|AT| = sinφ/ρ ≤ Θ_bX^{γ−1}/ζ; phase 2 via Lemma B-3(e) with ρ_m ≥ ζkλ ≥ 4l, |p_a| ≤ ρ_a|û×e| + |y_a|, X_b ≤ (1+1/k)(g̃+τ′),
the ∫(g̃+τ′)^{γ−2} bound (also when τ₀ = 0) and (g̃+τ)/(g̃+τ₀) ≤ 1 + τ/(kλ). All correct; all ingredients hold on a working
front (Lemma T2-W(a)).

## 4. Theorem Q2.M

§4.1: (T3\*), (T4\*), (T5\*), κ_z, c_zlo, c_zhi, c_y match thm:HT "sharper forms" and its proof (forward zone ξ ≤ u;
tail ξ ≤ ξ_e + u′, |T−n̂| ≤ |ψ|; z₀ = −z_E ∈ [0.9939ξ_e, 1.00013ξ_e]; |y₀| ≤ 1.000003ε^{1−v/2}); (T2) has κ₂ = 1/2;
sharper (T1) with C₀ = 5.4λ₀^{1−3v_T−a′} is valid for v ≤ v_T, λ ≤ 1. Conversions to θ₀, θ_y, z₀ ≥ ε/ζ: correct.
Orientation: û = −n̂, û^⊥ = −n̂^⊥, so x_E − P = z₀û + y₀û^⊥ and the tail tangent −T has |−T−û| = |T−n̂|. Correct.

Step 2 (common legs while l(a_j, b_A) > ε), step 3 (heading on [t_td, t_w]), step 5 ((TW): tail pair inside the
departure arc, g_w ≥ U−U_E−W₁−ε ≥ 64R, the ratio computation with exponents a′−γ_D ≥ 0 and 0), step 6 ((S1′) via concavity
and (T2) with u_a + u′_b ≥ W₁ for good pairs; (S2′) as in cor:End), step 7: correct.

**(F-D) fix (applying Q2.D with the actual duration).** (D2) is verified by Q2.H only on [0, t_w − t_td], whereas §4.2 sets
D := (κ_adv W₁ + ε)/(1−v₀) ≥ t_w − t_td. Text: "Apply Theorem Q2.D with D_act := t_w − t_td ≤ D. In Q2.D, X\* is used only as
an upper bound of X_s(τ) on [0, D], so X\* := U_E + z₀^max + D (with the bound D) is admissible; L_h, K_w, δ_t are
non-decreasing in D; keep k := k_fac·4(1+δ_t(D))/ζ, which satisfies k ≥ 4(1+δ_t(D_act))/ζ; c_n, c_β, (TS) are
non-decreasing in δ_t and in τ = D_act ≤ D." (State in Q2.D: "X\* ≥ U_E + z₀ + D".)

**(F-A) fix (stage A).** cor:End / Remark E-restart(1) is stated with R given by its formula; stage A uses γ_D and the main
R, which is smaller. Add: "The proof of cor:End uses R only through R ≤ 1, R ≤ λ₀/32, R ≤ c_sep/16, C₀R^{a′} ≤ γ/400, so
it holds for every smaller R with v ≤ min(2e-11γ², (a′−γ)/22, 1e-6γR/(4U_max+2))." (Stage A's (E2) is vacuous: U_A < λ₀.)

## 5. Constants (independent recomputation, `code/referee/Q2_1/constants.py`)

Choices ω̄ = 1/2, k_fac = 1, δ₀ = R/2, γ with γ_D = 1/4, R maximal with (TS) ≤ γ/400, ε\* = min(ε_T, R/64,
(R/(100c_zhi))²), v₀ = 1e-6γR/(4U_max+2) (fixed point).

* a′ = 1/2, C₀ = 0.86: R = 5.2816e-7, **v₀ = 4.7157e-15**, ε\* = 1.136e-17. At v = 4.7e-15 all 40 side conditions hold
  (also at (1e-20, 1e-30)). Binding: v(4U_max+2) ≤ 1e-6γR and (TS) = γ/400; the O(v) departure term vKR^{γ_D} ≈ 1.6e-14
  is negligible; δ_t = 7.8e-15, ω₀ = 0.2775, θ_h = 12.24, K_w = 1.65, L_h = 6.85.
* a′ = 0.99, C₀ = 5.2045: R = 1.0962e-4, **v₀ = 9.788e-13**; all side conditions hold at v = 9.7e-13.
  (Remark: a′ = 1 − 3v_T, C₀ = 5.4 gives v₀ = 1.033e-12, still below 2e-11γ² = 1.25e-12.)
* Sanity: eq:T2-const with the (H_T) constants gives v₀ = 4.1426e-51, ε\* = 2.1966e-44, R_B = 2.0713e-42,
  W = 1.9113e-11: Table tab:T2-const reproduced.

T₀ = T₂ + 2U_max/(1−v₀) = 16.74 + O(1e-14); state a rounded-up value (e.g. 16.75).

## 6. Final claims

Every direction: (T0) + Q2.E′(b′) with Lemma T2-W(c)(3′). Fixed in advance: design T and Construction C depend only on
(v, min(ε,ε\*)); side conditions are monotone in (v, ε). Speed ≤ 1: design T, unit-speed legs, constant after T_stop.
Time: T_stop ≤ t_td + 2U/(1−v) ≤ T₀. Corollary Q2.X: lem:A41 hypotheses (nested dyadic D_N, ε_N → 0, one T₀) as in
cor:Exact. OK.

**Verdict:** for core = old the new assembly is correct; Theorem Q2.M holds with v₀ = 4.7e-15 (round-6 data) and
v₀ = 9.7e-13 (sharper (T1), a′ = 0.99), after the three textual fixes (F-H), (F-D), (F-A), none of which changes a constant.
Claims for core = End\* and with Q3 data remain conditional on unrefereed inputs.
