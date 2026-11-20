# Referee report RA2 — stream A-2 claims (`referee/A2-claims.md`)

Referee: independent (did not read reports/A-2.md or code/A2/). Inputs: BRIEF.md §1–2, paper/main.tex §4–5 and
"The angle hypothesis", referee/A2-claims.md. Scripts: `code/referee/RA2/` (commands in §5).

## 0. Verdicts

| Claim | Verdict |
|---|---|
| Lemma A2.1(a) \|β_i\| ≤ A, W ≤ A | **OK** |
| Lemma A2.1(b) \|β_i\| nondecreasing in a leg; (E_γ) decided at leg ends | **OK** |
| Lemma A2.1(c) D never jumps up; D(s2−) ≤ D(s1) − (cos γ − v)(s2 − s1) | **OK** (the proof integrates each ρ_i, so a change of maximiser needs no Dini derivative) |
| Lemma A2.1(d) D ≤ Φ | **OK** |
| Prop. A2.2 (E_γ), (E'_γ), (E_K) | **OK**, with one sentence to add for (E'_γ) (G1) |
| Theorem A2.3 (i), (ii), λ = 0 versions, M₁ and M₂ | **OK (conditional)**. Two small gaps: t_f must be defined (G2), and the claim "PROVED (conditional)" depends on a hypothesis with a uniform constant, which the numerics do not yet support (G3; this does not affect validity) |
| v1 = 0.4747526, explicit-bounds table, γ = 0.5 row | **OK**: reproduced to all printed digits (±0.01) |
| Remark 4.2 (edge formula, cone example) | **OK**, but the last sentence overstates (G4) |
| §4.3 structure (mirror order, Φ⁺ identity, Φ⁺ ≤ 2Φ⁻) | **OK**. One sentence is wrong as written (G5) |
| §4.4 half-plane claim, Φ_s′ bound, Δ ≤ 2\|PQ\| | **OK**. The rule at t0 must be specified (G6) |

No ERROR found. All gaps below are fixable in a sentence or two.

## 1. Step-by-step check

**A2.1(a).** For bearings in (−π, π], |β_i| is the geodesic distance on S¹ between u = r̂_j and r̂_i, and a_k is the
geodesic distance between r̂_k and r̂_{k+1}. The triangle inequality gives |β_i| ≤ Σ_{k=j}^{i−1} a_k ≤ A. This holds
for any configuration, not only for chase states. Off catch instants every remaining ρ_i > 0, so every r̂_i is
defined. W ≤ A is Lemma 2. Verdict: correct.

**A2.1(b).** This is Lemma A2 (half-plane persistence): a bearing in (0, π) increases, a bearing in (−π, 0) decreases,
and the two rays are invariant. A candidate caught accidentally has β = 0, so removing it never lowers the maximum
below an earlier value. The bearing of a remaining candidate is continuous up to and including the catch of the
target, because that candidate stays at positive distance. So sup_{[s, t_c)} max|β| equals the value at t_c measured
from the old heading, and it is attained.

At the catch instant the convention ("leg containing t") does not matter: the next leg starts with values that are
again bounded by that leg's own end value. So (E_γ) holds iff, for every leg ending after t_f, max_i |β_i| at its end
(old heading) is ≤ γ. Verdict: correct.

**A2.1(c).** On an open leg interval ρ_i′ = v − r̂_i·u = v − cos β_i for every remaining i (target included:
ρ_j′ = −(1−v)). The proof fixes s, picks a maximiser i at s, and integrates ρ_i′ ≤ v − cos γ over (s1, s). That
candidate is remaining on the whole of [s1, s], and its bearing bound on (s1, s) follows from the hypothesis.
Continuity at s1 holds because positions are continuous. So D(s) ≤ D(s1) − (cos γ − v)(s − s1) for every s, however
often the maximiser changes, and no derivative of D is needed. At a catch, planned or accidental, the removed point
has ρ = 0 and the others are continuous, so D does not jump up. In fact D is continuous except at T_end.
Verdict: correct.

**A2.1(d).** ρ_i ≤ |S_j − H| + Σ_{k=j}^{i−1}|S_{k+1} − S_k| ≤ Φ by the triangle inequality along the polyline of
remaining candidates. Verdict: correct.

**Prop. A2.2.**
- T_end is finite (finitely many legs, each of length ρ_j/(1−v)).
- D > 0 on [t_f, T_end): no two candidates are at H at the same instant (backward uniqueness, Corollary E2), and the
  caught point is removed at its catch.
- Chaining (c) across legs (D has no upward jumps) gives 0 < D(t) ≤ D(t_f) − c(t − t_f) for t < T_end. Letting
  t ↑ T_end gives the bound.

The (E_K) case is Lemma 2 plus downward jumps plus Φ ≥ D > 0. Verdict: correct.

> **G1 (wording, (E'_γ)).** ρ_{N(t)} jumps *up* if S_{N(t)} is caught accidentally, so the tail argument needs
> "no upward jump". Add this sentence: "Under (E'_γ), S_{N(t)} is never caught accidentally before T_end. An
> accidental catch puts it on [H, S_j] closer than S_j, so it would not be the farthest point. Hence
> ρ_{N(t)} = D on [t_f, T_end), and the D-argument applies with only β_N bounded, because the maximiser is S_N
> throughout."

**Theorem A2.3.** Checked line by line.

1. **Ordered phase.** On [t0, t_f] the chain is ordered, so A = β_N ∈ [0, π] and W ≤ β_N. Lemma B1 then gives
   Ψ′ ≤ −[(1−λ)(1−v) + λ(1 − cos x) − vx] at x = β_N, which is ≤ −m(v, λ). Sign and argument are correct.
2. **Jumps.** Ψ jumps only downward:
   - at an accidental catch of an interior candidate, Φ drops and ρ_N is unchanged;
   - at an accidental catch of S_N itself, Φ drops by ρ_prev and −λρ_N drops by λρ_prev, where ρ_prev is the
     distance of the new last candidate. The claims file writes ρ_{N−1}; that is correct when S_{N−1} is still
     uncaught;
   - at planned catches Φ is continuous, and ρ_{N(t)} is continuous except at T_end.

   Ψ is C¹ on open legs between the finitely many accidental catches. Hence Ψ(t_f) ≤ Ψ(t0) − m(t_f − t0).
3. **Is Ψ(t_f) carried into the end-phase bound correctly?** Yes. If t_f is an accidental-catch time, use the
   post-jump value: it is ≤ Ψ(t_f−), so the ordered-phase inequality still holds. D(t_f) and Φ(t_f) are taken after
   the deletion, consistently. Then:
   - T_end − t_f ≤ D(t_f)/c_E ≤ Φ(t_f)/c_E ≤ Ψ(t_f)/((1−λ)c_E), using (d) and (1−λ)Φ ≤ Ψ;
   - Ψ(t_f) ≥ 0 and Ψ(t0) − Ψ(t_f) ≥ 0, so (Ψ(t0) − Ψ(t_f))/m + Ψ(t_f)/((1−λ)c_E) ≤ Ψ(t0)/μ with
     μ = min{m, (1−λ)c_E}.
4. **The formula for M.** For each admissible λ, T_end ≤ t0 + 2πd/((1−v)μ(λ)). An infimum of valid upper bounds
   is a valid upper bound, so the sup in M₁ and M₂ need not be attained.
   - M > 0 iff some λ has m(v, λ) > 0, i.e. v < v1, because max_λ m is strictly decreasing in v. Then
     (1−λ)c_E > 0 since λ < 1.
   - With λ = 0, m = 1 − v(1+π), which gives the stated Φ-only versions.
   - (ii) is consistent with B2, and is slightly better than bounding Ψ′ directly under W ≤ K, because
     (1−λ)(1−v−vK) ≥ (1−λ)(1−v) − vK.
5. **Uniformity and Lemma 4.** T depends only on (d, v, γ) or (d, v, K). Each H_k is constant after its last catch,
   so it is 1-Lipschitz on [0, T], and Lemma 4 applies to the nested family. The limit path has speed ≤ 1, not
   exactly 1, and the claim states |H′| ≤ 1 correctly. The paper's statement should repeat that remark.

> **G2 (definition of t_f).** The claims file never defines t_f. Write t_f := inf{t ≥ t0 : the chain is not ordered
> at t}, and t_f := T_end if the chain is never disordered. Then:
>
> - The chain is ordered on all of [t0, t_f]: order is closed within a leg, preserved at switches (Lemma A3(b)),
>   and accidental catches remove only β = 0 points.
> - t_f is attained as a tie of a consecutive pair (Lemma A4). The affine law excludes a touch without crossing,
>   so t_f is well defined.
> - Order **is** regained and lost again after t_f in practice. In my random-set chases (900 sets, §2.3) up to 14
>   regains after t_f occur, and the certified set of Prop. A9 regains order once. The theorem tolerates this,
>   because (E_γ) and (E_K) are imposed on all of [t_f, T_end) and the proof uses no ordering after t_f. Say so.
>
> Optional strengthening, for free: the proof works verbatim with t_f replaced by any τ_k such that the chain is
> ordered on [t0, τ_k] and (E) holds on [τ_k, T_end). Assuming (E) only after the *last* such τ, rather than after
> the first loss of order, is strictly weaker.

> **G3 (status of the hypothesis; not a flaw in the proof).** The constants γ and K must be uniform over the whole
> family. In my dyadic chases they have not saturated by N = 2047 (§2.4):
>
> - γ_obs(v = 0.2) = 0.096, 0.145, 0.199 for N = 2⁹, 2¹⁰, 2¹¹;
> - γ_obs(v = 0.4) = 0.228, 0.284, 0.331;
> - K_obs(v = 0.2) = 0.0033, 0.0085, 0.0162, roughly ×2 per doubling.
>
> These are still far below arccos v and (1−v)/v, so there is no contradiction. But the theorem's hypothesis is
> supported only by extrapolation, which the "PROVED (conditional)" label should not hide. The explicit-bounds table
> uses γ = γ_∞ + 0.05 and K = W_∞ + 0.1 from extrapolations I did not check. Label those constants NUMERICAL.

## 2. Numerical evidence

Method: my own simulator `sim.py`, written independently of the team's code.
- **Exact straight-run map.** Uses x = log tan(|β|/2), C = ρ·g(β) constant, and k(x) = h/C decreasing. Bearings come
  from a vectorised log-form bisection, which is accurate at β → 0 and β → π.
- **Exact t_f.** The first loss of order is located from the affine crossing law of Lemma A4, not by sampling.
- **Samples per leg.** 9 equispaced samples plus 6 clustered at the catch (1 − 10⁻ᵏ)τ. The special sets use 200 + 12.

### 2.1 Validation
- The map agrees with RK45 (rtol 1e-12) on 1000 random legs: max relative position error 9.95e-12.
- Uniform N = 2000 chase: T_end = 13.2127, 18.9669, 28.8100, 47.0409 at v = 0.2, 0.3, 0.4, 0.5. This reproduces the
  team's N = 2000 values 13.21/18.97/28.81/47.04 (STATE.md, stream F).
- The two A-1 sets of §4.1 give sup_{t≥t_f} max|β| = 3.1305 (A9 set, v = 0.1) and 3.1186 (robust set, v = 0.2). This
  agrees with the claimed 3.130 and 3.119.

### 2.2 Static and single-leg tests (`check_static.py 4000`)
- **Test set.** 36 000 configurations over 4000 random chain states of five kinds: generic, narrow cone,
  near-equal distances (the maximiser of ρ switches), near-radial zigzag, and near-twins at 1e-7. Each state was
  sampled at 9 times along a straight leg towards its first point, including τ(1 − 1e-7) and τ.
- **Results.**
  - 0 violations of |β| ≤ A (worst |β| − A = 4.4e-16), W ≤ A, or D ≤ Φ.
  - 0 violations of the edge formula w = (ρ_P + ρ_Q)(1 − cos a)/ℓ = cos b + cos c.
  - (c) was tested for every pair s1 < s2 with γ = max|β| on [s1, s2]: 0 violations, worst slack +6.8e-13 (rounding).
- **Flags traced to rounding.** Early runs flagged a few W > A and |β| > A cases. All came from cancellation at
  near-twin edges (ℓ ~ 1e-8). Recomputing the flagged states in 50-digit arithmetic (`diag_W2.py`) gives W < A with
  margin ≈ 5e-10. After removing the cancellation (unit vectors from exact bearings, 2 sin²(a/2) instead of 1 − cos a,
  edge length from (ρ_P, ρ_Q, a)), the flags disappear (`diag_rand132b.py`).

### 2.3 Simulated chases on random sets (`check_chase.py random 300 {11,12,13}`)
- **Sets.** 900 sets with v ∈ [0.02, 0.47] and 2–40 directions; 40% have a near-twin at 1e-9 … 1e-3 and 30% a
  geometric cluster.
- **Checks along every chase.** All give 0 violations or flags.
  - Lemma A2.1(a)–(d), plus (b) as monotonicity of |β_i| within each leg;
  - "(E_γ) can be checked at leg ends": dense γ_obs equals leg-end γ_obs in every chase;
  - Ψ(t2) − Ψ(t1) ≤ −m(v, λ)(t2 − t1) on the ordered phase, for λ ∈ {0, 0.2, 0.4, λ*, 0.8}, and
    Ψ(t_f) ≤ Ψ(t0) − m(t_f − t0);
  - D(t) ≤ D(t_f) − (cos γ − v)(t − t_f) on the end phase, whenever cos γ_obs > v;
  - Prop. A2.2 under (E_γ), (E'_γ) and (E_K), with γ and K set to the observed sups;
  - T_end − t0 ≤ Ψ(t0)/μ (both cases), T_end ≤ T, and Φ(t0) ≤ 2π/(1−v).
- **End phases.** 710 of the 900 chases have a nonempty end phase. Only 87 of them satisfy cos γ_obs > v: random sets
  generally violate (E_γ), consistent with §4.1. (E_K) holds in most of them, with the bound satisfied.
- **Regains after t_f.** Histogram over the 900 chases: 0 regains in 207 chases, 1–5 in 555, and 6–14 in the remaining 138.

### 2.4 Dyadic chases (`check_chase.py dyadic ...`; N = 2^k − 1 non-zero directions)

| v | N | t_f | T_end | γ_obs | K_obs | T_end − t_f | D(t_f)/(cos γ − v) | Φ(t_f)/(1−v−vK) | (T_end−t0)/(Ψ(t0)/μ) | T (claimed bound) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.05 | 2047 | 8.319 | 8.339 | 0.0022 | 0.0000 | 0.0192 | 0.0192 | 0.0192 | 0.209 | 8.70 |
| 0.1 | 511 | 9.524 | 9.610 | 0.0058 | 0.0000 | 0.0856 | 0.0856 | 0.0856 | 0.215 | 10.58 |
| 0.2 | 511 | 12.212 | 13.164 | 0.0955 | 0.0033 | 0.9517 | 0.9561 | 0.9522 | 0.211 | 16.87 |
| 0.2 | 1023 | 11.938 | 13.195 | 0.1450 | 0.0085 | 1.2569 | 1.2700 | 1.2588 | 0.211 | 16.87 |
| 0.2 | 2047 | 11.680 | 13.213 | 0.1988 | 0.0162 | 1.5335 | 1.5635 | 1.5380 | 0.211 | 16.87 |
| 0.3 | 511 | 16.038 | 18.838 | 0.1813 | 0.0123 | 2.8001 | 2.8541 | 2.8106 | 0.036 | 31.78 |
| 0.4 | 1023 | 21.440 | 28.666 | 0.2837 | 0.0312 | 7.2262 | 7.6307 | 7.3302 | 0.049 | 91.79 |
| 0.4 | 2047 | 20.862 | 28.814 | 0.3313 | 0.0432 | 7.9527 | 8.5688 | 8.1124 | 0.049 | 91.79 |
| 0.45 | 2047 | 25.151 | 36.443 | 0.3320 | 0.0429 | 11.2918 | 12.2581 | 11.5641 | 0.091 | 312.54 |

- The last column is T for the observed γ, which matches the γ = 0.5 row of the claims to within 0.01.
- For N ≤ 127 and v ≤ 0.2, order is never lost: t_f = T_end and the end phase is empty.
- All dyadic chases (k = 3, 5, 7, 9, 10, 11) gave 0 violations of every check listed in §2.3.
- Prop. A2.2 is nearly sharp: duration/bound = 0.95–0.999.
- The full bound is very loose: T_end ≈ 0.04–0.24 of the bound.
- γ_obs and K_obs grow with N (G3).

### 2.5 End-phase bounds from arbitrary chain states (`check_endphase_states.py 2000`)
Chases were started from random cone or zigzag chain states (not reachable states). The bounds are tested against the
γ, γ_N and K observed over the whole run:
- (E_γ): T_end ≤ D(0)/(cos γ − v) in all 45 cases where cos γ > v. Max ratio 0.9997, median 0.77, so the bound is
  essentially sharp.
- (E'_γ): 0 violations in 46 cases.
- (E_K): 0 violations in 267 cases.

### 2.6 Constants (`constants.py`)
- v1 = 0.474752638 and λ* = 0.6551824, matching the paper to the 9 digits computed.
- The explicit-bounds table is reproduced exactly: T(i) = 163.67, 55.33, 34.07, 37.43, 43.41, 91.79, 312.54 and
  T(ii) = 8.81, 10.81, 16.93, 21.15, 31.78, 91.79, 312.54.
- The γ = 0.5 row gives 21.34, 31.78, 49.27, 91.79, 312.54 against the claimed 21.35 at v = 1/(1+π), a rounding
  difference.

## 3. Remark 4.2, §4.3, §4.4

**Remark 4.2. OK.**
- The identity (r̂_Q − r̂_P)·(ρ_Q r̂_Q − ρ_P r̂_P) = (ρ_P + ρ_Q)(1 − cos a) is correct (it is Lemma E1). It was also
  checked numerically against cos b + cos c.
- The zigzag example is reproduced. At δ = 0.5, n = 100, η = 1e-6: max|β| = 0.5, A = 50, W = 49.48 = 2n sin(δ/2),
  D = 1.0, Φ = 50.5.

> **G4.** "Hence no Φ- or Ψ-type functional can be certified from a cone" should read "…from a cone condition alone".
> The example shows that the pointwise implication cone ⇒ bounded W fails. It does not show that such states occur
> in a dyadic chase. That is all §A2.3(i) needs to justify switching to D.

**§4.3 structure. OK.**
- At a tail fold (S_{N−1} ∈ [H, S_N], chain ordered up to N−2), the new bearings β_i − β_N ∈ [−β_N, 0] are
  non-increasing along (S_{N−1}, S_N, S_{N−2}, …, S_j). This is mirror order.
- Φ⁺ − Φ⁻ = ρ_{N−1} − ρ_j + |S_N S_{N−2}| − ℓ_{N−2}. With ρ_{N−1} = ρ_N − ℓ_{N−1} this is the stated formula. The
  bracket is ≤ 0 by the triangle inequality, and ρ_N ≤ Φ⁻.
- On 5000 random folds: max |Φ⁺ − formula| = 7e-15, and 0 violations of either inequality or of mirror order.
- The ρ′ comparison (ρ_P − ρ_Q)′ = cos β_Q − cos β_P ≤ 0 for |β_P| ≤ |β_Q| is correct.

> **G5.** "the reversed chain has ρ decreasing along it" is false at its first edge (ρ_{N−1} < ρ_N). Beyond that edge
> it is a property of the observed dyadic folds, not a consequence of the structure. Restate it as "from S_N on, ρ
> decreases along the reversed chain in the observed folds (NUMERICAL)". I did not re-run the T = 42.67 / 8·10²⁰
> numerics.

**§4.4. OK.**
- Within legs, Lemma A2 keeps bearings in [0, π]. At a switch the new bearings are β_i − β_min ∈ [0, π − β_min].
- Between ties, W_s ≤ A_s = β_max ≤ π, because consecutive angles telescope. Lemma 2's identity holds for any fixed
  ordering of the polyline that starts at the target.
- At a tie, P (closer) overtakes Q (Lemma A4), so the order (X, P, Q, Y) becomes (X, Q, P, Y), and
  Δ = (|XQ| − |XP|) + (|PY| − |QY|) ≤ 2|PQ|. On 200 000 random and near-radial ties the max of Δ/(2|PQ|) is
  1.000000 with 0 violations, and the sup 1 is approached when X–P–Q–Y are nearly collinear along the ray.
- Edge cases:
  - a missing neighbour gives Δ ≤ |PQ|;
  - a simultaneous k-fold tie reverses a block and gives Δ ≤ 2|first − last|;
  - accidental catches only lower Φ_s.

> **G6.** The rule needs its start specified. At t0 the bearings θ_i ∈ (θ*, 2π − θ*) (measured from the initial
> heading) straddle the backward ray. "Smallest bearing" in (−π, π] would pick a middle candidate (θ just above π),
> and then the half-plane claim fails at once. Fix: "the first target is S_1, i.e. bearings at t0 are measured
> counterclockwise in (θ*, 2π − θ*); thereafter the smallest bearing". The spread 2 arccos v < π then gives [0, π)
> after the first switch. Also say that ties for the smallest bearing are broken by the closer point.

## 4. Limits and regularity
- **Accidental catches.** The simulator only treats exact forward-ray points as accidental. 0 near-ray events
  (|β| < 1e-12) occurred in any chase, so no accidental catch was exercised numerically. The proofs handle
  accidental catches correctly: D, Φ and Ψ all jump down or stay continuous.
- **Ties.** Bearing ties are measure-zero events located exactly by the affine law. Collinear triangles are harmless
  (Lemma 2), and the closed-condition argument for t_f is correct.
- **Final leg.** Only the target remains, so max|β| = 0 and D = ρ_j decreases at rate 1 − v ≥ cos γ − v. At T_end,
  D = Φ = Ψ = 0, so the case t_f = T_end (empty end phase) is consistent.
- **Uniformity in N.** Proved given the hypothesis (T is independent of k). Not supported yet by the data (G3).

## 5. Reproduction (PowerShell, `$env:OPENBLAS_NUM_THREADS=1`, in `code/referee/RA2/`)
- `python validate.py`: RK45 agreement and the N = 2000 times (≈ 5 min).
- `python constants.py`: v1, λ*, the table and the γ = 0.5 row.
- `python check_static.py 4000`: §2.2, Remark 4.2, §4.3, §4.4 (output `out_static.txt`).
- `python check_chase.py special | random 300 11 | random 300 12 | random 300 13 | dyadic 0.05,0.1,0.2,0.3,0.4,0.45 3,5,7,9 | dyadic 0.05,0.2,0.4,0.45 10,11`
  (outputs `out_*.txt`; the N = 2047 runs take ≈ 3.5 min each).
- `python check_endphase_states.py 2000`: §2.5.
- `python diag_W2.py` and `python diag_rand132b.py`: the rounding diagnoses in §2.2.

