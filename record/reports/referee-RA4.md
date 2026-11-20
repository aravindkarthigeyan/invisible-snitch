# Referee report RA4 — claims of A-4 (`referee/A4-claims.md`)

Referee: independent, adversarial. Inputs read: `BRIEF.md` §1–2, `paper/main.tex` (Prop. prop:integrals, Lemma lem:k,
Lemma lem:A2, Lemma lem:limit with its Claim, Section sec:linear), `referee/A4-claims.md`, and (for the statement being
refuted in §4) `reports/A-3.md` §8 and `referee/B-claims.md` §7. I did not read `reports/A-4.md` or `code/A4/`. All code is
my own, in `code/referee/RA4/` (Python 3.12, numpy/scipy/mpmath; PowerShell: `$env:OPENBLAS_NUM_THREADS=1`).

## Verdicts

| Claim | Verdict | Summary |
|---|---|---|
| Lemma A4.1 (vanishing vision radius) | **OK** as stated | Hypotheses are exactly right. Nestedness, or something equivalent to it, is essential (counterexample below). The limit catches every direction **exactly**, with **speed ≤ 1**. |
| Lemma A4.2 (straight-run identity) | **OK** | Algebra checked. Random exact runs: relative error 2·10⁻¹¹. |
| Prop. A4.3 (kink amplification, exact) | **OK** | Each step checked. 400 random runs: 0 violations. |
| Cor. A4.3' (no N-uniform constant) | **GAP (minor, fixed below)** | The statement is unconditional, but the proof uses tan²κ₀ ≤ m+1. Monotonicity of κ covers the other case. |
| "Consequence" (A-3 §8 induction is false) | **OK** on a radial chain (PROVED). **NUMERICAL** on a curved background | On a circular background in the exact chase I measured the same m^μ growth (slope 0.249 vs μ = 0.25; 0.427 vs 0.429). |
| Amplification table (exact chase vs linear model) | **OK, reproduced** | Independent code reproduces every quoted digit. The formula also holds at n = 1 and n = 0. |
| B-recursion maps the discrete circle to itself | **OK** | This is the identity P(n+1) − n^q = P(n). The recursion matches B-1's linearisation. |
| Prop. A4.4 (a), (b), (d) | **OK** | About the linear model (L) only. |
| Prop. A4.4 (c) | **OK statement, GAP in proof (minor, fixed below)** | The step ψ(p+2+μ) − ψ(2) ≤ log(p+3) is false for μ ≳ 3. The claim survives because it is trivial for μ > 1/log 3. |
| §5.1 "Reading" | **Overstated (wording fix)** | The obstruction holds only for operator norms on a *single* space. On an analytic scale X_r → X_{r'}, T_μ → I as μ → 0. |

---

## 1. Lemma A4.1 (vanishing vision radius)

**Step check.** The proof is the proof of Lemma lem:limit with "caught at t_N" replaced by "ρ ≤ ε_n at t_n".
- Arzelà–Ascoli: the H_n are 1-Lipschitz on [0, T] with H_n(0) = 0. OK.
- *Fix α ∈ D_M; for n ≥ M (n in the subsequence) α ∈ D_n.* This uses **nestedness**, and only there.
- *Existence of t_n.* Before its first catch the trajectory exists. If α is caught at t_c ≤ T, take t_n = t_c (ρ = 0). OK.
- *If H does not catch α on [0, t*], then ρ_α ≥ c > 0 on [0, t*].* The maximal solution under H lives on [0, t_max), and
  ρ → 0 as t → t_max because |S'| = v. S then extends continuously with S(t_max) = H(t_max), which is a catch. So "not
  caught on [0, t*]" gives t_max > t*, and a continuous positive ρ has a positive minimum on the compact interval. OK.
- *The Claim (paper) gives ρ^{(n)} ≥ c/4 on [0, min(t*+δ, T)].* I checked the Claim's Gronwall step. By Dunkl–Williams,
  |x̂ − ŷ| ≤ 2|x−y|/(|x|+|y|) ≤ (4/c)|x−y| on {|x|, |y| ≥ c/4}, so the paper's constant 8v/c is safe. I tested the
  inequality on 2·10⁵ random pairs: max ratio 1.000000. The open-closed argument is correct. The Claim needs ρ ≥ c/2
  under H on [τ, τ+δ], which |ρ'| ≤ 1+v gives. Since t_n ≤ T and t_n → t*, eventually t_n ≤ min(t*+δ, T), so
  ε_n ≥ c/4, contradicting ε_n → 0. OK.
- *Final step.* The set of directions not caught by H on [0, T] is open, by the Claim with H_N ≡ H, τ = T. Its
  complement is closed and contains the dense set ∪D_n. OK.

**Is the capture exact?** Yes. The contradiction rules out ρ_α > 0 on all of [0, t*], so ρ_α reaches 0 under H at some
time ≤ t* ≤ T. This is exact capture in the sense of the paper. The limit path is only 1-Lipschitz (speed ≤ 1), as
Remark (b) says.

**Exact hypotheses (the question asked).**
- With nested D_n, "H_n sees every α ∈ D_n" is the right hypothesis. It is equivalent to "H_n sees D_1 ∪ … ∪ D_n".
- The weakest form this proof supports: there is a dense set E such that each α ∈ E is seen by H_n (radius ε_n, by
  time T) **for all sufficiently large n**. (Set D'_n = {α ∈ E : seen by H_k for all k ≥ n}; these are nested and seen
  by H_n.)
- **Without nestedness the lemma is false, even with ε_n = 0.** Take D_n = {α_{k(n)}}, where (α_k) is dense and k(n)
  takes every value infinitely often. Let H_n be the straight run at angle α_{k(n)}, and T = d/(1−v). Every H_n catches
  its own direction exactly at T, and every α_k is caught infinitely often. But no path catches two directions by
  d/(1−v):
  - ρ' = v − r̂·H' ≥ −(1−v), so a catch by time d/(1−v) forces ρ' = −(1−v) a.e., that is H' = r̂_α a.e.;
  - two directions α ≠ α' would need H' = r̂_α = r̂_{α'} a.e., which is false near t = 0.

  Seeing each direction infinitely often is therefore not enough. Numerics (`compact_checks.py` §2): the limit path
  stays ≥ 0.019 away from the direction 10⁻³ and ≥ 0.30 away from the direction 0.1.
- Finiteness of D_n is not needed (D_n = all directions is fine). Density of ∪D_n, a uniform T, and ε_n → 0 are all
  needed.

**Recommendation.** A4.1 can enter the paper as a one-line generalisation of Lemma lem:limit: replace "catches every
direction of D_N by time T" with "comes within ε_N of every direction of D_N by time T, ε_N → 0". Lemma lem:limit is the
case ε_N = 0, and the proof text needs only the substitution above. Remark (d) is a correct implication. Note that it
also covers discretised ε-controllers: H_n only has to see a nested finite set D_n, not all directions. The *numerical*
support cited there (brief table, H4 stability) is evidence about the hypothesis, not part of the lemma. I did not
referee Remark (c) (Theorem D1 range).

## 2. Lemma A4.2

- y = ρ sin β = C tan^v(β/2), and tan(β/2) = sin β/(1+cos β) = y/(2ρ cos²(β/2)).
- So y^{1−v} = C 2^{−v} ρ^{−v} cos^{−2v}(β/2). Raising to the power q gives the identity, with vq = μ. Correct.
- Monotonicity: by Lemma lem:A2, β increases. Independently, y' = (v r̂ − u)·n = v sin β ≥ 0.

**Numerics** (`straight_run.py`): 400 DOP853 runs (rtol 10⁻¹³), with v ∈ [0.01, 0.97], ρ₀ ∈ [10⁻², 10²] and β₀ including
values within 10⁻⁴ of 0 and π.
- Maximum relative error of y ρ^μ cos^{2μ}(β/2) against (C/2^v)^q: **1.9·10⁻¹¹**.
- Drift of C (control): 1.0·10⁻¹¹.
- y never decreased.

## 3. Proposition A4.3 and Corollary A4.3'

**A4.3: all steps correct.**
- The forward ray is invariant (Lemma lem:A2), so all targets P_i stay on it and the run is straight up to p_m/(1−v).
- (x_Q − p_m)' = (v cos β_Q − 1) + (1 − v) = −v(1 − cos β_Q) ≤ 0.
- From A4.2, y(t)/y(0) = (ρ₀/ρ)^μ (cos(β₀/2)/cos(β/2))^{2μ}. The last factor is ≥ 1 because β is non-decreasing.
- Once x_Q ≤ p_m, the vector Q − P_m has a non-positive u-component and y > 0, so κ ≥ π/2.

`straight_run.py` §2: 400 random (v, p_m, Q), 300 times each, gave **0 violations**; the slack is ≥ 0.

**A4.3': GAP (minor).** The displayed bound is stated with no condition on κ₀. Case 2 of the proof uses tan²κ₀ ≤ m+1,
both for the inequality ρ_Q(t₁) ≤ 10ℓ and for the √ estimate. The statement is still true. **Fix:**
- While x_Q > p_m, tan κ = y_Q/(x_Q − p_m) is non-decreasing (numerator non-decreasing, denominator positive and
  non-increasing). After that, κ ≥ π/2. So κ(t₁) ≥ κ₀ always.
- If tan²κ₀ > m+1 and m ≥ 2, then tan²κ₀ > 3, so κ(t₁) ≥ κ₀ > π/3.
- If m = 1, then t₁ = 0 and κ(t₁) = κ₀ ≥ arctan(tan κ₀ (2/10)^μ).

Add one sentence covering these cases. **Numerics** (`kink_chain.py`): 600 random cases, 42 of them with tan²κ₀ > m+1,
with m ≤ 120 and ℓ ∈ [10⁻³, 10]: **0 violations**. κ was non-decreasing in all 200 tested runs.

**Other steps checked:**
- Case 1 (subtracting p_m u from r_Q increases the angle with u).
- h(0) ≤ (1+v)ρ₀.
- ρ₀ − (m−1)ℓ ≤ ℓ(2 + tan²κ₀/(2(m+1))).
- 5(1+v) ≤ 10.

**Consequence (A-3 §8 is not inductive).** The quoted A-3 statement matches `reports/A-3.md` §8: turning ≤ K·gap within
r₀ and a C²-close far chain at leg j imply the same at leg j+1, with constants independent of N.
- With κ₀ = Kℓ at distance r₀ = mℓ, A4.3' gives turning ≥ min{π/3, arctan(Kℓ((m+1)/10)^μ)} one gap from Harry. Its
  ratio to ℓ tends to infinity as ℓ → 0. Correct for every v > 0.
- The literal one-step induction with the *same* K already fails after one leg: a kink with turning exactly Kℓ at index n
  becomes Kℓ((n+2)/(n+1))^μ.
- The refutation is exact for a straight (radial) background.
- I tested whether it survives curvature, which matters if "C²-close to the static arc" excludes a straight far chain.
  Setup (`kink_circle.py`, `kink_circle_scaling.py`): candidates spaced ℓ along a circle tangent to Harry's heading,
  with and without a kink δ = 10⁻⁷ at P_m, chased with the exact straight-run map and exact contact.
  - The difference in turning at P_m, one gap from Harry, scales as m^μ with r₀ = 0.2 fixed and ℓ → 0. The log₂-slopes
    at m = 400 are 0.249 (μ = 0.25) and 0.427 (μ = 0.429). Values are within 0.5% of ((m+1)/2)^μ.
  - With strong curvature (R_c = 0.3 or 0.5, kink at distance 1) the far-field factor drops by about 2.
  - The near-field law ((n₁+1)/(n₂+1))^μ still holds to 0.7% there.

  So the curved-background claim is NUMERICAL in the exact chase (A-4 proves it only in the linear model). It is robust.

**Amplification table: reproduced to every quoted digit** by my independent exact chase (`kink_chain.py`; the exact
(C, h) straight-run map agrees with DOP853 to 1.7·10⁻¹³). Examples:
- v = 0.45, m = 400, δ = 10⁻³: 1.7596, 18.956, 43.352, 54.840.
- v = 0.1: 1.0798, 1.4912, 1.6686, 1.7228.

The formula ((m+1)/(n+1))^μ also holds at n = 1 and at n = 0 (Harry's actual turn on leaving P_m: 1.9464 vs 401^{0.111} =
1.946). The restriction n ≥ 2 is therefore conservative. At v = 0.6 with δ = 10⁻³ the exact values fall below the model
(1387 vs 2839), because the angle is no longer small. That is a nonlinear effect, outside the claim.

**B-recursion.** The rank-one update is B'_i = B_i − B_{j+1}(ρ_i/ρ_{j+1})^q, with B = (φ − ψ)ρ^q. This matches B-1's
linearisation (bearing ∝ ρ^{−q} on a run, then subtract the turn ψ = bearing of the new target). For B_n = cP(n) with
P(n) = Σ_{k<n} k^q, after one leg B'_i = c[P(i+1) − i^q] = cP(i). OK. The "What the right hypothesis must look like"
paragraph is CONJECTURE and was not refereed. It is consistent with the transport law I measured.

## 4. Proposition A4.4 (linear model (L) only)

**What is proved.** T_μ is defined from the Abel equation (L) of `paper/main.tex` sec:linear. The proved results concern
this operator only. Identifying T_μ with D_H of the true catch map is NUMERICAL and heuristic, inherited from H-1.

- **(a) OK.** F((1−v)τ) = ∫₀^τ(1−s/τ)^μ θ(s) ds. ∂_τ of the kernel is μ(1−s/τ)^{μ−1}s/τ², which is integrable, so the
  differentiation is valid for continuous θ. The mass is μaB(μ, 2) = a/(1+μ) = 1.
  - Numerically I computed F from (L) by quadrature at 40 digits, took a centred difference with step 10⁻¹², and
    compared with the ν_μ-average. Agreement was 10⁻¹⁶ for v = 0.1–0.7, including the non-smooth θ = |s − 0.4|.
  - ν_μ → δ₁ as μ → 0: ν((1−η, 1]) = aη^μ − μη^{μ+1} → 1.
- **(b) OK.** μaB(μ, p+2) = Γ(a+1)Γ(p+2)/Γ(p+a+1), using aΓ(a) = Γ(a+1). Quadrature matches to 10⁻¹⁶. R(p) is
  decreasing by log-convexity, and R(p) ~ Γ(a+1)p^{−μ}.
- **(c) Statement OK, proof step wrong for large μ.** The chain −log R ≤ μ[ψ(p+2+μ) − ψ(2)] is correct. The next
  inequality, ψ(p+2+μ) − ψ(2) ≤ log(p+3), fails at p = 0 for μ ≳ 3.1 (μ = 5: 1.450 > 1.099; μ = 10: 2.020 > 1.099).
  **Fix:**
  - For μ ≤ 1: ψ(p+2+μ) ≤ ψ(p+3) < log(p+3), and ψ(2) > 0.
  - For μ ≥ 1/log 3 ≈ 0.91: 1 − R ≤ 1 ≤ μ log 3 ≤ μ log(p+3).

  The two ranges overlap, so (c) holds for all μ > 0. Grid check: 260 values of μ ∈ [10⁻⁴, 50] × 501 values of
  p ∈ [0, 10¹²], computed with mpmath log-gamma at 40 digits, give max (1−R)/(μ log(p+3)) = **0.983**, and 1 − R ≥ 0
  everywhere. (A float log-gamma version wrongly gave 2.17 from cancellation at p ~ 10¹². Use high precision.)
- **(d) OK as stated.**
  - (T_μ − I)τ^p = (R(p) − 1)τ^p and R(p) → 0, so the operator norm is ≥ 1 on any normed space containing the monomials.
  - inf ‖T_μ f‖/‖f‖ ≤ R(p) → 0, so T_μ has no bounded inverse.
  - On C[0, 1], ‖T_μ‖ = 1 (ν is a probability measure), and the test function gives (I − T_μ)θ(1) ≥ 2 − 2(aη^μ − μη^{μ+1})
    → 2. Exact values for μ = 0.05: 0.137, 0.947, 1.934, 2.000 at η = 10⁻¹, 10⁻⁶, 10⁻³⁰, 10⁻³⁰⁰. The convergence in η is
    slow for small μ, as the formula predicts.
- **log p\* table OK:** 13.609, 6.694, 3.208, 1.948, 0.939. The gloss "≈ 0.7/μ" is loose: exactly,
  μ log p* → log 2 + log Γ(2+μ). It is 10–20% off at v = 0.2–0.3.

**"Reading": overstated, fix the wording.** (d) rules out an IFT or contraction in v at v = 0 *in a fixed Banach space*.
It does **not** rule out a scale-of-spaces argument (Ovsyannikov, Nishida–Nirenberg, Nash–Moser). Take
X_r = {Σ c_p τ^p : Σ|c_p| r^p < ∞} and s = r'/r < 1. Then:
- ‖T_μ − I‖_{X_r→X_{r'}} = sup_p (1−R(p))s^p ≤ μ sup_p log(p+3) s^p, which tends to 0 as μ → 0.
- ‖T_μ^{-1}‖_{X_r→X_{r'}} = sup_p s^p/R(p) is finite, of order (r − r')^{−μ}.

Numerics (`tmu.py` §6, s = 0.9): ‖T_μ − I‖ = 0.0085, 0.041, 0.17 and ‖T_μ^{-1}‖ = 1.000, 1.000, 1.013 at μ = 0.01, 0.05,
0.25. The correct reading is therefore: "T_μ loses μ (Mellin) derivatives. A perturbation argument in v must be
loss-tolerant, and no fixed-space IFT works." This agrees with the paper's statement that the linear problem is well posed
in analytic classes for every v < 1. Replace "in any space" with "in any single normed space containing the monomials".

## 5. Reproduction (`code/referee/RA4/`)
- `python straight_run.py`: A4.2 identity and monotonicity; the A4.3 inequality on random runs.
- `python kink_chain.py`: independent exact chain chase; amplification table; Cor. A4.3' including the
  tan²κ₀ > m+1 cases; monotonicity of κ.
- `python kink_circle.py`, `python kink_circle_scaling.py`: a kink on a circular background in the exact chase; m^μ
  scaling.
- `python tmu.py`: A4.4 (a)–(d), the counterexample to the proof step of (c), log p*, and the analytic-scale norms.
- `python compact_checks.py`: Dunkl–Williams constant; the non-nested counterexample; an explicit ε_n → 0 family.

