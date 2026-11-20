# Referee report RD2a: Theorem D2, Claims 1-5, Corollary D2.1 (referee/D2-claims.md)

Referee: independent, adversarial. I read only `referee/D2-claims.md`. I did not read reports/D2-1.md, code/D2/, or any other referee report.
Independent code: `code/referee/D2a/constants.py` (mpmath constant checks) and `code/referee/D2a/simulate_W.py` (simulation of construction W),
plus the logs `code/referee/D2a/run2.log` and `code/referee/D2a/run3.log` (the ε=0.001 run, N=6000, dtfrac 0.25).
Status: all verdicts and all simulations are final.

## Summary of verdicts

| Item | Verdict |
|---|---|
| Claim 1 (field F) | OK |
| Claim 2 (virtual candidates) (a)-(d) | OK (one cosmetic remark) |
| Claim 3 (local Lipschitz implies Lipschitz) | OK |
| Construction W | OK with fixes (two wording fixes: the degenerate connector and the domain of max) |
| Claim 4 | OK |
| Claim 5 (bootstrap, J*, time bound) | OK |
| Theorem D2 | OK with fixes (one rounding goes the wrong way; the conclusion is unaffected) |
| Corollary D2.1 | OK |
| "Limit-of-method remark" | NOT PRESENT in referee/D2-claims.md, so there was nothing to referee |

No GAP and nothing FALSE found.

## Problem fidelity

- Harry's path P depends only on (v, ε) and the d-scaling. Every object in W (the virtual trajectories S̃_φ, the fronts Γ_j, the cut points a_j, and the connector directions) comes from P on earlier times, so P is fixed in advance and does not depend on α. The virtual system S̃' = vF(S̃ − P) is non-anticipating and has unique solutions (the RHS is continuous in t and (v/ε)-Lipschitz in S), so the recursive definition is legitimate.
- Speed ≤ 1:
  - A walk is an arclength parametrisation of the frozen curve Γ_j, so |P(τ'_j+s_1) − P(τ'_j+s_2)| ≤ |σ_j-length between them| = |s_1 − s_2|.
  - A connector is a unit-speed segment.
  - Junctions: P(τ'_j) = Γ_j(a_j); the walk ends at Γ_j(a_{j+1}) = S̃_{a_{j+1}}(τ'_j); the connector ends at S̃_{a_{j+1}}(τ'_{j+1}) = Γ_{j+1}(a_{j+1}). So P is continuous.
  - Numerically the maximum |ΔP|/Δt is 1.000000 in every run.
- "Seen" means ≤ ε, and the proof uses ≤ ε throughout. No strengthening or weakening of the problem was found.

## Claim 1: OK
- (a) Firm non-expansiveness of the projection onto a closed convex set gives monotonicity and 1-Lipschitz for π_ε, hence ε^{-1}-Lipschitz for F. Also |F| ≤ 1.
- (b) If min(|x|, |y|) ≤ ε, part (a) gives the bound. Otherwise the identity |x−y|² − |x||y| |x̂ − ŷ|² = (|x|−|y|)² is correct (expand |x̂−ŷ|² = 2 − 2x·y/(|x||y|)).

## Claim 2: OK
- (a) Global existence and uniqueness, and the Gronwall bound with D(0) = χ ≤ |θ−φ|, are correct.
- (b) d/dt|S̃_θ − S̃_φ|² = 2v(F(x)−F(y))·(x−y) ≥ 0 is correct, since x − y = S̃_θ − S̃_φ (P cancels).
- (c) Virtual equals real up to the first ε-contact. This is checked carefully:
  - t0 > 0 because ρ(0) = 1 > ε.
  - On [0, t0], ρ ≥ ε. Where |x| = ε, F(x) = x/|x|, so S̃ solves the true ODE while staying at distance ≥ ε > 0 from P.
  - The true ODE has RHS continuous in t and locally Lipschitz in S on the open set {S ≠ P(t)}, so the solution is unique while it stays in that set and S_θ = S̃_θ on [0, t0].
  - The real candidate cannot hit P before ρ reaches ε (continuity), so "defined only while |S−H| > 0" causes no problem.
  - At t0, ρ = ε, which counts as seen. Correct.
- (d) The a.e. derivative bound D' ≤ v|F(y)−F(x)| ≤ vD/max(ε, ρ_θ − D) is correct: it uses Claim 1b with min(|x|, |y|) ≥ ρ_θ − D. Gronwall on log D is fine because D > 0 by (b). As φ → θ, D → 0 uniformly on [0, t] by (a); the integrand is bounded by 1/ε, so dominated convergence applies. The stretch bound exp(vJ_θ(t)) is correct.
- Cosmetic remark: in (d), "φ ≠ θ (mod 2π)" should be read with φ, θ real and |φ − θ| the real difference. This is harmless because D(0) = χ ≤ |φ−θ|.

## Claim 3: OK
This is the standard continuation argument. The set of admissible b contains a and is closed by continuity. The local estimate at b* extends it past b*. One-sided limsup at the endpoints is sufficient.

## Construction W: OK with fixes
- Connector 1:
  - ρ_0' = −1 + v·min(1, ρ_0/ε) ≤ −(1−v) is correct.
  - The exact meeting time is (1−ε)/(1−v) + ℓ·log(ℓ/(ℓ−ε)) ≤ 1/(1−v). This was checked analytically and numerically: τ'_1 = 1.0078 against the bound 1.0078 at ε = 0.01, and the closing distance is about 1e-9.
- Walks:
  - Γ_j is Lipschitz by Claim 2a, so σ_j is finite and continuous.
  - a_{j+1} = max{σ_j ≤ ℓ} exists, and w_j = ℓ for a non-final walk. P is well defined because Γ_j is constant on level sets of σ_j.
- Connectors:
  - The collinear ansatz is correct. S̃ moves along +u at speed v·min(1, ρ/ε), Harry moves at speed 1 along +u, and the transverse components stay 0, so by uniqueness this is the motion.
  - Since ρ ≤ ε, ρ' = −1 + vρ/ε ≤ −(1−v). The exact duration is ℓ·log(ℓ/(ℓ−ρ_0)) ≤ ε/(1−v). In the simulation the closing mismatch is below 1e-6·ε at every connector.
- **Fix 1 (degenerate connector).** If ρ_{a_{j+1}}(τ_{j+1}) = 0, then u is undefined. Add this text: "If ρ_{a_{j+1}}(τ_{j+1}) = 0 the connector is empty: τ'_{j+1} := τ_{j+1}, c_{j+1} := 0."
- **Fix 2 (domain of max).** In Claim 4(b), write "θ*(s) := max{φ ∈ [a_j, 2π] : σ_j(φ) = s − τ'_j}". The domain is implicit in the current text.

## Claim 4: OK
- (a) This is the key point. At s_φ, P = Γ_j(φ) = S̃_φ(τ'_j), and S̃_φ moves at speed ≤ v during [τ'_j, s_φ], whose length is σ_j(φ) ≤ ℓ. So ρ_φ(s_φ) ≤ vℓ = ε, and Claim 2c turns this into a real sighting.
  - The informal phrase "each candidate he passes has moved at most ε since the front was frozen" is exactly this inequality.
  - It holds for every φ in [a_j, a_{j+1}], including φ where σ_j is locally constant: those points share the same Γ_j value, so P really visits it.
- (c) The intervals [a_j, a_{j+1}] tile [0, 2π] once the construction stops, so the tip near 2π lies in the final walk. No direction is "never passed" when W stops. Termination is exactly what Claim 5 supplies.
- (b) This is correct as stated (with Fix 2).

## Claim 5: OK
The bootstrap is checked line by line.
- **The induction is not circular.**
  - (B_1) comes from the explicit phase-1 estimate.
  - (B_j) uses only J up to τ'_j. It gives the Λ-Lipschitz property of Γ_j via Claim 2d and Claim 3, because e^{vJ*} ≤ Λ.
  - The step (B_j) ⇒ (B_{j+1}) uses the Lipschitz property of fronts 1..j (from (B_1..B_j)), the non-finality of walks 1..j, and the connector bound ε/(1−v). The connector bound is unconditional. Nothing about walk j+1 is used.
- **Phase 1.**
  - g' ∈ [−1−v, −1+v] and |g(0)| ≤ 1, so |g| ≤ 2/(1−v) on [0, 1/(1−v)].
  - The change of variables gives J^{(1)} = (2/(1−v))(1 + log(2/((1−v)ε))). This matches the first two terms of (1−v)J*.
- **Lower bound.** ρ_φ ≥ χ(φ, θ*) − ε (Claims 4b and 2b) and the ψ trick are correct.
- **Layer cake.** The identity 1/ψ = ∫ 1{ψ<y} y^{-2} dy is correct, and the integrand vanishes for y ≤ ε.
  - ψ is measurable: θ* is monotone on each walk and constant on each connector.
- **Case y > 1.** m(y) ≤ Σw_i + Σc_i ≤ 2πΛ + j·ε/(1−v), and j ≤ 2πΛ/ℓ, which gives 2πΛ/(1−v). Correct.
- **Case ε < y ≤ 1.**
  - |A_y| = 4·arcsin y ≤ 2πy, because arcsin is convex on [0, 1]. This was checked numerically.
  - A_y has at most two components in [0, 2π].
  - Walking time is ≤ Λ|A_y|, because σ_i is Λ-Lipschitz and monotone and the [a_i, a_{i+1}] do not overlap.
  - Connector count is ≤ 2 + |A_y|Λ/ℓ, because consecutive a_i differ by ≥ ℓ/Λ.
  - The algebra (2πΛy + 2ε)/(1−v) is correct. Integrating gives (2πΛL + 2 − 2ε)/(1−v) ≤ (2πΛL + 2)/(1−v).
- **Sum.** J^{(1)} + (2πΛL+2)/(1−v) + 2πΛ/(1−v) = J*(Λ) exactly. This was verified symbolically.
- **Termination and time.**
  - Fewer than 2πΛ/ℓ walks are non-final, so the next walk is final.
  - The final walk length is σ_N(2π) ≤ Λ(2π − a_N), using (B_N).
  - T ≤ 1/(1−v) + 2πΛ + 2πΛv/(1−v) = (1+2πΛ)/(1−v). Correct.
- Λ ≥ 1 is not actually used; it is harmless.

## Theorem D2: OK with fixes
All constants were recomputed in `constants.py` at 40 digits:

| Quantity | Value | Comparison |
|---|---|---|
| 2 + 4π | 14.56637 | the claim's 14.567 is OK |
| 4 + 4π + 2 log 2 + 2/27 | 18.02674 | the claim's 18.028 is OK |
| log(1/(1−v)) ≤ v/(1−v) | ≤ 1/27 for v ≤ 1/28 | OK |
| (22L+28)·27/28 | 21.2142857 L + 27 | **not** 21.215 L + 27 |
| 14.567 / 21.2142857 | 0.686660 | < log 2 = 0.693147 |
| 18.028 / 27 | 0.667704 | < log 2 |
| exact max over L ∈ [0, 100] of v_2·J*(2) | 0.66761, attained at L → 0 | margin 0.0255 below log 2 |
| (1 + 4π)·28/27 | 14.06883 | < 14.07 ≤ 14.1 OK |

- The large-L limit of v_2·J*(2) is (2+4π)/22 = 0.6621.
- **Fix 3 (rounding direction).** Rounding 21.2143 up to 21.215 in a denominator makes the displayed bound slightly too small, so it is not a valid upper bound as written. Replace the line with:
  "v J*(2) ≤ (14.567 L + 18.028)/((22L + 28)(27/28)) = (14.567 L + 18.028)/(21.2142… L + 27) ≤ max(14.567/21.2142, 18.028/27) = max(0.6867, 0.6677) < 0.6931 < log 2."
  The conclusion is unchanged.
- Remark on sharpness of the method: as L → ∞ the condition with Λ = 2 needs c ≥ (2+4π)/log 2 = 21.015. The constant 22 is therefore close to optimal for this Λ = 2 argument, not slack. Optimising over Λ gives a different constant; this is not needed for the theorem.
- Scaling: the time bound in units of d and ℓ = εd/v are correct, because the problem is invariant under scaling space and time by d.

## Corollary D2.1: OK
The termination and time argument uses only:
- ℓ = σ_j(a_{j+1}) ≤ Λ(a_{j+1} − a_j) for non-final walks;
- σ_N(2π) ≤ Λ(2π − a_N) for the final walk;
- c_i ≤ ε/(1−v).

These need the Lipschitz property on the walked part [a_j, a_{j+1}] only. If W never stopped, infinitely many advances of ≥ ℓ/Λ would exceed 2π, so W stops. Claim 4c then gives full coverage.

## Simulation (independent; `code/referee/D2a/simulate_W.py`)
**Method.**
- A grid variant of W with N+1 grid directions φ_k = 2πk/N. Each a_j is taken as the last grid point with polyline arclength ≤ ℓ, so w_j ≤ ℓ. This keeps ρ ≤ vw_j ≤ ε, which is all Claim 4a needs.
- 3000 random probe directions are integrated alongside but are not used to build the path.
- RK4 with step ε·dtfrac. The connector durations are exact (closed form).
- "Seen" means that the sampled min_t ρ is ≤ ε.

| ε | v | walks | T | bound | max grid Lip(Γ_j) | max vJ at walk starts | max minρ/ε (grid / probes) | unseen |
|---|---|---|---|---|---|---|---|---|
| 0.9 | v_2 = 0.03298 | 1 | 7.48 | 14.03 | 1.038 | 0.037 | 0.155 / 0.155 | 0/2001, 0/3000 |
| 0.5 | v_2 = 0.02312 | 1 | 7.43 | 13.89 | 1.041 | 0.040 | 0.198 / 0.198 | 0/2001, 0/3000 |
| 0.1 | v_2 = 0.01271 | 1 | 7.37 | 13.74 | 1.043 | 0.042 | 0.539 / 0.539 | 0/4001, 0/3000 |
| 0.01 | v_2 = 0.007733 | 5 | 7.42 | 13.67 | 1.067 | 0.112 | 0.463 / 0.436 | 0/8001, 0/3000 |
| 0.001 | v_2 = 0.005556 | 36 | 7.39 | 13.64 | 1.057 | 0.122 | 0.133 / 0.130 | 0/6001, 0/3000 |
| 0.01 (stress) | 10·v_2 = 0.0773 | 57 | 9.01 | 14.70 | 2.008 | 1.345 | 0.375 / 0.253 | 0/8001, 0/3000 |

A 40·v_2 stress run was abandoned, unfinished, because the machine is heavily loaded. That run is outside the theorem and is not needed for any verdict.

Observations:
- At v = v_2, every grid and probe direction is seen, and T is about 7.4. That is roughly half the proved bound (1+4π)/(1−v), consistent with the theorem. The observed fronts are far less stretched than the worst case: Lipschitz about 1.04 to 1.07 against the allowed 2. The maximum J is about 13 to 19, against J*(2) of about 50 to 90.
- Even at 10·v_2, outside the theorem's hypothesis, W still sees everything. The front Lipschitz constant reaches about 2.0.
- The bound e^{vJ} (3.84) is loose against the observed 2.0, as expected from a Gronwall bound.
