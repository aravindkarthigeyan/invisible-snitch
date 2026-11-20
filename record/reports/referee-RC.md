# Referee report RC: claims C0–C9 (tangent-vector stretching, Osgood form of the author's condition)

Referee: independent adversarial referee. Inputs: `BRIEF.md` §1–2, `paper/main.tex`, `referee/C-claims.md`,
and the author's note `refs/Epsilon_zero_results.txt` (to pin down what the author's quantity means). I did not read
`reports/C-1.md` or `code/C/`. All code is mine, in `code/referee/RC/`. Reproduce (PowerShell, `$env:OPENBLAS_NUM_THREADS=1`,
from that directory):

| script | what it tests | runtime | output |
|---|---|---|---|
| `python rc_tangent.py` | C0, C1, C2, C3, C4, C8 (variational ODE, DOP853, rtol 1e-12) | ~1 min | `rc_tangent.out` |
| `python rc_chase.py` | C5 (i)–(iii), C5b, ODE cross-check of the exact-map chase | ~2 min | `rc_chase.out` |
| `python rc_weight_argmax.py` | where the weighted C5 constant is attained; N up to 4096 | ~4 min | `rc_weight_argmax.out` |
| `python rc_later_catch.py` | one-sided wavefront quotient at later catches | seconds | `rc_later_catch.out` |
| `python rc_sweep_osgood.py` | C9 (greedy ε-sweep), C5a (model recursion) | ~10 s | `rc_sweep_osgood.out` |

`snitchcore.py` implements the exact straight-run map from main.tex Prop. 1 / Lemma 1, written from scratch in the variable
s = ln tan(|β|/2), where g = sech(s)e^{−vs} and k = (v − tanh s)cosh(s)e^{vs}. It agrees with direct ODE integration to
about 1e-13 for ρ(α,t₀), and the chase built on it agrees with the ODE to about 1e-8. Throughout, d = 1.

## Verdicts

| claim | verdict | one line |
|---|---|---|
| C0 (restated) | OK | — |
| C3 component ODEs | OK | residuals ≤ 3e-9 on 60 random curved paths |
| C1 head-on law | OK | rel. error ≤ 1e-10 (v ≤ 0.9, ρ down to 1e-4ρ₀); backward-ray law ≤ 6e-13 |
| C2 | **GAP** (the statement is imprecise; the conclusion is true) | the formula is the trajectory limit; the author's quantity is the one-sided endpoint derivative, a different limit, also infinite |
| C4 | OK as mathematics; **GAP** in the interpretive sentence | its hypothesis is the trajectory stretch, not the author's endpoint quantity; its conclusion is averaged, not pointwise |
| C5 (i) | **GAP** (minor) | it silently assumes there are no accidental catches; re-index (fix below) |
| C5 (ii) | OK | monotonicity of f is essential (counterexample below) |
| C5 (iii) | OK | uniform in N exactly as Lemma 4 needs; speed ≤ 1, correctly stated |
| Remark C5a | OK for the model recursion (needs f continuous) | sharp only for what (i) and (ii) alone can give |
| Prop. C5b | OK; the attached numerical remark is **ERROR** (minor) | Q₀ ≍ α₁^{−v} exactly; "f = 0.4(1+t) works for v ≤ 0.5" fails as N → ∞ for v ≲ 0.34 |
| C8 | OK | all inequalities hold on random curved paths |
| C9 | OK | all hypotheses and conclusions hold in greedy sweeps; caveat on the (R1)/(R2) chord bound below |

---

## C0 and C3: OK

**Step check.** r̂' = (r' − (r'·r̂)r̂)/ρ = (−u + (u·r̂)r̂)/ρ = −(u_⊥/ρ) r̂⊥, and r̂⊥' = R₉₀ r̂' = (u_⊥/ρ) r̂.
Since J' ⟂ r̂, we get J_r' = J·r̂' = −J_t u_⊥/ρ and J_t' = J'·r̂⊥ + J·r̂⊥' = (vJ_t + J_r u_⊥)/ρ. Also
∂_αγ = (r̂ × J)/ρ = J_t/ρ, and d|J|/dt = (v/ρ)(|J|² − J_r²)/|J| = v|sinφ||J_t|/ρ. Everything is correct.

Regularity: H only Lipschitz is fine. The field is C^∞ in S away from H and continuous in t, so the flow is C¹ in the initial
data and J satisfies the variational equation; u = H' is needed only a.e. (it appears only in C3 and C8).

**Numerics** (`rc_tangent.py`, 60 random paths with |H'| ≤ 1, varying heading and speed, random v and α, ρ ≥ 0.26):
- max |J_r' − formula| = 2.7e-9 and max |J_t' − formula| = 1.1e-9 (both relative);
- max |γ_t + u_⊥/ρ| = 5.4e-9;
- max |d|J|/dt − v|sinφ||∂_αγ|| = 2.7e-10.

## C1: OK

On the forward ray u_⊥ ≡ 0, so J_r' = 0 and J_t' = vJ_t/ρ with ρ' = −(1−v), giving J_t ∝ ρ^{−κ}. The tan φ law, the |J|²
law and the log-integral follow. So does d ln|J|/d ln(ρ₀/ρ) = κ sin²φ. On the backward ray ρ' = 1+v, so J_t ∝ ρ^{v/(1+v)}.

**Numerics.**
- α = 0, H = (t,0), v ∈ {0.1, 0.3, 0.5, 0.7, 0.9}, down to ρ = 1e-6: J_r ≡ 0 and J_t/pred − 1 ≤ 2e-8. The worst case is
  v = 0.9, where κ = 9 and J ~ 1e54.
- 40 random (v ≤ 0.9, ρ₀, J₀): J_r and J_t laws and the log-integral identity hold to ≤ 1e-10.
- Backward ray: ≤ 6e-13.

**Numerical warning (not an error in the claim).** The forward ray is itself unstable: the off-ray angle grows like
ρ^{−1/(1−v)}. With an oblique u, a rounding error of 1e-16 in the initial position leaks J_t into J_r and gives errors of
order 1 by ρ = 1e-4ρ₀ at v ≈ 0.74. I therefore used u = e_x, which is legitimate by rotation equivariance. Anyone reproducing
C1 numerically must do the same.

## C2: GAP. The statement must say which limit it means

What is proved, and correct: for t < t₀, |∂_αS(0,t)| = d(d/(d−(1−v)t))^κ, with J_r ≡ 0, so it tends to ∞ as t ↑ t₀. This is
verified to ≤ 2e-8 (see C1).

The problem is that at t = t₀ the candidate α = 0 is at H(t₀) and its trajectory ends there, so ∂_αS(0,t₀) is not
defined. "The bound fails at t = t₀" therefore needs a definition, and there are two natural ones. They are **different
limits**:

1. **Trajectory limit**, lim_{t↑t₀} ∂_αS(0,t). This is what C2 computes. J becomes purely transverse (sin φ → 1).
2. **One-sided endpoint derivative of the wavefront**, lim_{α→0+} ∂_αS(α,t₀), or the difference quotient
   |S(α,t₀) − H(t₀)|/α. This is the author's meaning: in `Epsilon_zero_results` the unknown s lives on
   Ω = {α ≥ θ(t)}, and the initial front γ is "defined by continuous extension" at its end.

C2's proof does not cover meaning 2. It follows instead from main.tex Prop. 4: ρ(α,t₀) = d g(α)/g(β), with g(α) ~ 2^v α^{1−v}
and β → θ*. This gives

  |S(α,t₀) − H(t₀)|/α ~ (2^v d/g(θ*)) α^{−v}  and  |∂_αS(α,t₀)| ~ (1−v)(2^v d/g(θ*)) α^{−v}, both → ∞.

Here J becomes **radial**: sin φ → 0. Numerically (`rc_tangent.py`, α down to 1e-5, v ∈ {0.1, 0.3, 0.5, 0.7}) the ratio to
this asymptote is 1.000 and sin φ ≈ 3e-9 to 2e-6. So ∂_αS has no continuous extension to the corner (α,t) = (0,t₀). The
two limits have different directions and different rates (ρ^{−κ} in time versus α^{−v} in angle).

**Fix: replace the statement of C2 by the following.**
> (a) For t < t₀, |∂_αS(0,t)| = d(d/(d−(1−v)t))^κ → ∞ as t ↑ t₀.
> (b) At t₀ the wavefront's one-sided derivative at its endpoint is infinite: |∂_αS(α,t₀)| ~ (1−v)2^v d α^{−v}/g(θ*) as α → 0+.
>
> So under either reading, the author's bound |∂_αS(θ(t),t)| ≤ C(1+t) fails at t = t₀ (author's phase-2 time 0) for every
> v ∈ (0,1). The singularity in (b) is integrable in α (α^{−v} ∈ L¹). This is why it does not refute the strategy, only the
> unweighted bound; see C5b.

**On "the same holds at every catch of the discrete chase".** In meaning 1 this follows from C1. In meaning 2 it also holds
whenever J_t ≠ 0 at the start of the leg. The reason is a local version of Prop. 4: a neighbour at offset δ has
C ∝ δ^{1−v} and h_end = (1+v)J_r δ + O(δ²), so h/C ∝ δ^v → 0, β → θ*, and ρ ≍ δ^{1−v}. Checked in `rc_later_catch.py`
(N = 32, catches j = 3 and j = 10, δ down to 1e-11): the local exponents of the quotient converge to −0.200 / −0.400 for
v = 0.2 / 0.4. C2 should say which meaning it intends at each catch. Both are true.

## C4: mathematics OK; interpretive sentence GAP

**Step check.** ρ' = v − u·r̂ ≥ −(1−v) and ρ(t_c−) = 0 together give ρ(t) ≤ (1−v)(t_c − t). Then
ln|J(t)/J(s)| = v∫ sin²φ/ρ ≥ κ∫ sin²φ dτ/(t_c−τ). Both conclusions follow. Two points the proof uses silently, both true:
- J ≠ 0, because the variational flow is invertible and J(α,0) ≠ 0;
- |J| is nondecreasing, so limsup = lim.

**Numerics** (`rc_tangent.py`): 40 random lead-angle pursuits (H' = R_ψ r̂ with cos ψ > v, a curved catch at
t_c = ρ₀/(cos ψ − v)) and several start times s. The maximum of log(bound) − log|J| is 0.0: the bound is attained at τ = s and
never violated.

**GAP in "So any sweep for which the author's quantity is finite must catch each direction with the wavefront tangent
pointing at Harry."** Two problems:
1. C4's hypothesis is the trajectory limit (meaning 1 above), not the author's endpoint quantity (meaning 2). C2 shows these
   are different limits that need not agree.
2. The conclusion is ∫ sin²φ dτ/(t_c−τ) < ∞. That is an averaged (logarithmic-density) statement and gives liminf sin φ = 0,
   not sin φ → 0.

**Fix:** "If the trajectory stretch lim_{t↑t_c}|∂_αS(α,t)| is finite, then ∫^{t_c} sin²φ dτ/(t_c−τ) < ∞. In particular J is
asymptotically radial along a set of times of full logarithmic density." Drop "the author's quantity" unless one also proves
that ∂_αS extends continuously to the caught set. C2 shows it does not at t₀.

## Theorem C5

**(i) GAP (minor; fix written out).** The formula t_{N−1} = t₀ + (1−v)^{−1}Σ_{j≤N−2} Q_jΔ_j assumes every S_j is chased in
turn. main.tex allows accidental catches (skips). If S_{j+1} was caught during an earlier leg, then ℓ_j = |S_{j+1}(t_j) − H(t_j)|
is undefined, and t_{N−1} need not be the end time.

**Fix:** let 0 = j₀ < j₁ < … < j_K be the indices actually chased. Set Δ_m = α_{j_{m+1}} − α_{j_m} and
Q_m = |S_{j_{m+1}}(t_{j_m}) − H(t_{j_m})|/Δ_m. Then T_end = t_{j_K} = t₀ + (1−v)^{−1}Σ_m Q_mΔ_m, and Σ_m Δ_m ≤ α_{N−1} < 2π.
Statements (ii) and (iii) then hold verbatim with this indexing.

Numerically no skip ever occurred (legs = N−1 in every run), but near-collinear leg starts with |β| as small as 2e-5 do occur
(v = 0.35, N = 256). The identity itself holds to ≤ 1.4e-14 (`rc_chase.py`).

The underlying fact, that each leg takes ℓ/(1−v), was cross-checked by integrating every candidate with the ODE along the
exact-map path (v = 0.2, 0.4, 0.3; N = 8, 8, 16): ρ_target(t_j − δ)/((1−v)δ) − 1 ≤ 1.2e-8 with δ = 1e-4 × leg length.
Going closer to the catch is ruined by the forward-ray instability noted under C1.

**(ii) OK.** F(t_{j+1}) − F(t_j) = ∫ds/f ≤ (t_{j+1} − t_j)/f(t_j) because f(s) ≥ f(t_j); summing telescopes from F(t₀) = 0.

Monotonicity of f is genuinely used. With the decreasing f = (1+t)^{−3} and the minimal w_j = Q_j/f(t_j) (v = 0.2, N = 128),
F(t_end) = 9657 > RHS = 9512.

Random tests: 800 nondecreasing f (powers 0 ≤ p ≤ 2, exponentials, random step functions, and random over-estimated w), with
v ∈ {0.1, 0.2, 0.35, 0.5} and N = 128. The maximum normalised value of LHS − RHS is −7e-5 < 0.

**(iii) OK.** It is uniform in N in exactly the sense Lemma 4 needs: one nested family with dense union containing 0, the
same f and M for every N, and t_end ≤ T* independent of N. F is continuous and strictly increasing (since 0 < 1/f ≤ 1/f(t₀)),
so F^{−1}(M/(1−v)) exists. The strict inequality F(∞) > M/(1−v) is required. Speed: the limit path has |H'| ≤ 1, not = 1,
and C5 states this correctly.

**On the Osgood formulation.** C5 does not claim "finite time iff ∫dt/f = ∞", and that would be false. The sufficient
condition is F(∞) > M/(1−v). Divergence ∫^∞ dt/f = ∞ is exactly what makes it hold for every M. The author's f = C(1+t) gives
T* = (1+t₀)e^{2πC/(1−v)} − 1, which is correct.

Two recommendations:
- State the convention w_j := Δ_j^{−1}∫_{α_j}^{α_{j+1}} w for a fixed w ∈ L¹. Then Σ w_jΔ_j ≤ ∫w = M holds automatically for
  every N.
- Say plainly that, with w_j = Q_j/f(t_j), (iii) is a restatement of a uniform bound on the capture time. C5's text already
  concedes this.

**Chain test on real chases** (`rc_chase.py`, w = θ^{−v} + (2π−θ)^{−2v/(1+v)} cell-averaged, f = c_N(1+t) with c_N minimal):
t_end ≤ T* in every case. The bound is very loose: for example v = 0.5, N = 2048 gives t_end = 47.05 and T* = 5404.

## Remark C5a: OK (for the model recursion, with f continuous)

dα = (1−v)dt/f gives α(t) = (1−v)F(t), so the solution blows up at α = (1−v)F(∞). The C-threshold for f = C(1+t)^p with
p > 1 is correct.

"Cannot be weakened" needs one extra ingredient: that left-endpoint Euler converges, which requires f continuous. If
t_{N−1} stayed bounded by T_b, then on [t₀,T_b] the steps tend to 0 and f(t_{j+1})/f(t_j) → 1, so
F(t_{N−1}) ≥ (1−o(1))·2π/(1−v) > F(T_b), a contradiction. This shows only that (i)+(ii) cannot give more from a pointwise
bound. It does not show that an actual chase realises Q_j = f(t_j). The claim is labelled "for the model recursion",
which is fair.

**Numerics** (`rc_sweep_osgood.py`, v = 0.3):

| f | N = 1e2 … 1e6 | prediction |
|---|---|---|
| C = 0.5, p = 1 | t_{N−1} → 215.003 from below | T* = 215.003 |
| C = 0.05, p = 1.5 (below threshold 0.143) | → 4.743 | finite |
| C = 0.15, p = 1.5 (above threshold) | 6407 at N = 1e2, then overflow (∞) | blows up |

## Proposition C5b: OK. The attached numerical remark: ERROR (minor)

**Step check.** C = d g(α₁) ~ d 2^v α₁^{1−v} and β(α₁,t₀) → θ* with g(θ*) > 0, so
Q₀ = ρ(α₁,t₀)/α₁ ~ (2^v d/g(θ*)) α₁^{−v}. The precise statement:

> For every f : [t₀,∞) → (0,∞) and every nested dense family containing 0, Q₀^{(N)} > f(t₀) for all large N.

So no unweighted pointwise bound holds uniformly in N, for any v ∈ (0,1). Any admissible weight has w₀ ≳ α₁^{−v}, which is
harmless because it is integrable.

**Numerics** (`rc_chase.py`, exact map, N up to 2^20): the fitted exponent is −0.0986, −0.2968, −0.4967, −0.6977 for
v = 0.1, 0.3, 0.5, 0.7. The ratio to the asymptote is 1.0000. In actual chases, max_j Q_j/(1+t_j) grows like N^v: at v = 0.2
it is 0.871, 1.141, 1.503, 1.727 for N = 64, 256, 1024, 2048.

**ERROR in "Numerically (§4) this holds for v ≤ 0.5 with f = 0.4(1+t)".** I used the cell-averaged convention, which is the
one that makes Σ w_jΔ_j = ∫w hold automatically. Under it, the maximum of Q_j/((1+t_j)w_j) is attained at j = 0 in every run.
Its N → ∞ limit is exactly

  (1−v)² 2^v / ((2−v) g(θ*)) = 0.464, 0.434, 0.396, 0.358 for v = 0.1, 0.2, 0.35, 0.5.

The computed values at N = 4096 are 0.347, 0.388, 0.386, 0.356 and still rising towards these limits
(`rc_weight_argmax.out`). So c = 0.4 fails as N → ∞ for v ≲ 0.34.

**Fix:** state the convention for w_j and use c ≥ 0.47, or normalise w differently. This does not affect any proved claim.

Not checked (the material was not provided to me): the §4 end-point exponent p₁ ≈ 2v/(1+v), and "starting the clock at
t₁ > t₀ does not repair it".

## C8: OK

∂_tγ = −u_⊥/ρ and ρ∂_αγ = J_t (shown under C3). |J_r(t)| ≤ |J_r(s)| + ∫|∂_αγ||u_⊥| and
|J(t)| ≤ |J(s)| + v∫|∂_αγ| follow by integrating C3 and C0.

The straight-step identities are correct for |u| = 1:
- ρβ' = sin β gives d ln tan(β/2) = dt/ρ;
- |u_⊥| = |sin β| and β is monotone on a straight run, so ∫|u_⊥|/ρ = Δ|β|;
- the head-on case gives ln(ρ₀/ρ₁)/(1−v).

The trawler check is exact: for a static Harry, S = (d+vt)e^{iα} and |J| = d+vt.

The necessity of a weight near α = 0 is correct. Since |J(α,t₀)| ≍ α^{−v} (verified above), C8 forces
sup_{τ≤t₀}|∂_αγ(α,τ)| ≥ (|J(α,t₀)| − d)/(vt₀) ≍ α^{−v}. The (2π−α) exponent is numerical, from §4, and was not checked.

**Numerics** (`rc_tangent.py`, 60 random curved paths, s = 0, t up to 4): the maximum of LHS − RHS is −3.1e-2 for the J_r
bound, −1.4e-3 for the additive |J| bound and −2.4e-3 for the exponential bound. All are satisfied.

## C9: OK

**Step check.** At t_k the previous target is at distance exactly ε, so ρ_k ≤ ε + Q_kΔ_k and τ_k ≤ Q_kΔ_k/(1−v). θ_k is
strictly increasing by the definition of "first unseen". The telescoping is as in C5(ii), with F based at
t₁ = (d−ε)/(1−v). The author correctly does not claim a statement for all directions.

**Numerics** (`rc_sweep_osgood.py`, greedy sweep with exact minimum distance per step, v ∈ {0.2, 0.35, 0.5},
ε ∈ {0.1, 0.05}, N = 512):
- θ_k is strictly increasing;
- |dist(previous target) − ε| ≤ 1.4e-15;
- max(τ_k − Q_kΔ_k/(1−v)) < 0;
- F(T) − RHS < 0 for f = c(1+t) with c ∈ {0.1, 0.5, 2}.

The sweep end times (12.77, 13.00, 22.39, 22.69, 44.88, 45.50) are consistent with the main.tex table.

**Caveat for (R1)/(R2)**, which are not among the claims refereed here. The step "chord ≤ ∫|J|dα" over [θ_{k−1}, θ_k] needs
every continuum direction in that arc to have ρ > 0 on [0,t_k]. With ε > 0 Harry can pass exactly through a direction that is
not in the finite set. That trajectory then ends, and by the local Prop. 4 computation above the front tears into two pieces
whose ends separate like δ^{1−v}. The chord bound then needs an extra gap term, or a proof that this does not happen before
t_k.

## Summary of required edits

1. **C2:** state both limits, (a) the trajectory limit and (b) the one-sided endpoint derivative ~ (1−v)2^v d α^{−v}/g(θ*).
   Say that (b) is the author's meaning, that both are infinite, and that they differ in direction.
2. **C4:** replace "the author's quantity" by "the trajectory stretch", and "tangent pointing at Harry" by the averaged
   statement.
3. **C5(i):** re-index over the targets actually chased (accidental catches).
4. **C5(iii):** state the cell-average convention for w_j.
5. **C5a:** add "f continuous".
6. **C5b numerics:** the constant 0.4 is too small for v ≲ 0.34 as N → ∞; the j = 0 term tends to (1−v)²2^v/((2−v)g(θ*)).
