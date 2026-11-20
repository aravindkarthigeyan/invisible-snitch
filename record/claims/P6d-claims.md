# P6d — claims for independent referees (PROVED statements only): the start hypothesis (ST)

Stream P6d, round 6. Formulation unchanged: Harry has speed ≤ 1, H(0) = 0, path fixed in advance (depends on v, ε only);
Snitch S' = v(S − H)/|S − H|, S(0) = e^{iα} (d = 1); vision radius ε. Plane = ℂ = ℝ².

**Claimed PROVED:** Lemma D0 (tangent law), Claim D1 (curvature of the front at exact first contact), Claim D2 (global
geometry at first contact), Claim D3 (the connector does not create curvature), **Theorem D (the start S satisfies the
start hypothesis (ST) of `referee/P6a-claims.md` §5 with κ = 1/2, R = min(1/792, δ/100), uniformly in ε)**, Corollary D
(what Corollary M of P6a becomes).
**Not proved here:** the tip hypothesis (T) (stream P6c); nothing about the left-behind arm beyond its state at t_0.

**External inputs (statements used, with their sources).**
* `referee/P6a-claims.md`: the field F, f, A, a* and Lemma V; virtual candidates and Lemma VC; Lemma 1(i),(ii),(iii);
  Lemma 2(i); the definitions of l, c, E, of construction C's leg rule, of (ST) = (IC1)–(IC3). Lemma 1(iii) is used only
  for the *true* flow (field x/|x|, smooth off Harry), where it is an identity for C^∞ curves.
* `referee/P6c-claims.md` §0 and Claim 1(a),(b),(e),(f): for P(t) = t on [0, t_0], t_0 := 1/(1 − v), α ∈ (0, π),
  (ρ, β) := polar coordinates of S_α(t_0) − P(t_0), g(β) := sin β/tan^v(β/2), θ* := arccos(−v), g(θ*) ≤ 1,
  g_max := g(arccos v), τ := tan(α/2):
  (a) ρ g(β) = g(α), ρ(cos β + v) = −(1 − cos α), β ∈ (θ*, π);
  (b) B := ρ β_α = sin β · τ/(1 − v) > 0,  A := ρ_α = ρ(cos α − v)/sin α + (v − cos β) τ/(1 − v), both terms > 0 if cos α > v;
  (e) with α_s ∈ (0, arccos v) defined by g(α_s) = ε g_max: every |α| ≤ α_s is seen during [0, t_0]; for
      α ∈ [α_s, 2π − α_s], ρ_α(t) ≥ ε on [0, t_0] (so virtual = true candidate there);
  (f) ρ_s := ρ(α_s) ∈ (ε, 1.4 ε] for v ≤ 1/4, ε ≤ 1/20.
  Also from §0 there: the ordinate y of a candidate relative to Harry's line obeys y' = v y/ρ.
* Standard ODE theory: a field that is C¹ in x with globally Lipschitz derivative has a flow whose x-derivative is
  locally Lipschitz in the initial point.

Elementary identities used: g(α) = (1 + cos α) τ^{1−v}, sin α = τ(1 + cos α), dτ/dα = (1 + τ²)/2 = 1/(1 + cos α).

---------------------------------------------------------------------------------------------------------------------

## 0. The start S and notation

**Start S.** (i) Phase 1: P(t) = t for 0 ≤ t ≤ t_0 = 1/(1 − v) **exactly** (not "until the virtual candidate 0 is met").
(ii) Connector: O := P(t_0), u := (x_{α_s}(t_0) − O)/ρ_s; P(t) = O + (t − t_0)u until P meets the virtual candidate
x_{α_s}, at time t_s. (iii) From t_s on: the legs of construction C with first base a_{j_s} := α_s (leg rule of
P6a-claims §4; end label 2π, or 2π − α_s — "C_cut").
Virtual candidates x_θ are those of P6a-claims §1 for this path P (x_θ' = vF(x_θ − P), x_θ(0) = e^{iθ}); r := x − P,
ρ := |r|, m(ρ) := max(ρ, ε), Γ(ρ) := ρ/m(ρ)². T = e^{iψ} is the unit tangent of the front (direction of increasing
label), φ := arg r − ψ (so sin φ = T^⊥·r̂, cos φ = T·r̂, as in P6a-claims), p := T^⊥·r = ρ sin φ.
For a set 𝒜 of consecutive labels and a time t: k_𝒜(t) := sup_{a<b in 𝒜} |ψ_b − ψ_a|/l_t(a,b) (Lipschitz constant of
the tangent angle in arclength; ψ a continuous lift).

**Lemma D0 (tangent law; finiteness).** (a) For every label and time: ψ_t = −v Γ(ρ) sin φ cos φ (:= 0 if ρ = 0);
|ψ_t| ≤ v|p|/m(ρ)² ≤ v/m(ρ). (b) k_𝒜(t) < ∞ for every compact label set 𝒜, locally uniformly in t.
(c) If k := k_𝒜(t) < ∞ and a < b in 𝒜 with k·l_t(a,b) ≤ π, then
c(a,b;t) ≥ (2/k) sin(k l_t(a,b)/2) ≥ max( (2/π) l_t , l_t − k² l_t³/24 ), i.e. E(a,b;t) ≤ (k²/24) l_t(a,b)³.

*Proof.* (a) Lemma 1(ii) of P6a: T_t = v(AT − (T·AT)T) = v(T^⊥·AT)T^⊥, and by Lemma V(ii),
A = (f/ρ)I − (f/ρ − f') r̂r̂ᵀ with f/ρ − f' = ρ/m(ρ)² (= ρ/ε² inside the disc, 1/ρ outside; proof of Lemma V(iii)). So
T^⊥·AT = −Γ(ρ)(T^⊥·r̂)(T·r̂). At ρ = 0, A = (2/ε)I and T^⊥·AT = 0. Γ ≤ 1/m.
(b) DF is globally Lipschitz: inside the disc DF = (2ε − |x|)I/ε² − x xᵀ/(|x|ε²), outside DF = Π/ρ with ρ ≥ ε, and DF is
continuous across ρ = ε. So ∂_θx is locally Lipschitz in θ, and |∂_θx| ≥ 1 (Lemma VC(a)); hence ψ is Lipschitz in θ
and in arclength.
(c) Let e₀ := T at the arclength midpoint. |ψ(s) − ψ_mid| ≤ k|s − s_mid| ≤ π/2, so
c ≥ (x_b − x_a)·e₀ = ∫cos(ψ(s) − ψ_mid) ds ≥ ∫_{−l/2}^{l/2} cos(kσ)dσ = (2/k) sin(kl/2); sin x ≥ 2x/π and sin x ≥ x − x³/6
on [0, π/2]. ∎

## 1. Claim D1 (the front at exact first contact has curvature ≤ 2.2)

**Claim D1.** Let v ≤ 10⁻² and consider the true front α ↦ S_α(t_0), α ∈ (0, 2π), for Phase 1. It is a C^∞ curve and its
curvature satisfies |κ| ≤ 2.2 everywhere; more precisely |κ| ≤ 2.2 for α ∈ (0, 1/2] ∪ [2π − 1/2, 2π) and |κ| ≤ 1.1 for
α ∈ [1/2, 2π − 1/2]. Moreover, for α ∈ (0, 1/2]: tan(ψ − β) = B/A =: m ∈ (0, 0.63 ρ].
Consequently k_𝒜(t_0) ≤ 2.2 for every compact 𝒜 ⊂ (0, 2π), and (by (e)) the same holds for the virtual front on
𝒜 ⊂ [α_s, 2π − α_s].

*Proof.* Smoothness: for α ∈ (0, 2π) the true candidate stays at positive distance from Harry on [0, t_0]
(off the axis by y' = vy/ρ; α = π moves away), and the flow of x/|x − P(t)| is C^∞ there. By the reflection symmetry
it suffices to treat α ∈ (0, π].

*Arm, α ∈ (0, 1/2].* Numbers: τ ≤ tan(1/4) < 0.2554, cos α > 0.8775, c' := cos α − v ≥ 0.8675, 1 − v ≥ 0.99,
1 + cos α ≥ 1.8775, sin α ≤ 0.4795, τ/sin α = 1/(1 + cos α) ≤ 0.5327, 1 + τ² ≤ 1.0653.
From (a): g(β) ≤ g(θ*) ≤ 1 (g decreases on [arccos v, π)), so **ρ ≥ g(α) = (1 + cos α)τ^{1−v}**. From (b):
0 < B ≤ τ/(1 − v), 0 < v − cos β < 1 + v, and
  (L1) A ≥ ρ c'/sin α,   (L2) A ≥ g(α)c'/sin α = c' τ^{−v} ≥ c' ≥ 0.8675.
The curve is z(α) = ρe^{iβ} (relative to O), z_α = (A + iB)e^{iβ}, so ψ = β + arctan m, m = B/A > 0,
ψ_α = β_α + m_α/(1 + m²), ds/dα = (A² + B²)^{1/2} ≥ A, and β_α = B/ρ. Hence
  **|κ| ≤ B/(ρA) + |m_α|/A = m/ρ + |B_α|/A² + B|A_α|/A³.**
(1) m/ρ = B/(ρA) ≤ τ sin α/((1 − v)c'ρ²) (by L1) = τ²(1 + cos α)/((1 − v)c'ρ²) ≤ τ^{2v}/((1 − v)c'(1 + cos α))
    ≤ 1/(0.99·0.8675·1.8775) < 0.63. (This also gives m ≤ 0.63ρ.)
(2) B_α = cos β·(B/ρ)·τ/(1 − v) + sin β (1 + τ²)/(2(1 − v)). First part over A²:
    ≤ τ²/((1 − v)²ρA²) ≤ τ² sin²α/((1 − v)²c'²ρ³) = τ⁴(1 + cos α)²/((1 − v)²c'²ρ³) ≤ τ^{1+3v}/((1 − v)²c'²(1 + cos α))
    ≤ 0.2554/(0.9801·0.7525·1.8775) < 0.185. Second part over A²: ≤ 1.0653/(2·0.99·0.7525) < 0.715 (by L2).
(3) A_α. With (c'/sin α)' = −(1 − v cos α)/sin²α and ρ_α = A:
    A_α = A c'/sin α − ρ(1 − v cos α)/sin²α + sin β (B/ρ) τ/(1 − v) + (v − cos β)(1 + τ²)/(2(1 − v)),
    and A c'/sin α = ρc'²/sin²α + (v − cos β)τc'/((1 − v) sin α), c'² − 1 + v cos α = −sin²α − v c'. So
    **A_α = −ρ − vρc'/sin²α + (v − cos β)τc'/((1 − v) sin α) + sin β·Bτ/((1 − v)ρ) + (v − cos β)(1 + τ²)/(2(1 − v)).**
    Each term times B/A³:
    T1 = ρB/A³ ≤ (sin α/c')·B/A² (L1) ≤ sin α·τ/((1 − v)c'³) ≤ 0.4795·0.2554/(0.99·0.6528) < 0.190;
    T2 = vρc'B/(sin²α A³) = v·[ρc'/(sin α A)]·B/(sin α A²) ≤ v·(τ/sin α)/((1 − v)c'²) ≤ 0.72 v ≤ 0.0072;
    T3 ≤ (1 + v)(τ/sin α)(c'/A)·B/((1 − v)A²) ≤ 1.01·0.5327·0.2554/(0.99²·0.7525) < 0.187;
    T4 ≤ τ³/((1 − v)³ρA³) ≤ τ³ sin³α/((1 − v)³c'³ρ⁴) = τ⁶(1 + cos α)³/((1 − v)³c'³ρ⁴) ≤ τ^{2+4v}/((1 − v)³c'³(1 + cos α))
       ≤ 0.0653/(0.9702·0.6528·1.8775) < 0.055;
    T5 ≤ 1.01·1.0653·0.2554/(2·0.99²·0.6528) < 0.215.
Sum: |κ| ≤ 0.63 + 0.185 + 0.715 + 0.190 + 0.0072 + 0.187 + 0.055 + 0.215 < 2.2.

*Middle, α ∈ [1/2, π].* Claim: ρ_α(t) ≥ 0.479 on [0, t_0]. For α ∈ [1/2, π/2]: y' = vy/ρ ≥ 0, so ρ ≥ y ≥ sin α ≥ sin(1/2).
For α ∈ [π/2, π]: X := Re x_α satisfies X' = v(X − t)/ρ ≤ 0 as long as X ≤ t, which holds initially (X = cos α ≤ 0) and
therefore always; so X ≤ cos α ≤ 0, |y| ≥ sin α, ρ² = (t − X)² + y² ≥ cos²α + sin²α = 1.
At t = 0 the front is the unit circle, |κ| = 1. By Lemma 1(iii) of P6a (true flow),
κ_t = (v/ρ)(1 − 3 sin²φ)κ + (v/ρ²) sin φ (3cos²φ − 1), and |1 − 3 sin²φ| ≤ 2, |sin φ (3cos²φ − 1)| = |s(2 − 3s²)| ≤ 1
(s = sin φ ∈ [−1, 1]). So d|κ|/dt ≤ 4.18 v|κ| + 4.36 v, and with t_0 ≤ 1.0102:
|κ(t_0)| ≤ (1 + 1.05)e^{4.23v} − 1.05 ≤ 1.1.
*Lipschitz constant.* A C² curve with |κ| ≤ 2.2 has |ψ_b − ψ_a| ≤ 2.2 l(a,b). ∎

## 2. Claim D2 (global geometry at t_0)

**Claim D2.** Let δ ∈ (0, 1], v ≤ 10⁻³δ, and let ε ≤ 1/20. At time t_0, for the front of Phase 1:
(a) σ(α) := |∂_αS_α(t_0)| ≤ 1.52 (χ/2)^{−v} for all α ∈ (0, 2π), χ := min(α, 2π − α); and σ ≤ 1.0022 for χ ≥ 1/2.
(b) l_{t_0}(α_s, 2π − α_s) ≤ 6.82.
(c) For all labels a < b in [α_s, 2π − δ/2]: c(a,b; t_0) ≥ min( (2/π) l_{t_0}(a,b), 0.48 δ ).

*Proof.* (a) For χ ≥ 1/2: Lemma 1(i) of P6a (true flow): (log w)_t = v sin²φ/ρ ≤ v/0.479 (Claim D1, middle), w(0) = 1,
so σ ≤ e^{1.0102v/0.479} ≤ 1.0022 ≤ 1.52(χ/2)^{−v}. For α ∈ (0, 1/2]: by (a) of P6c,
cos β = −v − g(β)τ^{1+v} ≥ −10⁻³ − 0.2554 (g(β) ≤ 1), so 1 + cos β ≥ 0.7436, 1 − cos β ≥ 1, g(β) ≥ 0.7436^{(1+v)/2} ≥ 0.862.
Then ρ/sin α = g(α)/(g(β) sin α) = τ^{−v}/g(β) ≤ 1.161τ^{−v}, A ≤ ρ/sin α + (1 + v)τ/(1 − v) ≤ (1.161 + 0.257)τ^{−v},
ρ ≤ 2τ^{1−v}/0.862 ≤ 0.594, m ≤ 0.63ρ ≤ 0.375 (Claim D1), σ = A(1 + m²)^{1/2} ≤ 1.418·1.068 τ^{−v} ≤ 1.52(α/2)^{−v} (τ ≥ α/2).
(b) ≤ 2∫_0^{1/2}1.52(α/2)^{−v}dα + 1.0022(2π − 1) ≤ 2·1.523·(1/2)^{1−v} + 5.295 ≤ 6.82
(∫_0^Δ 1.52(α/2)^{−v}dα = 1.52·2^v Δ^{1−v}/(1 − v) ≤ 1.523 Δ^{1−v}).
(c) Let l := l_{t_0}(a,b). The tangent angle is 2.2-Lipschitz on [a,b] (Claim D1). If l ≤ π/2.2 (= 1.428…): Lemma D0(c)
gives c ≥ (2/π)l. If l > π/2.2: then Δ := b − a ≥ 1/2. Indeed, if Δ < 1/2 then either [a,b] ⊂ (0, π] or ⊂ [π, 2π), and
since the bound in (a) is decreasing in χ, l ≤ ∫_0^Δ 1.52(x/2)^{−v}dx ≤ 1.523·(1/2)^{1−v} < 0.77; or π ∈ (a,b), where
χ ≥ π − 1/2 and l ≤ 1.0022·(1/2); both are < 1.428. Every candidate has speed v, so |S_α(t_0) − e^{iα}| ≤ vt_0 ≤ 1.002v and
c ≥ |e^{ib} − e^{ia}| − 2.004v = 2 sin(Δ/2) − 2.004v with 1/2 ≤ Δ ≤ 2π − δ/2, i.e. 2 sin(Δ/2) ≥ 2 sin(δ/4) ≥ 0.4948δ
(δ/4 ≤ 1/4, sin x ≥ 0.9896x there). With v ≤ 10⁻³δ: c ≥ 0.49δ. ∎

## 3. Claim D3 (the connector creates no curvature ahead)

**Claim D3.** Let δ ∈ (0, 1], v ≤ 10⁻³δ, ε ≤ δ²/6400, start S, and 𝒜 := [α_s, 2π − δ/2] (labels). Then
(a) x_{α_s}(t) = P(t) + d(t)u on [t_0, t_s] with d' = −1 + v f(d), d(t_0) = ρ_s; t_s − t_0 ≤ ρ_s/(1 − v) ≤ 1.402 ε;
    P(t_s) = x_{α_s}(t_s).
(b) l_{t}(a,b) ≤ e^{3v} l_{t_0}(a,b) for all labels a < b and t ∈ [t_0, t_s].
(c) **k_𝒜(t) ≤ 2.2 + 49 v ≤ 2.25 for all t ∈ [t_0, t_s].**

*Proof.* (a) The ansatz solves x' = vF(x − P) (F(du) = f(d)u, P' = u) with the right initial value; uniqueness
(Lemma VC(a)). d' ≤ −(1 − v); ρ_s ≤ 1.4ε by (f). (b) Lemma 2(i), V(ii) of P6a: l' = v∫T·AT ds ≤ (2v/ε) l; 2·1.402v ≤ 3v.

(c) *Step 1: the pair inequality.* Fix t ∈ [t_0, t_s] and write k := k_𝒜(t) < ∞ (Lemma D0(b)). Parametrise the arc by
arclength s at time t. The function h(s) := Γ(ρ) sin φ cos φ = (T^⊥·r)(T·r)/(ρ m(ρ)²) is Lipschitz in s (a Lipschitz
function of (r, T), which are Lipschitz in s), ψ_t = −v h (Lemma D0(a)), and for a.e. s:
   h_s = Γ'(ρ) cos φ · sin φ cos φ + Γ(ρ) cos 2φ · (−sin φ/ρ − ψ_s),
because ρ_s = T·r̂ = cos φ, (arg r)_s = −sin φ/ρ, and φ = arg r − ψ. (Justification at the exceptional points: the
curve is injective (Lemma VC(b)), so r(s) = 0 for at most one s; Γ is C¹ except at ρ = ε, where it is Lipschitz; on the
set {s : ρ(s) = ε} the points with ρ_s ≠ 0 are isolated, and at the others ρ(s') − ε = o(|s' − s|), so Γ(ρ(·)) has
derivative 0 = Γ'·ρ_s there for either one-sided value of Γ'.) Since |Γ'| ≤ 1/m², Γ/ρ = 1/m², Γ ≤ 1/m and |ψ_s| ≤ k a.e.:
   |h_s| ≤ 2|sin φ|/m(ρ)² + k/m(ρ)  a.e.
Hence for labels a < b in 𝒜:  |d/dt(ψ_b − ψ_a)| = v|h(b) − h(a)| ≤ v l_t(a,b) Ξ(t),
   Ξ(t) := 2 S(t) + k_𝒜(t)/ε,   S(t) := sup_{𝒜, ρ>0} |sin φ|/m(ρ)² ≤ 1/ε².
Let K(t) := sup_{[t_0,t]} k_𝒜 (non-decreasing; K(t_0) ≤ 2.2 by Claim D1). Integrating, and using that l is non-decreasing
in time (Lemma VC), for t_0 ≤ t' ≤ t ≤ t_s:
   |ψ_b − ψ_a|(t) ≤ l_t(a,b) [ k_𝒜(t') + v ∫_{t'}^t (2 S̄(τ) + K(τ)/ε) dτ ]                                (*)
for any bound S̄ ≥ S. With S̄ = 1/ε², (*) shows K(t) ≤ K(t') + C(t − t') with C := v(2/ε² + K(t_s)/ε): K is continuous.

*Step 2: bound of S while K ≤ 4.* Let τ ∈ [t_0, t_s] with K(τ) ≤ 4, d := d(τ) ≤ ρ_s ≤ 1.4ε.
The angle φ_s(τ) at the label α_s (where r̂ = u is constant in time) obeys φ' = −ψ_t = vΓ(d) sin φ cos φ, so
|φ_s(τ)| ≤ |φ_s(t_0)| e^{1.402v}, and |φ_s(t_0)| = arctan m(α_s) ≤ 0.63ρ_s ≤ 0.882ε (Claim D1). So |φ_s(τ)| ≤ 0.9ε ≤ 1/2.
Let a ∈ 𝒜, a > α_s, l := l_τ(α_s, a).
 *Near, l ≤ 1/8.* Every tangent T_{s'}, s' ∈ [α_s, a], makes with u an angle ≤ |ψ_{s'} − ψ_{α_s}| + |φ_s| ≤ 4l + 1/2 ≤ 1. So
 (x_a − x_{α_s})·u = ∫T·u ≥ l cos 1 ≥ 0.54 l, and since r_a = (x_a − x_{α_s}) + d u: ρ_a ≥ r_a·u ≥ d + 0.54 l. Thus
 d ≤ ρ_a and l ≤ 1.86ρ_a. Further p_a = T_a^⊥·(x_a − x_{α_s}) + d T_a^⊥·u with
 |T_a^⊥·(x_a − x_{α_s})| ≤ ∫|sin(ψ_a − ψ_{s'})|ds' ≤ Kl²/2 and |T_a^⊥·u| ≤ Kl + |φ_s|. So
 |sin φ_a| = |p_a|/ρ_a ≤ K(1.86²/2 + 1.86)ρ_a + |φ_s| ≤ 3.6Kρ_a + 0.9ε ≤ (3.6K + 0.9) m(ρ_a), and
 |sin φ_a|/m(ρ_a)² ≤ (3.6K + 0.9)/ε. The same bound holds at a = α_s (|sin φ| ≤ 0.9ε).
 *Far, l > 1/8.* By (b), l_{t_0}(α_s, a) ≥ e^{−3v}/8 ≥ 0.124; by Claim D2(c), c(α_s, a; t_0) ≥ min(0.0789, 0.48δ) ≥ 0.078δ;
 chords do not decrease (Lemma VC(b)); so ρ_a(τ) ≥ 0.078δ − d ≥ 0.078δ − 1.4ε ≥ 0.07δ and |sin φ_a|/m² ≤ 205/δ².
 Hence S(τ) ≤ (3.6K(τ) + 0.9)/ε + 205/δ² whenever K(τ) ≤ 4.

*Step 3: bootstrap.* Let τ* := sup{τ ≤ t_s : K(τ) ≤ 4} (> t_0 by continuity). For t < τ*, (*) with t' = t_0 and Step 2:
   K(t) ≤ 2.2 + v(t − t_0)[ (2(3.6·4 + 0.9) + 4)/ε + 410/δ² ] ≤ 2.2 + 1.402v·34.6 + 575 vε/δ² ≤ 2.2 + 49v ≤ 2.25
(ε ≤ δ²/6400, v ≤ 10⁻³). By continuity K(τ*) ≤ 2.25 < 4, so τ* = t_s. ∎

## 4. Theorem D and Corollary D

**Theorem D (the start S satisfies (ST)).** Let δ ∈ (0, 1], R := min(1/792, δ/100), κ := 1/2,
   v ≤ 10⁻³δ,   ε ≤ ε₀ := min(δ²/6400, R/64).
For the start S:
1. (Seen.) Every direction α with |α| ≤ α_s (mod 2π) is seen by time t_0; α_s ≤ 2.1 ε.
2. (Leg start.) t_s ≤ t_0 + 1.402ε ≤ 1.0011 and P(t_s) = x_{α_s}(t_s); |x_{α_s}(t_0) − P(t_0)| = ρ_s ≤ 1.4ε.
3. (IC1) At t_s, on the arc 𝒜 = [α_s, 2π − δ/2] the tangent angle of the virtual front is 2.25-Lipschitz in arclength,
   and E(a,b; t_s) ≤ (2.25²/24) λ³ ≤ κ² λ³ for all pairs in 𝒜 with λ := l_{t_s}(a,b) ≤ 1.39 (in particular for λ ≤ 32R).
4. (IC2) c(a,b; t_s) ≥ 16R for all pairs in 𝒜 with λ > 32R.
5. (IC3) κR ≤ 1/1584 and ε ≤ R/64.
6. (Lengths.) l_{t_s}(α_s, 2π − α_s) ≤ 6.85 and l_{t_s}(α_s, 2π) ≤ 6.9.
Hence (ST) of P6a-claims §5 holds at the leg start t_s = t_{j_s}, base a_{j_s} = α_s, on the arc [α_s, 2π − δ/2], with
ε-independent constants. Labels not covered by (ST): [2π − δ/2, 2π]; of these, (2π − α_s, 2π] are already seen (item 1),
and [2π − δ/2, 2π − α_s] is the left-behind arm, on which at time t_0 the front is the mirror image of the right arm
(Claim D1: curvature ≤ 2.2, |tan(ψ − β)| ≤ 0.63ρ, no point within ε of O).

*Proof.* 1: (e). Since α_s < π/2: tan^{1−v}(α_s/2) = g(α_s)/(1 + cos α_s) ≤ εg_max ≤ 1, so
α_s ≤ 2 tan(α_s/2) ≤ 2(εg_max)^{1/(1−v)} ≤ 2εg_max ≤ 2.1ε (log g_max = ((1+v)/2)log(1+v) + ((1−v)/2)log(1−v) ≤ v²). 2: Claim D3(a), (f), t_0 ≤ 1.0011.
3: Claim D3(c) and Lemma D0(c) (2.25 λ ≤ π for λ ≤ 1.39; 2.25²/24 < 0.211). 4: let λ > 32R. By Claim D3(b),
l_{t_0}(a,b) ≥ e^{−3v}λ ≥ 0.997·32R; by Lemma VC(b) and Claim D2(c), c(t_s) ≥ c(t_0) ≥ min(0.634·0.997·32R, 0.48δ)
≥ min(20.2R, 48R) ≥ 16R. 5: R/2 ≤ 1/1584. 6: Claim D2(b) and D3(b): 6.82e^{3v} ≤ 6.85. For labels θ ∈ (2π − α_s, 2π):
on [0, t_ε], t_ε := (1 − ε)/(1 − v), the candidate is true and ρ_θ ≥ 1 − (1 − v)t ≥ ε (as in Lemma C(1) of P6a); by Lemma
1(i), V(ii), (log|∂_θx|)_t ≤ v a*(ρ), which integrates to ≤ μ log(1/ε) on [0, t_ε] (μ = v/(1 − v)) and to ≤ (2v/ε)·2.41ε on
[t_ε, t_s] (t_s − t_ε ≤ ε/(1 − v) + 1.402ε). So l_{t_s}(2π − α_s, 2π) ≤ α_s ε^{−μ}e^{4.82v} ≤ 2(g_max)^{1/(1−v)}e^{4.82v} ε ≤ 2.02ε. ∎

**Corollary D (Corollary M of P6a with the start S).** Let δ ∈ (0, 1] and K_T be absolute constants such that the tip
hypothesis (T) of P6a-claims §4 holds with b* := 2π − δ for every t ≥ t_s, for the path "start S, then the legs of
construction C from the base α_s", for all v ≤ v₁ and ε ≤ ε₀ = min(δ²/6400, R/64), R = min(1/792, δ/100). Put L_s := 6.9,
K* := 32 + 1/1960 + 32L_s/R + K_T and v₀ := min(v₁, 10⁻¹², 10⁻⁶R/29.6, 1/(2K*)). Then for v ≤ v₀, ε ≤ ε₀ every direction is
seen by time 1.0011 + 2.1·6.9 < 15.5, independent of ε, and (Lemma A4.1 of the paper) is caught exactly.

*Proof.* This is Corollary M of P6a verbatim, with κ = 1/2, R as above, T_s = 1.0011, L_s = 6.9: the path has speed ≤ 1,
is fixed in advance and coincides with construction C from the leg start t_s on; all labels < a_{j_s} = α_s are seen
(Theorem D.1); R_{j_s} = l_{t_s}(α_s, 2π) ≤ L_s (D.6); (ST) holds on [a_{j_s}, 2π − δ/2] (D.3–5); a_{j_s} = α_s ≤ 2.1ε < 2π − δ;
ε₀ ≤ δ. (Theorem D needs v ≤ 10⁻³δ; this follows from v ≤ 10⁻⁶R/29.6 ≤ 10⁻⁸δ/29.6.) ∎

**Remarks.** (1) *C_cut.* If the legs are run with end label b_e = 2π − α_s instead of 2π (everything beyond is seen),
the same holds with R_{j_s} = l_{t_s}(α_s, 2π − α_s) ≤ 6.85, provided Theorems R, B are read with b_e in the place of 2π
(their proofs use the last label only as the end of the arc; this is the reading already used in
`referee/P6a2-claims.md`). Hypothesis (ST⁺) of Theorem F there holds for the start S with m = 2:
t_s − t_0 ≤ 1.402ε, r_{a_{j_s}} = ρ_s ≤ 1.4ε, a_{j_s} = α_s ≤ 2.1ε, R_{j_s} ≤ 6.85, (ST) on [α_s, 2π − θ₀/2] (θ₀ = δ).
Here t_0 = 1/(1 − v) exactly and O = P(t_0) is the true corner — NOT construction C's own first contact with the
virtual candidate 0.
(2) Theorem D gives more than (ST): a pointwise bound on the tangent's Lipschitz constant (hence (IC1) at all scales
λ → 0, not only λ ≥ ε/2), on an arc that reaches to within δ/2 of the tip.
(3) The restriction ε ≤ δ²/6400 (instead of ε ≲ δ) is only used in the "far" case of Claim D3, Step 2.
