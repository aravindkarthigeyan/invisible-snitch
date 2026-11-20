# Referee report R0: everything Theorem B uses except (H)

**Question.** Try to break Prop 1, Lemma 1, Prop 2, Prop 4, Prop 5, Prop 6(1)-(2), Lemma 2, Lemma 3, Lemma 4 and the
deduction in the proof of Theorem B in `snitch_proved.tex`. (H) itself is out of scope.

**Result (status: PROVED, modulo the fixes below).** No ERROR found. Every identity and inequality survived line-by-line
checking and numerical attack. There are four GAPs, all fixable in a few lines:
G1 (Prop 6(1): the "isotopy of the punctured plane" sentence is false as written), G2 (the discrete chase and Φ are
undefined if a later candidate is caught "accidentally" in an earlier leg), G3 (Lemma 4: the continuation step needs
e + ‖H_N − H‖ < c/4, not e < c/4), G4 (Theorem B / Lemma 4: H_N must be extended to [0,T] after the chase ends).
None changes a statement or a constant.

Code: `code/referee/R0/`. `snitch_exact.py` is an exact straight-run map built from the integrals of Prop 1
(bisection for k⁻¹ in a logistic variable so that β near 0 and near π both keep full relative precision); it agrees
with an rtol 1e-12 ODE solve to 1.5e-12. Reproduce every number below with
`cd code/referee/R0 && python -W ignore t1_integrals_k.py && python -W ignore t2_wavefront.py && python -W ignore t3_chase.py && python -W ignore t4_lemma4.py`
(t1 takes about 6 min, t3 several minutes).

---

## Prop 1 (integrals) — OK

Line check. r' = v r̂ − u. Radial component ρ' = v − cos β; perpendicular component with r̂⊥ = (−sin β, cos β):
ρβ' = −r̂⊥·u = sin β. (r·u)' = v cos β − 1, (vρ)' = v² − v cos β, sum v² − 1. For C:
d/dβ[v ln tan(β/2) − ln sin β] = v/sin β − cot β = (v − cos β)/sin β, matching dρ/ρ. Division by β' is legitimate
because sin β ≠ 0 on 0<|β|<π (and one can instead differentiate ρ g(β) directly: (ρ g)' = ρ' g + ρβ' g' = g[(v − cos β) + sin β (cos β − v)/sin β] = 0).
Reflection handles β<0. Note h and C use the unit heading u; for |H'|<1 they are not integrals (not used that way).

Numerics (t1): 300 random runs (v ∈ (0.01,0.99), ρ0 over 3 decades), ODE at rtol 1e-12: max relative drift of
h + (1−v²)t is 1.7e-11, of C is 4.8e-9; |ρ' − (v − cos β)| ≤ 7e-16.

## Lemma 1 (k monotone) — OK

g'/g = cot β − v·(½sec²(β/2))/tan(β/2) = cot β − v/sin β. Quotient rule gives the displayed numerator, and
sin²β + (cos β + c)(cos β − v) = 1 + (c−v)cos β − cv. With c = v this is 1 − v² > 0. Limits: g ~ 2^v β^{1−v} → 0 at 0;
at π, g ≈ δ(δ/2)^v → 0 (δ = π − β). g is continuous with zero limits at both ends, hence bounded; k is a continuous
strictly decreasing bijection (0,π) → ℝ, so k⁻¹ is continuous (used in Prop 4).

Numerics: 20 000 random (v, c, β), c ∈ (−3,3): max relative error of (eq:Fprime) vs central differences 9e-8.
k strictly decreasing on a 200 001-point grid for v ∈ {0.001, …, 0.999}; k⁻¹(0) − arccos(−v) ≤ 1.3e-15;
sup g ranges 1.000 to 1.991.

## Prop 2 (ray) — OK (one wording nit)

For 0<|β|<π: β = 0 and β = π are equilibria of β' = sin β/ρ and the (ρ, β) system is smooth while ρ>0, so by
uniqueness β never reaches 0 or π; then ρ = C/g(β) ≥ C/sup g > 0. On-ray cases are explicit. "Moreover ρ' ≥ −(1−v)
always": for general |H'| ≤ 1 this is ρ' = v − r̂·H' ≥ v − 1, not literally (eq:polar) (which assumes unit u).
Suggest writing that formula.

Numerics: 300 candidates with |β0| from 1e-12 to π, ρ0 over 5 decades, 119 times up to 50ρ0: never caught;
min ρ / (C/sup g) = 1.000000 (the bound is attained, at β = arg max g, as expected).

## Prop 4 (angle at first contact) — OK

h(t0) = d(cos α + v) − (1+v)d = −d(1 − cos α) ✓; h/C = −(1−cos α)/g(α) ~ −α^{1+v}/2^{1+v} ✓; continuity of k⁻¹ gives
β → θ*, and C = d g(α) → 0 gives ρ → 0 ✓.

Numerics (t2): α = 10⁻¹…10⁻⁸ for v ∈ {0.05, 0.2, 0.24, 0.5, 0.9}: bearing at α = 1e-8 equals arccos(−v) to 1e-9; ρ → 0
like α^{1+v} (e.g. v = 0.2: 0.195, 7.7e-4, 4.9e-7 at α = 0.1, 1e-4, 1e-8). The asymptotic ratio
(h/C)/(−α^{1+v}/2^{1+v}) → 1.

## Prop 5 (bearings ordered) — OK

c = v − (1−v²)t/d ∈ (−1, v] for t ∈ [0, t0) ✓. Bracket 1 − cv + (c−v)x equals (1−v)(1+c) at x = 1 and (1+v)(1−c) at
x = −1 (both expanded and checked) ✓. As α → 0⁺ (resp. π⁻), h/C → +∞ (resp. −∞), so β maps (0,π) onto (0,π)
increasingly; α = 0, π stay at β = 0, π; reflection gives the lower half. Hence β is a degree-1 monotone circle map
and the total variation is 2π.

Numerics: 20 000 equally spaced α, v ∈ {0.05, 0.2, 0.24, 0.5, 0.8, 0.95}, t/t0 up to 0.9999: bearing differences all
strictly positive.

## Prop 6(1) (simple closed curve) — GAP G1 (wording; conclusion true)

"Its flow is an isotopy of the punctured plane as long as no candidate reaches 0" is false as stated: the flow of
v r̂ − u is not defined on the whole punctured plane for any positive time, because points on the forward ray at
relative distance ρ < (1−v)t reach 0 before t (e.g. relative position (0.1, 0) reaches 0 at time 0.1/(1−v)).

Fix: (i) injectivity: if S_α(t) = S_α'(t) with both away from H, backward uniqueness for the locally Lipschitz field
gives α = α'; so α ↦ S_α(t) is a continuous injection of the circle, i.e. a Jordan curve (continuity in α holds because
on [0,t], t<t0, ρ(α,s) is jointly continuous and positive on a compact set, hence bounded below). (ii) winding number:
it equals the degree of α ↦ β(α,t), which is 1 by Prop 5 (or: it is continuous in t while the curve avoids H(t), and is
1 at t = 0). The same argument shows α ↦ S_α(t) is smooth (smooth dependence on initial data), which Prop 6(2) needs.

## Prop 6(2) (L ≤ 2πd + 2πvt) — OK

Regularity: ∂_αS obeys the linear ODE w' = (v/ρ)(I − r̂r̂ᵀ)w with w(0) = d(−sin α, cos α) ≠ 0, so w never vanishes;
|w| is C¹ in t; the integrand is jointly smooth in (α, t) on the circle × [0, t1], t1 < t0 (ρ bounded below there), so
L is C¹ on [0, t0) and differentiation under the integral is justified. Where ∂_αS ∥ r̂, sin φ = 0 and the integrand
is 0 — no singularity (φ is defined since w ≠ 0 and ρ > 0). ρ|∂_αβ| = |w||sin φ| is the perpendicular component of
∂_α r = ∂_α S ✓. Integrand v sin²φ|w|/ρ = v|sin φ||∂_αβ| ≤ v|∂_αβ| ✓; ∫|∂_αβ| = total variation = 2π by Prop 5
(reference direction irrelevant). L(0) = 2πd, so L(t) ≤ 2πd + 2πvt and → 2πd/(1−v) at t0 ✓. Rectifiability: smooth
closed curve for t < t0; at t0 only the limit of L is used (Lemma 3).

Numerics (t2): L/(2π + 2πvt) ≤ 1 at every sampled time for v from 0.05 to 0.95 (min 0.767 at v = 0.95);
max averaged L'/(2πv) = 0.9991 (v = 0.05, early times: the bound is nearly sharp at t = 0, where sin φ = ±1).
Pointwise formula vs finite difference of L (20 000 nodes): v = 0.2, t/t0 = 0.3: 1.217475 vs 1.217475;
v = 0.5, t/t0 = 0.9: 2.262960 vs 2.262900; all below 2πv.

## Lemma 2 (Φ' = −(1−v) + vW, W ≤ A) — OK, with GAP G2 in the definition of the chase

Line check. Pursuit of S_j is a straight run on the line H S_j (S_j moves along r̂_j = u) ✓. |S_{i+1} − S_i|' =
e·(v r̂_{i+1} − v r̂_i) = v(cos c_i + cos b_i) ✓. b+c = π − a, so cos b + cos c = 2 sin(a/2) cos((b−c)/2) ≤ 2 sin(a/2)
≤ a (cos((b−c)/2) ≥ 0 since |b−c| ≤ π) ✓. Continuity at a catch ✓.

Regularity: between catches each term of Φ is C¹ provided (a) the remaining S_i are away from H and (b) consecutive
S_i are distinct. (b) holds by backward uniqueness. (a) holds by Prop 2 except in the case below. Collinearity of H,
S_i, S_{i+1} is harmless: |S_{i+1} − S_i| is still differentiable, and the angle identity a+b+c = π holds for all three
degenerate triangles (H between: (π,0,0); S_i between: (0,π,0); S_{i+1} between: (0,0,π)); checked numerically.

**G2 (accidental catches).** If at the start of the leg towards S_j some later S_i (i > j) lies on the open segment
(H, S_j), Prop 2 says it is caught during that leg, before S_j. Then "run straight at the current position of α_i"
and the term |S_{i+1} − S_i| in Φ are undefined afterwards. This is a codimension-one coincidence and is not excluded
by anything in the paper for the fixed dyadic sets. It does not occur numerically (minimum clearance below), but the
proof must handle it. Fix: in the definition of the chase, skip a candidate already caught, and delete it from the
polyline at its catch time. At that instant S_i = H, so deletion replaces |S_i − S_{i−1}| + |S_{i+1} − S_i| by
|S_{i+1} − S_{i−1}|, a downward jump (triangle inequality); before deletion r̂_i is constant (S_i rides the ray) so the
identity holds up to the catch. (H) must then be read for this modified polyline (it is the one the chase uses).
Theorem B's integration tolerates downward jumps. (Only an accidental catch of a *later* candidate is possible;
earlier ones are already caught; during [0, t0] only α = 0 is caught, by Prop 2.)

Numerics (t3): 3000 random configurations (1 to 11 remaining points, v ∈ (0.01, 0.95)), a quarter each with
P1 on the ray beyond P0, H between P0 and P1, and a later leg collinear with H. Exact-map forward step and RK4 backward
step, central difference: max |Φ'_fd − (−(1−v)+vW)| = 9.6e-7 (finite-difference level); max (W − A) = 1.1e-16 ≤ 0;
max |a+b+c−π| over degenerate triangles = 4.2e-8.

## Lemma 3 (Φ(t0) ≤ 2πd/(1−v)) — OK

Vertices S_0, …, S_N lie on Γ(t) in cyclic order (α increasing), so each chord ≤ the arc between consecutive
vertices and the closed perimeter P(t) ≤ L(t) < 2πd/(1−v). Each S_i is continuous on [0, t0] and S_0(t0) = H(t0);
Φ(t0) is the open polyline H = S_0 → S_1 → … → S_N, i.e. P(t0) − |S_N − S_0| ≤ lim P(t) ✓.

Numerics (t2): 300 sets (uniform random, clustered with s.d. 0.05 about α = 0 on both sides, equally spaced),
N up to 400, v ∈ (0.01, 0.95): max Φ(t0)/(2π/(1−v)) = 0.9970.

## Lemma 4 (compactness) — OK, with GAP G3 (and G4, see Theorem B)

* Arzelà–Ascoli ✓ (equi-Lipschitz, H_N(0) = 0, on the fixed interval [0, T] — requires G4).
* ODE under a merely continuous H: the field is jointly continuous on {S ≠ H(t)} and locally Lipschitz in S, so
  unique local solutions; since |S'| = v, S has a limit at the end of the maximal interval, which must satisfy
  S = H; so "not caught on [0, τ]" ⇔ existence with ρ > 0 on [0, τ] ⇒ min ρ = c > 0 ✓.
* Lipschitz constant: on {|x| ≥ r}, |x̂ − ŷ| ≤ |x − y|/r (r x̂ is the metric projection onto the ball B_r, which is
  1-Lipschitz). So F is (4v/c)-Lipschitz in each argument on {ρ ≥ c/4}; the paper's 8v/c is valid (it is the bound
  from the elementary 2/r estimate). Numerically max |x̂−ŷ|·r/|x−y| = 0.99946 over 2·10⁵ samples.
* Gronwall bound as stated ✓ (t4: speed-1 zigzags H_N with ‖H_N − H‖ = 1/N converging to H(t) = (0.8t, 0): the
  observed max |S_N − S| is 4 to 6 orders below the Gronwall bound, and decays like ‖H_N − H‖²). This example also
  illustrates the paper's remark that the limit can have speed < 1.
* **G3 (continuation).** The text says the bound on e = |S^N_{α'} − S_α| "is below c/4". That is not enough: one needs
  ρ_N = |S^N_{α'} − H_N| ≥ |S_α − H| − e − ‖H_N − H‖ ≥ c/2 − e − ‖H_N − H‖ > c/4, i.e. e + ‖H_N − H‖ < c/4. Choose U and
  N0 so that this holds; then the set of s ≤ min(τ+δ, T) on which ρ_N ≥ c/4 on [0, s] is closed, and open in
  [0, min(τ+δ,T)] by the strict inequality, hence everything. Also note ρ_N > 0 throughout implies α' is not caught by
  H_N there, so "caught candidates stop existing" never interferes.
* Main step: t_N ≤ T, subsequence t_N → t* ✓ (subsequences are taken after H is fixed, per α — fine). If α is not
  caught by H on [0, t*], the Claim with τ = t* gives ρ_N ≥ c/4 on [0, min(t*+δ, T)], which contains t_N for large N
  (t_N ≤ T always, t_N < t* + δ eventually): contradiction ✓. So catch time under H ≤ liminf t_N ≤ T: "caught by T" is
  preserved under uniform limits (it is the catch *failure* that is open).
* Openness of the uncaught set: for α uncaught on [0, T], ρ ≥ c > 0 on [0, T], Claim with H_N = H, τ = T gives a
  neighbourhood uncaught on [0, T] ✓. This only uses candidates that exist on all of [0, T], so caught candidates
  "stopping" is irrelevant ✓. Closed + dense ⇒ whole circle ✓.
* What the statement needs: finite sets, nested (only used to get α ∈ D_N for all N ≥ M along the subsequence; "α lies
  in infinitely many D_N" suffices), dense union, uniform T, and |H_N'| ≤ 1, H_N(0) = 0 on [0, T]. **No** order,
  dyadic structure, or 0 ∈ D_N is needed by Lemma 4 (0 ∈ D_N is needed by the chase).

## Theorem B deduction (time bound T) — OK, with GAP G4 (and G2 inherited)

Φ' ≤ −κ, κ = 1 − v(1+π) > 0, on each leg; Φ continuous (or with downward jumps under G2); Φ > 0 until the final catch
(distinct live candidates never coincide), Φ = 0 at it; each leg has finite length |S_j − H|/(1−v) and there are N
legs, so the chase terminates; integrating, end time ≤ t0 + Φ(t0)/κ ≤ d/(1−v) + 2πd/((1−v)κ) = T ✓ (algebra
rechecked). Every α_i is caught at or before the end ✓.

**G4.** Lemma 4 needs each H_N defined on all of [0, T] with |H_N'| ≤ 1. Say: after its last catch H_N stays put. (Or
continues straight; anything 1-Lipschitz.) Trivial but should be written.

Visiting order: candidates are chased in increasing α; besides the accidental case (G2), no candidate is caught out of
order (Prop 2: a straight leg catches only what lies on its forward ray). Accidental early catches do not hurt the
conclusion (they only help), but they do need the G2 definition.

Also note (H) is only needed for the dyadic sets actually used (or any nested dense family containing 0); the theorem
could assume that weaker form.

Numerics (t3), exact chase, 8 substeps per leg:

| v | N | Φ(t0) | bound 2π/(1−v) | end time | T | max A | max(W−A) | max[avg Φ' + κ] | accidental catches | min clearance |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.05 | 8 | 5.591 | 6.614 | 7.236 | 9.394 | 2.703 | −0.19 | −0.055 | 0 | 2.4 |
| 0.05 | 512 | 6.565 | 6.614 | 8.325 | 9.394 | 3.098 | −0.004 | −0.057 | 0 | 132 |
| 0.15 | 8 | 6.130 | 7.392 | 9.607 | 20.69 | 2.666 | −0.19 | −0.167 | 0 | 2.2 |
| 0.15 | 512 | 7.246 | 7.392 | 11.19 | 20.69 | 3.054 | −0.008 | −0.168 | 0 | 85 |
| 0.24 | 8 | 6.720 | 8.267 | 12.81 | 1375 | 2.633 | −0.19 | −0.271 | 0 | 2.1 |
| 0.24 | 512 | 7.999 | 8.267 | 15.11 | 1375 | 3.015 | −0.024 | −0.260 | 0 | 56 |

(N = 32, 128 rows are in the script output and interpolate.) "min clearance" = min over legs of the perpendicular
distance from a later candidate to the segment [H, S_j], divided by |S_j − H|, over candidates whose projection
falls inside the segment; 0 would be an accidental catch. Max A here is sampled only at 8 points per leg, so it
underestimates the brief's 3.139; it is not evidence about (H). The slope bound Φ' ≤ −κ holds with large margin
(the averaged slope stays ≥ 0.05 below −κ), because W stays well below π. End times are 1.1–1.3 (v = 0.05), 1.8–2.1
(v = 0.15) and ~90 (v = 0.24) times below T; T blows up as v → 1/(1+π) (κ = 0.0060 at v = 0.24). End time 15.1 at
v = 0.24, N = 512 is consistent with the paper's 13.24 at v = 0.2.

## What I tried that failed to break anything
Near-π precision: my first map lost α = π (arctan2 rounds β to π exactly), producing spurious "violations" of
Props 5 and 6(2). This was a bug in my code, fixed by computing π − |β| as atan2(|y|, −x); recorded here because
any simulator of this problem must do the same.

## Most useful next step
Insert the four fixes (G1: injectivity + degree argument; G2: "skip and delete caught candidates", Φ may jump down;
G3: require e + ‖H_N − H‖ < c/4; G4: extend H_N to [0, T]). Then a second referee should check Theorem B with (H)
restated for the modified chase.
