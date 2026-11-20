# Referee report RP8b-1 — `referee/P8b-claims.md` (v1): assembly of the main theorem for design T

Independent, adversarial. Read in full: `referee/P8b-claims.md`, `paper/sec_B.tex`, `paper/sec_E.tex`,
`paper/main.tex` (lem:limit, lem:A41). NOT read before the verdict: `reports/P8b-1.md`, `code/P8b/`.
Referee code: `code/referee/P8b_1/constants.py`, `p8d_sim.py`, `out_p8d.txt`.

Problem checked against: Harry speed ≤ 1, H(0) = 0, path fixed in advance (may depend on v, d, ε, not on α);
Snitch S′ = v(S−H)/|S−H|, S(0) = d e^{iα}, v < 1; seen = |S_α(t) − H(t)| ≤ ε at some t; exact capture S_α(t) = H(t).
**No silent change of the problem found** (d = 1 normalisation only; "seen" always refers to the TRUE candidates;
the path depends on (v, ε) only; the limit path of the corollary has speed ≤ 1, not = 1).

## 0. Summary of verdicts

| Claim | Verdict |
|---|---|
| Lemma P8.W (a) | **OK** |
| Lemma P8.W (b) | **OK** |
| Lemma P8.W (c) | **OK with fix F1** (well-definedness of a leg: c(a_j,a_{j+1};t_j) > 0 is not automatic on a working front) |
| Lemma P8.W (d) | **OK** (full check done, §1 below; F1 is automatically satisfied under (ST_γ)) |
| Lemma P8.A | **OK** |
| Theorem P8.D (i)–(v) | **OK** (every constant recomputed; simulation consistent) |
| Lemma P8.H | **OK** |
| Hypothesis (H_T) as a statement | precise and used verbatim; **two text fixes F2, F3** (F2 is needed: as written, (T0) is false at u = 0 for the intended realisation) |
| Proposition P8.I (a), (b) | **OK** (all pairs covered, §3 below) |
| Theorem P8.M | **OK, conditional on (H_T)** (and F1, F2); honestly labelled |
| Corollary P8.X | **OK, conditional on (H_T)**; hypotheses of lem:A41 all met |
| Constants v₀, ε_*, T₀, Remark (4) | **OK** — reproduced: v₀ = 1.54·10⁻⁴⁷ (N8 set), 1.61·10⁻⁵¹ (P8a set), T₀ = T₂ + 15.72 (= 19.5 iff T₂ = 3.78); text fixes F5, F6 |

No FALSE statement and no GAP in a proof was found. The main theorem is **not** unconditional: it rests on (H_T),
of which the items (X1), (X2) are not even in P8a's interim statement (the claims file says so).

---------------------------------------------------------------------------------------------------------------------

## 1. Lemma P8.W — the working front (full check)

### 1.1 What a working front is, and the three questions asked

* *Is it a continuous curve in the label?* By definition yes: x⁰ ∈ C¹([0,U]), |∂_u x⁰| ≡ 1, and x(·,t) is the image of
  x⁰ under the flow of the C¹ field vF(· − P(t)) from t_w; so x(·,t) ∈ C¹ with w ≥ 1. The content — that the true front
  through the seen hole, including the limit point at the caught axis label, glued to the virtual candidates
  [α₀, α₀+1.02ε), IS such a C¹ unit-speed curve — sits entirely in (H_T) (existence of x⁰), not in P8b. P8b never
  integrates the true field through its singularity: before t_w nothing is integrated here, and after t_w every label
  (true or ghost) follows the VIRTUAL field, which is C¹ with F(0) = 0.
* *Is the true field singular at distance 0 / candidates re-entering the ε-disc?* Irrelevant after t_w for the reason
  just given. For a true label, (b) is correct: either S_θ was within ε at some time ≤ t_w (seen; nothing to prove —
  this covers true labels with ρ_u(t_w) ≤ ε and labels that had been inside the disc earlier), or ρ_u(t_w) > ε and the
  virtual and true trajectories coincide on [t_w, t*] by uniqueness for the true ODE in {ρ ≥ ε}. Hole labels are ghost
  labels: nothing is claimed about their directions after t_w ((T0) says they were seen before t₂).
* *Is Construction C on it a path fixed in advance?* Yes: x⁰ is a function of (v, ε) (one admissible choice in (H_T);
  in the intended realisation it is determined by P|[0,t₂]), each leg is computed from P and the working front at
  earlier times, nothing depends on α.

### 1.2 Line-by-line check of [B] and of Theorems B / End on a working front

I went through every lemma of `sec_B.tex` and every step of the proofs of Theorem B (Steps 1–5, (Imp), consequence),
Theorem R (Claim, induction) and Theorem End (continuity argument, Steps 1–5, (b), (c)), Corollary End, and
lem:E-facts, asking where the proof uses anything beyond "x(·,t) is the flow image of a C¹ curve under x′ = vF(x−P)".

| Item | What it uses | On a working front |
|---|---|---|
| Lemma V (i)–(iv) | the field only | valid |
| Lemma VC (a) | ODE, ‖DF‖ ≤ 2/ε, A ≥ 0, \|∂x\| = 1 initially | valid with θ → u, time 0 → t_w |
| Lemma VC (b) | Lemma V(iv) | valid (any two solutions) |
| Lemma VC (c) | ρ_θ(0) = 1 > ε and "virtual = true until first entry" | **NOT valid as stated**; correctly replaced by P8.W(b) (true labels only) |
| "c(a,b) > 0 for b − a < 2π" (after VC) | injectivity of θ ↦ e^{iθ} + VC(b) | **NOT available**: x⁰ is not assumed injective → F1 |
| Lemma 1 (i),(ii) | variational equation, w > 0 | valid; (iii),(iv) (C² "since time 0") are not used anywhere |
| Lemma 2 (i)–(iii); (iv) | variational equation; (iv) needs ρ ≥ ε only | valid ((iv) unused) |
| Lemma 3 (a)–(e) | Lemma 2, Lemma V, static hull geometry | valid |
| Lemma 4 (a),(b) | static | valid |
| Lemma C (0) | \|∂x\| ≤ e^{2vT/ε} relative to the initial parametrisation | valid with T − t_w |
| Lemma C (1), (5) | phase 0, Prop. length | not valid, **not used** by P7.B/P7.E/P8b |
| Lemma C (2) | ansatz + uniqueness for the virtual ODE; needs the leg direction u to exist | valid **given c(a_j,a_{j+1};t_j) > 0** (F1) |
| Lemma C (3) | VC(c) | replaced by (3′) |
| Lemma C (4) | l′ ≤ (2v/ε)l, leg duration | valid |
| Theorem R, Claim | (F_b), (S), C(2),(4), 3(d), 4(b) | valid (only used for P7.B(c), which P8b does not use) |
| Theorem B / End, (Imp) closing | l′ ≤ (2v/ε)l, \|E′\| ≤ (4v/ε)l, Lemma C(0) | valid |
| Step 1 (a)–(d) | (J1) resp. (I1), maximality of a_{j+1}, (CA), C(4) | valid |
| Step 2 (TL) | Lemma 4(a), (J1), (J2), (CA) — static | valid |
| Step 3 | hull in B(x_a,l), (∗), Lemma 3(e), C(2), (TL), (1c) | valid |
| Step 4 | Lemma 3(a), V(iii), C(2), (∗), (mu), (1c) | valid |
| Step 5 | Lemma 2(i), 3(c) | valid |
| End (b), (c) | Step 1, Lemma C(3) → (3′), Claim of Thm R | valid with "true labels" |
| Cor. End proof | algebra on (E1), (E2) | valid |
| lem:E-facts (a)–(c) | static; variational equation | valid |
| Theorem End's "ℰb − a_s < 2π", "P(0) = 0" | only for c > 0 and VC(c) | replaced by F1 and (b) |

Monotonicity of distances, the evolution laws inside the ε-disc, the Lipschitz bound 2/ε and non-contraction all
come from the field and hold for every flow line whatever its initial point; none of the proofs uses that the
candidates obeyed the virtual field (or any field) BEFORE the leg start t_s, nor that the labelled curve is the image
of the unit circle. So the author's short argument for (d) gives the right answer; the only two places where the
initial curve enters are exactly VC(c) (handled) and injectivity (F1, not mentioned).

### 1.3 Fix F1 (exact text)

Construction C needs x_{a_{j+1}}(t_j) ≠ P(t_j) = x_{a_j}(t_j) to define a leg. In [B]/[P7] this is "b_E − a_s < 2π".
A working front may self-intersect (in design T, x⁰(U) lies within C_zε^{1/4} of x⁰(0) and (T5) allows z₀ = y₀ = 0;
(T1) does not exclude a tiny loop inside a pair of label length < ε/2). Replace in (c):

> "(c) Construction C from a leg start (t_s,a_s), t_s ≥ t_w, cut at b_E, **is defined as long as
> c(a_j,a_{j+1};t_j) > 0 at every non-final leg start reached; under this proviso** [B, Lemma C(0),(2),(4)] hold
> verbatim, and (3′) …"

and add to (d): "Under (S1) the proviso holds: by Step 1(a) (valid at every leg start t_j ≤ t\*, where (J1) holds by
continuity) a non-final leg has label advance ≥ ε/2, hence c(a_j,a_{j+1};t_j) ≥ ½min(λ,32R) > 0 by (CA)."
With this, the continuity argument is unchanged (if t\* = t_j, leg j+1 is defined). In Proposition P8.I the legs
j+1 ≤ j_I are covered by stage A, the later ones by the application at t_I; so design T_g is well defined.

---------------------------------------------------------------------------------------------------------------------

## 2. Lemma P8.A, Theorem P8.D, Lemma P8.H

**P8.A — OK.** T·AT ≤ 1/ρ₀ on the arc, l′ ≤ (v/ρ₀)l; then ρ_m ≥ ρ₀ ≥ max(ε,4l_t); Lemma 3(e) with
|p_a| ≤ ρ_m + l ≤ 1.25ρ_m. Same proof as lem:E-far with constant ρ₀; pairwise hull is legitimate.

**P8.D — OK.** Re-derived every line:
* (i) z′ = vf z/ρ − P′·û ≥ 0.99875 − v; z_s(t_E) ≥ z₀ + 0.99875u_s; 2/0.49 = 4.0816 ≤ 4.1. ✓.
* (ii) y′ = v(f/ρ)y − û×P′ (sign and û×û^⊥ = 1 checked); (3.3) even holds with 1 in place of 2; the integral
  uses a(τ′) ≥ τ′+ε and 1+γ−η ≥ 1. ✓
* (iii) ∂_tD₁ identity verified algebraically; |q_û| ≤ |y|/(0.49a)² (4.165 ≤ 4.17); second part needs γ > η = 4.1v,
  true by (D3); final Θa_*^γ ≤ 0.050007. ✓
* (iv) 0.0103 + 0.1913 + 1.05 = 1.2516 ≤ 1.26. ✓ (the ρ < ε window is τ′ ≤ 1.041ε).
* (v) 13^{1/4} = 1.8988; 1.08·1.003·1.6^{1/4} = 1.2183; 1.4^{5/4} = 1.5229; 2(1.00002)^{3/2}/0.998³ = 2.0121;
  2.013·(4/3)·5^{−3/4} = 0.8027 ≤ 0.9; ρ_m ≥ 0.998(g̃+τ′) ≥ 4.99λ ≥ max(ε, 4l). ✓ Both cases of N_* correct.
* Simulation (`p8d_sim.py`: virtual field + variational equation, ε = 10⁻⁴, γ = 1/4, ϑ₀ = ϑ_h = 0.09 (D2 used to
  93%), z₀ ∈ {0, 0.7ε, 5ε}, three sign patterns of tilt/heading/y₀): all of (i)–(v) hold; (iii) is saturated at
  t_E (ratio 0.999) as it must be; (ii) used to 59%, (iv) to 20%; (v) ≤ 1.000. In range (v = 2.5·10⁻⁶) this is a weak
  test; at v = 0.02 (out of range, informational) the same inequalities still held. (A first run showed "(v) ratio
  1.6": roundoff in l − c for a straight sub-arc; gone with a cancellation-free N.)

**P8.H — OK.** Steps 1–3 and the time bound re-derived (1.03·2^{1/4} = 1.2249; 8.04·2^{1/4}·10⁻⁴ = 9.6·10⁻⁴;
all pairs K₁..K₄, I, J are family pairs of the leg in question, with first point the base or ≥ the target, label
length in [ε/2, 2Λ] ⊂ [ε/2, R], u_b ≤ U_A; at t_j the convention F1 of [P7] puts J, I in 𝔉(t_j)). Cosmetic: in the
case i ≤ j−2, |e_I − û_{i+1}| ≤ 0.66κ directly (I ⊂ K₄ ⊃ K₃); the lemma uses v ≤ 10⁻⁴, which follows from the
standing v ≤ 2·10⁻¹¹γ₁² and should be said; for j = j_s Step 3 is empty.

**Circularity (P8.D ↔ forward bootstrap): none.** The order of logic is strictly
(T1),(T2) on [0,U/2] → Cor. End (stage A, arc [0,U_A], self-contained: Theorem End for an arc involves only pairs
with u_b ≤ U_A and the legs, which depend only on labels ≤ a_{j+1}; candidates do not interact, so the proximity of
the tail to Harry is irrelevant for it) → (TL), (CA), (J2) on [t₂,t_I] by causality (Remark E-B(4)) → P8.H → (DP) on
[t₂,t_I] → P8.D for the tail. Stage A needs nothing from the E_Y side: its (E2) uses u′_b ≥ U/2 ≥ 1/2 only. The
constants are also non-circular (ϑ_h is defined from R_A, γ_*, ϑ_T; W from ϑ_h).

---------------------------------------------------------------------------------------------------------------------

## 3. Proposition P8.I — (ST_end) at t_I

(ST_end) in P7's exact form (sec_E: (E1) for ALL pairs of 𝖠 = [a_{j_I},b_E] with ε/2 ≤ λ ≤ λ₀, (E2) for ALL pairs
with λ > λ₀, λ = arclength at the leg start, C₀λ₀^{a′} ≤ 1, P(t_s) = x_{a_s}(t_s)) is what is proved, with
(a_I, C_I, Λ_I, c_I) and λ_I = l_{t_I}.

* **(E1_I).** Such a pair has t₂-label length λ ≤ λ_I ≤ W/40, so it cannot join the X₀ side to the E_Y side. The
  trichotomy (D) u′_a ≤ W / (A) u′_a > W, u_b ≤ U_A / (P) u′_a > W, u_b > U_A is exhaustive. (A): family pair of stage
  A at t_I (a ≥ a_{j_I}; 𝔉(t_{j_I}) = family of leg j_I ∋ pairs with a ≥ a_{j_I}) ✓. (P): the distance bound uses (T2)
  for the long pair (a_j, s) — base next to X₀, s possibly close to E_Y — giving ρ_s ≥ min(c_sep, u′_s/2) − 2ε;
  0.25 − 0.0225 − 1/39 = 0.2019 ≥ 1/5 ✓; 2.5·2.1·25 = 131.25 ≤ 132 ✓. (D): P8.D(v) in the labels u′ ✓,
  1 + 0.42W/λ ≤ W/λ for λ ≤ W/40 ✓, K_D ≤ C_I ✓. Enlargement of pairs with λ < ε/2 is legitimate in each case
  (Fact 0.1 needs no membership of the enlarged pair in 𝖠; the room is there).
* **(E2_I)** — this is where pairs with one point near X₀ and one near E_Y occur. λ_I > Λ_I ⇒ λ ≥ (8/9)Λ_I (needs
  the Stretch bound, proved for all pairs by splitting into [ε/2,ε]-pieces, each in (A), (P) or (D)) ✓. λ > λ₀:
  (T2) and u_a ≥ u_{a_{j_I}} ≥ W give c ≥ min(c_sep, W/2) = W/2 ≥ c_I — the pair (a_{j_I}, b_E) included; chords are
  non-decreasing ✓. λ ≤ λ₀: c(t₂) ≥ λ/2 ≥ (4/9)Λ_I = c_I ✓.
* Then Cor. End gives (S1) c ≥ ½min(λ_I,32R_B) for all pairs with λ_I ≥ ε/2 (c_I = (4/9)Λ_I ≥ 16R_B since
  R_B ≤ Λ_I/36) — the exact (S1) that (∗) of Step 1(d) needs for the far pairs of the tail. **All pairs are covered.**
* (a): hypotheses of P8.H verified with G_f = 3W (ϑ_T(3W)^{γ_*} ≤ 1/20, 2.02W ≤ min(3W,R_A,U_A),
  (2.02W/R_A)^{γ_*} ≤ 1/10); D ≤ 2.01W/(1−v). Hypotheses (D0)–(D3) of P8.D verified (a_* ≤ 4.11W).

---------------------------------------------------------------------------------------------------------------------

## 4. Budget, constants, "larger ε"

`constants.py` recomputes §5 and checks 19 side conditions used in §6 (all hold for both constant sets):

| | N8 set | P8a interim set |
|---|---|---|
| γ₁, γ_*, a_I, γ_B | 1/4, 1/4, 1/8, 1/16 | same (assuming a′ = 1/2, γ_T = 1/4) |
| R_A, M_A, ϑ_h | 6.25·10⁻⁶, 0.100, 7.05 | 5.28·10⁻⁷, 0.186, 17.9 |
| W, C_I, Λ_I | 2.98·10⁻¹⁰, 8.81, 7.44·10⁻¹² | 1.44·10⁻¹¹, 28.6, 3.59·10⁻¹³ |
| R_B | 9.8·10⁻³⁹ | 7.9·10⁻⁴³ |
| v₀ (binding: 10⁻⁶γ_BR_B/(4.5U_max+2)) | 1.54·10⁻⁴⁷ | 1.61·10⁻⁵¹ |
| ε_* (if ε_T, C_z not binding) | 1.5·10⁻⁴⁰ | 1.2·10⁻⁴⁴ |
| T₀ = T₂ + 2.3U_max + 1 | T₂ + 20.32 | T₂ + 15.72 (= 19.5 for T₂ = 3.78) |

* Exponent chain: (a′,γ_T) → γ₁ = min(a′/2,¼) → γ_* = min(a′/2,γ_T) → a_I = γ_*/2 → γ_B = γ_*/4 ✓. Two
  applications of Cor. End.
* **Scale: it is NOT "R → 16^{−1/γ}R".** The hand-over is not the restart of Remark E-restart (which the header
  rightly lists as not used): R_B = (γ_B/(400C_I))^{1/a_I} with C_I ≈ 0.34R_A^{−γ_*} + …, 1/a_I = 2/γ_* = 8, i.e.
  R_B ≈ 10⁻³⁸, against 16^{−4}R_A ≈ 10⁻¹⁰ for a P7 restart. Correct as computed; Remark (3)'s words "one restart" should
  be "one hand-over (Prop. P8.I)" (F5).
* v₀'s five terms each match a use: v_T ((H_T)); 2·10⁻¹¹γ_B² (both Cor. End, P8.D (D3), P8.H); stage B with
  U_I ≤ (9/8)U_max; stage A with U_A ≤ U_max/2; 132v ≤ W (case (P)). ε_* ≤ R_B/64 implies ε ≤ R_A/64, W/100, Λ_I/2;
  (W/C_z)⁴ gives z₀ ≤ W. T_stop ≤ t₂ + 2.1W + 2.25U_max/(1−v) ≤ T₀ ✓.
* **"Larger ε reuse the ε_\* path": immediate.** The true candidates do not depend on ε (the Snitch's law contains no
  ε; ε enters only Harry's path and the definition of "seen"), and |S−H| ≤ ε_* ≤ ε. The path for ε > ε_* still depends
  on (v, ε) only.

---------------------------------------------------------------------------------------------------------------------

## 5. Corollary P8.X and lem:A41

lem:A41 needs: finite nested D_N with dense union ✓ (dyadic); ε_N → 0 ✓ (2^{−N}ε_*); paths H_N, |H_N′| ≤ 1 on [0,T],
H_N(0) = 0 (used by Arzelà–Ascoli in lem:limit) ✓ (design T_g for (v,ε_N), constant after T_stop, same v for all N);
within ε_N of every direction of D_N by time T — P8.M gives it for EVERY direction, for the true candidates ✓;
T = T₀ independent of N ✓ (depends only on the constants of (H_T)). Conclusion of lem:A41: ONE path H, |H′| ≤ 1,
H(0) = 0, catching EVERY direction of [0,2π) exactly by T₀ (density + openness of the non-caught set) ✓. This is the
problem's exact capture at ε = 0 (speed ≤ 1; not speed = 1). **OK, conditional on (H_T).**

---------------------------------------------------------------------------------------------------------------------

## 6. (H_T): precision, use, labelling

* Stated as: absolute constants; for all v ≤ v_T, ε ≤ ε_T: t₂ ≤ T₂ and existence of n̂, x⁰, 𝒢 with (T0)–(T5). All
  quantities (N, c, T of x⁰; P(t₂); true candidates at t₂; "seen during [0,t₂]") are determined by (v, ε) through the
  path (T1),(T2) and by x⁰. Existential in x⁰ is fine for P8.M. **Used verbatim**: (T0) [X₀ = x⁰(0); true/ghost;
  coverage], (T1) [stage A; cases (P), (D); (E2_I) for λ ≤ λ₀] for ALL pairs incl. those meeting the ghost hole (X2),
  (T2) [stage A; case (P); (E2_I)] for ALL pairs incl. A₁–A₂ pairs (X1), (T3) on u ≤ 3W, (T4) on u′ ≤ W, (T5),
  1 ≤ U ≤ U_max, t₂ ≤ T₂. Nothing beyond (H_T) is used.
* **F2 (needed).** (T0) says 𝒢 ⊂ (0,U), so u = 0 must be a true label. In the intended realisation x⁰(0) = P(t₂) is
  the VIRTUAL candidate α₀ at distance 0, while the true candidate α₀ is at positive distance at t₂ (it is caught
  ≤ vε/(3(1−v)²) later, as §5 itself says), and no true candidate sits at P(t₂). So (T0) as written is false there.
  Replace "𝒢 ⊂ (0,U)" by "𝒢 ⊂ [0,U]". Nothing in §§1–6 uses that u = 0 or u = U is true.
* **F3.** (H_T) must fix D₁ ("for the value of D₁ fixed in the design; all constants may depend on it"); the text
  quotes D₁ = 1 (P8a) and D₁ = 0.1 (numerics) side by side.
* Note for P8a (not refereed here): a true label requires S_θ not caught before t₂; any candidate of the hole or of
  the bulk caught exactly during run 2 must be put in 𝒢 with a point making x⁰ C¹.
* **Honest labelling: yes.** Header, P8.M and P8.X all say "modulo (H_T)"; (X1), (X2) are flagged as missing even
  from P8a's interim statement; Remark (4)'s numbers are labelled as coming from numerical/interim constants.

## 7. List of text fixes

* **F1** (P8.W(c),(d)): proviso c(a_j,a_{j+1};t_j) > 0, and the sentence that (S1) + Step 1(a) give it (§1.3).
* **F2** ((H_T)(T0)): 𝒢 ⊂ [0,U].
* **F3** ((H_T)): fix D₁.
* **F4** (header): "[B] Theorem B/R not used" vs P8.W(d) citing the Claim of Theorem R — say "only via P7.B(c), which
  is not used in §6".
* **F5** (Remark (3)): "one restart" → "one hand-over (Proposition P8.I); the scale is R_B = (γ_B/(400C_I))^{1/a_I},
  not 16^{−1/γ}R".
* **F6** (Remark (4)): list a′, γ_T, T₂ (and that G_T, C_z, v_T, ε_T are not binding) for the P8a set; add ε_*.
* **F7** (P8.H): state v ≤ 10⁻⁴ (from the standing assumption); (P8.D (3.3)): the factor 2 can be 1 (harmless).

## 8. Bottom line

Modulo (H_T) with F2, and with F1 inserted, Theorem P8.M (every direction seen by T₀ for all ε ∈ (0,1), v ≤ v₀) and
Corollary P8.X (exact capture by one 1-Lipschitz path) are correctly proved from sec_B / sec_E / lem:A41, every
citation being used within its hypotheses. The result remains **conditional**; v₀ ≈ 10⁻⁴⁷–10⁻⁵¹.
