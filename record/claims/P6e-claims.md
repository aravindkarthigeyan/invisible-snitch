# P6e-claims: a lossless bound for Q = r ∂ψ/∂r on the left-behind arm, up to the entry time

Stream P6e, round 6. Only PROVED statements, with proofs. Numerics and discussion: `reports/P6e-1.md`; code `code/P6e/`.

**Claimed PROVED:** Lemma E1 (arm at exact first contact), Lemma E2 (pointwise heading modulus of Harry's path from
Theorem B), Lemma E3 (scaling identities — the exact law for the *self-similarity defect*), Proposition E4 (window
estimate with a saturated propagator; general path hypotheses), Corollaries E5, E6, E7, **Theorem E (for the reference construction "start S +
C_cut": |Q(r, t)| ≤ 1.134 r + 0.57 v + 10⁻⁸ ≤ 0.12 for all arm points with t_0-radius r ≥ 16 ε and all times from t_0 to the
entry time, uniformly in ε)**, Corollary E5 (excess class).
**Not proved here:** anything after the entry time (the final stretch (FS)).

## 0. Setting, notation, inputs

Formulation as in `referee/P6a-claims.md`: plane = ℂ, a·b = Re(a b̄), a × b = Im(ā b); field F, virtual candidates x_θ,
Lemma V, Lemma VC, Lemma 1, Lemma C; μ = v/(1 − v).
**Reference construction (P6d, §0): start S + C_cut.** Phase 1: P(t) = t on [0, t_0], t_0 := 1/(1 − v) exactly; O := P(t_0).
Connector: P(t) = O + (t − t_0)u, u := (x_{α_s}(t_0) − O)/ρ_s, until P meets x_{α_s} at t_s (t_s − t_0 ≤ 1.402 ε, ρ_s ≤ 1.4 ε).
Then the legs of construction C (step ε, unit speed) from the base a_{j_s} = α_s, with end label b_e = 2π − α_s.
**Standing assumptions:** δ = θ_0 = 0.1, R := 10⁻³ (= min(1/792, δ/100)), M := R^{−1/4}/140 (0.0401 < M < 0.0402),
v ≤ 10⁻¹², ε ≤ ε_0 := δ²/6400. Label sets R := [α_s, 0.2], B := [0.2, 2π − 0.2], 𝒜 := [2π − 0.1, b_e] (the arm).
τ := t − t_0. θ* := arccos(−v), u_0 := e^{iθ*}, b_∞ := θ* − π (the direction −u_0).

**Arm coordinates.** For a label b = 2π − α ∈ 𝒜 let r := |x_b(t_0) − O| (strictly increasing in α, Lemma E1); r is used as
the label of 𝒜. x = x(r, τ), ρ := |x − P|, r̂ := (x − P)/ρ, β := arg r̂ (continuous lift), T = e^{iψ} := ∂_r x/|∂_r x|,
w := |∂_r x|, φ := β − ψ (so cos φ = T·r̂, sin φ = T × r̂, as in P6a), **Q := r ∂_rψ** (= r w κ).
Entry time t_e := the first leg start with base label ≥ 2π − 0.2 (so for t ≤ t_e the base label is in R ∪ B).

**Inputs (statements used).**
* P6c-claims §0, Claim 1(a),(b),(e),(f) (front at exact first contact; for α ∈ (0, π), polar coordinates (ρ, β) about O):
  ρ g(β) = g(α), ρ(cos β + v) = −(1 − cos α), β ∈ (θ*, π), g(β) ≤ g(θ*) ≤ 1; A := ρ_α > 0, B := ρβ_α > 0 for cos α > v;
  labels in [α_s, 2π − α_s] have ρ ≥ ε on [0, t_0] (virtual = true there); ρ_s ≤ 1.4 ε. Lemma G2's computation
  (r_a ≥ r_b + 0.067 for α_a ∈ [0.2, arccos v], α_b ≤ 0.1; r ≥ 1 for α ≥ arccos v), which for t_0 = 1/(1−v) is the case
  η = 0 of its proof. P6c2 Claim 14(a): Q_t = (v/ρ) cos 2φ · Q + (v r w/ρ²) sin φ (3cos²φ − 1) where ρ > ε, front C².
* P6d-claims: Claim D1 and its proof (formulas for A_α, B_α; m := B/A = tan(ψ − β) ≤ 0.63 ρ for α ≤ 1/2); Claim D3 with
  Step 2 of its proof (|arg u − ψ_{α_s}(t)| ≤ 0.9 ε on [t_0, t_s)); Theorem D (the start S satisfies (ST) at t_s on
  [α_s, 2π − δ/2] with κ = 1/2, R = 10⁻³; tangent angle 2.25-Lipschitz in arclength at t_s; U := l_{t_s}(α_s, 2π − δ/2) ≤ 6.85).
* P6a-claims: Theorem B (doubly refereed) for the legs after t_s: (I1), (I2), (CA) for the family; Step 1(a),(b) of its
  proof (label advance per leg ∈ [ε/2, ε]; elapsed time ≤ T_B = 4U + 2 ≤ 29.4; legs last ≤ 2ε); Step 2 (TL):
  |e_J − e_I| ≤ 91 M λ_I^{1/4} for family pairs J ⊂ I at any time (a consequence of (I1), (I2), (CA), Lemma 4(a)).
  Lemma C(2),(4): during leg j+1, x_{a_j}, P, x_{a_{j+1}} are collinear in this order, P' = the unit vector from x_{a_j} to
  x_{a_{j+1}}, |P − x_{a_j}| ≤ ε₁ ≤ 2ε.
* P6a2-claims: Corollary N (no dawdling). Its proof uses t_0 and O only through "t_s − t_0 ≤ mε, r_{a_{j_s}} ≤ mε,
  r_a := |x_a(t_0) − O|" and the triangle inequality; for the start S these hold with m = 2 (P6d, Remark (1)). With
  K = max(2, U/(16R)) ≤ 428.2 it gives, for every leg start t_j ≥ t_s with base in R ∪ B:
  **(A1) t_j − t_0 ≤ C_A (r_{a_j} + ε), C_A := 2584.** (Theorem B needs v(4U + 2) ≤ 10⁻⁶R: true for v ≤ 10⁻¹².)

---------------------------------------------------------------------------------------------------------------------

## Lemma E1 (the arm at t_0, start S). PROVED

Let v ≤ 10⁻², α ∈ (0, 0.1], and (ρ, β), A, B, m = B/A as above (right arm; the left arm is its mirror image in the real
axis). Then
(a) ρ is strictly increasing in α; ρ(0.1) ≤ 0.104; ρ(α_s) = ρ_s ≤ 1.4 ε.
(b) 0 < β − θ* ≤ 0.51 ρ.
(c) 0 < m = tan φ_0 ≤ 0.63 ρ, where φ_0 is the angle φ of the mirrored (left-arm) point at τ = 0.
(d) the curvature of the front satisfies |κ| ≤ 1.13, and |Q_0| ≤ 1.133 ρ, Q_0 := Q at τ = 0.
(e) For the left-arm point with radius r (position x_0 := x(r,0) − O = r e^{−iβ}): at τ = 0, β_arm = −β, ψ = −β − φ_0, and
    b_∞ − ψ(r, 0) = 2 arcsin v + (β − θ*) + φ_0.

*Proof.* (a) A > 0 (Claim 1(b)). ρ = g(α)/g(β); g(0.1) = sin 0.1/tan^v(0.05) ≤ 0.09984 · 20^{0.01} ≤ 0.1029. By (b) below,
cos β ∈ [−0.0602, 0), so g(β) = (1 − cos²β)^{1/2}((1 + cos β)/(1 − cos β))^{v/2} ≥ 0.9981 · 0.9993 ≥ 0.997; ρ ≤ 0.1033.
(b) −(cos β + v) = (1 − cos α)/ρ = g(β)(1 − cos α)/g(α) = g(β) tan^{1+v}(α/2) > 0. Further
tan^{1−v}(α/2) = g(α)/(1 + cos α) = ρ g(β)/(1 + cos α) ≤ ρ/1.995, so tan(α/2) ≤ (0.5013ρ)^{1/(1−v)} ≤ 0.5013 ρ (base < 1), and
tan^{1+v}(α/2) ≤ tan(α/2). Hence 0 < cos θ* − cos β ≤ 0.5013 ρ ≤ 0.0502 (α ≤ 0.1 gives tan(α/2) ≤ 0.05005 directly), so
cos β ≥ −0.0602, β ≤ 1.6311, and cos θ* − cos β = 2 sin((β+θ*)/2) sin((β−θ*)/2) with (β+θ*)/2 ∈ [π/2, 1.6311], where
sin ≥ 0.998. So sin((β − θ*)/2) ≤ 0.2512 ρ ≤ 0.0262 and β − θ* ≤ 2 arcsin(0.2512ρ) ≤ 0.503 ρ.
(c) Claim D1 of P6d (m ∈ (0, 0.63ρ]). The right arm has tangent angle β + arctan m (z_α = (A + iB)e^{iβ}); mirroring,
the left arm has bearing −β from O and tangent angle ψ = −β − arctan m, so φ(0) = β_arm − ψ = arctan m =: φ_0. This is (e)
too: b_∞ − ψ = θ* − π + β + φ_0 = (2θ* − π) + (β − θ*) + φ_0 and 2θ* − π = 2 arcsin v.
(d) We repeat the arm part of the proof of Claim D1 with the numbers for α ≤ 0.1: τ̃ := tan(α/2) ≤ 0.0500417,
cos α ≥ 0.9950042, c' := cos α − v ≥ 0.985, 1 − v ≥ 0.99, 1 + cos α ≥ 1.995, sin α ≤ 0.0998334,
τ̃/sin α = 1/(1 + cos α) ≤ 0.501253, 1 + τ̃² ≤ 1.0025042. As there: ρ ≥ g(α) = (1 + cos α)τ̃^{1−v}, 0 < B ≤ τ̃/(1 − v),
0 < v − cos β < 1 + v, (L1) A ≥ ρc'/sin α, (L2) A ≥ c'τ̃^{−v} ≥ c', and
|κ| ≤ m/ρ + |B_α|/A² + B|A_α|/A³, with the formulas for B_α, A_α of Claim D1. The eight terms are bounded exactly as in
that proof:
 m/ρ ≤ τ̃^{2v}/((1−v)c'(1+cos α)) ≤ 1/(0.99·0.985·1.995) < 0.51404;
 first part of |B_α|/A² ≤ τ̃^{1+3v}/((1−v)²c'²(1+cos α)) ≤ 0.0500417/(0.9801·0.970225·1.995) < 0.02638;
 second part ≤ (1+τ̃²)/(2(1−v)c'²) ≤ 1.0025042/(2·0.99·0.970225) < 0.52186;
 T1 ≤ sin α·τ̃/((1−v)c'³) < 0.00529;  T2 ≤ v(τ̃/sin α)/((1−v)c'²) < 0.00522;
 T3 ≤ (1+v)(τ̃/sin α)τ̃/((1−v)²c'²) < 0.02665;  T4 ≤ τ̃^{2+4v}/((1−v)³c'³(1+cos α)) < 0.00136;
 T5 ≤ (1+v)(1+τ̃²)τ̃/(2(1−v)²c'³) < 0.02705.
Sum < 1.1279. Finally Q_0 = r ∂_rψ = ρ (ds/dρ) ∂_sψ with ds/dρ = (A² + B²)^{1/2}/A = (1 + m²)^{1/2} ≤ (1 + 0.0656²)^{1/2}
≤ 1.0022 (by (c), (a)); |Q_0| ≤ 1.0022 · 1.1279 ρ. ∎

## Lemma E2 (heading modulus of Harry's path). PROVED (given Theorem B for start S)

(a) Let j_s ≤ i ≤ j be leg indices with u_{a_{j+1}} + R ≤ U, h_k := the heading (unit velocity) of leg k+1, and
λ := u_{a_{j+1}} − u_{a_i} ≤ R/100. Then |h_j − h_i| ≤ 365 M λ^{1/4}.
(b) |h_{j_s} − u| ≤ 3.15 ε and |u − u_0| ≤ 0.72 ε.
(c) Consequently, for a.e. τ ≥ 0 with 4τ + ε ≤ R/100:
   **|P'(t_0 + τ) − u_0| ≤ ϑ̄(τ) := 520 M (τ + 2ε)^{1/4}.**

*Proof.* (a) h_k = e_{J_k}(t) for all t in leg k+1, J_k := (a_k, a_{k+1}) (Lemma C(2)); the label length of J_k is in
[ε/2, ε] (Step 1(a)). If i = j there is nothing to prove. Let i < j, and b' the label with u_{b'} = u_{a_j} + λ (≤ U),
I := (a_i, a_{j+1}), I' := (a_j, b'). All pairs below have label lengths in [ε/2, 2λ] ⊂ [ε/2, R].
(1) At t_i: I is a family pair (first label = base a_i), J_i ⊂ I, J_j ⊂ I (a_j ≥ a_{i+1}); by (TL) twice,
|h_i − e_{J_j}(t_i)| ≤ 182 M λ^{1/4}.
(2) At t_i: J_j ⊂ I' (as u_{a_{j+1}} ≤ u_{a_j} + λ), both family pairs: |e_{J_j}(t_i) − e_{I'}(t_i)| ≤ 91 M λ^{1/4}.
(4) At t_j: I' is a family pair (first label = base a_j) and J_j ⊂ I': |h_j − e_{I'}(t_j)| ≤ 91 M λ^{1/4}.
(3) Rotation of I' on [t_i, t_j]. With e := e_{I'}(t), c := c(I'; t) ≥ λ/2 (CA): e' = Π_e(x_{b'}' − x_{a_j}')/c, Π_e := I − eeᵀ,
and x_a' = vF(r_a) with |Π_eF(r_a)| ≤ |Π_e r̂_a| (|F| = f ≤ 1; F = 0 if r_a = 0). Fix t in leg k+1, i ≤ k < j, and
a ∈ {a_j, b'}. Put I'' := (a_k, b'), a family pair of label length ≤ 2λ; θ := 182 M (2λ)^{1/4} ≤ 182·0.0402·(2·10⁻⁵)^{1/4}
< 0.49. By Lemma C(2), x_a − P = (x_a − x_{a_{k+1}}) + ρ̃ h_k with ρ̃ ≥ 0. Here h_k = e_{J_k}, J_k ⊂ I''; and if a ≠ a_{k+1},
x_a − x_{a_{k+1}} is a positive multiple of e_{(a_{k+1}, a)}, where (a_{k+1}, a) ⊂ I'' is a family pair (label length ≥ ε/2:
for a = a_j it contains J_{k+1}; for a = b' it is ≥ λ). Also I' ⊂ I''. By (TL), h_k, e_{(a_{k+1},a)} and e are within
91M(2λ)^{1/4} of e_{I''}, hence the first two are within θ of e. So x_a − P = α₁e₁ + ρ̃h_k with α₁, ρ̃ ≥ 0, unit vectors
e₁, h_k with |e₁ − e|, |h_k − e| ≤ θ: |Π_e(x_a − P)| ≤ (α₁ + ρ̃)θ, (x_a − P)·e ≥ (α₁ + ρ̃)(1 − θ²/2), and
|Π_e r̂_a| ≤ θ/(1 − θ²/2) ≤ 1.15 θ (if α₁ + ρ̃ = 0 then F(r_a) = 0). Therefore |e'| ≤ (2v/λ)·2·1.15θ. The legs i+1, …, j
advance the label by ≥ ε/2 each and last ≤ 2ε each, so t_j − t_i ≤ 4(u_{a_j} − u_{a_i}) ≤ 4λ, and
|e_{I'}(t_j) − e_{I'}(t_i)| ≤ 18.4 vθ ≤ M λ^{1/4} (v ≤ 10⁻¹²).
Sum: (182 + 91 + 1 + 91) M λ^{1/4}.
(b) By Step 2 of the proof of Claim D3, |arg u − ψ_{α_s}(t)| ≤ 0.9 ε for t < t_s, hence at t_s (ψ is continuous in t). By
Theorem D.3 the tangent angles on the arc [α_s, a_{j_s+1}] (length ε at t_s) are within 2.25 ε of ψ_{α_s}(t_s), so the chord
direction h_{j_s} (a positive combination of these tangents) is within angle 2.25 ε of T_{α_s}. Total ≤ 3.15 ε.
u = e^{iβ(α_s)} and 0 < β(α_s) − θ* ≤ 0.51 ρ_s ≤ 0.72 ε (Lemma E1(b)).
(c) On the connector P' = u. Let t_0 + τ lie in leg i+1. Each earlier leg k+1 ≥ j_s+1 lasts at least c(J_k; t_k) ≥ ε/4
(the distance to the target decreases at rate 1 − vf ≤ 1, and (CA) with label length ≥ ε/2), so i − j_s ≤ 4τ/ε and
λ := u_{a_{i+1}} − u_{α_s} ≤ (i − j_s + 1)ε ≤ 4τ + ε ≤ R/100; u_{a_{i+1}} + R ≤ U since U ≥ 2π − 0.05 − α_s ≥ 6
(|∂_θx| ≥ 1). By (a), (b): |P' − u_0| ≤ 365M(4τ + ε)^{1/4} + 3.87ε ≤ 516.2 M (τ + ε/4)^{1/4} + 3.87 ε ≤ 520 M (τ + 2ε)^{1/4},
because 3.87 ε ≤ 3.8 M (2ε)^{1/4} for ε ≤ 0.004 (M ≥ 0.0401). ∎

## Lemma E3 (scaling identities: the law of the self-similarity defect). PROVED

Let P be any path that is piecewise C¹ with |P'| ≤ 1 on [t_0, t_1], O := P(t_0), and r ↦ x(r, τ) a C² family of *true*
candidates (ρ > 0 on the time interval; x' = v r̂), C² in r with T, ψ, φ, Q as in §0 (r any C¹ label). Define

  p(τ) := τ P'(t_0 + τ) − (P(t_0 + τ) − O),
  η(r, τ) := r ∂_r x − (x − O) + vτ r̂,
  ζ(r, τ) := r ∂_rψ + τ ∂_τψ = Q − (vτ/2ρ) sin 2φ.

Then η, ζ are continuous and piecewise C¹ in τ, and wherever P' exists

  ∂_τ η = (v/ρ) Π (η − p),   Π := I − r̂ r̂ᵀ,
  ∂_τ ζ = (v/ρ) cos 2φ · ζ + G,   G := (v/(2ρ²)) sin 2φ · r̂·(η − p) − (v/ρ²) cos 2φ · n·(η − p),  n := i r̂,

so |∂_τ|η|| ≤ (v/ρ)(|η| + |p|) and |G| ≤ (v/ρ²)(|η| + |p|). At τ = 0: ζ = Q_0, and if r is the radius about O,
|η(r, 0)| = r tan φ_0. (If P' is constant and the initial curve is a ray from O, then p ≡ 0, η ≡ 0, ζ ≡ 0:
this is the self-similar model of Claim 13.)

*Proof.* Put 𝔇 := r∂_r + τ∂_τ; then ∂_τ𝔇f = 𝔇∂_τf + ∂_τf. With y := x − P(t_0 + τ): ∂_τx = v y/|y| =: vF₁(y), DF₁ = Π/ρ,
Π y = 0. ξ := 𝔇x satisfies ∂_τξ = 𝔇(vF₁(y)) + vr̂ = (v/ρ)Π(𝔇x − τP') + v r̂. Since x' = v r̂, ξ = r∂_rx + vτr̂ and
η = ξ − (x − O); 𝔇x − τP' = η + (x − O) − τP' = η + y − p, and Πy = 0, so ∂_τη = (v/ρ)Π(η − p) + v r̂ − v r̂.
For ψ: ∂_τψ = Ψ(y, ψ) := −(v/(2|y|)) sin 2(arg y − ψ) (Lemma 1(ii) of P6a). ζ = 𝔇ψ, so
∂_τζ = 𝔇Ψ + Ψ = ∂_ψΨ · ζ + ∇_yΨ·(𝔇x − τP') + Ψ = (v/ρ) cos 2φ · ζ + ∇_yΨ·(η − p) + ∇_yΨ·y + Ψ. Ψ is homogeneous of degree −1 in
y, so ∇_yΨ·y = −Ψ; and ∇_yΨ = (v/(2ρ²)) sin 2φ r̂ − (v/ρ²) cos 2φ n (∂_ρΨ = −Ψ/ρ, ρ^{-1}∂_βΨ = −(v/ρ²) cos 2φ), of norm
≤ v/ρ². Regularity: within each C¹ piece of P the field is C^∞ in x off P and C¹ in τ, so x is C² in r with ∂_r∂_τ,
∂_τ∂_r continuous, and ∂_τψ = Ψ is C¹ in τ; η and ζ do not involve P', so they are continuous across the break points.
Initial values: τ∂_τψ = 0 at τ = 0. If r = |x − O| at τ = 0 then ∂_rρ = 1 = w cos φ_0, so r∂_rx = (r/cos φ_0)T and
|r∂_rx − (x − O)|² = r²(1/cos²φ_0 − 2 + 1) = r² tan²φ_0. ∎

## Proposition E4 (the window: saturated propagator). PROVED

*Hypotheses.* v ≤ 10⁻³; 0 < τ_3 ≤ v/1000; ε > 0; P is piecewise C¹ with unit speed on [t_0, t_0 + τ_3], O = P(t_0), and
 (H1) |P'(t_0 + s) − u_0| ≤ ϑ̄(s) for a.e. s ∈ [0, τ_3], ϑ̄ non-decreasing, ϑ̄(τ_3) ≤ v/40.
A true candidate family r ↦ x(r, τ) as in Lemma E3, r ∈ [r_a, r_b] ⊂ [16ε, vτ_3], with initial data at τ = 0 satisfying
(with θ* = arg u_0, b_∞ = θ* − π):
 (H2) x(r, 0) − O = r e^{−iβ}, 0 < β − θ* ≤ 0.51 r; φ(r, 0) = φ_0 ∈ (0, arctan(0.63 r)]; |Q_0| ≤ 1.133 r;
      b_∞ − ψ(r, 0) = 2 arcsin v + (β − θ*) + φ_0;
 (H3) ∫_0^{τ_3} ϑ̄(s) ds/(r + s) ≤ v/10.
*Conclusions,* for every such r and all τ ∈ [0, τ_3]:
 (i) 0.998 (r + τ) ≤ ρ ≤ r + (1 + v)τ; in particular ρ > ε.
 (ii) the bearing error e := β − b_∞ (the angle from −u_0 to r̂; continuous, e(0) = −(2 arcsin v + (β − θ*)) in the notation
      of (H2)) satisfies |e| ≤ 2.04 v, and |e| ≤ e_0 := 0.09 v for τ ≥ τ_1 := 31 r.
 (iii) (one-sidedness) for τ ∈ [τ_1, τ_3]: φ̄ := b_∞ − ψ ∈ [1.98 v, π/2 + e_0], φ = φ̄ + e ∈ [1.89 v, π/2 + 2e_0]; φ̄ is
      non-decreasing as long as it is ≤ π/2 − e_0.
 (iv) (saturation) for 0 ≤ s ≤ τ ≤ τ_3: exp(∫_s^τ (v/ρ) cos 2φ) ≤ 1/(3.7 v).
 (v) |ζ| ≤ 0.307 r/v + 0.055 v ≤ 0.056 v and **|Q| ≤ 0.56 v**.
 (vi) w(τ) ≤ w(0) ((r + τ)/r)^ν, ν := 1.0021 v.

*Proof.* Write P(t_0 + τ) − O = τu_0 + q(τ); by (H1) |q(τ)| ≤ ∫_0^τϑ̄ ≤ τϑ̄(τ) ≤ vτ/40, and
p(τ) = ∫_0^τ (P'(τ) − P'(s)) ds gives |p(τ)| ≤ 2τϑ̄(τ) (a.e. τ). Let x_0 := x(r,0) − O and d := x(r,τ) − x(r,0), |d| ≤ vτ.
*(i)* x − P = x_0 − τu_0 + d − q. (x_0 − τu_0)·(−u_0) = τ − r cos(β + θ*), and β + θ* = π + 2 arcsin v + (β − θ*), so
−cos(β + θ*) = cos(2 arcsin v + β − θ*) ≥ 1 − (2.001v)²/2 ≥ 0.99999 (note r ≤ vτ_3 ≤ 10⁻⁶ v, so 0.51 r ≤ 10⁻⁶ v). Hence
(x − P)·(−u_0) ≥ τ + 0.99999 r − vτ − vτ/40 ≥ 0.998 (r + τ) > 0, which gives the lower bound; the upper bound holds since the
relative speed is ≤ 1 + v. Consequently, for s ≤ τ: N(s, τ) := ∫_s^τ v/ρ ≤ ν log((r + τ)/(r + s)).
*(ii)* Let ℓ(z) := Im((z − O) ū_0) (the coordinate transversal to u_0), ℓ_x := ℓ(x), ℓ_P := ℓ(P) = Im(q ū_0), |ℓ_P(τ)| ≤ vτ/40.
Define e ∈ (−π/2, π/2) by (x − P)/(−u_0) = ρ e^{ie} (possible by (i): the real part is positive); e is continuous and
β = b_∞ + e. Then ρ sin e = −(ℓ_x − ℓ_P), and ℓ_x' = v Im(r̂ ū_0) = (v/ρ)(ℓ_x − ℓ_P). At τ = 0:
ℓ_x = −r sin(β + θ*) = r sin(2 arcsin v + β − θ*) ∈ (0, 2.0006 v r]. By Gronwall and (i),
 |ℓ_x(τ)| ≤ ((r+τ)/r)^ν 2.0006 v r + ∫_0^τ ((r+τ)/(r+s))^ν (v/(0.998(r+s))) (vs/40) ds
       ≤ 2.0006 v r^{1−ν}(r+τ)^ν + (v²/39.8)(r + τ)
(∫_0^τ(r+s)^{−ν}ds ≤ (r+τ)^{1−ν}/(1−ν)). So
 |sin e| ≤ (|ℓ_x| + |ℓ_P|)/ρ ≤ 2.0047 v (r/(r+τ))^{1−ν} + 0.0252 v² + 0.02506 v.
This is ≤ 2.031 v always, and for τ ≥ 31 r: (1/32)^{1−ν} ≤ 0.03136, so |sin e| ≤ 0.0880 v + 0.0252 v²; arcsin x ≤ 1.001x here.
*(iii)* φ = β − ψ = φ̄ + e. By (H2), φ̄(0) ∈ [2v, 2.0000004 v + 1.14 r] ⊂ [2v, 2.0012 v]. φ̄' = −ψ' = (v/2ρ) sin 2φ =
(v/2ρ) sin(2φ̄ + 2e).
Phase A, τ ≤ τ_1: Δ(τ) := |φ̄(τ) − φ̄(0)| has Δ' ≤ (v/ρ)|φ| ≤ (v/ρ)(2.0012v + 2.04v + Δ), so
Δ(τ) ≤ 4.05 v (e^{N(0,τ)} − 1) ≤ 4.05v·(32^ν − 1) ≤ 14.1 v². Hence φ̄(τ_1) ∈ [1.985 v, 2.02 v].
Phase B, τ ∈ [τ_1, τ_3], where |e| ≤ e_0 = 0.09v: the right side f(τ, y) := (v/2ρ) sin(2y + 2e(τ)) is Lipschitz in y,
f(τ, c) > 0 for every c ∈ [1.98v, π/2 − e_0) (then 2c + 2e ∈ (0, π)), and f(τ, π/2 + e_0) ≤ 0. By comparison with the
constant sub-/super-solutions: if φ̄(τ_a) ≥ c with c ∈ [1.98v, π/2 − e_0) then φ̄ ≥ c on [τ_a, τ_3]; and φ̄ ≤ π/2 + e_0. This
gives (iii) (φ̄ ≥ 1.98 v, monotonicity below π/2 − e_0).
*(iv)* Let a(τ) := (v/ρ) cos 2φ. On [0, τ_1]: ∫a ≤ N(0, τ_1) ≤ 3.48 v. On [τ_1, τ_3] split by the value of φ̄; by the
monotonicity in (iii), S_1 := {φ̄ < π/4}, S_2 := {π/4 ≤ φ̄ < π/4 + e_0}, S_3 := {φ̄ ≥ π/4 + e_0} are consecutive intervals.
On S_1: 2φ ∈ [2φ̄ − 2e_0, 2φ̄ + 2e_0] ⊂ (0, π) and 2φ̄ − 2e_0 ∈ [3.78 v, π/2). Since cos is decreasing on [0, π],
cos 2φ ≤ cos(2φ̄ − 2e_0); since sin is concave on [0, π] and 2φ̄ + 2e_0 ≤ π − (2φ̄ − 2e_0) (i.e. φ̄ ≤ π/4),
sin 2φ ≥ sin(2φ̄ − 2e_0) > 0, i.e. v/ρ ≤ 2φ̄'/sin(2φ̄ − 2e_0). Therefore a ≤ 2φ̄' cot(2φ̄ − 2e_0) = (d/dτ) log sin(2φ̄ − 2e_0), and
for s < τ in S_1: ∫_s^τ a ≤ log(1/sin(2φ̄(s) − 2e_0)) ≤ log(1/sin 3.78v).
On S_2: 2φ ∈ [π/2 − 2e_0, π/2 + 4e_0], so sin 2φ ≥ 0.99, φ̄' ≥ 0.495 v/ρ, cos 2φ ≤ sin 2e_0 ≤ 0.18 v; hence
∫_{S_2} a ≤ 0.18 v ∫_{S_2} (v/ρ) ≤ 0.18 v · e_0/0.495 ≤ 0.04 v².
On S_3: φ ∈ [π/4, π/2 + 2e_0], cos 2φ ≤ 0, a ≤ 0.
So for τ_1 ≤ s ≤ τ: ∫_s^τ a ≤ log(1/sin 3.78 v) + 0.04v², and for s < τ_1 add ≤ 3.48 v. As sin 3.78v ≥ 3.7799 v:
exp(∫_s^τ a) ≤ e^{3.48v + 0.04v²}/(3.7799 v) ≤ 1/(3.7 v) (and ≤ e^{3.48 v} ≤ 1/(3.7v) if τ ≤ τ_1).
*(v)* Lemma E3: |η|' ≤ (v/ρ)(|η| + |p|), |η(0)| = r tan φ_0 ≤ 0.63 r². With (i) and |p(s)| ≤ 2sϑ̄(s):
 |η(τ)| ≤ ((r+τ)/r)^ν 0.63 r² + ∫_0^τ ((r+τ)/(r+s))^ν (v/(0.998(r+s))) 2sϑ̄(s) ds ≤ 0.63 r^{2−ν}(r+τ)^ν + 2.01 vϑ̄(τ)(r + τ).
Then, with ρ² ≥ 0.996(r+s)²,
 I := ∫_0^{τ_3} (|η| + |p|)/ρ² ds ≤ 0.6326 r^{2−ν}∫_0^∞(r+s)^{ν−2}ds + 2.02 v∫_0^{τ_3}ϑ̄(s)ds/(r+s) + 2.01∫_0^{τ_3}ϑ̄(s)ds/(r+s)
   ≤ 0.633 r + 0.202 v² + 0.201 v   (by (H3)).
Duhamel for ζ (Lemma E3: ζ(τ) = e^{∫_0^τ a}Q_0 + ∫_0^τ e^{∫_s^τ a}G ds, |G| ≤ (v/ρ²)(|η| + |p|)) with (iv):
|ζ(τ)| ≤ (|Q_0| + v I)/(3.7v) ≤ (1.133 r + 0.633 vr + 0.202 v³ + 0.201 v²)/(3.7 v) ≤ 0.307 r/v + 0.055 v, and r/v ≤ τ_3 ≤ v/1000. Finally |Q − ζ| = (vτ/2ρ)|sin 2φ| ≤ v/(2·0.998) ≤ 0.5011 v.
*(vi)* w'/w = v sin²φ/ρ ≤ v/ρ (Lemma 1(i) of P6a) and (i). ∎

## Theorem E (lossless bound for Q up to the entry time; start S + C_cut). PROVED

Under the standing assumptions (v ≤ 10⁻¹², ε ≤ δ²/6400, δ = 0.1), for every arm label with t_0-radius r ≥ 16 ε and every
t ∈ [t_0, t_e]:

  **|Q(r, t)| ≤ 1.134 r + 0.57 v + 10⁻⁸ ≤ 0.12.**

More precisely, with τ_3 := ½ (v/(20800 M))⁴ and r_2 := vτ_3: |Q| ≤ 0.57 v if 16ε ≤ r ≤ r_2, and
|Q| ≤ 1.134 r + 10⁻⁸ if r ≥ max(r_2, 16ε). Moreover the arm points with r ≥ 16ε have ρ > ε on [t_0, t_e] and never were
in the ε-disc, so the front is C^∞ there.

*Proof.* **Distances.** Let b ∈ 𝒜, r = r_b ≥ 16ε, t ∈ [t_0, t_e]. If t is in leg j+1 put D(t) := r_{a_j}; on the connector
D := ρ_s (base α_s). By Lemma C(4) (on the connector: |P − x_{α_s}| ≤ ρ_s ≤ 1.4ε) and Lemma VC(b):
ρ_b(t) ≥ |x_b(t_0) − x_{a_j}(t_0)| − 2ε. If a_j ∈ R: by Lemma E1(b) for α ≤ 0.2 (same proof: 0 < −cos β − v ≤ tan^{1+v}(α/2) ≤
0.1004) both x_{a_j}(t_0) − O and the mirror image of x_b(t_0) − O have bearings with sin ≥ 0.9949, so
|x_b(t_0) − x_{a_j}(t_0)| ≥ 0.9949 (D + r) and **ρ_b ≥ 0.99(D + r) − 2ε ≥ 0.865 (D + r)**. If a_j ∈ B: ρ_b ≥ 0.067 − 2ε ≥ 0.066
(Lemma G2's computation). In particular ρ_b > ε; with Claim 1(e) the points were never in the ε-disc, the front is C^∞
near them, and Claim 14(a) and Lemma 1 apply: |Q|' ≤ (v/ρ)|Q| + v r w/ρ² (|sin φ(3cos²φ − 1)| ≤ 1), w'/w ≤ v/ρ.
**Times.** D is non-decreasing in t while the base is in R (Lemma E1(a) for α ≤ 0.2: A > 0), and by (A1) and the leg
duration ≤ 2ε (connector: τ ≤ 1.402 ε): τ ≤ C_A(D(t) + 3ε). Hence m(y) := |{τ : base in R, D < y}| ≤ C_A(y + 3ε). The base
is in R ∪ B for a total time ≤ 1.402ε + T_B ≤ 29.5. With Y := sup D ≤ 0.21 and 3ε ≤ 3r/16 (layer cake, as in Claim 8 of P6c):
 ∫_{R} dτ/(r + D) = ∫_0^∞ m_t(y) dy/(r+y)² ≤ C_A[∫_0^Y (y + 3ε)dy/(r+y)² + (Y + 3ε)/(r + Y)] ≤ C_A[log(1 + Y/r) + 1.4],
 ∫_{R} dτ/(r + D)² ≤ C_A[∫_0^Y 2(y + 3ε)dy/(r+y)³ + (Y + 3ε)/(r + Y)²] ≤ 2.4 C_A/r.

**Case I: r ≥ r_2.** N_I := ∫_{t_0}^{t} v/ρ ≤ (v/0.865) C_A[log(1/r_2) + 1.4] + 29.5 v/0.066. Here
log(1/r_2) = 5 log(1/v) + log 2 + 4 log(20800M) ≤ 5 log(1/v) + 27.7, and v(5 log(1/v) + 30) ≤ 1.7·10⁻¹⁰ for v ≤ 10⁻¹²; so
N_I ≤ 1.157·2584·1.7·10⁻¹⁰ + 4.5·10⁻¹⁰ ≤ 10⁻⁶. Then w ≤ w(0)e^{N_I} ≤ 1.0023 (Lemma E1(c): w(0) = (1 + m²)^{1/2} ≤ 1.0022), and
 |Q(t)| ≤ e^{N_I}[|Q_0| + 1.0023 v r (2.4 C_A/(0.748 r) + 29.5/0.066²)] ≤ 1.000001[1.133 r + 3.22 vC_A + 706 v] ≤ 1.134 r + 10⁻⁸.

**Case II: 16ε ≤ r < r_2.** Then 2ε ≤ vτ_3/8 ≤ τ_3, τ_3 ≤ v/1000, 4τ_3 + ε ≤ R/100. *Window [0, τ_3].* We apply Proposition E4 to the arm points with radii in [16ε, r_2].
(H1): Lemma E2(c), ϑ̄(s) = 520M(s + 2ε)^{1/4},
ϑ̄(τ_3) ≤ 520 M (2τ_3)^{1/4} = v/40. (H2): Lemma E1 (b)–(e) (and Q, ψ, φ refer to true candidates: ρ > ε). (H3): r ≥ 2ε, so
(s + 2ε)^{1/4}/(r + s) ≤ (s + 2ε)^{−3/4} and ∫_0^{τ_3} ϑ̄(s)ds/(r+s) ≤ 520M·4(τ_3 + 2ε)^{1/4} = 4ϑ̄(τ_3) ≤ v/10. Hence
|Q(r, τ)| ≤ 0.56 v on [0, τ_3] and w(τ_3) ≤ 1.0022 ((r + τ_3)/r)^ν.
*After the window, τ ∈ [τ_3, t_e − t_0].* (The connector is over: 1.402ε < τ_3.) At time τ_3 (leg j+1):
|P − O| ≥ (P − O)·u_0 ≥ τ_3(1 − v/40), so D = r_{a_j} ≥ |P − O| − |P − x_{a_j}| − |x_{a_j}(t) − x_{a_j}(t_0)| ≥ 0.999τ_3 − 2ε − vτ_3 ≥
0.99 τ_3, and D ≥ 0.99τ_3 afterwards; also D ≥ τ/C_A − 3ε. So, while the base is in R,
ρ ≥ 0.99 max(0.99τ_3, τ/C_A − 3ε) − 2ε ≥ 0.49τ_3 + 0.495τ/C_A − 3.5ε ≥ 0.48(τ_3 + τ/C_A) (3.5ε ≤ 0.01τ_3), and ρ ≥ 0.066 while it
is in B. Therefore
 N_C := ∫_{τ_3}^{τ} v/ρ ≤ (vC_A/0.48) log(1 + 29.5/(C_Aτ_3)) + 447 v ≤ 10⁻⁶   (log(1/τ_3) ≤ 4 log(1/v) + 27.7),
 ∫_{τ_3}^{τ} ds/ρ² ≤ C_A/(0.2304 τ_3) + 29.5/0.066² ≤ 4.35 C_A/τ_3 + 6773,
 r w ≤ 1.0022 r^{1−ν}(2τ_3)^ν e^{N_C} ≤ 1.0023 r^{1−ν} ≤ 1.0023 (vτ_3)^{1−ν} ≤ 1.0024 vτ_3
((vτ_3)^{−ν} = exp(ν(5 log(1/v) + 27.7)) ≤ 1 + 10⁻⁹). Hence
 |Q(τ)| ≤ e^{N_C}[0.56 v + v·1.0024 vτ_3 (4.35 C_A/τ_3 + 6773)] ≤ 1.000001[0.56 v + 4.37 C_A v² + 6800 v²τ_3] ≤ 0.57 v. ∎

## Corollary E5 (excess class of the arm at the entry time). PROVED

Under the assumptions of Theorem E, with Q̄ := 0.12: for arm labels with radii 16ε ≤ r ≤ r' and every t ∈ [t_0, t_e],
 |ψ(r', t) − ψ(r, t)| ≤ 1.134 (r' − r) + (0.57 v + 10⁻⁸) log(r'/r) ≤ Q̄ log(r'/r),
 E(r, r'; t) ≤ ½ l_t(r, r') [1.134 (r' − r) + (0.57 v + 10⁻⁸) log(r'/r)]²   whenever the bracket is ≤ π/2.

*Proof.* ψ(r') − ψ(r) = ∫_r^{r'} Q dr''/r''. The unit tangents of the sub-arc lie in a cone of opening ≤ osc ψ < π, which
contains the chord direction e; so T·e ≥ cos(osc ψ) and E = ∫(1 − T·e) ds ≤ l (1 − cos osc ψ) ≤ l (osc ψ)²/2. ∎

## Corollary E6 (the tangents of the arm stay in a quarter-plane cone; the hook turns one way). PROVED

Under the assumptions of Theorem E, for every arm label with r ≥ 16ε and every t ∈ [t_0, t_e]:
 b_∞ − ψ(r, t) ∈ [−10⁻⁶, π/2 + 10⁻⁶],
i.e. all unit tangents of the arm part r ≥ 16ε lie in the closed cone of opening π/2 + 2·10⁻⁶ spanned (up to 10⁻⁶) by −u_0
and its rotation by −π/2.

*Proof.* φ̄ := b_∞ − ψ. Case I (r ≥ r_2): φ̄(0) = 2 arcsin v + (β − θ*) + φ_0 ∈ [0, 2.1v + 1.14 r] ⊂ [0, 0.119] (Lemma E1), and
|ψ'| ≤ v/(2ρ) (Lemma 1(ii)) gives |φ̄(t) − φ̄(0)| ≤ N_I/2 ≤ 5·10⁻⁷. Case II (r < r_2): on [0, τ_1], φ̄ ∈ [1.98v, 2.02v]
(proof of E4(iii), phase A); on [τ_1, τ_3], φ̄ ∈ [1.98 v, π/2 + 0.09 v] (E4(iii)); afterwards |φ̄(t) − φ̄(τ_3)| ≤ N_C/2 ≤ 5·10⁻⁷. ∎

## Corollary E7 (distance of the arm from the self-similar hook relation, time-resolved). PROVED

Under the assumptions of Theorem E let 16ε ≤ r ≤ r_2 = vτ_3 and ϑ̄(τ) = 520M(τ + 2ε)^{1/4}. Then for all τ ∈ [0, τ_3]:
 (a) |Q − (vτ/2ρ) sin 2φ| = |ζ(r, τ)| ≤ 0.31 r/v + 2.2 ϑ̄(τ);
 (b) |r∂_rx − (x − O) + vτ r̂| = |η(r, τ)| ≤ 0.63 r^{2−ν}(r + τ)^ν + 2.01 v ϑ̄(τ)(r + τ), ν = 1.0021 v;
 (c) |sin(β − b_∞)| ≤ 2.0047 v (r/(r+τ))^{1−ν} + 1.01 ϑ̄(τ);
and at the entry time: Q(r, t_e) = (1 + θ_1)[(vτ_3/2ρ) sin 2φ + ζ](r, τ_3) + θ_2 with |θ_1| ≤ 2·10⁻⁶, |θ_2| ≤ 1.2·10⁻⁸ v.
(In the straight-departure model of Claim 13 the left sides of (a), (b) vanish identically. So at time τ the arm at
radius r satisfies the hook relations up to r/v + (τ + 2ε)^{1/4}-terms: small for small scales *and* small times.)

*Proof.* In the proof of Proposition E4, (H3) was used only through ∫_0^τ ϑ̄(s)ds/(r+s); for the present ϑ̄ and r ≥ 2ε this is
≤ 4ϑ̄(τ) for every τ (proof of Theorem E, Case II). So I(τ) := ∫_0^τ (|η| + |p|)/ρ² ≤ 0.633 r + (2.02 v + 2.01)·4ϑ̄(τ), and
|ζ(τ)| ≤ (1.133 r + v I(τ))/(3.7 v) ≤ 0.31 r/v + 2.2 ϑ̄(τ): (a). (b) is the bound for |η(τ)| in that proof. (c): in step (ii)
of that proof replace |ℓ_P(s)| ≤ vs/40 by |ℓ_P(s)| ≤ sϑ̄(s): |ℓ_x(τ)| ≤ 2.0006 v r^{1−ν}(r+τ)^ν + 1.004 vϑ̄(τ)(r+τ), and
|sin e| ≤ (|ℓ_x| + τϑ̄(τ))/(0.998(r+τ)). Entry time: Q' = aQ + F on [τ_3, t_e − t_0] with ∫|a| ≤ N_C ≤ 10⁻⁶ and
∫|F| ≤ 1.2·10⁻⁸ v (proof of Theorem E, Case II); Q(τ_3) = ζ + (vτ_3/2ρ) sin 2φ. ∎

---------------------------------------------------------------------------------------------------------------------
**What is used from where (for the referee).** Theorem E = [Lemma E1: geometry at t_0] + [Lemma E2 ⇐ Theorem B + Theorem D:
the heading of Harry is 1/4-Hölder with a small constant, pointwise] + [Lemma E3: exact identities] + [Proposition E4:
abstract window estimate] + [(A1) ⇐ Corollary N: used only for the crude far-field integrals] + [Claim 14(a), Lemma 1].
The only place where smallness of v beyond "v ≤ 10⁻³" enters is Theorem B (v ≤ 10⁻¹²) and the crude integrals N_I, N_C
(which need v C_A log(1/v) ≪ 1).
