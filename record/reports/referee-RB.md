# Referee report RB: stream-B claims (Lemma B1, Theorem B2, Props B3, B4, B5 and the §7 linear model)

Referee: independent and adversarial. I read `BRIEF.md`, `paper/main.tex` and `referee/B-claims.md` only. I did not open
`reports/B-1.md` or `code/B/`. All scripts are in `code/referee/RB/` and run from that directory with `python -W ignore <script>`.
The chase simulator `rb3_chase.py` is my own. It uses the exact straight-run map, obtained by inverting the integrals
(C, h) of Prop. 1 with k(s) = [(1+v) − (1−v)s²] s^(v−1)/2, s = tan(|β|/2), by bisection in log s.
As Rule 4 requires, I checked it against the paper's table before using it: ε = 0, N = 256 gives T = 13.11, 18.72 and 28.19 at
v = 0.2, 0.3, 0.4. The table has 13.24, 19.08 and 29.24 at N = 2000, and T increases with N. It also reproduces the stream-B
§7 times: 78.6 at v = 0.52 (N = 512) and 186 at v = 0.55 (N = 256).

## Summary of verdicts

| Claim | Verdict |
|---|---|
| Lemma B1(a) (1−λ)Φ ≤ Ψ ≤ Φ | **OK** |
| Lemma B1(b) continuity | **GAP (minor)**: false at an accidental catch of the last candidate. Ψ only jumps **down** there, so nothing downstream breaks. Fix below. |
| Lemma B1(c) rate identity | **OK** (algebra checked; finite differences agree to 2e-6 on 2000 random and adversarial states and to 5e-7 along simulated chases) |
| Theorem B2 (conditional on (K)) | **GAP**, easy to fix: "choose any λ with m > 0, then c > 0" is **false** (counterexample below). Positivity of c is argued only numerically. The fixed choice λ = λ\* proves it analytically. The value v1 = 0.474752638**033** is **wrong from the 10th decimal on**; the correct value is v1 = 0.47475263829074210294519… The rest checks out: the closed form for m, λ\*, the time bound, and the deduction from (K). |
| Prop B3 (sharpness at v1) | **OK** |
| Prop B4 ((H) cannot certify Φ + κρ_N beyond 1/(1+π)) | **OK** (the order of limits η → 0 before δ → 0 is essential and is stated) |
| Prop B5 (generating function, growth for 1/2 < v < 3/4) | **OK about the model**. Two minor wording points: the q = 3 case and the claim that the zigzag is the dominant mode, which is numerical. |
| §7 linear model derivation | **OK as a linearisation**, and I verified it to 1e-10 against the exact nonlinear chase of equally spaced candidates on a ray. The **link to the real chase is a CONJECTURE**, as labelled. |

Side finding, not a B claim: in my simulator **(H) itself fails above 1/2**. The maximum of A is 3.483 at v = 0.52 (N = 512) and
3.926 at v = 0.55 (N = 256). (K) fails there too (W − |β_N| up to 0.97). This does not affect B2, whose range is v < 0.4748.
It does mean that (K) and (H) depend on v and must be read "for the given v".

---

## 1. Lemma B1

**(a) OK.** Φ is the length of a polyline from H to S_N, so Φ ≥ ρ_N ≥ 0. Then Ψ = Φ − λρ_N lies in [Φ − λΦ, Φ].
This also settles a question from the brief: Ψ = 0 if and only if Φ = 0 (because λ < 1), which happens if and only if every
candidate is caught. So the end of the chase is exactly Ψ = 0. On the final leg Ψ = (1−λ)ρ_N → 0 (`rb6`: last sample about 1e-2,
taken one substep before the catch).

**(b) GAP (minor).** "ρ_N is continuous because … S_N is caught only at the end" is not justified. If S_N lies on the segment from H to S_j
at the start of leg j, it is caught early. The remark in the claims says Lemma 2 of the tex "tacitly assumes this does not occur".
That is inaccurate: the tex Lemma 2 handles accidental catches explicitly. After the deletion ρ_N (= 0 at the catch) has no meaning.
The fix:

> Let N(t) be the index of the last *remaining* candidate, and put Ψ = Φ − λ ρ_{N(t)}. Ψ is continuous except at accidental
> catches, where it can only jump down. If an intermediate S_i is deleted, Φ drops by the triangle-inequality excess and ρ_{N(t)}
> is unchanged. If the last candidate S_N is deleted, then just before the deletion Φ₋ includes |S_N − S_{N'}| = ρ_{N'}, where N' is
> the new last index. Just after, Φ₊ = Φ₋ − ρ_{N'}, and ρ jumps from 0 to ρ_{N'}. So Ψ₊ = Ψ₋ − (1+λ)ρ_{N'} < Ψ₋.
> Two candidates cannot be caught at the same instant, because distinct candidates never coincide (backward uniqueness).
> (a) and (c) hold verbatim with N(t). Ψ ≥ (1−λ)Φ ≥ 0 survives every deletion.

(K) must then be read with β_{N(t)}. Theorem B2's argument only needs "Ψ' ≤ −c on open intervals, with finitely many downward jumps",
so the conclusion is unchanged. In my simulations no accidental catch ever came close: every candidate ahead of Harry and nearer than
the target had a bearing of at least 1.46 rad.

**(c) OK.** Lemma 2 gives Φ' = −(1−v) + vW, and Eq. (polar) gives ρ_N' = v − cos β_N. Then
Ψ' = −(1−v) − λv + λcos β_N + vW = −(1−λ)(1−v) + vW − λ(1−cos β_N), which I expanded and checked.

β_N is well defined while ρ_N > 0. That holds on every open leg except just before an accidental catch of S_N, and there S_N is on
the forward ray, so β_N = 0 and the formula still holds. When S_N = S_j (the final leg), β_N = 0, W = 0 (empty sum) and
Ψ' = −(1−λ)(1−v), which finite differences confirm (`rb2`: −0.24 against −0.24). The formula uses only cos β_N, so the branch
choice (−π, π] does not matter.

Numerical evidence:
- `rb2_rate_states.py`: 2000 random states (1–12 candidates, v in (0.01, 0.99), λ in [0, 1), every fifth one adversarial with S_N
  almost directly behind Harry). The largest gap between an RK4 central difference and the formula is 2.2e-6, at the O(dt²) level.
  (a) holds in all cases, and W ≤ A in all cases.
- `rb3_chase.py`: along real chases at v = 0.2–0.55 and N = 256–2048, the largest gap between the finite difference and the formula
  is at most 5.4e-7.

## 2. Theorem B2 (conditional on (K))

**Closed form for m(v,λ): OK.** Let f(x) = (1−λ)(1−v) + λ(1−cos x) − vx, so f' = λ sin x − v.
- If λ ≤ v, f' ≤ 0 and the minimum is at π.
- If λ > v, f' < 0 on [0, x₁), f' > 0 on (x₁, π−x₁) and f' < 0 on (π−x₁, π], with x₁ = arcsin(v/λ). The candidates for the
  minimum are therefore x₁ and π.
- λ cos x₁ = √(λ²−v²) gives m_int.

`rb1_threshold.py` compares the closed form with brute force (2e5 grid points) on 3000 random (v, λ) pairs plus edge cases (λ = v(1 ± 1e-9), λ = 1 − 1e-9). The largest gap is 6e-17.

**Characterisation of v1: OK.** Write M(v) = max_λ m(v,λ).
- ∂f/∂v = −(1−λ) − x < 0, so M is strictly decreasing and v1 is unique.
- m_π − m_int = λ + √(λ²−v²) + v·arcsin(v/λ) − vπ has λ-derivative 1 + √(λ²−v²)/λ > 0, so the two branches cross exactly once.
- ∂m_int/∂λ = v − cos x₁ (envelope). At the crossing for v1, cos x₁ = 0.689 > v1, so m_int is decreasing there while m_π is increasing.
  The maximum of min(m_π, m_int) is therefore at the crossing, and v1 solves m_π = m_int = 0. ✔
- From m_π = 0, λ\* = ((π+1)v1 − 1)/(1+v1). ✔

**Value of v1: ERROR (numerical).** I solved the two equations two independent ways at 30 and 60 digits (`rb1_threshold.py` and `rb1b_v1.py`):

  v1 = 0.474752638290742102945191…, λ\* = 0.655182444791002805224646…

The claimed 0.474752638**033** is off by 2.6e-10. At that value M = +3.7e-10, while at my value M = 1.5e-16. This is cosmetic, but the
digits must be corrected.

**Positivity of c: GAP.** The statement says "Choose λ with m(v,λ) > 0. Put c = min(m, (1−λ)(1−v) − v·w0), which is > 0."
**Counterexample:** v = 0.05, λ = 0.99. Then m = 0.0082 > 0, but (1−λ)(1−v) − 0.3v = −0.0055 < 0.

The proof concedes that the optimal λ is needed and then supports it only by a numerical monotonicity claim. My numerics agree with
that claim: (1−λ_opt)(1−v)/v decreases in v and is 0.3815 at v1, and the second term is at least 0.0397 on (0, v1). But that is not
a proof. **Fix (fully analytic):** take **λ = λ\*** (fixed) for every v < v1.
- m(v, λ\*) > m(v1, λ\*) = 0, because m is strictly decreasing in v.
- (1−λ\*)(1−v) − 0.3v > 0 if and only if v < (1−λ\*)/(1.3−λ\*) = 0.53475 > v1.

Hence c > 0 for all v < v1. If a better T is wanted, λ_opt(v) can be used wherever both terms are checked to be positive.

With λ\* the bounds get worse. For d = 1, T is 45.1, 60.7, 131.8, 410.8 and 2171 at v = 0.2415, 0.3, 0.4, 0.45, 0.47, against the
claimed (optimal-λ) values 21.4, 31.8, 91.8, 313 and 1713. I reproduced the claimed table exactly: 21.3 (they round to 21.4), 31.8,
49.3, 91.8, 312.6, 1714.4. λ_opt/v stays in [1.3796, 1.3815], which confirms "λ_opt ≈ 1.38v".

**Deduction from (K): OK.**
- Case W ≤ |β_N|: Ψ' ≤ −f(|β_N|) ≤ −m.
- Case W ≤ w0: Ψ' ≤ −(1−λ)(1−v) + v·w0, using 1 − cos ≥ 0.
- Final leg: Ψ' = −(1−λ)(1−v) ≤ −m, because m ≤ f(0).

Ψ is piecewise C¹ on finitely many intervals with only downward jumps, so Ψ(t) ≤ Ψ(t0) − c(t−t0). Combined with Ψ ≥ 0 and
Ψ(t0) ≤ Φ(t0) ≤ 2πd/(1−v) (Lemma 3; scaling in d checked), this gives T as stated. Lemma 4 is then applied to nested dyadic sets,
each of which contains 0, and H_N stays put after its last catch. ✔

Check on simulated chases (`rb6_psi_monotone.py`, N = 512, λ = λ_opt):

| v | largest slope of Ψ | required (≤ −c) | Ψ(t0) | 2π/(1−v) | T_sim | T bound |
|---|---|---|---|---|---|---|
| 0.3 | −0.410 | −0.296 | 8.57 | 8.98 | 18.8 | 31.8 |
| 0.45 | −0.206 | −0.037 | 10.49 | 11.42 | 35.9 | 313 |
| 0.47 | −0.184 | −0.0069 | 10.81 | 11.86 | 39.6 | 1714 |

(K) held in every sample for v ≤ 0.5. The largest W − |β_N| was 1.3e-3, 5.8e-3 and 8.2e-3 at v = 0.5 for N = 256, 1024 and 2048,
in line with the claimed 0.0076–0.0106. **The status of (K) stays CONJECTURE.** Theorem B2 is a correct conditional theorem once
the fixes above are made.

## 3. Prop B3: OK
- The states are S_j = (r, 0) and S_{j+k} on the circle of radius r at bearings kx/n. Each triangle is isosceles with apex angle x/n,
  so cos b + cos c = 2 sin(x/2n) and W = 2n sin(x/2n) < x = |β_N|. The states therefore satisfy (K), and W → x.
- The rate is −(1−λ)(1−v) + vW − λ(1−cos x), which tends to −f(x) from below.
- f'(0) = −v < 0, so the minimiser of f is never 0 and sup_(K) Ψ' ≥ −m(v,λ). For v ≥ v1, m ≤ 0 for every λ in [0,1), so no uniform
  negative rate exists. (For λ < 0, m is smaller still, and λ ≥ 1 gives no termination argument.)

`rb2` at v1, λ\*, with x in {0.5, x₁ = 0.8105, 2.0, π} and n = 10, 100, 1000: finite differences, the formula and −f(x) agree,
and the rate tends to 0 at both minimisers x₁ and π. That confirms the double minimum at (v1, λ\*).

Caveat (already stated): these states are abstract and need not occur in a chase. B3 is sharpness of the *method*, not of capture.

## 4. Prop B4: OK
- (a) x = π: A = π, W → π, ρ_N' = 1 + v. ✔
- (b) Zig-zag: A = nδ ≤ π, cos β_N → 1, and W → 2n sin(δ/2) → π, **provided η → 0 first** (as written).
  `rb2`: δ = 0.01 gives W = 3.1398 at η = 1e-4 but only 2.845 at η = 1e-2.
- For κ ≥ 0 use (a); for κ < 0 use (b). Either way sup ≥ v(1+π) − 1. ✔

## 5. Prop B5 and the §7 linear model

**Derivation of the model: OK, and stronger than "heuristic".**
- Linearising Eq. (polar) at β = 0 gives ρ' = −(1−v) and dβ/β = −q dρ/ρ, so β ∝ ρ^(−q). All candidates on the ray recede at the
  same speed v, so the spacing l is preserved and each leg lasts l/(1−v).
- Let G_n(k) = k^q·(deviation of the candidate at distance kl). Then G_{n+1}(k) = G_n(k+1) − k^q δ_n with δ_n = G_n(2), and
  G_n(1) = 0 is automatic.
- Unrolling: δ_n = G_0(n+2) − Σ_{k=0}^{n−1} (k+2)^q δ_{n−1−k}. With a seed only on candidate 2, this is the stated recursion. ✔

`rb5_model_vs_exact.py` runs the exact nonlinear chase of 60 equally spaced candidates on a ray, with a 1e-12 seed. It matches the
recursion with relative error at most 3.6e-10, 1.2e-12, 2.3e-13 and 1.3e-13 over 15 legs at v = 0.4, 0.5, 0.55 and 0.6.

So the following is PROVED: *the recursion is the exact first-order linearisation of the discrete chase about the configuration
"candidates equally spaced on a ray ahead of Harry".*

Nonlinear saturation: with a 1e-3 seed at v = 0.55 the turns saturate at about 1.44 rad, in line with the claimed ±1.47 in the real chase.

**Generating function: OK.**
- D − 1 = −zGD, and 1 + zG = Σ_{m≥0} (m+1)^q z^m = Li_{−q}(z)/z, so D = z/Li_{−q}(z). Checked symbolically against power-series
  inversion: zero difference at q = 1.5, 2, 2.5 (`rb4_model.py`).
- q = 2: D = (1−z)³/(1+z), so δ = 1, −4, 7, −8, 8, −8, … and δ_n = 8(−1)^n exactly for n ≥ 3. ✔
- Li_{−q}(−1) = −η(−q) = (2^(1+q)−1)ζ(−q). Checked with mpmath for q in {1.5, 2, 2.2, 2.5, 3, 3.5, 3.9, 4, 4.5}: positive exactly on (2, 4).
- ζ(−q) > 0 on (2, 4): by the functional equation, sin(πs/2) > 0 for s in (−4, −2), and Γ(1−s) and ζ(1−s) are positive.
- Near 0, Li_{−q}(−x) = −x + O(x²) < 0. The intermediate value theorem gives z0 in (−1, 0). The numerator z0 ≠ 0, so z0 is a pole of D
  and limsup |δ_n|^(1/n) ≥ 1/|z0|. ✔

Minor wording points:
- (i) "for q not an integer": q = 3 (v = 2/3) lies in the range. There Li_{−3} = z(1+4z+z²)/(1−z)⁴ is rational, analytic off z = 1,
  with Li_{−3}(−1) = 1/8 > 0. Just say "Li_{−q} is analytic on ℂ \ [1, ∞) for every real q".
- (ii) The proof gives only limsup ≥ 1/|z0| along a subsequence. That z0 is the *dominant* singularity, which is what makes the
  growth a clean period-2 zigzag at rate exactly 1/|z0|, is NUMERICAL. The argument-principle count of zeros of Li_{−q}/z in
  |z| < 0.98 is exactly 1 for v = 0.51–0.74 and exactly 0 for v = 0.4, 0.45, 0.5. The ratio δ_n/δ_{n−1} at n = 120 equals 1/|z0|
  to 6 digits.

Claimed growth rates, reproduced exactly:

| v | 0.51 | 0.52 | 0.53 | 0.55 | 0.6 | 0.7 |
|---|---|---|---|---|---|---|
| 1/\|z0\| | 1.07095 | 1.14777 | 1.23113 | 1.42059 | 2.07806 | 5.27592 |

For v < 1/2 the recursion decays only slowly (ratio about 0.969 at n = 150), which suggests polynomial rather than exponential decay.
"Decays" is fine as a NUMERICAL statement.

**What is proved and what is conjectured.**
- PROVED: (1) the recursion is the linearisation of the exact chase about an equally spaced radial row of candidates;
  (2) its generating function is z/Li_{−q}(z); (3) for 1/2 < v < 3/4 the seeded solution has limsup |δ_n|^(1/n) ≥ 1/|z0| > 1;
  (4) at v = 1/2 it is exactly 8(−1)^n from n = 3 on. All of these hold in the model and do not depend on the spacing l.
- NUMERICAL: z0 is the only pole in the unit disk; the solution decays for v < 1/2.
- CONJECTURE: that this governs the real chase, and the consequence that "no functional decreases uniformly beyond 1/2".
  - The real candidates are not equally spaced. Near the V vertex at first contact, ρ_k ∝ k^(1−v) to leading order.
  - The wavefront is curved, which acts as a nonzero forcing G_0(n+2).
  - The row is finite.
  - Growth saturates nonlinearly.
  - Every finite chase still terminates. The issue is uniformity in N, which the model does not address.

Supporting evidence for the link (`rb5b_power_spacing.py`, spacing ρ_k = k^(1−v)): the seeded zigzag decays at v = 0.45,
grows slowly (sub-exponentially) at v = 0.5, and grows by about 1.45 per leg at v = 0.55. My full chase shows the period-2 zigzag
at v ≥ 0.52 (largest |turn| in the second half: 1.09 at v = 0.52, 1.54 at v = 0.55) and none at v ≤ 0.5. Both fit the conjecture,
but neither proves it.

## Reproduction
```
cd code/referee/RB
python rb1_threshold.py         # closed form vs brute force, v1, lam*, c>0, counterexample, T table
python rb1b_v1.py               # v1 to 60 digits, independent method
python -W ignore rb2_rate_states.py   # B1(a),(c) on random/adversarial states; B3, B4 states
python -W ignore rb3_chase.py 0.5 2048    # (K), rate identity, A along the chase (args: v N [lam])
python rb4_model.py             # z/Li_{-q}, Li(-1)=(2^{1+q}-1)zeta(-q), zero counts, growth rates (mpmath, ~5 min)
python -W ignore rb5_model_vs_exact.py    # linear recursion vs exact chase on an equally spaced ray
python -W ignore rb5b_power_spacing.py    # same with spacing k^(1-v)
python -W ignore rb6_psi_monotone.py      # Psi slope <= -c along simulated chases
```
(`rb4b_zeros.py` is a slower numpy cross-check of the zero locations. It is optional and gave no result I rely on.)
