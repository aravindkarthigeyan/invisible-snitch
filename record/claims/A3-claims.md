## 4. Proved results

### Lemma A3.1 (Abel–Fáry bound, sharp form). PROVED
During leg j, at a time when no remaining candidate is at H, let e_i = (S_{i+1} − S_i)/|S_{i+1} − S_i| (j ≤ i ≤ N − 1),
κ_i ∈ [0, π] the turning angle of the polyline at S_i (j < i < N), and when κ_i < π let ψ_i be the angle between r̂_i and
the bisector e_{i−1} + e_i. Then
  W = r̂_N·e_{N−1} − r̂_j·e_j + Σ_{i=j+1}^{N−1} r̂_i·(e_{i−1} − e_i),  |r̂_i·(e_{i−1} − e_i)| = 2 sin(κ_i/2)|sin ψ_i|,
hence W ≤ r̂_N·e_{N−1} − u·e_j + Σ 2 sin(κ_i/2)|sin ψ_i| ≤ 2 + Σ κ_i. If moreover no direction in [α_j, α_N] has been caught
by time t (so γ_t is a continuous injective arc), then Σ κ_i ≤ TC(γ_t), where TC is the total curvature in the sense of
Milnor/Sullivan (sup of the turning of inscribed polygons; = ∫|κ| ds + Σ corner angles for piecewise C² arcs).
So **W ≤ 2 + TC(γ_t)**.
*Proof.* Summation by parts of W = Σ_{i=j}^{N−1}(r̂_{i+1} − r̂_i)·e_i. Since |e_{i−1}| = |e_i| = 1, e_{i−1} − e_i is orthogonal
to e_{i−1} + e_i and has length 2 sin(κ_i/2); so its scalar product with r̂_i is 2 sin(κ_i/2) times the component of r̂_i
orthogonal to the bisector (if κ_i = π the bound 2 sin(κ_i/2) = 2 still holds). 2 sin(x/2) ≤ x. The candidate polyline is
inscribed in γ_t with vertices in curve order (the chain order is the α order). Refinement never decreases turning:
inserting X between consecutive vertices A, B, the direction of AB is a positive combination of those of AX and XB, so it
lies on the shorter arc between them and ∠(AX, AB) + ∠(AB, XB) = ∠(AX, XB); two triangle inequalities on the circle of
directions give ∠(e_PA, e_AB) + ∠(e_AB, e_BQ) ≤ ∠(e_PA, e_AX) + ∠(e_AX, e_XB) + ∠(e_XB, e_BQ). Hence the turning of the
candidate polyline is ≤ the sup over inscribed polygons, which is TC (Milnor 1950; J. M. Sullivan, *Curves of finite
total curvature*, 2008, for the equality with ∫|κ|ds + corners). ∎
*Remark.* The sharp form shows that the turning only costs where the chain is non-radial (|sin ψ_i| large); in the
near-radial end phase the endpoint terms almost cancel (r̂_N·e_{N−1} ≈ 1 ≈ u·e_j). The continuum analogue is
W_c := ∫ sin²φ/ρ ds = [cos φ]_{ends} − ∫ κ (r̂·N) ds (φ = angle between tangent and r̂), and L_arc' = v W_c exactly.
Numerically max(W − 2 − TC) ≈ −2.0 in every run: the bound is very lossy.

### Lemma A3.2 (evolution of the wavefront's tangent angle and curvature). PROVED
Let H be any path with |H'| ≤ 1 and let I be an interval of directions none of which is caught on [t1, t2]. Write
T = ∂_αS, τ = its angle, θ = the polar angle of r = S − H, φ = τ − θ, κ = ∂_ατ/|T| (signed curvature), and
Ω := (v/2ρ) sin 2φ. Then T never vanishes, and on I × [t1, t2]
  ∂_t τ = Ω = (v/2ρ) sin 2φ,   ∂_t log|T| = (v/ρ) sin²φ,
  ∂_t κ = (v/ρ)(cos 2φ − sin²φ) κ − (v/ρ²) sin φ (3cos²φ − 1),
  ∂_t(∂_ατ) = (v/ρ) cos 2φ ∂_ατ − (v|T|/ρ²) sin φ (3cos²φ − 1).
None of these contains H'; each direction evolves by an ODE in t alone (no α-derivatives of τ on the right of the first law).
*Proof.* Differentiating (1) in α: ∂_tT = (v/ρ)(I − r̂r̂ᵀ)T (paper, Prop. 6). T(t) = M(t)T(t1) with M the fundamental matrix
of a linear ODE with continuous coefficients, so T ≠ 0. With r̂⊥ the rotation of r̂ by +90°, T = |T|(cos φ r̂ + sin φ r̂⊥) and
(I − r̂r̂ᵀ)T = |T| sin φ r̂⊥; projecting on T̂ and T̂⊥ (r̂⊥·T̂ = sin φ, r̂⊥·T̂⊥ = cos φ) gives ∂_t|T| = (v/ρ) sin²φ |T| and
|T|∂_tτ = (v/ρ)|T| sin φ cos φ. Differentiate ∂_tτ in α using ∂_αρ = |T| cos φ, ∂_αθ = |T| sin φ/ρ, ∂_αφ = ∂_ατ − ∂_αθ:
∂_α Ω = −(v/2ρ²)|T| cos φ sin 2φ + (v/ρ) cos 2φ (∂_ατ − |T| sin φ/ρ) = (v/ρ) cos 2φ ∂_ατ − (v|T|/ρ²) sin φ (cos²φ + cos 2φ),
and cos²φ + cos 2φ = 3cos²φ − 1. Finally ∂_tκ = ∂_t(∂_ατ)/|T| − κ ∂_t log|T|. ∎
Checks: circle about a fixed Harry (φ = π/2, κ = 1/R): κ_t = −v/R² = d(1/R)/dt with R' = v. Radial line: κ_t = 0.
Finite-difference test on random arcs (`test_laws.py`): relative errors 4.6·10⁻⁷ (τ_t), 1.1·10⁻⁴ (κ_t, O(h²) differencing).

### Proposition A3.3 (rate of the total curvature). PROVED
On a time interval inside one leg, suppose τ(·, t) is C² on [α_j, α_N] with finitely many interior critical points
c_1(t) < … < c_m(t), each a simple zero of ∂_ατ depending C¹ on t (c_0 = α_j, c_{m+1} = α_N). Then
TC(t) = Σ_{k=0}^{m} |τ(c_{k+1}) − τ(c_k)| and
  TC'(t) = Σ_{k=0}^{m} σ_k [Ω(c_{k+1}) − Ω(c_k)],  σ_k = sign of ∂_ατ on (c_k, c_{k+1}),
i.e. +2Ω at every local maximum of τ, −2Ω at every local minimum, ±Ω at the two ends. In particular
|TC'| ≤ (v/2)[1/ρ(α_j) + 1/ρ(α_N) + 2 Σ_k 1/ρ(c_k)].
*Proof.* On each (c_k, c_{k+1}) τ is strictly monotone, so the variation there is |τ(c_{k+1}) − τ(c_k)|. Differentiate:
d/dt τ(c_k(t), t) = ∂_ατ·c_k' + ∂_tτ = Ω(c_k) because ∂_ατ(c_k) = 0; the ends are fixed within a leg. ∎
*Remark (no comparison principle).* By Lemma A3.2, ∂_ατ at a fixed α obeys a linear ODE in t with source
F = −(v|T|/ρ²) sin φ(3cos²φ − 1). At a point where ∂_ατ and ∂²_ατ vanish (and ∂³_ατ = c ≠ 0), ∂_ατ ≈ c(α − a)²/2 + F(t − t*),
so a pair of inflections is created on the side of t* where F(t − t*)/c < 0. F vanishes only where the tangent is radial
(sin φ = 0) or at |cos φ| = 1/√3, so nothing local forbids creation: there is no Sturm/maximum principle for the inflection
count (unlike curve-shortening flows, there is no diffusion in α). That the count stayed ≤ 2 numerically is a global fact.

### Lemma A3.4 (hull perimeter). PROVED
Let R(t) be the set of remaining candidates of any chase in which, on each leg, Harry moves with constant velocity u,
|u| = 1, pointing at a remaining candidate (chain chase, bearing-sorted chase, …), and let
P(t) = perimeter of K(t) = conv({H(t)} ∪ R(t)) (P = 2·length for a segment). Let B_H(t) ∈ [0, π] be the opening of the
smallest closed sector with apex H containing R(t), B_H := π if no sector of opening < π contains it. Then:
(a) P is continuous on [t0, T_end] (in particular it does not jump at planned or accidental catches) and Lipschitz;
(b) for a.e. t, P'(t) ≤ −(1 + cos B_H) + v(π + B_H) (≤ 2πv always);
(c) P ≤ 2Φ, and P ≥ 2 max_i ρ_i, so P = 0 iff the chase is over.
*Proof.* (a) A candidate is removed only at the instant it coincides with H, which leaves K unchanged; between removals
every point of {H} ∪ R moves with speed ≤ 1, and the perimeter of the hull of finitely many points is Lipschitz in them
(Cauchy's formula below). (b) Cauchy: P = ∫_0^{2π} h(θ, t) dθ with support function h = max over p ∈ {H} ∪ R of ⟨p, e_θ⟩.
For each θ, h(θ, ·) is a max of finitely many C¹ functions (candidates are C¹ while ρ > 0; H is affine on a leg), so it has
a right derivative D⁺h(θ, t) = max over active p of ⟨p', e_θ⟩ (Danskin), and the difference quotients are bounded by 1;
by dominated convergence P'⁺(t) = ∫ D⁺h(θ, t) dθ. Except for finitely many θ (normals of hull edges) the active point is
unique and is the vertex V whose normal arc N_V contains θ. Hence P'⁺ = Σ_V ⟨V', ∫_{N_V} e_θ dθ⟩ = Σ_V 2 sin(ε_V/2)⟨V', n_V⟩,
where ε_V = |N_V| is the exterior angle and n_V the outer bisector; Σ_V ε_V = 2π. A candidate vertex has V' = v r̂_V, so it
contributes ≤ 2v sin(ε_V/2) ≤ vε_V. If H is a vertex, its interior angle is B_H < π, ε_H = π − B_H, and u (pointing at a
point of R) lies in the interior sector, at angle x ≤ B_H/2 from −n_H; so H contributes
2 sin((π − B_H)/2)(−cos x) ≤ −2cos²(B_H/2) = −(1 + cos B_H). If H is not a vertex it contributes 0 = −(1 + cos π) and
ε_H := 0 ≤ π − B_H. Summing: P'⁺ ≤ −(1 + cos B_H) + v(2π − ε_H) ≤ −(1 + cos B_H) + v(π + B_H). Where P is differentiable
(a.e.) P' = P'⁺. (c) K = conv of the polyline H S_j … S_N of length Φ; by Cauchy, P = ∫_0^π w(θ)dθ with w the width, and
w(θ) ≤ Σ_edges |⟨edge, e_θ⟩|, ∫_0^π |⟨e, e_θ⟩| dθ = 2|e|. P ≥ 2 diam K ≥ 2 max ρ_i. ∎
Numerical test (`hull_check.py`): 150 random sets (v ∈ [0.02, 0.7], 2–30 directions, 30 % with a near-twin pair at gap
10⁻⁹…10⁻³), 100 860 configurations, exact map: max[ΔP − ∫bound]/Δt = −0.025 ≤ 0; max(P − 2Φ) = 2·10⁻¹³; P continuous at
catches to O(10⁻⁷τ) (the residual of stopping 10⁻⁷τ before the catch). (A first version evaluated the bound at the catch
instant itself, where the target's direction is rounding noise, and reported a spurious 0.71; `hull_debug.py`.)

### Theorem A3.5 (capture conditional on an end-phase sector condition). PROVED (conditional)
Let D_1 ⊂ D_2 ⊂ … be finite direction sets containing 0 with dense union (e.g. dyadic) and v < v1 = 0.4747526383.
Suppose there is γ ∈ [0, π] with c_H := 1 + cos γ − v(π + γ) > 0 such that
  **(E_H, γ)**: for the chain chase of every D_k, at every t ∈ [t_f, T_end), the remaining candidates lie in a closed
  sector with apex H(t) and opening ≤ γ (t_f = first loss of bearing order, A-1).
Then there is a path with |H'| ≤ 1 catching every direction exactly by
  T = d/(1−v) + 2πd/((1−v)μ),  μ = sup_{0≤λ<1} min{ m(v, λ), (1 − λ)c_H/2 } > 0,
m(v, λ) = min_{0≤x≤π}[(1−λ)(1−v) + λ(1−cos x) − vx] (stream B). For v < 1/(1+π), λ = 0 gives μ ≥ min{1 − v(1+π), c_H/2}.
*Proof.* Ordered phase [t0, t_f]: exactly as in A-2 Thm A2.3: Ψ = Φ − λρ_{N(t)} has Ψ' ≤ −m(v, λ) (A-1 Lemma A3(a): A = β_N,
W ≤ A; B-1 Lemma B1), only downward jumps, Ψ(t0) ≤ Φ(t0) ≤ 2πd/(1−v). End phase: by Lemma A3.4(b) and (E_H, γ),
P' ≤ −(1 + cos B_H) + v(π + B_H) ≤ −c_H (the right side is increasing in B on [0, π], its derivative being
sin B + v > 0, so under B_H ≤ γ it is at most its value at γ, which is −c_H). P is continuous and
P > 0 before T_end, so T_end − t_f ≤ P(t_f)/c_H ≤ 2Φ(t_f)/c_H ≤ 2Ψ(t_f)/((1 − λ)c_H). Adding,
T_end − t0 ≤ (Ψ(t0) − Ψ(t_f))/m + 2Ψ(t_f)/((1−λ)c_H) ≤ Ψ(t0)/min{m, (1−λ)c_H/2}. Every H_k is 1-Lipschitz on [0, T] (it
stays put after its last catch); apply Lemma 4 of the paper. ∎
*Comparison with A-2.* A-2's (E_γ) bounds the half-angle |β_i| ≤ γ about the heading and needs γ < arccos v → π/2 as v → 0.
(E_H) bounds the full opening of the remaining set and allows γ up to γ_H(v), the root of 1 + cos γ = v(π + γ):

| v | 0.01 | 0.02 | 0.05 | 0.1 | 0.2 | 0.24 | 0.3 | 0.35 | 0.4 | 0.45 | 0.47 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| γ_H(v) | 2.795 | 2.655 | 2.380 | 2.070 | 1.619 | 1.465 | 1.248 | 1.075 | 0.904 | 0.733 | 0.663 |
| arccos v | 1.561 | 1.551 | 1.521 | 1.471 | 1.369 | 1.328 | 1.266 | 1.213 | 1.159 | 1.104 | 1.082 |
| measured sup B_H after t_f (NUMERICAL) | | | | 0.915 | 1.018 | 0.952 | 0.840 | 0.750 | 0.651 | 0.564 | 0.518 |
| T via (E_H) with γ = B_H + 0.1 | | | | 13.7 | 30.5 | 41.6 | 70.3 | 122.5 | 242.6 | 775 | 1716 |

(π − γ_H ≈ 2√(πv) for small v; measured values: deep tail mt = 40, k = 8, sampled at 0, ¼, ½, ¾, 0.9, 0.99 of every leg,
`tc.py v 8 2 "0.25,0.5,0.75,0.9,0.99" 1 40`; bounds `hbound.py`.) For v ≳ 0.27 the cone condition (E_γ) is the weaker
requirement; for small v (E_H) is far more robust: if, as A-2 suggests, the measured cone tends to π/2 as v → 0, (E_γ)
becomes marginal while (E_H) keeps a margin ≈ π/2. The (E_H) time bounds are worse than A-2's (E_K) bounds (T = 10.8 at
v = 0.1) because P(t_f) is only bounded by 2Φ(t_f).

