# P6f-claims — statements and proofs of the PROVED claims of stream P6f (final stretch)

**Nothing here proves the round-6 goal, and nothing here proves hypothesis (FS) of Theorem F (`referee/P6a2-claims.md`).**
What is proved: a static geometric lemma (F1), two elementary termination criteria for the legs of construction C
(F2, F4), and a conditional final-stretch theorem (F3) whose hypothesis (P_q) — a log-Lipschitz bound on the tangent angle
of the remaining arc *at every time of the final stretch*, with the non-small constant q = 1/4 — is NOT proved
(and is expected to be false for general entry data when ε ≪ L·Q̄^{1/μ}; see `reports/P6f-1.md` §3).
Formulation unchanged: Harry speed ≤ 1, path fixed in advance, S' = v(S − H)/|S − H|, vision radius ε. No strengthening.

**Notation and external inputs (statements only), all from `referee/P6a-claims.md` (v3):**
* virtual candidates x_θ, field F, f, A = DF, a*(ρ) (§1); Lemma V(ii): 0 ≤ A ≤ a*(ρ) I, a* ≤ 2/ε;
  Lemma VC(a),(b),(c) (existence; pairwise distances non-decreasing; ρ_θ(t) ≤ ε ⇒ θ is seen by t);
* l_t(a,b), c(a,b;t), T (unit tangent, direction of increasing label), Lemma 2(i): (d/dt) l_t(a,b) = v∫_a^b T·AT ds;
* construction C, its legs (base a_j at time t_j, target a_{j+1} with l_{t_j}(a_j, a_{j+1}) = ε on a non-final leg, heading u
  constant on a leg), μ = v/(1 − v), ε₁ = e^{2μ}ε, and Lemma C:
  (2) during leg j+1: x_{a_{j+1}}(t) = P(t) + ρ(t)u with ρ' = −1 + v f(ρ), and x_{a_j}(t) = P(t) − β(t)u, β ≥ 0; a leg lasts
      ≤ ε/(1 − v);
  (3) every θ ∈ [a_j, a_{j+1}] is seen by t_j; if the construction stops, every label up to the end label is seen;
  (4) for t in leg j+1: l_t(a,b) ≤ e^{2μ} l_{t_j}(a,b) for all a < b, in particular l_t(a_j, a_{j+1}) ≤ ε₁.
* C_cut: the same construction with end label b_e instead of 2π (the legs and Lemma C are unchanged; "final leg" means
  a_{j+1} = b_e, which happens iff l_{t_j}(a_j, b_e) ≤ ε; the construction stops when P meets x_{b_e}).
Throughout, t_{j_1} is a leg start of C_cut ("entry"), R_j := l_{t_j}(a_j, b_e) (remaining length at the leg start t_j),
D(t) := |x_{b_e}(t) − P(t)| (distance to the far end). For a time t in leg j+1 and a label s ∈ [a_j, b_e]:
σ_t(s) := l_t(s, b_e) (current arclength from the far end; strictly decreasing in s because |∂_θx| ≥ 1).

---------------------------------------------------------------------------------------------------------------------

## Lemma F1 (static: a log-Lipschitz tangent gives chord-arc and a thin cone). PROVED

Let Γ: [0, Λ] → ℝ² be a C¹ curve parametrised by arclength σ, Γ'(σ) = e^{iψ(σ)} with ψ continuous. Let 0 ≤ σ_0 < Λ,
0 < q < 1, and assume

  **(LL_q)**  |ψ(a) − ψ(b)| ≤ q |log(a/b)|  for all a, b ∈ [σ_0, Λ] ∩ (0, Λ].

For σ ∈ (0, Λ] put e := e^{iψ(σ)} and, for vectors, z·e, z × e the components along e and across e. Then:

(a) for σ_0 ≤ σ' < σ ≤ Λ, σ' > 0:  (Γ(σ) − Γ(σ'))·e ≥ (1 − q²)(σ − σ')  and  |(Γ(σ) − Γ(σ')) × e| ≤ q(σ − σ');
    hence |Γ(σ) − Γ(σ')| ≥ (1 − q²)(σ − σ') (chord-arc), and the vector Γ(σ') − Γ(σ) makes an angle
    ≤ θ_q := arctan(q/(1 − q²)) with −e.
(b) for 0 ≤ σ' < σ_0 and σ with y := σ − σ_0 > σ_0/(1 − q²):
    (Γ(σ) − Γ(σ'))·e ≥ (1 − q²)y − σ_0 > 0 and |(Γ(σ) − Γ(σ')) × e| ≤ qy + σ_0; so Γ(σ') − Γ(σ) makes an angle
    ≤ arctan[(qy + σ_0)/((1 − q²)y − σ_0)] with −e, and this bound is decreasing in y.
(If σ_0 = 0, (a) holds for all 0 < σ' < σ and, by continuity, for σ' = 0.)

*Proof.* (a) Γ(σ) − Γ(σ') = ∫_{σ'}^{σ} e^{iψ(u)} du, so with δ(u) := ψ(u) − ψ(σ), |δ(u)| ≤ q log(σ/u) (u ≤ σ):
(Γ(σ) − Γ(σ'))·e = ∫_{σ'}^σ cos δ(u) du ≥ ∫_{σ'}^σ (1 − ½q² log²(σ/u)) du (cos x ≥ 1 − x²/2 for all real x), and
(Γ(σ) − Γ(σ')) × e = −∫ sin δ(u) du, of modulus ≤ q∫_{σ'}^σ log(σ/u) du. With x := σ'/σ ∈ (0, 1) and u = σw:
 ∫_{σ'}^σ log(σ/u) du = σ[(1 − x) + x log x] ≤ σ(1 − x) = σ − σ'   (x log x ≤ 0);
 ∫_{σ'}^σ log²(σ/u) du = σ∫_x^1 log²w dw = σ[2(1 − x) − x log²x + 2x log x] = σ[2(1 − x) + x log x (2 − log x)] ≤ 2(σ − σ'),
because log x < 0 < 2 − log x (antiderivative of log²w: w log²w − 2w log w + 2w). This gives both inequalities. The
modulus of a vector is at least its e-component; the angle with −e of the vector −(Γ(σ) − Γ(σ')) has tangent
|cross|/(along) ≤ q/(1 − q²).
(b) Γ(σ) − Γ(σ') = (Γ(σ) − Γ(σ_0)) + (Γ(σ_0) − Γ(σ')), and |Γ(σ_0) − Γ(σ')| ≤ σ_0 − σ' ≤ σ_0 (arclength). Apply (a) to
(σ_0, σ) (if σ_0 = 0 there is nothing to prove). The function y ↦ (qy + σ_0)/((1 − q²)y − σ_0) has derivative of the sign
of −qσ_0 − (1 − q²)σ_0 < 0. ∎

*Remarks (not needed below).* (1) (LL_q) is equivalent to: ψ∘exp is q-Lipschitz on [log σ_0, log Λ]; for C² curves:
|Q| ≤ q, Q := ∂ψ/∂ log σ = σκ. (2) The constants are sharp to first order in q: for the logarithmic spiral
ψ = q log σ (σ_0 = 0) and σ' = 0, Γ(σ) − Γ(0) = σe/(1 + iq), i.e. along = σ/(1 + q²), |cross| = qσ/(1 + q²). (3) No bound on the
total turning ψ(Λ) − ψ(σ_0) is assumed: the tangent may wind arbitrarily often. Numerical check of (a) on 400 random
curves (log-spirals, zig-zags, random walks; q ∈ (0.02, 0.9)): `code/P6f/check_F1.py`, no violation.

---------------------------------------------------------------------------------------------------------------------

## Lemma F2 (far-end potential). PROVED

Consider C_cut from the leg start t_{j_1}, and let c_0 ∈ (v, 1]. Let t* > t_{j_1} be such that the construction has not
stopped before t*, and assume

  **(H_{c_0})**  for every t ∈ [t_{j_1}, t*) with D(t) > 0:  u(t)·(x_{b_e}(t) − P(t)) ≥ c_0 D(t)

(u(t) = heading of the leg containing t; at a switch time either leg may be used). Then

  D(t*) ≤ D(t_{j_1}) − (c_0 − v)(t* − t_{j_1}),  hence  t* ≤ t_{j_1} + D(t_{j_1})/(c_0 − v) ≤ t_{j_1} + R_{j_1}/(c_0 − v).

Consequently, if (H_{c_0}) holds at all times before the stopping time, C_cut stops by t_{j_1} + R_{j_1}/(c_0 − v), and
every label in [a_{j_1}, b_e] is seen by then.

*Proof.* P is 1-Lipschitz and x_{b_e} is v-Lipschitz, so D is Lipschitz, hence absolutely continuous. Fix a leg and put
r := x_{b_e} − P. Inside the leg, r' = vF(r) − u. If r(t) = 0 then r'(t) = −u ≠ 0, so the zeros of r inside a leg are
isolated; there are finitely many legs before t* (Lemma C(0)); so {t < t* : D(t) = 0} is a null set. At every other
time inside a leg, D is differentiable and D' = (r/D)·(vF(r) − u) = v f(D) − u·r/D ≤ v − c_0, by (H_{c_0}) and f ≤ 1.
Integrate. D ≥ 0 gives the bound on t*; D(t_{j_1}) = c(a_{j_1}, b_e; t_{j_1}) ≤ R_{j_1} because P(t_{j_1}) = x_{a_{j_1}}(t_{j_1}).
If the construction never stopped, t* could be taken arbitrarily large: contradiction. Seeing: Lemma C(3). ∎

*Remarks.* (1) On a final leg (H_1) holds automatically (the target is x_{b_e}). (2) (H_{c_0}) is a condition on ONE
point of the front, the far end: its bearing from the heading must stay ≤ arccos c_0 < arccos v. No regularity of the
arc, no sector condition for the other points, and no bound on K̃ is needed. (3) (H) is the hull-perimeter lemma
(P6b.4 / P6c Claim 11) for the two-point set {P, x_{b_e}}, whose "perimeter" is 2D.

---------------------------------------------------------------------------------------------------------------------

## Lemma F4 (last blob). PROVED

Let m ≥ 1 and assume 2μe^{2μ}m ≤ 1/2 (true if v ≤ 1/100 and v ≤ 0.24/m). If at a leg start t_j of C_cut the remaining
length satisfies R_j ≤ mε, then C_cut stops after at most 2m further non-final legs and one final leg, i.e. by
t_j + (2m + 1)ε/(1 − v), and every label in [a_j, b_e] is seen by then.

*Proof.* Let leg i+1 (i ≥ j) be non-final and R_i ≤ mε. Then l_{t_i}(a_{i+1}, b_e) = R_i − ε, and by Lemma 2(i),
Lemma V(ii) (T·AT ≤ a* ≤ 2/ε) and Lemma C(4), for t in the leg:
(d/dt) l_t(a_{i+1}, b_e) ≤ v(2/ε) l_t(a_{i+1}, b_e) ≤ (2v/ε)e^{2μ}R_i. The leg lasts ≤ ε/(1 − v), so
R_{i+1} ≤ R_i − ε + 2μe^{2μ}R_i ≤ R_i − ε + 2μe^{2μ}mε ≤ R_i − ε/2. By induction R_i ≤ mε − (i − j)ε/2 for all non-final
legs, so there are at most 2m of them; then R ≤ ε and the leg is final. Each leg lasts ≤ ε/(1 − v). Seeing: Lemma C(3).
(Numbers: for v ≤ 1/100, μ ≤ 1.0102v and e^{2μ} ≤ 1.0205, so 2μe^{2μ}m ≤ 2.062vm ≤ 0.495 if v ≤ 0.24/m.) ∎

---------------------------------------------------------------------------------------------------------------------

## Theorem F3 (conditional final stretch: persistence of a log-Lipschitz class with a NON-SMALL constant suffices). PROVED (implication; the hypothesis (P) is NOT proved)

Constants: q := 1/4, M := 13, σ_0 ≥ ε a length, m := Mσ_0/ε, and v ≤ min(1/100, 0.24/m).
Consider C_cut from a leg start t_{j_1}. Assume:

  **(P)**  for every leg j+1 with j ≥ j_1 and R_j ≥ Mσ_0, and every time t of that leg: the tangent of the front at
  time t has a continuous angle ψ_t on [a_j, b_e] with
     |ψ_t(s) − ψ_t(s')| ≤ q |log(σ_t(s)/σ_t(s'))|   for all s, s' ∈ [a_j, b_e] with σ_t(s), σ_t(s') ≥ σ_0.

Then C_cut stops, and every label of [a_{j_1}, b_e] is seen, by the time

  t_{j_1} + R_{j_1}/(0.76 − v) + (2m + 1)ε/(1 − v)  ≤  t_{j_1} + 1.34 R_{j_1} + 1.02(2m + 1)ε.

*Proof.* Let j_2 ≥ j_1 be the first leg index with R_{j_2} < Mσ_0, or the index at which the construction stops if there
is none (if the construction stops earlier, there is nothing to prove; we show below that the time until t_{j_2} is
bounded, so j_2 exists).
*Step 1: (H_{0.76}) holds at every time t of a leg j+1 with j_1 ≤ j < j_2.* Fix such t. Let Γ be the arc [a_j, b_e] at
time t, parametrised by σ = σ_t ∈ [0, Λ], Λ := σ_t(a_j) ≥ R_j ≥ Mσ_0 (lengths are non-decreasing in t; Lemma VC). The front
is a regular C¹ curve (Lemma VC(a)), Γ'(σ) = −T, and (P) is (LL_q) for Γ on [σ_0, Λ]. Put a := Λ, b := σ_t(a_{j+1}),
e := Γ'(a), e_b := Γ'(b). By Lemma C(4), a − b = l_t(a_j, a_{j+1}) ≤ ε₁ ≤ 2ε ≤ 2σ_0, so b ≥ (M − 2)σ_0 = 11σ_0 > σ_0, and
a − b > 0.
 (i) By Lemma C(2), x_{a_j}(t), P(t), x_{a_{j+1}}(t) are collinear in this order and u is the direction from x_{a_j}(t) to
 x_{a_{j+1}}(t), i.e. of Γ(b) − Γ(a). By Lemma F1(a), u makes an angle ≤ θ_q = arctan(q/(1 − q²)) = arctan(4/15) < 0.2607
 with −e.
 (ii) w := x_{b_e}(t) − x_{a_{j+1}}(t) = Γ(0) − Γ(b). By Lemma F1(b) with σ = b, σ' = 0, y = b − σ_0 ≥ 10σ_0
 (> σ_0/(1 − q²)): w makes an angle ≤ arctan[(10q + 1)/(10(1 − q²) − 1)] = arctan(3.5/8.375) < 0.3959 with −e_b. By (P),
 the angle between e_b and e is ≤ q log(a/b) ≤ q log(M/(M − 2)) = ¼ log(13/11) < 0.0418. So w makes an angle < 0.4377
 with −e.
 (iii) x_{b_e}(t) − P(t) = w + ρu with ρ := |x_{a_{j+1}}(t) − P(t)| ≥ 0 (Lemma C(2)). Both w and u lie in the closed
 convex cone of half-angle 0.4377 (< π/2) around −e, hence so does w + ρu ≠ 0; so the angle between x_{b_e} − P and u is
 < 0.4377 + 0.2607 = 0.6984, and cos 0.6984 > 0.765 > 0.76. In particular D(t) > 0.
*Step 2.* By Lemma F2 with c_0 = 0.76 and t* = t_{j_2}: t_{j_2} ≤ t_{j_1} + R_{j_1}/(0.76 − v) (this also shows that j_2
exists: the legs j_1 < j ≤ j_2 are finitely many in bounded time by Lemma C(0)).
*Step 3.* If the construction has not stopped at t_{j_2}, then R_{j_2} < Mσ_0 = mε and Lemma F4 applies.
Numbers: 1/(0.76 − 0.01) < 1.34, 1/(1 − v) ≤ 1.02. ∎

*Remarks.* (1) **What (P) is.** It is the scale-invariant class of (E_Q) ("tangent angle q-Lipschitz in the logarithm of
the distance from the far end"), in the variable "current arclength from the far end", with the fixed non-small constant
1/4, and it is required on scales ≥ σ_0 only; σ_0 may be any fixed multiple of ε (the cost is m = 13σ_0/ε in the blob
term and in the bound on v). At the entry time, (P) is exactly hypothesis (E_Q) with Q̄ ≤ 1/4. **(P) at later times does
not follow from (E_Q) at entry by anything proved here.**
(2) Theorem F3 replaces (FS) in Theorem F of P6a2 in the following sense: the proof of Theorem F uses (FS) only to bound
the time of the legs with base label > 2π − 2θ_0; Theorem F3 bounds that time directly (R_{j_1} ≤ L_s there). The
re-assembly is not written out here.
(3) With the hull-perimeter lemma (P6c Claim 11(b), unrefereed) in place of Lemma F2, the same proof works for every
q ≤ 1/2 (cone of half-angle < 0.89 around −e containing the whole remaining arc and the heading; opening γ < 1.78,
c_γ = 1 + cos γ − v(π + γ) ≥ 0.79 − 4.93v). This variant is NOT claimed here.
(4) Only the far end enters: what is really needed is (H_{c_0}) of Lemma F2 for some c_0 > v on the legs with R_j ≥ mε.
