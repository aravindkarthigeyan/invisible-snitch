# P6c-claims: statements claimed PROVED by stream P6c (tip and endgame), with full proofs

Only PROVED statements appear here. Numerical evidence, heuristics and conjectures are in `reports/P6c-1.md`.
Numerical sanity checks of every formula below: `code/P6c/check_tip.py` (output `check_tip.out`).

## 0. Setting and facts used

d = 1, 0 < v < 1, 0 < ε < 1. Plane = ℂ, a·b = Re(a b̄). Harry's path P is 1-Lipschitz, P(0) = 0. The Snitch
candidate θ starts at e^{iθ} and obeys S' = v (S − P)/|S − P| while S ≠ P. It is *seen* by time t if |S_θ(s) − P(s)| ≤ ε
for some s ≤ t.

**Straight-run integrals (paper, Prop. `prop:integrals`, Lemma `lem:k`).** While Harry moves with constant unit velocity u,
write a candidate off Harry's line in polar form S − P = ρ e^{iβ} u (bearing β ∈ (0, π) after a reflection). Then
ρ' = v − cos β, ρ β' = sin β, and with

  g(β) := sin β / tan^v(β/2) = (1 + cos β)^{(1+v)/2} (1 − cos β)^{(1−v)/2},   g'/g = (cos β − v)/sin β,

  C := ρ g(β) is constant,   h := ρ (cos β + v) satisfies h' = −(1 − v²).

(One line each: h' = (v − cos β)(cos β + v) − sin²β = v² − 1; (log C)' = (v − cos β)/ρ + ((cos β − v)/sin β)(sin β/ρ) = 0.)
g increases on (0, arccos v], decreases on [arccos v, π), g(0+) = g(π−) = 0,
g_max := g(arccos v) = (1+v)^{(1+v)/2}(1−v)^{(1−v)/2}. k(β) := (cos β + v)/g(β) = h/C is strictly decreasing from +∞ to
−∞ on (0, π) (k' = −(1−v²)/(g sin β)), so (C, h) determine (ρ, β): β = k^{-1}(h/C), ρ = C/g(β).
A candidate with β ∈ (0, π) at one time of a straight run keeps β ∈ (0, π) and ρ ≥ C/g_max > 0 during the run
(y' = v y/ρ for the ordinate y relative to Harry's line, so y keeps its sign while ρ > 0, and then C is constant).

Notation: θ* := arccos(−v), g(θ*) = (1−v)^{(1+v)/2}(1+v)^{(1−v)/2} ≤ 1
(log g(θ*) = ((1+v)/2) log(1−v) + ((1−v)/2) log(1+v) ≤ −v²), t_0 := 1/(1−v).

**Virtual candidates (paper, Lemmas D2.1–D2.4).** F(x) := x/max(|x|, ε); |F| ≤ 1, F is ε^{-1}-Lipschitz, monotone, and
|F(x) − F(y)| ≤ |x − y|/max(ε, min(|x|, |y|)). S̃_θ(0) = e^{iθ}, S̃_θ' = v F(S̃_θ − P), ρ_θ := |S̃_θ − P|,
J_θ(t) := ∫_0^t ds/max(ε, ρ_θ). Then: (a) global existence/uniqueness, |S̃_θ(t) − S̃_φ(t)| ≤ e^{vt/ε}|θ − φ|; (b)
|S̃_θ − S̃_φ| is non-decreasing in t; (c) ρ_θ(t) ≤ ε for some t ⇒ θ is seen by t; S̃_θ = S_θ as long as ρ_θ ≥ ε.
Lemma D2.3: a continuous curve γ on an interval with limsup_{x'→x}|γ(x') − γ(x)|/|x' − x| ≤ Λ at every x is Λ-Lipschitz.

---

## Claim 1 (T1: the front at first contact — exact description of the tip). PROVED

Let P(t) = t on [0, t_0] (Phase 1). For α ∈ (0, π) let (ρ, β) = (ρ(α), β(α)) be the polar coordinates of
S_α(t_0) − P(t_0) (bearing measured from the positive real axis), σ(α) := |∂_α S_α(t_0)|, and φ(α) the angle between
∂_α S_α(t_0) and the radial direction e^{iβ}.

(a) ρ (cos β + v) = −(1 − cos α) and ρ g(β) = g(α). Hence β ∈ (θ*, π) and ρ ≥ g(α)/g(θ*).

(b) ρ β_α = sin β · tan(α/2)/(1 − v),   ρ_α = ρ (cos α − v)/sin α + (v − cos β) tan(α/2)/(1 − v).
In particular β_α > 0 on (0, π), and ρ_α > 0 when cos α ≥ v.

(c) (Radial flatness.) If cos α > v then φ ∈ (0, π/2) and

  tan φ ≤ g(θ*) sin β tan^{1+v}(α/2) / ((1 − v)(cos α − v))
      ≤ [g(θ*)/((1 − v)(cos α − v))] · ( g(θ*) ρ/(1 + cos α) )^{(1+v)/(1−v)}.

For v ≤ 0.1 and α ≤ 1/2: tan φ ≤ 1.43 (0.533 ρ)^{(1+v)/(1−v)} ≤ 0.77 ρ.

(d) (Stretch.) If cos α > v:

  (cos α − v)/(g(θ*) tan^v(α/2)) ≤ σ ≤ [ρ (cos α − v)/sin α + (1+v) tan(α/2)/(1−v)] (1 + tan²φ)^{1/2},

and α^v σ(α) → (1 − v) 2^v/g(θ*) as α → 0+. (So σ ≍ α^{-v}: not bounded, but integrable.)

(e) (Seen set.) Let α_s ∈ (0, arccos v) be defined by g(α_s) = ε g_max. Every α with |α| ≤ α_s is seen during [0, t_0].
For α ∈ [α_s, 2π − α_s]: ρ_α(t) ≥ ε for all t ∈ [0, t_0] (so S̃_α = S_α on [0, t_0]).

(f) ρ_s := ρ(α_s) satisfies ε < ρ_s ≤ ε (1+v)^v (1−v)^{(1−v)/2} (1 − v − 2 g_max² ε)^{−(1+v)/2} whenever
v + 2 g_max² ε < 1 and ε g_max ≤ 1; for v ≤ 1/4, ε ≤ 1/20 this gives ρ_s ≤ 1.4 ε.

(g) (Order.) On the arc [α_s, 2π − α_s] the bearing of S_α(t_0) from P(t_0) is strictly monotone, with total variation
< 2(π − θ*) = π − 2 arcsin v, and no point of the arc is within distance ε of P(t_0).

**Proof.** α ∈ (0, π) stays in the open upper half-plane with ρ > 0 on [0, t_0] (§0), so the flow is C¹ in α there and
(ρ, β) are C¹ functions of α.

(a) At t = 0: ρ = 1, β = α, so C = g(α), h(0) = cos α + v. At t_0, (1 − v²) t_0 = 1 + v, so
h(t_0) = cos α + v − (1 + v) = −(1 − cos α) < 0. Thus cos β < −v, i.e. β ∈ (θ*, π); g is decreasing on
[arccos v, π) ∋ θ*, so g(β) ≤ g(θ*) and ρ = g(α)/g(β) ≥ g(α)/g(θ*).

(b) Differentiate the two identities of (a) in α. The second, divided by g(β), reads (using g'/g and g(α)/g(β) = ρ)

  ρ_α + ρ β_α (cos β − v)/sin β = ρ (cos α − v)/sin α.                         (1)

The first reads ρ_α (cos β + v) − ρ β_α sin β = −sin α. Substituting ρ_α from (1) and using
(cos β − v)(cos β + v)/sin β + sin β = (1 − v²)/sin β:

  ρ β_α (1 − v²)/sin β = sin α + ρ (cos β + v)(cos α − v)/sin α = [sin²α − (1 − cos α)(cos α − v)]/sin α
                = (1 − cos α)(1 + v)/sin α,

because ρ (cos β + v) = −(1 − cos α) and sin²α − (1 − cos α)(cos α − v) = (1 − cos α)(1 + cos α − cos α + v).
This gives ρ β_α; then (1) gives ρ_α. Since cos β < −v, v − cos β > 2v ≥ 0, so both terms of ρ_α are positive when cos α ≥ v.

(c) ∂_α S = ρ_α e^{iβ} + ρ β_α i e^{iβ}, so tan φ = ρ β_α/ρ_α with ρ_α, ρ β_α > 0, and dropping the second (positive) term
of ρ_α,

  tan φ ≤ sin β tan(α/2) sin α / ((1 − v)(cos α − v) ρ) = sin β · 2 sin²(α/2)/((1 − v)(cos α − v) ρ).

By (a), 1/ρ ≤ g(θ*)/g(α), and g(α) = 2 sin^{1−v}(α/2) cos^{1+v}(α/2), so 2 sin²(α/2)/g(α) = tan^{1+v}(α/2): first
inequality. Also g(α) = (1 + cos α) tan^{1−v}(α/2) and g(α) = ρ g(β) ≤ ρ g(θ*) give
tan(α/2) ≤ (g(θ*) ρ/(1 + cos α))^{1/(1−v)}: second inequality (with sin β ≤ 1).
Numbers for v ≤ 0.1, α ≤ 1/2: g(θ*) ≤ 1, cos α ≥ 0.87758, (1 − v)(cos α − v) ≥ 0.9 · 0.77758 = 0.69982,
1/0.69982 < 1.43, 1/(1 + cos α) ≤ 0.5326. Finally ρ ≤ |S_α(t_0) − e^{iα}| + |e^{iα} − 1| + |1 − t_0| ≤ v t_0 + α + v t_0
≤ 0.7223, so 0.533 ρ < 1 and, the exponent being ≥ 1, 1.43 (0.533ρ)^{(1+v)/(1−v)} ≤ 1.43 · 0.533 ρ ≤ 0.77 ρ.

(d) σ = (ρ_α² + (ρβ_α)²)^{1/2} = ρ_α (1 + tan²φ)^{1/2}. Lower bound: σ ≥ ρ_α ≥ ρ (cos α − v)/sin α
≥ g(α)(cos α − v)/(g(θ*) sin α), and g(α)/sin α = tan^{-v}(α/2). Upper bound: v − cos β ≤ 1 + v in (b).
Limit: by (a) and (c), 0 < −(cos β + v) = (1 − cos α)/ρ ≤ g(θ*) tan^{1+v}(α/2) → 0, so β → θ*, ρ ∼ g(α)/g(θ*);
g(α) ∼ 2 (α/2)^{1−v} = 2^v α^{1−v}; hence ρ (cos α − v)/sin α ∼ (1 − v) 2^v α^{-v}/g(θ*), the second term of ρ_α is
O(α), and tan φ → 0.

(e) α = 0: ρ = 1 − (1 − v)t reaches ε before t_0. Let 0 < α ≤ α_s. The bearing is continuous in t, equals
α < arccos v at t = 0 and β(α) > θ* > arccos v at t_0, so at some time it equals arccos v, where
ρ = C/g_max = g(α)/g_max ≤ g(α_s)/g_max = ε (g increasing on (0, arccos v]). Negative α: reflection.
Let α ∈ [α_s, π). The bearing is increasing in t (ρβ' = sin β > 0). If α ≥ arccos v then cos β ≤ v throughout,
ρ' = v − cos β ≥ 0 and ρ ≥ 1 > ε. If α_s ≤ α < arccos v then ρ = g(α)/g(β) ≥ g(α)/g_max ≥ g(α_s)/g_max = ε.
α = π: ρ = 1 + (1 + v)t. α ∈ (π, 2π − α_s]: reflection.

(f) ρ_s = ε g_max/g(β_s) with β_s := β(α_s) > θ* > arccos v, so g(β_s) < g_max and ρ_s > ε. Since α_s < π/2,
tan^{1−v}(α_s/2) = g(α_s)/(1 + cos α_s) ≤ ε g_max ≤ 1, so tan(α_s/2) ≤ ε g_max and
1 − cos α_s = 2 sin²(α_s/2) ≤ 2 ε² g_max². By (a), −cos β_s − v = (1 − cos α_s)/ρ_s ≤ 2 ε g_max², i.e.
cos β_s ≥ −c_s, c_s := v + 2 g_max² ε < 1. As 1 − cos β_s ≥ 1 + v,
g(β_s) = (1 + cos β_s)^{(1+v)/2}(1 − cos β_s)^{(1−v)/2} ≥ (1 − c_s)^{(1+v)/2}(1 + v)^{(1−v)/2}, and
ρ_s/ε = g_max/g(β_s) ≤ (1+v)^v (1−v)^{(1−v)/2} (1 − c_s)^{−(1+v)/2}.
For v ≤ 1/4, ε ≤ 1/20: g_max² = exp((1+v) log(1+v) + (1−v) log(1−v)) is increasing in v
(derivative log((1+v)/(1−v)) ≥ 0), so g_max² ≤ 1.25^{1.25} · 0.75^{0.75} < 1.07, ε g_max ≤ 1, c_s ≤ 0.357,
(1+v)^v ≤ 1.25^{0.25} < 1.058, (1−v)^{(1−v)/2} ≤ 1, (1 − c_s)^{−(1+v)/2} ≤ 0.643^{−0.625} < 1.32; product < 1.4.

(g) By (b) β is strictly increasing on (0, π), from θ* (limit, by (d)) to π; reflection gives monotonicity on
(π, 2π) with values in (π, 2π − θ*); β(π) = π. So the total variation on [α_s, 2π − α_s] is < 2π − 2θ*.
For α ∈ [α_s, arccos v]: ρ(α) = g(α)/g(β) > g(α)/g_max ≥ ε; for α ≥ arccos v, ρ ≥ 1 by (e). ∎

**Remark (reading).** With Phase 1 ending exactly at t_0, the singular blob of the tip is entirely inside the set already
seen; the two unseen arms start at distance ρ_s ∈ (ε, 1.4ε] from Harry, leave him at bearings within
g(θ*) tan^{1+v}(α/2) (in cosine) of ±θ*, and are flat as seen from Harry at every scale ρ ≥ ε with exponent
γ = (1+v)/(1−v) ≥ 1 and an ε-independent constant; the only singularity is that of the parametrisation, σ ≍ α^{-v}.

---

## Claim 2 (T2: universal inner profile of the virtual front of construction W). PROVED

Let V(X) := v X/max(|X|, 1) − 1 (a globally Lipschitz autonomous field on ℂ). For c > 0 let σ_c := −2vc/((1−v²) g_max) and,
for σ ≤ σ_c, Z_c(σ) := R e^{iβ} with β := k^{-1}(−(1−v²)σ/c) ∈ (0, arccos v], R := c/g(β). R is decreasing in σ and
→ ∞ as σ → −∞; let σ_c¹ := sup{σ ≤ σ_c : R ≥ 1 on (−∞, σ]}. Then Z_c solves X' = V(X) on (−∞, σ_c¹]; let X_c be the
unique solution of X' = V(X) on ℝ that equals Z_c there.

*Statement.* Let P(s) = s on [0, τ] (any τ > 0, any ε ∈ (0,1)). For α ∈ (0, arccos v], c := g(α)/ε and all t ∈ [0, τ]:

  S̃_α(t) − P(t) = ε X_c( (t − t_0)/ε + (1 − cos α)/((1 − v²) ε) ).

In particular, at the end τ_1' = t_0 − ε σ_* of connector 1 of construction W (Theorem D2), where
σ_* := 1/(1−v) − (1/v) log(1/(1−v)) = Σ_{n≥1} (n/(n+1)) v^n ∈ (v/2, v/(1−v)),

  |S̃_α(τ_1') − P(τ_1') − ε X_c(−σ_*)| ≤ (1 + v)(1 − cos α)/(1 − v²) ≤ 2 (g(α))^{2/(1−v)}/(1 − v)   (if g(α) ≤ 1):

the front within C ≤ Mε of the tip is ε times a curve c ↦ X_c(−σ_*) depending only on v, up to an error
≤ 2 M^{2/(1−v)} ε^{2/(1−v)}/(1−v) = o(ε). For c ≥ g_max the profile is explicit: X_c(σ) = R e^{iβ} with
R g(β) = c, R (cos β + v) = −(1 − v²) σ for all σ.

**Proof.** Z_c: β ↦ k(β) is a decreasing bijection (0, arccos v] → [k(arccos v), ∞) = [2v/g_max, ∞), and
−(1−v²)σ/c ≥ 2v/g_max iff σ ≤ σ_c; as σ decreases, β decreases to 0, g(β) → 0, R → ∞. The curve Z_c has
C := R g(β) = c and h := R(cos β + v) = −(1−v²)σ. In {|X| ≥ 1, Im X > 0} the field is V(X) = v X/|X| − 1, the relative
field of a straight run, whose solutions are exactly the curves with C constant and h' = −(1−v²) (the map (R, β) ↦ (C, h)
is injective on the half-plane); so Z_c is a solution wherever R ≥ 1, i.e. on (−∞, σ_c¹] (R is monotone there because
R' = v − cos β < 0 for β < arccos v).
Put t(σ) := t_0 − (1 − cos α)/(1 − v²) + εσ and Y(σ) := (S̃_α(t(σ)) − P(t(σ)))/ε for t(σ) ∈ [0, τ]. Since
F(εY) = Y/max(|Y|, 1), Y' = v F(εY) − 1 = V(Y). At t = 0, i.e. σ_0 := −(t_0 − (1 − cos α)/(1−v²))/ε,
Y(σ_0) = e^{iα}/ε. On the other hand −(1−v²)σ_0/c = ((1 + v) − (1 − cos α))/g(α) = k(α), so Z_c(σ_0) has β = α
(allowed as α ≤ arccos v) and R = c/g(α) = 1/ε ≥ 1; R being decreasing in σ, σ_0 ≤ σ_c¹. Thus Y(σ_0) = X_c(σ_0) and
Y = X_c by uniqueness. τ_1': S̃_0 − P = ρ_0 ≥ 0 on the axis with ρ_0' = −1 + v min(1, ρ_0/ε); ρ_0 = ε at time
(1 − ε)/(1 − v), and the remaining time is ∫_0^ε dρ/(1 − vρ/ε) = (ε/v) log(1/(1−v)); the series for σ_* follows from
1/(1−v) = Σ v^n and (1/v) log(1/(1−v)) = Σ v^n/(n+1). The error bound: |X_c'| ≤ 1 + v, time shift
(1 − cos α)/((1−v²)ε), and 1 − cos α ≤ 2 tan²(α/2) = 2 (g(α)/(1 + cos α))^{2/(1−v)} ≤ 2 g(α)^{2/(1−v)}.
For c ≥ g_max: R = c/g(β) ≥ 1 always, so the solution stays in the outer region, where it is given by the invariants. ∎

---

## Claim 3 (T3: transport of tangent vectors along a straight run). PROVED

Let a ↦ S_a be a C¹ curve of candidates (true dynamics) lying in the open half-plane to the left of Harry's line during a
straight unit-speed run, with polar coordinates (ρ, β) about Harry. Then c_1 := ∂_a C and c_2 := ∂_a h do not depend on
time, and at every time of the run

  ρ_a = [ sin²β · c_1/g(β) + (cos β − v) c_2 ]/(1 − v²),   ρ β_a = sin β [ (cos β + v) c_1/g(β) − c_2 ]/(1 − v²).

**Proof.** For each a, C is constant and h(t) = h(t_1) − (1−v²)(t − t_1); differentiating in a (the flow is C¹ in a) gives
the first claim. From C = ρ g(β), h = ρ(cos β + v):
c_1/g(β) = ρ_a + ρβ_a (cos β − v)/sin β, c_2 = ρ_a (cos β + v) − ρβ_a sin β. This linear system in (ρ_a, ρβ_a) has
determinant −sin β − (cos²β − v²)/sin β = −(1 − v²)/sin β ≠ 0, and the displayed pair solves it:
ρ_a + ρβ_a (cos β − v)/sin β = [sin²β + cos²β − v²] c_1/(g (1−v²)) + [(cos β − v) − (cos β − v)] c_2/(1−v²) = c_1/g;
ρ_a(cos β + v) − ρβ_a sin β = [(cos β+v) sin²β − sin²β (cos β + v)] c_1/(g(1−v²)) + [cos²β − v² + sin²β] c_2/(1−v²) = c_2. ∎

---

## Claim 4 (T4: the hook law — a ray left behind at a wedge angle). PROVED

Let ω ∈ (0, π/2) with cos ω > v. At time 0 Harry is at 0 and then runs straight, P(s) = s. Consider the candidates
Q_r, r > 0, with Q_r(0) = r e^{i(π − ω)} (a ray from Harry's starting point making the angle ω with the backward
direction). For s > 0 let (ρ, β) be the polar coordinates of Q_r(s) − P(s), λ := s/r, φ the angle between ∂_r Q_r(s)
and the line through Harry and Q_r(s), and A := (2^v g(π − ω)/(1 + v))^{1/(1+v)}, g(π − ω) = sin ω tan^v(ω/2).

(a) ρ g(β) = r g(π − ω), ρ (−cos β − v) = r (cos ω − v) + (1 − v²) s, β ∈ (π − ω, π).
(b) ρ β_r = −λ sin β,   ρ_r = [ρ sin²β/r + (v − cos β)(cos ω − v)]/(1 − v²) > 0.
(c) |tan φ| = (1 − v²) λ sin β / [ρ sin²β/r + (v − cos β)(cos ω − v)].
(d) [g(π−ω)(cos ω − v)/(cos ω − v + (1 − v²)λ)]^{1/(1+v)} ≤ sin β ≤ A λ^{−1/(1+v)}.
(e) |tan φ| ≤ (1 − v²) A λ^{v/(1+v)} / ((v + cos ω)(cos ω − v)).
(f) λ^{−v/(1+v)} |tan φ| → (1 − v) A/(cos ω − v) as λ → ∞.
(g) |∂_r Q_r(s)| ≥ λ sin β ≥ λ [g(π−ω)(cos ω − v)/(cos ω − v + (1 − v²)λ)]^{1/(1+v)}, which tends to ∞ like
    λ^{v/(1+v)} as λ → ∞.

*Tip case.* For ω = 2 arcsin v (the angle between the left arm of Claim 1 and the backward extension of the right arm;
needs v < 1/2): cos ω − v = (1 − 2v)(1 + v), v + cos ω = (1 − v)(1 + 2v), g(π − ω) = 2 v^{1+v} (1 − v²)^{(1−v)/2},
A = 2v ((1 − v²)^{(1−v)/2}/(1 + v))^{1/(1+v)} ≤ 2v, and (e) reads

  |tan φ| ≤ A λ^{v/(1+v)}/(1 − 4v²) ≤ 2v (s/r)^{v/(1+v)}/(1 − 4v²).

**Proof.** (a) Initially ρ = r, β = π − ω ∈ (π/2, π): C = r g(π − ω), h(0) = r (v − cos ω), h(s) = h(0) − (1−v²)s.
β increases in s (ρβ' = sin β > 0) and stays < π (§0).
(b) Claim 3 with a = r: c_1 = g(π − ω), c_2 = v − cos ω. Then
(cos β + v) c_1/g(β) − c_2 = (cos β + v) ρ/r − (v − cos ω) = (h(s) − h(0))/r = −(1 − v²) λ, which gives ρβ_r; and
ρ_r = [sin²β ρ/r + (cos β − v)(v − cos ω)]/(1−v²). Since cos β < −cos ω < −v, both terms are positive.
(c) tan φ = ρβ_r/ρ_r.
(d) From the product form of g, sin^{1+v}β = g(β) (1 − cos β)^v, so g(β) ≤ sin^{1+v}β ≤ 2^v g(β) (β > π/2).
By (a), g(β) = r g(π − ω)/ρ and ρ = [r (cos ω − v) + (1−v²)s]/(−cos β − v) with cos ω − v ≤ −cos β − v ≤ 1 − v. Hence
(1 + v) s ≤ ρ ≤ r + (1 − v²)s/(cos ω − v), which gives g(π−ω)(cos ω − v)/(cos ω − v + (1−v²)λ) ≤ g(β) ≤ g(π−ω)/((1+v)λ).
(e) Drop the first term of the bracket in (c), use v − cos β ≥ v + cos ω and (d).
(f) As λ → ∞, g(β) → 0 with β ∈ (π − ω, π), so β → π; then −cos β − v → 1 − v, ρ/s → 1 + v,
sin^{1+v}β = g(β)(1 − cos β)^v ∼ 2^v g(π−ω)/((1 + v)λ), i.e. sin β ∼ A λ^{−1/(1+v)}; and
ρ sin²β/r = (ρ/s) λ sin²β ∼ (1 + v) A² λ^{−(1−v)/(1+v)} → 0. So the bracket in (c) tends to (1 + v)(cos ω − v).
(g) |∂_r Q| ≥ |ρβ_r| = λ sin β, and (d).
Tip case: sin(2a) = 2v(1−v²)^{1/2}, tan a = v/(1−v²)^{1/2}, cos 2a = 1 − 2v² for a = arcsin v;
(1 − v²)/((1 − v)(1 + 2v)(1 − 2v)(1 + v)) = 1/(1 − 4v²). ∎

**Consequences (PROVED for this model).** (i) A straight arm that Harry leaves along a line making the angle ω with it is
turned towards the perpendicular of Harry's direction of departure at the universal rate λ^{v/(1+v)}; the part of the arm at
distance r from the corner is within arctan η of radial as long as s/r ≤ ((1 − 4v²) η/(2v))^{(1+v)/v} (tip case), and by
(f) it is *not* (|tan φ| > η) for s/r large. (ii) By (g) the stretch of the left-behind arm relative to its
arclength at departure is unbounded in s/r: for a vision radius ε it reaches ≍ A (s/ε)^{v/(1+v)} at r ≍ ε. Hence no bound
on the *supremum* of the stretch of the left-behind arm can be uniform in ε, for any v > 0; only integrated (length-type)
quantities can. Indeed the length is uniformly controlled: |∂_r Q| ≤ ρ_r + λ sin β, where by (b) and (d)
λ sin β ≤ A λ^{v/(1+v)} and ρ_r ≤ [ρ sin²β/r + (1 + v)(cos ω − v)]/(1 − v²) with
ρ sin²β/r ≤ (1 + (1 − v²)λ/(cos ω − v)) min(1, A² λ^{−2/(1+v)}), which is bounded in λ. So
|∂_r Q_r(s)| ≤ c_1(v, ω) + A (s/r)^{v/(1+v)}, and ∫_0^R |∂_r Q_r(s)| dr ≤ c_1 R + A (1 + v) s^{v/(1+v)} R^{1/(1+v)} —
finite, with no dependence on a cut-off at r = ε.

---

## Claim 5 (L: local sweep lemma — Theorem D2 at a bounded scale ratio). PROVED

*Setting.* P is 1-Lipschitz on [0, τ], [a, b] ⊂ [0, 2π], S̃_θ the virtual candidates (θ ∈ [a, b]), Γ(θ) := S̃_θ(τ),
and P(τ) = Γ(a). Γ is Lipschitz and injective (§0 (a), (b)); let x(θ) := length of Γ on [a, θ] (continuous, strictly
increasing), R := x(b). Assume the **chord-arc condition** with constant A ≥ 1:

  |Γ(θ) − Γ(φ)| ≥ |x(θ) − x(φ)|/A   for all θ, φ ∈ [a, b].

From time τ on, Harry follows construction W on [a, b] (ℓ := ε/v): *walk j* (j ≥ 1, starting at τ_j', τ_1' = τ,
a_1 = a, where P(τ_j') = S̃_{a_j}(τ_j')): Γ_j(θ) := S̃_θ(τ_j') on [a_j, b], walk Γ_j by arclength for length ℓ or until b
(then *final*; stop), reaching parameter a_{j+1} at time τ_{j+1}; *connector j+1*: run straight at S̃_{a_{j+1}} until
meeting it at τ_{j+1}' (duration ≤ ε/(1 − v), as in §D2: ρ' = −1 + v min(1, ρ/ε) from ρ ≤ vℓ = ε).

*Statement.* Let Λ > 1 and

  (1 − v) J_loc := 4AΛ (1 + log⁺(R/(4Aε))) + 1.

If v J_loc ≤ log Λ, the construction stops after at most 1 + ΛR/ℓ walks, at a time ≤ τ + ΛR/(1 − v); every θ ∈ [a, b] is
seen by then; every walked front satisfies length(Γ_j on [θ, φ]) ≤ Λ |x(θ) − x(φ)|; and
J_θ(t) − J_θ(τ) ≤ J_loc for all θ ∈ [a, b] and all t up to the stopping time. With Λ = 2 it suffices that

  v ≤ (1 − v) log 2 / (8A (1 + log⁺(R/(4Aε))) + 1).

**Proof.** *Seeing* (as Lemma D2.4). On walk j let θ*(s) be the parameter with P(s) = Γ_j(θ*(s)); on connector j,
θ*(s) := a_j. On walk j, |S̃_{θ*(s)}(s) − P(s)| = |S̃_{θ*}(s) − S̃_{θ*}(τ_j')| ≤ v(s − τ_j') ≤ vℓ = ε; on a connector
ρ_{a_j} decreases from a value ≤ ε. So |P(s) − S̃_{θ*(s)}(s)| ≤ ε for all s ≥ τ, and every θ ∈ [a_j, a_{j+1}] is seen
(§0 (c)).

*Stretch relative to Γ.* Fix θ and t ≥ τ. For φ ≠ θ let D(s) := |S̃_φ(s) − S̃_θ(s)| > 0. As in Lemma D2.2(d),
D' ≤ v D/max(ε, ρ_θ − D) a.e., so D(t) ≤ D(τ) exp(v ∫_τ^t ds/max(ε, ρ_θ − D)). As φ → θ, sup_{[τ,t]} D → 0 (by §0 (a),
D(s) ≤ e^{v(s−τ)/ε} D(τ), and D(τ) → 0), and dominated convergence (integrand ≤ 1/ε) gives, with
ΔJ_θ(t) := J_θ(t) − J_θ(τ) and D(τ) ≤ |x(φ) − x(θ)| (chord ≤ arc),

  limsup_{φ→θ} |S̃_φ(t) − S̃_θ(t)|/|x(φ) − x(θ)| ≤ exp(v ΔJ_θ(t)).

By Lemma D2.3 applied in the variable x ∈ [x(a_j), R]: if ΔJ_θ(τ_j') ≤ J_loc for all θ, then
Γ_j ∘ x^{-1} is e^{vJ_loc} ≤ Λ-Lipschitz, i.e. Γ_j-length ≤ Λ · x-length on every sub-arc.

*Induction.* (B_j): ΔJ_θ(t) ≤ J_loc for all θ ∈ [a, b], t ∈ [τ, τ_j']. (B_1) is trivial. Assume (B_1), …, (B_j), walk j
non-final. Then walks i ≤ j are on fronts with Γ_i-length ≤ Λ · x-length, each has Γ_i-length ℓ, so
x(a_{i+1}) − x(a_i) ≥ ℓ/Λ and j ≤ ΛR/ℓ. Fix φ and t ∈ (τ, τ_{j+1}']. For s ∈ [τ, t], by seeing, §0 (b) (from time τ)
and chord-arc,

  ρ_φ(s) ≥ |S̃_φ(s) − S̃_{θ*(s)}(s)| − ε ≥ |Γ(φ) − Γ(θ*(s))| − ε ≥ |x(φ) − x(θ*(s))|/A − ε,

hence max(ε, ρ_φ(s)) ≥ ψ(s) := max(ε, |x(φ) − x(θ*(s))|/(2A)) (if u/A − ε < u/(2A) then u/(2A) < ε). By the layer-cake
formula, ∫_τ^t ds/max(ε, ρ_φ) ≤ ∫_ε^∞ m(y) y^{-2} dy with m(y) := |{s ∈ [τ, t] : ψ(s) < y}|. ψ(s) < y forces
x(θ*(s)) ∈ I_y := (x(φ) − 2Ay, x(φ) + 2Ay) ∩ [0, R], an interval of length |I_y| ≤ min(4Ay, R). Walking time with
x(θ*) ∈ I_y: on walk i Harry moves by arclength of Γ_i, so the time spent over an x-interval is at most Λ times its length;
total ≤ Λ |I_y|. Connectors i ≥ 2 with x(a_i) ∈ I_y: consecutive a_i differ by ≥ ℓ/Λ in x, so there are at most
1 + Λ|I_y|/ℓ of them, each of duration ≤ ε/(1−v) = vℓ/(1−v): total ≤ ε/(1−v) + Λ|I_y| v/(1−v). So
m(y) ≤ (Λ |I_y| + ε)/(1 − v). Let y_0 := R/(4A). If y_0 ≥ ε:

  (1−v) ∫_ε^∞ m y^{-2} dy ≤ ∫_ε^{y_0} (4AΛ y + ε) y^{-2} dy + ∫_{y_0}^∞ (ΛR + ε) y^{-2} dy
               = 4AΛ log(y_0/ε) + (1 − ε/y_0) + 4AΛ + ε/y_0 = 4AΛ (1 + log(R/(4Aε))) + 1;

if y_0 < ε: (1−v)∫_ε^∞ m y^{-2} dy ≤ (ΛR + ε)/ε ≤ 4AΛ + 1. In both cases ΔJ_φ(t) ≤ J_loc: (B_{j+1}).

*Termination and time.* Each non-final walk advances x by ≥ ℓ/Λ: at most ΛR/ℓ non-final walks. Total walking time
= Σ Γ_i-length of [a_i, a_{i+1}] ≤ Λ R; connectors ≤ (ΛR/ℓ) ε/(1 − v) = ΛR v/(1−v). Sum: ΛR/(1 − v).
Λ = 2: v J_loc ≤ log 2 ⇔ v (8A(1 + log⁺) + 1) ≤ (1 − v) log 2. ∎

**Corollary 5.1 (finishing move at a bounded scale ratio).** If at some time τ of any construction Harry stands at the
end Γ(a) of an arc of virtual candidates of length R ≤ Mε and chord-arc constant A, and
v ≤ (1 − v) log 2/(8A(1 + log⁺(M/(4A))) + 1), then following W on that arc he sees all of it within time 2Mε/(1 − v).
(Immediate.) The constant depends on M and A only — log M replaces the log(1/ε) of Theorem D2.

---

## Claim 6 (K: growth of the length of an arc of virtual candidates). PROVED

Let P be 1-Lipschitz, [a, b] a parameter interval, t_1 < t_2, and ℒ(t) := length of the curve θ ↦ S̃_θ(t), θ ∈ [a, b].
For s ∈ [t_1, t_2] let U(s) := {θ ∈ [a, b] : ρ_θ(s) > ε},
TVβ_out(s) := the sum over the components I of U(s) of the total variation on I of a continuous branch of
arg(S̃_θ(s) − P(s)) (in [0, ∞]), and ℒ_in(s) := the length measure of the curve at time s of the compact set [a, b] ∖ U(s).

(a) (Exact chord law.) If x := S̃_θ − P and y := S̃_φ − P satisfy |x|, |y| ≥ ε at time s, and ω ∈ [0, π] is the angle
between x and y, then (d/ds)|x − y| = v (|x| + |y|)(1 − cos ω)/|x − y| ≤ v (1 + |x − y|/(4ε)) ω.
(b) If TVβ_out(s) + ℒ_in(s)/ε ≤ κ for every s ∈ [t_1, t_2], then ℒ(t_2) − ℒ(t_1) ≤ v κ (t_2 − t_1).
(c) (Far field.) If ρ_θ(s) ≥ D ≥ ε for all θ ∈ [a, b], s ∈ [t_1, t_2], then ℒ(t_2) ≤ ℒ(t_1) e^{v(t_2 − t_1)/D}, and
TVβ_out(s) ≤ ℒ(s)/D.

**Proof.** (a) For |x|, |y| ≥ ε, F(x) = x/|x|, and (x/|x| − y/|y|)·(x − y) = |x| + |y| − (x·y)(1/|x| + 1/|y|)
= (|x| + |y|)(1 − cos ω); (d/ds)|x − y| = v (F(x) − F(y))·(x − y)/|x − y|. Next
|x − y|² = (|x| − |y|)² + 4|x||y| sin²(ω/2) ≥ 4|x||y| sin²(ω/2), so
(|x| + |y|)(1 − cos ω)/|x − y| ≤ [(|x| + |y|)/(2(|x||y|)^{1/2})] 2 sin(ω/2) ≤ c ω with
c := ½((|x|/|y|)^{1/2} + (|y|/|x|)^{1/2}) ≤ ½(1 + (1 + |x − y|/ε)^{1/2}) ≤ 1 + |x − y|/(4ε)
(max/min ≤ 1 + |x − y|/ε since min ≥ ε).
(b) Chords of any two candidates satisfy (d/ds)|x − y| ≤ v |x − y|/ε a.e. (F is ε^{-1}-Lipschitz). Let Π: a = θ_0 < … <
θ_n = b, Σ_Π(s) := Σ_i |S̃_{θ_i}(s) − S̃_{θ_{i−1}}(s)|, μ_Π := sup_{s ∈ [t_1,t_2]} max_i chord_i(s). For a.e. s,
by (a) for the indices i with [θ_{i−1}, θ_i] ⊂ U(s) (then ω ≤ the variation of the continuous argument over that
interval) and the Lipschitz bound for the others (chord ≤ length of the sub-arc),

  g_Π(s) := (1/v) (d/ds) Σ_Π(s) ≤ (1 + μ_Π/(4ε)) TVβ_out(s) + ℓ_s(N_Π(s))/ε,

where ℓ_s is the length measure at time s and N_Π(s) is the union of the partition intervals meeting K(s) := [a, b] ∖ U(s).
Also 0 ≤ g_Π(s) ≤ Σ_Π(s)/ε ≤ ℒ(t_2)/ε (ℒ is non-decreasing by §0 (b)). Take partitions Π_n with mesh → 0 and
Σ_{Π_n}(t_2) → ℒ(t_2). Then μ_{Π_n} → 0 (chords ≤ e^{vt_2/ε} · mesh), and N_{Π_n}(s) is contained in the
mesh-neighbourhood of the closed set K(s), so limsup_n ℓ_s(N_{Π_n}(s)) ≤ ℓ_s(K(s)) = ℒ_in(s). Hence
limsup_n g_{Π_n}(s) ≤ κ for a.e. s, and by the reverse Fatou lemma (domination by the constant ℒ(t_2)/ε)

  ℒ(t_2) − ℒ(t_1) ≤ lim_n [Σ_{Π_n}(t_2) − Σ_{Π_n}(t_1)] = lim_n v ∫_{t_1}^{t_2} g_{Π_n} ≤ v κ (t_2 − t_1),

using Σ_{Π_n}(t_1) ≤ ℒ(t_1).
(c) |F(x) − F(y)| ≤ |x − y|/max(ε, min(|x|, |y|)) ≤ |x − y|/D gives (d/ds) chord ≤ v chord/D for every chord, hence for
every Σ_Π and for ℒ. The argument of a curve at distance ≥ D from P has variation ≤ length/D. ∎

---

## Claim 7 (C: construction W_cut and the conditional reduction). PROVED (as an implication)

**Construction W_cut** (v ≤ 1/4, ε ≤ 1/20). *Phase 1:* P(s) = s on [0, t_0]. Let α_s be as in Claim 1(e), b := 2π − α_s.
*Connector 1:* from P(t_0) run straight at S̃_{α_s} until meeting it, at time τ_1' ≤ t_0 + ρ_s/(1 − v) ≤ t_0 + 1.4ε/(1−v)
(the straight-line ansatz of §D2: the distance obeys ρ' = −1 + v min(1, ρ/ε) ≤ −(1 − v)). *Then* construction W on the arc
[α_s, b] exactly as in Claim 5 (a_1 := α_s; walks of length ℓ = ε/v on the frozen virtual front, connectors), until the
final walk reaches b. The path is 1-Lipschitz and depends only on (v, ε).
For s ≥ t_0 let θ*(s) be Harry's current parameter (α_s on connector 1), and κ(s) := TVβ_out(s) + ℒ_in(s)/ε of Claim 6
for the *remaining arc* [θ*(s), b].

(a) (Unconditional.) Every direction passed by a walk is seen; every α with |α| ≤ α_s is seen by t_0. So W_cut sees every
direction as soon as it stops. At t_0: κ(t_0) < π − 2 arcsin v, and the remaining front has length ≤ 2π/(1 − v).
(b) (Conditional.) **Hypothesis (K_κ):** κ(s) ≤ κ for every s from t_0 until the construction stops (or forever, if it
does not), where κ is a constant with vκ < 1 − v. Then W_cut stops, and every direction is seen by

  T ≤ t_0 + 1.4ε/(1 − v) + [2π/(1 − v) + 1.4 vκε/(1 − v)]/(1 − v − vκ).

More generally the same conclusion holds if, instead of (K_κ), the lengths satisfy
ℒ(t_2; c) − ℒ(t_1; c) ≤ vκ (t_2 − t_1) for the arcs [c, b] with c = a_{j+1}, [t_1, t_2] = [τ_j', τ_{j+1}'] (j ≥ 1) and
c = α_s, [t_1, t_2] = [t_0, τ_1'] (this is what Claim 6(b) delivers from (K_κ)).

**Proof.** (a) Claim 1(e) and the seeing paragraph of Claim 5 (which uses only S̃ and the construction). On [α_s, b],
S̃ = S on [0, t_0] (Claim 1(e)), so by Claim 1(g) there is no point of the arc within ε of P(t_0) and the bearing has
total variation < π − 2 arcsin v. Length at t_0: the true front has length ≤ 2π + 2πv t_0 = 2π/(1 − v)
(paper, Prop. `prop:length`(2)).
(b) Let L_j := ℒ(τ_j'; a_j) be the length of the remaining front at the start of walk j. Walk j (non-final) covers
length ℓ of Γ_j, so ℒ(τ_j'; a_{j+1}) = L_j − ℓ. The arc [a_{j+1}, b] is contained in the remaining arc [θ*(s), b] for
s ∈ [τ_j', τ_{j+1}'], and TVβ_out and ℒ_in are monotone under passing to a sub-arc, so Claim 6(b) and (K_κ) give
L_{j+1} = ℒ(τ_{j+1}'; a_{j+1}) ≤ L_j − ℓ + vκ (ℓ + ε/(1 − v)) = L_j − ηℓ, η := 1 − vκ/(1 − v) > 0 (ε = vℓ).
Hence the number n of non-final walks is ≤ L_1/(ηℓ) and the construction stops. The final walk has length
L_{n+1} ≤ L_1 − nηℓ, so the total walked length is ≤ nℓ + L_1 − nηℓ ≤ L_1 + (1 − η)L_1/η = L_1/η, and connectors
2, …, n+1 take ≤ n vℓ/(1 − v) ≤ L_1 v/(η(1 − v)). Total after τ_1': ≤ L_1/(η(1 − v)) = L_1/(1 − v − vκ). Finally
L_1 ≤ ℒ(t_0; α_s) + vκ(τ_1' − t_0) ≤ 2π/(1 − v) + 1.4 vκε/(1 − v) by Claim 6(b) on [t_0, τ_1'] and (a). ∎

**Corollary 7.1 (splitting into bulk and left arm; far field automatic).** Fix θ_0 ∈ (0, π) and split the remaining arc
at b − θ_0 into its bulk part and its left-arm part 𝒜(s) := [max(θ*(s), b − θ_0), b]. Then κ(s) ≤ κ_B(s) + κ_E(s)
(the quantities of Claim 6 for the two parts; TV and length are sub-additive under cutting an arc). So (K_κ) follows from
(B): κ_B(s) ≤ κ_B and (E): κ_E(s) ≤ κ_E for all s, with κ = κ_B + κ_E. Moreover, on any time interval [t_1, t_2] on which
the whole left arm stays at distance ≥ D ≥ ε from Harry, κ_E(s) ≤ ℒ_𝒜(t_1) e^{v(t_2 − t_1)/D}/D (Claim 6(c)): (E) can
only fail while Harry is near the left arm, i.e. just after t_0 and in the endgame.

---

# Round 6b — the left arm during the sweep, for construction C of P6a

Claims 8–12 concern construction C of `referee/P6a-claims.md` (C¹ field F(x) = f(|x|)x/|x|, virtual candidates x_θ,
legs with step ε, base labels a_j, leg starts t_j, t_0 = end of leg 0, O := P(t_0) = x_0(t_0)). They **use** the
following statements of P6a (not refereed at the time of writing): Lemma V (0 ≤ A ≤ a*(ρ)I, a* = 1/ρ for ρ ≥ ε,
= 2/ε inside), Lemma VC (chords and |∂_θx| non-decreasing; ρ_θ(t) ≤ ε ⇒ θ seen), Lemma 1(i),(ii)
(w_t/w = v T·AT ≤ v a*(ρ); ψ_t = −(v/ρ) sin φ cos φ for ρ ≥ ε), Lemma 2(i) (l_t = v∫T·AT ds), Lemma 3(c),(d) with the
Gronwall consequence, Lemma 4(b), Lemma C(2),(4) (x_{a_j}, P, x_{a_{j+1}} collinear in this order during leg j+1;
|P(t) − x_{a_j}(t)| ≤ ε₁ = e^{2μ}ε; legs last ≤ ε/(1−v)), and Lemma A3.4 of the paper. Everything else is proved here.

**Standing assumptions:** v ≤ 1/100, ε ≤ 10⁻³, θ_0 := 0.1. Then μ = v/(1−v), ε₁ ≤ 1.03ε, g_max ≤ 1.0001.
**Construction C_cut:** construction C with the final label 2π replaced by b_e := 2π − α_s (α_s of Claim 1(e)); i.e. the
front is the arc [0, b_e] and the construction stops when a_{j+1} = b_e. (Lemma C and Theorem R of P6a hold verbatim with
2π replaced by b_e, because their proofs use the label 2π only as the end of the arc; and the labels in (b_e, 2π] are seen
by t_0, see G0.) **Label sets:** R := [0, 2θ_0] (right arm), B := [2θ_0, 2π − 2θ_0], 𝒜 := [2π − θ_0, b_e] (left arm).
r_a := |x_a(t_0) − O|. K_arm(t) := ∫_𝒜 T·AT ds (at time t).

## Lemma G (geometry of the front of C at t_0). PROVED

G0. t_0 = 1/(1−v) − εs_0 with 0 ≤ s_0 ≤ v/(1−v) ≤ 0.0102. Every α with |α| ≤ α_s is seen by t_0, and for
    0 ≤ α < α_s: r_α ≤ 2.03ε. For α ∈ [α_s, 2π − α_s], x_α = S_α on [0, t_0] and r_α ≥ ε.
G1. For a ∈ R, b ∈ 𝒜: |x_a(t_0) − x_b(t_0)| ≥ 0.9(r_a + r_b) − 4ε.
G2. For a ∈ B, b ∈ 𝒜: |x_a(t_0) − x_b(t_0)| ≥ 0.067; and r_b ≤ 0.104 for b ∈ 𝒜, r_a ≤ 0.206 for a ∈ R.
G3. On 𝒜 (and on the outer part [α_s, 2θ_0] of R) r is strictly monotone in the label; the angle φ_0 between the
    tangent at t_0 and the direction from O satisfies tan φ_0 ≤ 0.52 r + 0.011 ε/r ≤ 0.064 on 𝒜; hence the t_0-length of
    the part of 𝒜 with radii in [r_1, r_2] is ≤ 1.0021 (r_2 − r_1).

*Proof.* G0. Phase 0 ends at t_ε = (1−ε)/(1−v) and leg 0 (ρ_t = −1 + v f(ρ) from ε to 0) lasts between ε and ε/(1−v), so
t_0 − 1/(1−v) ∈ [−εv/(1−v), 0]. For α ∈ [α_s, π], ρ ≥ ε on [0, 1/(1−v)] ⊃ [0, t_0] (Claim 1(e)); so the true candidate
solves the virtual equation. Let 0 < α < α_s and suppose the true ρ ≥ ε on [0, t_0]. With η := (1 − v²)εs_0 ≤ v(1+v)ε,
h(t_0) = η − (1 − cos α) (as in Claim 1(a), h decreases at rate 1−v²). If the bearing reached arccos v at a time ≤ t_0,
then ρ = g(α)/g_max < ε there; otherwise cos β(t_0) > v, so h(t_0) = ρ(cos β + v) > 2vρ ≥ 2vε > η: contradiction either
way. So there is a first time t_e ≤ t_0 with ρ = ε, the candidate is seen (Lemma VC), and since a true candidate has
ρ_t ≥ −(1−v), t_e ≥ t_ε. Then r_α ≤ ε + (1 + v)(t_0 − t_ε) ≤ ε + (1+v)ε/(1−v) ≤ 2.03ε (relative speed ≤ 1 + v).
Formulas at t_0 for α ∈ [α_s, π) (polar coordinates about O): ρ(cos β + v) = η − (1 − cos α), ρ g(β) = g(α).
Differentiating as in Claim 1(b): ρβ_α = sin β [(1+v)(1 − cos α) + η(cos α − v)]/((1−v²) sin α) and
ρ_α = ρ(cos α − v)/sin α − ρβ_α (cos β − v)/sin β. As η/ρ ≤ v(1+v), cos β ≤ −v + v + v² ≤ v, so for cos α > v:
ρ_α ≥ ρ(cos α − v)/sin α > 0 and

  tan φ_0 = ρβ_α/ρ_α ≤ (1 − cos α)/((1−v)(cos α − v)ρ) + εs_0/ρ.                                   (G*)

Bearings for α ≤ 0.2: |cos β + v| ≤ η/ρ + (1 − cos α)/ρ ≤ 0.0101 + g_max tan^{1+v}(α/2) ≤ 0.1105 (ρ ≥ ε,
ρ ≥ g(α)/g_max, 2 sin²(α/2)/g(α) = tan^{1+v}(α/2), tan 0.1 < 0.1004), so |cos β| ≤ 0.1205 and |β − π/2| ≤ 0.121,
cos 0.121 > 0.9926.
G1. If α_a ≥ α_s: Im(x_a − O) ≥ 0.9926 r_a, and by reflection Im(x_b − O) ≤ −0.9926 r_b; so the distance is
≥ 0.99(r_a + r_b). If α_a < α_s: distance ≥ r_b − r_a ≥ 0.9(r_a + r_b) − 1.9 r_a ≥ 0.9(r_a + r_b) − 4ε.
G3. Monotonicity: ρ_α > 0. In (G*): tan^{1−v}(α/2) = g(α)/(1 + cos α) = ρg(β)/(1 + cos α) ≤ 1.0001 r/1.995, so
tan(α/2) ≤ 0.5014 r (the base is < 1 and the exponent 1/(1−v) ≥ 1), (1 − cos α)/ρ ≤ g_max tan^{1+v}(α/2) ≤ 0.5015 r,
(1−v)(cos α − v) ≥ 0.99 · 0.985; εs_0 ≤ 0.0102ε. Length: ds = (1 + tan²φ_0)^{1/2} dr.
G2. g(β) ≥ (1 − 0.1205²)^{1/2} (0.879/1.121)^{0.005} ≥ 0.991 for |cos β| ≤ 0.1205; g(0.1) ≤ sin 0.1/0.05^{0.01} ≤ 0.1029,
so r ≤ 0.104 on 𝒜; g(0.2) ≤ sin 0.2/0.1^{0.01} ≤ 0.2034, so r ≤ 0.206 on R. For a ∈ B with α_a ∈ [0.2, arccos v] (or its
mirror image): r_a ≥ ρ(0.2) ≥ ρ(0.1) + ∫_{0.1}^{0.2} ρ(cos α − v)/sin α dα ≥ ρ(0.1) + (0.0998/1.0001)(0.970)(log 2)
≥ ρ(0.1) + 0.067 (ρ ≥ g(α)/g_max ≥ sin 0.1/g_max on [0.1, 0.2], 1/sin α ≥ 1/α); for α_a ∈ [arccos v, 2π − arccos v],
r_a ≥ 1 (Claim 1(e)). As r_b ≤ ρ(0.1) for b ∈ 𝒜, |x_a − x_b| ≥ r_a − r_b ≥ 0.067. ∎

## Claim 8 ((T) while the base is not on the left arm). PROVED, conditional on the no-dawdling hypothesis (A1)

**Hypothesis (A1)** (constant C_A ≥ 1 with vC_A ≤ 1/100): for every leg start t_j of C_cut with a_j ∈ R:
t_j − t_0 ≤ C_A (r_{a_j} + ε).

*Statement.* Under (A1), for every t ≥ t_0 in a leg j+1 with a_j ≤ 2π − 2θ_0:

  K_arm(t) ≤ max( 50 + 5.3 C_A², 2.4 e^{16 v (t − t_0)} ).

Moreover, for b ∈ 𝒜 with r_b ≥ 16ε the stretch w_b(t)/w_b(t_0) is ≤ 1.035 (1 + D/r_b)^κ while a_j ∈ R, where
D := r_{a_j} and κ := 2.23 vC_A ≤ 0.0223; and the length of 𝒜 is ≤ 0.15 e^{16v(t − t_0)} while a_j ∈ B.

*Proof.* Let t be in leg j+1 and b ∈ 𝒜, r := r_b. By Lemma C(4), Lemma VC and Lemma G,

  ρ_b(t) ≥ |x_b(t) − x_{a_j}(t)| − ε₁ ≥ |x_b(t_0) − x_{a_j}(t_0)| − ε₁ ≥ 0.9(D + r) − 5.03ε (a_j ∈ R);  ≥ 0.065 (a_j ∈ B).

Hence, for a_j ∈ R: ρ_b ≥ 0.45(D + r) if r ≥ 16ε, and ρ_b ≥ 0.45 D if D ≥ 16ε.
*Time.* For s in a leg i+1 put D(s) := r_{a_i}. By (A1) and the leg duration, s − t_0 ≤ C_A(D(s) + 3ε), and for every y
the set {s : D(s) < y} is contained in [t_0, t_0 + C_A(y + 3ε)]. On the outer part of R, D is non-decreasing in s
(Lemma G3), and D ≤ 2.03ε before; so Y := sup_{s ≤ t} D(s) ≤ max(D(t), 2.03ε).
*Stretch of a point with r ≥ 16ε (a_j ∈ R).* By the layer-cake formula 1/(r + D) = ∫_D^∞ dy/(r + y)²,

  ∫_{t_0}^t ds/(r + D(s)) ≤ C_A [ ∫_0^Y (y + 3ε) dy/(r + y)² + (Y + 3ε)/(r + Y) ] ≤ C_A [ log(1 + Y/r) + 1.4 ]
               ≤ C_A [ log(1 + D/r) + 1.53 ],

so ∫ a*(ρ_b) ≤ 2.23 C_A log(1 + D/r) + 3.4 C_A and w_b(t)/w_b(t_0) ≤ exp(v∫a*) ≤ 1.035 (1 + D/r)^κ.
*Core (r < 16ε; t_0-length ≤ 16.04ε by G3).* If D(t) < 16ε: t − t_0 ≤ 19 C_A ε, the stretch is ≤ e^{(2v/ε)·19C_Aε} ≤ e^{0.38},
and the contribution to K_arm is ≤ (2/ε)(16.04ε)(1.47) ≤ 47. If D(t) ≥ 16ε: the times with D(s) < 16ε have measure
≤ 19C_Aε and afterwards ρ ≥ 0.45 D(s), so ∫a* ≤ 38 C_A + 2.23 C_A [log(D/16ε) + 1.4], the stretch is ≤ 1.51 (D/16ε)^κ, and
the contribution is ≤ 16.04ε · 1.51 (D/16ε)^κ/(0.45 D) ≤ 3.4.
*Inner part (16ε ≤ r ≤ D).* T·AT ≤ 1/ρ ≤ 1/(0.45 D); length ≤ ∫ 1.0021 · 1.035 (2D/r)^κ dr ≤ 1.038 · 2^κ D/(1 − κ);
contribution ≤ 1.038 · 1.016 · 1.023/0.45 ≤ 2.4.
*Outer part (r > D1 := max(D, 16ε)).* Here ρ ≥ 0.45 r ≥ ε and T·AT = sin²φ/ρ. Let T_0, ê_0 be the tangent and the unit
vector from O at t_0, ê the unit vector from P(t), τ := t − t_0. Then
|sin φ| ≤ |sin∠(T, T_0)| + |sin φ_0| + |sin∠(ê, ê_0)|, with: |sin φ_0| ≤ 0.52 r + 0.011ε/r (G3);
∠(T, T_0) ≤ ∫ v/(2ρ) ≤ vτ/(0.9 r) (Lemma 1(ii) of P6a); |sin∠(ê, ê_0)| ≤ |(x_b(t) − P(t)) − (x_b(t_0) − O)|/r ≤
(1 + v)τ/r (candidate speed ≤ v, Harry speed ≤ 1). So |sin φ| ≤ 0.52 r + 0.011ε/r + 1.03 τ/r, and with stretch
≤ 1.035 · 2^κ ≤ 1.052, τ ≤ C_A(D + 3ε) ≤ 1.19 C_A D1, r ≤ 0.104:

  contribution ≤ (3 · 1.052 · 1.0021/0.45) ∫_{D1}^{0.104} [0.2704 r + 0.000121 ε²/r³ + 1.061 τ²/r³] dr ≤ 0.011 + 5.27 C_A².

Sum for a_j ∈ R: ≤ 47 + 2.4 + 0.011 + 5.27C_A² ≤ 50 + 5.3 C_A².
*a_j ∈ B.* ρ ≥ 0.065 ≥ 1/16 on 𝒜, so K_arm ≤ 16 ℓ(t), ℓ := length of 𝒜, and ℓ_t = vK_arm ≤ 16vℓ (Lemma 2(i)). At the
last time with base in R (D ≤ 0.206): core ≤ 16.04ε · 1.51 (0.206/16ε)^κ ≤ 0.03; rest ≤ ∫_0^{0.104} 1.038 (0.31/r)^κ dr
≤ 0.12. So ℓ(t) ≤ 0.15 e^{16v(t − t_0)} and K_arm ≤ 2.4 e^{16v(t − t_0)}. ∎

*Remarks.* (1) No flatness of the arm is used: the part inside radius D is at distance ≳ D and has length ≲ D
(power-law stretch with exponent κ < 1), the part outside is radially aligned up to O(τ/r) simply because Harry has moved
only τ ≲ D. (2) K_arm ≥ K_tip of Theorem R/Corollary M with b* = 2π − θ_0 (δ = θ_0) as long as a_{j+1} ≤ b*; so Claim 8
is hypothesis (T) of Corollary M, verbatim except for the end label (b_e instead of 2π), for all legs with
a_j ≤ 2π − 2δ. It says nothing once the base is beyond 2π − 2δ.

## Claim 9 (what replaces (F_b) on the arm: flatness relative to the remaining length). PROVED (implication)

Let t be in leg j+1 of C (or C_cut), b_end the final label, L := l_t(a_j, b_end), and suppose
**(F_a):** E(a_j, s; t) ≤ c_0 l (l/L)^{2γ} + c_1 ε for every s ∈ (a_{j+1}, b_end], l := l_t(a_j, s), with γ ∈ (0, 1],
c_0 + c_1 ≤ 1/4. Then K̃(t) := ∫_{a_{j+1}}^{b_end} T·AT ds ≤ 16e^{2μ} + 4c_0(1 + 1/γ) + 2c_1.

*Proof.* As in Theorem R of P6a with r_0 := L (no far part). l ≤ 8ε₁: measure ≤ 8ε₁, T·AT ≤ 2/ε: ≤ 16e^{2μ}. For
l > 8ε₁: Φ(l) := c_0 l(l/L)^{2γ} + c_1ε ≤ l/4, so c(a_j, s) ≥ 3l/4 and ρ_s ≥ 3l/4 − ε₁ ≥ l/2 > ε; Lemma 3(d) and
Lemma 4(b) of P6a (P on the chord [x_{a_j}, x_{a_{j+1}}]) give a contribution
≤ 2[Φ(L)/(L/2) + ∫_{8ε₁}^{L} 4Φ(l) l^{-2} dl] ≤ 2[2c_0 + c_1/4 + 2c_0/γ + c_1/2]. ∎

## Claim 10 (regularity of the arm is preserved up to a power-law loss). PROVED given Lemma 3(c) of P6a; conditional on (A1)

Let a < b be labels of 𝒜 with radii ≥ r ≥ 16ε and t_0-length λ ≤ r/12, N := (2E(a,b))^{1/2}. While the base is in R:

  N(t) ≤ 1.06 (1 + D/r)^{3.79 vC_A} [ N(t_0) + 48 vC_A λ^{3/2} r^{−1−1.5κ} ].

*Proof.* l_t(a,b) ≤ 1.035 λ (1 + D/r)^κ ≤ 0.0863 (r + D) (Claim 8). The convex hull of the arc lies within l of x_a, so
ρ_m ≥ 0.45(r + D) − l ≥ 0.3637 (r + D) ≥ max(ε, 4l). Lemma 3(c) (Gronwall form) with |p_a| ≤ ρ_a ≤ 1.25 ρ_m:
N(t) ≤ exp(1.375 v∫ds/ρ_m)[N(t_0) + 2.5 v∫ l^{3/2} ρ_m^{-2} ds]. By the layer-cake bounds of Claim 8,
∫ds/ρ_m ≤ 2.75 C_A[log(1 + D/r) + 1.53], and ∫ ds/(r + D(s))² ≤ C_A[∫_0^Y 2(y + 3ε)dy/(r + y)³ + (Y + 3ε)/(r + Y)²] ≤
2.4 C_A/r; l^{3/2} ≤ 1.053 λ^{3/2} r^{−1.5κ} (as r + D < 1), ρ_m^{-2} ≤ 7.56 (r + D)^{-2}. ∎

(While the base is in B the same lemma gives N(t) ≤ e^{26v(t−t1)}[N(t1) + 1450 v(t − t1)λ^{3/2}] as long as
16v(t − t_0) ≤ 0.18: there ρ_m ≥ 0.0535 ≥ 4l.) *Reading:* far-field evolution keeps the class
"E(a,b) ≲ (v²/r²)λ³ for pairs at radius r", but the proved constant degrades like r^{−7.6vC_A}; this is the crude
amplification rate v/ρ, not the true one.

## Claim 11 (hull-perimeter endgame for construction C). PROVED (implication; the cone hypothesis is not proved)

For t in leg j+1 of C (or C_cut, final label b_end) let X(t) := {x_s(t) : s ∈ [a_{j+1}, b_end]},
Π(t) := perimeter of conv({P(t)} ∪ X(t)), G(γ) := −(1 + cos γ) + v(π + γ).

(a) If Π(t) ≤ 2ε, every label in [a_{j+1}, b_end] is seen by t. Π(t) ≤ 2(ε + l_t(a_{j+1}, b_end)).
(b) Let t1 < t2 and γ ∈ [0, π). If for every s ∈ [t1, t2] the set X(s) lies in a closed sector with apex P(s), opening
    ≤ γ, containing the current heading, then Π(t2) ≤ Π(t1) + G(γ)(t2 − t1).
(c) (Cone criterion.) If at time s (in leg i+1) all unit tangents of the arc [a_i, b_end] lie in a closed convex cone Q of
    opening ≤ γ < π, the hypothesis of (b) holds at s.
(d) Hence: if the cone condition (c) holds from a leg start t_{j_1} on, with c_γ := −G(γ) > 0, then every direction with
    label ≥ a_{j_1} is seen by t_{j_1} + 2(ε + R_{j_1})/c_γ, R_{j_1} the remaining length at t_{j_1}. No flatness, no (T).

*Proof.* (a) Two points of a compact convex set of perimeter Π are at distance ≤ Π/2; so ρ_s ≤ ε for all remaining s:
Lemma VC(c). The hull lies in the hull of the curve "segment from P to x_{a_{j+1}}, then the arc", whose length is
≤ ε + l_t (Lemma C(2): the distance from P to x_{a_{j+1}} is ≤ ε at t_j and decreases during the leg), and the perimeter
of the hull of a curve is ≤ twice its length.
(b) Inside one leg: for a finite F ⊂ [a_{j+1}, b_end] containing a_{j+1}, the points x_s, s ∈ F, are C¹ with velocities
v f(ρ_s) r̂_s (radial from P, speed ≤ v), and P moves with unit velocity u towards x_{a_{j+1}}, a point of F (Lemma C(2)).
The proof of Lemma A3.4 (Cauchy formula, Danskin) gives for the perimeter Π_F of conv({P} ∪ F-points): the derivative is
≤ Σ_V 2 sin(ε_V/2)⟨V_t, n_V⟩ with exterior angles ε_V summing to 2π; a candidate vertex contributes ≤ v ε_V; P is a
vertex (the F-points lie in a sector of opening < π at P), its interior angle is the opening B_F ≤ γ of the smallest
sector at P containing the F-points, u lies in that sector, and P contributes ≤ −(1 + cos B_F). So the derivative is
≤ G(B_F) ≤ G(γ) (G increasing). Sup over F gives Π. At a leg switch the set X shrinks and P is continuous, so Π does not
increase.
(c) x_{a_{i+1}} − x_{a_i} = ∫T ds ∈ Q, and by Lemma C(2) the heading u is its direction; for s ≥ a_{i+1},
x_s − P = (x_s − x_{a_{i+1}}) + ρu ∈ Q. So X ⊂ P + Q.
(d) (a), (b), (c): Π(t_{j_1}) ≤ 2(ε + R_{j_1}) and Π decreases at rate c_γ until it is ≤ 2ε. ∎

## Claim 12 (tangent trapping). PROVED

For a virtual candidate with ρ > 0 on [t1, t2], let ψ be a continuous tangent angle, β a continuous bearing from
Harry, φ := β − ψ. Then ψ_t = −v m(ρ) sin φ cos φ with m = 1/ρ (ρ ≥ ε), m = ρ/ε² (ρ < ε) (Lemma 1(ii), V(ii),(iii) of P6a:
T_t = v(AT − (T·AT)T) and e^⊥·Ae = sin χ cos χ (f/ρ − f_ρ)). Consequently, if β(t) ∈ [β_−, β_+] on [t1, t2] with
β_+ − β_− < π/2 and ψ(t1) ∈ [β_+ − π/2, β_−], then ψ(t) ∈ [β_− − π/2, ψ(t1)] on [t1, t2] (and symmetrically,
ψ(t1) ∈ [β_+, β_− + π/2] ⇒ ψ(t) ∈ [ψ(t1), β_+ + π/2]).

*Proof.* Upper barrier: if ψ = ψ(t1) at some time then φ = β − ψ ∈ [β_− − ψ(t1), β_+ − ψ(t1)] ⊂ [0, π/2], so ψ_t ≤ 0.
Lower barrier: if ψ = β_− − π/2 then φ = β − β_− + π/2 ∈ [π/2, π), so sin φ cos φ ≤ 0 and ψ_t ≥ 0. ∎

(The tangent is attracted to the perpendicular of the direction to Harry and never crosses it. Applied to the arm it
bounds the tangent span by π/2 + (spread of the directions to Harry) *provided all points of the arm lie on the same
side*, i.e. sin φ has one sign along the arm; that sign statement is not proved.)
