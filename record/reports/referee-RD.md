# Referee report RD: claims D1 to D6 (`referee/D-claims.md`)

Referee: independent adversarial referee (RD). I read `BRIEF.md` §1–2, `paper/main.tex` and `referee/D-claims.md`.
I did not read `reports/D-1.md`. I looked at `code/D/check_constants.py` only after I had formed my own view and run my own checks (see §6).
All scripts are in `code/referee/RD/`, and their outputs are in `code/referee/RD/out/` and `code/referee/RD/rd_constants.out`.
Normalisation throughout: d = 1, speed 1, Snitch speed v.

## 0. Verdicts

| Claim | Verdict | One line |
|---|---|---|
| **Theorem D1** (ε>0, v ≤ min{1e-4, (ε/(403+210 log(3.34/ε)))^{1/2}}, everything seen by time 8, path of speed exactly 1) | **OK** (PROVED). Three cosmetic corrections (N1–N3) | I checked every step and every constant and found no logical gap. In a numerical test of 20,000 uniform plus up to 3,180 adversarial directions at 12 (ε, v) pairs, nothing was unseen. The worst miss distance was 0.5001ε, against the proof's bound of up to 0.998ε. |
| Lemma D1 (unit vectors) | OK | |
| Lemma D2 (first-order prediction) and the "further facts" (∂_θQ bound, identity (*)) | OK | |
| Lemma D3 (tip seen in Phase 1) | OK | |
| (P1a), (P1b) | OK | |
| Lemma D4 (time spent near a point) | OK, with a minor GAP that the slack absorbs (N2) | When the arc of a_k values wraps across θ = 0 there can be one more connector. The bound becomes 3.33r + 43.3v, still ≤ 6.29r + 61.2v. |
| Bootstrap (H1)–(H3), connector bound, error bound, seeing step | OK | There is no circularity: Γ_k depends only on P on [0, τ_k]. |
| **Lemma D5** (exact seen set of one straight leg; F is a homeomorphism of R²∖{0}) | **OK** | The "needle" corollary is OK as stated. The curvature remark after it (useful leg length O((ε/κ)^{1/2})) is a heuristic and should be labelled one. |
| **Proposition D6** (conditional reduction via K ≤ K*) | **GAP (regularity), fixable.** Parts (a) and (c) are OK. | In (b) the arc {S_α : α_target ≤ α < 2π} contains already-seen directions, which a leg can catch exactly (ρ = 0). The Λ' formula and the arc itself are then not defined as written. The fix is in §4. |

## 1. Theorem D1: step-by-step check

### 1.1 Reduction to (A0)
If v < ε/8 then v < ε/(1+2π), because 1+2π = 7.283 < 8. Theorem A then applies, with time 1+2π < 8. Otherwise ε ≤ 8v ≤ 8·10⁻⁴, and v² ≤ ε/(403+210 log(3.34/ε)) gives ε ≥ 403v². Both are correct.

**N1 (statement).** In the regime v < ε/8 the path used is Theorem A's circle sweep, not "one straight run, then windows". The statement should say "the path of Theorem A if v < ε/8, otherwise the window path".
Numerically the window path also works there: at ε = 10⁻², 10⁻³ with v = 10⁻⁴ and 0.9·10⁻⁴, all directions were seen, with worst miss 0.04ε to 0.38ε. But the proof's constants do not cover that regime; for example M = 50v there, not ≤ 5.41v.

### 1.2 Lemmas D1, D2 and the further facts
- D1 is |a/|a| − b/|b|| ≤ |a−b|/|b| + ||b|−|a||/|b|. Correct.
- D2 compares S_θ(t) = e^{iθ} + v∫unit(S−P) with Q_θ, and uses |S_θ(s) − e^{iθ}| ≤ vs. Correct. The singular set {D_θ = 0} is: s = 0 for θ = 0 only in Phase 1, and empty in Phase 2 because D ≥ |P| − 1 ≥ 0.48v.
- ∂_θ unit(e^{iθ} − P) = (I − ww^T) i e^{iθ}/D_θ. Correct, so |∂_θQ − ie^{iθ}| ≤ v∫ds/D.
- Differentiation under the integral is justified. For θ' near θ ∈ [δ₁, 2π−δ₁], 1/D_{θ'} ≤ max(π/(2δ₁), 1/(0.48v)): in Phase 1 D ≥ |sin θ'|, or D ≥ 1 when |θ'| ≥ π/2.
- (*): from D² = 1 − 2e·P + |P|² we get 1 − e·P = (D² + 1 − |P|²)/2. Correct.

### 1.3 Phase 1
- **D3.** t₀ = (1−ε/2)/(1−v) ≤ 1/(1−v) ≤ 1+2v.
  - h(t₀) = (1+v)ε/2 − (1 − cos α) ∈ [(1+v)ε/4, (1+v)ε/2], using α ≤ δ₁ ≤ 0.3ε and 0.045ε² ≤ ε/4.
  - cos β_c = (1−v)/2 gives sin β_c ≥ √3/2 and tan(β_c/2) ≤ 1, so g(β_c) ≥ √3/2.
  - g(α) ≤ 2^v α^{1−v} ≤ √2·0.3ε = 0.4243ε < (√3/4)ε = 0.4330ε.
  - So h/C ≥ k(β_c), β(t₀) ≤ β_c, and ρ(t₀) ≤ ε. Correct.
  - Monotonicity of k is Lemma 1 of the paper, and C is constant because the candidate stays in the open half-plane.
- **(P1a).** AM–GM gives c_θ(s) ≥ √(1−s²) for s ≤ 1, and c ≥ −1 on [1, t₁]. The integral of √(1−s²) is π/4. Correct.
- **(P1b).** ∫₀^{t₁} ds/max(a,|s−b|) ≤ 2 + 2 log(t₁/a) for b ∈ [0,1]. Then 2 + 2 log(π t₁/2) = 2.9036 ≤ 2.91, and (2/(1−v)) log(1/(0.3ε)) ≤ 2.0004 log(3.334/ε) for all ε ≤ 8·10⁻⁴ (grid check, worst slack −0.002).
  - By quadrature, the maximum of J₁ over θ ∈ [δ₁, π] is 9.79, 18.31 and 32.12 at ε = 8·10⁻⁴, 10⁻⁵, 10⁻⁸. The bound gives 19.58, 28.35 and 42.17.
  - vJ₁ ≤ 0.00302 at v = 10⁻⁴ with ε = 403v², which is the worst case. Claimed: 0.004 or 0.005. OK.

### 1.4 Construction (Phase 2)
- Γ_k depends only on P on [0, τ_k].
- Connector k runs X_k → Γ_k(a_k). The walk follows Γ_k for arclength ℓ = ε/(2v), or until θ = 2π − δ₁.
- **Speed exactly 1.** The connectors are unit-speed segments. Γ_k is C¹ with |∂_θΓ_k| ∈ [0.976, 1.024] > 0, so the arclength parametrisation exists and is C¹. The path is continuous at every junction, since connector k ends at Γ_k(a_k) and walk k ends at X_{k+1} = Γ_k(a_{k+1}). After the last window Harry may continue in any unit-speed way. So the speed is exactly 1, with no limiting argument. Correct.
- **Coverage.** Every θ ∈ [δ₁, 2π−δ₁] lies in exactly one window, because θ is strictly increasing along each walk and consecutive windows share endpoints a_{k+1}. θ ∈ [−δ₁, δ₁] is covered by D3 and its reflection, so the end of the circle α → 2π is covered too. I also checked θ = ±δ₁(1 ± 10⁻⁹) and 2π − 10⁻¹² numerically (§2).
- **Finite.** Each non-final walk has length exactly ℓ, and the total walked length is ≤ 6.44. So there are at most 1 + 6.44/ℓ windows.

### 1.5 Bootstrap: order of the induction
The induction is on k, with statement (H1)–(H3) for the path on [0, τ_k]. The steps go in this order:
1. Upper radius: |P| ≤ 1 + 7.5v. This uses (H3) at k.
2. D4 at time τ_k. This uses (H2) for windows j < k and c_j ≤ M.
3. (H1) for walk k and connector k. Connector k ends at Γ_k(a_k) and starts at Γ_{k−1}(a_k), or at (1+2v, 0) when k = 1.
4. (H2) for Γ_k. This uses (H1) up to τ_k and D4.
5. (H3) at k+1. This uses (H2) for Γ_k.

No step uses a statement about the future, so the induction is not circular.

### 1.6 Constants (all redone in `rd_constants.py`)

| Item | Claimed | Recomputed |
|---|---|---|
| c₁ | ≤ 3.0002v + δ₁ | 3v + 2v² + δ₁ |
| M = max(c₁, ε/(2(1−v))) | ≤ 5.41v | ≤ 5.4002v, from δ₁ ≤ 0.3ε ≤ 2.4v. Induction c_k ≤ v(c_{k−1} + ℓ) ≤ M because vℓ = ε/2. |
| \|P\|² − 1 | ≤ 20.01v | 1.50·10⁻³ at v = 10⁻⁴, ≤ 2.001·10⁻³. √20.01 = 4.4733. |
| D4, walks | 3.236(r+8v) | 1.03π = 3.2358; arcsin x ≤ πx/2 checked |
| D4 total | 3.33r + 37.9v | 3.3234r + 37.880v |
| M/ℓ | ≤ 0.027 | 10.82/403 = 0.02685 |
| (H1) bracket at v = 10⁻⁴ | ≥ 0.497 | 0.49766. Connector minimum norm: 1 + 0.4966v. |
| J₂ | ≤ 6.29 log(3.96/v) + 131.8 | exact layer-cake value is 198.29 at v = 10⁻⁴ (bound 198.39) |
| vJ₂ | ≤ 0.0199 | 0.01983 |
| v(J₁ + J₂) | ≤ 0.024 | 0.02286 |
| Σℓ | ≤ 6.44 | 6.4340 |
| Σc | ≤ 0.0012 | 0.001185 |
| τ | ≤ 7.45 | 7.4414 |
| E phase-2 bracket | 6.29 log(0.2375/v) + 11.87 | exact 60.748 vs 60.761 at v = 10⁻⁴; 1.9/8 = 0.2375 |
| E | ≤ 2v²[97.88 + 52.33L] | 2v²[97.871 + 52.321L] |
| Seeing condition | v² ≤ ε/(402.4 + 209.4L) | v² ≤ ε/(402.34 + 209.32L). (A0) implies it for all ε ≤ 8·10⁻⁴ (grid of 5,000 values down to 10⁻⁴⁰). |
| log(0.2375/v) ≤ L | | uses v ≥ ε/8: 0.2375/v ≤ 1.9/ε ≤ 3.334/ε. Correct. |

The layer-cake steps are correct:
- ∫ds/D = ∫r⁻²|{D<r}|dr, with |{D<r}| = 0 for r < 0.48v.
- ∫φ(D)ds = ∫(−φ')|{D<r}|dr for the decreasing φ = min(1, 8v/r), where −φ' = 8v/r² on r > 8v.
- The tail r > 1.9 is bounded by 8/1.9 = 4.21.

**N2 (Lemma D4, wrap-around).** The a_k lie in [δ₁, 2π − δ₁]. An arc of length π(r + M + 8v) around e^{iθ} with θ near 0 meets this interval in two pieces. The count is then "≤ 2 + 1.03π(r+M+8v)/ℓ", not "1 + …", plus k = 1. This adds one connector, at most 5.41v. The total becomes 3.33r + 43.3v ≤ 6.29r + 61.2v, so the generous form actually used is unaffected. Fix: write "at most 2 + …".

**N3 (statement).** "Beats Theorem A for every ε/d < 7.3·10⁻⁴" should read "< (1+2π)·10⁻⁴ = 7.283·10⁻⁴". For ε ∈ [7.284, 7.3]·10⁻⁴, Theorem A allows ε/7.283 > 10⁻⁴ = v_D. The example at ε = 10⁻⁶ (1.677·10⁻⁵ vs 1.373·10⁻⁷) is correct.

I tried to break the proof at the points the author flagged (layer-cake, connector count, circularity of the margin, use of k decreasing in D3) and found nothing beyond N2.

## 2. Theorem D1: numerical test

### 2.1 Method
- **Path (`rd_core.py`).** Built only from the written construction. Phase 1 is the segment [0, 1+2v].
  - For each window, Γ_k(θ) = e^{iθ} + v∫₀^{τ_k} unit(e^{iθ} − P) is evaluated **in closed form** on every straight piece of the past path, since the path is piecewise straight. The closed form agrees with adaptive quadrature to 1.8·10⁻¹³.
  - The connector runs to Γ_k(a_k). The walk follows Γ_k for arclength ℓ, realised as the inscribed polyline through the vertices Γ_k(θ_i). The θ-mesh is h = 2·10⁻⁴, plus 14 geometrically refined nodes just after a_k, where Γ_k has structure on scale v.
  - The vertices are independent of the test directions.
- **Candidates.** Each candidate is propagated **exactly** across every straight piece with the (C,h) translation. The minimum distance over a piece is computed exactly as C/g(β_m) when β crosses β_m = arccos v, and otherwise as the minimum of the endpoint distances. Against DOP853 (rtol 10⁻¹³) on 160 random and adversarial legs, v ∈ {10⁻⁶, …, 0.3}, the end positions agree to 2.6·10⁻¹⁴ and the minimum distances to a relative 4.4·10⁻¹¹ (`rd_test_core.py`).
- **Curved pieces.** In `rd_ode_check.py` each walk is replaced by the C² cubic spline through the same vertices, a genuinely curved path. The Snitch ODE is integrated on it with DOP853 (rtol 10⁻¹², atol 10⁻¹⁶), and the closest approach is located by an event on d|S−P|²/dt = 0.
  - The spline-ODE and polyline-exact miss distances differ by 5.0·10⁻⁵ε at ε = 10⁻⁴ (212 directions) and 5.2·10⁻⁴ε at ε = 10⁻⁵ (162 directions). These equal the predicted chord error h²/(8ε).
  - The worst ratio is the same in both: 0.49878 and 0.50001.
- **Mesh convergence.** At ε = 10⁻⁵ (20,000 directions), h = 4·10⁻⁴, 2·10⁻⁴ and 10⁻⁴ give the same worst ratio (0.500103) and maximum E (49.49v²) to the digits shown.
- **Directions.** 20,000 stratified-uniform directions, plus adversarial ones:
  - θ = δ₁(1 ± 10⁻⁹), δ₁(1 + 10⁻⁶), 0.5δ₁, 1.5δ₁, 10⁻¹²;
  - the mirror images near 2π;
  - π and π ± 10⁻⁹;
  - for every window, a_k ± {10⁻¹⁰, 10⁻⁸, 10⁻⁶, 2·10⁻⁸, 6·10⁻⁵} and a_{k+1} − those.

  That is 30 to 3,180 adversarial directions per run.
- **Recorded per direction.** The minimum distance during its own window, the time it is seen, and E_θ(τ_k) = |S_θ(τ_k) − Γ_k(θ)|.

### 2.2 Results (`out/run_main_*.out`)

| ε | v (fraction of v_D) | windows | unseen | worst miss / ε | max E / v² | proof's bound on miss / ε | last seen |
|---|---|---|---|---|---|---|---|
| 10⁻² | 1.0·10⁻⁴ (1.0) [v<ε/8: Thm A regime] | 1 | 0 | 0.040 (window), 0.300 (Phase 1) | 1.39 | n/a | 7.264 |
| 10⁻² | 0.9·10⁻⁴ (0.9) [same] | 1 | 0 | 0.036 / 0.300 | 1.39 | n/a | 7.264 |
| 10⁻³ | 1.0·10⁻⁴ (1.0) [same] | 2 | 0 | 0.380 | 40.3 | n/a | 7.283 |
| 10⁻³ | 0.9·10⁻⁴ (0.9) [same] | 2 | 0 | 0.354 | 44.0 | n/a | 7.282 |
| 5·10⁻⁴ | 1.0·10⁻⁴ (1.0) | 3 | 0 | 0.468 | 39.3 | 0.523 | 7.284 |
| 5·10⁻⁴ | 0.9·10⁻⁴ (0.9) | 3 | 0 | 0.461 | 42.1 | 0.518 | 7.284 |
| 10⁻⁴ | 1.0·10⁻⁴ (1.0) | 13 | 0 | 0.4988 | 43.6 | 0.629 | 7.285 |
| 10⁻⁴ | 0.9·10⁻⁴ (0.9) | 12 | 0 | 0.4985 | 45.1 | 0.605 | 7.285 |
| 10⁻⁵ | 5.704·10⁻⁵ (1.0) | 72 | 0 | 0.5001 | 49.5 | 0.998 | 7.284 |
| 10⁻⁵ | 5.133·10⁻⁵ (0.9) | 65 | 0 | 0.5001 | 50.3 | 0.904 | 7.284 |
| 10⁻⁶ | 1.677·10⁻⁵ (1.0) | 211 | 0 | 0.49997 | 57.2 | 0.998 | 7.284 |
| 10⁻⁶ | 1.509·10⁻⁵ (0.9) | 190 | 0 | 0.49996 | 57.7 | 0.904 | 7.284 |

**Bootstrap quantities, in every D1-regime run:**

| Quantity | Claimed | Observed |
|---|---|---|
| min \|P\| − 1 over Phase 2 | ≥ 0.48v | 0.81v to 0.87v |
| \|∂_θΓ_k\| | ∈ [0.976, 1.024] | ∈ [1.00001, 1.0013] |
| M | ≤ 5.41v | ≤ 2.8v |
| τ_end | ≤ 7.45 | 7.285 |
| Phase-1 directions | all seen in Phase 1 | worst 0.300ε, matching the h(t₀) analysis of D3 |

**Reading of the numbers.**
- The worst direction is always at the end of a walk. Over the window that direction drifts v(c_k + ℓ) ≈ ε/2, and Harry stands on its prediction, so the miss is ε/2 + O(E).
- The actual prediction error E ≈ 40–58 v² is about 3% of the proof's bound 2v²(97.88 + 52.33L). The theorem's constants are therefore safe but conservative.
- The stress tests beyond the claimed range are in §2.3.

### 2.3 Stress tests beyond the claimed range (`out/run_stress_*.out`)
I used 5,000 uniform directions plus adversarial ones, with the same path code and h = 2·10⁻⁴.

| ε | v | v / v_D | unseen | worst miss / ε | max E / v² |
|---|---|---|---|---|---|
| 10⁻³ | 6.89·10⁻⁴ (cap 10⁻⁴ removed) | 6.9 | 0 | 0.498 | 33.4 |
| 10⁻⁴ | 3·10⁻⁴ | 3 | 0 | 0.500 | 40.1 |
| 10⁻⁴ | 10⁻³ | 10 | 0 | 0.504 | 36.1 |
| 10⁻⁴ | 3·10⁻³ | 30 | **6,710 of 10,715** | 3.0 | 33.4 |
| 10⁻⁶ | 5.03·10⁻⁵ | 3 | 0 | 0.500 | 55.0 |
| 10⁻⁶ | 1.68·10⁻⁴ | 10 | **1,931 of 25,000** | 1.37 | 48.8 |

The ε = 10⁻⁶, 30× run (6,300 windows) was stopped for time. Its outcome is predictable from the 10× row.

**What the stress tests show.**
- The construction fails roughly when E ≈ (35 to 57)v² exceeds about ε/2, that is at v ≈ 0.1ε^{1/2}.
- So the theorem's range is conservative by a factor of about 3 to 10 in v. The log factor and the cap v ≤ 10⁻⁴ are artefacts of the bounds, not of the construction. The cap is not needed at ε = 10⁻³.
- The mechanism behind the failures is the one the proof identifies: the accumulated prediction error E grows with elapsed time, so failures sit in the last windows (θ → 2π).
- In no run did the bootstrap quantities come near their claimed limits.

## 3. Lemma D5: OK
- **F is a bijection.**
  - On each open half-plane the (C,h) chart is a bijection onto {±C > 0}. For fixed C > 0, h/C = k(β) runs over all of R.
  - The forward ray maps to {C = 0, h > 0} and the backward ray to {C = 0, h < 0}, since g(0⁺) = g(π⁻) = 0.
  - F is continuous across both rays, because ρg(β) → 0.
  - F⁻¹ is continuous at (0, h₀): h/|C| → ±∞ forces β → 0 or β → π, with ρ → h₀/(1+v) or ρ → |h₀|/(1−v). Numerically, C = 10⁻⁸ gives ρ to 8 digits (`out/rd_d5.out` (2)).
  - Near the backward ray F⁻¹ is only Hölder: γ = π − β behaves like C^{1/(1+v)}. This is harmless for the homeomorphism claim.
- **The constant m.** m = min_β max(g, |cos β + v|) > 0 because g and cos β + v never vanish together. Numerically m = 0.707 (v ≤ 10⁻⁴), 0.320 (v = 0.5), 0.005 (v = 0.99).
- **Round trip.** F⁻¹∘F matches the identity to a relative 4·10⁻¹⁵ on 100,000 points, including points within 10⁻⁸ of the forward ray and 10⁻⁶ of the backward ray.
- **Translation and seen criterion.** These are correct. Along a leg with C ≠ 0, h/|C| decreases, so β increases. ρ = |C|/g(β) is unimodal with its minimum at β_m. So the downward ray from (C, h) meets V_ε iff |C| ≤ εg_max and h ≥ h_low(C). Equivalently: ρ ≤ ε now, or (|β| ≤ β_m and |C| ≤ εg_max). Against DOP853 long legs (v ∈ {10⁻⁴, 0.2, 0.5}, 1,200 cases, half of them placed near the boundary of the criterion), the criterion gave **0 mismatches**.
- **Needle corollary.** This is OK as stated. g(β) ≤ 2^vβ^{1−v} gives "seen ⇐". The bound g(β) ≥ (2β/π)^{1−v} on (0, β_m] (sin β ≥ 2β/π and tan(β/2) ≤ 2β/π) gives "only those, up to constants".
- **Remark after the corollary.** The claim that front curvature limits the useful leg length to O((ε/κ)^{1/2}) is a heuristic and should be labelled one. It is not used anywhere.

## 4. Proposition D6: GAP (regularity in (b)), fixable; (a) and (c) OK

**(a) is OK.**
- The seen-by-t set is closed, by continuous dependence on α while ρ_α stays above ε.
- α* = inf U(t) is not in U(t). Every α_n ∈ U(t) with α_n ↓ α* has ρ_{α_n} > ε on [0, t]. Hence ρ_{α*} ≥ ε on [0, t], and in particular α* was never caught.
- Each leg lasts at least (ε − ε/2)/(1−v), and α** > α*.
- Numerically (`rd_d6.py`, N = 4000, ε = 0.05), the minimum leg length equals ε/(2(1−v)) to 4 digits at v = 0.2 and v = 0.4.

**(b) as written.**
- The switching inequality is correct: chord ≤ arc, plus the triangle inequality. Numerically the largest jump of Ψ at a switch is ≤ −2·10⁻¹⁰.
- K ≤ TV(bearing) is correct (sin²φ ds/ρ = |sin φ||dθ|). Numerically K/TV ≤ 0.75.
- The Ψ' formula matches finite differences to the discretisation error (4·10⁻⁴ at v = 0.2).
- **The gap.** Λ is the length of {S_α : α_target ≤ α < 2π}, and this set includes **already-seen** directions. Proposition 3 of the paper says a leg *catches* (ρ = 0) every direction that lies on the segment [H, S_target] at the start of the leg. Nothing in LG prevents part of the remaining arc from lying on that segment: Harry does not stop for seen directions, and he does not stop before ρ = 0 for directions closer than ρ_target − ε/2. At such a time t_c the trajectory S_α of the caught direction ends, so for t > t_c neither the arc nor Λ is defined. The formula Λ' = v∫sin²φ |∂_αS|/ρ dα also needs ρ > 0 on the arc. The hypothesis "K ≤ K*" does not exclude this, because the bearing variation stays finite as a point of the arc passes through Harry.

**Fix (pick one).**
1. **(Simplest.)** Continue every trajectory through Harry by the homeomorphism of Lemma D5. In (C,h) coordinates a straight leg is a translation, so a candidate on the forward ray passes through 0 onto the backward ray. This defines a continuous "generalised flow" on the whole circle of directions for any piecewise-straight path, so the arc stays a continuous curve and Λ is defined. One must then show:
   - (i) Λ is continuous at the passage time t_c;
   - (ii) Λ is absolutely continuous on each leg, with Λ' = vK almost everywhere.

   For (i): near the backward ray F⁻¹ is Hölder with exponent 1/(1+v), and the image arc is monotone in β. So its length stays finite and varies continuously. Before this fix, (b) should say explicitly: "valid on time intervals where no point of the arc has ρ = 0".
2. Or add to the hypothesis of (c): "no direction of [α_target, 2π) is caught during the chase", or "Λ is absolutely continuous with Λ' = vK almost everywhere". This keeps D6 a clean conditional statement.
3. Or replace exact catches. End every leg when ρ_target = ε/2 **or** when some point of the remaining arc reaches ρ = ε/4, whichever is first. The duration bound in (a) and the switching inequality then need re-checking.

**(c).** The bound Ψ(t₀) ≤ ε/2 + L(t₀) is correct if read as ρ_{α*}(t₀) ≤ |H − S₀| + arc(0, α*). Proposition 6(2) applies at t₀ = (1 − ε/2)/(1−v), which is before first contact. The conclusion T ≤ t₀ + Ψ(t₀)/(1 − v(1+K*)) follows, because Ψ ≥ ε/2 > 0 while legs run.
- Numerically at v = 0.2 the observed K* is about 3.28 on the N = 4000 polyline (the report says 2.95; the difference is polyline discretisation near Harry). That gives T ≤ 55.3 against an actual 13.0.
- At v = 0.4, v(1 + K*) > 1 and the bound is void. This is consistent with D6 being only conditional.

## 5. Summary of required edits
1. **D1 statement.** Say that for v < ε/8 the path is Theorem A's (N1). Replace "7.3·10⁻⁴" with "(1+2π)·10⁻⁴ ≈ 7.283·10⁻⁴" (N3).
2. **Lemma D4.** Change "1 + 1.03π(r+M+8v)/ℓ" to "2 + …" to cover arcs wrapping θ = 0; the total becomes 3.33r + 43.3v (N2). Nothing downstream changes.
3. **D5.** Label the curvature or leg-length remark as heuristic.
4. **D6(b).** Add the regularity caveat or use the generalised-flow fix from §4.

With these edits, **Theorem D1 can enter the main document as PROVED.** It is unconditional, has an explicit path of speed exactly 1, and uses no compactness. It improves on Theorem A only for ε/d < 7.283·10⁻⁴, and only by changing the exponent: v ≍ (ε/log(1/ε))^{1/2} instead of v ≍ ε. A second referee is still required by the brief, because this would be a main theorem.

## 6. About `code/D/check_constants.py` (read after forming my view)
The script checks the elementary inequalities one by one:
- g bounds;
- D3, via the exact straight map with 200 sub-steps;
- (P1a), and the ∫ds/max(a, |s−b|) bound with random (a, b);
- (P1b), by quadrature;
- the arithmetic chains for the margin, J₂, E, D4 and M.

I verified the same items independently. The script does **not**:
- (i) build the actual D1 path;
- (ii) test Lemma D4 or the bootstrap (H1)–(H3) on a real path;
- (iii) test the D4 wrap-around case;
- (iv) simulate candidates end-to-end.

So it checks what each line of the proof asserts, not that the construction works. §2 of this report supplies that end-to-end check.

## 7. Reproduce
From `code/referee/RD/`, with `OPENBLAS_NUM_THREADS=1`:

| Command | What it does |
|---|---|
| `python rd_constants.py` | every constant in §1.6 |
| `python rd_test_core.py` | validates the closed-form integral and the exact leg map against quadrature and DOP853 |
| `python rd_run.py EPS VFRAC [NCAND] [H]` | one run of the table in §2.2, e.g. `python rd_run.py 1e-6 1.0 20000 2e-4` (about 13 minutes) |
| `python rd_batch.py 12` | the whole matrix in §2.2, convergence and stress runs; output in `out/run_*.out` |
| `python rd_ode_check.py 1e-4 1.0 200` | curved-walk ODE check |
| `python rd_d5.py` | Lemma D5 checks |
| `python rd_d6.py 0.2 0.05 4000` | Proposition D6 checks |
