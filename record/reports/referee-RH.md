# Referee report RH: stream H (Lemma H1, Prop. H2, §3.1, Theorem H3, Prop. H4) and stream C (Prop. C6)

Referee: independent, adversarial. Inputs read: `BRIEF.md` §1–3, `paper/main.tex`, `referee/H-claims.md` only
(not `reports/H-1.md`, `reports/C-1.md` or `code/H`, `code/C`). Every step below was re-derived by hand; every
number was recomputed with my own scripts in `code/referee/RH/` (outputs saved next to each script as `*.out`).
Commands (PowerShell, from `code/referee/RH/`, `$env:OPENBLAS_NUM_THREADS=1`):
`python rh_zeros.py`, `python rh_recursion.py`, `python rh_recursion_fft.py`, `python rh_gammainc.py`,
`python rh_linearization.py`.

## 0. Summary of verdicts

| Claim | Verdict | One line |
|---|---|---|
| Lemma H1 (Lipschitz heading ⇒ head-on capture) | **OK** (scope remark) | Proof checked line by line; needs unit speed near τ (or speed ≥ s0 > v), and does not apply to the speed-≤1 limit paths of Lemma 6 (compactness). |
| Prop. H2, derivation of (L) | **OK** as a formal first variation; **GAP** only in the label: the Gateaux-derivative step can be made rigorous in a few lines (fix in §2.2) | My independent nonlinear backward integration agrees with (L) to relative error O(ε²) (5e-6, 5e-8, 5e-10 for ε = 1e-2, 1e-3, 1e-4). |
| Prop. H2 (a) order of loss, (b) analytic well-posedness, (c) evolution form | **OK** (minor fix in (b)) | (b): replace sup over \|X\| = R by \|X\| = R'' < R. Relevance caveat: the actual Γ is not analytic at the tip (§3.1). |
| §3.1 contact-point shape F = cX^{2a} | **OK** at leading order | Exact (C,h) computation: local exponent → 2a to 6 digits for v = 0.3, 0.5, 0.7; c > 0. |
| Theorem H3 (zeros of W in the disk = ⌊a/2⌋) | **OK** | Argument principle re-done; three independent numerical counts agree for 31 values of a incl. a = 2 ± 1e-4, 4 ± 1e-3, 6 ± 1e-2. |
| H3(2) "stable for v < 1/2" | **OK as stated** (x_n → 0); **GAP** in the interpretation "errors not amplified", which needs x ∈ ℓ¹ — true, fix in §4.3 (x_n ~ n^{-1-a}/(Γ(a)Γ(-a))) | ‖x‖₁ = 3.11, 6.33, 20.1, 43.4, 90.2, 465 for a = 1.2, 1.5, 1.8, 1.9, 1.95, 1.99: finite but ∝ 1/(2−a) as v → 1/2. |
| H3(3) marginal at v = 1/2; H3(4) one real zero in (−1,0) for 1/2 < v < 3/4 | **OK** | z0 and growth factors reproduced to 5 digits. |
| §4 "the discrete chase is collocation of (L)" | **OK** as an exact statement about the linearisation about the uniform radial state | Nonlinear discrete chase on a perturbed ray agrees with (R) to relative O(ε²) (e.g. 1e-7 at ε = 1e-8, v = 0.6, 13 legs). |
| Prop. H4 formula and Routh–Hurwitz verdicts | **OK** | Σ(λ) identity checked by quadrature; e_2,e_3,e_4 Hurwitz, e_5,e_6,e_7 not. |
| Prop. H4 "unstable **iff** Γ(a+1,s) has a zero with Re s > 0" | **GAP** ("only if" not proved) | Fix in §6.2. |
| v* ≈ 0.78 | **OK (NUMERICAL)** | a* = 4.54538943598, ω* = 2.85252555945, v* = 0.779996848656. |
| Prop. C6 (a), (c) | **OK** | |
| Prop. C6 (b) (stable for v ≤ 0.369) | **OK but superseded** | Correct, weaker than H3(2). No inconsistency: H3 proves all v < 1/2; C's "0.369 < v < 1/2 NUMERICAL only" can be upgraded to PROVED by citing H3. |
| H's closing sentences ("that is the controller, not the mathematics"; "well-posed for every v < 1") | **CONJECTURE**, not a result | Nothing proved about the nonlinear continuous sweep. |

The dividing line (detailed in §7): **everything proved concerns linear models** — (L), its collocation (R), and the
delay model (E). The link "linear model ⇔ true nonlinear chase" is (i) a first variation that is rigorous-able
(fix below) and checked numerically to O(ε²) about a *straight-ray* base state, and (ii) a frozen-coefficient
heuristic for the actual chase, whose base state is *not* a uniformly spaced ray. No statement about capture or
non-capture for the original problem follows from H or C.

---

## 1. Lemma H1 — OK

Setting: unit speed, heading u = (cos φ, sin φ) with |φ'| ≤ K a.e. near τ; ρ > 0 on [t1, τ), ρ → 0.

Step check.
* φ_r' = (r × r')/ρ², r' = v r̂ − u, r × r̂ = 0, r × u = ρ sin(φ − φ_r) = −ρ sin β, so φ_r' = sin β/ρ and
  β = φ_r − φ gives ρβ' = sin β − ρφ'. ρ' = r̂·r' = v − cos β. ✔ (numerically on a curved path: residuals 4e-6, 1e-6,
  finite-difference level; `rh_linearization.py` Part 4).
* ρ' ≥ v − 1 for any path ⇒ ρ(t) ≤ (1−v)(τ−t) ⇒ ∫^τ dt/ρ = ∞. ✔
* On B = {δ/2 ≤ |β| ≤ π − δ/2}, sin|β| ≥ sin(δ/2) and Kρ < sin(δ/2)/2, so |β|' ≥ sin(δ/2)/(2ρ) > 0 a.e. ✔
  (|β| is absolutely continuous on B because B avoids β = 0 and β = π where |·| and the branch cut act.)
* (i) a downward crossing of [δ/2, δ] ⊂ B is impossible (take the last time |β| = δ). ✔
  (ii) staying in [δ, π−δ/2] contradicts ∫ dt/ρ = ∞. ✔ (iii) [π−δ, π−δ/2] ⊂ B because δ < π/2; then
  ρ' ≥ v + cos δ > 0 contradicts ρ → 0. ✔

Scope remarks (not errors):
1. Unit speed is used in two places (sin β coefficient, ρ' = v − cos β). With speed s(t) ≤ 1 the same proof works
   if s ≥ s0 > 0 near τ (ρβ' = s sin β − ρφ', so replace sin(δ/2) by s0 sin(δ/2) in r*; in step (iii)
   ρ' = v − s cos β ≥ v > 0 still). Without a positive lower speed bound near τ the proof does not go through.
2. Only Lipschitz continuity of φ on a left neighbourhood of τ is needed; corners before that are harmless.
3. It does **not** apply to the limit path produced by the compactness Lemma (`main.tex` Lemma 6): that path is only
   1-Lipschitz, may have speed < 1 and no Lipschitz heading. So H1 cannot be used to say that the eventual capturing
   path catches head-on.
4. The remark "in backward time β ≈ 0 is attracting" is correct and is exactly what makes the backward integration in
   §2 well conditioned (backward error damping factor (η/τ)^μ).

## 2. Proposition H2 and the derivation of (L)

### 2.1 The derivation — checked, correct
Base state: H(s) = (s,0), candidate caught at τ starts at ((1−v)τ, 0) (paper Prop. 3). Perturbation: heading εθ(s),
H_y = εη, η' = θ. With r_y = εw: S_y' = ε(θ + w') and S_y' = v r_y/ρ = εvw/ρ. The longitudinal error is O(ε²)
*relatively and uniformly up to capture*: ρ' = v − cos β with β = O(ε), so ρ = (1−v)(τ−s)(1 + O(ε²)) and
v/ρ = μ/(τ−s)·(1 + O(ε²)). Hence w' = −θ + μw/(τ−s), w(τ) = 0 bounded; homogeneous solutions c(τ−s)^{−μ}, unique
bounded solution w(s) = (τ−s)^{−μ}∫_s^τ(τ−σ)^μθ. (Direct differentiation confirms it.) Near capture
w ≈ θ(τ)(τ−s)/a, so r_y/ρ → εθ(τ)/(a(1−v)) = εθ(τ): the relative position is aligned with the heading at capture,
consistent with H1. At s = 0, S_y(0) = εw(0) (η(0) = 0) gives
τ^μ F((1−v)τ) = ∫_0^τ (τ−s)^μ θ(s) ds = Γ(a) I^aθ(τ). ✔

**Independent numerical check** (`rh_linearization.py` Part 1). θ(s) = sin 3s + s² − 1/2 + 0.3 cos 7s (different from
H's test function); exact nonlinear ODE for (H,S) integrated *backwards* from τ − η (η = 1e-6, start on the heading
ray at distance (1−v)η), DOP853 rtol 1e-13:

| v | τ | rel. err of y(0)/ε vs F_lin, ε = 1e-2 / 1e-3 / 1e-4 | \|x(0) − (1−v)τ\| |
|---|---|---|---|
| 0.3 | 0.7 | 5.3e-6 / 5.3e-8 / 5.3e-10 | 3e-6 / 3e-8 / 3e-10 |
| 0.3 | 1.5 | 1.2e-5 / 1.2e-7 / 1.2e-9 | 2e-5 / 2e-7 / 2e-9 |
| 0.6 | 0.7 | 4.5e-6 / 4.5e-8 / 4.6e-10 | 1e-6 / 1e-8 / 1e-10 |
| 0.6 | 1.5 | 1.6e-5 / 1.6e-7 / 1.6e-9 | 1e-5 / 1e-7 / 1e-9 |
| 0.8 | 0.7 | 6.8e-6 / 6.8e-8 / 6.2e-10 | 3e-7 / 3e-9 / 3e-11 |
| 0.8 | 1.5 | 2.0e-5 / 2.0e-7 / 2.0e-9 | 4e-6 / 4e-8 / 4e-10 |

The error is O(ε²) (not O(ε)) because the problem is odd under θ → −θ, y → −y; the longitudinal shift is O(ε²)
as claimed. So the linearisation is right, including the singular coefficient at capture.

### 2.2 GAP (labelling only) and fix: rigorous first variation
H labels the identification "(L) is the Gateaux derivative" NUMERICAL. It can be PROVED along these lines (I checked
each inequality; write σ = τ − s, φ = εθ, ‖θ'‖∞ = K1):
1. Backward bearing equation: dβ/dσ = −sin β/ρ + εθ'(τ−σ), with β → 0 as σ → 0 (H1). Since ρ ≤ (1−v)σ and, while
   |β| ≤ π/2, sin|β| ≥ (2/π)|β|: d|β|/dσ ≤ −(2/π)|β|/((1−v)σ) + εK1, whence |β(σ)| ≤ εK1σ (comparison with the
   linear ODE; the bound keeps |β| ≤ π/2 for ε small).
2. Then dρ/dσ = cos β − v = (1−v) + O(ε²σ²), so ρ = (1−v)σ(1 + O(ε²)).
3. The exact transverse equation is S_y' = v sin ψ = v r_y/ρ (exact) and H_y' = sin(εθ) = εθ + O(ε³). With
   r_y = εw: w' = −θ + μ w/(τ−s) + e(s), |e| ≤ Cε²(‖θ‖³∞ + |w|/(τ−s)), and |w|/(τ−s) ≤ (1−v)(|β|+ε|θ|)/ε is
   bounded by steps 1–2. The variation-of-constants formula with the bounded-solution selection (the homogeneous
   solution (τ−s)^{−μ} is excluded by w(τ) = 0; the propagator ((τ−σ)/(τ−s))^μ ≤ 1 on s ≤ σ) gives
   |w − w_lin| ≤ Cε²τ, uniformly on [0,τ].
Uniqueness of "the candidate caught at τ" also follows: two such backward solutions both satisfy step 1, and their
difference obeys the same contracting backward equation. With this, (L) is the Fréchet derivative (in C¹ heading
perturbations) of the catch map at the straight run; the label can become PROVED.

### 2.3 H2 (a), (b), (c) — OK
(a) Laplace/convolution: L[s^μ] = Γ(a)p^{−a}. Monomials: ∫_0^τ(τ−s)^μ s^q ds = B(a,q+1)τ^{a+q} ⇒
F(X) = B(a,q+1)(X/(1−v))^{q+1}; slope/heading ratio (q+1)B(a,q+1)/(1−v) = Γ(a+1)Γ(q+2)/Γ(q+a+1) ~ Γ(a+1)q^{−μ}. ✔
Note that the order-a derivative acts on τ^μF((1−v)τ), not on F; locally (away from τ = 0) the loss is exactly a.
(b) Termwise inversion: θ-coefficient f_n(1−v)^nΓ(n+a)/(Γ(a)Γ(n)), radius |X| < R. ✔ Uniqueness by Titchmarsh. ✔
*Minor fix*: the bound "sup_{|X|≤R'}|θ| ≤ C sup_{|X|=R}|F|" presumes F is bounded on the closed disk; state it with
|X| = R'' for any R' < R'' < R.
*Relevance caveat*: the actual data is not analytic at the tip (F = cX^{2a}+…, generalised powers, §3.1). The
generalised-power version (each X^p, p > 0, matched by τ^{p−1} with a finite non-zero multiplier) is correct, but
"well-posed in analytic classes" is about a class the real wavefront does not belong to.
(c) Along characteristics X = (1−v)(τ−t): d/dt F = −θ + μ(1−v)F/X = −θ + vF/X, i.e.
∂_tF = (1−v)∂_XF + vF/X − θ. ✔ θ = ∂_XF(t,0) from w ≈ θ(τ)(τ−s)/a. ✔ Tip: O(1) terms cancel; O(X) gives
θ' = (2−v)c. ✔ (Requires F(t,·) ∈ C² at X = 0, true when θ is smooth.)

## 3. §3.1 contact-point shape — OK (leading order)
h/C = −(1−cos α)/g(α) ~ −α^{1+v}/2^{1+v}; β − θ* = (h/C)/k'(θ*) with k'(θ*) = −(1−v²)/(g(θ*)sin θ*) (from
eq. (Fprime) with c = v) gives the stated positive coefficient; ρ ~ 2^v α^{1−v}/g(θ*); hence
F = ρ sin(β − θ*) ∝ ρ^{2a}, since (1+v)/(1−v) + 1 = 2a. ✔
Numerical (`rh_linearization.py` Part 3; exact (C,h) inversion at 60 digits, α from 1e-2 to 10^{-7.5}): local exponent
of F vs X → 2.857143, 4.000000, 6.666667 for v = 0.3, 0.5, 0.7 (= 2a), with F/X^{2a} → 0.1940, 0.02706, 5e-5 > 0.
The consequence θ = θ* + c'τ^{2a−1}, c' = c(1−v)^{2a}Γ(3a)/(Γ(a)Γ(2a)) is the monomial formula with q = 2a − 1. ✔
(It is a statement about (L) linearised about the *tangent ray of the + branch*; valid for small τ only.)

## 4. Theorem H3 — OK (with the ℓ¹ addendum)

### 4.1 Proof check
* Σ_k w_k z^k = (1/a)(Li_{−a}(z)/z − Li_{−a}(z)) = (1−z)Li_{−a}(z)/(az). ✔
* Jonquière with s = −a: Li_{−a}(e^{iφ}) = Γ(1+a)(2π)^{−1−a}[e^{iψ}ζ(1+a,λ) + e^{−iψ}ζ(1+a,1−λ)]. ✔ (my check vs
  `mpmath.polylog`: max rel. error 1.8e-15 at 24 points, a ∈ {1.3, 2.5, 3.7, 5.2}.)
* arg(1 − e^{iφ}) = (φ−π)/2 ∈ (−π/2, π/2), so the principal branch of (1−z)^{a+1} is continuous on the circle minus 1. ✔
* arg G = (a+1)(φ−π)/2 + ψ + arg(P + Qe^{−iπ(1+a)}) − φ = (a−1)φ/2 + arg(P + Qe^{iχ0}). ✔
  χ0 ∈ (−π, π) ⇔ a/2 < m < a/2 + 1 ⇔ m = ⌊a/2⌋ + 1 (a not even). ✔ Non-antipodal positive combination never
  vanishes, argument confined to the short arc. ✔ Total change (a−1)π + χ0 = 2π(m−1) = 2π⌊a/2⌋. ✔
* Continuity of G at z = 1 inside the closed disk: Li_{−a}(z) = Γ(1+a)(−log z)^{−1−a} + (analytic in |log z| < 2π),
  and ((1−z)/(−log z))^{a+1} → 1 with both bases in the right half-plane, so G(1) = Γ(1+a)/a = Γ(a). ✔ The argument
  principle for a function continuous on the closed disk, analytic inside, zero-free on the circle (limit r ↑ 1). ✔
* Even a: P = Q at λ = 1/2 and e^{iχ} = −1 ⇒ W(−1) = 0; since ζ(1+a,·) is strictly decreasing this is the only
  boundary zero. ✔
* (3) Li_{−2} = z(1+z)/(1−z)³ ⇒ 1/W = 2(1−z)²/(1+z) = 2, −6, 8, −8, … ✔ (recursion output identical).
* (4) count 1 ⇒ simple; real by conjugate symmetry; W > 0 on [0,1) ⇒ z0 ∈ (−1,0); 1/W − A/(z−z0) in the disk
  algebra ⇒ x_n = −(A/z0)z0^{−n} + o(1). ✔ Independent sign check: W(−1) ∝ η(−a) = (1−2^{1+a})ζ(−a) < 0 on (2,4). ✔

### 4.2 Numerical verification (`rh_zeros.py`)
Three independent counts of zeros of W in the disk, 31 values of a:
(A) winding of G on |z| = 1 via the Hurwitz formula (≈4·10^5 points, refined near φ = 0, π, 2π, including the point
G(1) = Γ(a)); (B) winding on |z| = r for r = 0.99 and 0.999 from the **raw power series** (coefficients of
(1−z)^{⌈a⌉+1}Li_{−a} computed in 50-digit arithmetic, evaluated exactly at 2^17 points by folding + FFT — no polylog
formula involved); (C) Newton/bisection on mpmath.polylog.

| a | v | ⌊a/2⌋ | (A) \|z\|=1 | min\|G\| on circle | (B) r=0.99 | (B) r=0.999 |
|---|---|---|---|---|---|---|
| 1.05, 1.2, 1.5, 1.8, 1.9 | ≤0.474 | 0 | 0 | ≥ 0.086 | 0 | 0 |
| 1.99, 1.999, 1.9999 | 0.4975–0.49997 | 0 | 0 | 8.5e-3, 8.5e-4, 8.5e-5 | 0 | 0 |
| 2.0001 | 0.50002 | 1 | 1 | 8.5e-5 | 0 | 0 |
| 2.001 | 0.5002 | 1 | 1 | 8.5e-4 | 0 | 1 |
| 2.01, 2.1, 2.5, 3, 3.5, 3.9, 3.99, 3.999 | | 1 | 1 | | 1 | 1 |
| 4.001 | 0.7501 | 2 | 2 | 2.0e-3 | 1 | 1 |
| 4.01 | 0.7506 | 2 | 2 | 2.0e-2 | 1 | 2 |
| 4.5, 5, 5.5, 5.99 | | 2 | 2 | | 2 | 2 |
| 6.01 | 0.8336 | 3 | 3 | 0.16 | 2 | 3 |
| 6.5, 7, 7.5 | | 3 | 3 | | 3 | 3 |
| 8.5, 9.5 | | 4 | 4 | | 4 | 4 |
| 10.5 | 0.905 | 5 | 5 | | 5 | 5 |

All (A) counts equal ⌊a/2⌋. The (B) shortfalls occur only just above an even integer, where the new zero sits near
z = −1 outside |z| < r (e.g. a = 2.0001: z0 ≈ −1 + O(1e-4)); they disappear as r ↑ 1, exactly as the theorem predicts.
min|G| on the circle → 0 linearly in |a − 2k| (the boundary zero at z = −1 for even a).

(C) Zeros located with mpmath (30 digits): no real zero in (−1,0) for v = 0.45, 0.49; z0 = −0.9932 (v = 0.501),
−0.933754 (0.51), −0.871254 (0.52), −0.703934 (0.55), −0.481218 (0.6), −0.313703 (0.65), −0.267949 = −2+√3 (2/3),
−0.18954 (0.7), −0.116142 (0.74), −0.101021 = −5+2√6 (0.75); two real zeros −0.852376, −0.087119 at v = 0.76 and
−0.430575, −0.043096 at v = 0.8 (Eulerian A_5). Newton from a 48-point grid finds no other zeros in |z| < 0.999: for
a = 4.5, 5, 5.5 the two zeros are both real negative, for a = 6.5 three real negative zeros (−0.0133, −0.1630, −0.7187).
H's table (z0 and 1/|z0|) is reproduced to all printed digits.

### 4.3 GAP in the interpretation of H3(2), and the fix
H3(2) proves x_n → 0. "Errors are not amplified from step to step" for a *stream* of per-step errors δ_m (rounding,
discretisation) needs Σ|x_n| < ∞; x_n → 0 alone allows an accumulated error growing like Σ_{n≤N}|x_n|.
**Fix (PROVED by standard singularity analysis):** for 1 < a < 2, W is analytic in C \ [1,∞) and zero-free on the
closed disk minus {1}, with W ~ Γ(a)(1−z)^{−a} at 1; by compactness W is zero-free in a Δ-domain at 1, and
from Li_{−a}(z) = Γ(1+a)(−log z)^{−1−a} + ζ(−a) + O(log z),
1/W = (1−z)^a/Γ(a) + O(|1−z|^{a+1}) + O(|1−z|^{2a}) in that Δ-domain, so by the Flajolet–Odlyzko transfer theorem
x_n ~ n^{−1−a}/(Γ(a)Γ(−a)), hence x ∈ ℓ¹.
Numerically (`rh_recursion_fft.py`, Taylor coefficients of 1/W from boundary values, 2^22-point FFT, agreeing with the
recursion to ≤ 2e-7): n^{1+a}|x_n| → 0.4775 (a = 1.5; predicted 1/(Γ(1.5)Γ(−1.5)) = 0.4775), 0.3368 (a = 1.8;
predicted 0.3368), 0.1865 (1.9), 0.0957 (1.95). ‖x‖₁ = 3.114, 6.334, 20.06, 43.38, 90.22, 465.5 for
a = 1.2, 1.5, 1.8, 1.9, 1.95, 1.99: finite, but blowing up like 1/(2 − a) as v ↑ 1/2 (a transient zigzag from the
zero of W just outside z = −1). So the head-on chase is stable for v < 1/2 with a stability constant that degenerates at
v = 1/2. (Note: the plain float recursion of length 6000 accumulates rounding error ~1e-16·n^a and shows spurious
tail growth for a ≥ 1.8 — use the FFT route for tails.)

### 4.4 Growth factors for a > 2 (`rh_recursion.py`)
|x_n/x_{n−1}| at n = 60 and 100: 1.07095 (v = 0.51), 1.42059 (0.55), 2.07806 (0.6), 3.73205 (2/3), 5.27592 (0.7),
8.61011 (0.74), 23.20385 (0.8), all with strictly alternating sign: identical to H's table and to C's numbers.

## 5. "The discrete chase is collocation of (L)" — what it exactly means

**Exact meaning.** Take the base state "Harry runs along a ray; candidates lie on the ray at time 0 at uniform
longitudinal spacing (1−v)h". Perturb transverse offsets by εF_n. The discrete chase uses a constant heading θ_j on
((j−1)h, jh] and catches candidate j at jh. Because (L) holds *exactly* (to first order) for any heading function,
evaluating it at τ_n = nh with a piecewise-constant θ gives (R) with w_k = ((k+1)^a − k^a)/a — no quadrature error:
(R) is the product-integration / piecewise-constant collocation of the first-kind Volterra equation (L) at the right
end points (collocation parameter c = 1). Equivalence with C's (Lin): summation by parts with c_j = θ_j − θ_{j−1}
turns Σ w_{n−j}θ_j into (1/a)Σ(n−j+1)^a c_j, i.e. C's kernel; spacing normalisations agree
(a·h^{−a}(nh)^μ = n^μ for (1−v)h = 1). Numerically a·cumsum(c) = x to 1e-13 (`rh_recursion.py`).

**Nonlinear check (new, `rh_linearization.py` Part 2).** Exact nonlinear discrete chase (each leg straight at the
target, the target moving along the forward ray, other candidates integrated with DOP853 rtol 1e-13), candidates at
((1−v)n, εF_n):

| v | data | legs | max rel. dev. of θ_NL/ε from (R): ε = 1e-6 / 1e-8 | last ratio NL vs lin (ε = 1e-8) |
|---|---|---|---|---|
| 0.4 | impulse / sin(0.7n) | 13 | 2e-11 / 3e-9 ; 1e-11 / 6e-10 | 0.7071 / 0.7071 |
| 0.6 | impulse / sin(0.7n) | 13 | 1e-3 / 1e-7 ; 1e-7 / 8e-8 | 2.0781 / 2.0781 |
| 0.7 | impulse / sin(0.7n) | 8 | 0.14 / 2e-5 ; 3e-4 / 6e-8 | 5.2758 / 5.2759 |
| 0.8 | impulse / sin(0.7n) | 6 | 0.97 / 0.05 ; 0.64 / 4e-4 | 22.04 / 23.21 |

Deviations shrink like ε² until the amplified perturbation leaves the linear regime (large deviations at ε = 1e-6
are nonlinear saturation after a growth of 5.3^8 or 23^6). So (R) is the correct linearisation of the nonlinear
discrete chase about the uniform radial state.

**What is proved vs numerical.**
* PROVED (given §2.2): for any fixed number n of legs, the nonlinear discrete chase near the uniform radial state is a
  smooth finite-dimensional map whose derivative is (R); hence for v > 1/2 and any n there is ε0(n) such that a
  perturbation of size ε < ε0(n) is amplified by ≈ (1/|z0|)^n with alternating sign. This is a finite-time linear
  instability statement.
* NOT proved: (i) instability of the actual chase, which starts at the contact point with non-uniform spacing
  (ρ_i ∝ i^{1−v}), a curved Γ and finitely many candidates — this uses (R) as a frozen-coefficient model (C's measured
  1.46, 2.31, 3.9 vs predicted 1.42, 2.08, 3.19 shows the model is indicative, not exact); (ii) any nonlinear stability
  for v < 1/2 (linear stability of (R) with constant ∝ 1/(1−2v) does not control the nonlinear chase over the
  unbounded number of legs N → ∞ without an extra argument); (iii) anything about capture: an unstable discretisation
  is not an obstruction, and a stable linearisation is not a capture proof.

## 6. Proposition H4 — formula OK, "iff" has a GAP, threshold confirmed

### 6.1 Checks
* (E): pointing at the candidate caught at t+δ if Harry kept θ(t) constant gives, by (L),
  (t+δ)^μF = ∫_0^t(t+δ−s)^μθ + θ(t)δ^a/a. ✔
* By parts and y = λ(δ+x): Σ(λ) = (λ/a)∫_0^∞(δ+x)^a e^{−λx}dx = (1/a)e^{λδ}λ^{−a}Γ(a+1,λδ), Re λ > 0. ✔ Quadrature
  check at three complex λ: rel. errors 3e-17, 6e-9, 6e-18 (`rh_gammainc.py`).
* Γ(n+1,s) = n!e^{−s}e_n(s). Roots of e_n: max Re = −1, −0.70196, −0.27056 (n = 2,3,4), +0.23981, +0.80361, +1.40659
  (n = 5,6,7). This is the classical fact that the Taylor sections of e^s are Hurwitz iff n ≤ 4. ✔
* Argument-principle counts of zeros of e^sΓ(a+1,s) in {Re s > 0, |s| < 40} (mpmath, 9000 contour points): 0 for
  v = 0.70, 0.72, 0.74, 0.75, 0.76, 0.77, 0.775; 2 for v = 0.78, 0.785, 0.79, 0.80, 0.82, 0.84, 0.85.
* Threshold, solving Γ(a+1, iω) = 0 for real (a, ω) directly: **a* = 4.54538943598, ω* = 2.85252555945,
  v* = 0.779996848656** (H: 4.54539, 2.855, 0.779997 ✔). Note v = 0.78 (a = 4.54545) is just above threshold.
* Tracked rightmost zero, rate·ε = Re(s)(1−v): −0.06764 (0.75), −0.02308 (0.77), +0.02368 (0.79), +0.04796 (0.80),
  +0.09855 (0.82); period/ε ≈ 10.01–10.04. All match H's "continuum prediction" column.

### 6.2 GAP: the "only if" direction, and the fix
"If" is proved: a zero s0 with Re s0 > 0 gives a homogeneous exponential solution and a pole of 1/Σ in the right
half-plane. "Only if" (no such zero ⇒ no exponential growth) is asserted, not proved. The kernel k(x) = (δ+x)^μ is not
in L¹, so the standard Paley–Wiener theorem for Volterra equations does not apply as is. Fix: write the solution of
(E) as θ̂ = f̂/Σ and invert on Re λ = γ > 0. Since Σ(λ) ~ δ^a/a + δ^μ/λ + … as |λ| → ∞ in Re λ ≥ γ and
Σ(λ) ~ Γ(a)λ^{−a} → ∞ as λ → 0, 1/Σ is bounded on Re λ ≥ γ for every γ > 0 when there are no zeros there;
the inverse transform then grows at most like e^{γt} for every γ > 0, i.e. subexponentially. That gives
"no exponential instability iff no zero in Re s > 0" (zeros on the imaginary axis, which occur only at a = a*, give
marginal oscillation). This should be written out or the claim weakened to "if".
Also: the identification of the brief's discrete greedy controller with (E) is (correctly) labelled NUMERICAL by H.

### 6.3 Interpretive claims — CONJECTURE
"That is the controller, not the mathematics" and "the linearisation of the continuous ε = 0 sweep is well-posed in
analytic classes for every v < 1" do not imply that any nonlinear sweep exists for v ≥ 0.78 (or for any v): the data is
non-analytic at the tip, the evolution form (c) has a non-local feedback whose nonlinear well-posedness is open, and
the analytic radius is consumed as the sweep proceeds. These are reasonable conjectures, not results.

## 7. Prop. C6 and consistency with H3

* C6(a) ✔: W_σ(0) = 1, W_σ(−1⁺) = η(−σ) = (1−2^{1+σ})ζ(−σ) < 0 where ζ(−σ) > 0, i.e. σ ∈ (2,4) ∪ (6,8) ∪ …; IVT.
  Integer σ via Eulerian polynomials (palindromic, simple negative roots) ✔. For σ ∈ (4,6), (8,10), … C's IVT gives
  nothing, but H3 still gives ⌊σ/2⌋ ≥ 2 zeros — numerically a pair of real negative zeros (two sign changes, so the
IVT at z = −1 cannot see them; see §4.2(C)). So H3 extends C6(a) to every σ > 2.
* C6(b) ✔: e_i second differences, e_i ↓ for 1 < σ < 2 (third derivative < 0; e_1 − e_2 > 0 checked), e_0 ≥ e_1 iff
  σ ≤ log₂3; Kakeya–Eneström-type bound; boundary equality only at z = 1. Correct but restricted to v ≤ 0.369 because
  of the e_0 ≥ e_1 requirement of the monotone-coefficient method.
* C6(c) ✔.
* **Consistency.** (Lin) and (R) are the same linear system (summation by parts, §5), so the two propositions concern
  the zeros of the same function Li_{−a}(z)/z. There is **no contradiction**: C6(b) is a weaker, correct sufficient
  condition; H3(2) proves zero-freeness for all 1 < a < 2 by the argument principle, which I re-derived and verified
  (zero count 0 for a = 1.05 … 1.9999 by three methods). The answer to "which is right?" is: both; H3 is sharp, and
  C's "0.369 < v < 1/2 is NUMERICAL only" should be upgraded to PROVED by citing H3 (with the ℓ¹ addendum of §4.3 if
  one wants bounded responses to persistent errors; C's own ℓ^∞ argument via square-summable coefficients also works
  once zero-freeness is known).

## 8. Recommended edits before anything enters the main document
1. H2: replace "NUMERICAL" for the Gateaux identification by the short proof of §2.2 (or keep NUMERICAL and cite both
   checks). Fix the sup in (b). Add the caveat that real data is not analytic at the tip.
2. H3(2): add x ∈ ℓ¹ with x_n ~ n^{−1−a}/(Γ(a)Γ(−a)) (transfer theorem), and note ‖x‖₁ → ∞ as v ↑ 1/2.
3. H4: prove "only if" as in §6.2 or state only "if".
4. Throughout: say explicitly that (R) is the linearisation about a *uniformly spaced radial* state and that its use for
   the real chase is a frozen-coefficient heuristic; no capture/non-capture statement follows.
5. C6: cite H3 for 0.369 < v < 1/2.
