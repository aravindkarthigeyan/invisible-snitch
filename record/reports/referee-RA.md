# Referee report RA: claims of stream A (`referee/A-claims.md`)

Referee: independent, adversarial. I read only `BRIEF.md`, `paper/main.tex` and `referee/A-claims.md`, plus the
certification scripts in `code/A/` that Props A9/A10 rely on (`certify.py`, `ode_check.py`, `verify_cex.py`, `chase.py`).
I did **not** read `reports/A-1.md`.
All referee code is in `code/referee/RA/` (my own implementation; it does not import `code/A/` except for one cross-check).
Run with PowerShell, `$env:OPENBLAS_NUM_THREADS=1`, from `code/referee/RA/`.

## Verdicts

| Claim | Verdict | One line |
|---|---|---|
| A1 (A(t0) < 2 arccos v, limit as the set fills out) | **OK** (+ convention note) | Correct for the right limit at t0 (chase of S_1). The left limit is θ_N > π. |
| A2 (half-plane persistence) | **OK** | |
| A3 (ordered ⇒ A = β_N ≤ π; switches keep the order) | **OK, with a presentational GAP** (fix below) | The switch argument is right. The base case and the time range have to be stated. |
| A4 (pairwise crossing rule) | **OK** | |
| Cor. A5 (how order is first lost) | **OK** | |
| A6 (radial monotonicity) | **OK** (limited use) | Its premise usually fails at t0. |
| Remark A7 (Abel form) | **OK** | |
| Cor. A8 ((K) holds while ordered) | **OK** (+ a small strengthening) | "generic" is not needed: β_N < π for every finite set. |
| Prop. A9 (certified A > π, v = 1/10) | **OK**: certified, independently re-certified | |
| Prop. A10 (certified W > π, v = 6/25) | **OK**: certified, independently re-certified | |

No ERROR was found.

---

## Lemma A1: OK

Checked each step. At t0 = d/(1−v), h = −d(1−cos α) and C = d g(α) > 0, so h/C < 0 = k(θ*) and b ∈ (θ*, π).
With c = −1 the bracket in (eq. Fprime) is (1+v)(1−cos α) > 0, so b increases in α. The backward ray is invariant.
Reflection handles α ∈ (π, 2π). The θ_i fill an arc of length 2π − 2θ* = 2 arccos v < π, so consecutive unsigned angles telescope. The limit follows from Prop. 4 (`prop:V`).

Numerics (`test_lemmas.py`, part A1). 1400 random sets with v ∈ {0.01, …, 0.95}, N ≤ 30: 0 violations of strict ordering in (θ*, 2π−θ*), of A(t0) = θ_N − θ_1, or of A(t0) < 2 arccos v.
Uniform sets converge to 2 arccos v. For v = 0.2: 2.2836, 2.7088, 2.7370, 2.73876 at N = 10, 10², 10³, 10⁴, against 2.738877.
The "correction to the brief" is right: A(t0) is 2 arccos v, not π.

**Convention note (affects how (H) is stated; it is not an error in A1).** A(t0) here is the right limit: the chase of S_1, polyline S_1…S_N.
During the initial run [0, t0), the target is S_0, the polyline is S_0, S_1, …, S_N, and A(t) = θ_N(t).
In particular A(0) = α_N, and A(t0⁻) = θ_N(t0) ∈ (π, 2π−θ*) whenever α_N > π. Numerically, A(t0⁻) = 4.51 at v = 0.2 for a uniform set.
So if "every time of the discrete chase" in (H) included the initial run, (H) would fail trivially for every set with a direction in (π, 2π).
The proof of Theorem B uses Φ' ≤ … only for t > t0, because Lemma 3 (`lem:start`) bounds Φ(t0).
**Fix:** state (H) and every A-claim for t ≥ t0, with A(t0) the right limit.

## Lemma A2: OK

The rays are invariant, and ρβ' = sin β > 0 on (0, π). Moreover k⁻¹(ℝ) = (0, π), so the bearing never reaches 0 or π. Non-capture follows from Prop. `prop:ray`.
Checked by **direct ODE integration** (DOP853, rtol 1e-11), independently of the exact map: 400 random (v, pairs, durations), 0 violations.
The exact map in `ra_sim.py` agrees with the ODE to 3.7e-13 (`test_sanity.py`).

## Lemma A3: OK, with a presentational GAP

**The switch argument (checked hardest).**
Suppose the chain is ordered at the left limit of leg j: 0 ≤ β_{j+1} ≤ … ≤ β_N ≤ π, measured from u_j.
The new heading is r̂_{j+1}, which is u_j rotated by β_{j+1}. Every remaining bearing becomes β_i − β_{j+1}.
Because β_i ≥ β_{j+1} by the order hypothesis, and the old β_i ≤ π, the new bearings lie in [0, π − β_{j+1}] ⊂ [0, π] and are still nondecreasing.
So yes: when S_j is caught, all remaining bearings are ≥ that of S_{j+1}, and after the turn they stay in [0, π].
The bearings at the left limit are well defined because all non-targets keep ρ > 0 (backward uniqueness and Prop. `prop:ray`).

Within a leg, Lemma A2 keeps every non-target in [0, π]: left points stay in (0, π), and points on the 0-ray and the π-ray stay there.
So the order can only fail through a consecutive pair crossing. (a) is then a telescoping sum: consecutive differences are ≤ π, so each unsigned angle equals β_{i+1} − β_i.

**Edge cases.**

- *Accidental catch.* A candidate is caught accidentally only if it is on the forward ray (bearing 0) and closer than the target. Under the order hypothesis, S_{j+1}, …, S_{i−1} are then also at bearing 0.
  Deleting a term from a nondecreasing sequence in [0, π] leaves one, so the order and A = β_N (last remaining point) survive. The sum over i ≥ j loses a zero angle.
- *Ties at a switch.* If β_{j+1} = β_{j+2}, then S_{j+2} starts leg j+1 on the forward ray. If it is closer than S_{j+1}, it is accidentally caught (case above). If it is farther, it stays at bearing 0 for the whole leg.
  The tie β_i = β_{i+1} is allowed by "≤". Two distinct candidates cannot coincide (backward uniqueness).
- *Points on β = π.* Such a point stays at π within a leg. It becomes the new heading's backward ray only if all remaining points are at π, which is harmless.
  A left point never reaches π (k⁻¹(ℝ) = (0, π)).
  So by induction from t0, where β_N = θ_N − θ_1 < 2π − 2θ* < π, we get **β_N < π strictly for every finite set**, not only for generic sets.
- *Points on β = 0 beyond the target.* They stay at 0, and the order is unaffected.

**GAP (presentational) and fix.**
(c) needs a base case that the proof never states, and the time range must be fixed. Replace (c) by:

> (c) For every finite set 0 = α_0 < … < α_N < 2π, the chain is ordered at t0⁺ (start of the chase of S_1): by Lemma A1, β_i = θ_i − θ_1 ∈ [0, 2π − θ* − θ_1) ⊂ [0, π) and nondecreasing.
> Hence for all t ≥ t0 (A(t0) the right limit) up to the first time at which, inside some leg, two consecutive remaining non-target candidates reverse their bearing order, the chain is ordered and A = β_N < π. Accidental catches delete a bearing-0 point and preserve the order.
> (On [0, t0) the statement is false: A(t) = θ_N(t) > π when α_N > π. See A1.)

**Numerics** (`test_lemmas.py`, `ra_sim.py`; per leg I sample 30 equispaced fractions plus 1 − 10^{−m}, m = 2..12).
The sets are 132 per seed: uniform N ∈ {8, 30, 120}; random N ∈ {3, 6, 15, 40}; twin pairs at gaps 1e-2 to 1e-6; and points clustered near 0 and 2π. Each family is run at v ∈ {0.05, 0.1, 0.2, 0.3, 0.5, 0.7}. Three seeds were run.

| Check | Result |
|---|---|
| Switch preserved order | 0 violations |
| A ≤ π while ordered | 0 violations |
| W ≤ A while ordered | 0 violations |
| Max A while ordered | 3.136 |
| Max A overall | 12.8 (unordered twin sets) |
| Sets that lost order | 66–67 of 132 |
| Order losses located | 221–224 |

An earlier version of my simulator flagged |A − β_N| > 1e-7 in some ordered samples. These were all float cancellation in the target position R_0 − u(1−v)s at s/τ ≥ 1 − 10⁻⁹. After placing the target exactly on the ray, `debug_flags.py` reports 0 flags.
The clean run (seed 2, `test_lemmas_seed2.out`) has 0 violations of every check, including A = β_N while ordered and Remark A7, over 99,912 samples, 77,675 of them ordered and 216 order losses.

## Lemma A4: OK

f(s) = h_P(s)/C_P − h_Q(s)/C_Q with h(s) = h(0) − λs, so f is affine in s. Also β_P < β_Q ⇔ f > 0, because k is decreasing.
(i) needs f ≢ 0. This holds because (C, h) determines the position on one side, so distinct candidates have distinct (C, h); worth adding one clause.
(ii) and (iii) are correct. At a tie, C_P/C_Q = ρ_P/ρ_Q.
ODE test on 400 random pairs, independent of the exact map: k(β_P) − k(β_Q) is affine to 1e-6 relative. There were 121–128 crossings, never more than one per run, and the closer point was the overtaker in 100% of them.

## Corollary A5: OK

The infimum s* of the failure times is an ordered instant (the order condition is closed). A pair reversed at s_n ↓ s* is tied at s*.
A tie at 0 or at π is permanent, so the tie lies in (0, π). The slope of f is negative, so C_i < C_{i+1} and ρ_i < ρ_{i+1}.
Accidental catches inside the leg do not affect this argument.
"First instant of failure" really means the last ordered instant; a wording point only.
Numerics: every one of the 221–224 losses was bisected to 80 steps. Each time the reversed pair was consecutive, non-target, tied in (0, π), with ρ_i < ρ_{i+1} and C_i < C_{i+1} at the leg start. 0 violations.

## Lemma A6: OK (limited use)

At a first zero of g_i, the two points are distinct with equal ρ, so β_i < β_{i+1} in [0, π] and g_i' = cos β_i − cos β_{i+1} > 0, a contradiction. For the target, g_j' = 1 − cos β_{j+1} ≥ 0.
Numerics: 1238–1263 legs satisfied the premise, with 0 violations.
**Caveat:** the premise ρ_j < … < ρ_N typically fails at t0, since S_N starts within O((2π−α_N)^{1−v}) of Harry. So the lemma does not by itself apply to the whole chase.

## Remark A7: OK

The Abel summation is correct, including the case of two points. |e_{i−1} − e_i| = 2 sin(φ/2) ≤ φ.
Identity and bound are checked at every sample, with 0 violations after the cancellation fix.
Turning at t0 for uniform sets: 5.8728 / 5.8798 at N = 10³ / 8·10³ for v = 0.2, against 2π − 2 arcsin v = 5.8805. For v = 0.5: 5.2340 / 5.2359 against 5.2360. So the claim holds in the limit, approached from below.

## Corollary A8: OK

It combines Lemma 2 (W ≤ A) with A3(a). Strengthening: "β_N ∈ (0, π) for a generic set" can be replaced by **β_N ∈ [0, π) for every finite set**, by the induction in A3.

Numerical side-claims (`test_uniform.py`, uniform sets):

| v | N | sup A while ordered | sup A after first loss | first loss at leg | remaining then |
|---|---|---|---|---|---|
| 0.2 | 50 | 2.922 | — (never lost) | — | — |
| 0.2 | 200 | 2.991 | 0.033 | 193 / 199 | 6 |
| 0.2 | 1000 | 3.059 | 0.144 | 927 / 999 | 72 |
| 0.5 | 50 | 2.721 | 0.082 | 45 / 49 | 4 |
| 0.5 | 200 | 2.804 | 0.192 | 170 / 199 | 29 |
| 0.5 | 1000 | 2.907 | 0.296 | 807 / 999 | 192 |

This agrees with "A ≤ 0.32 in the end phase". A's figure for v = 0.5, N = 50 is 2.62; mine is 2.72, probably a different N or sampling convention, which is immaterial.
**Note:** the end phase grows with N: 192 of 999 points remain at the first loss for v = 0.5. So the open part of (K) is not a "few last points" phenomenon.

## Props A9 and A10: OK

### Re-running the authors' script

`code/A/certify.py` reproduces both certificates exactly:

- **A9:** A − π ∈ [0.1498600678069104…, …], with width about 3e-41.
- **A10:** W − π ∈ [0.909319036919724…, …], and A − π = 2.73196…

### Audit of `certify.py`

- **Input enclosure.** `iv.mpf('1.278182093392')` returns a genuine two-sided enclosure (checked). v = vn/vd is computed as an interval quotient.
- **Rounding.** I read the mpmath 1.3.0 source. `mpi_exp`, `mpi_log`, `mpi_cos_sin` and `mpi_atan2` use round_floor / round_ceiling on the endpoints, and division and sqrt are outward-rounded.
  tanh and cosh are built from `iv.exp` by interval operations, which gives valid (if wider) enclosures.
  One quirk: `mpi_atan2` returns π for y = [0, 0] with x straddling 0, which is wrong. It is unreachable here, because y = |cross| is never the exact zero interval at these configurations; certified bounds are about 1e-41 wide.
- **Trajectory, not just a final formula.** Each straight run uses the proved exact solution of Prop. 1. The point is certified off the heading line (the script aborts otherwise), so C > 0 is constant and the run cannot catch it.
  The catch times t0 = 1/(1−v) and τ_1 = ρ_1/(1−v) come from Prop. `prop:ray` and Lemma 2, evaluated on the enclosure of ρ_1.
  The inversion β = k⁻¹(h/C), done in u = log tan(β/2), is certified by checking k(u_lo) > sup q and k(u_hi) < inf q in interval arithmetic, with k strictly decreasing (Lemma 1). This is sound even if the endpoint conversions round inward.
  The heading (u_x, u_y) is an interval box that contains non-unit vectors. This is still rigorous: the map is evaluated as an interval extension at a box containing the true heading.
- **Chase legitimacy.** α_0 = 0 is implicit and caught at t0. The listed α's are strictly increasing in (0, 2π); for A9 the last one is 2π − 0.0100000000006, so all gaps are ≥ 0.01. Leg 1 targets S_1.
  Accidental catches are excluded rigorously, since every non-target is certified off the forward ray. No skipped candidate is mishandled.
  v = 1/10 and v = 6/25 = 0.24 are both below 1/(1+π) ≈ 0.24145.

### Independent re-certification (`ra_certify.py`)

This uses a different code path: polar form (ρ, world angle), k inverted directly in β with a certified bracket, and A computed as Σ|b_{i+1} − b_i| after certifying every bearing in [0, π]. It also certifies A1's ordering at t0 and the legitimacy of the set.

- **A9:** A = [3.29145272139670365444695723431000220120…] and A − π ≥ 0.149860067806. W = 2.0989521105716576…
- **A10:** A − π ≥ 2.73196084721, and W − π ∈ [0.909319036919724, 0.909319036919724] at 50 digits.

Both match `certify.py` to every printed digit.

### Time profile (`scan_cex.py`, mpmath 60 digits)

- **A9:** order is lost between s/τ = 0.99 and 0.999. A > π on the whole interval s/τ ∈ [0.999, 1), rising to 3.29161. W stays ≤ 2.17 < π throughout.
  So A9 refutes (H) on an open time interval, but not the inequality W ≤ π that Theorem B actually uses.
- **A10:** W ≤ 2.29 up to s/τ = 1 − 10⁻⁹, then rises to 4.054 in the left limit. The caveat in the claim is accurate: the violation is momentary and gives a negligible increase of Φ.

A small inaccuracy: the "ODE check W = 4.0508" for A10 is a double-precision ODE at s/τ = 1 − 10⁻¹², which is good to only about 4 digits (the certified value is 4.05091). That is harmless, since the interval certificate is the proof.
The numerical-only side claims also reproduce, approximately, with my simulator:

| Claim | Claimed | Mine | Note |
|---|---|---|---|
| v = 0.35 seven-point set (`verify_cex.py` re-run): A | 4.95 | 4.9517 | |
| v = 0.2 twin set: sup A | 5.867 | 5.852 | my time sampling is coarser near the catch |
| v = 0.2 twin set: sup W | 3.988 | 3.980 | same |

**Consequence for Theorem B.** I agree. Under the reading t ≥ t0, (H) is false for some finite sets.
Under the literal reading that includes [0, t0), it is false for every set with a direction in (π, 2π); see A1.
The proof of Theorem B already says that only the nested dyadic family needs (H). The statement should be changed to:

> **(H_dyadic)** for the sets D_k = {2πi/2^k} and all t ≥ t0, A ≤ π, or more economically W ≤ π.

## Sanity of my simulator (rule 4)

`test_sanity.py`: the exact map agrees with DOP853 to 3.7e-13. The total chase time for v = 0.2 and 0.3 with 2000 directions is 13.213 and 18.967. That agrees with `code/A/chase.py` to 1e-13, increases with N (13.162, 13.194, 13.213, 13.224 for N = 500, 1000, 2000, 4000), and is consistent with the paper's 13.24 / 19.08 only as N grows. The paper's table entry at "2000 candidates" is about 0.2–0.6% higher than both simulators give at N = 2000; this is worth a look by whoever owns that table.

## Reproduce

```
cd code/referee/RA
python test_sanity.py
python test_lemmas.py 0        # also 1, 2 (output of seed 2 in test_lemmas_seed2.out)
python debug_flags.py          # 0 flags after the cancellation fix
python test_uniform.py 50 200 1000
python ra_certify.py 1/10 "1.278182093392,1.288182093392,1.38054291417,6.253166882374,6.263185307163,6.273185307179" 0.999999
python ra_certify.py 6/25 "0.412411719969,0.41241171997,0.696029615234,1.331539471428,2.98214094828,3.518379401584,6.035941613736,6.283185299154" 0.999999999999
python scan_cex.py
python ../../A/certify.py 1/10 "<A9 set>" 0 0.999999 W   # authors' certificate, reproduced
```
