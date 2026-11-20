# P6a — claims for independent referees (PROVED statements only)

**Version 3 (round 6c).** Changes against version 2 (the text first sent to the referees): all fixes F1–F10 of
`reports/referee-RP6a-2.md` applied (Lemma C(0) no accumulation; Theorem B restricted to legs with u_{a_{j+1}} ≤ U;
Step 4 case a = a_j, b < a_{j+1}; ρ_m ≥ 8λ; (IC1) only for λ ≥ ε/2; roundings 42.11, 1.0034·10⁸; Corollary M wording;
numerical sentence corrected), and a new Remark (4) after Theorem B (relaxed start condition). No statement was
strengthened.

Stream P6a, round 6 / 6b. Formulation unchanged: Harry has speed ≤ 1, H(0) = 0, path fixed in advance (it may depend on
v, ε, not on α); Snitch S' = v(S − H)/|S − H|, S(0) = d e^{iα}; vision radius ε ∈ (0, d); win = every α is within ε at
some time. Normalise d = 1. μ := v/(1 − v). Plane = ℝ² = ℂ; a × b := a₁b₂ − a₂b₁; J = rotation by +90°; e^⊥ := Je.

Everything below is claimed PROVED: Lemmas V, VC, 1–4, C; Theorem R (reduction: flatness of the bulk seen from the
base + separation + tip bound ⇒ ε-independent sweep time); **Theorem B (bulk): flatness and separation propagate from
a start condition (ST) for all v ≤ 10⁻¹²-type absolute bounds**; Corollary M (conditional main statement).
**The absolute-v₀ goal is NOT proved**: Corollary M still assumes the start condition (ST) at some leg and the tip bound
(T); both are only checked numerically (reports/P6a-1.md, Round 6b). Constants are deliberately wasteful.
External inputs: Proposition "Topology, length, area"(2) of paper/main.tex (front length L(t) ≤ 2π + 2πvt for
t < 1/(1 − v), true dynamics, Harry running straight from the centre), Lemma A4.1 of the paper (only in Corollary M),
and standard ODE theory (C¹ dependence on initial data for a C¹ field with bounded derivative).

---------------------------------------------------------------------------------------------------------------------

## 1. The field and the virtual candidates

f(ρ) := 1 for ρ ≥ ε, f(ρ) := (ρ/ε)(2 − ρ/ε) for 0 ≤ ρ ≤ ε;  F(x) := f(|x|) x/|x| (F(0) := 0);  A(x) := DF(x).
a*(ρ) := 1/ρ for ρ ≥ ε, a*(ρ) := 2/ε for ρ < ε.   (This is a C¹ variant of the field x/max(|x|, ε) of Theorem D2.)

**Lemma V (field).**
(i) F ∈ C¹(ℝ²), |F| ≤ 1, F(x) = x/|x| for |x| ≥ ε.
(ii) With ρ = |x|, r̂ = x/ρ, Π := I − r̂r̂ᵀ: A = f'(ρ) r̂r̂ᵀ + (f(ρ)/ρ) Π; A is symmetric and 0 ≤ A ≤ a*(ρ) I;
     for ρ ≥ ε, A = Π/ρ.
(iii) For every unit vector e: |e^⊥ · A(x) e| ≤ |x × e| / max(ρ, ε)².
(iv) (F(x) − F(y)) · (x − y) ≥ 0.

*Proof.* F(x) = g(|x|)x with g(ρ) = (2ε − ρ)/ε² on [0, ε] and g = 1/ρ on [ε, ∞). g is continuous, and g' = −1/ε²
resp. −1/ρ² agree at ρ = ε, so g ∈ C¹(0, ∞); near 0, F(x) = (2εx − |x|x)/ε² and x ↦ |x|x is C¹. Hence (i)
(|F| = f ≤ 1). DF = g I + ρg' r̂r̂ᵀ = (f/ρ)Π + (g + ρg') r̂r̂ᵀ and g + ρg' = f'. Inside the disc
f' = (2/ε)(1 − ρ/ε) ∈ [0, 2/ε], f/ρ = (2 − ρ/ε)/ε ∈ [1/ε, 2/ε]; outside f' = 0, f/ρ = 1/ρ. This is (ii).
(iii): write e = cos χ r̂ + sin χ n, n := Jr̂; then e^⊥ = −sin χ r̂ + cos χ n and
e^⊥·Ae = sin χ cos χ (f/ρ − f'), where f/ρ − f' = ρ/ε² (ρ < ε), = 1/ρ (ρ ≥ ε), i.e. = ρ/max(ρ, ε)²; and
|sin χ| = |x × e|/ρ. (iv): (F(x) − F(y))·(x − y) = ∫₀¹ (x − y)·A(y + τ(x − y))(x − y) dτ ≥ 0. ∎

Let P be a 1-Lipschitz path. **Virtual candidates:** x_θ' = v F(x_θ − P(t)), x_θ(0) = e^{iθ}. r_θ := x_θ − P,
ρ_θ := |r_θ|.

**Lemma VC.** (a) x_θ exists uniquely on [0, ∞), |x_θ'| ≤ v; θ ↦ x_θ(t) is C¹, ∂_t ∂_θx = vA(r)∂_θx, and
|∂_θx(θ, t)| is non-decreasing in t, ≥ 1. (b) |x_θ(t) − x_φ(t)| is non-decreasing in t. (c) If ρ_θ(t) ≤ ε for some
t, the true candidate θ is seen by time t.

*Proof.* (a) vF(· − P(t)) is continuous in t, C¹ in x with ‖DF‖ ≤ 2/ε: global existence, uniqueness, C¹ dependence on
the initial point, and the variational equation. ∂_t|∂_θx|² = 2v ∂_θx·A∂_θx ≥ 0 and |∂_θ e^{iθ}| = 1.
(b) d/dt |x_θ − x_φ|² = 2v(F(r_θ) − F(r_φ))·(r_θ − r_φ) ≥ 0. (c) Let t₁ := inf{s : ρ_θ(s) ≤ ε} ≤ t. On [0, t₁],
ρ_θ ≥ ε, where F is the unit field, so x_θ solves the true equation there (right side locally Lipschitz off P); by
uniqueness it is the true candidate on [0, t₁], and its distance to Harry at t₁ is ≤ ε. ∎

**Notation for the front.** Fix t. The front θ ↦ x_θ(t) is a regular C¹ curve (Lemma VC(a)); ds = |∂_θx|dθ;
T := unit tangent; for labels a < b:
  l(a,b) := ∫_a^b ds (length),  c(a,b) := |x_b − x_a| > 0 (by VC(b)),  e = e_{ab} := (x_b − x_a)/c,
  E(a,b) := l − c ≥ 0 (**two-point excess**),  N(a,b) := (2E)^{1/2}.
At a point of the front: ρ, r̂; cos φ := T·r̂, sin φ := T × r̂ (φ = angle from T to r̂).

## 2. Evolution identities

**Lemma 1 (pointwise laws).** Let w := |∂_θx|.
(i) w_t = v w T·AT; for ρ > ε this is w_t/w = v sin²φ/ρ.
(ii) T_t = v(AT − (T·AT)T); for ρ > ε the tangent angle ψ (T = e^{iψ}) obeys ψ_t = −(v/ρ) sin φ cos φ.
(iii) Let θ₀, t₀ be such that ρ > ε on a neighbourhood and x(·, t) is C² there (true whenever the points of a
neighbourhood of θ₀ have stayed in {ρ > ε} since time 0, the field being C^∞ in x there). With κ := ∂_sψ:
   ∂_sρ = cos φ,  ∂_sφ = −κ − sin φ/ρ,
   **κ_t = (v/ρ)(1 − 3 sin²φ) κ + (v/ρ²) sin φ (3 cos²φ − 1).**
(iv) If moreover P(t) lies on the front, at arclength 0, and the arc [0, s] is C² with ρ > 0 on (0, s], then
ρ sin φ (s) = −∫₀^s κ ρ cos φ du, hence
   κ_t(s) = (v/ρ) [ (1 − 3 sin²φ) κ(s) − (3 cos²φ − 1) ρ^{-2} ∫₀^s κ ρ cos φ du ].
(So to leading order in φ: κ_t = (v/ρ)(κ(s) − weighted mean of κ on [0, s]); constant κ is neutral.)

*Proof.* (i), (ii): ∂_t∂_θx = vA∂_θx (Lemma VC), ∂_θx = wT; so w_t = vw T·AT and T_t = v(AT − (T·AT)T). For ρ > ε,
A = Π/ρ, T = cos φ r̂ − sin φ n (n = Jr̂), ΠT = −sin φ n, T·AT = sin²φ/ρ, and
AT − (T·AT)T = −(1/ρ)[sin φ n + sin²φ T] = −(1/ρ)[sin φ cos²φ n + sin²φ cos φ r̂] = −(sin φ cos φ/ρ) JT,
because JT = cos φ n + sin φ r̂ (Jr̂ = n, Jn = −r̂). So T_t = −(v sin φ cos φ/ρ) JT, i.e. ψ_t = −(v/ρ) sin φ cos φ.
(iii) ∂_sρ = T·r̂ = cos φ. ∂_s r̂ = ΠT/ρ = −(sin φ/ρ) n, so the direction angle β of r̂ has ∂_sβ = −sin φ/ρ, and
φ = β − ψ gives ∂_sφ = −sin φ/ρ − κ. Since κ = ∂_θψ/w: κ_t = ∂_s(ψ_t) − κ w_t/w, and
∂_s(−(v/2ρ) sin 2φ) = (v/2ρ²) cos φ sin 2φ − (v/ρ) cos 2φ ∂_sφ = (v/ρ²) sin φ cos²φ + (v/ρ) cos 2φ (κ + sin φ/ρ).
So κ_t = (v/ρ)κ(cos 2φ − sin²φ) + (v/ρ²) sin φ (cos²φ + cos 2φ), which is the claim. (∂_t and ∂_θ commute on ψ
because x is C² in θ with ∂_t∂²_θx continuous: second variational equation.)
(iv) ρ sin φ = T × r and ∂_s(T × r) = κ JT × r + T × T = −κ T·r = −κρ cos φ ((Ja) × b = −a·b); T × r → 0 as s → 0. ∎

**Lemma 2 (two-point identities).** For labels a < b and every t (derivatives in t):
(i) l' = v ∫_a^b T·AT ds;  c' = v e·(F(r_b) − F(r_a)) = v ∫_a^b e·AT ds;
(ii) **E' = v ∫_a^b (T − e)·A T ds = v∫(T − e)·A(T − e) ds − (v/2)∫ (e·Ae)|T − e|² ds + v∫ τ q ds,**
     τ := T·e^⊥, q := e^⊥·A e (A = A(r(s)));
(iii) ∫_a^b |T − e|² ds = 2E = N²;  ∫_a^b τ ds = 0;  |τ| ≤ |T − e|;
(iv) (triangle with Harry) if ρ_a, ρ_b ≥ ε and P is differentiable at t: X := r_a × r_b = r_a × (x_b − x_a) satisfies
     X' = vX(1/ρ_a + 1/ρ_b) − P' × (x_b − x_a).

*Proof.* (i) l = ∫|∂_θx|dθ and Lemma 1(i) (dominated convergence: |w_t| ≤ (2v/ε)w). c' = e·(x_b' − x_a') and
F(r_b) − F(r_a) = ∫_a^b ∂_s F(r(s)) ds = ∫ AT ds. (ii) Subtract; then (T − e)·AT = (T − e)·A(T − e) + (T − e)·Ae and
(T − e)·Ae = [(T − e)·e](e·Ae) + [(T − e)·e^⊥](e^⊥·Ae), with (T − e)·e = T·e − 1 = −|T − e|²/2 and
(T − e)·e^⊥ = τ. (iii) |T − e|² = 2 − 2T·e and ∫T ds = x_b − x_a = ce; ∫τ ds = (x_b − x_a)·e^⊥ = 0.
(iv) r' = v r̂ − P' for ρ ≥ ε; X' = v(r̂_a × r_b + r_a × r̂_b) − P' × r_b − r_a × P' = vX(1/ρ_a + 1/ρ_b) − P' × (r_b − r_a). ∎

## 3. Differential inequalities for the excess

**Lemma 3.** Fix labels a < b and a time t; l, c, e, E, N as above.
(a) For every constant q̄:  E' ≤ v ∫_a^b a*(ρ)|T − e|² ds + v ∫_a^b τ (q − q̄) ds.
(b) E' ≤ v N ‖AT‖_{L²((a,b), ds)}.
(c) **(far inequality)** Let K be the convex hull of the arc {x_s : a ≤ s ≤ b}, ρ_m := dist(P, K), and assume ρ_m ≥ ε.
    Put p_a := r_a × e (so |p_a| = distance from P to the line through x_a, x_b). Then
       E' ≤ (v/ρ_m)(1 + l/ρ_m + 2l²/ρ_m²) N² + 2v l^{3/2} |p_a| N / ρ_m³,
       l' ≤ (2v/ρ_m) [ l (|p_a| + l^{1/2}N)²/ρ_m² + N² ].
(d) **(metric inequality)** On a sub-arc (s₁, s₂) with ρ ≥ ε: ∫_{s₁}^{s₂} T·AT ds = ∫ sin²φ/ρ ds ≤ 2∫_{s₁}^{s₂} dG/ρ,
    G(s) := l(s₁, s) + ρ_{s₁} − ρ_s = ∫_{s₁}^s (1 − cos φ) ds ≥ 0; and
       ∫_{s₁}^{s₂} dG/ρ ≤ G(s₂)/ρ_{s₂} + ∫_{s₁}^{s₂} G/ρ² ds.
Consequence of (c) (Duhamel form; N_η := (N² + η²)^{1/2}, then η → 0): if on [t₁, t₂] the hull stays at distance
ρ_m(t) ≥ max(ε, 4 l(t)) from P, then with α := 1.375 v/ρ_m and β := 2v l^{3/2}|p_a| ρ_m^{-3}:
       N(t₂) ≤ exp(∫_{t₁}^{t₂} α) N(t₁) + ∫_{t₁}^{t₂} exp(∫_t^{t₂} α) β(t) dt.

*Proof.* (a) In Lemma 2(ii): (T − e)·A(T − e) ≤ a*|T − e|² (Lemma V(ii)); the second term is ≤ 0 (A ≥ 0); and
∫τ q = ∫τ(q − q̄) since ∫τ = 0. (b) Cauchy–Schwarz in E' = v∫(T − e)·AT and Lemma 2(iii).
(c) On K − P we have |y| ≥ ρ_m ≥ ε, so q(s) = Q(r(s)) with Q(y) := e^⊥·Π(y)e/|y| = −(y·e)(y·e^⊥)/|y|³. In the
coordinates m := y·e, p := y·e^⊥ (|y|² = m² + p²): ∂_pQ = −m(m² − 2p²)/|y|⁵, ∂_mQ = −p(p² − 2m²)/|y|⁵, hence
|∂_pQ| ≤ 1/|y|² (max of |c(3c² − 2)| on [−1, 1] is 1) and |∂_mQ| ≤ 2|p|/|y|³. For s ∈ [a, b] the segment
y(σ) = r_a + σ(x_s − x_a), σ ∈ [0, 1], lies in K − P; along it dp = δ(s)dσ, dm = ((x_s − x_a)·e)dσ with
δ(s) := (x_s − x_a)·e^⊥ = ∫_a^s τ, |δ(s)| ≤ ∫_a^b |T − e| ≤ l^{1/2}N, |(x_s − x_a)·e| ≤ l, and
|p| ≤ |p_a| + |δ(s)|. Therefore
   |q(s) − q(a)| ≤ l^{1/2}N/ρ_m² + 2l(|p_a| + l^{1/2}N)/ρ_m³.
Use (a) with q̄ = q(a), a* ≤ 1/ρ_m on the arc, ∫|T − e|² = N², ∫|τ| ≤ l^{1/2}N:
   E' ≤ (v/ρ_m)N² + v l^{1/2}N [ l^{1/2}N/ρ_m² + 2l(|p_a| + l^{1/2}N)/ρ_m³ ],
which is the first claim. For the length: T·AT = sin²φ/ρ, and ρ sin φ = T × r = e × r + (T − e) × r, so
|ρ sin φ| ≤ |p(s)| + ρ|T − e| with |p(s)| = |r(s) × e| ≤ |p_a| + l^{1/2}N; hence
sin²φ ≤ 2(|p_a| + l^{1/2}N)²/ρ² + 2|T − e|², and integrate with ρ ≥ ρ_m.
(d) sin²φ = (1 − cos φ)(1 + cos φ) ≤ 2(1 − cos φ); ∂_sρ = cos φ gives G' = 1 − cos φ; integrate by parts:
∫G'/ρ = [G/ρ] + ∫G cos φ/ρ² ds ≤ G(s₂)/ρ_{s₂} + ∫G/ρ² (G ≥ 0, G(s₁) = 0).
Consequence: N_ηN_η' = E' ≤ αN² + βN ≤ αN_η² + βN_η with α = (v/ρ_m)(1 + 1/4 + 2/16), β = 2vl^{3/2}|p_a|/ρ_m³; so
N_η' ≤ αN_η + β; variation of constants; let η → 0. ∎

**Lemma 4 (static geometry of the front at a fixed time).**
(a) (sub-chord tilt) For a ≤ a' < b' ≤ b: |e_{a'b'} − e_{ab}| ≤ [ l(a',b')^{1/2} N(a,b) + E(a',b') ] / c(a',b').
(b) (excess seen from a point of a chord) Let a₀ < a₁ ≤ s₁ < s and let P lie on the segment [x_{a₀}, x_{a₁}]. Then
    G := l(s₁, s) + ρ_{s₁} − ρ_s ≤ E(a₀, s).

*Proof.* (a) c(a',b')e_{a'b'} − l(a',b')e_{ab} = ∫_{a'}^{b'}(T − e_{ab})ds, of norm ≤ l(a',b')^{1/2}(∫_a^b|T − e_{ab}|²)^{1/2}
= l(a',b')^{1/2}N(a,b); and the left side equals c(a',b')(e_{a'b'} − e_{ab}) − E(a',b')e_{ab}.
(b) ρ_{s₁} ≤ |P − x_{a₁}| + l(a₁, s₁), ρ_s ≥ c(a₀, s) − |P − x_{a₀}|, and |P − x_{a₀}| + |P − x_{a₁}| = c(a₀, a₁) ≤
l(a₀, a₁). Add. ∎

## 4. Construction C (virtual greedy chase with step ε) and the reduction theorem

t_ε := (1 − ε)/(1 − v), ε₁ := e^{2μ}ε, Λ₀ := 2π e^{2μ}/(1 − v).

**Construction C.**
* Phase 0: P(s) := s (real axis) for 0 ≤ s ≤ t_ε.
* Leg 0: P continues straight along the real axis at unit speed until it meets x₀ (label θ = 0), at time t₀. a₀ := 0.
* Leg j+1 (j ≥ 0): at time t_j, P(t_j) = x_{a_j}(t_j). Let a_{j+1} := max{θ ∈ [a_j, 2π] : l_{t_j}(a_j, θ) ≤ ε}.
  If a_{j+1} = 2π: stop (P constant afterwards). Otherwise l_{t_j}(a_j, a_{j+1}) = ε; P runs at unit speed along the
  ray from P(t_j) through x_{a_{j+1}}(t_j) until it meets x_{a_{j+1}}, at time t_{j+1}.
Each step is computed from P on earlier times, so P depends only on (v, ε).

**Lemma C.** (0) *No accumulation.* On [0, T], |∂_θx| ≤ e^{2vT/ε} (Lemma 1(i), V(ii)). A non-final leg j+1 with t_j ≤ T has
ε = l_{t_j}(a_j, a_{j+1}) ≤ e^{2vT/ε}(a_{j+1} − a_j); so at most 2πe^{2vT/ε}/ε legs start before T. Hence either the
construction stops or t_j → ∞, and P is a well-defined 1-Lipschitz path on [0, ∞).
(1) Phase 0: virtual = true candidates on [0, t_ε]; ρ₀(t_ε) = ε. Leg 0 lasts ≤ ε/(1 − v); t₀ ≤ 1/(1 − v).
(2) During leg j+1, with u the unit vector from P(t_j) to x_{a_{j+1}}(t_j): x_{a_{j+1}}(t) = P(t) + ρ(t)u with
ρ' = −1 + vf(ρ) ≤ −(1 − v), and x_{a_j}(t) = P(t) − β(t)u with β ≥ 0, β(t_j) = 0. So x_{a_j}(t), P(t), x_{a_{j+1}}(t) are
collinear in this order; the leg lasts τ_{j+1} ≤ c(a_j, a_{j+1}; t_j)/(1 − v) ≤ ε/(1 − v), and P is 1-Lipschitz.
(3) Every θ ∈ [a_j, a_{j+1}] is seen by time t_j. If the construction stops, every direction is seen by the stopping
time.
(4) For t in leg j+1: l_t(a_j, a_{j+1}) ≤ ε₁, hence |P(t) − x_{a_j}(t)| ≤ c(a_j, a_{j+1}; t) ≤ ε₁; and
l_t(a, b) ≤ e^{2μ} l_{t_j}(a, b) for all a < b.
(5) R₀ := l_{t₀}(0, 2π) ≤ Λ₀.

*Proof.* (1) A true candidate has ρ_θ' = v − r̂·P' ≥ −(1 − v), so ρ_θ(t) ≥ 1 − (1 − v)t ≥ ε
on [0, t_ε]; there the true candidates solve the virtual equation (F is the unit field on |x| ≥ ε), so they are the
virtual ones by uniqueness. Candidate 0 stays on the positive axis with ρ₀ = 1 − (1 − v)t. On leg 0 the ansatz
x₀ = P + ρu, u = (1, 0), solves both equations with ρ' = −1 + vf(ρ) ≤ −(1 − v), ρ(t_ε) = ε. (2) Same ansatz for the
target. For a_j: the ansatz x_{a_j} = P − βu (r = −βu, F(r) = −f(β)u, P' = u) solves x' = vF(r) iff β' = 1 + vf(β),
β(t_j) = 0, so β ≥ 0; uniqueness. c(a_j, a_{j+1}; t_j) ≤ l_{t_j}(a_j, a_{j+1}) ≤ ε. (3) ρ_θ(t_j) = c(a_j, θ; t_j) ≤ l_{t_j}(a_j, θ) ≤ ε; Lemma
VC(c). The intervals [a_j, a_{j+1}] cover [0, 2π]. (4) l' = v∫T·AT ≤ (2v/ε) l (Lemma 2(i), V(ii)) and τ_{j+1} ≤ ε/(1 − v).
(5) By (1) and the cited Proposition, l_{t_ε}(0, 2π) ≤ 2π + 2πvt_ε < 2π/(1 − v); leg 0 multiplies lengths by ≤ e^{2μ}. ∎

**Hypotheses** (constants γ ∈ (0, 1], r₀ ∈ (0, 1], c₀, c₁ ≥ 0 with c₀ + c₁ ≤ 1/4, r₁ ∈ (0, 1], K_T ≥ 0, b* ∈ (0, 2π];
a starting leg index j_s ≥ 0 and a bound L_s ≥ R_{j_s} := l_{t_{j_s}}(a_{j_s}, 2π); for j_s = 0 one may take L_s = Λ₀).
For every leg j+1 > j_s reached by the construction and every t ∈ [t_j, t_{j+1}]:
* **(F_b) flatness of the bulk seen from the base.** For every label s ∈ (a_{j+1}, b*] with l := l_t(a_j, s) ≤ r₀:
     E(a_j, s; t) ≤ Φ(l) := c₀ l (l/r₀)^{2γ} + c₁ ε.
* **(S) separation.** For every s ∈ (a_{j+1}, b*] with l_t(a_j, s) > r₀: ρ_s(t) ≥ r₁.
* **(T) tip.** K_tip(t) := ∫_{max(a_{j+1}, b*)}^{2π} T·AT ds ≤ K_T.

**Theorem R (reduction).** Assume (F_b), (S), (T) and put
   K* := 16 e^{2μ} + 4c₀(1 + 1/γ) + 2c₁ + 2e^{2μ}L_s/r₁ + K_T.
If μK* < 1, construction C stops after at most L_s/(ε(1 − μK*)) legs after leg j_s, at a time
   T ≤ t_{j_s} + L_s/((1 − v)(1 − μK*))   (for j_s = 0: T ≤ 1/(1 − v) + Λ₀/((1 − v)(1 − μK*))),
and every direction is seen by then.

*Proof.* Let R_j := l_{t_j}(a_j, 2π) and K̃(t) := ∫_{a_{j+1}}^{2π} T·AT ds for t in leg j+1.
*Claim:* if R_j ≤ L_s then K̃ ≤ K* on leg j+1. Split (a_{j+1}, 2π] into the tip part (labels > b*; ≤ K_T by (T)) and
s ∈ (a_{j+1}, b*], which we split by l := l_t(a_j, s) (strictly increasing in s; ds = dl).
 Near part, l ≤ 8ε₁: measure ≤ 8ε₁ and T·AT ≤ a* ≤ 2/ε: contribution ≤ 16e^{2μ}.
 Far part, l > r₀: ρ ≥ r₁ by (S), so T·AT ≤ a*(ρ) ≤ 2/r₁ (if ρ ≥ ε: 1/ρ ≤ 1/r₁; if ρ < ε: 2/ε < 2/ρ ≤ 2/r₁); the length is
 ≤ l_t(a_{j+1}, 2π) ≤ e^{2μ}R_j ≤ e^{2μ}L_s (Lemma C(4)): contribution ≤ 2e^{2μ}L_s/r₁.
 Middle part, 8ε₁ < l ≤ r₀ (labels s ∈ (s₁, s₂], s₁ the label with l = 8ε₁; s₁ > a_{j+1} since l_t(a_j, a_{j+1}) ≤ ε₁):
 for l ≥ ε, Φ(l) ≤ (c₀ + c₁)l ≤ l/4, so c(a_j, s) ≥ 3l/4 and, by Lemma C(4),
 ρ_s ≥ c(a_j, s) − |P − x_{a_j}| ≥ 3l/4 − ε₁ ≥ l/2 (≥ 4ε₁ > ε). So Lemma 3(d) applies on (s₁, s₂), and by Lemma 4(b)
 (P ∈ [x_{a_j}, x_{a_{j+1}}], Lemma C(2)) G(s) ≤ E(a_j, s) ≤ Φ(l). Hence the contribution is
   ≤ 2[Φ(l₂)/(l₂/2) + ∫_{8ε₁}^{l₂} 4Φ(l)/l² dl] ≤ 4(c₀ + c₁/8) + 8[c₀/(2γ) + c₁ε/(8ε₁)] ≤ 4c₀(1 + 1/γ) + 2c₁,
 where l₂ ≤ r₀ is the value of l at s₂. This proves the claim.
*Induction.* R_{j_s} ≤ L_s (for j_s = 0: Lemma C(5)). If R_j ≤ L_s (j ≥ j_s) and leg j+1 is not final, then by Lemma 2(i)
   R_{j+1} = l_{t_j}(a_{j+1}, 2π) + v∫_{t_j}^{t_{j+1}} K̃ dt ≤ R_j − ε + vK*ε/(1 − v) = R_j − ε(1 − μK*) ≤ L_s.
So R_j ≤ L_s − (j − j_s)ε(1 − μK*); as R_j ≥ 0 there are at most L_s/(ε(1 − μK*)) non-final legs after j_s, each of
duration ≤ ε/(1 − v) (and t₀ ≤ 1/(1 − v)). Everything is seen by Lemma C(3). ∎

**Remarks.** (1) Without any hypothesis the proof gives the *criterion*: if K̃(t) ≤ K* for all t ≥ t_{j_s} and μK* < 1, the
same conclusion holds (K̃ is the quantity K of Prop. D6 for the virtual front beyond the current target).
(2) The proof uses the path only from t_{j_s} on (legs of construction C) and the bound L_s; what Harry did before
t_{j_s} is irrelevant, as long as all directions with labels < a_{j_s} have been seen.

## 5. The bulk theorem (propagation of flatness)

Standing assumptions in this section: v ≤ 10⁻¹² (so e^{2μ} ≤ 2, ε₁ ≤ 2ε, every leg lasts ≤ 2ε), and construction C.

**Labels.** Fix a leg start t_s := t_{j_s} and a label b* ∈ (a_{j_s}, 2π]. Re-label the arc [a_{j_s}, b*] of the front by
its arclength at time t_s measured from x_{a_{j_s}}: u ∈ [0, U], U := l_{t_s}(a_{j_s}, b*). For labels a < b in [0, U]:
λ := u_b − u_a (the *label length*; λ = l_{t_s}(a,b)). Lengths and chords are non-decreasing in t (Lemma VC), so
l_t(a,b) ≥ λ and c(a,b; t) ≥ c(a,b; t_s) for t ≥ t_s.

**Start hypothesis (ST)** at t_s, with constants κ > 0, R ∈ (0, 1]:
 (IC1) E(a,b; t_s) ≤ κ²λ³ for all pairs in [0, U] with ε/2 ≤ λ ≤ 32R;
 (IC2) c(a,b; t_s) ≥ 16R for all pairs in [0, U] with λ > 32R;
 (IC3) κR ≤ 1/1584 and ε ≤ R/64.
By (IC1), (IC3): for ε/2 ≤ λ ≤ 32R, E ≤ λ·(32κR)² ≤ λ/2, so c(a,b;t_s) ≥ λ/2. Hence for all pairs with λ ≥ ε/2 and all
t ≥ t_s:
 (CA) c(a,b; t) ≥ min(λ, 32R)/2.
((CA) is used only for family pairs and in (*) of Step 1(d), which is trivially true when w_s < 4ε.)

**Family.** For t in leg j+1 (t_j ≤ t ≤ t_{j+1}, j ≥ j_s, u_{a_{j+1}} ≤ U: target inside the labelled arc) the family 𝔉(t) consists of the pairs (a,b) with
u_b ≤ U, ε/2 ≤ λ ≤ R, and (a = a_j or a ≥ a_{j+1}). The *gap* of such a pair is g := u_a − u_{a_j} ≥ 0. A pair is *far* if
g ≥ 64λ, *near* otherwise. The family only shrinks as t grows, and g is non-increasing in t.

**Theorem B (bulk).** Assume (ST), v ≤ 10⁻¹² and v(4U + 2) ≤ 10⁻⁶R. Put M := R^{-1/4}/140. Then for every t ≥ t_s up to
the end of the last leg j+1 with u_{a_{j+1}} ≤ U (target inside the labelled arc), and every pair in 𝔉(t):
   (I1) l_t(a,b) ≤ 2λ;    (I2) E(a,b; t) ≤ ½M²λ^{3/2}  (i.e. N ≤ Mλ^{3/4}).
Consequently, if b' is a label with u_{b'} ≤ U − ε/2, then for every leg j+1 > j_s with a_{j+1} < b' and every t in it,
hypotheses (F_b) and (S) of Theorem R hold with b' in the place of b*, and γ = 1/4, r₀ = R, c₀ = M²R^{1/2}/2 = 1/39200,
c₁ = 0, r₁ = R/8.

*Proof of the consequence.* Here u_{a_{j+1}} < u_{b'} ≤ U − ε/2, so the leg is one of those considered and Step 1(a)
below applies: u_{a_{j+1}} − u_{a_j} ≥ ε/2. Let
s ∈ (a_{j+1}, b']; the pair (a_j, s) has λ ≥ ε/2.
If l := l_t(a_j, s) ≤ R then λ ≤ l ≤ R, the pair is in 𝔉(t), and E ≤ ½M²λ^{3/2} ≤ ½M²R^{1/2}·l(l/R)^{1/2}: (F_b).
If l > R then λ > R/2 (if λ ≤ R, (I1) gives λ ≥ l/2), and by (CA) and Lemma C(4):
ρ_s ≥ c(a_j, s; t) − |P − x_{a_j}| ≥ min(λ, 32R)/2 − 2ε ≥ R/4 − R/32 ≥ R/8: (S). ∎

*Proof of Theorem B.* Let t* be the supremum of the times t' such that (I1), (I2) hold for all t ∈ [t_s, t'] and all
pairs of 𝔉(t). At t_s: l = λ and E ≤ κ²λ³ ≤ κ²R^{3/2}λ^{3/2} ≤ M²λ^{3/2}/128 (by (IC3): κR^{3/4} ≤ M/(8√2)). We show:
**(Imp)** if (I1), (I2) hold on [t_s, t*) then for every t ≤ t* and every pair of 𝔉(t): l_t ≤ √2 λ and E ≤ ¼M²λ^{3/2}.
This proves the theorem: (I1), (I2) then hold at t* by continuity (a pair of 𝔉(t*) is in 𝔉(t) for t < t* close to
t*), and for t ∈ [t*, t* + δ]: l_t ≤ e^{2vδ/ε}l_{t*} (as l' ≤ (2v/ε)l) and |E'| ≤ v∫|T − e||AT| ds ≤ (4v/ε) l, so
E(t) ≤ ¼M²λ^{3/2} + δ(8v/ε)·2λ; both stay below the bounds (I1), (I2) for a δ > 0 that depends only on (v, ε, M)
because λ ≥ ε/2; since 𝔉(t) ⊂ 𝔉(t*), t* would not be the supremum unless it is the final time.
From now on (I1), (I2) are assumed on [t_s, t*), all times are < t*, and "family" bounds refer to them.

**Step 1 (legs, times, distances).** (a) For the legs considered (u_{a_{j+1}} ≤ U): u_{a_{j+1}} − u_{a_j} ∈ [ε/2, ε]: it is ≤ l_{t_j}(a_j, a_{j+1}) ≤ ε; and if it were
< ε/2, the label s with u_s = u_{a_j} + ε/2 (which is ≤ U, since otherwise a_{j+1} would have label > U) would have
l_{t_j}(a_j, s) ≤ 2·ε/2 = ε by (I1) and s > a_{j+1}, contradicting the maximality of a_{j+1}. (b) Hence there are at most
2U/ε + 1 legs considered, and the time elapsed since t_s is ≤ T_B := 4U + 2. (c) For a fixed label a the gaps
at successive legs are spaced by ≥ ε/2 and each leg lasts ≤ 2ε; so for every non-increasing h ≥ 0 and 0 ≤ g₀:
   ∫_{ {t: g(t) ≥ g₀} } h(g(t)) dt ≤ 2ε h(g_min) + 4∫_{g_min}^∞ h(g) dg,  g_min := the smallest gap ≥ g₀ attained.
(d) For t in leg j+1 and a label s with w_s := u_s − u_{a_j} ≥ 0: by (CA) and Lemma C(4),
   (*) ρ_s ≥ min(w_s, 32R)/2 − 2ε;  hence max(ρ_s, ε) ≥ min(w_s, 32R)/6.
(With m := min(w_s, 32R): if m ≤ 6ε, ε ≥ m/6; if m > 6ε, m/2 − 2ε ≥ m/6.)

**Step 2 (tilt lemma (TL)).** *At any time, if J ⊂ I are pairs of the family, then |e_J − e_I| ≤ 91 M λ_I^{1/4}.*
First let J' ⊂ I' be family pairs sharing an endpoint with λ_{I'} ≤ 3λ_{J'}. By Lemma 4(a), (I1), (I2), (CA):
 |e_{J'} − e_{I'}| ≤ [(2λ_{J'})^{1/2} M(3λ_{J'})^{3/4} + ½M²λ_{J'}^{3/2}]·2/λ_{J'} = Mλ_{J'}^{1/4}[2√2·3^{3/4} + Mλ_{J'}^{1/4}] ≤ 6.7 Mλ_{J'}^{1/4}
(MR^{1/4} = 1/140). Now let J = (α, β) ⊂ I = (a, b). (A) Extend to the right: β_k := min(u_α + 2^kλ_J, u_b), k = 0, …, k₁
(β_{k₁} = b); the arcs (α, β_k) are in the family (same first point α, length ≤ R), consecutive lengths have ratio ≤ 2,
and Σ_{k<k₁} 6.7M(2^kλ_J)^{1/4} ≤ 6.7M λ_I^{1/4}/(1 − 2^{-1/4}) ≤ 42.11 Mλ_I^{1/4}. (B) If α > a, extend to the left down to
a° := a if a ≥ a_{j+1}, a° := a_{j+1} if a = a_j: α_k := max(u_b − 2^kλ(α,b), u_{a°}); the arcs (α_k, b) start at labels
≥ a_{j+1}, so they are in the family; same sum ≤ 42.11 Mλ_I^{1/4}. (C) If a = a_j ≠ a°: (a_{j+1}, b) ⊂ (a_j, b) with
λ(a_j, b) ≤ λ(a_{j+1}, b) + ε ≤ 3λ(a_{j+1}, b) (as λ(a_{j+1}, b) ≥ λ_J ≥ ε/2): one more step, ≤ 6.7Mλ_I^{1/4}. Total ≤ 91Mλ_I^{1/4}. ∎
Consequence: for a family pair (a,b) and any family sub-arc J ⊂ (a,b) (in particular J = (a, s) with u_s − u_a ≥ ε/2)
with label length λ_J (shorter arcs are always enlarged to label length ε/2 where (μ) is used),
   (μ) ∫_J |T − e_{ab}|² ds ≤ 2N(J)² + 2l(J)|e_J − e_{ab}|² ≤ 2M²λ_J^{3/2} + 4λ_J·91²M²λ^{1/2} ≤ C_μ M²λ^{1/2}λ_J,  C_μ := 33126,
and by Cauchy–Schwarz ∫_J |T − e_{ab}| ds ≤ (2λ_J·C_μM²λ^{1/2}λ_J)^{1/2} ≤ 258 Mλ^{1/4}λ_J.

**Step 3 (far pairs: (I2) with M/2).** Let (a,b) be far at time t (leg j+1): g ≥ 64λ ≥ 32ε, so a > a_{j+1}, and the pair
has been in the family and far since t_s. Put ĝ := min(g, 32R). The hull of the arc lies in B(x_a, l), l ≤ 2λ, so by (*)
(with ε₁ ≤ 2ε ≤ 4λ) ρ_m ≥ ĝ/2 − 6λ ≥ ĝ/4 (if g ≤ 32R: 6λ ≤ 6g/64; otherwise 16R − 6R ≥ 8R); in particular
ρ_m ≥ 8λ ≥ max(ε, 4l), and Lemma 3(c) (Duhamel form) applies on the whole far period with α ≤ 1.375v/ρ_m ≤ 5.5v/ĝ.
*Amplification.* Between a time with gap g₁ and a later one with gap g₂ (both ≤ 32R), Step 1(c):
∫α dt ≤ 5.5v[2ε/g₂ + 4 log(g₁/g₂)] ≤ 0.35v + 22v log(g₁/g₂); while g > 32R, ∫α dt ≤ 5.5vT_B/(32R). So with ν := 22v and
A₀ := exp(v(0.35 + 0.18T_B/R)) ≤ 2: exp(∫α) ≤ A₀ (min(g₁, 32R)/g₂)^ν.
*Forcing* β = 2vl^{3/2}|p_a|/ρ_m³. If g > R/2: |p_a| ≤ ρ_a ≤ ρ_m + l ≤ 1.25ρ_m; for R/2 < g ≤ 32R, ρ_m ≥ 0.4g ≥ 13l and ρ_m ≥ R/8, so β ≤ 2v(2λ)^{3/2}·(14/13)·64/R² ≤ 408vλ^{3/2}/R²;
for g > 32R, ρ_m ≥ 16R − 2ε − 2λ ≥ 13.9R and β ≤ 2v(2λ)^{3/2}·1.25/(13.9R)² ≤ 0.04vλ^{3/2}/R².
If g ≤ R/2: P lies on [x_{a_j}, x_{a_{j+1}}] (Lemma C(2)), so |p_a| ≤ max_{a'∈{a_j, a_{j+1}}} dist(x_{a'}, line(x_a, x_b)), and
dist = c(a',a)|e_{a'a} × e_{ab}| ≤ c(a',a)(|e_{a'a} − e_{a'b}| + |e_{ab} − e_{a'b}|). The pairs (a',a), (a,b), (a',b) are in the
family (label lengths ≥ 64λ − ε ≥ ε/2, resp. ≤ g + λ ≤ R), so by (TL) and c(a',a) ≤ l ≤ 2g:
   |p_a| ≤ 2g·2·91M(g + λ)^{1/4} ≤ 366 M g^{5/4},  and  β ≤ 2v(2λ)^{3/2}·366Mg^{5/4}·64/g³ ≤ 1.33·10⁵ vMλ^{3/2}g^{-7/4}.
*Result.* At a time with gap g₂ ≥ 64λ, using N(t_s) ≤ √2κλ^{3/2}, Step 1(c) with h(g) = g^{ν−7/4} and ν ≤ 1/12:
 N ≤ A₀(32R/g₂)^ν[√2κλ^{3/2} + 408vT_Bλ^{3/2}/R²] + A₀·1.33·10⁵vMλ^{3/2} g₂^{-ν}[2εg₂^{ν−7/4} + 4g₂^{ν−3/4}/(3/4 − ν)]
   ≤ A₀[(√2κ + 408vT_B/R²)R^{3/4} + 3.6·10⁴ vM] λ^{3/4}
((32R/g₂)^νλ^{3/2} ≤ (R/λ)^νλ^{3/2} ≤ R^{3/4}λ^{3/4}; g₂^{-3/4}(1/16 + 6) ≤ 6.07(64λ)^{-3/4} ≤ 0.268λ^{-3/4}). Since
√2κR^{3/4} ≤ M/8, 408vT_BR^{-5/4} ≤ 408·10⁻⁶R^{-1/4} ≤ M/16 and 3.6·10⁴v ≤ 1/16: **N ≤ 2·(M/4)λ^{3/4} = (M/2)λ^{3/4}, i.e.
E ≤ M²λ^{3/2}/8 for far pairs.**

**Step 4 (near pairs).** Let (a,b) ∈ 𝔉(t) be near (a = a_j, g = 0; or a ≥ a_{j+1}, g < 64λ). The total time a given pair
spends near is ≤ (128λ/ε + 1)·2ε + 2ε ≤ 264λ (Step 1(c); the last 2ε is the leg in which a is the base). When it
becomes near (or at t_s) E ≤ M²λ^{3/2}/8 (Step 3, resp. the start). We bound the increase ΔE of E while near by
integrating Lemma 3(a) with q̄ = 0: E' ≤ I + II, I := v∫_a^b a*(ρ)|T − e|² ds, II := v∫_a^b |τ||q| ds, e := e_{ab}.
Put ρ̄ := max(ε, min_{[a,b]}ρ) and g̃ := max(g, ε). By (*), every s ∈ [a, b] has w_s ≥ g, so ρ̄ ≥ min(g,32R)/6.
(A near pair can have g ∈ (32R, 64R) when λ > R/2; then 6ρ̄ ≥ 32R ≥ λ and log⁺(λ/(6ρ̄)) = 0; otherwise 6ρ̄ ≥ g̃. So
log⁺(λ/(6ρ̄)) ≤ log⁺(λ/g̃) in all cases.)
*Term I.* a*(ρ) = (1/ε)1_{ρ<ε} + ∫_{max(ρ,ε)}^∞ y^{-2}dy, so I = v[μ(ε)/ε + ∫_ε^∞ μ(y)y^{-2}dy], μ(y) := ∫_{s∈(a,b), ρ_s<y}|T − e|² ds.
By (*), ρ_s < y forces w_s < 2y + 4ε when 2y + 4ε ≤ 32R; so these s lie in the sub-arc J_y of (a,b) starting at a
with label length max(min(λ, 2y + 4ε − g), ε/2) ≤ min(λ, 6y) (y ≥ ε), a family pair. By (μ): μ(y) ≤ C_μM²λ^{1/2}min(λ, 6y)
(also for larger y, trivially), and μ(y) = 0 for y ≤ min ρ. Hence
   I ≤ vC_μM²λ^{1/2}[6 + ∫_{ρ̄}^{λ/6} 6 dy/y + ∫_{λ/6}^∞ λ dy/y²] ≤ 6vC_μM²λ^{1/2}[2 + log⁺(λ/(6ρ̄))] ≤ 6vC_μM²λ^{1/2}[2 + log⁺(λ/g̃)].
*Term II.* By Lemma V(iii), |q| ≤ |p(s)|/max(ρ_s, ε)², p(s) := (x_s − P) × e, and since P ∈ [x_{a_j}, x_{a_{j+1}}],
|p(s)| ≤ max_{a'}|(x_s − x_{a'}) × e|. Let ϑ := 260Mλ^{1/4} if 65λ ≤ R, ϑ := 2 otherwise (note 258Mλ^{1/4} ≤ ϑ ≤ 2).
 – If a' ≤ a (always when a ≥ a_{j+1}; and a' = a_j when a = a_j): (x_s − x_{a'}) × e = ∫_a^s τ + (x_a − x_{a'}) × e. The first
 term is ≤ ∫_{(a,s)}|T − e| ≤ 258Mλ^{1/4}λ'_s ≤ ϑλ'_s, λ'_s := max(u_s − u_a, ε/2) (Step 2). The second vanishes if a' = a. Assume first
 65λ ≤ R. If g' := u_a − u_{a'} ≥ ε/2 it equals c(a',a)|e_{a'a} × e_{ab}| ≤ 2g'·(|e_{a'a} − e_{a'b}| + |e_{ab} − e_{a'b}|) ≤ 4ϑg: the
 three pairs (a',a), (a,b), (a',b) are in the family (λ(a',b) ≤ 65λ ≤ R), c(a',a) ≤ 2g' by (I1), and (TL) bounds each
 tilt by 91M(65λ)^{1/4} ≤ ϑ. If 0 < g' < ε/2 (only a' = a_{j+1}): with J₀ := (a', label u_{a'} + ε/2) ⊂ (a', b),
 |(x_a − x_{a'}) × e| ≤ l(a',a)^{1/2}(∫_{J₀}|T − e_{ab}|²)^{1/2} ≤ ε^{1/2}[2M²(ε/2)^{3/2} + 2ε(2ϑ)²]^{1/2} ≤ 3ϑε.
 – If a = a_j and a' = a_{j+1}: (x_s − x_{a'}) × e = ±∫ τ over the arc between a' and s, contained in (a, max(s, a')):
 ≤ ϑ·max(λ'_s, ε) when a' ≤ b. If a' = a_{j+1} > b (possible when ε/2 ≤ λ < u_{a_{j+1}} − u_{a_j}), put I := (a_j, a_{j+1}) (a family
 pair, ε/2 ≤ λ_I ≤ ε ≤ 2λ). Then |(x_s − x_{a'}) × e| ≤ ∫_I |T − e_{ab}| ds ≤ l(I)^{1/2}N(I) + l(I)|e_I − e_{ab}| ≤ (√2 + 182)Mλ_I^{5/4}
 ≤ 219 Mλ^{1/4} ε ≤ ϑε, by (I1), (I2) and (TL) applied to (a,b) ⊂ I.
 So if 65λ ≤ R: |p(s)| ≤ ϑ(λ'_s + 4g + 3ε) ≤ ϑ(5w_s + 4ε) (λ'_s ≤ w_s − g + ε/2), and with (*), for w_s ≤ 32R,
 |q| ≤ ϑ(5w_s + 4ε)/max(ε, w_s/6)² ≤ 34ϑ/max(ε, w_s/6) = 204ϑ/max(w_s, 6ε) = ∫_{max(w_s,6ε)}^∞ 204ϑ y^{-2}dy.
 If 65λ > R (ϑ = 2) the same bound holds trivially: |p(s)| ≤ ρ_s gives |q| ≤ 1/max(ρ_s, ε) ≤ 6/max(w_s, 6ε). In both cases,
 for w_s > 32R, |p| ≤ ρ_s and ρ_s ≥ 15R give |q| ≤ 1/(15R). Therefore, with ∫_{s∈(a,b), w_s<y}|T − e| ds ≤ ϑ min(λ, y) for
 y ≥ 6ε (Step 2, sub-arc of label length ≤ max(y − g, ε/2); zero if y ≤ g):
   II ≤ 204vϑ² ∫_{max(6ε, g)}^∞ min(λ, y) y^{-2}dy + (v/(15R))∫_a^b|T − e| ds ≤ 204vϑ²[1 + log⁺(λ/g̃)] + 0.1vMλ^{5/4}/R
 (∫|T − e| ≤ l^{1/2}N ≤ √2 Mλ^{5/4}).
*Time integrals.* ∫_{near}[1 + log⁺(λ/g̃)]dt ≤ 264λ + 8ε log⁺(λ/ε) + 4∫_ε^λ log(λ/g)dg ≤ 272λ (Step 1(c); at most two
legs have g < ε, each contributing ≤ 2ε log⁺(λ/ε); and ε log(λ/ε) ≤ λ/e), and ∫_{near}[2 + log⁺]dt ≤ 536λ. So
   ΔE ≤ 6·536·C_μ vM²λ^{3/2} + 204·272 vϑ²λ + 26.4 vMλ^{9/4}/R ≤ 1.07·10⁸vM²λ^{3/2} + 5.6·10⁴vϑ²λ + 3700 vM²λ^{3/2}
 (Mλ^{9/4}/R ≤ M²λ^{3/2}·(λ/R)^{3/4}/(MR^{1/4}) ≤ 140M²λ^{3/2}). If 65λ ≤ R: ϑ²λ = 67600M²λ^{3/2}, ΔE ≤ 3.9·10⁹vM²λ^{3/2}.
 If 65λ > R: ϑ²λ = 4λ ≤ 4(65/R)^{1/2}λ^{3/2} = 4·8.07·19600 M²λ^{3/2}, ΔE ≤ 3.6·10¹⁰vM²λ^{3/2}. In both cases, as v ≤ 10⁻¹²,
 **ΔE ≤ M²λ^{3/2}/8, so E ≤ M²λ^{3/2}/4 for near pairs.** With Step 3 this is the E-part of (Imp).

**Step 5 ((I1) with √2).** l(t_s) = λ, l' = v∫T·AT. *Far, g > R/2:* T·AT ≤ 1/ρ_m ≤ 8/R, so (log l)' ≤ 8v/R, total ≤ 8vT_B/R.
*Far, g ≤ R/2:* Lemma 3(c): l' ≤ (2v/ρ_m)[l(|p_a| + l^{1/2}N)²/ρ_m² + N²], with |p_a| + l^{1/2}N ≤ 366Mg^{5/4} + √2Mλ^{5/4} ≤ 367Mg^{5/4},
ρ_m ≥ g/4, N² ≤ M²λ^{3/2} ≤ lM²g^{1/2}: (log l)' ≤ (8v/g)(367²·16 + 1)M²g^{1/2} ≤ 1.73·10⁷vM²g^{-1/2}; by Step 1(c),
∫g^{-1/2}dt ≤ 2ε(32ε)^{-1/2} + 8(R/2)^{1/2} ≤ 5.8R^{1/2}; total ≤ 1.0034·10⁸vM²R^{1/2} ≤ 5200v. *Near:* T·AT ≤ a*(ρ), so
l' ≤ v[m(ε)/ε + ∫_ε^∞ m(y)y^{-2}dy] with m(y) := |{s ∈ (a,b): ρ_s < y}| ≤ min(2λ, 12y) (as for μ(y), with (I1) for the
sub-arc J_y); hence l' ≤ 12v[2 + log⁺(λ/g̃)] and the increase while near is ≤ 12·536 vλ ≤ 6500vλ.
Altogether l_t ≤ λ exp(8vT_B/R + 5200v) + 6500vλ ≤ √2λ. ∎

**Remarks.** (1) The constants are deliberately wasteful; the only structural requirements are: exponent 1/2 + γ with
0 < γ < 1/2 (γ = 1/4 here), the smallness MR^γ ≪ 1, and v small against absolute constants and against R/U.
(2) Theorem B does not use the tip at all: every estimate for a pair (a,b) involves only the arc from the base to b.
(3) No weight in the gap is needed: the homogeneous amplification (ρ₀/ρ)^{22v} acts on data of exponent 3/2 and is
absorbed by lowering the exponent to 3/4, and the forcing is concentrated at gaps g ≈ λ.

(4) **Relaxed start (Theorem B with a transient).** The proof uses (ST) at t_s only through: (CA) at t_s; the start
value E ≤ M²λ^{3/2}/8 for pairs that are near at t_s; and N(t_s) in the first term of the *Result* of Step 3. Hence
Theorem B, its consequence and Corollary M remain true, with the same proof and constants, if (IC1)–(IC3) are replaced
by: **(W1)** c(a,b; t_s) ≥ min(λ, 32R)/2 for all pairs in [0, U] with λ ≥ ε/2; **(W2)** for all pairs with
ε/2 ≤ λ ≤ R: E(a,b; t_s) ≤ (M²/128) λ^{3/2} · min(1, 64λ/min(u_a, 32R))^{44v} (u_a = gap at t_s); **(W3)** ε ≤ R/64 —
where M = R^{-1/4}/140 and R ∈ (0, 1] is now a free parameter. [Near pairs: E ≤ M²λ^{3/2}/128. Far pairs with start gap
g_s = u_a ≥ 64λ: A₀(min(g_s, 32R)/g₂)^ν N(t_s) ≤ 2·(M/8)λ^{3/4}(64λ/g₂)^ν ≤ (M/4)λ^{3/4}, and the two forcing terms are
≤ A₀(M/16 + M/16)λ^{3/4} as before, so N ≤ (M/2)λ^{3/4}.] (W2) admits an additive transient near the base: a kink with
excess E_kink(a,b) is allowed as long as κ²λ³ + E_kink ≤ (M²/128)λ^{3/2}(…)^{44v}. For a kink of turning angle Θ at scale
ε (E_kink ≈ Θ²ε) this requires Θ² ≲ M²ε^{1/2}/360, which is NOT uniform as ε → 0 at fixed Θ ~ v. So this proof does
not tolerate an ε-independent additive term c₁ε in (I2); an ε-uniform treatment of the kink needs an invariant
adapted to the kink tail (not proved; see reports/P6a-1.md, Round 6c, §6c.6).

## 6. Conditional main statement

**Corollary M.** Suppose that for some absolute constants κ, R, T_s, L_s, K_T, δ, and all ε ≤ ε₀, v ≤ v₁, construction C
(or any 1-Lipschitz path fixed in advance such that, at some time t_s, P(t_s) = x_a(t_s) for a label a =: a_{j_s}, every
label in [0, a_{j_s}] has been seen by t_s, and P follows the legs of construction C from t_s on) reaches a leg
start t_s ≤ T_s with remaining length R_{j_s} ≤ L_s at which (ST) holds on the arc [a_{j_s}, 2π − δ/2] (a_{j_s} < 2π − δ),
and that (T) holds for all t ≥ t_s with b* := 2π − δ; let ε₀ ≤ min(δ, R/64). Here the leg index j_s (hence a_{j_s}, t_s) may
depend on (v, ε); the constants κ, R, T_s, L_s, K_T, δ may not. Let K* := 32 + 1/1960 + 32L_s/R + K_T and
   v₀ := min(v₁, 10⁻¹², 10⁻⁶R/(4L_s + 2), 1/(2K*)).
Then for v ≤ v₀ and ε ≤ ε₀ every direction is seen by time T_s + 2.1L_s, independent of ε; and (Lemma A4.1 of the paper)
every direction is caught exactly by a path of speed ≤ 1 for these v.

*Proof.* U ≤ R_{j_s} ≤ L_s, so Theorem B applies on [a_{j_s}, 2π − δ/2]. As |∂_θx| ≥ 1, the labels satisfy
U − u_{2π−δ} ≥ δ/2 ≥ ε/2, so b' := 2π − δ is admissible and Theorem B gives (F_b), (S) for b* = 2π − δ with γ = 1/4, r₀ = R, c₀ = 1/39200, c₁ = 0, r₁ = R/8.
Theorem R (started at j_s) has K* = 16e^{2μ} + 20c₀ + 16e^{2μ}L_s/R + K_T ≤ 32 + 1/1960 + 32L_s/R + K_T, and μK* ≤ v(1 + 2v)K* ≤ 0.51,
hence the time is ≤ t_s + L_s/((1 − v)(1 − μK*)) ≤ T_s + 2.1L_s. ∎

**What is NOT proved:** the hypotheses of Corollary M, i.e. the start (ST) and the tip (T). NUMERICAL (every leg,
`code/P6a/everyleg.py`, v = 0.05, 0.1, 0.2, ε = 0.02 … 0.005): for the head-on start, (IC1) and (IC2) hold from the second
leg after first contact with κ² ≤ 0.038 on arcs up to 0.11, and K_tip ≤ 0.27 from then on; (IC3) is NOT satisfied by
these parameters (it requires R ≤ 1/(1584κ) ≈ 3.2·10⁻³ and ε ≤ R/64), and v is 11 orders above the range of Theorem B.
Moreover (referee RP6a-2, §4) (ST) at a FIXED leg index is not ε-uniform for the head-on start: the first-contact kink
has a tail ahead of the base (at j_s = 2, v = 0.1: sup E/λ³ = 0.019, 0.019, 0.40, 11.2, 190 for ε = 5·10⁻³ … 10⁻⁵). So
j_s must grow as ε → 0, or the start condition must be relaxed (Remark (4) after Theorem B and its limits).
