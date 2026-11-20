# Referee report RP6d-2 (second, adversarial) on `referee/P6d-claims.md` — the start hypothesis (ST)

Scope: start S, Lemma D0, Claims D1–D3, Theorem D, Corollary D of `referee/P6d-claims.md`; Claim 1(a),(b),(e),(f),(g) of
`referee/P6c-claims.md`. `referee/P6a-claims.md` (v3) is assumed. I did not read the streams' reports/code, nor
`reports/referee-RP6d-1.md`. Angle: rebuild, interface with Theorem B / Corollary M, ε-uniformity, what is left for (T).
Code and outputs: `code/referee/P6d_2/` (`check_front.py/.out`, `sim_start.py`, `sim_*.out`).

## 0. Verdicts

| Statement | Verdict |
|---|---|
| P6c Claim 1(a),(b),(e),(f),(g) | **OK** (re-derived independently; checked to 1e-22 against own formulas and to 1e-31…1e-41 against direct ODE integration) |
| Lemma D0 (a),(b),(c) | **OK** |
| Claim D1 (|κ| ≤ 2.2 on the arms, ≤ 1.1 in the middle, m ≤ 0.63ρ) | **OK** (every number recomputed; true sup|κ| ≈ 1.00, sup m/ρ ≈ 0.516) |
| Claim D2 (a),(b),(c) | **OK** ((b) is tight in the rounding: 6.8189 ≤ 6.82; true length ≤ 6.289 for v ≤ 1e-3) |
| Claim D3 (a),(b),(c) | **OK** |
| Theorem D items 1–6 and the conclusion "(ST) at t_s, base α_s, arc [α_s, 2π − δ/2]" | **OK**; the closing sentence about the left arm needs fix F1 (it is true at t_0 and silent — correctly — about t_s, but is misleading without the caveat) |
| Corollary D | **OK** as a conditional statement, with clarification F2 (which front and which labels (T) refers to) |
| Remark (1) (C_cut, (ST⁺), reference to P6a2) | **not refereed** (depends on `referee/P6a2-claims.md`, outside my brief); the numbers quoted in it (t_s − t_0 ≤ 1.402ε, ρ_s ≤ 1.4ε, α_s ≤ 2.1ε, 6.85) are those of Theorem D and are OK |

No GAP and no FALSE statement found. One finding that matters for the *next* step ((T)), not for the claims: after the
connector the left-behind arm has curvature ≈ v²/(2ε) at its inner end (§3.3) — the "curvature ≤ 2.2" description of the
left arm is a t_0-statement only.

## 1. Rebuild

### 1.1 The front at t_0 (own derivation)
Only the two straight-run invariants were taken from P6c §0 and re-proved in one line each (C = ρ g(β) constant,
h = ρ(cos β + v), h' = v² − 1). At time t of Phase 1: C = g(α), h = cos α + v − (1 − v²)t, so at t_0 = 1/(1 − v):
h = −(1 − cos α). This is (a). For the tangent I did *not* use (b): I differentiated (C, h) in α and solved the 2×2 system
   ρ_α g(β) + (ρβ_α) g'(β) = g'(α),   ρ_α (cos β + v) − (ρβ_α) sin β = −sin α
numerically (50 digits). Result (`check_front.out`): relative difference to the author's A, B of (b): ≤ 3.9e-22 for
α ∈ [1e-15, 1/2], v ∈ {1e-12, 1e-6, 1e-3, 1e-2}. Positions against a direct Taylor-ODE integration of the true dynamics
from t = 0 (no invariants): ≤ 1e-31 (v = 1e-2) … 3e-41 (v = 1e-12).
By hand: (a) ⇒ cos β < −v, g(β) ≤ g(θ*) ≤ 1, ρ ≥ g(α) ✓; elimination gives (b) ✓ (I redid the algebra:
sin²α − (1 − cos α)(cos α − v) = (1 − cos α)(1 + v)). (e): for 0 < α ≤ α_s the *true* bearing passes arccos v before t_0,
and there the true ρ = g(α)/g_max ≤ ε — a statement about true candidates and the closed vision disc ✓; for
α ∈ [α_s, π): ρ ≥ g(α)/g_max ≥ ε on [0, t_0] ✓ (equality only for α = α_s, at one instant). (f): ρ_s/ε ∈ (1, 1.0003] in all
my runs (bound 1.4) ✓.

### 1.2 Own bound on the curvature of the arm
Near the tip, with τ = tan(α/2): −(cos β + v) = g(β)τ^{1+v}, m = B/A ≤ τ^{1+v}/((1 − v)c'), ρ ≍ 2τ^{1−v}. Hence
ψ − θ* = (β − θ*) + arctan m = O(τ^{1+v}) = O(ρ^{(1+v)/(1−v)}) and dψ/ds ≍ ((1+v)/(1−v))(ρ/2)^{2v/(1−v)}: the curvature
is **bounded up to the tip and tends to 0 there** (for v = 0 it is ≡ 1, the unit circle). There is no v/ε-type term: the
true flow does not know ε. Numerically (curvature from a 50-digit derivative of ψ(α)): sup over α ∈ [1e-15, 1/2] of |κ| =
1.0000, 0.99999859, 0.99859, 0.98597 for v = 1e-12, 1e-6, 1e-3, 1e-2 (attained at α = 1/2); κ(α = 1e-15) = 0.9999, 0.9999,
0.935, 0.509; middle sup|κ| = 1.0000 … 0.99125; sup m/ρ = 0.516; sup σ(α/2)^v ≤ 1.0000. So 2.2 / 1.1 / 0.63 / 1.52 hold
with a factor ≈ 2 / 1.1 / 1.2 / 1.5 to spare.
Line-by-line recomputation of the author's bound: (1) 0.6202; (2) 0.1844 + 0.71499; the identity for A_α re-derived
((c'/sin α)' = −(1 − v cos α)/sin²α; c'² − 1 + v cos α = −sin²α − vc'); T1 0.1895, T2 0.715v, T3 0.1863, T4 0.0549,
T5 0.2148; sum 2.1842 < 2.2 ✓ (two of the roundings, 0.71499 < 0.715 and 0.1844 < 0.185, are sharp to the 4th digit but
correct). Middle: 2/0.479 = 4.175, 1/0.479² = 4.358, bound 1.0886 ≤ 1.1 ✓.

### 1.3 Own estimate of the connector
Harry moves a distance ≤ 1.4ε along u, and the arm leaves x_{α_s} at an angle |φ_s| ≤ arctan(0.63ρ_s) ≤ 0.9ε from u
(numerically 0.35ε … 0.50ε). For a point of the arm at arclength l from x_{α_s}, Harry's offset from its tangent line is
≤ κ(l²/2 + dl) + d|φ_s|, so |sin φ| ≲ κρ + ε and |∂_s ψ_t| ≲ v(κ + 1)/ε near the base; times the duration 1.4ε this is a
change O(v) of the Lipschitz constant, ε-free. That is exactly the structure of the author's Step 2/3 (constants
3.6K + 0.9, 34.6, 49v — all re-checked: cos 1 = 0.5403, 1/0.54 = 1.852, 1.86²/2 + 1.86 = 3.59, 1/0.07² = 204.1,
1.402·34.6 = 48.51, 1.402·410/6400 = 0.09). The key structural fact is that **the connector runs along the arm itself**
(aiming error ≤ 0.9ε); an aiming error Θ would give Δκ ~ vΘ/ε. Simulation: the Lipschitz constant on 𝒜 changes by
< 5e-5 during the connector in every run (claimed ≤ 49v).
The bootstrap is sound: K is continuous by (*) with the crude S̄ = 1/ε², K(t_0) ≤ 2.2 < 4, and Step 2 only uses K ≤ 4.

## 2. Interface with Theorem B / Theorem R / Corollary M (checked verbatim against P6a v3)

Corollary M allows "any 1-Lipschitz path fixed in advance such that, at some time t_s, P(t_s) = x_a(t_s) for a label
a =: a_{j_s}, every label in [0, a_{j_s}] has been seen by t_s, and P follows the legs of construction C from t_s on",
with t_s ≤ T_s, R_{j_s} = l_{t_s}(a_{j_s}, 2π) ≤ L_s, (ST) on [a_{j_s}, 2π − δ/2], a_{j_s} < 2π − δ, ε₀ ≤ min(δ, R/64).

* **Path.** Phase 1 (to the exact real number t_0), connector (direction u and α_s are functions of (v, ε) only), legs:
  speed ≤ 1, fixed in advance ✓. P(t_s) = x_{α_s}(t_s) *exactly* (D3(a): d' = −1 + vf(d) reaches 0 in finite time) — this
  is what Lemma C(2) needs for the first leg (β(t_s) = 0) ✓. Nothing in Theorems R, B refers to legs before j_s
  (I re-read Steps 1–5: Lemma C(2),(4) are used for legs j+1 > j_s only; "time since t_s"; Lemma C(0) is path-independent).
* **Which front.** (ST), U, λ, E, c, R_{j_s} and (T) are all defined for the **virtual** front x_θ(t_s) of P6a
  (C¹ field f) for the actual path. Theorem D describes exactly that: on [α_s, 2π − α_s] the candidates have ρ ≥ ε on
  [0, t_0] (P6c 1(e)), where F is the unit field, so virtual = true *including the tangent vectors* (variational equation
  along the same trajectory with A = Π/ρ; at the single grazing instant of α_s, A is continuous) — hence D1/D2 (true
  front) transfer to the virtual front on that arc at t_0; from t_0 to t_s Claim D3 is written for the virtual field
  (Γ(ρ) = ρ/m², m = max(ρ, ε)), where candidates near α_s *are* inside the disc ✓. For labels in (−α_s, α_s) the virtual
  front is not the true front (the "blob"), but those labels are outside the (ST) arc and enter only through
  (i) "seen": proved for the true candidates (§1.1) ✓; (ii) R_{j_s}: item 6 bounds the virtual length of (2π − α_s, 2π)
  by 2.02ε using only w_t/w ≤ va*(ρ) — correct, and uniform because α_s ≤ 2 g_max^{1/(1−v)} ε^{1+μ} cancels ε^{−μ} ✓
  (simulation: 1.000ε … 1.0035ε); (iii) hypothesis (T) — see §4.
* **(IC1)** pairs in [0, U] with ε/2 ≤ λ ≤ 32R, E ≤ κ²λ³, κ = 1/2: item 3 gives E ≤ 0.211λ³ for all λ ≤ 1.39 ⊃ (0, 32R] ✓
  (measured sup E/λ³ = 0.035 … 0.0417 ≈ 1/24). **(IC2)** ✓ (20.2R and 48R; measured min c = 32.0R). **(IC3)** ✓.
  Arc [α_s, 2π − δ/2], a_{j_s} = α_s ≤ 2.1ε < 2π − δ ✓, ε₀ = min(δ²/6400, R/64) ≤ min(δ, R/64) ✓.
  v(4U + 2) ≤ 10⁻⁶R follows from v₀ ≤ 10⁻⁶R/29.6 and U ≤ 6.9 ✓; K* formula ✓; T_s: t_0 + 1.402ε ≤ 1.001001 + 2.77e-5 ≤ 1.0011
  ✓ (this uses ε ≤ R/64 ≤ 1/50688, not just ε ≤ δ²/6400); 1.0011 + 2.1·6.9 = 15.49 ✓.
* **Seen.** Every label in [0, α_s] ∪ [2π − α_s, 2π]: true candidates within the closed disc during [0, t_0] ✓. (Labels
  ±α_s only touch ρ = ε; +α_s is in any case reached by the connector, 2π − α_s by the last leg.)

Conclusion: the output of Theorem D is verbatim the hypothesis of Corollary M / (ST) of Theorem B. No mismatch.

## 3. Uniformity in ε

3.1 *No hidden offsets.* t_0 = 1/(1 − v), α_s (g(α_s) = εg_max), u, t_s are exact real numbers defined by (v, ε); the
theorem needs no stability under perturbation of them. The construction is not "construction C's leg 0" (which stops at
t_0 − εs_0 and produces the known non-uniform kink); the difference is real and the claims say so. I found no place
where an η-offset re-enters: D3(a) is an exact ansatz; D1 is applied at exactly t_0.
3.2 *Constants.* All constants in D1–D3 and Theorem D are free of ε; ε enters only through ε ≤ δ²/6400 (far case of
D3 Step 2), ε ≤ R/64, ε ≤ 1/20. The stretch σ ≍ α^{−v} is unbounded at the tip but enters only integrated (D2(a),(b)) ✓.
Simulations for ε from 1.9e-5 down to 1e-12 (v = 1e-3) show k_𝒜(t_s) = 0.99913 independent of ε.
3.3 *Finding (not a defect of the claims): the left-behind arm after the connector.* During the connector Harry leaves
O along +u while the left arm leaves O along ≈ −ū at the wedge angle 2 arcsin v; Harry's offset from the left arm's
line is ≈ 2vd, the arm stays outside the disc, so ψ_t ≈ −2v²d/(s + d)² at distance s from O, and after the connector
   Δψ(s) ≈ −2v²[log(1 + ε/s) − ε/(s + ε)],   Δκ(s) ≈ 2v²ε²/(s(s + ε)²),   i.e. **κ ≈ v²/(2ε) at the inner end s ≈ ε**.
Simulation (first grid cell of the left arm, mid-point s ≈ 1.05ε resp. 1.1ε; prediction 0.453 v²/ε resp. 0.412 v²/ε):
(v, ε) = (1e-3, 1e-7): 3.57; (1e-3, 1e-9): 413.3 (pred. 412); (1e-3, 1e-12): 4.138e5; (1e-2, 1e-8): 4033 (pred. 4120);
(1e-3, 1.9e-5): not visible (0.02). So the Lipschitz constant of the tangent on the left arm at t_s is **not** ε-uniform
(total turning 2v²(log 2 − 1/2) is). This does not touch (ST) (the arc 𝒜 stops at 2π − δ/2 and the far case of D3
covers its left-arm part), but whoever proves (T) must not start from "curvature ≤ 2.2 on the left arm" at t_s.

## 4. What is left for (T)

Corollary M needs (T) with b* = 2π − δ: K_tip(t) = ∫_{max(a_{j+1}, 2π−δ)}^{2π} T·AT ds ≤ K_T for all t ≥ t_s, for the
virtual front, end label 2π. Theorem D covers [α_s, 2π − δ/2]; the overlap [2π − δ, 2π − δ/2] is exactly the margin that
Corollary M requires (b' = 2π − δ ≤ U − ε/2 in arclength) — the split is consistent. Two points for the (T) stream:
(i) with end label 2π, K_tip includes the already-seen blob (2π − α_s, 2π] of the *virtual* front: length ≈ ε, and
T·AT up to 2/ε when Harry is on it (at t_0 the blob alone contributes 1.000 to K_tip, total 1.12 for δ = 1; at t_s:
total 0.12, 0.005, 4e-4 for δ = 1, 0.2, 0.05) — bounded, but it must be carried through the endgame or removed by C_cut,
whose compatibility with Theorems R/B is not part of the refereed P6a text; (ii) §3.3.

## 5. Fixes (exact text; none changes a statement that is used)

**F1** (Theorem D, last sentence). Replace "(Claim D1: curvature ≤ 2.2, |tan(ψ − β)| ≤ 0.63ρ, no point within ε of O)" by
"(Claim D1 and P6c 1(g): **at time t_0** curvature ≤ 2.2, |tan(ψ − β)| ≤ 0.63ρ, no point within ε of O. This is not
claimed at t_s: during the connector the inner end of the left arm acquires curvature ≈ v²/(2ε), with total turning
O(v²).)"
**F2** (Corollary D, statement). After "holds with b* := 2π − δ for every t ≥ t_s" insert "(K_tip taken for the virtual
front of P6a-claims §1 and all labels up to 2π, i.e. including the already-seen labels (2π − α_s, 2π])".
**F3** (Theorem D, item 2, proof). "t_0 ≤ 1.0011" → "t_0 ≤ 1.001002 and 1.402ε ≤ 1.402/50688 < 2.8·10⁻⁵ (ε ≤ R/64)".
**F4** (Claim D2). (a), (b) need only v ≤ 10⁻³, ε-free; say so ("v ≤ 10⁻³δ is used only in (c)"). In the proof of (c)
"c ≥ 0.49δ" should read "c ≥ 0.4948δ − 0.002004δ ≥ 0.49δ ≥ 0.48δ".
**F5** (Claim D1, statement). Add "(virtual = true on [α_s, 2π − α_s] at t_0 together with the tangent vector ∂_θx,
since A = Π/ρ along a trajectory with ρ ≥ ε)" — this is what makes k_𝒜(t_0) a statement about the virtual front.
**F6** (Lemma D0(b)). "locally Lipschitz in θ" → "Lipschitz in θ on compact label sets, uniformly for t in compact sets
(Gronwall for the second variation)", which is what "locally uniformly in t" and the finiteness of K(t_s) use.

## 6. Numerical summary (`code/referee/P6d_2/sim_*.out`)

Simulation of the start S for the virtual field with the variational equation (labels started at t_ε from the closed
form, RK4; double precision, and 34-digit mpmath for v = 1e-12 and for ε ≤ 1e-8 — double precision is *not* adequate
below ε ≈ 1e-8, my first such runs were discarded). k = sup of |Δψ|/Δs over adjacent labels.

| v | ε | δ | mode | α_s/ε | ρ_s/ε | (t_s−t_0)/ε | k_𝒜(t_0) | k_𝒜(t_s) | sup E/λ³ | min c/16R (λ>32R) | l(α_s,2π−α_s) at t_s | K_tip t_0 / t_s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1e-12 | 1e-6 | 1 | mp | 1.0000 | 1.0000 | 1.0000 | 1.000000 | 1.000000 | 0.0415 | 2.005 | 6.28318 | 1.122 / 0.122 |
| 1e-12 | 1e-10 | 1 | mp | 1.0000 | 1.0000 | 1.0000 | 1.000000 | 1.000000 | 0.0416 | 2.001 | 6.28319 | 1.122 / 0.122 |
| 2e-4 | 6e-6 | 0.2 | double | 0.9975 | 1.0000 | 1.0001 | 0.99983 | 0.99983 | 0.0415 | 2.004 | 6.28431 | 1.005 / 0.005 |
| 1e-3 | 1.9e-5 | 1 | double | 0.9885 | 1.000002 | 1.0007 | 0.99913 | 0.99913 | 0.0412 | 2.001 | 6.28882 | 1.122 / 0.122 |
| 1e-3 | 1e-7 | 1 | double | 0.9833 | 1.000002 | 1.0007 | 0.99913 | 0.99913 | 0.0412 | 2.003 | 6.28885 | 1.122 / 0.122 |
| 1e-3 | 1e-9 | 1 | mp | 0.9788 | 1.000002 | 1.0007 | 0.99913 | 0.99913 | 0.0408 | 2.019 | 6.28885 | 1.122 / 0.122 |
| 1e-3 | 1e-12 | 1 | mp | — | 1.000002 | 1.0007 | 0.99913 | 0.99913 | 0.0408 | 2.006 | 6.28885 | 1.122 / 0.122 |
| 1e-2 (outside Thm D) | 1e-4 | 1 | double | 0.9049 | 1.0002 | 1.0069 | 0.99125 | 0.99125 | 0.0389 | 2.001 | 6.34017 | 1.121 / 0.121 |
| 1e-2 (outside Thm D) | 1e-8 | 0.05 | mp | 0.8245 | 1.0002 | 1.0069 | 0.99125 | 0.99125 | 0.0353 | 2.001 | 6.34036 | 1.000 / 4e-4 |

Claims: k ≤ 2.2 / 2.25, E/λ³ ≤ 0.211, min c ≥ 16R, length ≤ 6.85, ρ_s/ε ≤ 1.4, (t_s − t_0)/ε ≤ 1.402 — all satisfied with
large margins and with no trend in ε. |P(t_s) − x_{α_s}(t_s)| ≤ 2e-12 ε in every run; RK4 (virtual field) agrees with the
closed form (true flow) on [α_s, 2π − α_s] at t_0, min ρ(t_0)/ε = ρ_s/ε > 1 there (no point of the arc inside the disc).
Limits of the numerics: the grid is a sample (adjacent-label ratios, sub-sampled pairs); it confirms, it does not prove.
