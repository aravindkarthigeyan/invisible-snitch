## 2. Head-on capture
**Lemma H1 (PROVED).** Let Harry's heading u(t) = (cos φ(t), sin φ(t)) be Lipschitz, |φ'| ≤ K. If a candidate has
ρ(t) > 0 on [t1, τ) and ρ(t) → 0 as t ↑ τ, then its bearing β(t) (angle of r = S - H from u) tends to 0.

*Proof.* With φ_r the angle of r, φ_r' = (r × r')/ρ² = -(r × u)/ρ² = sin β/ρ, so ρβ' = sin β - ρφ' (a.e.) and
ρ' = v - cos β. Also ρ' ≥ -(1-v), hence ρ(t) ≤ (1-v)(τ-t) and ∫^τ dt/ρ = ∞. Fix δ ∈ (0, π/2) and pick t2 < τ with
sup_{[t2,τ)} ρ < r* := sin(δ/2)/(2K) (any t2 if K = 0). On the band B = {δ/2 ≤ |β| ≤ π-δ/2}, |β| is absolutely continuous with
|β|' ≥ (sin(δ/2) - Kρ)/ρ ≥ sin(δ/2)/(2ρ) > 0 a.e. Suppose |β(s)| ≥ δ for some s ∈ [t2, τ). (i) |β| never drops below δ
after s: it would have to cross [δ/2, δ] ⊂ B downwards, where it is increasing. (ii) |β| cannot stay in [δ, π-δ/2] on all of
[s, τ), since there |β|' ≥ sin(δ/2)/(2ρ) and ∫_s^τ dt/ρ = ∞. (iii) So |β| ≥ π-δ/2 at some t3 < τ, and by the same crossing
argument |β| ≥ π-δ on [t3, τ), where ρ' = v - cos β ≥ v + cos δ > 0. Then ρ is increasing on [t3, τ) with ρ(t3) > 0,
contradicting ρ → 0. Hence |β| < δ on [t2, τ). ∎

So every candidate is caught exactly head-on, with closing speed → 1-v. In backward time the bearing equation
dβ/dσ = -sin β/ρ + φ' is *attracting* towards β ≈ 0: the backward-from-capture problem is the stable one.

## 3. Linearisation about a straight stretch: an Abel (Riemann–Liouville) equation of order a = 1/(1-v)
Notation: μ = v/(1-v), a = μ + 1 = 1/(1-v).

Base state (exact solution): Harry on the x-axis, H(s) = (s, 0), s ≥ 0. By Prop. 3 of snitch_proved.tex the candidate
caught at time τ sits at time 0 at ((1-v)τ, 0): the catch curve is the forward ray.
Perturbation: heading angle εθ(s), H(s) = ∫_0^s (cos εθ, sin εθ). The candidate caught at τ is at time 0 at
((1-v)τ + O(ε²), ε F((1-v)τ) + O(ε²)).

**Derivation of the linearised catch map (formal first variation; checked numerically, see below).** Write r = S - H,
r_y = ε w. Transverse component of S' = v r̂: S_y' = v r_y/ρ + O(ε²), and S_y = εη + εw with η' = θ, ρ = (1-v)(τ-s) + O(ε).
Hence w'(s) = -θ(s) + μ w(s)/(τ-s), with w(τ) = 0. The homogeneous solutions are c (τ-s)^{-μ}, unbounded at capture,
so the unique bounded solution is w(s) = (τ-s)^{-μ} ∫_s^τ (τ-σ)^μ θ(σ) dσ. At s = 0:

    τ^μ F((1-v)τ) = ∫_0^τ (τ-s)^μ θ(s) ds = Γ(a) (I^a θ)(τ),                                   (L)

I^a the Riemann–Liouville integral of order a. (The solution formula for the linear ODE is PROVED, elementary. The
statement that (L) is the Gateaux derivative of the nonlinear catch map is the formal first variation; I did not write
out a rigorous differentiability proof, so that identification is NUMERICAL: `code/H/linearization_check.py`
integrates the exact nonlinear ODE backwards from capture for θ(s) = sin 3s + s² - 1/2 and v = 0.3, 0.6, 0.8 and finds
|y/ε - F_lin|/|F_lin| = 1e-5, 1e-7, 1e-9 for ε = 1e-2, 1e-3, 1e-4, i.e. O(ε²) agreement.)

Inverse (Harry's steering from the shape):  θ = D^a[ τ^μ F((1-v)τ) ] / Γ(a).

**Proposition H2 (PROVED, for the linear equation (L)).**
(a) *Exact order of the loss.* Under Laplace transform in τ, (L) reads L[τ^μ F((1-v)τ)](p) = Γ(a) p^{-a} L[θ](p): the map
heading ↦ transverse offset is fractional integration of order exactly a = 1/(1-v); heading ↦ slope F' is smoothing of order
exactly μ = v/(1-v). On monomials: θ = τ^q (q > -1) gives F(X) = B(a, q+1) (X/(1-v))^{q+1}, and in matched variables
(X = (1-v)τ) the slope/heading ratio is Γ(a+1)Γ(q+2)/Γ(q+a+1) ~ Γ(a+1) q^{-μ} as q → ∞.
So the brief's heuristic is confirmed exactly: **Harry's heading is a derivative of order 1/(1-v) of Γ's transverse
shape (order v/(1-v) of Γ's slope; Harry's curvature is of order 1/(1-v) of Γ's slope).**
(b) *No exponential instability; analytic well-posedness of the linear problem.* If F(X) = Σ_{n≥1} f_n X^n converges for
|X| < R, the unique L¹_loc solution of (L) is θ(τ) = Σ_{n≥1} f_n (1-v)^n [Γ(n+a)/(Γ(a)Γ(n))] τ^{n-1}, convergent for
|τ| < R/(1-v), i.e. for |X| < R in the matched variable: no loss of radius. For R' < R,
sup_{|X|≤R'} |θ(X/(1-v))| ≤ C(a,R,R') sup_{|X|=R} |F|.
(c) *Evolution form.* With F(t, X) the offset of Γ(t) at distance X ahead of Harry (fixed reference direction),
∂_t F = (1-v) ∂_X F + v F/X - θ(t), θ(t) = ∂_X F(t, 0): transport towards the tip at speed 1-v (outflow at X = 0, so no
boundary condition), a singular zeroth-order term giving amplification X^{-μ} along characteristics (this is the brief's
"stretching exponent v/(1-v)"), and a nonlocal feedback through the tip slope. At the tip, pointwise,
θ'(t) = (2-v) ∂_X² F(t,0)/2: the turning rate is fixed by the tip curvature.

*Proof.* (a) Convolution theorem; L[s^μ] = Γ(μ+1) p^{-μ-1} = Γ(a)p^{-a}. Monomials: ∫_0^τ (τ-s)^μ s^q ds = B(a,q+1) τ^{a+q},
divide by τ^μ. In matched variables θ(X/(1-v)) = (1-v)^{-q}X^q while F'(X) = (q+1)B(a,q+1)(1-v)^{-q-1}X^q, so the ratio is
(q+1)B(a,q+1)/(1-v) = aΓ(a)Γ(q+2)/Γ(q+a+1) = Γ(a+1)Γ(q+2)/Γ(q+a+1) (using 1/(1-v) = a); Stirling gives ~ Γ(a+1) q^{1-a}.
(b) Termwise inversion of (a) with q = n-1: f_n X^n with X = (1-v)τ needs θ-coefficient f_n(1-v)^n / B(a, n) =
f_n (1-v)^n Γ(n+a)/(Γ(a)Γ(n)). Since Γ(n+a)/Γ(n) ~ n^a, the radius is unchanged; the bound follows from Cauchy's estimate
|f_n| ≤ sup|F| R^{-n} and Σ n^a (R'/R)^n < ∞. Uniqueness: I^a is injective on L¹_loc (Titchmarsh convolution theorem).
(c) Differentiate along characteristics X = (1-v)(τ - t) using the linear ODE of the derivation; for F = θ(t)X + c(t)X² + o(X²)
the O(X) terms give θ' = (2-v)c. ∎

**Answer to the brief's trichotomy (for the linearisation):** neither backward-heat (no exponential growth in frequency:
the symbol is p^{-a}, polynomial) nor pure transport (there is a genuine loss): it is a **Volterra equation of the first kind
with Abel kernel of order a = 1/(1-v)** — a *finite* derivative loss, "mildly ill-posed" in C^k (loss a from the offset,
μ from the slope), **well-posed in analytic classes**. Nothing qualitative happens to the continuous linear problem at
v = 1/2; what happens at v = 1/2 is that μ crosses 1, i.e. a crosses 2 — which is exactly the stability threshold of the
discrete chase (section 4).

### 3.1 The contact point (local data at t = t0)
From Prop. 5 of snitch_proved.tex: for small α > 0, h/C = -(1-cos α)/g(α) ≈ -α^{1+v}/2^{1+v}, so with
k'(θ*) = -(1-v²)/(g(θ*) sin θ*):
β - θ* ≈ g(θ*) sin θ* α^{1+v} / (2^{1+v}(1-v²)) and ρ ≈ 2^v d α^{1-v}/g(θ*). Hence along the + branch
β - θ* ≈ κ0 ρ^{(1+v)/(1-v)} = κ0 ρ^{2a-1}, κ0 > 0, i.e. in the frame of the tangent ray of the branch,
**F(X) = c X^{2a}(1 + o(1)), c > 0 (a non-integer power in general).** (PROVED at leading order; it is the expansion in
Prop. 5's proof carried one order further, using only k'(θ*) ≠ 0 from Lemma 1. Higher-order terms are a generalised power
series in α^{1-v}, α^{1+v}, α², not computed.)
Consequence for the linearised sweep (PROVED for (L), applied to F = cX^{2a}): Harry turns instantaneously by θ* at t0
(the angle between his incoming heading and the + branch), then θ(τ) = θ* + c' τ^{2a-1}, c' = c(1-v)^{2a}Γ(3a)/(Γ(a)Γ(2a)) > 0:
the corner is followed by a C¹ heading with curvature ~ τ^{2a-2} → 0. The candidates are eaten at rate
α(τ) ∝ τ^{1/(1-v)} near t0 (since X ∝ α^{1-v}), consistent with |∂_α S| ~ α^{-v} → ∞ at the tip.
The singularity of the field v(S-H)/|S-H| at the contact point therefore costs nothing in the linear theory: the multiplier
Γ(q+2)/Γ(q+a+1) is finite and nonzero for every exponent q > -1, so every generalised power X^{p}, p > 0, in the data
is matched by a power τ^{p-1} in the heading.

## 4. The discrete chase is piecewise-constant collocation of (L); it is unstable exactly for v > 1/2
**Observation (exact, given (L)).** In the discrete chase, the heading is constant on leg j (Harry runs straight at
candidate j, which stays on his forward ray), and candidate j is caught at the end of leg j. In the linearisation,
catch times are fixed by the longitudinal positions to first order, so with uniform catch-time spacing h,
τ_j = jh, condition (L) at τ_n reads
    Σ_{j=1}^n w_{n-j} θ_j = g_n := h^{-a} (nh)^μ F((1-v)nh),     w_k = ((k+1)^a - k^a)/a,           (R)
because ∫_{(j-1)h}^{jh} (nh - s)^μ ds = h^a w_{n-j}. (R) is a lower-triangular Toeplitz system. Its solution is
θ = x * g where x_n are the Taylor coefficients of 1/W(z), W(z) = Σ_k w_k z^k = (1-z) Li_{-a}(z)/(a z).
A perturbation of size δ entering at step m (from rounding, from the discretisation error of the smooth sweep, or from the
non-smooth start at t0) is propagated to step m + n as δ·x_n. So the per-step growth factor of errors is
λ(v) := limsup |x_n|^{1/n}, independent of h.

**Theorem H3 (PROVED).** Let a = 1/(1-v) > 1 and G(z) = (1-z)^a W(z).
1. G is analytic in |z| < 1, continuous on |z| ≤ 1, G(1) = Γ(a) > 0. If a is not an even integer, G has no zeros on
   |z| = 1 and the number of zeros of W in |z| < 1 is exactly ⌊a/2⌋. If a is an even integer, W(-1) = 0.
2. 0 < v < 1/2 (1 < a < 2): W has no zeros in the closed disk; 1/W = (1-z)^a/G is in the disk algebra, so x_n → 0
   (stable; errors are not amplified from step to step).
3. v = 1/2 (a = 2): W = (1+z)/(2(1-z)²), 1/W = 2(1-z)²/(1+z), x = (2, -6, 8, -8, 8, -8, ...): marginal, a persistent
   period-2 zigzag that neither grows nor decays.
4. 1/2 < v < 3/4 (2 < a < 4): W has exactly one zero z0 in |z| < 1; it is simple, real, and z0 ∈ (-1, 0). Hence
   x_n = C z0^{-n} + o(1) with C ≠ 0: **errors grow by the factor λ(v) = 1/|z0| per step, with alternating sign (a zigzag),
   and λ does not depend on h.** For v ≥ 3/4 there are ⌊a/2⌋ ≥ 2 unstable zeros (v = 3/4: one inside plus z = -1).

*Proof.* Facts used: Li_s(z) = Σ k^{-s}z^k is analytic on C \ [1, ∞) in z; for Re s < 0 and 0 < φ < 2π the Jonquière
formula Li_{-a}(e^{iφ}) = Γ(1+a)(2π)^{-1-a}[e^{iψ} ζ(1+a, λ) + e^{-iψ} ζ(1+a, 1-λ)], ψ = π(1+a)/2, λ = φ/2π (verified
numerically to 1e-14 in `code/H/stability.py`); near z = 1, Li_{-a}(z) = Γ(1+a)(-log z)^{-1-a} + (analytic).
(1) Continuity at z = 1 and G(1) = Γ(1+a)/a follow from the last expansion since (1-z)/(-log z) → 1. On the circle,
arg(1 - e^{iφ}) = (φ-π)/2, so writing P = ζ(1+a,λ) > 0, Q = ζ(1+a,1-λ) > 0,
    arg G(e^{iφ}) = (1+a)(φ-π)/2 - φ + ψ + arg(P + Q e^{-iπ(1+a)}) = (a-1)φ/2 + arg(P + Q e^{iχ0}),
where χ0 ∈ (-π, π) is the representative of -π(1+a) mod 2π, i.e. χ0 = -π(1+a) + 2πm with m = ⌊a/2⌋ + 1 (a not even).
P + Qe^{iχ0} is a positive combination of two unit vectors that are not antipodal, so it never vanishes and its argument
stays in the closed arc between 0 and χ0 of length |χ0| < π; as φ ↓ 0, P → ∞ (argument → 0) and as φ ↑ 2π, Q → ∞
(argument → χ0). Total change of arg G around the circle: (a-1)π + χ0 = 2π(m-1) = 2π⌊a/2⌋. By the argument principle
(G is continuous on the closed disk, analytic inside, nonzero on the boundary) W, which has the same zeros as G in the open
disk, has exactly ⌊a/2⌋ zeros there. If a is even, e^{-iπ(1+a)} = -1 and P = Q at φ = π, so W(-1) = 0.
(2) ⌊a/2⌋ = 0 and G ≠ 0 on the closed disk, so 1/W = (1-z)^a/G is continuous on the closed disk and analytic inside; its
Taylor coefficients are its Fourier coefficients on the circle, which tend to 0 (Riemann–Lebesgue).
(3) Li_{-2}(z) = z(1+z)/(1-z)³; expand.
(4) Exactly one zero. W has real coefficients, so non-real zeros come in conjugate pairs; the zero is real. On [0,1) all
w_k > 0 gives W > 0. So z0 ∈ (-1, 0). (Independently: Li_{-a}(-1) = -η(-a) = (2^{1+a}-1)ζ(-a) > 0 for 2 < a < 4 because
ζ > 0 on (-4,-2), while Li_{-a}(x) = x + O(x²) < 0 for small x < 0.) Simple: the argument-principle count is 1.
Then 1/W - A/(z - z0) (A the residue) extends continuously to the closed disk, so its coefficients → 0, and the
coefficients of A/(z - z0) are -(A/z0) z0^{-n}. ∎

**Numbers (NUMERICAL, from the exact formulas; `code/H/stability.py`, `code/H/stability_fast.py`):**

| v | a | zeros of W in disk | z0 | growth factor 1/|z0| per step |
|---|---|---|---|---|
| ≤ 0.49 | < 2 | 0 | – | stable (x_n → 0) |
| 0.50 | 2 | (z = -1 on circle) | -1 | 1 (marginal zigzag) |
| 0.51 | 2.041 | 1 | -0.93375 | 1.0710 |
| 0.52 | 2.083 | 1 | -0.87125 | 1.1478 |
| 0.55 | 2.222 | 1 | -0.70393 | 1.4206 |
| 0.60 | 2.5 | 1 | -0.48122 | 2.0781 |
| 0.65 | 2.857 | 1 | -0.31370 | 3.1877 |
| 2/3 | 3 | 1 | -2+√3 = -0.26795 | 3.7321 |
| 0.70 | 3.333 | 1 | -0.18954 | 5.2759 |
| 0.74 | 3.846 | 1 | -0.11614 | 8.6101 |
| 0.80 | 5 | 2 | | 23.2 |

Winding numbers computed from the Jonquière formula (2·10^5 points) equal ⌊a/2⌋ for all 13 tested v in [0.1, 0.9];
growth factors from the impulse response of (R) (exact recursion, 200–400 steps) agree with 1/|z0| to 5 digits.

**Overshoot variants do not help (NUMERICAL).** If instead Harry catches candidate j a fraction c ∈ (0,1) of the way through
a straight leg and then keeps going straight for the rest of the leg, (R) becomes collocation at parameter c with
W_c(z) = (1-z)/a · Σ_k (k+c)^a z^k. Zero counts in |z| < 0.995 (FFT + argument principle, `stability_fast.py`):
for every c ∈ {0.2,…,0.9} and every v ∈ {0.5, 0.55, …, 0.8} there is at least one zero (often two), and for v = 0.3 the
schemes with c ≤ 0.7 are already unstable. Among "one straight leg per candidate, uniform collocation parameter"
chases, the brief's c = 1 is the most stable, and none is stable for v > 1/2.

## 6. The ε > 0 greedy chase: same mechanism, threshold v* ≈ 0.7800 (explains the brief's failure at v = 0.8)
The brief's ε > 0 controller ("head for the first unseen candidate; switch when it is within ε") is, linearised and in the
limit h → 0 with ε fixed, the rule "point at the candidate that would be caught at time t + δ, δ = ε/(1-v), if Harry kept going
straight". In (L) this gives a Volterra equation of the **second** kind with a fixed look-ahead delay:

    (δ^a/a) θ(t) + ∫_0^t (t+δ-s)^μ θ(s) ds = (t+δ)^μ F((1-v)(t+δ)).                                   (E)

**Proposition H4 (PROVED for the linear model (E)).** Exponential solutions θ = e^{λt} of the homogeneous version of (E)
(on (-∞, t], i.e. away from the start) exist iff Σ(λ) := δ^a/a + ∫_0^∞ (δ+x)^μ e^{-λx} dx = 0, and for Re λ > 0
Σ(λ) = (1/a) e^{λδ} λ^{-a} Γ(a+1, λδ) (upper incomplete gamma). Hence the model is exponentially unstable iff Γ(a+1, s) has a
zero s with Re s > 0; the growth rate is Re(s)(1-v)/ε per unit time: independent of h, and **growing as ε → 0**.
For integer a = n, Γ(n+1, s) = n! e^{-s} e_n(s) with e_n(s) = Σ_{k≤n} s^k/k!. The exact Routh–Hurwitz arrays (rational
arithmetic, `code/H/eps_pursuit.py`) give: e_2, e_3, e_4 Hurwitz-stable (first columns all positive); e_5, e_6, e_7 not
(a zero or negative entry in the first column). So **v = 1/2, 2/3, 3/4: stable; v = 4/5, 5/6, 6/7: unstable**.
*Proof of the formula.* Substitute θ = e^{λs}: ∫_{-∞}^t (t+δ-s)^μ e^{λs} ds = e^{λt}∫_0^∞ (δ+x)^μ e^{-λx} dx. By parts,
∫_0^∞ (δ+x)^μ e^{-λx} dx = -δ^a/a + (λ/a)∫_0^∞ (δ+x)^a e^{-λx} dx, and ∫_0^∞ (δ+x)^a e^{-λx} dx = e^{λδ} λ^{-a-1} Γ(a+1, λδ). ∎
(Identifying the brief's discrete greedy controller with (E) is the h → 0 limit of the collocation structure of section 4 with
parameter c = 1 + ε/((1-v)h) → ∞; that step is NUMERICAL, checked below.)

**NUMERICAL.** Tracking the rightmost zero of Γ(a+1, ·) (mpmath, 30 digits) from the root 0.23981 + 3.12834i of e_5, it crosses
the imaginary axis at **a* = 4.54539, i.e. v* = 1 - 1/a* = 0.779997** (crossing frequency about 2.855). The number of zeros in
{Re s > 0, |s| < 40} (argument principle) is 0 for a = 3, 4, 4.3, 4.5 and 2 for a = 4.6, 4.8, 5, 5.5; for |s| > 40,
Γ(a+1,s) ~ s^a e^{-s} ≠ 0. Predicted growth rate × ε: +0.0480 (v = 0.8), +0.0986 (v = 0.82), -0.0676 (v = 0.75).
Test against the exact nonlinear greedy chase on a straight ray with a 1e-10 kick (`eps_pursuit_test.py`, ε = 1,
spacing h = δ/10 and δ/20):

| v | rate measured (c-1 = 10) | (c-1 = 20) | continuum prediction | period measured (c-1 = 20) | predicted |
|---|---|---|---|---|---|
| 0.75 | -0.0644 | -0.0666 | -0.0676 | 10.27 | 10.03 |
| 0.77 | -0.0214 | -0.0225 | -0.0231 | 10.25 | 10.01 |
| 0.79 | +0.0234 | +0.0233 | +0.0237 | 10.27 | 10.02 |
| 0.80 | +0.0468 | +0.0471 | +0.0480 | 10.29 | 10.04 |
| 0.82 | +0.0952 | +0.0965 | +0.0986 | 10.37 | 10.12 |

(At v = 0.7 the measured decay rate, -0.11, is slower than the tracked branch's -0.17, presumably because of another, less damped
zero or a finite-c effect; it is still decaying.) Finite-c check: zero counts of W_c (c > 1) in |z| < 0.99 are 0 at v ≤ 0.75 and 2
at v ≥ 0.8 for c = 4, 8, 16 (`eps_greedy.py`; for c ≤ 2 near v = 0.75-0.78 and for v ≥ 0.85 the FFT count is not reliable).
**Conclusion (NUMERICAL, plus PROVED for the linear model): the brief's ε > 0 greedy simulator must lose the wavefront for
v > 0.78, with an oscillation of period about 10ε and e-folding time about 21ε at v = 0.8, whatever the step size.** That is the
controller, not (as far as the linear theory can tell) the mathematics: the linearisation of the continuous ε = 0 sweep is
well-posed in analytic classes for every v < 1 (Prop. H2). A larger look-ahead L > ε only rescales δ (slower growth, same sign).


---- From a second team member (stream C), same linearised recursion:
## 3. Where v/(1−v) and v = 1/2 really enter: zigzag instability of the head-on discrete chase

The brief's heuristic ("worst-case stretching while Harry closes on a candidate is a power law with exponent v/(1−v),
≤ 1 iff v ≤ 1/2") is made precise by Lemma C1, but it does **not** govern the stretch at the caught point
(§4: J is radial there, and the radial part is not stretched, Lemma C3). It governs the *stability of the discrete
head-on chase*, and there the threshold v = 1/2 is exact.

**Linearised model.** Radial steady state: candidates at distances m·s (m = 1,2,…) on Harry's forward ray. This is an
exact solution of the discrete chase (Prop. 3: forward-ray candidates stay on the ray, all move at speed v, each leg
lasts s/(1−v) and shortens every distance by s). Perturb by lateral offsets y_m = O(δ). One leg = (a) turn toward the
target: offsets become z_m = y_m − m y_1 + O(δ²), turning angle c = y_1/s + O(δ²); (b) head-on run of length s:
by Prop. 1, C = ρ g(β) is constant and g(β) = 2^v β^{1−v}(1+O(β²)), so β ∝ ρ^{−1/(1−v)} and the offset ρβ is
multiplied by (m/(m−1))^κ, while ρ drops by s + O(δ²); (c) relabel m → m−1. Following one candidate
(P_j := Y_j m_j^κ satisfies P_{j+1} = P_j − m_j^{1+κ}c_j) gives, **to first order in δ, exactly** (s = 1):
  Σ_{j=0}^{k} (k+1−j)^{σ} c_j = (k+1)^κ y_{k+1}(0),   σ := 1 + κ = 1/(1−v).          (Lin)
So C(z)·W_σ(z) = G(z) with W_σ(z) = Σ_{i≥0}(i+1)^σ z^i = Li_{−σ}(z)/z. (This is a discretised first-kind Volterra
equation; its continuum version is the fractional steering law of order 1 + 1/(1−v) noted in the brief.)

**Proposition C6 (PROVED for the linearised recursion (Lin)).**
(a) If 1/2 < v < 3/4 (2 < σ < 4), W_σ has a zero z_0 ∈ (−1,0). Hence for generic data (e.g. one perturbed candidate)
limsup|c_k|^{1/k} ≥ 1/|z_0| > 1: the turning angles grow geometrically with alternating sign (zigzag), at a rate
per leg independent of the spacing s. Same for v = 1 − 1/n, n ≥ 3 integer, and for σ ∈ (6,8) ∪ (10,12) ∪ ….
(b) If 0 < v ≤ 1 − 1/log₂3 ≈ 0.369 (1 < σ ≤ log₂3), W_σ has no zero in the closed unit disc minus {1}, 1/W_σ is
continuous on the closed disc, so c is bounded whenever Σ_k (k+1)^κ|y_{k+1}(0)| < ∞: no geometric growth.
(c) v = 1/2 (σ = 2): W_2 = (1+z)/(1−z)³, zero exactly on |z| = 1: marginal.
Proof. (a) W_σ(0) = 1. Li_{−σ} is analytic on C∖[1,∞), so W_σ(z) → Li_{−σ}(−1)/(−1) = η(−σ) = (1−2^{1+σ})ζ(−σ)
as z → −1⁺. The real zeros of ζ on the negative axis are exactly −2,−4,…, and ζ(−3) = 1/120 > 0, ζ(−7) = 1/240 > 0,
so ζ(−σ) > 0 on (2,4) ∪ (6,8) ∪ …; thus η(−σ) < 0 and the IVT gives z_0. For C = G/W_σ with G(z_0) ≠ 0, the radius
of convergence of C is ≤ |z_0| < 1. Integer σ = n: W_n = A_n(z)/(1−z)^{n+1} with A_n the Eulerian polynomial, which is
palindromic with n−1 simple negative real roots (Frobenius); for n ≥ 3 they come in pairs r, 1/r with r ≠ −1, so
one root lies in (−1,0) (n = 3: −2+√3; n = 4: −(5−2√6)).
(b) (1−z)²W_σ = Σ e_i z^i with e_0 = 1, e_i = (i+1)^σ − 2i^σ + (i−1)^σ (i ≥ 1). For 1 < σ < 2, e_i > 0 (convexity), e_i → 0, and
e_i strictly decreases for i ≥ 1: for i ≥ 2, e_i − e_{i+1} = −Δ³(x^σ) on [i−1,i+2] ⊂ [1,∞), where (x^σ)''' < 0 (mean
value theorem); and e_1 − e_2 = 3·2^σ − 3 − 3^σ > 0 because it vanishes at σ = 1, 2 and has second derivative
3(ln2)²2^σ − (ln3)²3^σ < 0 on [1,2]; e_0 ≥ e_1 = 2^σ − 2 iff σ ≤ log₂3. Then
(1−z)Σe_i z^i = e_0 − Σ_{i≥1}(e_{i−1}−e_i)z^i, the coefficients are ≥ 0 and sum to e_0, so the subtracted series has
modulus < e_0 for |z| < 1, and on |z| = 1 equality needs z^i = 1 for all i ≥ 2, i.e. z = 1. Near z = 1,
W_σ ~ Γ(1+σ)(1−z)^{−1−σ}, so 1/W_σ → 0; hence 1/W_σ is continuous on the closed disc, its Taylor coefficients are
square-summable, hence bounded, and c = (1/W_σ) * G is bounded for G ∈ ℓ¹. (c) direct. ∎
NUMERICAL (code/C/zigzag.py): for v ∈ {0.2, 0.35, 0.45} no zeros in |z| ≤ 0.99 (argument principle, 4000 points) and
η(−σ) > 0; growth factors per leg 1/|z_0| = 1.421, 2.078, 3.188, 5.276, 9.899, 23.20 for v = 0.55, 0.6, 0.65, 0.7,
0.75, 0.8 (v = 0.75, 0.8 agree with the Eulerian roots 5+2√6 and the root −0.0431 of A_5). Direct iteration of
(Lin) with random 1e−12 data reproduces the same factors to 4 digits. The case 0.369 < v < 1/2 is NUMERICAL only.

**Nonlinear check (NUMERICAL, code/C/zigzag_check.py).** In the exact nonlinear discrete chase, the turning angles
after the corner turn (θ* = arccos(−v)) alternate in sign from the first legs for v ≥ 0.55 and not at all for
v ≤ 0.5; the measured mean growth per leg over the linear phase (|turn| < 0.3) is 1.46–1.47 (v = 0.55, pred. 1.42),
2.31–2.32 (0.6, pred. 2.08), ≈3.9 (0.65, pred. 3.19), ≈ 6.5–9 over the first 3 legs (0.7, pred. 5.28), at N = 1000 and
4000 (independent of N, as predicted). The excess over the prediction is consistent with the non-uniform spacing
near the corner (ρ_i ∝ i^{1−v}). At v = 0.6 the turns saturate near ±1.8 rad and the chase loses the front (T = NaN);
at v = 0.55 the chase still ends but at T ≈ 214 (N=1000), 233 (N=4000), versus ≈ 60 expected by interpolation.
**Conclusion:** the brief's "exact-contact discrete chase is unstable for v > 0.5" is exactly this linear zigzag
instability with threshold κ = 1 ⇔ v = 1/2; it is a property of the head-on discretisation (first-kind Volterra
inversion of order 1 + 1/(1−v) by a rectangle rule), not evidence against capture. A consequence for proofs: for
v > 1/2, Lemma 4 cannot be fed by the head-on discrete chase; a stable discretisation is needed (§7).

