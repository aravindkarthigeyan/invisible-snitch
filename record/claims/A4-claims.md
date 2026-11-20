## 2. Lemma A4.1 (vanishing vision radius). PROVED
**Statement.** Let D_1 ⊂ D_2 ⊂ … be sets of directions with dense union, ε_n > 0 with ε_n → 0, and T < ∞. Suppose that
for each n there is a path H_n with H_n(0) = 0, |H_n'| ≤ 1, such that every α ∈ D_n is *seen with radius ε_n* by time T:
ρ^{(n)}_α(t) := |S^{(n)}_α(t) − H_n(t)| ≤ ε_n for some t ≤ T (S^{(n)} the Snitch under H_n; a candidate caught earlier
counts, ρ = 0). Then there is a path H with |H'| ≤ 1 that catches every direction α ∈ [0, 2π) exactly by time T.
(In particular D_n = all directions is allowed: ε-sweeps of all directions with T uniform as ε → 0 suffice.)

**Proof.** As in Lemma 4 (Compactness) of `paper/main.tex`, a subsequence H_n → H uniformly on [0, T], H 1-Lipschitz.
Fix α ∈ D_M. For n ≥ M let t_n ≤ T be a time with ρ^{(n)}_α(t_n) ≤ ε_n (the trajectory exists on [0, t_n]: before its
first catch it is defined, and if it is caught before t_n take t_n = the catch time). Pass to a further subsequence with
t_n → t* ≤ T. Suppose H does not catch α on [0, t*]. Then S_α under H exists on [0, t*] with ρ_α > 0 there, so
ρ_α ≥ c > 0 on [0, t*] (continuity, compactness). The Claim in the proof of Lemma 4 (with α' = α, τ = t*) gives δ > 0
and n_0 such that ρ^{(n)}_α ≥ c/4 on [0, min(t* + δ, T)] for n ≥ n_0 in the subsequence. Since t_n → t* and t_n ≤ T, for
large n t_n ∈ [0, min(t* + δ, T)], so ε_n ≥ ρ^{(n)}_α(t_n) ≥ c/4, contradicting ε_n → 0. Hence H catches every α ∈ ∪D_n
by T. The final step of Lemma 4 is unchanged: by the Claim with H_N = H the set of directions not caught by H on [0, T] is
open; its complement is closed and contains the dense set ∪D_n, so it is everything. ∎

*Remarks.* (a) Only uniform convergence H_n → H and the Claim are used; nothing about how H_n was built. (b) As in
Lemma 4 the limit has speed ≤ 1, not exactly 1. (c) Theorem D1 cannot be fed into A4.1: its range v ≤ v_D(ε) shrinks as
ε → 0. (d) Corollary (CONJECTURE-conditional, PROVED implication): if the brief's ε-greedy sweep (or the LG chase of
Prop. D6, or any explicit ε-controller) has sweep time ≤ T*(v) along a sequence ε → 0, exact capture holds by T*(v).
NUMERICAL support: brief table (times converge as ε ↓ 0 for v ≤ 0.7) and H-1 Prop. H4 (the greedy controller is
linearly stable for v < v* ≈ 0.78, whereas the exact discrete chase is unstable for v > 1/2). So the ε-route is the one
that can, in principle, go beyond 1/2; for small v it also removes the gap-scale near field below ε (see §5.4).

## 3. Exact straight-run identity for lateral offsets. PROVED
**Lemma A4.2.** On a straight unit-speed run with heading u, for a candidate with bearing β ∈ (0, π) and distance ρ,
its lateral offset y := ρ sin β (distance from Harry's line of motion) satisfies
  y · ρ^μ · cos^{2μ}(β/2) = (C/2^v)^q,  q = 1/(1−v), μ = v/(1−v) = q − 1,
where C = ρ sin β / tan^v(β/2) is the invariant of Prop. 1. Moreover y is non-decreasing along the run.
*Proof.* y = ρ sin β = C tan^v(β/2), and tan(β/2) = sin β/(2cos²(β/2)) = y/(2ρ cos²(β/2)). Hence
y^{1−v} = C 2^{−v} ρ^{−v} cos^{−2v}(β/2); raise to the power q. β is non-decreasing on a run (Lemma A2 of the paper) and
tan^v(β/2) is increasing, so y = C tan^v(β/2) is non-decreasing. ∎
*Reading.* C^q ≍ y ρ^μ is the exact (nonlinear) version of B-1/H-1's B_i = (φ_i − ψ)x_i^q: straight runs act on it as the
identity, while geometric quantities (offsets, turning angles) are multiplied by ρ^{−μ}.

## 4. Kink amplification: the A-3 §8 induction is not inductive

### Proposition A4.3 (exact). PROVED
Let Harry run straight with heading u. Let P_1, …, P_m be candidates on the forward ray at distances p_1 < … < p_m, and Q
a candidate with x_Q := (Q − H)·u > p_m and lateral offset y_Q > 0 (bearing in (0, π/2)). In the chain chase of
(P_1, …, P_m, Q, …) Harry never turns before P_m is caught (each target is on the forward ray, which is invariant), so
the chase up to time p_m/(1−v) is one straight run. Let κ(t) ∈ (0, π) be the turning angle of the chain at P_m (angle
between u and Q − P_m). Then for every t < p_m/(1−v) with x_Q(t) > p_m(t):
  tan κ(t) ≥ tan κ(0) · (ρ_Q(0)/ρ_Q(t))^μ,
and if x_Q(t) ≤ p_m(t) then κ(t) ≥ π/2.
*Proof.* tan κ = y_Q/(x_Q − p_m). With r = Q − H, r' = v r̂ − u, so x_Q' = v cos β_Q − 1, and p_m' = −(1 − v); hence
(x_Q − p_m)' = −v(1 − cos β_Q) ≤ 0. By Lemma A4.2, y_Q(t)/y_Q(0) = (ρ_Q(0)/ρ_Q(t))^μ (cos(β_Q(0)/2)/cos(β_Q(t)/2))^{2μ}
≥ (ρ_Q(0)/ρ_Q(t))^μ because β_Q is non-decreasing. Dividing, tan κ(t) ≥ tan κ(0)(ρ_Q(0)/ρ_Q(t))^μ while x_Q > p_m; once
x_Q ≤ p_m the vector Q − P_m has non-positive u-component and positive y, so κ ≥ π/2. ∎

### Corollary A4.3' (no N-uniform constant). PROVED
Take spacing ℓ: p_i = iℓ (i ≤ m), Q = ((m+1)ℓ, ℓ tan κ_0) relative to H(0), any further candidates collinear beyond Q
(the chain is straight except for one kink of angle κ_0 at P_m, so every turning angle is ≤ κ_0 and the chain is C^{1,1}
with discrete curvature ≤ κ_0/ℓ). At the start of the leg towards P_m (time t_1 = (m−1)ℓ/(1−v), when P_m is the target at
distance ℓ and Q the next candidate),
  κ(t_1) ≥ min{ π/3, arctan[ tan κ_0 · ((m+1)/10)^μ ] }.
*Proof.* If β_Q(t_1) > π/3 then, as P_m lies ahead of H on the ray and x_Q > p_m (else κ ≥ π/2), the direction P_m → Q
makes an angle ≥ β_Q(t_1) with u, so κ ≥ π/3. Otherwise cos β_Q + v ≥ 1/2 and, by (h) of Prop. 1,
ρ_Q(t_1) = h_Q(t_1)/(cos β_Q + v) ≤ 2[(1+v)ρ_Q(0) − (1−v²)t_1] ≤ 2(1+v)[ρ_Q(0) − (m−1)ℓ]
≤ 2(1+v)[2ℓ + ℓ tan²κ_0/(2(m+1))] ≤ 5(1+v)ℓ ≤ 10ℓ for tan²κ_0 ≤ m+1 (used √(a²+b²) ≤ a + b²/(2a)); and ρ_Q(0) ≥ (m+1)ℓ.
Apply Prop. A4.3. ∎
**Consequence.** With κ_0 = K·ℓ (allowed by "turning ≤ K·gap") placed at distance r0 = mℓ, the turning at the target
vertex when it reaches Harry is ≳ K·ℓ·(r0/(10ℓ))^μ: its ratio to the gap is unbounded as N → ∞ (ℓ → 0, r0 fixed), for
every v > 0. So the A-3 §8 statement "turning ≤ K·gap within r0 and C²-close far chain at leg j ⇒ the same at leg j+1,
constants independent of N" is false (already for the radial chain; the far chain here is exactly straight). The same
holds on top of a circular background in the linearised model of B-1/H-1 (linear superposition; the B-recursion maps the
"discrete circle" B_n = c Σ_{k<n} k^q to itself exactly, PROVED by P(n+1) − n^q = P(n) for P(n) = Σ_{k<n}k^q, and a kink
on it evolves by the pure-transport formula below until it reaches index 2).

**Exact amplification profile (linear model, PROVED; exact chase, NUMERICAL).** In the linearised model a kink of turning
δ at chain index m (all earlier candidates on the heading line) has turning δ((m+1)/(n+1))^μ when it sits at index n ≥ 2
(the heading does not change while index 2 is unperturbed, and offsets scale by ((n+1)/n)^μ per leg). The exact chase
(`code/A4/kink.py`, exact straight-run map of `code/H/chase.py`, h = 10⁻³) reproduces this:

| v | μ | m | δ | turning ratio at n = m/2, 10, 3, 2: exact chase (model) |
|---|---|---|---|---|
| 0.1 | 0.111 | 400 | 10⁻⁶ | 1.0798 (1.0798), 1.4912 (1.4912), 1.6686 (1.6686), 1.7228 (1.7228) |
| 0.2 | 0.25 | 400 | 10⁻³ | 1.1885 (1.1885), 2.4572 (2.4572), 3.1642 (3.1643), 3.4002 (3.4002) |
| 0.3 | 0.429 | 400 | 10⁻³ | 1.3445 (1.3445), 4.6700 (4.6701), 7.2044 (7.2046), 8.1497 (8.1499) |
| 0.45 | 0.818 | 400 | 10⁻³ | 1.7596 (1.7596), 18.956 (18.958), 43.352 (43.376), 54.840 (54.888) |

(m = 50 and δ = 10⁻⁶ rows likewise; full output of `python kink.py`.)

**What the right hypothesis must look like (CONJECTURE).** By Lemma A4.2 the quantity that straight runs preserve is C^q,
not the turning angle; a deviation from the smooth profile of size η at distance ρ arrives at the gap scale with size
η(ρ/ℓ)^μ. Hence an N-uniform near-field lemma must carry *scale-weighted* control: at the start of every leg, for the
chain at distance ρ from Harry (ℓ ≤ ρ ≤ r0), the deviation of the second differences of B_i := C_i^q (in the heading frame)
from those of the static/circular profile is ≤ K·ℓ^{1+μ}… equivalently deviations of turning ≤ K·ℓ·(ℓ/ρ)^μ: a discrete
C^{2,μ} condition, μ = v/(1−v). For v → 0 it is barely stronger than C², but it is strictly stronger for every v > 0,
and the far field must supply it (C² closeness does not). The switch update in these variables is the rank-one B-1
recursion B'_i = B_i − B_{j+1}(ρ_i/ρ_{j+1})^q; its stability (H-1, Theorem H3) plus control of this weighted norm,
nonlinear errors O(β²) and the far-field input is what remains. Not proved.

### 5.1 Implicit function / contraction in v around the v = 0 sweep. Negative, PROVED for the linear model
**Proposition A4.4.** For H-1's linearised catch map (L): τ^μ F((1−v)τ) = ∫_0^τ (τ−s)^μ θ(s) ds (θ = heading
perturbation, F = transverse offset of the catch curve, a = 1 + μ = 1/(1−v)), define T_μθ(τ) := F'((1−v)τ) (catch-curve
slope at the matched point). Then for θ ∈ C[0, 1]:
(a) T_μθ(τ) = ∫_0^1 θ(τs) dν_μ(s), dν_μ = μ a (1−s)^{μ−1} s ds, a probability measure; ν_μ → δ_1 as μ → 0, T_0 = I.
(b) T_μ τ^p = R_μ(p) τ^p, R_μ(p) = Γ(a+1)Γ(p+2)/Γ(p+a+1) for p ≥ 0; R_μ(0) = 1, R_μ ↓ 0 as p → ∞ (~Γ(a+1)p^{−μ}).
(c) 0 ≤ 1 − R_μ(p) ≤ μ log(p + 3).
(d) In any normed space of functions on [0, 1] in which T_μ acts and which contains the monomials τ^p (p ∈ ℕ), for every
μ > 0: ||T_μ − T_0|| ≥ 1 and T_μ^{−1} is unbounded; on C[0, 1], ||T_μ − I|| = 2.
*Proof.* (a) F((1−v)τ) = τ^{−μ}∫_0^τ(τ−s)^μθ(s)ds = ∫_0^τ(1 − s/τ)^μ θ(s) ds; differentiate in τ:
(1−v)F'((1−v)τ) = ∫_0^τ μ(1 − s/τ)^{μ−1}(s/τ²)θ(s) ds = μ∫_0^1(1−σ)^{μ−1}σ θ(τσ) dσ; divide by 1 − v = 1/a.
Mass: μ a B(μ, 2) = μ a/(μ(μ+1)) = 1. (b) μ a B(μ, p+2) = aΓ(μ+1)Γ(p+2)/Γ(p+μ+2) = Γ(a+1)Γ(p+2)/Γ(p+a+1).
(c) log R = [log Γ(2+μ) − log Γ(2)] − [log Γ(p+2+μ) − log Γ(p+2)]; by convexity of log Γ the second bracket is ≥ the first
for p ≥ 0, so R ≤ 1; and −log R ≤ μ[ψ(p+2+μ) − ψ(2)] ≤ μ log(p+3) (mean value theorem, ψ increasing, ψ(x) ≤ log x,
ψ(2) > 0); 1 − R ≤ −log R. (d) (T_μ − I)τ^p = (R(p) − 1)τ^p and R(p) → 0; T_μ^{−1}τ^p = τ^p/R(p). On C[0,1]:
||T_μ|| = 1 gives ≤ 2; for ≥ 2 take θ continuous, |θ| ≤ 1, θ(1) = 1, θ = −1 on [0, 1−η]: (I − T_μ)θ(1) ≥ 2 − 2ν_μ((1−η, 1])
and ν_μ((1−η, 1]) ≤ a η^μ → 0. ∎
*Reading.* At v = 0 the catch map is the identity (c_0 = H), so an IFT in v would need D_H c_0 to depend continuously on v
at 0 in operator norm; (d) says it does not, in any space (the linearisation H-1 checked to O(ε²) is about a straight
stretch, so for the circle sweep this is the local, high-frequency part; NUMERICAL as an identification, as in H-1).
(c) quantifies where the loss lives: on modes p ≤ e^{c/μ} the map is within μ log(p+3) of the identity; 1 − R = 1/2 at
log p* = 13.6, 6.7, 3.2, 1.9, 0.94 for v = 0.05, 0.1, 0.2, 0.3, 0.45 (`code/A4/tmu.py`; ≈ 0.7/μ). This is the scale-
separation behind A-2's N^{−κ} (κ ≈ μ/3) convergence: small-v perturbation theory "sees" nothing wrong until the gap is
below e^{−c/v}, but any N-uniform statement must handle those scales (Prop. A4.3 is the same phenomenon in real space).

