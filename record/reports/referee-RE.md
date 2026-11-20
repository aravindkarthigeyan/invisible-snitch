# Referee report RE: claims E1–E8', E3', E5, E7, bisection (from `referee/E-claims.md`)

Referee: independent adversarial check. I read only BRIEF.md, `paper/main.tex` §1–4 and `referee/E-claims.md`, and did not read `reports/E-1.md` or `code/E/`.
Scripts are in `code/referee/RE/`. Each one runs as `python <script>` from that directory, and its output is saved next to it as `*_output.txt`.
Formulation: the same as the brief (|H'| ≤ 1, H(0) = 0, ε = 0 unless stated). Nothing was strengthened.

## Summary of verdicts

| Claim | Verdict | One-line reason |
|---|---|---|
| Lemma E1 | **OK** (wording fix) | Identity is correct. The hypothesis should read "ρ_P, ρ_Q > 0 on [0, t*)". "Forward uniqueness" should be "uniqueness (backwards in time)". |
| Corollary E2 | **OK** | Correct as stated, for speed ≤ 1. |
| Theorem E3 (a)–(d) | **OK** | Every regularity point checks out (details below). Numerically the Lipschitz ratio is ≤ 1 on all paths tested, with equality on straight runs. |
| Corollary E4a | **OK** | It is just (P0); E3 is not needed. |
| Corollary E4b | **OK as a conditional** | The hypothesis is stated honestly. Say "for a.e. τ" and "continuous extension from the uncaught side". |
| Theorem E5 | **OK** (two comparison remarks need relabelling) | Every step verified symbolically and numerically. It holds for speed ≤ 1, and it needs only a *dense* set of directions caught by T. |
| E3' | **OK** | Correct. |
| Corollary (ε > 0 lower bound) | **GAP (minor, fixed below)** | The hypothesis "every direction is seen by T" is missing from the statement, and the arc-containment step needs one line. |
| Proposition E7 | **OK** | Equivariance and the single-spiral catch set are confirmed to 1e-9. |
| Lemma E8 / Cor. E8' | **OK for unit-speed straight runs** (statement must say "unit speed") | E8 is **false** for a slower straight run (counterexample below). E8 is sharp (attained as β₀ → 0). |
| Bisection no-go | **OK** | Correct, and it holds for any order within each level. |

There are no ERRORs in the claims as they apply to the paper's setting, where "straight run" means unit speed.

---

## Lemma E1. OK

*Algebra.* S_P − S_Q = r_P − r_Q, and (r̂_P − r̂_Q)·(ρ_P r̂_P − ρ_Q r̂_Q) = ρ_P + ρ_Q − (ρ_P + ρ_Q)cos ψ. This is correct, and H' does not enter.

*Fix (wording).*
- The fact used is uniqueness for the IVP solved backwards from time t. The field is locally Lipschitz in S near S ≠ H(t), so this holds. It is not "forward uniqueness".
- It needs ρ_P, ρ_Q > 0 on all of [0, t], not only on I. After a capture the continuation S_P is not unique, so "S_P" is not even defined.
- State the lemma for I = [0, t*) with both candidates uncaught on I. The statement "stays ≥ |P − Q|" also needs I to start at 0.
- With that reading the proof is complete. f is C¹ because S_P and S_Q are C¹: their right-hand sides are continuous in t, since H is continuous.

*Numerics* (`t1_chase_E1E2E3.py`, `t2_catchcurve.py`).
- Pairwise distances were checked along exact discrete chases (v = 0.1–0.5, N ≤ 256) and along reversed-hound families on 7 path types × v ∈ {0.2, 0.5, 0.8}. They never decreased by more than 1e-14, which is rounding level.

## Corollary E2. OK

- ρ_Q(τ(P)) = |S_Q − S_P|(τ(P)) ≥ |P − Q| > 0 by E1 and continuity.
- Then (P0) holds on [τ(P), τ(Q)), where ρ_Q > 0.
- Only |H'| ≤ 1 is used, so it holds for speed ≤ 1.
- The version from start time t is also correct, since t ≤ τ(P) ≤ τ(Q) and f is monotone.
- Numerically the ratio |S_P(t) − S_Q(t)| / ((1 − v)|Δτ|) is < 1 for every pair at every leg start of the chase (table below).

## Theorem E3. OK (all parts)

Checked step by step, with the specific questions from the brief answered.

1. **Catch map well defined?** Yes.
   - E2 (from time t) makes τ injective on K_t.
   - If "uncaught at t" allows τ(P) = t, then X_t(P) = H(t) = c(t), which is consistent.
2. **Step 2.** |X_t(P) − X_t(Q)| ≤ f(τ(P)) = ρ_Q(τ(P)) ≤ (1 − v)(τ(Q) − τ(P)). This is correct: E1 gives monotonicity on [t, τ(P)), then continuity, then (P0).
3. **Step 3** is (P0). It is correct.
4. **Extension with the same constant?** Yes.
   - Extension to the closure of E holds by completeness of ℝ².
   - On a complementary gap (a, b), linear interpolation has slope |c(b) − c(a)|/(b − a) ≤ 1 − v.
   - For x < y not in the same gap, let b₁ be the right end of x's gap (or x itself) and a₂ the left end of y's gap (or y). Then |c(x) − c(y)| ≤ (1 − v)[(b₁ − x) + (a₂ − b₁) + (y − a₂)] = (1 − v)(y − x).
   - "Constant after the last point" is also fine. There is no first-point issue, since t ∈ E.
5. **Is the set of capture times closed?** This is **not needed**, because the proof extends to the closure.
   - In general the closure may contain times τ* that are not first-capture times. If P_n → P* with τ(P_n) → τ*, then P* is caught at some time ≤ τ*, possibly earlier.
   - At such a τ*, c(τ*) is still lim X_t(P_n), which is harmless.
6. **(a)** H¹(γ([a, b])) ≤ length(γ) is standard. **(b)** Take a countable union over T = n; each piece has finite H¹, so the union has Lebesgue measure 0. In fact the whole caught set lies on one locally Lipschitz curve c₀ : [0, ∞) → ℝ². This is correct and is a genuine generalisation of Prop 8.
7. **(c)**
   - c_t([t, T]) is compact, so it contains the closure of the uncaught positions. This gives ℓ_t ≤ length(c_t) ≤ (1 − v)(T − t).
   - Pre-contact refinement: {s : c_t(s) ∈ Γ(t)} is closed and nonempty, so a first time t' exists. Points of Γ(t) are not visited before t', so Γ(t) ⊂ c_t([t', T]).
   - length(c_t|[t,t']) ≥ |c_t(t') − H(t)| ≥ ρ_min, and length(c_t|[t',T]) ≥ H¹(Γ(t)) = L(t).
   - Γ(t) is injective (backward uniqueness) and C¹ with |∂_αS| ≥ d > 0, because |∂_αS| is non-decreasing by the variational equation. So H¹ = ∫|∂_αS| by the area formula.
   - On the brief's question: the proof does **not** need the statement "a connected set containing a Jordan curve of length L and a point at distance δ has H¹ ≥ L + δ". That statement is nevertheless true. f = dist(·, Γ) is 1-Lipschitz, and f(K) ⊇ [0, δ] by connectedness, so H¹(K \ Γ) ≥ H¹(f(K \ Γ)) ≥ δ, and H¹(K ∩ Γ) = L.
8. **(d)** At t = 0, ρ_min = d and L = 2πd. Correct.

*Numerics.*
- **Exact discrete chase** (`t1_chase_E1E2E3.py`). It uses exact straight steps via the (C, h) integrals; the self-test against an rtol 1e-12 ODE agrees to 5e-13 (`t0_selftest.py`).
  - At every leg start t and for every pair of uncaught candidates, I computed the Lipschitz ratio |X_t(P) − X_t(Q)| / ((1 − v)|τ_P − τ_Q|) and the start ratio |X_t(P) − H(t)| / ((1 − v)(τ_P − t)).
  - Max (Lipschitz ratio − 1) ranged from −1e-2 (N = 16) to −9e-8 (N = 256), all < 0. Max (start ratio − 1) ≤ 2e-14, which is equality: the current target lies on the forward ray.
- **Arbitrary paths via reversed hounds** (`t2_catchcurve.py`).
  - For each release time τ, the unique candidate caught at τ is integrated backwards from H(τ − δ) + (s − v)δ û (rtol 1e-11). Any trajectory that hits Harry going backwards is discarded, because it was caught earlier.
  - This gives the catch map on 200 release times for these paths: straight, zigzag (±60°, legs 0.15), back-and-forth, circle R = 0.6, outward spiral, 3 random piecewise paths with speeds in [0.2, 1], and 3 random unit-speed piecewise paths. Each was run for v = 0.2, 0.5, 0.8, with snapshot times t ∈ {0, …, 6}.
  - The full table is at the end of this report. Every max (Lipschitz ratio − 1) is ≤ 4e-12, which is rounding level. Equality is attained on straight pieces.

## Corollary E4. E4a OK; E4b OK as a labelled conditional

- **E4a.** S_{α₀}(τ) = H(τ) and |S_{α₁}(τ) − H(τ)| = ρ_{α₁}(τ) ≤ (1 − v)(τ' − τ) by (P0) alone. Citing "E3 started at τ" is slightly off, because α₀ is not uncaught at τ, but the claim is correct.
- **E4b.** The regularity hypothesis is stated and labelled honestly. Two small precision fixes:
  1. It is needed for a.e. τ, which is what the integration uses. α is automatically Lipschitz: by E2, |α(τ') − α(τ)| ≲ (1 − v)|τ' − τ|/d locally, so "absolutely continuous" is free.
  2. The extension is from the uncaught side α > α(τ); the caught side has no S. α' should then be the right derivative.
  3. Also, α(T) = 2π should be read as a limit. Direction 0 ≡ 2π is caught once, at t₀.
- The "Reading" paragraph is heuristic and is labelled as such. Fine.

## Theorem E5. OK

*Step-by-step check.*
1. (P0) gives ρ ≥ d − (1 − v)t, so no capture occurs before t₁. Correct. It uses only |H'| ≤ 1.
2. Winding: (α, s) ↦ S − H is a homotopy in ℝ² \ {0}. Correct.
3. Variational equation: ∂_r(r/|r|) = (I − r̂r̂ᵀ)/ρ and ∂_α r = ∂_α S, so ∂_t|J| = (v/ρ) sin²φ |J|.
   - The integrand is jointly continuous for t < t₁ (Hartman V.3.1; H is only needed to be continuous). So L ∈ C¹, even for merely Lipschitz H.
   - |J| ≥ d > 0, so |J| is differentiable.
4. ρ ∂_αβ = J · r̂^⊥, so ∫|∂_αβ| ≥ |∫∂_αβ| = 2π. Correct.
5. **Cauchy–Schwarz with the right measure.** The weight is w = |J|/ρ dα, and (∫|sin φ| w)² ≤ (∫ sin²φ w)(∫ w). The two factors are exactly L'/v and ≤ L/ρ_min. So (L²)' = 2LL' ≥ 8π²vρ_min. Correct.
6. ∫₀^{t₁}(d − (1 − v)s) ds = d²/(2(1 − v)), so L(t₁⁻)² ≥ 4π²d² + 4π²vd²/(1 − v) = 4π²d²/(1 − v). Correct.
7. t + (d − (1 − v)t)/(1 − v) = d/(1 − v), then let t ↑ t₁. Correct.

*Questions from the brief.*
- **Does it need every direction to be caught?** It needs Γ(t) ⊂ c_t([t, T]). Since the image is closed, it suffices that a dense set of directions is caught by T. This is a slight strengthening, and it is worth stating.
- **Does it hold for any path?** It holds for any path that catches (a dense set of) every direction by T. For other paths the statement is vacuous.
- **Speed ≤ 1 or = 1?** It holds for ≤ 1, which is the right class given the compactness lemma.

*Numerics* (`t3_E5_stretch.py`).
- Setup: M = 1024 candidates plus the variational equation, RK4 with dt = min(2e-3, 0.02ρ_min/v), up to 0.995 t₁.
- Paths: stationary, straight, slow straight (speed 0.4), circle, outward spiral, zigzag, back-and-forth, random with variable speed, random unit speed. Speeds: v = 0.2, 0.5, 0.8.
- The exact L' formula agrees with a finite difference of L to relative error ≤ 1e-3 (worst case: the straight run, where the integrand is peaked).

| quantity, minimum over all t ∈ (0, 0.995 t₁] | worst value over 27 runs |
|---|---|
| (L²)' / (8π² v ρ_min) − 1 | −4e-16 (stationary Harry: **exact equality**, Γ a circle centred on Harry) |
| L(t)² / [4π²d² + 8π²v(dt − (1 − v)t²/2)] − 1 | −3.5e-8 (clustered grid, quadrature error); otherwise ≥ +8e-7 |
| ∫\|∂_αβ\| / 2π − 1 | −7e-16 |
| winding number | always 1 |

- Equality in step 5 holds for the stationary Harry, so that inequality cannot be improved without using ρ > ρ_min.
- For the straight run at large v, |J| at α = 0 grows like (ρ/d)^{−v/(1−v)}. A uniform α-grid then overestimates L badly near t₁ (it gave 1e7 at v = 0.8). I used a grid clustered at α = 0 (p = 7, M = 4096) for that case.
- L(0.995 t₁) for the straight run: 7.68 / 11.70 / 26.8 for v = 0.2 / 0.5 / 0.8. The E5 floor 2πd/√(1 − v) is 7.02 / 8.89 / 14.05, and the Prop 3 cap 2π(1 + vt) is 7.85 / 12.5 / 31.3. So the bound is consistent and not tight for the straight run.
- End-to-end sanity check: exact discrete chase times T_N exceed the E5 bound for every v and N tested.

| v | E5 bound | T_N (N = 16 / 64 / 256) | greedy ε-sweep (ε = 0.05), my sim | brief's sweep |
|---|---|---|---|---|
| 0.1 | 8.47 | 8.97 / 9.45 / 9.59 | – | – |
| 0.2 | 10.03 | 12.13 / 12.87 / 13.11 | 12.98 | 13.2 |
| 0.35 | 13.53 | 20.6 / 22.1 / 22.8 | – | – |
| 0.5 | 19.77 | 40.3 / 43.5 / 45.5 | 45.8 | 48.6 |

My greedy-sweep simulator reproduces the brief's §3 sweep times to within the ε-dependence (ε = 0.05 here, versus the brief's ε → 0).

*The "Comparisons" paragraph.*
- **Correct:**
  - E5 > (1 + 2π)d/(1 − v), because (1 − v)^{3/2} < 1 − v. Numerically the minimum gap on (0, 1) is > 0.
  - E5 < T_B on (0, 1/(1 + π)), because √(1 − v) ≥ 1 − v ≥ 1 − (1 + π)v. Numerically the minimum gap is 2.3e-3 > 0.
  - The first-order coefficients are correct. Central differences give dT_B/dv(0) = 33.305579 = 1 + 4π + 2π², and dE5/dv(0) = 10.424778 = 1 + 3π.
- **Relabel 1:** "So Theorem B would be sharp to leading order" is technically true but misleading.
  - Order-0 agreement is automatic for *every* bound: at v = 0 the exact answer is (1 + 2π)d.
  - At the first non-trivial order the coefficients differ by a factor of 3.2 (33.3 versus 10.4). Suggested text: "Both equal (1 + 2π)d at v = 0. At first order in v they differ: 33.3 vd versus 10.4 vd."
- **Relabel 2:** "The lower-bound exponent 3/2 and this exponent 3 bracket the truth" is not proved.
  - The 6d/(1 − v)³ fit is NUMERICAL. It comes from an ε > 0 greedy sweep (my check: 11.7 / 17.5 / 27.8 / 48.0 / 93.7 / 222 versus 13.2 / 19.1 / 29.2 / 48.6 / 92 / 230).
  - The sweep is not shown to give an exact-capture (ε = 0) path. Its ε → 0 limit is not controlled, and the brief notes exact-contact instability for v > 0.5.
  - So the sweep is not a proved upper bound. Label the bracketing as CONJECTURE.

## E3'. OK

- E1 applies on [0, τ(P)], where ρ_P ≥ ε > 0 and ρ_Q > ε.
- Then |P − Q| ≤ |S_P − S_Q|(τ_P) ≤ ε + ρ_Q(τ_P) ≤ 2ε + (1 − v)(τ_Q − τ_P). Correct.
- Numerically (`t4_E3prime_E8_bisect.py`, greedy sweep, all 720 candidates sighted, v ∈ {0.2, 0.5}, ε ∈ {0.05, 0.2}), max |P − Q| / ((1 − v)|Δτ| + 2ε) is 0.42–0.72. The first sighting equals (d − ε)/(1 − v) to 1e-13.

## Corollary (ε > 0 lower bound). GAP (minor), fix written out

*Fix.*
- Add to the statement: "If every direction is seen by time T, then …".
- Step 3 needs one line. Let θ₀ = 2 arcsin(D/(2d)). D < d gives θ₀ < π/3. Fix a point p of the set; every other point is within angular distance θ₀ of p, so its offset from p lies in (−θ₀, θ₀). Let a ≤ 0 ≤ b be the extreme offsets. The angular distance between those two points is min(b − a, 2π − (b − a)) = b − a, since b − a < 2π/3. So b − a ≤ θ₀, and the set lies in an arc of length θ₀.
- Step 2 uses k = ⌈(T − t_ε)/δ⌉ (or 1) ≤ (T − t_ε)/δ + 1. That is fine.
- The limit ε → 0 then δ → 0 does give (1 + 2π)d/(1 − v), since δπ/((1 − v)δ/(2d)) = 2πd/(1 − v).

With the hypothesis added, the corollary is PROVED.

## Proposition E7. OK

- H(λt) = λ^{1 + ib/a} H(t) = μ_c H(t), and |H'| = |a + ib| = 1.
- The scaling and rotation invariance of the Snitch ODE is verified algebraically: |μ| = λ.
- Uniqueness per time follows from E2.
- On the circle, |μ_c P₁| = e^{ac}|P₁| is strictly monotone.

*Numerics* (`t5_spiral_E7.py`), for (a, b) ∈ {(0.6, 0.8), (0.3, 0.954), (0.9, −0.436)} and v ∈ {0.2, 0.5}:
- The ODE residual of μ_c S(t/λ) is 5e-16.
- The caught point P(τ), from backward hounds over τ ∈ [1, 4], satisfies P(τ) = (τ/τ₁)^{1 + ib/a} P(τ₁) to ≤ 1.5e-9. |P(τ)|/τ is constant, so exactly one radius d is met.
- For (a, b, v) = (0.3, 0.954, 0.5), every backward hound hits Harry. By equivariance the spiral then catches no point at all other than the origin. This is consistent with "at most one".
- The "autonomous-frame" bullets and the "shape Γ then spiral" remark are assessments, correctly not labelled as theorems.

## Lemma E8 and Corollary E8'. OK for unit-speed straight runs; the statement must say so

- The proof uses h' = −(1 − v²), which is Prop 1 and needs **unit** speed. For a straight run at speed s, h' = v(1 − s) r̂·u + v² − s is not constant.
- **Counterexample** for a slower run (`t6_E8_speed.py`): v = 0.5, ρ₀ = 1, τ = 10.
  - Harry stationary: ρ(τ) = 6 < bound 12.
  - Speed 0.3, β₀ = π/2: ρ = 7.63 < 12.
  - Speed 0.6, β₀ = π/2: ρ = 10.56 < 12.
- *Fix:* write "runs straight at unit speed". That is the paper's meaning of "straight run" in Prop 1, so within the paper the lemma is correct.
- *Algebra check.* The steps h(0) ≤ (1 + v)ρ₀, h ≥ −(1 − v)ρ and ρ(τ) ≥ −h(τ)/(1 − v) are correct.
- **Sharp:** as β₀ → 0⁺ with τ beyond the pass time, ρ(τ) equals the bound to 1e-6 (`t0b_nearray.py`).
- On 200,000 random and adversarial runs (β₀ near 0 and near π, v ∈ {0.1, 0.5, 0.9}), the minimum slack is −2e-14, which is rounding level.
- *Numerical note:* my first version had a spurious violation of −0.9. It came from float resolution of β near π and was fixed by bisecting on logit(β/π) with π − β carried separately.
- **E8'** follows from E8 and (P0). If the E8 bound is negative, the claim still holds, because then τ(Q) ≥ t + τ is larger than the right-hand side. Numerically the minimum slack is −2e-14. It needs the same unit-speed proviso for the straight leg; after the leg the path is arbitrary with speed ≤ 1.

## Bisection no-go. OK

- Telescoping E2 along the catch order gives τ_last ≥ (d + Σ|P_{i+1} − P_i|)/(1 − v).
- Within level j + 1 (j ≥ 1) the 2^j new points are spaced 2π/2^j apart, so any route through them has length ≥ (2^j − 1)·2d sin(π/2^j) ≥ 2d. Jumps between levels are ≥ 0.
- So T_N ≥ (d + 2d(k − 1))/(1 − v) → ∞.
- Numerically (`t4`): for k = 4, 8, 12 the explicit polyline is 18.0, 43.4, 68.6, against within-level sums 11.6, 35.9, 61.0 and 2d(k − 1) = 6, 14, 22. The last term / 2πd → 0.99997.
- Note: the argument uses only the minimum spacing, so it holds for **any** order within a level, not only increasing angle.
- Scope: it excludes strategies that catch the N = 2^k directions level by level. It says nothing about other orders.

## Catch-curve table (`t2_output.txt`)

Columns:
- releases with first capture / sampled;
- max (Lipschitz ratio) − 1, where the Lipschitz ratio is |X_t(P) − X_t(Q)| / ((1 − v)|τ_P − τ_Q|);
- max (start ratio) − 1;
- max decrease of a pairwise distance (E1).

Outputs are in `t2_output.txt`, `t2b_output.txt` (random paths) and `t2c_output.txt` (spiral, v = 0.8).

| path | v = 0.2 | v = 0.5 | v = 0.8 |
|---|---|---|---|
| straight | +5e-14 | +9e-14 | +9e-13 |
| zigzag | +1e-14 | +2e-14 | +6e-14 |
| back-and-forth (11, 9, 9 of 200 first captures) | +2e-15 | +6e-15 | +2e-14 |
| circle | −1.1e-4 | −1.0e-4 | −6.6e-5 |
| outward spiral | −1.0e-2 | −1.6e-2 | −4.0e-2 |
| random, speed in [0.2, 1] (3 seeds) | −3.3e-2 … −1.1e-1 | −5.2e-2 … −3.0e-1 | ≤ 2 captures |
| random, unit speed (3 seeds) | ≤ +1.0e-12 | ≤ +1.0e-12 | ≤ +4.0e-12 |

The entries are max (Lipschitz ratio − 1).
- No run exceeds 1 by more than rounding error (≤ 4e-12).
- Equality holds exactly on straight-run pieces: the ratio is 1 when both candidates are caught on the same straight piece.
- The start ratio behaves the same way.
- E1: no pairwise distance decreased by more than 3e-16.
- For back-and-forth paths most release times are re-captures, as expected, so they are discarded.
- Releases at speed ≤ v + 0.02 are skipped, since no capture is possible at speed ≤ v.

## Most useful next steps
1. Restate E5 as "if a dense set of directions is caught by T". This also makes E5 combine directly with the compactness lemma.
2. Improve E5 by not discarding ρ: the Cauchy–Schwarz step is tight only when ρ ≡ ρ_min (stationary Harry). A joint optimisation of the trade-off between ρ_min and L in step 7 would sharpen the 3/2 exponent.
