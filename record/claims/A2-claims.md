## 3. Proved results: the end phase reduces to one condition (PROVED)

Setting: any finite direction set containing 0, the chain chase of Section 4 of the paper (accidental catches handled as
there).

**Hypothesis (E_γ)** (for a finite set and γ ∈ [0, π)): at every t ∈ [t_f, T_end), every remaining candidate (target
included) has |β_i(t)| ≤ γ, bearings measured from the heading of the leg containing t.
Tail variant **(E'_γ)**: at every such t, |β_N(t)| ≤ γ and S_N is the farthest remaining candidate.
**Hypothesis (E_K)**: at every t ∈ [t_f, T_end) off the catch times, W(t) ≤ K.

### Lemma A2.1 (cone facts). PROVED
For every finite set and every time of the chain chase:
(a) every remaining candidate has |β_i| ≤ A, and W ≤ A;
(b) within a leg every |β_i| (i ≠ target) is nondecreasing; hence the sup over a leg of max_i |β_i| is its left limit at
the catch, and (E_γ) can be checked exactly from the configurations at the ends of the legs;
(c) D(t) := max over remaining candidates of ρ_i(t) never jumps up; if on an open leg interval (s1, s2) all remaining
candidates have |β_i| ≤ γ, then D(s2−) ≤ D(s1) − (cos γ − v)(s2 − s1);
(d) D ≤ Φ.

*Proof.* (a) |β_i| is the angular distance on the unit circle between u = r̂_j and r̂_i; by the triangle inequality for
angular distance it is ≤ Σ_{k=j}^{i−1} ∠(r̂_k, r̂_{k+1}) = Σ_{k<i} a_k ≤ A. W ≤ A is Lemma 2 of the paper.
(b) Lemma A2 of A-1: a left point's bearing increases strictly, a right point's decreases strictly, points on the
forward/backward ray stay there; a candidate caught accidentally is on the forward ray (β = 0) and is removed.
(c) On an open leg interval each ρ_i is C¹ with ρ_i' = v − cos β_i ≤ v − cos γ (cos decreases on [0, π]). For
s1 < s < s2 pick i with D(s) = ρ_i(s); then D(s) ≤ ρ_i(s1) − (cos γ − v)(s − s1) ≤ D(s1) − (cos γ − v)(s − s1); let
s ↑ s2 (each ρ_i is continuous). At a catch (planned or accidental) a candidate at distance 0 is removed and the others'
distances are continuous, so D does not jump up.
(d) ρ_i ≤ |S_j − H| + Σ_{k=j}^{i−1} |S_{k+1} − S_k| ≤ Φ. ∎

### Proposition A2.2 (end-phase duration). PROVED
If (E_γ) holds with cos γ > v, then T_end − t_f ≤ D(t_f)/(cos γ − v) ≤ Φ(t_f)/(cos γ − v). The same holds under (E'_γ)
with D replaced by ρ_N. If (E_K) holds with K < (1−v)/v, then T_end − t_f ≤ Φ(t_f)/(1 − v − vK).

*Proof.* D(t) > 0 for t < T_end (a remaining candidate not at H has ρ > 0), and by Lemma A2.1(c),
0 < D(t) ≤ D(t_f) − (cos γ − v)(t − t_f). Tail variant: ρ_N = D under (E'_γ) and ρ_N' = v − cos β_N. For (E_K): by Lemma 2,
Φ' = −(1−v) + vW ≤ −(1 − v − vK) between catches, Φ is continuous with only downward jumps, and Φ > 0 before T_end. ∎

*Remark.* (E_γ) asks nothing about ordering, W or A. The bound is nearly sharp numerically (§2.4).
*Numerical test of Lemma A2.1(a)–(d)* (`check_lemmas.py 300`): 300 random sets (v ∈ [0.02, 0.7], 2–25 directions, 30%
with a near-twin at gap 1e−9…1e−3), 48072 configurations (12 times per leg): 0 violations of each inequality.

### Theorem A2.3 (capture conditional on an end-phase hypothesis only). PROVED (conditional)
Let D_1 ⊂ D_2 ⊂ … be finite direction sets containing 0 with dense union (e.g. dyadic), v < v1 = 0.4747526.
(i) If there is γ with cos γ > v such that (E_γ) (or (E'_γ)) holds for the chase of every D_k, there is a path with
|H'| ≤ 1 catching every direction exactly by
  **T = d/(1−v) + 2πd/((1−v) M₁),  M₁(v,γ) = sup_{0≤λ<1} min{ m(v,λ), (1−λ)(cos γ − v) } > 0.**
(ii) If there is K < (1−v)/v such that (E_K) holds for every D_k, the same holds with
  **M₂(v,K) = sup_{0≤λ<1} min{ m(v,λ), (1−λ)(1 − v − vK) } > 0.**
Taking λ = 0 gives the Φ-only versions for v < 1/(1+π), with min{1 − v(1+π), cos γ − v} resp. 1 − v − v·max(π, K).

*Proof.* Fix k and λ ∈ [0,1) with m(v,λ) > 0 (possible iff v < v1). Ordered phase [t0, t_f]: by Lemma A3(a) of A-1,
A = β_N ∈ [0, π] and W ≤ A, so by Lemma B1(c) of B-1, on each open leg
Ψ' = −(1−λ)(1−v) + vW − λ(1 − cos β_N) ≤ −[(1−λ)(1−v) + λ(1 − cos x) − vx]_{x=β_N} ≤ −m(v,λ).
Ψ is continuous except for downward jumps at accidental catches (Lemma 2 of the paper; B-1 §3 remark: if S_N itself is
caught accidentally, Φ drops by ρ_{N−1} and −λρ_N drops by λρ_{N−1}), so Ψ(t_f) ≤ Ψ(t0) − m (t_f − t0), and
Ψ(t0) ≤ Φ(t0) ≤ 2πd/(1−v) (Lemma 3 of the paper). End phase: by Prop. A2.2 and (1−λ)Φ ≤ Ψ (B1(a)),
T_end − t_f ≤ Ψ(t_f)/((1−λ)c_E) with c_E = cos γ − v (case i) or 1 − v − vK (case ii). With μ = min{m, (1−λ)c_E},
T_end − t0 ≤ (Ψ(t0) − Ψ(t_f))/m + Ψ(t_f)/((1−λ)c_E) ≤ Ψ(t0)/μ ≤ 2πd/((1−v)μ).
After its last catch H_k stays put, so every H_k is 1-Lipschitz on [0, T] with T independent of k; Lemma 4 of the paper
gives the limit path. Optimise over λ. ∎

*What is new.* Theorem B needed (H) on the whole chase; B2 needed (K) on the whole chase. A-1 showed both hold up to t_f.
Part (ii) is B2 + A-1's Cor. A8, stated with the end-phase hypothesis in its simplest form. Part (i) is new: the end phase
can also be closed by a pure cone condition through the farthest-point functional D, which needs no control of W.

*Explicit bounds* (`tbound.py`, `tbound2.py`, d = 1; constants γ = γ_∞ + 0.05, K = W_∞ + 0.1 from §2.3):

| v | γ | T via (i) | K | T via (ii) | T_B2 (B's bound, (K) everywhere) |
|---|---|---|---|---|---|
| 0.05 | 1.48 | 163.7 | 0.92 | 8.81 | 8.70 |
| 0.10 | 1.34 | 55.3 | 0.80 | 10.81 | 10.58 |
| 0.20 | 1.10 | 34.1 | 0.55 | 16.93 | 16.87 |
| 0.24 | 1.025 | 37.4 | 0.50 | 21.15 | 21.15 |
| 0.30 | 0.89 | 43.4 | 0.38 | 31.78 | 31.78 |
| 0.40 | 0.73 | 91.8 | 0.27 | 91.79 | 91.79 |
| 0.45 | 0.61 | 312.5 | 0.21 | 312.5 | 312.5 |

With the dyadic values actually observed at N ≤ 16383 (γ ≤ 0.45) the cone route costs nothing for v ≥ 1/(1+π)
(e.g. γ = 0.5: T = 21.35, 31.78, 49.27, 91.79, 312.5 at v = 0.2415, 0.3, 0.35, 0.4, 0.45). As v → v1 every bound blows up
like 1/m (B's Prop. B3).

## 4. Negative results: what cannot work

### 4.1 (E_γ) fails for general finite sets, so a proof must use the family. NUMERICAL
`cone_any.py` (float exact-map simulator, 200 interior samples per leg), A-1's sets:
* v = 1/10, the six directions of Prop. A9: order is lost in the first leg; sup_{t≥t_f} max|β| = 3.130 > arccos 0.1 = 1.471.
* v = 0.2, A-1's robust set with all gaps ≥ 0.01 (0.966465112601, 0.976465112601, 0.986465112807, 1.165246778756,
  6.26318530718, 6.27318530718): sup_{t≥t_f} max|β| = 3.119 > arccos 0.2 = 1.369.
* v = 0.5, uniform 2^9 or 2^11 set plus a geometric tail cluster (§2.3): 1.26 > arccos 0.5 = 1.047, although the cone at
  onset is 0.46 — the cluster acts like near-twins when it is finally eaten.
So the data available at t_f for an arbitrary set (an ordered chain in [0, π] with one radial edge) imply no cone bound
with γ < arccos v; (E_γ) can only be proved from the uniform spacing of the family, i.e. as a quantitative statement.
(Float computations, not certified; the margins are ≥ 0.2 rad, so certification with `code/A/certify.py` is routine.)

### Remark 4.2 (a cone controls neither W nor A). PROVED
Exact edge formula: for consecutive candidates P, Q at distances ρ_P, ρ_Q with angle a at Harry and ℓ = |PQ|,
w = (r̂_Q − r̂_P)·(Q − P)/ℓ = (ρ_P + ρ_Q)(1 − cos a)/ℓ ≥ 0 (expand (r̂_Q − r̂_P)·(ρ_Q r̂_Q − ρ_P r̂_P)).
Points at radii (1+η)^k, k = 0..n, alternating between bearings 0 and δ, are radially monotone and lie in the cone |β| ≤ δ,
but A = nδ and, as η → 0, each w → 2 sin(δ/2), so W ≈ nδ is unbounded. Hence no Φ- or Ψ-type functional can be certified
from a cone; this is why Theorem A2.3(i) switches to D at t_f.

### 4.3 Route 2a: reverse the chain at the fold. Structure PROVED, failure NUMERICAL
At a tail fold (S_{N−1} on the segment [H, S_N]) the order (S_{N−1}, S_N, S_{N−2}, …, S_j) is mirror-ordered (bearings
β_i − β_N ∈ [−β_N, 0], decreasing), so Lemma A3 applies with left and right swapped, and
Φ⁺ = Φ⁻ − ρ_j + ρ_N + (|S_N S_{N−2}| − ℓ_{N−2} − ℓ_{N−1}) ≤ Φ⁻ − ρ_j + ρ_N ≤ 2Φ⁻.
But the reversed chain has ρ decreasing along it, and that is not preserved: for consecutive P, Q with |β_P| ≤ |β_Q|, at
equal distances (ρ_P − ρ_Q)' = cos β_Q − cos β_P ≤ 0. The near part of the old chain is swept behind Harry and the reversed
chase is a new main phase with a long tail, which folds again. Simulation with a reversal at every fold (`gchase.py`,
`test_policies.py`; fold times computed exactly from the affine law of Lemma A4): v = 0.24, N = 511: T = 42.67 (plain chase
15.11), six reversals, Φ 1.20 → 2.35 → 3.78 → … → 10.3, max W = 8.0, max A = 12.3. v = 0.5, N = 511: Φ roughly doubles at
each of 80 reversals and T ≈ 8·10^20, i.e. divergence.

### 4.4 Route 2b: the bearing-sorted chase. Half-plane PROVED, failure NUMERICAL
Rule: the next target is the remaining candidate of smallest bearing (this is the chain chase while the chain is ordered).
PROVED: all remaining bearings stay in [0, π] for the whole chase (Lemma A2 within legs; at a switch the new bearings are
β_i − β_min ∈ [0, π]); the polyline Φ_s through the candidates in bearing order satisfies Φ_s' ≤ −(1 − v(1+π)) between
bearing ties; at a tie of P (closer) and Q on one ray, with neighbours X, Y in bearing order, Φ_s jumps by
Δ = (|XQ| − |XP|) + (|PY| − |QY|) ≤ 2|PQ|, with Δ → 2|PQ| when X, P, Q, Y are nearly radially aligned, which is exactly the
end-phase geometry (a folded near-radial arc sorted by bearing zig-zags between its two branches).
NUMERICAL (`test_sorted.py`): v = 0.24, N = 511: T = 16.93 (chain chase 15.11); v = 0.5, N = 511: T = 1.19·10^5.

