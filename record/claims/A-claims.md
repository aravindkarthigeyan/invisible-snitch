## 4. Proved lemmas about the ordered phase (PROVED)

Notation as in Section 4 of `snitch_proved.tex`. During leg j (the chase of S_j) Harry's heading u_j is constant;
bearings β_i ∈ (−π, π] are measured from u_j, so β_j ≡ 0. "Left/right point": β ∈ (0,π) / β ∈ (−π,0).
Call the chain **ordered** at a time of leg j if 0 = β_j ≤ β_{j+1} ≤ … ≤ β_N ≤ π.
λ := 1 − v².

### Lemma A1 (the angle at the first instant). PROVED
For every finite set 0 = α_0 < α_1 < … < α_N < 2π, the bearings θ_i ∈ (0, 2π) of S_i(t0) measured from the
initial heading (1,0) satisfy θ* < θ_1 < θ_2 < … < θ_N < 2π − θ*, where cos θ* = −v. Hence
A(t0) = θ_N − θ_1 < 2π − 2θ* = 2 arccos v < π, and for α_1 → 0⁺, α_N → 2π⁻ (e.g. uniform sets, N → ∞),
A(t0) → 2 arccos v.

*Proof.* For α ∈ (0, π), Prop. 1 gives at t0 = d/(1−v): h = d(cos α + v) − λ t0 = −d(1 − cos α) < 0 and
C = d g(α) > 0, so h/C < 0 = k(θ*). Since k is strictly decreasing from +∞ to −∞ on (0,π) (Lemma 1),
the bearing b(α) = k⁻¹(h/C) lies in (θ*, π). As in the proof of Prop. 5 with c = v − λ t0/d = −1, the bracket
1 − cv + (c − v)cos α = (1+v)(1 − cos α) > 0, so h/C is strictly decreasing in α and b strictly increasing.
For α = π the point is on the backward ray, which is invariant (Prop. 1), so θ = π. For α ∈ (π, 2π) the
reflection (x,y) ↦ (x,−y) maps the problem to itself and gives θ(α) = 2π − b(2π − α) ∈ (π, 2π − θ*), increasing.
So the θ_i are strictly increasing in (θ*, 2π − θ*), an interval of length 2π − 2θ* < π (because θ* > π/2).
Hence each unsigned angle a_i between consecutive rays equals θ_{i+1} − θ_i, and A(t0) = Σ a_i = θ_N − θ_1.
Finally 2π − 2θ* = 2(π − θ*) = 2 arccos v, and by Prop. 4 θ_1 → θ*, θ_N → 2π − θ* as α_1 → 0, α_N → 2π. ∎

*Correction to the brief:* "A equals π at the first instant" is false; the value is 2 arccos v (e.g. 2.739 at v = 0.2,
2.094 at v = 0.5; the simulator reproduces this to 3 digits at N = 1000). What tends to π as N → ∞ is sup_t A,
attained shortly after t0.

### Lemma A2 (half-plane persistence within a leg). PROVED
Along a straight run with heading u, a candidate with bearing in (0, π) at the start keeps a bearing in (0, π),
strictly increasing in time, and is not caught; a candidate on the forward ray (β = 0) or backward ray (β = π)
stays on it. The same holds for (−π, 0) with "decreasing".

*Proof.* The two rays are invariant because on them the relative velocity v r̂ − u is parallel to r. For
β ∈ (0,π), C > 0 is constant and h decreases strictly (Prop. 1), so h/C decreases strictly and β = k⁻¹(h/C)
increases strictly, staying in k⁻¹(ℝ) = (0, π). By Prop. 3 such a candidate is not caught (ρ ≥ C/sup g > 0). ∎

### Lemma A3 (ordered ⇒ A ≤ π; switches preserve order). PROVED
(a) If the chain is ordered at some time, then A = β_N ≤ π at that time.
(b) If at the end of leg j (left limit, S_j at Harry) the bearings of S_{j+1}, …, S_N measured from u_j satisfy
0 ≤ β_{j+1} ≤ … ≤ β_N ≤ π, then the chain is ordered at the start of leg j+1.
(c) Consequently, A ≤ π at every time of the chase up to the first time at which, inside some leg, two
consecutive non-target candidates S_i, S_{i+1} have bearings in the wrong order.

*Proof.* (a) All bearings lie in [0, π], so the unsigned angle between consecutive rays is |β_{i+1} − β_i|
= β_{i+1} − β_i, and the sum telescopes to β_N − β_j = β_N ≤ π. (b) The new heading is r̂_{j+1}, so new bearings
are β_i − β_{j+1} ∈ [0, π − β_{j+1}], still nondecreasing. (c) Within a leg, by Lemma A2 every non-target
candidate starting in [0, π] stays in [0, π]; so the ordered property can only be lost by a consecutive pair
reversing; at switches it is preserved by (b); apply (a). (Order is a closed condition and all bearings are
continuous in time within a leg, so "up to the first time" is well defined; A ≤ π at the limiting instant too.) ∎

### Lemma A4 (pairwise crossing rule). PROVED
During one straight run (time s ∈ [0, τ]) let P, Q be left candidates. Then
f(s) := k(β_P(s)) − k(β_Q(s)) = h_P(0)/C_P − h_Q(0)/C_Q − λ s (1/C_P − 1/C_Q)
is affine in s, and β_P < β_Q ⇔ f > 0. Hence (i) the bearing order of P, Q changes at most once per run;
(ii) if C_P ≥ C_Q, an order β_P < β_Q present at s = 0 persists for the whole run; (iii) if β_P < β_Q at s = 0
and β_P > β_Q later, then at the crossing instant ρ_P < ρ_Q: **the closer point overtakes**.
Left and right candidates never share a bearing.

*Proof.* Prop. 1 and Lemma 1. At a crossing β_P = β_Q = b, so C_P/C_Q = ρ_P g(b)/(ρ_Q g(b)) = ρ_P/ρ_Q, and a
change of sign from + to − of an affine f needs negative slope, i.e. 1/C_P > 1/C_Q. ∎

### Corollary A5 (how order is first lost). PROVED
If the chain is ordered at the start of a leg and not ordered at some later time of the leg, then at the first
instant s* of failure there is a consecutive pair S_i, S_{i+1} (i > j) with β_i(s*) = β_{i+1}(s*) ∈ (0, π) and
ρ_i(s*) < ρ_{i+1}(s*): the edge E_i is radial and points **away** from Harry. Order is never lost at a switch.

*Proof.* The ordered set of times is closed; let s* be the infimum of the (relatively open) failure set. Since there
are finitely many consecutive pairs, one pair (i, i+1) is reversed at times s_n ↓ s*; by continuity it is tied at s*.
Points on the forward ray stay at bearing 0 and points at bearing π stay there, so two tied points that later reverse
lie in (0, π); by Lemma A4 the affine f has f(s*) = 0 and f(s_n) < 0, so its slope is negative, i.e. C_i < C_{i+1},
i.e. ρ_i < ρ_{i+1} at s*. Switches: Lemma A3(b). ∎

### Lemma A6 (radial monotonicity persists while ordered). PROVED
If during a leg the chain stays ordered and ρ_j < ρ_{j+1} < … < ρ_N at its start, then this holds throughout the leg;
it also survives switches (distances are continuous and the chain only loses its first point).

*Proof.* g_i = ρ_{i+1} − ρ_i is C¹ while both distances are positive, and ρ' = v − cos β (Prop. 1). If g_i(s*) = 0 at a
first zero, then β_i ≤ β_{i+1} in [0, π] and the two points are distinct (the flow of (1) is injective away from Harry),
so β_i < β_{i+1} and g_i'(s*) = cos β_i − cos β_{i+1} > 0, contradicting g_i > 0 on [0, s*). For i = j (Harry's target): g_j' =
(v − cos β_{j+1}) + (1 − v) = 1 − cos β_{j+1} ≥ 0, so g_j never decreases. ∎

### Remark A7 (Abel form of W). PROVED (one line)
W = r̂_N·e_{N−1} − u·e_j + Σ_{i=j+1}^{N−1} r̂_i·(e_{i−1} − e_i) ≤ 2 + Σ_i |e_{i−1} − e_i|, i.e. W ≤ 2 + (total
absolute turning of the chain). Not useful by itself: the turning starts at 2π − 2 arcsin v (≈ 5.88 at v = 0.2) and is
not monotone (`tat.py`: small increases near the end).


### Corollary A8 (reduction of B's hypothesis (K) to the end phase). PROVED
While the chain is ordered (Lemma A3), W ≤ A = β_N = |β_N|. Hence B's hypothesis
(K) "W ≤ max(|β_N|, w0)" holds automatically at every time up to the first loss of order (Corollary A5), for every
finite direction set. The only open part of (K) is the end phase after order is first lost.
*Proof.* W ≤ A is Lemma 2 of `snitch_proved.tex`; A = β_N ∈ [0, π] is Lemma A3(a). ∎

*Answer to B's warning (1).* By Lemma A3(a), A < π strictly at every time while the chain is ordered (β_N ∈ (0, π)
by Lemma A2, since S_N is never on the backward ray for a generic set). In every uniform/dyadic run, sup_t A is attained
early in the ordered phase (the tail S_N, which starts within ~(2π/N)^{1−v} of Harry, is swung behind him, so β_N → π⁻),
and A ≤ 0.32 throughout the unordered end phase. So the slow growth of sup A with N (2.62, 2.79, 2.90, 3.00 for
N = 50, 200, 1000, 6400 at v = 0.5) is approach to π from below, **not** evidence for A > π for uniform sets.
A > π for uniform sets would require it in the end phase, where A is an order of magnitude smaller.
For **non-uniform** sets, (H) is false: see Section 5.


## 5. Hypothesis (H) as stated is false (PROVED, computer-assisted with interval arithmetic)

(H) in Theorem B quantifies over **every** finite direction set containing 0. It fails, already for v < 1/(1+π).

### Proposition A9 (counterexample to (H)). PROVED (computer-assisted; rigorous outward-rounded interval arithmetic)
Let v = 1/10 and take the six directions (exact decimals, plus α_0 = 0)
α = 1.278182093392, 1.288182093392, 1.38054291417, 6.253166882374, 6.263185307163, 6.273185307179
(all gaps ≥ 0.01). During the first leg (chase of S_1), at time t0 + 0.999999·τ_1 (τ_1 = ρ_1(t0)/(1−v)),
**A ∈ [3.29145272139670, 3.29145272139670] (width < 1e−40), so A − π ≥ 0.1498 > 0.**

*Method* (`code/A/certify.py`, mpmath.iv at 60 digits). Every quantity is an interval containing the true value.
Each straight run uses the exact solution of Prop. 1 (C constant, h decreased by λτ); the new bearing parameter
u = log tan(b/2) solves k(u) = h/C, and its enclosure [u_lo, u_hi] is *certified* by checking in interval arithmetic
that k(u_lo) > sup(h/C) and k(u_hi) < inf(h/C) (k strictly decreasing, Lemma 1). Bearing signs (left/right) are
certified (interval excludes 0). A is the sum of atan2(|cross|, dot) over consecutive rays.
Independent check without the exact map (`ode_check.py`, DOP853, rtol 1e−13): A = 3.291452721343, W = 2.0990.
Float exact-map simulator: A rises from 3.129 (0.9τ) to 3.2915 (0.999999τ) to 3.2916 in the left limit.

*Mechanism.* Near-twin directions. When Harry is about to catch S_j, a candidate S_{j+1} whose direction is very
close to S_j's sits at distance O(gap) from Harry at a bearing close to the angle between the curve's tangent
∂_αS and the heading — which can be anywhere in (0, π) — while the next candidate S_{j+2}, further away, can have a
smaller bearing. The order breaks at the twin, and A picks up roughly twice the overshoot. Other certified/verified
instances: v = 0.35 with seven directions (gap 8e−4) gives A = 4.95 (ODE check, `verify_cex.py`).

### Proposition A10 (even W ≤ π fails for some finite sets). PROVED (computer-assisted, same method)
v = 6/25 = 0.24 < 1/(1+π), directions 0.412411719969, 0.41241171997, 0.696029615234, 1.331539471428,
2.98214094828, 3.518379401584, 6.035941613736, 6.283185299154. At time t0 + (1 − 10⁻¹²)τ_1:
W − π ∈ [0.909319036919, 0.909319036920] (certified W > π; also A − π ≈ 2.732 > 0). ODE check: W = 4.0508.
*Caveat:* this violation is momentary (W ≤ 2.29 until 10⁻⁹τ_1 before the catch); it comes from a twin pair at
gap 10⁻¹². It shows that no argument of the form "W ≤ π for every finite set at every time" can work, so B's (K)
must also be restricted to a specific family. For sets with all gaps ≥ 0.01 at v = 0.2 the optimiser found
sup W = 3.047 < π (`cex_gap.py`), so robust W > π at small v was **not** found.

*Also (NUMERICAL, float simulator only, not certified):* the same twin construction at v = 0.2 (directions 0.412454551721, 0.412454551722, 0.62900027389, 1.363359768916, 3.042009054938, 3.645569621094, 6.142689665505, 6.283185150892) gives sup A = 5.867 and sup W = 3.988 > π; at v = 0.1 a 4-direction twin set gives sup A = 4.18 (`cexA.py`).

### Consequence for Theorem B
The proof of Theorem B only uses (H) for the nested family fed to Lemma 4. Theorem B should be restated with
(H) (or (K), or any W ≤ K) required only for **one chosen nested dense family, e.g. dyadic D_k = {2πi/2^k}**.
As stated ("for every finite set"), (H) is false and Theorem B is vacuous.


