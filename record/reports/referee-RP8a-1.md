# Referee report RP8a-1 — `referee/P8a-claims.md` v2 (design T, touch-down data, Theorem P8a.H)

Independent adversarial referee. Read: `referee/P8a-claims.md` (all), `referee/P8b-claims.md` §§1, 5, 6 (interface),
`paper/sec_B.tex` (field F, Lemma V), `referee/P7-claims.md` §2 (statement of (ST_end)).
NOT read before the verdict: `reports/P8a-1.md`, `code/P8a/`.
Own code: `code/referee/P8a_1/` (`transport.py`, `design.py`, `endtoend.py`, `hole.py`, `lemma5.py`, `scan.py`,
`summ.py`; logs `scan_v1e-6.log`, `scan_v1e-9.log`, `scan_v1e-12.log`).

## 0. Verdict

**Theorem P8a.H: OK with fixes (all fixes are textual; no gap, no false statement found).**
(H_T) of P8b §5 holds for design T, D₁ = 1, for all v ∈ (0, 10⁻⁶], ε ∈ (0, 10⁻³], with the listed constants. Every
estimate is proved by an explicit analytic chain that is uniform in (v, ε) on that range; I found **no** inequality
that rests on a (v, ε) grid. One literal mismatch with (H_T) (M1 below: `𝒢 ⊂ (0,U)` versus `0 ∈ 𝒢`) must be
repaired on the P8b side (one character); it does not affect any proof.

| Claim | Verdict |
|---|---|
| Lemma 1 (coordinates (C, τ)) | OK |
| Lemma 2 (first-order transport) | OK (re-derived; ODE check ≤ 1e-44) |
| Lemma 3 (curvature transport) | OK (re-derived; ODE check ≤ 1e-44) |
| Lemma 4 (run 1, hole) | OK with fix F1 (proof of (d) gives 1.2vε as written; statement true) |
| Lemma 5 (tangency, data at t₁) | OK with fix F2 (one rounded number) |
| Lemma 6 (forward arc) | OK |
| Lemma 7 (tail, E_Y, seen labels) | OK with fix F3 (two rounded numbers) |
| Lemma 8 (virtual labels next to X₀) | OK |
| Lemma 9 (bulk) | OK |
| Lemma 10 (hole edges) | OK with fix F4 (typo) |
| Lemma 11 (true front through the hole, axis label) | OK |
| Proposition P8a.1 | OK (matches (ST_end) of P7 §2 on A₁: (E1), (E2), C₀λ₀^{a′} ≤ 1) |
| Theorem P8a.H | OK with fixes M1 (P8b text), F1–F4 |

## 1. The exact transport lemmas (task item 1)

Re-derived by hand:
* Lemma 2: with x_θ = X + iY, ∂_θh = X + v(X cos β + Y sin β) = Re(x_θ + v e^{iβ} x̄_θ); τ^v ∂_θC = Y − vρ∂_θβ =
  Y(1 − v cos β) + vX sin β = Im(…). Time independence because C and h + (1−v²)t are first integrals. Inverse and
  singular values 1 ± v of I + vR: correct.
* Lemma 3: I did not find an error in the determinant computation; the identity 𝔖(t = 0) = 0 on the unit circle
  (so k₁ = 𝒯/w₁³ − 𝔖₁ in run 1) is correct (bracket = −(cos α − v) − v + cos α = 0).

Numerics (`transport.py`, mpmath Taylor integrator at 45 digits; state (S, ∂_θS, ∂²_θS) integrated by the variational
equations of S′ = v(S−H)/|S−H|, no use of the integrals): v ∈ {1e-6, 1e-3, 0.1, 0.5}, labels α = 0.01 and three random
labels each, run 1 from the unit circle to t₁ **and then a second straight run with a random heading and random
duration** (generic initial curve). 17 identities per case: C, h, the four formulas of Lemma 1(a), Re Ξ = a,
Im Ξ = τ^v c, the inverse formula, k from Lemma 3 with J = a c′ − c a′, k₁ = 𝒯/w₁³ − 𝔖₁, and for the second run the
invariance of C, h + (1−v²)t, a, c and the two-time relation k″ = (τ″/τ′)^v (w′/w″)³(k′ + 𝔖′) − 𝔖″.
**Worst error over all 16 cases × 17 identities: 9.98e-45** (≥ 44 digits; required ≥ 30).
`endtoend.py`: the composed closed form (run 1 → frame of run 2 → t_s) against the ODE through the whole design for six
labels including two hole labels (true flow passing at distance 2e-4, 3.3e-4 < ε = 1e-3 from Harry): position/tangent
errors ≤ 1.1e-40, curvature equal to 15 printed digits.

## 2. Run 1 through the front; the hole; the axis label (task item 2)

* Seen set (Lemma 4(a)): correct. For 0 < α ≤ arccos v the point cos β = v is passed before t₁ (h₁ < 0), min ρ = g(α)/g_max,
  so seen ⇔ α ≤ α_s; α > arccos v: ρ increasing; α = π: ρ ≥ 1. α_s ≤ 2.1ε correct (numerically α_s/ε ≈ 1 − O(vln(1/ε))).
* α = 0: caught at t₀ = 1/(1−v) < t₁, no trajectory afterwards; every α ≠ 0 has C = g(α) > 0, hence ρ ≥ C/g_max > 0:
  never caught in run 1; in run 2, b ∈ (0, π) for α ≠ α₀ (Lemma 5(a), checked: an assert in `design.py` on every label
  evaluated, hole labels and lower half included). Correct.
* **Uniformity as α → 0 — reconciliation with the blow-up of the stretch.** The label-stretch does blow up:
  w₁ ≈ 𝒯 = (τ₁/τ_α)^v ~ α^{−2v/(1+v)} (α^{−v} at first contact, doubled by the passage). But Lemma 3 gives
  k₁ w₁³ = 𝒯 − 𝔖₁w₁³ with a *single* power of 𝒯, and Lemma 2 gives (1+v)w₁ ≥ Im Ξ = (cos α − v)𝒯. Hence
  𝒯/w₁³ ≤ (1+v)/(cos α − v) (indeed → 0 like 𝒯⁻²) and |𝔖₁| ≤ 2.0001v: the curvature **in arclength** is bounded
  uniformly; only the label parametrisation is singular, and ∫w₁dα < ∞. The tilt bound tan δ ≤ 1.1396 y gives tangent → i
  from both sides, so the arclength-parametrised curve is C¹ through Z₁ and its tangent angle is continuous with a.e.
  derivative ≤ 1.14: C^{1,1}. Transport to t_s by the smooth flow near the point 1 (distance ≥ 0.497 from Harry in run 2;
  checked: dist(1, [2, e^{iπ/3}]) = 1/2, foot = midpoint) keeps this, |k| ≤ (1.13951 + 0.07215)·1.00071 < 1.22. The
  argument is correct.
  `hole.py` (closed forms; labels α = 10⁻¹ … 10^(−10⁸)): for v = 1e-6, k₁ = 0.99999594 (α = 0.1), 0.99973 (1e-30),
  0.9120 (1e-10⁴), 0.398 (1e-10⁵), 1.0e-4 (1e-10⁶), **→ 1.0e-6 = v/(1−v²)** (1e-10⁷, 1e-10⁸), always below the bound of
  Lemma 4(c); tan δ/y → v/(1−v²) as well (the parabola of the Remark); w₁/(2/α)^{2v} ≤ 1 throughout; at t_s the
  curvature from both sides of the axis agrees (→ 5.67e-7) and ψ₊ − ψ₋ → 0. Same picture for v = 1e-3 and v = 0.1
  (k₁ → 0.001000001, 0.10101). So the claim is uniform, and the Remark after Lemma 4 is right.
* Z₁ = P(t₁) − (1+v): correct ((1−v)|z| ≤ |h₁| ≤ (1−v)|z| + vy).
* "Ghost label carrying Z_s": consistent with P8b §1 (the label is not true because S₀ is caught before t_w); nothing has
  to be seen there (seen at t₀). Hole labels 0 < |α| < α_s are *true* labels in P8b's sense and are seen; fine.

## 3. Run 2 (task item 3)

* Tangency (Lemma 5(a)): identity (1−v²)ρ₁∂_θβ₁ = sin β₁[h₁(cos θ − v) + sin²θ]/sin θ and
  h₁(cos θ − v) + sin²θ = (1−v²)t₁(cos α₀ − cos θ) re-derived; numerically ∂_θb/(Λ sin((θ−α₀)/2)) = 1.000… on 800
  labels of I_η down to |θ − α₀| = 1e-18 (`lemma5.py`). α₀ is the silhouette label seen from P(t₁); b has a double zero.
* t_s versus true catch time: the virtual α₀ stays on the ray, σ′ = −1 + vf(σ) inside the disc (f(σ) = (σ/ε)(2 − σ/ε),
  `sec_B.tex`), so t_s − t_a = ε∫₀¹dσ/(1 − vσ(2−σ)); t₂ − t_s ∈ (0, vε/(3(1−v)²)]. Checked: RK4 of the virtual field gives
  |x_{α₀}(t_s) − P(t_s)| = 5e-24 ε, ψ(α₀, t_s) = 0; (t₂ − t_s)/(vε/(3(1−v)²)) = 0.9999994 (v = 1e-6). The true candidate
  α₀ is at distance (1−v)(t₂ − t_s) > 0 from Harry at t_s — hence u = 0 is a ghost label (see M1).
* Labels seen in run 2 (Lemma 7(b)): correct. x ∈ [0.35vε, x_e]: C ≤ εg_max and h(t_s) ≤ 0 (I get the threshold
  0.3354vε), so the minimum C/g_max ≤ ε was passed in run 2. x ∈ (0, ε/2]: ρ(t_a) ≤ ε − 0.89x re-proved. The two ranges
  cover (0, x_e]. Scan: both criteria checked at x = 10⁻¹²vε … 0.999x_e, never failing.
* Forward labels: x ≥ 1.02ε ⇒ ρ ≥ ρ(t_s) ≥ 1.0136ε on run 2 (true, never seen yet); x ∈ (0, 1.02ε): not classified by
  Lemma 7 and correctly handled in Theorem H through the definition of 𝒢. (P8b's parenthesis "the virtual candidates of
  [α₀, α₀+1.02ε) have been inside the ε-disc" is not true for x between ≈ ε and 1.02ε — irrelevant, since (H_T) is
  existential in 𝒢 and P8a's 𝒢 is the right one.)
* E_Y: C is strictly monotone on each side of α₀ (∂_θ log C ≠ 0, Lemma 5(c)), so b_e is unique;
  1.277ε^{1/(2−2v)} ≤ x_e ≤ 1.566ε^{1/(2−2v)} re-proved; numerically x_e/ε^{1/(2−2v)} = 1.41433 … 1.41416 (≈ √2).
  Label b_e touches the ε-circle at one instant: true = virtual on [α_s, b_e].
* Virtual = true junction at α₀ + 1.02ε: RK4 of the virtual field versus the closed true form at x = 1.02ε, 1.5ε
  agrees to 1e-19 (relative to ε), as it must (ρ > ε throughout).

## 4. The inequalities (task item 4)

I recomputed every displayed numerical step by hand. All statements are true; the arithmetic slips are listed in §6.
The chains re-proved in full:

**(T1) at X₀ (near case).** u_a < max(λ, 1.04ε) ≤ 2.08λ ⇒ u_b < 3.08λ ≤ 0.077 ⇒ forward zone; |T − û| ≤ 1.69x^{1−μ} ≤
1.69u^{1−μ} (Lemma 8, x ≤ u); 2E = 2(l − c) ≤ 2∫(1 − T·û) = ∫|T − û|² (trivial, valid for any C¹ curve, virtual labels
included) ⇒ N ≤ (1.69/√(3−2μ))(3.08λ)^{3/2−μ} ≤ 5.275λ^{3/2−μ}. Lemma 8 itself: on [t_a, t_s], y′ = v(f/ρ)y,
|ψ_t| ≤ v|p|/max(ρ,ε)² ([B, Lemma V(iii)]), |p| ≤ y + ρ|ψ| ⇒ Gronwall with total exponent ≤ 2v/(1−v): correct, uniform.
**(T1) far case (bulk, E_Y, across the hole).** On {u ≥ 1.04ε} (x ≥ 1.0245ε ≥ 1.02ε, true C^∞ front off the label 2π)
the tangent angle is locally Lipschitz with constant ≤ 1.0002u^{−μ} (forward), ≤ 1.0001ε^{−μ_T} (tail, x ≥ x_e ≥ ε),
≤ 1.22 (elsewhere, **including across Z_s** by Lemma 11(c)); with u ≥ u_a ≥ λ, and λ ≥ ε/2 ⇒ ε^{−μ_T} ≤ (2λ)^{−μ_T}:
K = 1.22λ^{−3v}, Kλ ≤ π, E ≤ K²λ³/24 (re-proved: c ≥ ∫cos(ψ − ψ_mid) ≥ l − K²l³/24) ⇒ N ≤ 0.353λ^{3/2−3v}.
Both cases: N ≤ 5.4λ^{3/2−3v} ≤ 5.4·40^{−1/2+3v}λ ≤ 0.854λ. Uniform in ε (only λ ≥ ε/2 is used) and in v ≤ 10⁻⁶.
The curvature inputs: Lemma 6(d) (|k| ≤ 1.0001x^{−μ}: (τ/τ_b)^v ≤ ((1+v)r/h)^μ, |𝔖′| ≤ 3.42v, |𝔖″| ≤ 8.66vx^{−μ}) and
Lemma 7(c) ((τ/τ_b)^v ≤ 1.0000037x^{−μ_T}, |𝔖″| ≤ 8.38vx^{−μ_T}) re-derived step by step.
**(X1) = (T2) for pairs across the junction X₀/E_Y.** λ > 1/40 ⇒ Δ ≥ 0.02463 (from l ≤ 1.0152max(Δ, 0.02), which holds
through the hole because w ≤ 1.0151(2/χ)^{2v} at every label ≠ 2π and ∫(2/χ)^{2v} ≤ 1.000013Δ for Δ ≥ 0.02).
Δ ≤ 2π − 0.0246: c ≥ 2sin(0.0123) − 7.5e-6 ≥ 0.02459 ≥ c_sep. Δ > 2π − 0.0246: x_a + x_b < 0.0246, z_a = ∫₀^{u_a}cos ψ ≥
0.999u_a (|ψ| ≤ 0.0416), −z_b ≥ 0.9939x_b ≥ 0.9939u′_b/1.015 ≥ 0.979u′_b, c ≥ z_a − z_b. Correct, uniform in (v, ε).
**(T3)** trivial from Lemma 8. **(T4)** 1.647(x_e + u′)^{1/2} ≤ 1.647(1.4882(ε/2)^{1/4} + 0.4729u′^{1/4}) ≤ 3.231 max(·)^{1/4}.
**(T5)** z₀ ∈ [0.9939, 1.00013]x_e ⊂ [1.2692, 1.5663]ε^{1/(2−2v)}; |y₀| ≤ 1.000003ε^{1−v/2} ≤ 3.5ε^{3/4+μ/2} because
1/4 − v/2 − μ/2 > 0. Correct for all ε ≤ 10⁻³ (indeed for all ε < 1).

**"Verified only on a grid?"** No such place. Lemma 5(c) is a perturbation argument from v = 0 with explicit error
|d| ≤ 3.1e-6; Lemmas 6–11 are closed-form chains in which ε enters only through x ≥ 1.02ε, x ≥ x_e ≥ 1.277ε, λ ≥ ε/2
and δ(t_s) ≤ 3.4e-7ε, and v only through v ≤ 10⁻⁶. The numerical files are declared "not part of any proof" and I did
not need them.

**Numerical scan (own code `scan.py`, exact touch-down state, mpmath 67–135 digits).**
v ∈ {1e-12, 1e-9, 1e-6} × ε ∈ {1e-3, 1e-4, 1e-6, 1e-10, 1e-15, 1e-20, 1e-30} (21 runs). Per run: 100–180 labels (log grids
at X₀ from 10⁻³ε, at E_Y from x_e(1 + 10⁻⁴), hole labels from 10^(−dps/3) to 10α_s on both sides, 49 bulk labels),
all λ > λ₀ pairs among them for (T2)/(X1); 95–608 pairs for (T1) at scales λ = 0.51ε … 0.98λ₀ in 20 positions (starting
at X₀, 0.3λ, λ, 2.08λ, 1.04ε; ending at E_Y; straddling the axis label symmetric/asymmetric and the hole edges; bulk;
junctions x = 0.1), N computed as (2∫w(1 − cos(ψ − ψ_chord)))^{1/2} (validated against l − c). 66 named inequalities
per run (plus 21 informational maxima). **0 violations in 21 runs.** Worst ratios lhs/rhs (≤ 1 required), over all runs:

| inequality | worst ratio |
|---|---|
| (T1) N ≤ 0.86λ | 0.0525 (λ = 0.0245) |
| (T1) sharp N ≤ 5.4λ^{3/2−3v} | 0.0535 (true N/λ^{3/2} ∈ [0.28866, 0.28870] everywhere, incl. X₀, E_Y, hole) |
| (T2) c ≥ min(c_sep, (u_a+u′_b)/2) | 0.945 |
| (X1) c ≥ 0.999u_a + 0.979u′_b | 0.99901 |
| (T3) / sharp 1.69x^{1−μ} | 0.023 / 0.592 |
| (T4) / sharp 1.647x^{1−μ_T} | 0.092 / 0.607 |
| (T5) z₀ ≤ 1.57ε^{1/4}; |y₀| bound; sharp z₀, y₀ | 0.160; 0.044; 0.9025, 0.999999 |
| t_s ≤ 3.74; U ≤ 6.5 | 0.9979; 0.9666 |
| Lemma 6(d) |k| ≤ 1.0001x^{−μ}; Lemma 7(c) |k| ≤ 1.0001x^{−μ_T} | 0.99990; 0.99990 |
| Lemma 9(b)/11(c) |k| ≤ 1.22, w ≤ 1.00036(2/χ)^{2v} | 0.8197; 0.99964 |
| Lemma 6/7 position bounds (ρ, y, z, τ, w) | ≤ 0.99987 |
| Lemma 10 (b) | 0.862 |
| |x⁰ − e^{iΘ}| ≤ 3.74e-6 | 0.987 |

`lemma5.py` (800 labels of I_η, v = 1e-6 and 1e-12): r ∈ [1.63223, 1.83189], Λ ∈ [1.0608, 1.2611], A ∈ [0.99469, 1.000001],
b/x² ∈ [0.2727, 0.3061], r|∂b|/x ≤ 1.029, C/x^{2−2v} ∈ [0.4996, 0.50000], a ∈ [0.99500, 1.000002], x∂_θ log C ∈ ±[1.9983, 2.0000],
𝔖/v ∈ [−2.11, −1.88] — all inside the claimed intervals of Lemma 5(c); Lemma 4(b),(c) on 3141 labels: inside.

## 5. Match with (H_T) of P8b §5, item by item (task item 5)

| (H_T) item | P8a.H | match |
|---|---|---|
| design, D₁ ∈ (0,1] fixed | D₁ = 1 | yes (P8b: "P8a: D₁ = 1"). No other D₁ is assumed anywhere in P8b's proofs; D₁ occurs only in §5. P8b's numerics (D₁ = 0.1) are not covered — irrelevant for the theorem. (In P8b §3 "D₁ := 1 − T·û" is an unrelated local symbol.) |
| t₂ := time when the virtual α₀ is at distance 0 | t_s, P(t_s) = x_{α₀}(t_s) | yes |
| constant ranges: T₂, U_max ≥ 1, a′ ∈ (0,1], λ₀ ≤ 1/4, c_sep ≤ 1, γ_T ≤ 1/4, G_T ≤ 1 | 3.74, 6.5, 1/2, 1/40, 0.024, 1/4, 0.05 | yes |
| x⁰ ∈ C¹, unit speed, 1 ≤ U ≤ U_max, n̂ unit | yes, n̂ = û | yes |
| (T0) x⁰(0) = P(t₂) | yes | yes |
| (T0) "𝒢 ⊂ (0,U)", every u ∉ 𝒢 true | P8a: 𝒢 ∋ 0 (label α₀) | **M1: literal mismatch.** u = 0 cannot be true (S_{α₀}(t_s) ≠ X₀ = x⁰(0), distance (1−v)(t₂−t_s) > 0), so no choice of 𝒢 ⊂ (0,U) works; P8b's own "intended realisation" also puts α₀ into 𝒢. |
| (T0) every direction seen or true | yes (hole and [b_e, α₀] seen; (α₀, α₀+1.02ε) by definition of 𝒢; rest true) | yes |
| (T1) all pairs ε/2 ≤ λ ≤ λ₀, N ≤ C₀λ^{1/2+a′}, C₀λ₀^{a′} ≤ 1 | yes, on the whole x⁰ (X₀, hole, E_Y included) | yes |
| (T2) c ≥ min(c_sep, (u_a+u′_b)/2) for λ > λ₀ | same form | yes |
| (T3), (T4) with max(u, ε/2)^{γ_T}, u resp. u′ ≤ G_T | same | yes |
| (T5) P(t₂) − x⁰(U) = z₀n̂ + y₀n̂^⊥, 0 ≤ z₀ ≤ C_zε^{1/4}, |y₀| ≤ ϑ_T(z₀+ε)(ε/2)^{γ_T} | z₀ = −z_E > 0, y₀ = −y_E (n̂^⊥ = in̂) | yes |
| working front / true / ghost as in P8b §1 with t_w = t₂ | used with these definitions; hole labels true, α = 2π and (part of) [α₀, α₀+1.02ε) ghost | yes |

**M1 (fix in `referee/P8b-claims.md` §5, (T0)):** replace "a set 𝒢 ⊂ (0,U) of ghost labels" by "a set 𝒢 ⊂ [0,U) of ghost
labels". P8b's proofs use ghost/true only through Lemma P8.W(b),(c)(3′) (statements about true labels) and the last
clause of (T0); the direction α₀ of u = 0 is seen at t_a. Nothing else changes.

Other remarks on the interface (no action needed for P8a): P8b Remark (4) quotes interim constants ϑ_T = 4.3,
U_max = 6.4; the proved ones are 3.3 and 6.5 (T₀ = T₂ + 2.3U_max + 1 = 19.69). P8b's description of 𝒢 ("the hole labels
and [α₀, α₀+1.02ε)") differs from P8a's (only the label 2π and the forward labels that entered the disc); both are
admissible because (H_T) only asks for existence.

## 6. Required text fixes (P8a-claims)

* **F1 (Lemma 4(d), proof).** "both brackets are in [1, 1 + 0.6ε] … So 1 ≤ (1+θ_s)^{1+v} ≤ (1 + 0.6ε)^{2v}" yields
  θ_s ≤ 1.2vε, not the stated vε. Replace by: "the first bracket is ≤ 1 + 2.3ε² ≤ 1 + 0.0023ε (α_s ≤ 2.1ε), the second
  ≤ 1 + 0.5001ε (C ≤ 1.000001ε, τ₁ ≥ 1, |h₁| ≥ 1 − v²); their product is ≤ 1 + 0.51ε. So 1 ≤ (1+θ_s)^{1+v} ≤ (1 + 0.51ε)^v,
  θ_s ≤ 0.51vε." (True value: θ_s ≈ 0.75vε².)
* **F2 (Lemma 5(c), Λ).** "r² ∈ [2.66415, 3.35584]": the lower end is 2.664154 − 2·1.84·3.1e-6 = 2.66414. Replace 2.66415 by
  2.66414 (twice); Λ ≤ 1.33617 < 1.337 is unaffected.
* **F3 (Lemma 7(c),(d)).** "τ^{1+v} ≤ 2.0021·1.00012x/(0.4081x^{2−2v}(1−v)) ≤ 4.9064x^{−1+2v}": the left product is 4.9065.
  Write "≤ (2.002/(1−v))·1.00012x/(0.4081x^{2−2v}) ≤ 4.9063x^{−1+2v}" (drop the duplicated 1/(1−v)). Likewise in (d):
  "y_E ≤ εg_max(2.0021|h|/(εg_max))^{v/(1+v)}" with |h| ≤ 1.00012x_e gives 2.00234, not the 2.0023 of the statement;
  write 2.002003 instead of 2.0021 (then 2.00225 ≤ 2.0023), or state 2.0024. No downstream effect (power v).
* **F4 (Lemma 10, proof).** "the tangents are e^{i(π/2 ∓ δ_s)} at E₋ resp. e^{i(π/2+δ_s)} at E₊" → "e^{i(π/2−δ_s)} at E₋ and
  e^{i(π/2+δ_s)} at E₊".
* **F5 (optional, Lemma 5(c), ∂_θ log C).** The upper bound 2.67133/x uses (cos b − v)·b/sin b ≤ b cot b ≤ 1; with the
  quoted "b/sin b ≤ 1 + b²/5" alone one gets 2.671335. Say "b cot b ≤ 1".
* **F6 (optional, Theorem P8a.H, statement of 𝒢).** Add "(so 0 ∈ 𝒢; (H_T)(T0) is to be read with 𝒢 ⊂ [0,U), see RP8a-1 M1)".

## 7. Things I tried in order to break the claim (all failed)

* α → 0 down to 10^(−10⁸): curvature bounded, two-sided tangent continuous (§2).
* Pairs straddling the virtual/true junction, the hole edges ±α_s, the axis label at offsets 10⁻⁹λ, and ending
  exactly at E_Y, at all scales down to λ = 0.51ε with ε = 10⁻³⁰: N/λ^{3/2} stays 0.2887 (the front is, to 10⁻⁴, a unit
  circle at every scale ≥ ε/2; the exponents μ, μ_T are invisible for v ≤ 10⁻⁶ but correctly carried in the proof).
* Pairs (a near X₀, b near E_Y) with u_a, u′_b from 0 to 0.0246, including u_a = 0 and u′_b = 0: (X1) holds with ratio
  ≤ 0.99901 (c ≈ u_a + x_b + O(x²); the constant 0.999 is nearly sharp but valid).
* Sign conventions of (T5) and orientation of the tail (y > 0 on both sides of α₀, ψ < 0 on the tail): consistent.
* Seen-ness of the tiny tail labels x ≪ vε (covered by the t_a argument, not by the C-argument): correct.

Not checked: anything in `reports/P8a-1.md`, `code/P8a/`; [B], [D] Lemma D0, [P7] were taken as refereed (I re-proved the
two elementary facts actually used: D0(c) and Fact 0.2(i), and read [B, Lemma V(iii)] for D0(a) in Lemma 8).
