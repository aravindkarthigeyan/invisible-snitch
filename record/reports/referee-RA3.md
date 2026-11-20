# Referee report RA3 — stream A-3 claims (`referee/A3-claims.md`)

Referee: independent (did not read reports/A-3.md or code/A3/). Inputs: BRIEF.md §1–2, paper/main.tex §2–5 and
"The angle hypothesis" (Lemmas A1–A4, B1, Theorem B2, Lemma A21, Theorem A23), referee/A3-claims.md.
All scripts are new and independent: `code/referee/RA3/` (commands in §6). Python 3.12, numpy/scipy.

## 0. Verdicts

| Claim | Verdict |
|---|---|
| Lemma A3.1 (summation by parts, sharp form, W ≤ 2 + Σκ_i ≤ 2 + TC) | **OK**. Open-arc refinement and endpoint terms checked; the constant 2 is sharp for the polyline inequality |
| Lemma A3.2 (laws for τ, log\|T\|, κ, ∂_ατ) | **OK**. One wording fix (G1) |
| Proposition A3.3 (TC′ formula, \|TC′\| bound) | **OK** under its stated hypotheses. The remark on inflection creation is heuristic and is labelled as such |
| Lemma A3.4 (hull perimeter P: continuity, P′ ≤ −(1 + cos B_H) + v(π + B_H), P ≤ 2Φ) | **OK**. Vertex changes, Harry as vertex/edge point/interior, B_H = π, and catches all checked. Note (N1): B_H itself can jump down at a catch. This is harmless because the bound is used only almost everywhere |
| Theorem A3.5 (capture under (E_H, γ)) | **OK (conditional)**. The combination with Ψ and the time bound are correct. Observation (N2): (E_H, γ) ⟹ (E_γ) with the same γ, so the theorem is new as a hypothesis only for v < 0.2928 (where γ_H(v) > arccos v). The comparison paragraph should say so |
| γ_H table, T table, v1 | **OK**: reproduced to the printed precision (T differs by ≤ 0.2 % from optimising λ more finely) |

No ERROR found. The gaps are wording or presentation, each fixable in a sentence.

## 1. Lemma A3.1

**Identity.** By Lemma 2, cos b_i = −r̂_i·e_i and cos c_i = r̂_{i+1}·e_i, so W = Σ_{i=j}^{N−1}(r̂_{i+1} − r̂_i)·e_i.
Summation by parts gives r̂_N·e_{N−1} − r̂_j·e_j + Σ_{i=j+1}^{N−1} r̂_i·(e_{i−1} − e_i), with r̂_j = u. This is correct.
(For j = N − 1 the sum is empty. For j = N, W = 0 and the formula should not be used, since e_{N−1} is undefined. This
is cosmetic.)

**Sharp form.** |e_{i−1} − e_i| = 2 sin(κ_i/2), and e_{i−1} − e_i ⟂ e_{i−1} + e_i because both are unit vectors. So
|r̂_i·(e_{i−1} − e_i)| = 2 sin(κ_i/2)·|component of r̂_i ⟂ bisector| = 2 sin(κ_i/2)|sin ψ_i|. This is correct. At κ_i = π
the bound 2 still holds. The endpoint terms satisfy r̂_N·e_{N−1} ≤ 1 and −u·e_j ≤ 1, and 2 sin(x/2) ≤ x. So
W ≤ 2 + Σκ_i. The constant 2 cannot be lowered in the polyline inequality: with two remaining candidates on opposite
sides of H on a line, W = 2 and Σκ = 0. Adversarial search confirms that sup(W − 2 − Σκ) = 0.

**Open-arc Fáry/Milnor step.** The refinement argument is correct for open arcs, including at the endpoints.
- Inserting X between consecutive vertices A and B: e_AB is a positive combination of e_AX and e_XB (X ≠ A, B by
  injectivity), so e_AB lies on the closed shorter arc between them. Hence ∠(e_AX, e_AB) + ∠(e_AB, e_XB) = ∠(e_AX, e_XB).
  When e_AX = −e_XB this holds with either arc, both of length π.
- The turning at A and B before insertion is ∠(e_PA, e_AB) + ∠(e_AB, e_BQ). Two triangle inequalities on S¹ bound it by
  ∠(e_PA, e_AX) + ∠(e_AX, e_XB) + ∠(e_XB, e_BQ).
- If A is the first vertex (no P) or B is the last (no Q), drop the corresponding term. The inequality survives, since it
  only needs ∠(e_AB, ·) ≤ ∠(e_AX, e_AB) + ∠(e_AX, ·), etc.
- The chain S_j, …, S_N is inscribed in γ_t in curve order (α order), and its first and last vertices are the arc's
  endpoints. So Σκ_i ≤ sup over inscribed polygons = TC(γ_t).
- For a C² arc, TC = ∫|κ| ds (Milnor/Sullivan).

The hypothesis "no direction in [α_j, α_N] caught by time t" makes ρ ≥ c > 0 on the compact set [α_j, α_N] × [0, t]. So
α ↦ S_α(t) is C^∞ and injective (backward uniqueness), and γ_t is a smooth arc.

**Remark (W_c).** d/ds(t̂·r̂) = κ N·r̂ + sin²φ/ρ, so ∫ sin²φ/ρ ds = [cos φ] − ∫κ(r̂·N) ds. With Prop. 6(2),
L_arc′ = v W_c. Correct.

Numerics (NUMERICAL):
- 20 000 random polylines: identity error ≤ 5·10⁻¹⁵, max(W − sharp bound) = 1·10⁻¹², max(sharp bound − 2 − Σκ) < 0.
- Refinement on random smooth arcs (9 000 insertions) never decreases the turning: max decrease 2·10⁻¹² (rounding).
- Along 78 simulated chain chases, max(W − 2 − Σκ) ≤ −0.21 (v = 0.8; ≤ −0.43 for v ≤ 0.45).
- The chain turning never exceeds that of the common refinement by ~3 000 passive directions of the arc [α_j, α_N]
  (max difference −3.7·10⁻⁵).
- A first version compared against a polygon that omitted the intermediate candidates, which is not a refinement. With
  near-twin pairs closer than the passive grid it reported spurious positives of up to 0.31. This was fixed and rerun.

## 2. Lemma A3.2

∂_tT = (v/ρ)(I − r̂r̂ᵀ)T because H does not depend on α. Write T = |T|(cos φ r̂ + sin φ r̂⊥). Then
(I − r̂r̂ᵀ)T = |T| sin φ r̂⊥, and projecting onto T̂ and T̂⊥ gives ∂_t|T| = (v/ρ) sin²φ|T| and ∂_tτ = (v/ρ) sin φ cos φ.
I re-derived ∂_αΩ from ∂_αρ = |T| cos φ and ∂_αθ = |T| sin φ/ρ, together with the identity
cos φ sin 2φ/2 + cos 2φ sin φ = sin φ(3cos²φ − 1). The ∂_tκ law follows from the quotient rule. All four laws are
correct.

Regularity: the field v(x − H(t))/|x − H(t)| is C^∞ in x and continuous in t for Lipschitz H. So S is C^∞ in α and C¹ in
t, Ω is continuous in (α, t) and C^∞ in α, and ∂_t∂_ατ = ∂_α∂_tτ is legitimate. T ≠ 0 by linear ODE uniqueness, since
T(0) = d(−sin α, cos α) ≠ 0. I also checked the circle with φ = −π/2 (clockwise orientation): κ_t = +v/R² = d(−1/R)/dt.

**G1 (wording).** "None of which is caught on [t1, t2]" should read "on [0, t2]": a direction caught before t1 has no
trajectory on [t1, t2].

Numerics (`laws_fd.py`, NUMERICAL):
- Setup: RK4 in t (dt = 2·10⁻³, 10⁻³, 5·10⁻⁴), 6th-order differences in α (6 001 points), central time difference
  δ = 10⁻⁴. Harry follows a kinked random path or a smooth unit-speed circle. The initial curve is the unit circle or a
  wavy curve with 5 interior critical points of τ. v ∈ {0.1, 0.4, 0.8}.
- Smooth H: relative errors ≤ 2·10⁻⁶ (τ_t, log|T|_t) and ≤ 1.6·10⁻³ (κ_t, ∂_ατ_t; these are limited by second α-derivatives).
- Kinked H: ≤ 1.6·10⁻². RK4 drops to first order across the kinks, and the error does not change with dt.

## 3. Proposition A3.3

On each monotonicity interval of τ the variation is |τ(c_{k+1}) − τ(c_k)|. Since ∂_ατ(c_k) = 0,
d/dt τ(c_k(t), t) = Ω(c_k). This gives TC′ = Σσ_k[Ω(c_{k+1}) − Ω(c_k)], which is +2Ω at maxima, −2Ω at minima and ±Ω at
the ends. With |Ω| ≤ v/(2ρ) this gives the |TC′| bound. Correct.

The hypotheses (finitely many simple critical points, C¹ in t, fixed ends inside a leg) are part of the statement. They
are assumptions, not consequences. Note that the end term at α_j blows up like 1/ρ(α_j) at the end of each leg.

The inflection-creation remark is a correct local computation and is presented as a remark, not a claim.

Numerics (NUMERICAL): finite-difference TC′ against the formula agrees to ≤ 1·10⁻⁴ relative (wavy curve, 5 critical
points) and to 10⁻⁶ (smooth H, circle).

## 4. Lemma A3.4 (main check)

**(a) Continuity.** A candidate is deleted only at the instant it equals H, so K(t) is unchanged at that instant. Between
deletions every point of {H} ∪ R is 1-Lipschitz, so each support value h(θ, ·) is 1-Lipschitz and P = ∫h dθ is
2π-Lipschitz. This holds across leg switches and across both planned and accidental catches.

Numerics: the jump of P across every catch in all simulated chases is ≤ 9·10⁻¹⁶.

**(b) Derivative.** Danskin applies because h(θ, ·) is a max of finitely many functions, each C¹ from the right (H is
affine on a leg, using its right velocity at a switch, and candidates are C¹ while ρ > 0). This gives D⁺h(θ, t) for every
θ. Difference quotients are bounded by 1, so dominated convergence gives P′⁺ = ∫D⁺h.

*Vertex changes cost nothing.* The convergence is pointwise in θ for every θ. A point that is about to become a vertex
(for example, one lying on an edge at time t) is active only at the single edge-normal θ, a null set. So no
"birth/death of vertices" term appears. Off the finitely many edge normals the active point is the unique vertex V with
θ ∈ N_V, and ∫_{N_V} e_θ dθ = 2 sin(ε_V/2) n_V. The candidate terms are 2v sin(ε_V/2)⟨r̂_V, n_V⟩ ≤ vε_V.

*Harry is a vertex.*
- The interior angle of K at H is the opening of the cone spanned by R − H, which is B_H < π.
- The normal cone has opening π − B_H, and its bisector n_H is opposite to the inner bisector d of the tangent cone.
- u points at a point of R, so u lies in the tangent cone at angle x ≤ B_H/2 from d.
- Hence the contribution is 2 cos(B_H/2)(−cos x) ≤ −2cos²(B_H/2) = −(1 + cos B_H).

*Harry lies on an edge but is not a vertex.* Then R contains points on both rays of a line through H, so no sector of
opening < π contains R, and B_H = π by definition. Harry's normal "arc" is a single θ and contributes 0 = −(1 + cos π).

*Harry is interior.* Then B_H = π, again consistent.

*Summing.* Σ_{V≠H} ε_V = 2π − ε_H = π + B_H in every case. The case B_H ≥ π is handled entirely by the convention
B_H := π.

**(c)** P = ∫_0^π w(θ) dθ with w ≤ Σ_edges|⟨edge, e_θ⟩| and ∫_0^π|⟨e, e_θ⟩| dθ = 2|e|, giving P ≤ 2Φ. Also
P ≥ 2 diam K ≥ 2 max ρ_i. Correct, and it holds for any polyline through {H} ∪ R, so it does not depend on the chase.

**N1 (note, not a gap).** B_H(t) is not continuous at catches. Just before a catch the target sits at H in the heading
direction, and its deletion can drop B_H discontinuously. In the Prop. A9 chase at v = 0.1, B_H goes from 2.34 to 0.016.
P is continuous, the bound in (b) is used only almost everywhere, and the jumps are downward. So Theorem A3.5 is
unaffected. My first integrated test, which wrongly took a trapezoid across a catch, flagged this as a spurious "+0.79".
Refining inside the leg gives −0.16 (`integ_debug.py`).

Numerics (NUMERICAL):
- **Static** (`hull_static.py`):
  - 2 800 configurations in 7 families: uniform; half-plane with points within 10⁻³ of both boundary rays (B_H → π);
    opening π ± 10⁻³; points on a circular arc about H; collinear (10⁻⁹ noise); far tiny cluster (B_H ≈ 0); a point
    10⁻⁴ from H.
  - v ∈ {0.02, …, 0.95}, every admissible u (u at each point of R), one-sided difference at steps 10⁻⁶ and 10⁻⁸.
  - Max slack P′⁺ − bound = −6.6·10⁻³.
  - Nelder–Mead maximisation of the slack over positions (60 starts, n = 2–6): −1.4·10⁻².
  - P − 2Φ ≤ 0 and P − 2 max ρ ≥ 0 on 20 000 random sets.
- **Along chases** (`chase_check.py`, exact straight-run map validated against RK4 to 1.5·10⁻¹²):
  - Sets: dyadic N = 8–128; random sets; near-twin sets including the Prop. A9 set. v from 0.05 to 0.8, including the
    initial run [0, t0].
  - Pointwise one-sided difference at 10⁻⁷τ and the integrated (within-leg trapezoid) check: both ≤ 0 everywhere. The
    numbers are in §6.
  - The bound is asymptotically sharp. For dyadic sets the worst slack is exactly the t = 0 value
    2v(N sin(π/N) − π) ≈ −vπ³/(3N²): H is at the centre of the regular N-gon, B_H = π, and r̂_V = n_V. This gives
    −3.16·10⁻⁵ at N = 128, v = 0.05, matching the simulation.
  - Legs shorter than ~10⁻⁸ (near-twin pairs 10⁻⁹ apart) are below the rounding floor of a finite difference of P. They
    are skipped in the pointwise test (reported count) and covered by the static "near_H" family.

## 5. Theorem A3.5

**Ordered phase [t0, t_f].** This is identical to the paper's Theorem A23. Lemma A3(a) gives W ≤ A = β_{N(t)} ∈ [0, π].
Lemma B1 gives Ψ′ ≤ −[(1 − λ)(1 − v) + λ(1 − cos x) − vx] ≤ −m(v, λ), with only downward jumps. So
Ψ(t_f) ≤ Ψ(t0) − m(t_f − t0) and Ψ(t0) ≤ Φ(t0) ≤ 2πd/(1 − v).

**End phase [t_f, T_end).**
- (E_H, γ) gives B_H ≤ γ.
- c_H > 0 forces γ < π, since c_H(π) = −2πv.
- The right-hand side of (b) has B-derivative sin B + v > 0, so P′ ≤ −c_H almost everywhere.
- P is Lipschitz with P(T_end) = 0, hence T_end − t_f ≤ P(t_f)/c_H ≤ 2Φ(t_f)/c_H ≤ 2Ψ(t_f)/((1 − λ)c_H).

**Combination.** Since Ψ(t0) ≥ Ψ(t_f) and μ ≤ m, μ ≤ (1 − λ)c_H/2:
(Ψ0 − Ψf)/m + 2Ψf/((1 − λ)c_H) ≤ (Ψ0 − Ψf)/μ + Ψf/μ = Ψ0/μ.
Taking the infimum over admissible λ yields T. The sup in μ need not be attained, but the bound holds for every λ, so
it holds at the sup. The H_k stay put after their last catch and are 1-Lipschitz on [0, T], so Lemma 4 applies. The
λ = 0 corollary uses m(v, 0) = 1 − v(1 + π). Correct.

**N2 (presentation).** Because u points at the target, which is a remaining candidate, (E_H, γ) implies
|β_i| ≤ γ for all i, i.e. (E_γ) with the same γ. Conversely, (E_γ) implies (E_H, 2γ). Two consequences:
- For v ≥ v× = 0.2928 (the root of γ_H(v) = arccos v), every admissible (E_H, γ) already gives an admissible (E_γ), and
  Theorem A23(i) applies.
- In that range A3.5 can only improve the time constant, and it does not: under the same γ,
  T_A23(i) = 48.0, 59.0, 91.8, 312 against T_A3.5 = 70.3, 122.5, 242.5, 775 at v = 0.3, 0.35, 0.4, 0.45.
- At v = 0.1 and 0.2 the order reverses (A3.5: 13.7, 30.4 against A23(i): 17.4, 35.9).

The sentence "for v ≳ 0.27 the cone condition is the weaker requirement" should be replaced by this exact implication.
The theorem is valid as stated.

**Chase consistency** (NUMERICAL, a sanity check on the logic, not on (E_H)):
- In every simulated chase that lost order and had c_H > 0 for γ = measured sup B_H on [t_f, T_end):
  - P(t) ≤ P(t_f) − c_H(t − t_f) held (max violation 0);
  - (T_end − t_f)/(P(t_f)/c_H) ≤ 1;
  - T_end ≤ the stated T.
- (E_H) fails for the Prop. A9 set and for random near-twin sets: sup B_H ≈ 2.97–3.13, c_H < 0. So, like (E_γ), it can
  hold at most for structured families. The claims file restricts it to the chain chase of the D_k.
- Dyadic chases with N ≤ 128 never lost order for v ≤ 0.45 in my runs, which is consistent with the paper's remark that
  the end phase is reached only slowly as N → ∞. I did not reproduce the "measured sup B_H after t_f" row; it needs deep
  dyadic chases, which are outside this referee's scope.

**Tables.**
- γ_H(v) agrees to 3 decimals at every v. π − γ_H ~ 2√(πv) as v → 0 (expansion 1 − cos δ ≈ δ²/2 = 2πv).
- The T row agrees: 13.7, 30.4 (claimed 30.5), 41.6, 70.3, 122.5, 242.5 (242.6), 774.6 (775), 1713 (1716).
- v1 = 0.47475264 (my grid gives 0.4747526374; the paper's 0.47475263829 agrees to grid accuracy).

## 6. Reproduction (`cd code/referee/RA3`, `$env:OPENBLAS_NUM_THREADS=1`)

| Command | Checks |
|---|---|
| `python map_check.py` | exact straight-run map against RK4 |
| `python lemma31_random.py` | Lemma A3.1 identity, bounds, adversarial, refinement |
| `python laws_fd.py` (output `laws_fd.out`) | Lemma A3.2, Prop. A3.3 |
| `python hull_static.py 1` | Lemma A3.4 static and adversarial |
| `python run_all.py > chase_check.out` | Lemmas A3.1/A3.4 and Theorem A3.5 along chases; one line per chase. I ran it serially for v ≤ 0.4, and ran the v = 0.45/0.6/0.8 jobs and the twin reruns with `run_part.py chase_part2.out fam:v:p ...` and `extra_reruns.out` |
| `python summarize.py` | aggregates all chase lines (below) |
| `python integ_debug.py`, `python fd_debug.py twin 0.05 12` | the two numerical artefacts explained above (trapezoid across a catch; finite differences below the rounding floor on 10⁻⁷-long legs) |
| `python table_check.py` | v1, γ_H, T tables, comparison with A23(i) |

**Chase summary** (`summarize.py`, NUMERICAL).
- Coverage: 78 chain chases, using the exact map with 45 samples per leg (40 uniform plus 5 at 1 − 10⁻²…10⁻⁶ of the
  leg).
  - Dyadic N = 8–128 at v = 0.05, 0.1, 0.2, 0.3, 0.4, 0.45.
  - Dyadic N = 8–32 at v = 0.6, 0.8.
  - Random N = 6–32.
  - Near-twin sets, including Prop. A9.
- Lemma A3.4:
  - Pointwise max(P′⁺ − bound) = −3.2·10⁻⁵.
  - Integrated within-leg max = −5.0·10⁻⁵.
  - max(P − 2Φ) = 0 and min(P − 2 max ρ) = 0 (attained in the one-candidate case).
  - Max |jump of P| at a catch = 3.6·10⁻¹⁵.
  - 136 samples on legs shorter than 10⁻⁸ were skipped in the pointwise test.
- Lemma A3.1: max(W − 2 − Σκ) = −0.21.
- Theorem A3.5:
  - 9 chases lost order with c_H > 0 at γ = measured sup B_H (random sets; dyadic N = 64, 128 at v = 0.3–0.45, where
    sup B_H after t_f is 0.03–0.11).
  - In all of them: the linear decay P(t) ≤ P(t_f) − c_H(t − t_f) holds with zero violation;
    max (T_end − t_f)/(P(t_f)/c_H) = 0.79; max T_end/T = 0.76.
- Every sample was consistent with the claims. The only positive excursions found were the three test-harness artefacts
  described above, each resolved by refinement.
