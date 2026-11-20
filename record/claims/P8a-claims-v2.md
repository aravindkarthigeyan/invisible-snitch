# P8a — claims for independent referees: design T, the touch-down data; (H_T) holds

Stream P8a, round 8. Version 2 (v1 + Lemma 11, Theorem P8a.H = hypothesis (H_T) of `referee/P8b-claims.md` §5 verbatim). **Only statements claimed PROVED, with proofs.** Formulation as always: Harry has speed
≤ 1, H(0) = 0, path fixed in advance; Snitch S′ = v(S − H)/|S − H|, S(0) = e^{iα}; vision radius ε. Plane = ℂ.

**Claimed PROVED:** Lemma 1 (straight-run coordinates), Lemma 2 (first-order transport of the tangent), Lemma 3
(second-order transport: curvature), Lemma 4 (front after run 1; the hole), Lemma 5 (tangency; local data at t₁),
Lemma 6 (forward arc), Lemma 7 (tail and the end E_Y; labels seen in run 2), Lemma 8 (virtual labels next to X₀),
Lemma 9 (bulk), Lemma 10 (hole edges at t_s), Lemma 11 (the TRUE front through the hole is C^{1,1}; the axis label),
Proposition P8a.1 (arc-wise touch-down data: (ST_end) of P7 on A₁ = [α₀, 2π − α_s], data of A₂ = [α_s, b_e]), and
**Theorem P8a.H: hypothesis (H_T) of `referee/P8b-claims.md` §5 holds for design T (D₁ = 1) for all v ≤ v_* := 10⁻⁶ and
ε ≤ ε_* := 10⁻³, with the explicit constants listed there.**
**Not claimed:** anything after t_s; anything about the VIRTUAL front of [B] on seen labels (the hole (−α_s, α_s), the stretch
(b_e, α₀)) — (H_T) uses the true front through the hole; anything for v > 10⁻⁶ (the exact Lemmas 1–3 and the exact parts of Lemmas 4, 5 hold for all v ∈ (0,1)).

**External inputs.**
* [I] `paper/main.tex`, Prop. "integrals": for H with constant unit velocity u and a candidate with ρ > 0, in polar
  coordinates (ρ, β) of r = S − H about the direction u: ρ′ = v − cos β, ρβ′ = sin β, h := ρ(cos β + v) has h′ = −(1 − v²),
  C := ρ sin β/tan^v(β/2) is constant (0 < β < π).
* [B] `paper/sec_B.tex` (doubly refereed): field F, f, A = DF, a*(ρ) (Lemma V); virtual candidates x_θ, with |x_θ′| ≤ v,
  w := |∂_θx| non-decreasing and ≥ 1, chords non-decreasing, "ρ_θ(t) ≤ ε ⇒ θ seen by t" (Lemma VC); Lemma 1:
  w_t = v w T·AT ≤ v a* w; for the **true** flow (field x/|x|, any ρ > 0): w_t/w = v sin²φ/ρ, ψ_t = −(v/ρ) sin φ cos φ,
  k_t = (v/ρ)(1 − 3 sin²φ)k + (v/ρ²) sin φ (3cos²φ − 1). Notation l, c, E = l − c, N = (2E)^{1/2}.
* [D] `referee/P6d-claims.md` (doubly refereed), Lemma D0: (a) for the virtual front, ψ_t = −vΓ(ρ) sin φ cos φ,
  |ψ_t| ≤ v|p|/m(ρ)², p := T^⊥·r, m(ρ) := max(ρ, ε); (c) if the tangent angle is k-Lipschitz in arclength on [a,b] and
  k·l(a,b) ≤ π, then E(a,b) ≤ k² l(a,b)³/24.
* [P7] `referee/P7-claims.md`: Fact 0.2(i) (N(a,b)² ≤ μ_û(a,b) := ∫_a^b|T − û|²ds for every unit vector û) and the
  statement of hypothesis (ST_end) (§2). Nothing else of P7 is used.

**Conventions.** T = e^{iψ} unit tangent of the front in the direction of increasing label, w = |∂_θ x|, k = ∂_sψ the
curvature (k = 1 for the unit circle), φ := β − ψ (angle from T to r̂, as in [B], [D]). "True front" = the curve
θ ↦ S_θ(t) of true candidates continued by the flow of x/|x − H(t)| (C^∞ in θ as long as ρ > 0); it coincides with the
virtual front on every label that has had ρ ≥ ε up to that time ([B, Lemma VC(c)] and its proof).
**Standing assumptions from §2 on:** D₁ = 1, **0 < v ≤ 10⁻⁶, 0 < ε ≤ 10⁻³**. μ := v/(1−v) ≤ 1.000002·10⁻⁶,
μ_T := 3v/(1+v). g(β) := sin β/tan^v(β/2), g_max := g(arccos v); 1 ≤ g_max ≤ e^{v²} (g(π/2) = 1; [D, proof of Theorem D]).
All numerical constants are rounded in the safe direction; they are wasteful on purpose.
Numerical verification of every formula and inequality below (not part of any proof): `code/P8a/`, `reports/P8a-1.md` §3.

---------------------------------------------------------------------------------------------------------------------

## §1. Three exact lemmas on a straight run (all v ∈ (0,1))

Throughout §1: H moves with constant unit velocity u on a time interval; coordinates are taken in the *heading frame*
(u = 1 ∈ ℂ, H at the origin); a candidate is at r = ρe^{iβ} with 0 < β < π, and **τ := tan(β/2) ∈ (0, ∞)**.

**Lemma 1 (coordinates (C, τ)).** With C = ρ g(β) (constant) and h = ρ(cos β + v):
 (a) g(β) = 2τ^{1−v}/(1+τ²), and
  ρ = (C/2)(τ^{v−1} + τ^{v+1}), y := ρ sin β = C τ^v, z := ρ cos β = (C/2)(τ^{v−1} − τ^{v+1}),
  **h = (C/2)[(1+v)τ^{v−1} − (1−v)τ^{1+v}]**.
 (b) τ ↦ (1+v)τ^{v−1} − (1−v)τ^{1+v} is a strictly decreasing bijection (0,∞) → ℝ; hence τ is strictly increasing in time
  (h′ = −(1−v²) < 0), and the state at any time of the run is determined by (C, h).
 (c) min_τ ρ = C/g_max, attained at τ² = (1−v)/(1+v) (cos β = v); ρ is decreasing in time while cos β > v.
 (d) If h > 0: τ ≤ ((1+v)C/(2h))^{1/(1−v)}. If h < 0: (2|h|/((1−v)C))^{1/(1+v)} ≤ τ, and
  τ^{1+v} = (2|h|/((1−v)C))·[1 + (1+v)Cτ^{v−1}/(2|h|)].
*Proof.* (a) sin β = 2τ/(1+τ²), cos β = (1−τ²)/(1+τ²), so g = 2τ^{1−v}/(1+τ²), ρ = C/g, y = ρ sin β = Cτ^v,
z = ρ cos β = (C/2)τ^{v−1}(1 − τ²), h = z + vρ. (b) The derivative is −(1−v²)(τ^{v−2} + τ^v) < 0; limits ±∞. (c) ρ′ = v − cos β
by [I]; (d/dτ)(τ^{v−1} + τ^{v+1}) = τ^{v−2}((1+v)τ² − (1−v)); the minimum value is C/g(arccos v). (d) From (a):
(1+v)τ^{v−1} = 2h/C + (1−v)τ^{1+v} ≥ 2h/C, resp. (1−v)τ^{1+v} = 2|h|/C + (1+v)τ^{v−1} ≥ 2|h|/C. ∎

**Lemma 2 (first-order transport).** Let θ ↦ S_θ be a C¹ family of true candidates, all with 0 < β < π on the time
interval. Put x_θ := ∂_θS_θ (heading frame) and **Ξ := x_θ + v e^{iβ} \overline{x_θ}**. Then
  **Re Ξ = ∂_θh =: a, Im Ξ = τ^v ∂_θC =: τ^v c,**
and a(θ), c(θ) do not depend on time. Conversely x_θ = (Ξ − v e^{iβ} \overline{Ξ})/(1 − v²), and (1−v)w ≤ |Ξ| ≤ (1+v)w.
In particular, writing x_θ = w e^{iψ} and φ = β − ψ: a = w(cos ψ + v cos φ), c τ^v = w(sin ψ + v sin φ).
*Proof.* Write x_θ = X + iY. Since H does not depend on θ, ∂_θz = X, ∂_θy = Y, ∂_θρ = X cos β + Y sin β,
ρ∂_θβ = −X sin β + Y cos β. Then ∂_θh = X + v∂_θρ = X(1 + v cos β) + vY sin β = Re Ξ (because
v e^{iβ}(X − iY) = v(X cos β + Y sin β) + iv(X sin β − Y cos β)). By Lemma 1, C = yτ^{−v} and ∂_θ log τ = ∂_θβ/sin β
(dτ/dβ = τ/sin β), so τ^v∂_θC = Y − v y ∂_θβ/sin β = Y − vρ∂_θβ = Y(1 − v cos β) + vX sin β = Im Ξ. C and h + (1−v²)t are
constants of the motion and smooth functions of the position, so c, a are time-independent. The map
x ↦ x + v e^{iβ}x̄ is I + vR with R a reflection: its inverse is (I − vR)/(1−v²) and its singular values are 1 ± v. ∎

**Lemma 3 (second-order transport).** In the situation of Lemma 2 let the family be C². Then
**J := a ∂_θc − c ∂_θa** does not depend on time, and the curvature k of the front satisfies, with w, ψ, φ, ρ, β, τ at
the time considered,
  **k = τ^v J/((1−v²)w³) − 𝔖, 𝔖 := (v sin φ/((1−v²)ρ))·[ ρ a ∂_θ(log C)/w² − v − cos(φ − ψ) ].**
Consequently, for two times t′ < t″ of the run (data ′ and ″):
  k″ = (τ″/τ′)^v (w′/w″)³ (k′ + 𝔖′) − 𝔖″, and (w′/w″) ≤ 1.
*Proof.* Put V := Ξ = a + icτ^v, S := I + vR_β, R_βx := e^{iβ}x̄, so x_θ = S^{−1}V. Differentiating in θ:
∂_θV = ∂_θa + i(τ^v∂_θc + vcτ^v∂_θβ/sin β), ∂_β(S^{−1}) = −vR′_β/(1−v²) with R′_βx = ie^{iβ}x̄, and
∂_θx_θ = S^{−1}∂_θV + ∂_θβ·∂_β(S^{−1})V. For a real 2×2 matrix M, (Mp)×(Mq) = det M·(p×q), and det S^{−1} = 1/(1−v²). So
 kw³ = x_θ × ∂_θx_θ = (V × ∂_θV)/(1−v²) − (v∂_θβ/(1−v²)) x_θ × R′_β(Sx_θ).
Here V × ∂_θV = τ^vJ + v(acτ^v)∂_θβ/sin β; cτ^v/sin β = ∂_θC·τ^{v−1}(1+τ²)/2 = ρ∂_θC/C (Lemma 1(a)); with x_θ = we^{iψ}:
Sx_θ = w(e^{iψ} + ve^{iφ}), R′_β(Sx_θ) = iw(e^{iφ} + ve^{iψ}), x_θ × R′_β(Sx_θ) = w² Im(e^{−iψ}·i(e^{iφ} + ve^{iψ})) = w²(cos(φ−ψ) + v);
and ∂_θβ = w∂_sβ = −w sin φ/ρ (from ρ∂_θβ = −X sin β + Y cos β = w sin(ψ − β)). Hence
 kw³ = τ^vJ/(1−v²) − (v w sin φ/((1−v²)ρ))·[ρ a ∂_θ log C − w²(v + cos(φ−ψ))],
which is the formula. J is built from the time-independent a, c. The two-time relation follows by eliminating J;
w is non-decreasing ([B, Lemma 1(i)]: w_t/w = v sin²φ/ρ ≥ 0). ∎

*Remarks.* (i) Lemma 2 gives the tilt in closed form: with Y_r := cτ^v/a = y·∂_θ(log C)/a (if a > 0),
 **tan ψ = [(1 + v cos β)Y_r − v sin β] / [1 − v cos β − v sin β·Y_r], w = a|(1 − v cos β − v sin β Y_r) + i((1+v cos β)Y_r − v sin β)|/(1−v²).**
(Real and imaginary part of (Ξ − ve^{iβ}Ξ̄)/(1−v²) with Ξ = a(1 + iY_r).) (ii) All three lemmas are checked against a direct
integration of the ODE and against finite differences in θ to ≥ 20 digits (`check_formulas.py`).

---------------------------------------------------------------------------------------------------------------------

## §2. Design T; run 1 and the hole

**Design T.** (T1) P(t) = t (i.e. (t,0)) for 0 ≤ t ≤ **t₁ := 1/(1−v) + 1** = 2 + μ.
(T2) **α₀ := arccos(v + 1/t₁)**; ρ₀e^{iβ*} := S_{α₀}(t₁) − P(t₁) (polar form, ρ₀ > 0), **û := e^{iβ*}**; P(t) = P(t₁) + (t − t₁)û for
t₁ ≤ t ≤ t_s, where **t_s := t₁ + (ρ₀ − ε)/(1−v) + ε∫₀¹ dσ/(1 − vσ(2−σ))**. Put t_a := t₁ + (ρ₀−ε)/(1−v), t₂ := t₁ + ρ₀/(1−v).
(What follows t_s is not part of this document.)

For α ∈ (0,π) let (ρ₁(α), β₁(α)), τ₁ := tan(β₁/2), be the heading-frame polar coordinates of S_α(t₁) − P(t₁) for run 1
(u = 1); the lower half is the mirror image: S_{2π−α} = \overline{S_α} during run 1. In run 1: C = g(α) (at t = 0: ρ = 1, β = α,
τ = τ_α := tan(α/2)), h(t) = cos α + v − (1−v²)t, so **h₁ := h(t₁) = −(1−v²) − (1 − cos α) < 0**, a = −sin α,
c = g′(α) = (cos α − v)τ_α^{−v}.

**Lemma 4 (run 1).** (a) *Seen.* Let α_s ∈ (0, arccos v) be defined by g(α_s) = εg_max. A true candidate α ∈ (−π, π]
is seen during [0, t₁] iff |α| ≤ α_s. For α ∈ [α_s, 2π − α_s]: ρ_α ≥ ε on [0,t₁], so virtual = true on [0,t₁]. α_s ≤ 2.1ε.
(b) *Middle.* For α ∈ [1/2, 2π − 1/2]: ρ_α(t) ≥ 0.479 on [0,t₁]; at t₁ the true front has
 1 ≤ w₁ ≤ 1.0000042, |arg ∂_αS_α(t₁) − (α + π/2)| ≤ 2.1·10⁻⁶, |k₁ − 1| ≤ 2·10⁻⁵.
(c) *Arm.* For α ∈ (0, arccos v): ρ₁ ≥ 1 + v, y(α,t₁) ≥ sin α, and the true front at t₁ satisfies
 **|k₁| ≤ (1+v)/(cos α − v) + 2.0001v**; for α ∈ (0, 1/2]: |k₁| ≤ 1.14, the tangent is e^{i(π/2+δ)} with
 **0 ≤ δ ≤ tan δ ≤ 1.1396·y(α,t₁)**, and w₁ ≤ 1.0000015(2/α)^{2v}.
(d) *Half-width of the hole.* y_s := y(α_s, t₁) satisfies
 **y_s = (εg_max)^{1/(1+v)}(2(1+v))^{v/(1+v)}(1 + θ_s), 0 ≤ θ_s ≤ vε.**
(e) |k₁| ≤ 1.14 and w₁ ≤ 1.0000052(2/χ)^{2v}, χ := min(α, 2π − α), for all α ∈ (0, 2π).

*Proof.* (a) By Lemma 1(b),(c): τ increases from τ_α to τ₁, and h₁ < 0 means cos β₁ < −v, so τ₁² > (1+v)/(1−v) > (1−v)/(1+v).
If α ≤ arccos v the minimum point is passed and min ρ = g(α)/g_max, which is ≤ ε iff α ≤ α_s (g is increasing on
(0, arccos v)); if α > arccos v, ρ is increasing and min ρ = 1 > ε. Mirror for α < 0; α = 0 is caught at 1/(1−v) < t₁, α = π
has ρ ≥ 1. α_s ≤ 2.1ε: as in [D, Theorem D.1]: τ_s^{1−v} = εg_max(1+τ_s²)/2 ≤ εg_max, so α_s ≤ 2τ_s ≤ 2(εg_max)^{1/(1−v)} ≤ 2.1ε.
(b) For α ∈ [1/2, π/2]: y′ = vy/ρ ≥ 0 ([I]: y = Cτ^v, τ increasing), so ρ ≥ y ≥ sin α ≥ sin(1/2) > 0.479. For α ∈ [π/2, π]:
X := Re S_α has X′ = v(X − t)/ρ and (X − t)′ ≤ v − 1 < 0, X(0) − 0 = cos α ≤ 0; so X − t ≤ 0, X′ ≤ 0, X ≤ cos α ≤ 0, |Im S_α| ≥ sin α,
ρ² ≥ X² + y² ≥ 1. Mirror for the lower half. By [B, Lemma 1] (true flow), w(0) = 1, k(0) = 1, t₁ ≤ 2.0000011:
log w₁ ≤ vt₁/0.479 ≤ 4.18·10⁻⁶; |ψ_t| ≤ v/(2·0.479), so the tangent angle moves by ≤ 2.09·10⁻⁶; |1 − 3 sin²φ| ≤ 2 and
|sin φ(3cos²φ − 1)| ≤ 1 give d|k − 1|/dt ≤ v[4.1754(|k−1| + 1) + 4.3585], hence |k₁ − 1| ≤ 8.534vt₁e^{4.1754vt₁} ≤ 2·10⁻⁵.
(c) h₁ = ρ₁(cos β₁ + v) with −(1−v) ≤ cos β₁ + v < 0 and |h₁| ≥ 1 − v²: ρ₁ ≥ 1 + v. y = Cτ^v is non-decreasing, y(0) = sin α.
*Curvature.* Apply Lemma 3 with t′ = 0: there w = 1, k = 1, ψ = α + π/2, φ = −π/2, ρ = 1, a∂_θ log C = −sin α·(cos α − v)/sin α,
so 𝔖′ = −(v/(1−v²))[−(cos α − v) − v − cos(−π − α)] = 0; hence k₁ = 𝒯/w₁³ − 𝔖₁, 𝒯 := (τ₁/τ_α)^v ≥ 1. By Lemma 2,
(1+v)w₁ ≥ |Ξ| ≥ Im Ξ = (cos α − v)𝒯 > 0, and w₁ ≥ 1, so 𝒯/w₁³ ≤ 𝒯/w₁ ≤ (1+v)/(cos α − v). And
|𝔖₁| ≤ (v/((1−v²)ρ₁))[ρ₁(cos α − v)/w₁² + v + 1] ≤ v/(1−v²) + v/((1−v)ρ₁) ≤ 2.0001v. For α ≤ 1/2: cos α − v ≥ 0.87758, so
|k₁| ≤ 1.13951 + 2.1·10⁻⁶ < 1.14.
*Tilt.* By Lemma 2, (1−v²)∂_αS_α(t₁) = a[(1 − v cos β₁) − iv sin β₁] + c𝒯′[−v sin β₁ + i(1 + v cos β₁)] with a = −sin α < 0,
c𝒯′ := cτ₁^v = (cos α − v)𝒯 > 0: the real part is < 0, the imaginary part is > 0 (1 ± v cos β₁ > 0), so the tangent is
e^{i(π/2+δ)} with δ ∈ [0, π/2) and
 tan δ = [sin α(1 − v cos β₁) + v sin β₁(cos α − v)𝒯]/[v sin α sin β₁ + (1 + v cos β₁)(cos α − v)𝒯]
   ≤ (1+v) sin α/((1−v)(cos α − v)𝒯) + v sin β₁/(1−v).
With 𝒯 ≥ 1, sin α ≤ y, sin β₁ = y/ρ₁ ≤ y/(1+v): tan δ ≤ y[1.000002/0.87758 + 10⁻⁶] ≤ 1.1396y.
*Stretch.* |Ξ|² = sin²α + (cos α − v)²𝒯² ≤ 𝒯², so w₁ ≤ 𝒯/(1−v). By Lemma 1(d), (1−v)τ₁^{1+v} = 2|h₁|/C + (1+v)τ₁^{v−1} with
τ₁ ≥ 1, |h₁| ≤ 1 + 0.12242 (α ≤ 1/2), C = 2τ_α^{1−v}/(1+τ_α²) ≥ 1.8776τ_α^{1−v} (τ_α ≤ tan(1/4) < 0.25535), and
1 + v ≤ 0.2554/τ_α^{1−v}; so τ₁^{1+v} ≤ 1.4512/τ_α^{1−v}, τ₁/τ_α ≤ 1.4512τ_α^{−2/(1+v)}, 𝒯 ≤ 1.4512^vτ_α^{−2v} ≤ 1.0000004(2/α)^{2v}.
(d) By Lemma 1(a),(d) with C = εg_max, |h₁| = (1−v²)(1 + (1 − cos α_s)/(1−v²)):
 y_s^{1+v} = C^{1+v}(τ₁^{1+v})^v = εg_max(2(1+v))^v·[1 + (1−cos α_s)/(1−v²)]^v·[1 + (1+v)Cτ₁^{v−1}/(2|h₁|)]^v,
and both brackets are in [1, 1 + 0.6ε] (α_s ≤ 2.1ε, C ≤ 1.000001ε, τ₁ ≥ 1, |h₁| ≥ 1 − v²). So 1 ≤ (1+θ_s)^{1+v} ≤ (1 + 0.6ε)^{2v}.
(e) (b), (c) and the mirror symmetry; for χ ≥ 1/2, 1.0000042 ≤ 1.0000052(2/π)^{2v} ≤ 1.0000052(2/χ)^{2v}. ∎

*Remark (what the front looks like at the hole).* By the formula in the proof of (c), k₁ = 𝒯/w₁³ − 𝔖₁ with 𝒯/w₁³ ≤ (1+v)³/((cos α − v)³𝒯²)
and 𝒯 = (τ₁/τ_α)^v → ∞ only like (yα)^{−v}: the curvature tends to the parabola value v/((1−v²)D₁) of N8 only in the regime
(yα)^{2v} ≪ 1. For v ≤ 10⁻⁶ and any ε ≥ 10⁻³⁰⁰ the front next to the hole is, to 10⁻³, the unit circle (k ≈ 1, δ ≈ y; numerics).
Lemma 4(c) covers both regimes.

---------------------------------------------------------------------------------------------------------------------

## §3. Tangency: the data at t₁ in the frame of run 2

For θ ∈ (0, 2π), θ ≠ α₀, let **(r(θ), b(θ))** be the polar coordinates of S_θ(t₁) − P(t₁) about the direction û (the
heading frame of run 2), τ_b := tan(b/2), and for run 2: C := r g(b), a := ∂_θ[r(cos b + v)], c := ∂_θC (Lemma 2).
A(θ) := ∂_θr. η := 0.1; I_η := {θ : |θ − α₀| ≤ η}; x := |θ − α₀|.

**Lemma 5.** (a) *(exact, all v)* For θ ∈ (0, π): **ρ₁ ∂_θβ₁ = sin β₁·t₁(cos α₀ − cos θ)/sin θ.** Hence β₁ has its unique
minimum on (0,π) at α₀, b = β₁(θ) − β* ∈ [0, π) there, b ∈ (0, π) on the lower half, and
 **∂_θb = Λ(θ) sin((θ − α₀)/2), Λ(θ) := 2t₁ sin β₁ sin((θ+α₀)/2)/(ρ₁ sin θ) > 0 (0 < θ < π):**
b has a double zero at α₀: the true front at t₁ is tangent at S_{α₀}(t₁) to the ray of run 2.
(b) 0 ≤ π/3 − α₀ ≤ 1.2·10⁻⁶; |ρ₀ − √3| ≤ 10⁻⁵; t_s ≤ t₂ ≤ 3.7321, 0 ≤ t₂ − t_s ≤ vε/(3(1−v)²); every virtual candidate has
|x_θ(t) − e^{iθ}| ≤ vt ≤ 3.74·10⁻⁶ for t ≤ t_s; P([t₁,t_s]) lies within 5·10⁻⁶ of the segment 𝒮₀ := [2, e^{iπ/3}].
The virtual candidate α₀ stays on the ray of run 2, and **P(t_s) = x_{α₀}(t_s)**; ρ_{α₀}(t_a) = ε.
(c) On I_η (⊂ [0.947, 1.148]):
 1.632 ≤ r ≤ 1.832; 1.001 ≤ Λ ≤ 1.337; 0.994 ≤ A ≤ 1.00002; 1 ≤ w₁ ≤ 1.0000042; |k₁ − 1| ≤ 2·10⁻⁵;
 **0.2501x² ≤ b ≤ 0.33425x²**; r|∂_θb| ≤ 1.2247x; 0.4081x^{2−2v} ≤ C ≤ 0.6124x^{2−2v}; 0.9935 ≤ a ≤ 1.00044;
 for θ > α₀: 0 < ∂_θ log C ≤ 2.7327/x; for θ < α₀: −2.6714/x ≤ ∂_θ log C < 0 (so C is strictly monotone on each side);
 the quantity 𝔖 of Lemma 3 at t₁ (frame of run 2) satisfies |𝔖| ≤ 3.42v.

*Proof.* (a) From C = ρg(β), h = ρ(cos β + v), g′/g = (cos β − v)/sin β: (cos β + v)∂_θC − g∂_θh = ρ∂_θβ·g(1−v²)/sin β. In run 1,
∂_θC = g(θ)(cos θ − v)/sin θ, ∂_θh = −sin θ, g(θ)/g(β₁) = ρ₁, ρ₁(cos β₁ + v) = h₁, so
(1−v²)ρ₁∂_θβ₁ = sin β₁[h₁(cos θ − v) + sin²θ]/sin θ, and h₁(cos θ − v) + sin²θ = (1−v²)(1 − t₁(cos θ − v)) = (1−v²)t₁(cos α₀ − cos θ)
(t₁(cos α₀ − v) = 1). The sign of ∂_θβ₁ is that of θ − α₀. β₁ ∈ (arccos(−v), π) (h₁ < 0), so on the upper half
b = β₁ − β* ∈ [0, π/2); the mirror point of S_α has polar angle −β₁(α) about the axis of run 1, i.e. b = 2π − β₁(α) − β*
∈ (π − β*, 2π − 2β*] ⊂ (0, π) because β₁ ≥ β* > π/2. cos α₀ − cos θ = 2 sin((θ+α₀)/2) sin((θ−α₀)/2). The tangent at α₀:
∂_θ(S_θ − P)(t₁) = (A + ir∂_θb)e^{ib}û-frame = A at θ = α₀.
(b) 1/t₁ = 1/(2+μ) ∈ [1/2 − μ/4, 1/2], so cos α₀ − 1/2 ∈ [v − μ/4, v] ⊂ [0, 10⁻⁶] and sin α₀ ≥ 0.866. Candidates (true or
virtual) have speed ≤ v: |S_{α₀}(t₁) − e^{iα₀}| ≤ vt₁ ≤ 2.1·10⁻⁶, |e^{iα₀} − e^{iπ/3}| ≤ 1.2·10⁻⁶, |P(t₁) − 2| = μ, |e^{iπ/3} − 2| = √3:
|ρ₀ − √3| ≤ 4.5·10⁻⁶. t₂ ≤ 2.0000011 + 1.73206·1.000002 ≤ 3.7321. The true candidate α₀ has b = 0: it stays on the ray, at
distance ρ₀ − (1−v)(t − t₁) ([I]), which is ε at t_a; up to t_a it is also the virtual one. For t ≥ t_a the ansatz
x_{α₀} = P + σû solves x′ = vF(x − P) iff σ′ = −1 + vf(σ), σ(t_a) = ε ([D, Claim D3(a)]); σ reaches 0 after the time
∫₀^ε dσ/(1 − vf(σ)) = ε∫₀¹dσ/(1 − vσ(2−σ)) = t_s − t_a. And t₂ − t_s = ∫₀^ε[1/(1−v) − 1/(1−vf)]dσ = ∫₀^ε v(1−f)/((1−v)(1−vf)) dσ
∈ [0, (v/(1−v)²)∫₀^ε(1−f)] = [0, vε/(3(1−v)²)]. |P(t₁) − 2| ≤ 1.1·10⁻⁶ and |P(t_s) − e^{iπ/3}| ≤ 3.74·10⁻⁶ + 1.2·10⁻⁶; convexity.
(c) I_η ⊂ [π/3 − 0.1000012, π/3 + 0.1] ⊂ [1/2, π/2], so Lemma 4(b) applies: w₁, k₁. Write p := S_θ(t₁) − P(t₁) = e^{iθ} − 2 + d,
|d| ≤ vt₁ + μ ≤ 3.1·10⁻⁶. Numbers: cos(π/3 ∓ 0.1) = 0.5839604, 0.4110438; sin(π/3 ∓ 0.1) = 0.8117822, 0.9116156;
sin(π/3 ∓ 0.05) = 0.8399535, 0.8899327.
 *r:* |e^{iθ} − 2|² = 5 − 4cos θ ∈ [2.664154, 3.355825], so |e^{iθ} − 2| ∈ [1.632223, 1.831892] and r ∈ [1.632, 1.832].
 *Λ:* sin β₁/ρ₁ = Im p/r², Im p/sin θ ∈ 1 ± 3.9·10⁻⁶ (sin θ ≥ 0.8117), sin((θ+α₀)/2) ∈ [0.839952, 0.889933], r² ∈ [2.66415, 3.35584],
 t₁ ∈ [2, 2.0000011]: Λ ≥ 4·0.999996·0.839952/3.35584 > 1.001, Λ ≤ 4.0000022·1.0000039·0.889933/2.66415 < 1.337.
 *A:* A = ∂_θS_θ·r̂ (r̂ = p/|p|). By Lemma 4(b), |∂_θS_θ(t₁) − ie^{iθ}| ≤ 4.2·10⁻⁶ + 2.1·10⁻⁶; with p₀ := e^{iθ} − 2,
 |r̂ − p₀/|p₀|| ≤ 2|d|/|p₀| ≤ 3.8·10⁻⁶; and A₀ := ie^{iθ}·p₀/|p₀| = 2 sin θ/(5 − 4cos θ)^{1/2} has A₀² = 1 − (1 − 2cos θ)²/(5 − 4cos θ) ∈
 [1 − 0.177913²/2.66415, 1] ⊂ [0.988118, 1], A₀ ≥ 0.99404. So |A − A₀| ≤ 1.02·10⁻⁵ and 0.994 ≤ A ≤ 1.00002.
 *b:* b(α₀ ± x) = ∫₀^xΛ sin(x′/2)dx′ ∈ [Λ_min, Λ_max]·4 sin²(x/4), and (x²/4)(1 − x²/48) ≤ 4 sin²(x/4) ≤ x²/4; x ≤ 0.1.
 r|∂_θb| ≤ 1.832·1.337·sin(x/2) ≤ 1.2247x. In particular b ≤ 0.0033425, τ_b ∈ [b/2, (b/2)(1 + 2.9·10⁻⁶)].
 *C:* C = 2rτ_b^{1−v}/(1+τ_b²): C ≤ 2·1.832·1.000003(0.167125x²)^{1−v} ≤ 0.6124x^{2−2v} (0.167125^{−v} ≤ 1.0000018);
 C ≥ 2·1.632·0.999997(0.12505x²)^{1−v} ≥ 0.4081x^{2−2v}.
 *a:* a = A(cos b + v) − r sin b·∂_θb, |r sin b ∂_θb| ≤ 1.2247x·0.33425x² ≤ 4.1·10⁻⁴, A(cos b+v) ∈ [0.994(1 − 5.6·10⁻⁶), 1.0000112].
 *∂_θ log C* = A/r + (cos b − v)∂_θb/sin b. |∂_θb|/b = Λ(θ) sin(x/2)/b ∈ [Λ_min/Λ_max, Λ_max/Λ_min]·cot(x/4)/2, and
 (2/x)(1 − x²/32) ≤ cot(x/4)/2 ≤ 2/x, 1 ≤ b/sin b ≤ 1 + b²/5. So (cos b − v)|∂_θb|/sin b ∈ [1.4969/x, 2.67133/x], while
 0 < A/r ≤ 1.00002/1.632 < 0.6128 ≤ 0.06128/x. For θ > α₀ (∂_θb > 0): 0 < ∂_θ log C ≤ 2.7327/x. For θ < α₀ (∂_θb < 0):
 ∂_θ log C ≤ 0.6128 − 14.969 < 0 and ≥ −2.67133/x.
 *𝔖 at t₁:* in the frame of run 2 the tangent is (A + ir∂_θb)e^{ib}, so φ = b − ψ has |sin φ| = r|∂_θb|/w₁ ≤ 1.832·1.337·x/2;
 |𝔖| ≤ (v|sin φ|/((1−v²)r))[r a|∂_θ log C|/w₁² + 1 + v] ≤ (1.337vx/(2(1−v²)))[1.832·1.00044·2.7327/x + 1.000001]
 ≤ v·0.6685007·(5.00851 + 0.1000001) ≤ 3.42v. ∎

---------------------------------------------------------------------------------------------------------------------

## §4. Run 2: the forward arc

For t ∈ [t₁, t₂] put **δ(t) := t₂ − t** (δ(t_a) = ε/(1−v), 0 ≤ δ(t_s) ≤ vε/(3(1−v)²)). In run 2 a label has
 h(t) = r(cos b + v) − (1−v²)(t − t₁) = **(1+v)(r − ρ₀) − r(1 − cos b) + (1−v²)δ(t)** (because (1−v²)(t₂ − t₁) = (1+v)ρ₀).
Coordinates in the frame of run 2 at time t: S_θ(t) − P(t) = z + iy = ρe^{iβ}, tangent e^{iψ} (ψ = angle against û).

**Lemma 6 (forward arc: θ = α₀ + x, 0 < x ≤ η; true flow).** For every t ∈ [t₁, t₂) — as long as ρ_θ > 0, which holds:
(a) h(t) ≥ 0.9938x + (1−v²)δ(t) > 0; ρ ≥ h/(1+v) ≥ 0.99379(x + δ);
(b) **0 < y ≤ 0.6124 x² (1.8435/(x+δ))^μ**;
(c) with Y_r = y∂_θ log C/a: 0 < Y_r ≤ 2.751y/x ≤ 0.1685, and **|ψ| ≤ 1.685 x (1.8435/(x+δ))^μ**; 1 ≤ w ≤ 1.015.
(d) At t = t_s, for 1.02ε ≤ x ≤ η: τ ≤ 0.3081x^{1−μ}, 0.99379x ≤ ρ ≤ 1.00193x, ρ(t) ≥ ρ(t_s) ≥ 1.0136ε for all
 t ∈ [t₁, t_s] (so these labels are true up to t_s and the front is C^∞ there), and **|k| ≤ 1.0001 x^{−μ}**.
(e) The true front at any t ∈ [t₁, t₂) is tangent to û at the candidate α₀ (ψ → 0 as x → 0).

*Proof.* (a) r − ρ₀ = ∫_{α₀}^θ A ≥ 0.994x and r(1 − cos b) ≤ 1.832·(0.33425x²)²/2 ≤ 0.10234x⁴ ≤ 1.03·10⁻⁴x (Lemma 5(c)). h = ρ(cos β + v) ≤ (1+v)ρ.
In particular ρ > 0 and (Lemma 1) 0 < β < π persists on [t₁, t₂).
(b) By Lemma 1(d), τ ≤ ((1+v)C/(2h))^{1/(1−v)}, so y = Cτ^v ≤ C^{1+μ}((1+v)/(2h))^μ; C ≤ 2rτ_b^{1−v} gives C^{1+μ} ≤ (2r)^{1+μ}τ_b, hence
 **τ ≤ τ_b((1+v)r/h)^{1+μ} and y ≤ 2rτ_b((1+v)r/h)^μ.** Now 2rτ_b ≤ 1.000003·1.832·0.33425x² ≤ 0.6124x² and
 (1+v)r/h ≤ 1.832002/(0.9938(x+δ)) ≤ 1.8435/(x+δ).
(c) By Lemma 5(c): 0 < ∂_θ log C ≤ 2.7327/x, a ≥ 0.9935: Y_r ∈ (0, 2.751y/x], and y/x ≤ 0.6124x(1.8435/x)^μ ≤ 0.06125. In
Remark (i) after Lemma 3 the denominator is ≥ 1 − v − vY_r ≥ 1 − 1.17·10⁻⁶ and the numerator lies in [−v sin β, (1+v)Y_r], with
sin β = y/ρ ≤ y/(0.99379x): |ψ| ≤ |tan ψ| ≤ 2.75101y/x ≤ 1.685x(1.8435/(x+δ))^μ. And
w ≤ 1.00044·[(1+v+vY_r)² + ((1+v)Y_r + v)²]^{1/2}/(1−v²) ≤ 1.00044·1.0141 ≤ 1.015; w ≥ 1 by [B].
(d) δ(t_s) ≤ 3.4·10⁻⁷ε ≤ 3.3·10⁻⁷x. τ ≤ 1.000003·0.167125x²·(1.84343/x)^{1+μ} ≤ 0.3081x^{1−μ} ≤ 0.0309, so β ≤ 2τ, cos β ≥ 1 − 2τ² ≥ 0.9981 > v;
τ(t) ≤ τ(t_s) on [t₁,t_s], so cos β(t) > v there and ρ is decreasing (Lemma 1(c)): ρ(t) ≥ ρ(t_s) ≥ 0.99379·1.02ε. Upper bound:
ρ = h/(cos β + v) ≤ h/0.9981 and h ≤ (1+v)·1.0000102x + 3.3·10⁻⁷x. *Curvature:* Lemma 3 with t′ = t₁, t″ = t_s:
k = (τ/τ_b)^v(w₁/w)³(k₁ + 𝔖′) − 𝔖″, with (τ/τ_b)^v ≤ ((1+v)r/h)^{v(1+μ)} = ((1+v)r/h)^μ ≤ (1.84343/x)^μ ≤ 1.0000007x^{−μ},
|k₁| ≤ 1.00002, |𝔖′| ≤ 3.42v (Lemma 5(c)), and
 |𝔖″| ≤ (v|sin φ|/((1−v²)ρ))[ρa∂_θ log C/w² + 1 + v], |sin φ| ≤ β + |ψ| ≤ (0.6162 + 1.685·1.0000007)x^{1−μ},
 |sin φ|/ρ ≤ 2.3156x^{−μ}, ρa∂_θ log C ≤ 1.00193·1.00044·2.7327 ≤ 2.7392: |𝔖″| ≤ 8.66v x^{−μ}.
So |k| ≤ [1.0000007(1.00002 + 3.5·10⁻⁶) + 8.7·10⁻⁶]x^{−μ} ≤ 1.0001x^{−μ}.
(e) For t < t₂ the true flow is smooth near the candidate α₀ (ρ_{α₀} > 0); let x → 0 in (c) with δ(t) > 0 fixed. ∎

---------------------------------------------------------------------------------------------------------------------

## §5. Run 2: the tail, the end E_Y, the labels seen

**Lemma 7.** (a) *The end.* There is a unique label **b_e = α₀ − x_e**, x_e ∈ (0, η), with C(b_e) = εg_max, and
 **1.277 ε^{1/(2−2v)} ≤ x_e ≤ 1.566 ε^{1/(2−2v)}** (in particular x_e ≥ 1.277ε and x_e ≤ 0.05).
(b) *Seen in run 2.* Every true candidate θ ∈ [b_e, α₀] is seen by t_s. Every label θ ∈ [α_s, b_e] ∪ [α₀ + 1.02ε, 2π − α_s]
 has ρ_θ(t) ≥ ε for all t ∈ [0, t_s] (so there virtual = true up to t_s), with equality only for θ = b_e at one instant
 of run 2 (and for α_s, 2π − α_s at one instant of run 1).
(c) *Tail at t_s: θ = α₀ − x, x_e ≤ x ≤ η* (true candidates; frame of run 2 at t_s):
 0.9939x ≤ |h| ≤ 1.00012x, h < 0; τ ≥ 32.4;
 **−1.00013x ≤ z ≤ −0.9939x, 0.408 x^{2−μ_T} ≤ y ≤ 0.6125 x^{2−μ_T}**, ρ ≤ 1.00203x;
 **−1.647 x^{1−μ_T} ≤ ψ < 0**; 1 ≤ w ≤ 1.015; **|k| ≤ 1.0001 x^{−μ_T}**.
(d) *E_Y := x_{b_e}(t_s) = X₀ + z_Eû + iy_Eû* with −1.00013x_e ≤ z_E ≤ −0.9939x_e and
 **ε ≤ y_E ≤ 1.000001 ε (2.0023 x_e/ε)^{v/(1+v)}**.

*Proof.* (a) By Lemma 5(c), x ↦ C(α₀ − x) is continuous and strictly increasing on (0, η], with
0.4081x^{2−2v} ≤ C ≤ 0.6124x^{2−2v}; C(α₀ − η) ≥ 0.004 > εg_max. So x_e exists, is unique, and
(ε/0.6124)^{1/(2−2v)} ≤ x_e ≤ (1.000001ε/0.4081)^{1/(2−2v)}; 1.63292^{1/2} > 1.277, 2.4504^{(1+μ)/2} < 1.566; ε^{1/(2−2v)} ≥ ε.
(c) *h:* ρ₀ − r = ∫_θ^{α₀}A ∈ [0.994x, 1.0000102x], and (1−v²)δ(t_s) ≤ 3.4·10⁻⁷ε ≤ 2.7·10⁻⁷x (x ≥ x_e ≥ 1.277ε). So
h = −(1+v)(ρ₀ − r) − r(1 − cos b) + (1−v²)δ(t_s) < 0 and 0.9939x ≤ |h| ≤ 1.000012x + 1.03·10⁻⁴x.
 *τ:* 2|h|/C ≥ 2·0.9939x/(0.6124x^{2−2v}) ≥ 3.2459x^{−1}·x^{2v} ≥ 32.45. By Lemma 1(d): τ^{1+v} ≥ 32.45, τ ≥ 32.4, τ^{v−1} ≤ 0.0309, and
 **2|h|/C ≤ (1−v)τ^{1+v} ≤ 2.002|h|/C.**
 *y:* y = Cτ^v = C(τ^{1+v})^{v/(1+v)}: y ≤ C^{1/(1+v)}(2.0021|h|)^{v/(1+v)} ≤ (0.6124)^{1/(1+v)}x^{(2−2v)/(1+v)}(2.0024x)^{v/(1+v)} ≤ 0.6125x^{(2−v)/(1+v)},
 y ≥ C^{1/(1+v)}(2|h|)^{v/(1+v)} ≥ 0.4081^{1/(1+v)}x^{(2−2v)/(1+v)}(1.9878x)^{v/(1+v)} ≥ 0.408x^{(2−v)/(1+v)}; and (2−v)/(1+v) = 2 − μ_T.
 *ψ:* a ≥ 0.9935 and −2.6714/x ≤ ∂_θ log C < 0: −2.689y/x ≤ Y_r < 0; y/x ≤ 0.6125x^{1−μ_T} ≤ 0.06126. Here cos β < −v (h < 0), so in
 Remark (i): numerator = (1 + v cos β)Y_r − v sin β < 0 with modulus ≤ |Y_r| + v sin β, denominator = 1 − v cos β − v sin β Y_r ≥ 1.
 ρ ≥ ρ(|cos β| − v) = |h| ≥ 0.9939x, so v sin β = vy/ρ ≤ 1.01·10⁻⁶y/x. Hence −2.68901y/x ≤ tan ψ < 0, |ψ| ≤ 1.647x^{1−μ_T}.
 *z, ρ:* z = h − vρ < 0, |z| ≥ |h|; ρ ≤ |z| + y gives (1−v)|z| ≤ |h| + vy, |z| ≤ 1.00013x; ρ ≤ |z|(1 + (y/|z|)²)^{1/2}, y/|z| ≤ 0.0617.
 *w:* w ≤ 1.00044[(1 + v + v|Y_r|)² + ((1+v)|Y_r| + v)²]^{1/2}/(1−v²) ≤ 1.00044·1.0135 ≤ 1.015 (|Y_r| ≤ 0.1648).
 *k:* Lemma 3 (t′ = t₁, t″ = t_s; the labels are true by (b)). τ^{1+v} ≤ 2.0021·1.00012x/(0.4081x^{2−2v}(1−v)) ≤ 4.9064x^{−1+2v},
 τ ≤ 4.9064x^{−(1−2v)/(1+v)}, τ_b ≥ b/2 ≥ 0.12505x²: τ/τ_b ≤ 39.24x^{−3/(1+v)}, **(τ/τ_b)^v ≤ 1.0000037x^{−μ_T}.**
 |sin φ| = |sin(β − ψ)| ≤ sin β + |ψ| ≤ (0.6125/0.9939 + 1.647)x^{1−μ_T}, |sin φ|/ρ ≤ 2.2771x^{−μ_T},
 ρa|∂_θ log C| ≤ 1.00203·1.00044·2.6714 ≤ 2.678: |𝔖″| ≤ 8.38v x^{−μ_T}; |k₁| ≤ 1.00002, |𝔖′| ≤ 3.42v. So
 |k| ≤ [1.0000037(1.00002 + 3.5·10⁻⁶) + 8.4·10⁻⁶]x^{−μ_T} ≤ 1.0001x^{−μ_T}.
(d) (c) at x = x_e; y_E = εg_maxτ^v ≥ ε (τ ≥ 1, g_max ≥ 1) and y_E ≤ εg_max(2.0021|h|/(εg_max))^{v/(1+v)}.
(b) *Seen.* Label α₀: at distance ε at t_a. Labels x ∈ [0.35vε, x_e]: C ≤ εg_max (monotonicity), h(t_s) ≤ −0.994x + 3.4·10⁻⁷ε ≤ 0,
 so cos β(t_s) ≤ −v < v: the minimum point of Lemma 1(c) has been passed during run 2 (cos b > v at t₁), where the true distance was
 C/g_max ≤ ε. Labels x ∈ (0, ε/2]: at t_a, r − ρ₀ ∈ [−1.0000102x, −0.994x], so h(t_a) = (1+v)(r − ρ₀) − r(1−cos b) + (1+v)ε lies in
 [0.49ε, (1+v)(ε − 0.994x)]. By Lemma 6(b)'s inequality τ ≤ τ_b((1+v)r/h)^{1+μ} (valid whenever h > 0): τ(t_a) ≤ 0.1672x²(3.74/ε)^{1+μ}
 ≤ 0.3127x(3.74/ε)^μ (x²/ε ≤ x/2), and xε^{−μ} ≤ ε^{1−μ}/2 ≤ 1/2, so τ ≤ 0.157 and τ² ≤ 0.0491x(3.74/ε)^μ. Then cos β ≥ 1 − 2τ² and
 ρ(t_a) = h/(cos β + v) ≤ (ε − 0.994x)(1 + 2.11τ²) ≤ ε − 0.994x + 2.11·0.0491·3.74^μ·xε^{1−μ} ≤ ε − 0.89x < ε:
 the true candidate is within ε of Harry at t_a.
 *Not entering the disc.* Run 1: Lemma 4(a). Run 2: forward labels x ≥ 1.02ε with x ≤ η: Lemma 6(d). Tail x ∈ [x_e, η]: ρ ≥ C/g_max ≥ ε
 (Lemma 1(c), monotonicity of C), equality iff x = x_e at the instant cos β = v. Labels with |θ − α₀| ≥ η: Lemma 9(a) below. ∎

---------------------------------------------------------------------------------------------------------------------

## §6. The virtual labels next to X₀

**Lemma 8.** At time t_s, for every label θ = α₀ + x with 0 ≤ x ≤ η, the VIRTUAL front has tangent e^{iψ}, relative to û, with
 **|ψ(θ, t_s)| ≤ 1.69 x^{1−μ}**, and 1 ≤ w(θ,t_s) ≤ 1.0151. (For x ≥ 1.02ε the virtual front is the true one.) In particular
ψ(α₀, t_s) = 0: at touch-down the virtual front is tangent to Harry's heading at X₀ = P(t_s).

*Proof.* For 1.02ε ≤ x ≤ η this is Lemma 6(c),(d) at t = t_s ((1.8435/(x+δ))^μ ≤ 1.0000007x^{−μ}). Let 0 < x ≤ 2ε. On [0, t_a] the
label is true: in run 1 by Lemma 4(a); in run 2, ρ_θ(t) > ε for t < t_a because h_θ(t) − h_{α₀}(t) = (1+v)(r − ρ₀) − r(1 − cos b) ≥ 0.9938x > 0, i.e.
(1+v)ρ_θ ≥ h_θ > h_{α₀} = (1+v)ρ_{α₀}(t) ≥ (1+v)ε for t ≤ t_a. So at t_a the virtual front on [α₀, α₀ + 2ε] is the true one and by
Lemma 6(b),(c) with δ(t_a) ≥ ε:
 |ψ(t_a)| ≤ 1.685x(1.8435/(x+ε))^μ, 0 ≤ y(t_a) ≤ 0.6124x²(1.8435/(x+ε))^μ, w(t_a) ≤ 1.015 (and ψ(t_a) = 0 = y(t_a) at x = 0).
On [t_a, t_s] (length I := t_s − t_a ≤ ε/(1−v)) use the virtual field. With r = x_θ − P = z + iy in the frame of run 2:
r′ = vF(r) − û, so y′ = v(f(ρ)/ρ)y with 0 ≤ f/ρ ≤ a* ≤ 2/ε: 0 ≤ y(t) ≤ y(t_a)e^{2vI/ε}. By [D, Lemma D0(a)], |ψ_t| ≤ v|p|/m(ρ)² with
p = T × r = y cos ψ − z sin ψ, |p| ≤ y + ρ|ψ|, ρ/m(ρ)² ≤ 1/ε, 1/m(ρ)² ≤ 1/ε²: |ψ|′ ≤ (v/ε)|ψ| + vy/ε² (a.e.; |ψ| is Lipschitz). Gronwall:
 |ψ(t_s)| ≤ e^{vI/ε}[|ψ(t_a)| + (vI/ε²)e^{2vI/ε}y(t_a)] ≤ 1.0000011[1.685 + 1.000004·10⁻⁶·0.6124x/ε]x(1.8435/(x+ε))^μ ≤ 1.6851x(1.8435/x)^μ
(x/ε ≤ 2), which is ≤ 1.69x^{1−μ}. [B, Lemma 1(i)]: w(t_s) ≤ w(t_a)e^{2vI/ε} ≤ 1.015·1.0000021. For x = 0 the same argument gives ψ ≡ 0. ∎

---------------------------------------------------------------------------------------------------------------------

## §7. The bulk and the hole edges at t_s

**Lemma 9 (bulk).** Let θ ∈ (0, 2π) with |θ − α₀| ≥ η. (a) Its virtual candidate satisfies ρ_θ(t) ≥ 0.0049 for t ∈ [t₁, t_s]; if
moreover χ := min(θ, 2π−θ) ≤ 0.0021, then ρ_θ(t) ≥ 0.497 on [t₁,t_s]. (b) If θ ∈ [α_s, 2π − α_s], then at t_s the front near θ is
the true one, C^∞, with **|k| ≤ 1.22** and w ≤ 1.00036(2/χ)^{2v}.
(c) For every label θ ∈ [α₀, 2π − α_s] ∪ [α_s, b_e]: w(θ, t_s) ≤ 1.0151(2/χ)^{2v}. Consequently, for labels θ₁ < θ₂ in one of the two
arcs, Δ := θ₂ − θ₁: l_{t_s}(θ₁,θ₂) ≤ 1.0152·max(Δ, 0.02); U₁ := l_{t_s}(α₀, 2π − α_s) ≤ 5.3, U₂ := l_{t_s}(α_s, b_e) ≤ 1.07.

*Proof.* (a) By Lemma 5(b) the candidate is within 3.74·10⁻⁶ of e^{iθ} and P(t) within 5·10⁻⁶ of 𝒮₀, which lies on the tangent line
of the unit circle at e^{iπ/3}; dist(e^{iθ}, that line) = 1 − cos(θ − π/3) ≥ 1 − cos(0.1 − 1.2·10⁻⁶) ≥ 0.004995. For χ ≤ 0.0021:
|e^{iθ} − 1| ≤ 0.0021 and dist(1, 𝒮₀) = 1/2 (the foot (5/4, √3/4) of the perpendicular is the midpoint of 𝒮₀).
(b) Virtual = true up to t_s by Lemma 4(a) and (a). At t₁: |k₁| ≤ 1.13951, w₁ ≤ 1.0000052(2/χ)^{2v} (Lemma 4). On [t₁,t_s]
(length ≤ ρ₀/(1−v) ≤ 1.73207), [B, Lemma 1] with ρ ≥ 0.0049: w grows by ≤ e^{v·1.73207/0.0049} ≤ 1.000354;
d|k|/dt ≤ (2v/ρ)|k| + v/ρ² gives |k(t_s)| ≤ (1.13951 + 10⁻⁶·1.73207/0.0049²)e^{2·10⁻⁶·1.73207/0.0049} ≤ (1.13951 + 0.07215)·1.00071 < 1.22.
(c) Lemma 6(c), 7(c), 8 on I_η (there χ ≤ 1.15, (2/χ)^{2v} ≥ 1) and (b) elsewhere. For an interval J of length Δ ≥ 0.02,
∫_J(2/χ)^{2v}dθ ≤ 2∫₀^{Δ/2}(2/χ)^{2v}dχ = Δ(4/Δ)^{2v}/(1−2v) ≤ 1.000013Δ. U₁ ≤ 1.0151·0.1 + 1.00036·1.000013·(2π − α₀ − 0.1) ≤ 0.1016 + 5.139;
U₂ ≤ 0.1016 + 1.0004·0.9472. ∎

**Lemma 10 (the edges of the hole at t_s).** Let E₋ := x_{2π−α_s}(t_s), E₊ := x_{α_s}(t_s), G := E₊ − E₋. Then
(a) 2y_s ≤ |G| ≤ 1.00001·2y_s (y_s as in Lemma 4(d));
(b) the tangent directions ψ₋, ψ₊ of the front at E₋, E₊ satisfy |ψ₊ − arg G| ≤ 0.58|G|, |arg G − ψ₋| ≤ 0.58|G|;
(c) on both sides the front is the true one with |k| ≤ 1.22 (Lemma 9(b)). Hence, for the curve "A₁, then the segment
[E₋,E₊], then A₂", the tangent direction at arclength distance s from the midpoint of the gap differs from arg G by ≤ 1.22 s
+ 0.58|G| ≤ 2.4 s (s ≥ |G|/2).

*Proof.* At t₁, by symmetry, G(t₁) = 2iy_s, and the tangents are e^{i(π/2 ∓ δ_s)} at E₋ resp. e^{i(π/2+δ_s)} at E₊ with
0 ≤ δ_s ≤ 1.1396y_s = 0.5698|G(t₁)| (Lemma 4(c); α_s ≤ 2.1ε ≤ 1/2). (The mirror label 2π − α has tangent −\overline{∂_αS_α}.) On [t₁,t_s]
both points are true candidates at distance ≥ 0.497 from P (Lemma 9(a)), and so is the whole segment between them (|G| is
non-decreasing by [B, Lemma VC(b)] and (G)′ = v(r̂₊ − r̂₋) gives |G|′ ≤ v|G|/0.49: |G(t)| ≤ 1.000004|G(t₁)| ≤ 0.0043, proving (a);
every point of the segment is within 0.0022 + 0.0043 of 1). Let Q(e, r) := e × A(r)e = −sin(2(arg r − arg e))/(2|r|) for a unit vector e
(A(r) = Π/|r|). Then ψ_±′ = vQ(T_±, r_±) ([B, Lemma 1(ii)]), and, since r̂₊ − r̂₋ = ∫₀¹A(r₋ + sG)G ds,
(arg G)′ = Ĝ × G′/|G| = v∫₀¹Q(Ĝ, r₋ + sG)ds. Q is 1/|r|-Lipschitz in arg e and has |∇_rQ| ≤ 3/(2|r|²). So, with ρ_* := 0.49,
D_± := |ψ_± − arg G| obey D_±′ ≤ (v/ρ_*)D_± + 1.5v|G|/ρ_*², and
D_±(t_s) ≤ e^{1.74v/ρ_*}[D_±(t₁) + 1.74v·1.5|G(t_s)|/ρ_*²] ≤ 1.000004(0.5698 + 1.1·10⁻⁵)|G(t_s)| ≤ 0.58|G|. (c): Lemma 9(b), and
integration of the curvature along each arc. ∎

**Lemma 11 (the true front through the hole; the axis label).** (a) *Trajectories.* For every α ∈ (0, 2π) the true
trajectory S_α (solution of S′ = v(S − P)/|S − P|) exists for all t ∈ [0, t_s] and never meets Harry (in run 1, C = g(α) > 0, so
ρ ≥ C/g_max > 0; in run 2, b ∈ (0,π) for α ≠ α₀ by Lemma 5(a), same argument; α₀: ρ = ρ₀ − (1−v)(t − t₁) > 0 for t < t₂, and t_s ≤ t₂; if t_s = t₂ the label α₀ is caught exactly at t_s — it is a seen label, replaced by the virtual one in (H_T)). For 0 < |α| < α_s it passes within ε of Harry during run 1 (it is seen) but is not caught. The
single label α = 0 (≡ 2π) is caught at t₀ = 1/(1−v) < t₁: **it has no trajectory after t₀.**
(b) *The axis point.* Z₁ := lim_{α→0±} S_α(t₁) exists and equals P(t₁) − (1+v) (on the axis); more precisely
|S_α(t₁) − Z₁| ≤ 1.01(y(α,t₁) + 1 − cos α), and y(α,t₁) ≤ 1.01 g(α)^{1/(1+v)} → 0 as α → 0. The curve Γ₁ := {S_α(t₁): 0 < |α| ≤ 1/2} ∪ {Z₁} (labels α ∈ [−1/2, 1/2])
is a C¹ arc of finite length whose unit tangent is Lipschitz in arclength with constant 1.14; its tangent at Z₁ is i
(perpendicular to the axis).
(c) *At t_s.* Let Φ be the flow map of the true field x ↦ v(x − P(t))/|x − P(t)| from t₁ to t_s. On the 0.01-neighbourhood of the
point 1, Φ is a C^∞ diffeomorphism onto its image (distance ≥ 0.48 from P(t), t ∈ [t₁,t_s]). Put Z_s := Φ(Z₁) = lim_{α→0±}S_α(t_s).
The curve Γ_s := Φ(Γ₁ ∩ {|α| ≤ 0.005}) is a C¹ arc through Z_s whose unit tangent is Lipschitz in arclength with constant 1.22, and it
joins the true front of the labels outside the hole C¹-smoothly (it IS the true front for α ≠ 0). For all α ∈ (0,2π):
|S_α(t) − e^{iα}| ≤ vt ≤ 3.74·10⁻⁶ (t ≤ t_s), |Z_s − 1| ≤ 3.74·10⁻⁶, and the bounds of Lemma 9(b) (|k| ≤ 1.22, w ≤ 1.00036(2/χ)^{2v})
hold for the true front at every label θ ∈ (0, 2π) with |θ − α₀| ≥ η, hole labels included.
(d) *Convention.* In (H_T) the label α = 0 is a ghost label carrying the point Z_s. Nothing has to be seen there (α = 0 was
caught, a fortiori seen, at t₀).

*Proof.* (a) Lemma 1(c): on a straight run ρ ≥ C/g_max whenever 0 < β < π; C = g(α) > 0 in run 1 for α ∈ (0,π) (mirror for the lower
half); in run 2, C = rg(b) > 0 since b ∈ (0,π). Seen for |α| ≤ α_s: Lemma 4(a). α = 0: on the axis ahead of Harry, ρ′ = −(1−v), ρ(0) = 1.
(b) By Lemma 1(a),(d) at t₁ (h₁ < 0, |h₁| = 1 − v² + (1 − cos α)): y^{1+v} = C(2|h₁|/(1−v))^v[1 + (1+v)Cτ₁^{v−1}/(2|h₁|)]^v ≤ C·2.3^v·1.6^v
(C ≤ 1.000001, |h₁| ≤ 1.13, τ₁ ≥ 1), so y(α,t₁) ≤ 1.01g(α)^{1/(1+v)} → 0 as α → 0. z = h₁ − vρ₁ and ρ₁ = (z² + y²)^{1/2} give
(z < 0, |z| ≤ ρ₁ ≤ |z| + y) (1−v)|z| ≤ |h₁| ≤ (1−v)|z| + vy, so | |z| − (1+v) | ≤ (1 − cos α + vy)/(1−v). Hence Z₁ = P(t₁) − (1+v),
the same from below by symmetry. Tangent: by Lemma 4(c) the tangent at label α ∈ (0,1/2] is e^{i(π/2+δ)}, 0 ≤ δ ≤ 1.1396y → 0, and at
the mirror label it is −\overline{e^{i(π/2+δ)}} = e^{i(π/2−δ)} → i. Length: w₁ ≤ 1.0000015(2/|α|)^{2v} is integrable. So the arclength
parametrisation σ ↦ Γ₁(σ) is continuous, C^∞ off the point Z₁ with |Γ₁′| = 1, and Γ₁′ extends continuously by i at Z₁; therefore Γ₁ is C¹
(a continuous map which is differentiable off one point with a continuous extension of the derivative is C¹). The tangent angle is
continuous on the arc and has derivative k₁, |k₁| ≤ 1.14, off one point (Lemma 4(c),(e)): it is 1.14-Lipschitz.
(c) For |α| ≤ 0.005, |S_α(t₁) − 1| ≤ 0.005 + 2.1·10⁻⁶ and candidates move by ≤ 1.74v during run 2; P(t) is within 5·10⁻⁶ of 𝒮₀ and
dist(1, 𝒮₀) = 1/2 (Lemma 9(a)): the true field is C^∞ with bounded derivatives on the 0.02-neighbourhood of 1 for t ∈ [t₁,t_s], so Φ is a
C^∞ diffeomorphism there, Γ_s is C¹, and Φ(Z₁) = lim S_α(t_s). Off the label 0, Γ_s is the true front; the curvature law of
[B, Lemma 1(iii)] (true flow) with ρ ≥ 0.0049 gives, exactly as in the proof of Lemma 9(b), |k(t_s)| ≤ (1.13951 + 0.07215)·1.00071 < 1.22
and the bound on w at every label θ ≠ 0 with |θ − α₀| ≥ η (Lemma 4(c),(e) hold for ALL α ∈ (0, 2π), hole labels included; Lemma 9(a)
holds for the true candidates of all labels, with the same proof: speed v, distance from 𝒮₀). The tangent angle of Γ_s is continuous
with derivative bounded by 1.22 off one point: 1.22-Lipschitz. Speed ≤ v gives the position bounds; Z_s is a limit of such points.
(d) is a convention. ∎

---------------------------------------------------------------------------------------------------------------------

## §8. Proposition P8a.1 — the touch-down data arc by arc (P7's form)

> **Proposition P8a.1.** Let D₁ = 1, 0 < v ≤ 10⁻⁶, 0 < ε ≤ 10⁻³, and let P follow design T up to t_s (so t_s ≤ 3.7321, and P is 1-Lipschitz, fixed in advance). Let x_θ be the virtual candidates of P, û the heading of run 2,
> α_s, α₀, b_e = α₀ − x_e as in Lemmas 4, 5, 7. Then:
>
> **(0) Base and seen labels.** P(t_s) = x_{α₀}(t_s) =: X₀, and the virtual front is tangent to û at X₀. Every true candidate
> with label in [−α_s, α_s] ∪ [b_e, α₀] has been seen by t_s. The labels not yet known to be seen form the two arcs
> A₁ := [α₀, 2π − α_s] and A₂ := [α_s, b_e]; on [α_s, b_e] ∪ [α₀ + 1.02ε, 2π − α_s] the virtual front at t_s is the true front.
>
> **(1) (ST_end) on A₁, verbatim.** Label A₁ by u := l_{t_s}(α₀, ·) ∈ [0, U₁], U₁ ≤ 5.3, λ := u_b − u_a. With
> **λ₀ := 1/40, c_sep := 0.024**, and for any a′ ∈ (0, 1 − 3v], **C₀ := 5.4 λ₀^{1−3v−a′}** (so C₀λ₀^{a′} ≤ 0.14 ≤ 1):
>  (E1) N(a,b;t_s) ≤ 5.4 λ^{3/2−μ} ≤ C₀ λ^{1/2+a′} for all pairs in A₁ with ε/2 ≤ λ ≤ λ₀;
>  (E2) c(a,b;t_s) ≥ c_sep for all pairs in A₁ with λ > λ₀.
> So hypothesis (ST_end) of P7 §2 holds at the leg start t_s for the construction of P7 §1 from (t_s, a_s = α₀) cut at
> b_E = 2π − α_s (e.g. a′ = 1/2: C₀ = 5.4·40^{−1/2+3v} ≤ 0.86).
>
> **(2) The arc A₂ at t_s** (labels: arclength at t_s; U₂ ≤ 1.07): all its labels are true, the front is C^∞, and
>  (E1) N(a,b;t_s) ≤ 0.36 λ^{3/2−μ_T} for all pairs in A₂ with ε/2 ≤ λ ≤ λ₀; (E2) c(a,b;t_s) ≥ 0.024 for all pairs with λ > λ₀;
>  pointwise: |k| ≤ 1.22 max(1, (α₀ − θ)^{−μ_T}); and for the tail θ = α₀ − x, x_e ≤ x ≤ 0.1, in the frame (X₀; û, iû):
>  position zû + iyû with −1.00013x ≤ z ≤ −0.9939x, 0.408x^{2−μ_T} ≤ y ≤ 0.6125x^{2−μ_T}; tangent e^{iψ}û, −1.647x^{1−μ_T} ≤ ψ < 0;
>  hence μ_û(a,b) ≤ 1.647² l_{t_s}(a,b)·(α₀ − a)^{2−2μ_T} for pairs a < b ≤ b_e of the tail. The end E_Y = x_{b_e}(t_s):
>  1.277ε^{1/(2−2v)} ≤ x_e ≤ 1.566ε^{1/(2−2v)}, z_E ∈ [−1.00013x_e, −0.9939x_e], ε ≤ y_E ≤ 1.000001ε(2.0023x_e/ε)^{v/(1+v)}.
>
> **(3) Forward arc, pointwise** (θ = α₀ + x, 0 ≤ x ≤ 0.1; u ∈ [x, 1.0151x]): |ψ| ≤ 1.69x^{1−μ} (virtual front, all x);
>  for x ≥ 1.02ε: |k| ≤ 1.0001x^{−μ}, lateral offset 0 < y ≤ 0.6124x²(1.8435/x)^μ, distance from X₀ in [0.99379x, 1.00193x].
>
> **(4) The hole.** A₁ ends at E₋ = x_{2π−α_s}(t_s), A₂ starts at E₊ = x_{α_s}(t_s); |E₊ − E₋| ∈ [2y_s, 2.00002y_s],
>  y_s = (εg_max)^{1/(1+v)}(2(1+v))^{v/(1+v)}(1+θ_s), 0 ≤ θ_s ≤ vε; the tangents at E_∓ make angles ≤ 0.58|E₊ − E₋| with E₊ − E₋;
>  |k| ≤ 1.22 on both sides; α_s ≤ 2.1ε.
>
> **(5) Global.** Every virtual candidate satisfies |x_θ(t) − e^{iθ}| ≤ 3.74v for t ≤ t_s. Labels with |θ − α₀| ≥ 0.1 kept distance
>  ≥ 0.0049 from Harry during run 2. No constant depends on ε.

*Proof.* (0): Lemma 5(b), Lemma 8 (tangency), Lemma 4(a), Lemma 7(b). (3): Lemma 8, Lemma 6. (4): Lemma 10, Lemma 4. (5): Lemma 5(b), 9(a).

**(1), (E1).** On the forward zone (0 ≤ x ≤ 0.1), x ≤ u ≤ 1.0151x since 1 ≤ w ≤ 1.0151 (Lemma 8). So a label with u ≥ 1.04ε has
x ≥ 1.02ε: it is true, and all labels of A₁ with u ≥ 1.04ε form a C^∞ arc on which, by Lemma 6(d) and Lemma 9(b),
 |k| ≤ 1.0001x^{−μ} ≤ 1.0002u^{−μ} if x ≤ 0.1, |k| ≤ 1.22 otherwise; so |k| ≤ 1.22 max(1, u_a^{−μ}) on {u ≥ u_a} for any u_a ≥ 1.04ε.
Let (a,b) be a pair in A₁ with ε/2 ≤ λ ≤ λ₀.
 *Far case: u_a ≥ max(λ, 1.04ε).* The tangent angle is K-Lipschitz in arclength on [a,b] with K := 1.22λ^{−μ} (u_a^{−μ} ≤ λ^{−μ} if u_a ≤ 1,
 and 1 ≤ λ^{−μ}); Kλ ≤ π. By [D, Lemma D0(c)] (l_{t_s}(a,b) = λ): E ≤ K²λ³/24, N ≤ (1.22/√12)λ^{3/2−μ} ≤ 0.353λ^{3/2−μ}.
 *Near case: u_a < max(λ, 1.04ε) ≤ 2.08λ.* Then u_b < 3.08λ ≤ 0.077, so the pair lies in the forward zone, where
 |T − û| ≤ |ψ| ≤ 1.69x^{1−μ} ≤ 1.69u^{1−μ} (Lemma 8). By [P7, Fact 0.2(i)]: N² ≤ ∫_a^b|T − û|²ds ≤ 1.69²u_b^{3−2μ}/(3 − 2μ), so
 N ≤ (1.69/1.732)(3.08λ)^{3/2−μ} ≤ 0.9758·5.4055 λ^{3/2−μ} ≤ 5.3λ^{3/2−μ}.
Finally λ^{3/2−μ} ≤ λ^{3/2−3v} = λ^{1/2+a′}λ^{1−3v−a′} ≤ λ₀^{1−3v−a′}λ^{1/2+a′} (μ ≤ 3v, λ ≤ λ₀ < 1).
**(1), (E2).** Let θ₁ < θ₂ in A₁ with λ > 1/40, Δ := θ₂ − θ₁. By Lemma 9(c), 1/40 < 1.0152 max(Δ, 0.02), so Δ ≥ 0.0246; and
Δ ≤ 2π − α₀. By (5), c ≥ |e^{iθ₂} − e^{iθ₁}| − 7.5·10⁻⁶ = 2 sin(Δ/2) − 7.5·10⁻⁶ ≥ min(2 sin 0.0123, 2 sin(α₀/2)) − 7.5·10⁻⁶ ≥ 0.0245 > 0.024.
C₀λ₀^{a′} = 5.4λ₀^{1−3v} ≤ 5.4/39.99.

**(2).** All labels of A₂ are true up to t_s (Lemma 7(b)) and at distance > 0 from Harry, so the front is C^∞; by Lemma 7(c) and
Lemma 9(b), |k| ≤ 1.0001x^{−μ_T} on the tail (x = α₀ − θ ∈ [x_e, 0.1]) and |k| ≤ 1.22 elsewhere. So the tangent angle is K-Lipschitz on
A₂ with K := 1.22x_e^{−μ_T}, and x_e ≥ 1.277ε ≥ ε gives x_e^{−μ_T} ≤ ε^{−μ_T} ≤ (2λ)^{−μ_T} ≤ λ^{−μ_T} for λ ≥ ε/2 (λ < 1/2). [D, Lemma D0(c)]
(Kλ ≤ 1.22λ^{1−μ_T} ≤ π): N ≤ (1.22/√12)λ^{3/2−μ_T} ≤ 0.36λ^{3/2−μ_T}. (E2): as in (1), with Δ ≤ b_e − α_s < α₀ < π, 2 sin(Δ/2) ≥ 2 sin 0.0123.
The pointwise data are Lemma 7(c),(d),(a); μ_û(a,b) = ∫_a^b|T − û|²ds ≤ sup|ψ|²·l, and x ↦ x^{1−μ_T} is increasing. ∎

**Corollary (what P7 gives from (1)).** For a′ ∈ (0, 1−3v] put γ := min(a′/2, 1/4), R := min(1/1280, (γ/(400C₀))^{1/a′}) (this is P7.E's R,
since λ₀/32 = 1/1280 < c_sep/16). If ε ≤ R/64 and v ≤ min(10⁻⁶, 2·10⁻¹¹γ², 10⁻⁶γR/23.2) (4U₁ + 2 ≤ 23.2), then by Corollary P7.E
(if P7 is confirmed by its referees) Construction C from (t_s, α₀) cut at 2π − α_s keeps the invariants (J1), (J2), sees every label
of A₁ and stops within time 2U₁/(1−v) ≤ 10.7 of t_s at arclength distance ≤ ε from E₋. With a′ = 0.99: C₀ ≤ 5.4·40^{−0.0099} ≤ 5.21,
γ = 1/4, R ≥ (1/8336)^{1/0.99} ≥ 1.09·10⁻⁴; with a′ = 1/2: C₀ ≤ 0.86, R ≥ 5.2·10⁻⁷. *(This corollary is a citation of P7, not an
independent claim.)*

---------------------------------------------------------------------------------------------------------------------


## §9. Theorem P8a.H — hypothesis (H_T) of P8b holds for design T

Notation of `referee/P8b-claims.md` §§1, 5: t₂ there := our t_s; n̂ := û; "working front", "true label", "ghost label" as in
P8b §1 with t_w = t_s. (Our t₂ = t₁ + ρ₀/(1−v), the true catch time of α₀, is not used in this section.)

**The curve x⁰.** For α ∈ [α₀, 2π + b_e] (labels mod 2π) let
 Y(α) := the virtual candidate x_α(t_s) of [B] if α ∈ [α₀, α₀ + 1.02ε];
 Y(α) := the true candidate S_α(t_s) if α ∈ [α₀ + 1.02ε, 2π + b_e], α ≠ 2π (hole labels 0 < |α − 2π| < α_s included);
 Y(2π) := Z_s (Lemma 11).
The two definitions agree at α₀ + 1.02ε and on a neighbourhood to its right, and virtual = true on [α₀ + 1.02ε, 2π − α_s] ∪
[2π + α_s, 2π + b_e] (Lemma 7(b)). x⁰ := Y reparametrised by arclength u ∈ [0, U] from Y(α₀) = X₀; Θ(u) := the label of x⁰(u).
𝒢 := {u: Θ(u) = 2π} ∪ {u: Θ(u) ∈ [α₀, α₀ + 1.02ε) and the true candidate Θ(u) was within ε of Harry at some time ≤ t_s}.

> **Theorem P8a.H.** Let D₁ = 1. **(H_T) holds for design T for all v ∈ (0, v_*] and ε ∈ (0, ε_*], v_* := 10⁻⁶, ε_* := 10⁻³**, i.e.
> with the absolute constants
>  **v_T = 10⁻⁶, ε_T = 10⁻³, T₂ = 3.74, U_max = 6.5, a′ = 1/2, C₀ = 0.86, C_z = 1.57, λ₀ = 1/40, c_sep = 0.024, γ_T = 1/4, ϑ_T = 3.3,
>  G_T = 0.05,**
> for all v ∈ (0,v_T], ε ∈ (0,ε_T]: t_s ≤ T₂, and with n̂ := û and the curve x⁰: [0,U] → ℝ² above, which is C¹ with |∂_ux⁰| ≡ 1 and
> 1 ≤ U ≤ U_max, the following hold at time t_s (u′ := U − u; T = tangent of x⁰; λ := u_b − u_a):
>  (T0) x⁰(0) = P(t_s) (= X₀). Every u ∉ 𝒢 is true, and every direction θ ∈ [0,2π) is seen by Harry during [0,t_s] or is the
>   direction of a true label.
>  (T1) N(a,b) ≤ C₀ λ^{1/2+a′} for all pairs with ε/2 ≤ λ ≤ λ₀; and C₀λ₀^{a′} ≤ 1.
>  (T2) c(a,b) ≥ min(c_sep, (u_a + u′_b)/2) for all pairs with λ > λ₀.
>  (T3) |T(u) − n̂| ≤ ϑ_T max(u, ε/2)^{γ_T} for u ≤ G_T.
>  (T4) |T(u) − n̂| ≤ ϑ_T max(u′, ε/2)^{γ_T} for u′ ≤ G_T.
>  (T5) P(t_s) − x⁰(U) = z₀n̂ + y₀n̂^⊥ with 0 ≤ z₀ ≤ C_z ε^{1/4} and |y₀| ≤ ϑ_T (z₀ + ε)(ε/2)^{γ_T}.
> **Sharper forms actually proved** (P8b may use any of them): (T1) in the form N(a,b) ≤ 5.4 λ^{3/2−3v}, hence with any
> a′ ∈ (0, 1 − 3·10⁻⁶] and C₀ = 5.4·λ₀^{1−3·10⁻⁶−a′} (a′ = 0.99: C₀ = 5.21; a′ = 1/2: C₀ = 0.86); (T3) |T − n̂| ≤ 1.69u^{1−μ};
> (T4) |T − n̂| ≤ 1.647(x_e + u′)^{1−μ_T}; (T5) 1.269ε^{1/(2−2v)} ≤ z₀ ≤ 1.567ε^{1/(2−2v)}, ε ≤ |y₀| ≤ 1.000001ε(2.0023x_e/ε)^{v/(1+v)}.

*Proof.* t_s ≤ 3.7321 (Lemma 5(b)).
**x⁰ is C¹, |∂_ux⁰| = 1, 1 ≤ U ≤ 6.5.** Y is C¹ in the label with |∂_αY| ≥ 1 on [α₀, 2π) and (2π, 2π + b_e]: on [α₀, α₀ + 1.02ε] it is the
virtual front ([B, Lemma VC(a)]); beyond, the true front (C^∞, w ≥ 1); they coincide near α₀ + 1.02ε (Lemma 6(d) and its proof: every
forward label with 0.99379x > ε has ρ > ε on [0,t_s]). Near the label 2π, Y is the arc Γ_s of Lemma 11(c), a C¹ arc of finite
length. So the arclength parametrisation is C¹ with unit speed. Length: Lemma 9(c) and Lemma 11(c) give w ≤ 1.0151(2/χ)^{2v} at every
label ≠ 2π, so U ≤ 1.0151·0.2 + 1.00036·1.000013·2π ≤ 6.5; and U ≥ |Y(α₀ + π) − X₀| ≥ 2 − 7.5·10⁻⁶ ≥ 1. Also, as in Lemma 9(c):
**l(a,b) ≤ 1.0152 max(Δ, 0.02)** for labels at distance Δ := Θ_b − Θ_a (the hole labels obey the same bound for w).
**(T0).** x⁰(0) = x_{α₀}(t_s) = P(t_s) (Lemma 5(b)). If u ∉ 𝒢: either Θ(u) ∉ [α₀, α₀ + 1.02ε), Θ(u) ≠ 2π, and then x⁰(u) = S_Θ(t_s) with S_Θ
defined on [0,t_s] (Lemma 11(a)); or Θ(u) ∈ (α₀, α₀ + 1.02ε) and the true candidate was never within ε of Harry on [0, t_s]: then
the virtual candidate has had ρ ≥ ε throughout, so it equals the true one ([B, Lemma VC(c)] and its proof), S_Θ is defined on [0,t_s]
and x⁰(u) = S_Θ(t_s). (Θ = α₀ is in 𝒢: ρ_{α₀}(t_a) = ε.) Directions: θ ∈ [−α_s, α_s] are seen in run 1 (Lemma 4(a)); θ ∈ [b_e, α₀] are seen
in run 2 (Lemma 7(b)); θ ∈ (α₀, α₀ + 1.02ε) is seen (if its label is in 𝒢, by the definition of 𝒢) or is the direction of a true label;
all other θ are directions of true labels.
**Pointwise bounds on x⁰.** Collecting Lemmas 8, 6(d), 7(c), 9(b), 11(c): with x := Θ − α₀ on the forward zone (0 ≤ x ≤ 0.1; x ≤ u ≤ 1.0151x)
and x := α₀ + 2π − Θ on the tail (x_e ≤ x ≤ 0.1; x ≤ x_e + u′ because w ≥ 1, and u′ ≤ 1.015(x − x_e)):
 (i) |T − û| ≤ |ψ| ≤ 1.69x^{1−μ} on the forward zone; (ii) −1.647x^{1−μ_T} ≤ ψ < 0 on the tail;
 (iii) on {u ≥ 1.04ε} the tangent angle of x⁰ is locally Lipschitz in u, with a.e. derivative k, |k| ≤ 1.0002u^{−μ} on the forward zone,
 |k| ≤ 1.0001x^{−μ_T} ≤ 1.0001ε^{−μ_T} on the tail (x ≥ x_e ≥ ε), |k| ≤ 1.22 elsewhere (across the label 2π: Lemma 11(c));
 (iv) |x⁰(u) − e^{iΘ(u)}| ≤ 3.74·10⁻⁶ for all u.
**(T1).** Let ε/2 ≤ λ ≤ 1/40. *Far case u_a ≥ max(λ, 1.04ε):* by (iii) the tangent angle is K-Lipschitz on [u_a,u_b] with
K := 1.22λ^{−3v} (u^{−μ} ≤ λ^{−μ} for u ≥ u_a ≥ λ, u ≤ 1; ε^{−μ_T} ≤ (2λ)^{−μ_T} ≤ λ^{−μ_T}; μ, μ_T ≤ 3v), and Kλ ≤ π; by [D, Lemma D0(c)] (a statement
about any C¹ curve with K-Lipschitz tangent angle), N ≤ (K/√12)λ^{3/2} ≤ 0.353λ^{3/2−3v}. *Near case u_a < max(λ, 1.04ε) ≤ 2.08λ:* u_b < 3.08λ ≤ 0.077,
the pair lies in the forward zone, and by (i) and [P7, Fact 0.2(i)], N² ≤ ∫_{u_a}^{u_b}(1.69u^{1−μ})²du, so N ≤ (1.69/1.732)(3.08λ)^{3/2−μ} ≤ 5.3λ^{3/2−μ}.
Hence N ≤ 5.4λ^{3/2−3v} = 5.4λ^{1−3v−a′}λ^{1/2+a′} ≤ 5.4λ₀^{1−3v−a′}λ^{1/2+a′}; for a′ = 1/2: 5.4·40^{−1/2+3v} ≤ 0.86, and C₀λ₀^{a′} ≤ 0.14.
**(T2).** Let λ > 1/40 and Δ := Θ_b − Θ_a ∈ (0, 2π − x_e]. From l ≤ 1.0152 max(Δ, 0.02): Δ ≥ 0.0246. By (iv), c ≥ 2 sin(Δ/2) − 7.5·10⁻⁶.
*If Δ ≤ 2π − 0.0246:* c ≥ 2 sin(0.0123) − 7.5·10⁻⁶ ≥ 0.0245 ≥ c_sep. *If Δ > 2π − 0.0246:* then x_a := Θ_a − α₀ ≥ 0 and x_b := α₀ + 2π − Θ_b ≥ x_e
satisfy x_a + x_b < 0.0246: a lies in the forward zone, b in the tail. In the frame (X₀; û, iû): z_a = ∫₀^{u_a}cos ψ du ≥ 0.999u_a (by (i), |ψ| ≤ 0.042),
z_b ≤ −0.9939x_b (Lemma 7(c)) and u′_b ≤ 1.015x_b. So **c ≥ z_a − z_b ≥ 0.999u_a + 0.979u′_b ≥ (u_a + u′_b)/2.**
**(T3).** For u ≤ 0.05: x ≤ u ≤ 0.1 and by (i) |T − û| ≤ 1.69u^{1−μ} ≤ 1.69u^{1/4} ≤ 1.69 max(u,ε/2)^{1/4}.
**(T4).** For u′ ≤ 0.05: x ≤ x_e + u′ ≤ 0.1 (x_e ≤ 0.05), so by (ii) |T − û| ≤ 1.647(x_e + u′)^{1−μ_T} ≤ 1.647(x_e^{1/2} + u′^{1/2}), and
x_e^{1/2} ≤ 1.2514ε^{1/4} ≤ 1.4882(ε/2)^{1/4}, u′^{1/2} ≤ 0.473u′^{1/4}: |T − û| ≤ 1.647·1.9612·max(u′, ε/2)^{1/4} ≤ 3.3 max(u′,ε/2)^{1/4}.
**(T5).** x⁰(U) = E_Y = X₀ + z_Eû + y_E·iû (Lemma 7(d)), so z₀ = −z_E ∈ [0.9939x_e, 1.00013x_e] ⊂ [1.269ε^{1/(2−2v)}, 1.567ε^{1/(2−2v)}] ⊂ (0, 1.57ε^{1/4}],
and y₀ = −y_E, |y₀| ≤ 1.000001ε(2.0023x_e/ε)^{v/(1+v)} ≤ 1.000001ε(3.14ε^{−1/2})^{v} ≤ 1.000003ε^{1−v/2}, while
ϑ_T(z₀+ε)(ε/2)^{1/4} ≥ 3.3·1.269·2^{−1/4}ε^{(1+μ)/2+1/4} ≥ 3.5ε^{3/4+μ/2}, and ε^{1/4−v/2−μ/2} ≤ 1. ∎

**Remarks for the assembly.** (1) *The axis label is singular* (caught at t₀, no trajectory afterwards); the true front is nevertheless a
C^{1,1} arc through the limit point Z_s, with the same curvature bound 1.22 on both sides (Lemma 11). P8b needs nothing else there: the
label is a ghost label. (2) The hole labels 0 < |α − 2π| < α_s are *true* labels in the sense of P8b §1 (their trajectories exist and
x⁰ = S_α(t_s)); they are also seen. (3) P8b's derived constants with the values above and a′ = 1/2: γ₁ = γ_* = 1/4, c_A = 0.024,
R_A = (1/(1600·0.86))² ≥ 5.2·10⁻⁷; with the sharper (T1) (a′ = 0.99, C₀ = 5.21): γ₁ = 1/4, R_A = (1/8336)^{1/0.99} ≥ 1.09·10⁻⁴.
(4) D₁: Lemmas 1–3, 4(a), 4(d), 5(a) and the curvature formula in the proof of 4(c) are exact for every D₁ > 0; the numerical constants of
Lemmas 5(c)–11 were derived for D₁ = 1 only (P8b's numerics used D₁ = 0.1; the proof here does not cover that value).

---------------------------------------------------------------------------------------------------------------------

## §10. What is NOT proved here (precise list)

1. Nothing after t_s (departure from E_Y, hole crossing, final approach: P8b).
2. The VIRTUAL front of [B] on the seen stretch (b_e, α₀) and inside the hole is not analysed; (H_T) does not need it (x⁰ ends at b_e and
 uses the true front through the hole). N8 (numerical): the virtual front in the hole carries a dent of depth ≈ 1.2v²ε.
3. a′ = 1 is false at X₀ and at E_Y (true curvature ≈ x^{−μ}, x^{−μ_T}); every a′ ≤ 1 − 3v is proved.
4. Range: all inequalities with numerical constants are proved for v ≤ 10⁻⁶, D₁ = 1, ε ≤ 10⁻³ only (they use that the front is a
 10⁻⁵-perturbation of the unit circle away from the three singular places X₀, E_Y, the axis). Numerically (H_T) holds with similar
 constants up to v = 0.1 (`reports/P8a-1.md` §3), with a′ ≤ 1 − 3v/(1+v).
5. Proposition P8a.1 (§8) is the arc-wise form (P7 (ST_end) on A₁ alone); it is implied by, and superseded for the assembly by, Theorem P8a.H.
