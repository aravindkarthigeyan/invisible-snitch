# P7 — claims for independent referees: "Theorem B with an end", passive phases, departures

Stream P7, round 7. Version 1. **Only statements claimed PROVED, with proofs.** Self-contained modulo citations to
`paper/sec_B.tex` (doubly refereed), cited as [B]: Lemma V (= lem:B-V), Lemma VC (lem:B-VC), Lemma 1 (lem:B-1), Lemma 2
(lem:B-2), Lemma 3 (lem:B-3), Lemma 4 (lem:B-4), Lemma C (lem:B-C), Theorem R (thm:R), Theorem B (thm:Bulk) and the
displayed relations (B-1c), (B-star) of its proof. Notation of [B] throughout: field F, A = DF, a*(ρ); virtual candidates
x_θ, r = x − P, ρ = |r|; l, c, e, E = l − c, N = (2E)^{1/2}; μ := v/(1−v) **only inside "e^{2μ}"**; a×b = Im(āb).
Numerical tests (not part of any proof): `code/P7/`, summarised in `reports/P7-1.md`.

Contents. §0 three elementary facts. §1 Theorem P7.B (bulk bootstrap with general exponent **and an end**).
§2 Corollary P7.E (final approach into a benign end, hypothesis (ST_end)). §3 Lemma P7.A (passive far phase).
§4 Theorem P7.D (tangential departure from an end), Proposition P7.D′ (the exponent loss is real), Lemma P7.H
(hand-over from the invariants of Theorem P7.B). §5 Corollary P7.T (two-pass transport). §6 Proposition P7.C
(transversal departure: exact profile; it is a hook, not a rigid rotation).

---------------------------------------------------------------------------------------------------------------------

## §0. Three elementary facts

**Fact 0.1 (excess is monotone under inclusion).** At a fixed time, for labels a ≤ a′ < b′ ≤ b:
E(a′,b′) ≤ E(a,b).
*Proof.* l(a,b) = l(a,a′) + l(a′,b′) + l(b′,b) and c(a,b) ≤ c(a,a′) + c(a′,b′) + c(b′,b); subtract and use E ≥ 0. ∎

**Fact 0.2 (frozen direction).** Fix a unit vector û and a time. For a label interval J = (a,b) put
μ_û(J) := ∫_J |T − û|² ds. Then
 (i) μ_û(J) = 2[l(J) − (x_b − x_a)·û] = N(J)² + c(J)|e_J − û|²; in particular N(J)² ≤ μ_û(J), |e_J − û|² ≤ μ_û(J)/c(J),
 and μ_û is additive over adjacent intervals;
 (ii) (x_b − x_a)·û = l(J) − μ_û(J)/2, and |û × (x_b − x_a)| ≤ ∫_J|T − û| ds ≤ (l(J) μ_û(J))^{1/2}.
*Proof.* |T − û|² = 2 − 2T·û and ∫_J T ds = x_b − x_a = c e_J give the first equality; 2(l − c e·û) = 2(l − c) + 2c(1 − e·û)
and 2(1 − e·û) = |e − û|². (ii): the first is (i); û × (x_b − x_a) = ∫_J û × (T − û) ds, then Cauchy–Schwarz. ∎

**Fact 0.3 (pointwise law for a frozen direction).** Let P be any 1-Lipschitz path, û a fixed unit vector,
w = |∂_θ x|, and D(θ,t) := w(1 − T·û) = ½ w|T − û|². For every label θ, D is C¹ in t and
 ∂_t D = v w (T − û)·A T ≤ v [ 2a*(ρ) D + (2wD)^{1/2} |q_û| ],  q_û := û^⊥·A(r)û,  |q_û| ≤ |r × û| / max(ρ,ε)².
Consequently χ := (2D)^{1/2} = w^{1/2}|T − û| satisfies, for t₁ ≤ t₂ and 𝒜(t) := exp(v∫_{t₁}^{t} a*(ρ_θ)),
 χ(t₂) ≤ 𝒜(t₂) χ(t₁) + v ∫_{t₁}^{t₂} (𝒜(t₂)/𝒜(t)) w(t)^{1/2} |q_û(t)| dt,  and  w(t₂) ≤ 𝒜(t₂) w(t₁).
*Proof.* D = w − ∂_θx·û; by [B, Lemma VC(a), Lemma 1(i)], ∂_t∂_θx = vA∂_θx = v w AT and w_t = v w T·AT, so
∂_tD = v w (T − û)·AT. As in [B, Lemma 2(ii)] with e replaced by the constant û:
(T − û)·AT = (T − û)·A(T − û) − ½|T − û|²(û·Aû) + (T·û^⊥) q_û ≤ a*|T − û|² + |T − û||q_û| (A ≥ 0, A ≤ a*I by Lemma V(ii),
|T·û^⊥| = |(T − û)·û^⊥| ≤ |T − û|); multiply by v w. The bound for q_û is Lemma V(iii). For χ_η := (2D + η²)^{1/2}:
χ_ηχ_η′ = ∂_tD ≤ v a* χ_η² + v w^{1/2} χ_η |q_û|, so χ_η′ ≤ v a* χ_η + v w^{1/2}|q_û|; variation of constants, η → 0.
w_t = v w T·AT ≤ v a* w. ∎

---------------------------------------------------------------------------------------------------------------------

## §1. Theorem P7.B — the bulk bootstrap with exponent 1/2 + γ, on an arc that ENDS

**Construction C from (t_s, a_s) cut at b_E.** Let P be an arbitrary 1-Lipschitz path on [0, t_s], x_θ its virtual
candidates, and a_s < b_E labels with b_E − a_s < 2π and P(t_s) = x_{a_s}(t_s). For t ≥ t_s, P follows the legs of
construction C of [B] with the final label 2π replaced by b_E: with a_{j_s} := a_s, t_{j_s} := t_s,
a_{j+1} := max{θ ∈ [a_j, b_E] : l_{t_j}(a_j,θ) ≤ ε}; if a_{j+1} = b_E the construction **stops at t_j**; otherwise P runs at
unit speed along the ray from P(t_j) through x_{a_{j+1}}(t_j) until it meets x_{a_{j+1}}, at time t_{j+1}.
[B, Lemma C(0),(2),(3),(4)] hold verbatim (their proofs use the final label only as the end of the arc and use the
path only from the leg start on; cf. the last clause of [B, Cor. M]). By reflection of the plane, everything below
also holds for an arc traversed in the direction of decreasing labels.

**Standing assumptions of §1.** γ ∈ (0, 1/4] and v ≤ 2·10⁻¹¹γ² (so e^{2μ} ≤ 2, ε₁ ≤ 2ε, every leg lasts ≤ 2ε).
Put ν := 22v, R ∈ (0,1], **M := (γ/50) R^{−γ}** (so m := MR^γ = γ/50 ≤ 1/200), and the constants
 c₁ := 4.85, **C_TL := 16.5/γ**, C_μ := 2 + 2.25C_TL² ≤ 613/γ², C₁ := 1.6 C_TL = 26.4/γ, C_ϑ := 47/γ.
*Labels.* u ∈ [0,U] := arclength at time t_s along the arc [a_s, b_E], measured from x_{a_s}; U = l_{t_s}(a_s,b_E).
For labels a < b in the arc, λ := u_b − u_a. Lengths and chords are non-decreasing in t [B, Lemma VC].

**Start hypothesis (ST_γ)** at t_s:
 (S1) c(a,b;t_s) ≥ ½ min(λ, 32R) for all pairs with λ ≥ ε/2;
 (S2) N(a,b;t_s) ≤ (M/8) λ^{1/2+γ} · min(1, 64λ / min(u_a, 32R))^{ν} for all pairs with ε/2 ≤ λ ≤ R
   (the last factor is 1 when u_a = 0);
 (S3) ε ≤ R/64.
By (S1) and monotonicity of chords, for all t ≥ t_s and all pairs with λ ≥ ε/2:
 **(CA)** c(a,b;t) ≥ ½ min(λ, 32R).

*Family.* For t in leg j+1 (t_j ≤ t ≤ t_{j+1}, j ≥ j_s; at a switching time both legs count), 𝔉(t) := pairs (a,b) with
u_b ≤ U, ε/2 ≤ λ ≤ R and (a = a_j or a ≥ a_{j+1}). Gap g := u_a − u_{a_j} ≥ 0; *far* if g ≥ 64λ, *near* otherwise.
𝔉(t) shrinks and g is non-increasing as t grows.

> **Theorem P7.B.** Assume (ST_γ), γ ∈ (0,1/4], v ≤ 2·10⁻¹¹γ² and v(4U + 2) ≤ 10⁻⁶γR. Then:
> **(a) Invariants.** For every t from t_s until the construction stops and every pair of 𝔉(t):
>  (J1) l_t(a,b) ≤ (9/8)λ (in fact ≤ 1.01λ);  (J2) N(a,b;t) ≤ M λ^{1/2+γ}, i.e. E ≤ ½M²λ^{1+2γ}.
> **(b) The end.** Every non-final leg advances the base label by u_{a_{j+1}} − u_{a_j} ∈ [ε/2, ε]. The construction
>  stops, at a leg start T_stop = t_J with J − j_s ≤ 2U/ε and T_stop ≤ t_s + 2U/(1−v); at T_stop,
>  l_{T_stop}(a_J, b_E) ≤ ε, so every label of [a_s, b_E] has been seen by T_stop, and |P(T_stop) − x_{b_E}(T_stop)| ≤ ε.
> **(c) Flatness, separation, K̃.** For every non-final leg j+1 > j_s and every t in it, (F_b) and (S) of [B, Theorem R]
>  hold with b* = b_E and γ, r₀ = R, c₀ = γ²/5000, c₁ = 0, r₁ = R/8; and
>  K̃(t) := ∫_{a_{j+1}}^{b_E} T·AT ds ≤ 17 + 19U/R.
> **(d) Tilts.** At any such t, for pairs J ⊂ I of 𝔉(t): |e_J − e_I| ≤ C_TL M λ_I^γ = (0.33)(λ_I/R)^γ.
> No constant depends on ε.

So no pair is ever "beyond the arc": (J1), (J2) hold for pairs arbitrarily close to b_E (down to scale ε/2) while the
base approaches b_E, and the last leg is covered by (b).

### Proof of Theorem P7.B

**Continuity argument.** Let t* be the supremum of the times t′ ≤ T_end (T_end := stopping time, or ∞) such that
(J1), (J2) hold for all t ∈ [t_s,t′] and all pairs of 𝔉(t). At t_s: l = λ and N ≤ (M/8)λ^{1/2+γ}. We show
 **(Imp)** if (J1), (J2) hold on [t_s, t*), then for every t ≤ t* (t < ∞) and every pair of 𝔉(t):
  l_t ≤ 1.01λ and E ≤ ¼M²λ^{1+2γ}.
Given (Imp), exactly as in [B]: the bounds of (Imp) hold at t* by continuity (a pair of 𝔉(t*) is in 𝔉(t), t < t*); for
t ∈ [t*, t*+δ], l_t ≤ e^{2vδ/ε}l_{t*} and E(t) ≤ ¼M²λ^{1+2γ} + δ(4v/ε)·2λ (|E′| ≤ v∫|T − e||AT| ≤ (4v/ε)l), which stay
below (J1), (J2) for a δ > 0 depending only on (v,ε,M,γ) because λ ≥ ε/2; and 𝔉(t) ⊂ 𝔉(t*). So t* = T_end (finitely
many legs on bounded time intervals, Lemma C(0)). From now on (J1), (J2) ("family bounds") are assumed on [t_s,t*)
and, by continuity, at t*; all times are ≤ t*.

**Step 1 (legs, the end, times, distances).**
(a) *Dichotomy at a leg start t_j (j ≥ j_s).* (α) If U − u_{a_j} ≥ ε/2, then leg j+1 is final or
u_{a_{j+1}} − u_{a_j} ∈ [ε/2, ε]. (β) If U − u_{a_j} < ε/2, then l_{t_j}(a_j,b_E) ≤ ε, i.e. leg j+1 is final.
*Proof.* u_{a_{j+1}} − u_{a_j} ≤ l_{t_j}(a_j,a_{j+1}) ≤ ε always. (α): the label s with u_s = u_{a_j} + ε/2 is ≤ U, the
pair (a_j,s) is in 𝔉(t_j), and (J1) gives l_{t_j}(a_j,s) ≤ 9ε/16 ≤ ε, so a_{j+1} ≥ s by maximality. (β): by induction
on j. For j = j_s: l_{t_s}(a_s,b_E) = U < ε/2. For j > j_s: leg j was not final, so by the induction hypothesis (β)
did not apply at t_{j−1}; hence (α) applied and λ₁ := u_{a_j} − u_{a_{j−1}} ∈ [ε/2, ε]. With λ₂ := U − u_{a_j} < ε/2, the
pair (a_{j−1}, b_E) has label length λ₁ + λ₂ ∈ [ε/2, 3ε/2] ⊂ [ε/2, R] and belongs to 𝔉(t_j) (as a pair of leg j, whose
closed time interval contains t_j). By (J1) and l_{t_j}(a_{j−1},a_j) ≥ λ₁:
l_{t_j}(a_j,b_E) ≤ (9/8)(λ₁+λ₂) − λ₁ = λ₁/8 + 9λ₂/8 < ε/8 + 9ε/16 < ε. ∎
(b) Hence every non-final leg advances the base label by ≥ ε/2, there are at most 2U/ε non-final legs after j_s, each
of duration ≤ ε/(1−v) ≤ 2ε, and the time elapsed since t_s is at most T_B := 4U + 2 (indeed ≤ 2U/(1−v)).
(c) [B, (B-1c)] holds with the same proof: for a fixed label a the gaps at successive legs are spaced by ≥ ε/2, and
each leg lasts ≤ 2ε; so for non-increasing h ≥ 0 and g₀ ≥ 0,
 ∫_{{t: g(t) ≥ g₀}} h(g(t)) dt ≤ 2ε h(g_min) + 4∫_{g_min}^∞ h(g) dg,  g_min := smallest attained gap ≥ g₀.
(d) [B, (B-star)] holds with the same proof ((CA) and Lemma C(4)): for t in leg j+1 and w_s := u_s − u_{a_j} ≥ 0,
 ρ_s ≥ ½min(w_s,32R) − 2ε, hence max(ρ_s, ε) ≥ (1/6) min(w_s, 32R). (∗)

**Step 2 (tilt lemma) = part (d).** *At any time, for J ⊂ I in the family:* |e_J − e_I| ≤ C_TL M λ_I^γ. (TL)
First let J₁ ⊂ I₁ be family pairs with λ_{I₁} ≤ 3λ_{J₁}. By [B, Lemma 4(a)], (J1), (J2), (CA) (c(J₁) ≥ λ_{J₁}/2):
 |e_{J₁} − e_{I₁}| ≤ [ (9λ_{J₁}/8)^{1/2} M (3λ_{J₁})^{1/2+γ} + ½M²λ_{J₁}^{1+2γ} ] · 2/λ_{J₁}
  = Mλ_{J₁}^γ [ 2(9/8)^{1/2} 3^{1/2+γ} + Mλ_{J₁}^γ ] ≤ c₁ M λ_{J₁}^γ,
since 3^{1/2+γ} ≤ 3^{3/4} = 2.2796, 2·1.0607·2.2796 = 4.836 and Mλ^γ ≤ m ≤ 0.005. Let S := 1/(1 − 2^{−γ}); by concavity
of γ ↦ 1 − 2^{−γ} on [0,1/4], 1 − 2^{−γ} ≥ 4γ(1 − 2^{−1/4}) = 0.6364γ, so S ≤ 1.5714/γ. Now let J = (a′,b′) ⊂ I = (a,b),
t in leg j+1.
(A) b_k := min(u_{a′} + 2^kλ_J, u_b), k = 0,…,k₁, b_{k₁} = b. The arcs (a′,b_k) are in the family (first point a′,
length ≤ R), consecutive label lengths have ratio ≤ 2, and λ(a′,b_k) = 2^kλ_J ≤ λ_I for k < k₁:
Σ_{k<k₁} c₁M(2^kλ_J)^γ ≤ c₁ S M λ_I^γ.
(B) If a′ > a: let a° := a if a ≥ a_{j+1}, a° := a_{j+1} if a = a_j; a′_k := max(u_b − 2^kλ(a′,b), u_{a°}). The arcs (a′_k,b)
start at labels ≥ a_{j+1}, so they are in the family; the same sum is ≤ c₁SMλ_I^γ.
(C) If a = a_j ≠ a°: (a_{j+1},b) ⊂ (a_j,b), λ(a_j,b) ≤ λ(a_{j+1},b) + ε ≤ 3λ(a_{j+1},b) (λ(a_{j+1},b) ≥ λ_J ≥ ε/2): one
more step, ≤ c₁Mλ_I^γ.
Total ≤ c₁(2S + 1)Mλ_I^γ ≤ 4.85(3.1428/γ + 1)Mλ_I^γ ≤ (16.46/γ)Mλ_I^γ (1 ≤ 0.25/γ). This is (TL), and
C_TL M λ_I^γ = (16.5/γ)(γ/50)(λ_I/R)^γ. ∎
*Consequence.* For a family pair (a,b) and a family sub-arc J ⊂ (a,b) with label length λ_J (shorter arcs
starting at a family first point are enlarged to label length ε/2 inside (a,b) where this is used):
 ∫_J|T − e_{ab}|² ds ≤ 2N(J)² + 2l(J)|e_J − e_{ab}|² ≤ 2M²λ_J^{1+2γ} + (9/4)λ_J C_TL²M²λ^{2γ} ≤ C_μ M²λ^{2γ}λ_J, (Mu)
 ∫_J|T − e_{ab}| ds ≤ ((9/8)λ_J · C_μM²λ^{2γ}λ_J)^{1/2} ≤ C₁ M λ^γ λ_J
((9/8)C_μ = 2.25 + 2.53125C_TL² ≤ (1.6C_TL)², as C_TL ≥ 66).

**Step 3 (far pairs: N ≤ (3/8)Mλ^{1/2+γ}).** Let (a,b) be far at time t (leg j+1): g ≥ 64λ ≥ 32ε, so a > a_{j+1}, and
the pair has been in the family and far since t_s. Put ĝ := min(g,32R). The hull of the arc lies in B(x_a,l),
l ≤ 2λ, so by (∗) ρ_m ≥ ĝ/2 − 2ε − 2λ, and as in [B, Step 3]: if g ≤ 32R this is ≥ g/2 − 6λ ≥ (1/2 − 6/64)g, which is
≥ g/4 and ≥ 26λ; if g > 32R it is ≥ 16R − R/32 − 2R ≥ 13.9R ≥ 8R = ĝ/4 and ≥ 13.9λ. So
 ρ_m ≥ ĝ/4 and ρ_m ≥ 13.9λ ≥ max(ε, 4l),
and [B, Lemma 3(e)] applies on the whole far period with α ≤ 1.375v/ρ_m ≤ 5.5v/ĝ.
*Amplification.* Between gaps g₁ ≥ g₂ (both ≤ 32R), by (c): ∫α ≤ 5.5v[2ε/g₂ + 4log(g₁/g₂)] ≤ 0.35v + 22v log(g₁/g₂);
while g > 32R, ∫α ≤ 5.5vT_B/(32R). With A₀ := exp(v(0.35 + 0.18T_B/R)) ≤ 2:
 exp(∫α) ≤ A₀ (min(g₁,32R)/g₂)^ν.
*Forcing β = 2v l^{3/2}|p_a|/ρ_m³.* If g > R/2: exactly as in [B] (only l ≤ 2λ and the bounds on ρ_m are used),
β ≤ 408 vλ^{3/2}/R². If g ≤ R/2: P ∈ [x_{a_j}, x_{a_{j+1}}] (Lemma C(2)), so
|p_a| ≤ max_{a′∈{a_j,a_{j+1}}} dist(x_{a′}, line(x_a,x_b)) = c(a′,a)|e_{a′a} × e_{ab}| ≤ c(a′,a)(|e_{a′a} − e_{a′b}| + |e_{ab} − e_{a′b}|).
The pairs (a′,a), (a,b), (a′,b) are in the family (label lengths ≥ 64λ − ε ≥ ε/2, resp. ≤ g + λ ≤ R), c(a′,a) ≤ (9/8)g,
and (TL) with λ(a′,b) ≤ g + λ ≤ (65/64)g gives
 |p_a| ≤ (9/8)g · 2C_TL M((65/64)g)^γ ≤ 2.26 C_TL M g^{1+γ},
 β ≤ 2v(9λ/8)^{3/2} · 2.26C_TLMg^{1+γ} · 64/g³ ≤ 346 v C_TL M λ^{3/2} g^{γ−2}.
*Result.* Let g_s := u_a be the gap at t_s and g₂ ≥ 64λ the gap at time t. By Lemma 3(e), (S2) and (c) with
h(g) = g^{ν+γ−2} (non-increasing):
 N ≤ A₀(min(g_s,32R)/g₂)^ν N(t_s) + A₀(32R/g₂)^ν · 408vT_Bλ^{3/2}/R² + A₀ · 346vC_TLMλ^{3/2} g₂^{−ν}[2εg₂^{ν+γ−2} + 4g₂^{ν+γ−1}/(1−γ−ν)].
First term: ≤ 2·(M/8)λ^{1/2+γ}(64λ/min(g_s,32R))^ν(min(g_s,32R)/g₂)^ν = (M/4)λ^{1/2+γ}(64λ/g₂)^ν ≤ (M/4)λ^{1/2+γ}.
Second term: (32R/g₂)^ν ≤ (R/λ)^ν and λ^{3/2}(R/λ)^ν = λ^{1/2+γ}λ^{1−γ−ν}R^ν ≤ λ^{1/2+γ}R^{1−γ}; so it is
≤ 816(vT_B/R)R^{−γ}λ^{1/2+γ} = 816·(50/γ)(vT_B/R) Mλ^{1/2+γ} ≤ 0.041 Mλ^{1/2+γ}, by vT_B ≤ 10⁻⁶γR.
Third term: 2ε/g₂ ≤ 1/16 and 1−γ−ν ≥ 0.74, so [...] ≤ 5.47g₂^{ν+γ−1}, and g₂^{γ−1} ≤ (64λ)^{γ−1} ≤ 64^{−3/4}λ^{γ−1} = 0.0442λ^{γ−1};
so it is ≤ 2·346·5.47·0.0442 vC_TLMλ^{1/2+γ} ≤ 168·(16.5/γ)vMλ^{1/2+γ} ≤ 2772(v/γ)Mλ^{1/2+γ} ≤ 10⁻⁷Mλ^{1/2+γ}.
Hence N ≤ (1/4 + 0.041 + 10⁻⁷)Mλ^{1/2+γ} ≤ (3/8)Mλ^{1/2+γ}, i.e. **E ≤ (9/128)M²λ^{1+2γ} ≤ M²λ^{1+2γ}/8 for far pairs.**

**Step 4 (near pairs).** Let (a,b) ∈ 𝔉(t) be near. As in [B, Step 4] the total time a pair spends near is ≤ 264λ; when
it becomes near (or at t_s) E ≤ M²λ^{1+2γ}/8 (Step 3; resp. (S2): E(t_s) ≤ M²λ^{1+2γ}/128); and during the near period
all sub-arcs used below are family pairs. We bound the increase ΔE while near by integrating [B, Lemma 3(a)] with
q̄ = 0: E′ ≤ I + II, I := v∫_a^b a*(ρ)|T − e|², II := v∫_a^b|τ||q|, e := e_{ab}. Put ρ̄ := max(ε, min_{[a,b]}ρ),
g̃ := max(g,ε); as in [B], log⁺(λ/(6ρ̄)) ≤ log⁺(λ/g̃).
*Term I.* With ω(y) := ∫_{{s∈(a,b): ρ_s<y}}|T − e|² ds: I = v[ω(ε)/ε + ∫_ε^∞ ω(y)y^{−2}dy]. By (∗), ρ_s < y forces
w_s < 2y + 4ε when 2y + 4ε ≤ 32R, so these s lie in the sub-arc J_y of (a,b) starting at a with label length
max(min(λ, 2y+4ε−g), ε/2) ≤ min(λ,6y) (y ≥ ε), a family pair; by (Mu), ω(y) ≤ C_μM²λ^{2γ}min(λ,6y) (for larger y
trivially, since then 6y ≥ λ and ω ≤ N² ≤ M²λ^{1+2γ}), and ω(y) = 0 for y ≤ min ρ. Hence
 I ≤ vC_μM²λ^{2γ}[6 + ∫_{ρ̄}^{λ/6} 6dy/y + ∫_{λ/6}^∞ λdy/y²] ≤ 6vC_μM²λ^{2γ}[2 + log⁺(λ/g̃)].
*Term II.* |q| ≤ |p(s)|/max(ρ_s,ε)², p(s) := (x_s − P) × e, and |p(s)| ≤ max_{a′∈{a_j,a_{j+1}}}|(x_s − x_{a′}) × e|. Let
 ϑ := C_ϑ M λ^γ if 65λ ≤ R,  ϑ := 2 otherwise;
in both cases C₁Mλ^γ ≤ ϑ ≤ 2 (C₁m = 0.528; C_ϑ m = 0.94) and, if 65λ ≤ R, C_TL M(65λ)^γ ≤ 2.84C_TLMλ^γ ≤ ϑ. Put
λ_s′ := max(u_s − u_a, ε/2).
 – *Case a′ ≤ a.* (x_s − x_{a′}) × e = ∫_a^s τ + (x_a − x_{a′}) × e. The first term is ≤ ∫_{(a,s)}|T − e| ≤ C₁Mλ^γλ_s′ ≤ ϑλ_s′.
 The second vanishes if a′ = a. Let 65λ ≤ R. If g′ := u_a − u_{a′} ≥ ε/2: it equals c(a′,a)|e_{a′a} × e_{ab}| ≤
 (9/8)g′·2C_TLM(65λ)^γ ≤ 4ϑg ((a′,a), (a,b), (a′,b) are family pairs, λ(a′,b) ≤ 65λ ≤ R). If 0 < g′ < ε/2 (then
 a′ = a_{j+1}): with J₀ := (a′, label u_{a′}+ε/2) ⊂ (a′,b), a family pair, and (TL) in (a′,b) (λ(a′,b) ≤ 2λ):
 |(x_a − x_{a′}) × e| ≤ l(a′,a)^{1/2}(∫_{J₀}|T − e_{ab}|²)^{1/2} ≤ (9ε/16)^{1/2}[2M²(ε/2)^{1+2γ} + (9/8)ε(2ϑ)²]^{1/2} ≤ 3ϑε.
 – *Case a = a_j, a′ = a_{j+1} ≤ b.* (x_s − x_{a′}) × e = ±∫τ over the arc between a′ and s, contained in
 (a, max(s,a′)) ⊂ (a,b): ≤ ϑ max(λ_s′, ε).
 – *Case a = a_j, a′ = a_{j+1} > b* (then λ < ε). I := (a_j,a_{j+1}) is a family pair containing (a,b), with
 ε/2 ≤ λ_I ≤ ε ≤ 2λ: |(x_s − x_{a′}) × e| ≤ ∫_I|T − e_I| + l(I)|e_I − e_{ab}| ≤ (9λ_I/8)^{1/2}Mλ_I^{1/2+γ} + (9/8)λ_I C_TLMλ_I^γ
 ≤ 1.19C_TLM(2λ)^γ ε ≤ ϑε.
So if 65λ ≤ R: |p(s)| ≤ ϑ(λ_s′ + 4g + 3ε) ≤ ϑ(5w_s + 4ε), and with (∗), for w_s ≤ 32R,
 |q| ≤ ϑ(5w_s + 4ε)/max(ε, w_s/6)² ≤ 34ϑ/max(ε, w_s/6) = ∫_{max(w_s,6ε)}^∞ 204ϑ y^{−2}dy;
if 65λ > R (ϑ = 2) the same bound holds since |p| ≤ ρ_s. For w_s > 32R, |q| ≤ 1/ρ_s ≤ 1/(15R). With
∫_{{s∈(a,b): w_s<y}}|T − e| ≤ ϑ min(λ,y) for y ≥ 6ε (Step 2; zero if y ≤ g):
 II ≤ 204vϑ²∫_{max(6ε,g)}^∞ min(λ,y)y^{−2}dy + (v/15R)∫_a^b|T − e| ≤ 204vϑ²[1 + log⁺(λ/g̃)] + 0.1vMλ^{1+γ}/R.
*Time integrals* (as in [B], from (c)): ∫_near[1 + log⁺(λ/g̃)]dt ≤ 272λ, ∫_near[2 + log⁺(λ/g̃)]dt ≤ 536λ. So
 ΔE ≤ 3216 C_μ vM²λ^{1+2γ} + 55488 vϑ²λ + 26.4 vMλ^{2+γ}/R.
Here C_μ ≤ 613/γ²; Mλ^{2+γ}/R ≤ M²λ^{1+2γ}/m = (50/γ)M²λ^{1+2γ}; if 65λ ≤ R, ϑ²λ = (2209/γ²)M²λ^{1+2γ}; if 65λ > R,
ϑ²λ = 4λ ≤ 4(65/R)^{2γ}λ^{1+2γ} = 4·65^{2γ}M²λ^{1+2γ}/m² ≤ (80700/γ²)M²λ^{1+2γ}. In all cases
 ΔE ≤ (4.5·10⁹/γ²) v M²λ^{1+2γ} ≤ 0.09 M²λ^{1+2γ} ≤ M²λ^{1+2γ}/8,
so **E ≤ M²λ^{1+2γ}/4 for near pairs**; with Step 3 this is the E-part of (Imp).

**Step 5 ((J1): l ≤ 1.01λ).** l(t_s) = λ, l′ = v∫T·AT.
*Far, g > R/2:* T·AT ≤ 1/ρ_m ≤ 8/R; total increase of log l ≤ 8vT_B/R ≤ 8·10⁻⁶γ.
*Far, g ≤ R/2:* by [B, Lemma 3(c)], l′ ≤ (2v/ρ_m)[l(|p_a| + l^{1/2}N)²/ρ_m² + N²] with
|p_a| + l^{1/2}N ≤ 2.26C_TLMg^{1+γ} + 1.07Mλ^{1+γ} ≤ 2.27C_TLMg^{1+γ}, ρ_m ≥ g/4, N² ≤ M²λ^{1+2γ} ≤ lM²g^{2γ}:
(log l)′ ≤ (8v/g)(16·2.27²C_TL² + 1)M²g^{2γ} ≤ 661C_TL²vM²g^{2γ−1}; by (c), ∫g^{2γ−1}dt ≤ 2ε(32ε)^{2γ−1} + 4∫_0^{R/2}g^{2γ−1}dg
≤ (2.02/γ)R^{2γ}. Total ≤ 661·(272.25/γ²)(2.02/γ)v m² ≤ 146 v/γ.
*Near:* T·AT ≤ a*(ρ), so l′ ≤ v[m̃(ε)/ε + ∫_ε^∞ m̃(y)y^{−2}dy] with m̃(y) := |{s∈(a,b): ρ_s<y}| ≤ (9/8)min(λ,6y) ((J1) for
J_y); hence l′ ≤ 6.75v[2 + log⁺(λ/g̃)] and the increase while near is ≤ 3618vλ.
Altogether l_t ≤ λ exp(8·10⁻⁶γ + 146v/γ) + 3618vλ ≤ 1.00001λ. This proves (Imp), hence **(a)**. ∎

**Proof of (b).** By Step 1(a),(b) (now valid up to T_end): every non-final leg advances the base label by ≥ ε/2
(and ≤ ε), so there are at most 2U/ε non-final legs, each of duration ≤ ε/(1−v): the construction stops at a leg start
T_stop ≤ t_s + 2U/(1−v), with a_{J+1} = b_E, i.e. l_{T_stop}(a_J,b_E) ≤ ε. By Lemma C(3) every θ ∈ [a_j,a_{j+1}] is seen by
t_j, for all j ≤ J; these intervals cover [a_s,b_E]. |P − x_{b_E}| = c(a_J,b_E) ≤ l ≤ ε. ∎

**Proof of (c).** Let leg j+1 be non-final, t in it, s ∈ (a_{j+1}, b_E]. By (b), λ(a_j,s) ≥ ε/2. If l := l_t(a_j,s) ≤ R:
λ ≤ l ≤ R, the pair is in 𝔉(t), and E ≤ ½M²λ^{1+2γ} ≤ ½m² l (l/R)^{2γ}: (F_b) with c₀ = m²/2 = γ²/5000. If l > R: then
λ > R/2 (if λ ≤ R, (J1) gives λ ≥ 8l/9), and by (CA) and Lemma C(4), ρ_s ≥ ½min(λ,32R) − 2ε ≥ R/4 − R/32 ≥ R/8: (S).
For K̃ apply the Claim in the proof of [B, Theorem R] (which uses only (F_b), (S), Lemma C and R_j ≤ L_s) with b* = b_E,
K_T = 0 and L_s := (9/8)U: indeed R_j = l_{t_j}(a_j,b_E) ≤ (9/8)(U − u_{a_j}) (split [a_j,b_E] into consecutive family pairs
of 𝔉(t_j) with label lengths in [ε/2,R], the first starting at a_j; if U − u_{a_j} < ε/2 then R_j ≤ ε and leg j+1 is
final). The Claim gives K̃ ≤ 16e^{2μ} + 4c₀(1 + 1/γ) + 2e^{2μ}L_s/r₁ ≤ 16.01 + 0.001 + 18.01U/R (2·(9U/8)·(8/R) = 18U/R). ∎

**Remarks.** (1) *What the proof of Theorem B uses of (ST).* The cubic bound E ≤ κ²λ³ is used nowhere except through
the three items of [B, Remark "Relaxed start"]: (CA) at t_s, the start value of near pairs, and N(t_s) in the first term
of Step 3. All structural steps (tilt lemma, far forcing, near terms I, II, length) work for the invariant exponent
1 + 2γ with any γ ∈ (0, 1/4] (γ < 1 − ν would do, with other constants): the tilt-lemma constant is ∼ 1/γ (geometric
series over scales), the far forcing ∫g^{ν+γ−2}dg and the length integral ∫g^{2γ−1}dg converge, and v must be small
against γ². The start exponent only has to exceed the invariant exponent by the amplification exponent ν = 22v
((S2)). Theorem P7.B with γ = 1/4 is [B, Theorem B] under a relaxed start of the type (W1)–(W3) of the unrefereed remark
of [B] (with the normalisation m = MR^{1/4} = 1/200 and C_TL = 66 in place of 1/140 and 91, so (S2) is slightly
stronger than (W2)), **with a complete written proof**, and it removes the restriction
"legs whose target stays within the arc": when the arc where the start condition holds reaches the end of the unseen
set, the restriction is void.
(2) *Reflection.* For an arc traversed towards decreasing labels apply the theorem to the reflected configuration.
(3) *Harry at E.* If the design wants P = x_{b_E}, one more straight leg to x_{b_E} costs ≤ ε/(1−v).

---------------------------------------------------------------------------------------------------------------------

## §2. Corollary P7.E — final approach into a benign end

**Hypothesis (ST_end)** at a leg start t_s of the construction of §1 (arc A = [a_s,b_E], labels u ∈ [0,U] as in §1), with
constants a′ ∈ (0,1], C₀ > 0, λ₀ ∈ (0,1], c_sep > 0 such that C₀λ₀^{a′} ≤ 1:
 (E1) N(a,b;t_s) ≤ C₀ λ^{1/2+a′} (i.e. E ≤ ½C₀²λ^{1+2a′}) for all pairs in A with ε/2 ≤ λ ≤ λ₀;
 (E2) c(a,b;t_s) ≥ c_sep for all pairs in A with λ > λ₀.

> **Corollary P7.E.** Assume (ST_end). Put γ := min(a′/2, 1/4), R := min(1, λ₀/32, c_sep/16, (γ/(400C₀))^{1/a′}).
> Then for all ε ≤ R/64 and all v ≤ v₀ := min(2·10⁻¹¹γ², 10⁻⁶γR/(4U+2)), (ST_γ) holds and all conclusions of
> Theorem P7.B hold: the construction sees every label of A and stops within time 2U/(1−v) of t_s at arclength
> distance ≤ ε from the end, with K̃ ≤ 17 + 19U/R, and E(a,b;t) ≤ ½M²λ^{1+2γ} for all pairs ahead of the base at all
> scales ε/2 ≤ λ ≤ R, up to the end. v₀ and all constants depend only on (a′, C₀, λ₀, c_sep, an upper bound for U).

*Proof.* (S3) is assumed. ν = 22v ≤ 4.4·10⁻¹⁰γ² ≤ γ ≤ a′ − γ, so γ + ν ≤ a′. (S2): for ε/2 ≤ λ ≤ R (≤ λ₀):
N ≤ C₀R^{a′}(λ/R)^{a′}λ^{1/2} ≤ (γ/400)(λ/R)^{γ+ν}λ^{1/2} = (M/8)λ^{1/2+γ}(λ/R)^ν, and (λ/R)^ν ≤ min(1, 2λ/R)^ν ≤
min(1, 64λ/min(u_a,32R))^ν. (S1): for ε/2 ≤ λ ≤ λ₀, E ≤ ½(C₀λ^{a′})²λ ≤ λ/2, so c ≥ λ/2, which is ≥ ½min(λ,32R); for λ > λ₀,
c ≥ c_sep ≥ 16R. ∎

**Remark (same-side restart from the output of Theorem P7.B / Theorem B).** If (J1), (J2) hold with (γ₁,R₁,M₁) and
t_j is a later leg start, then at t_j, in the labels u′ := l_{t_j}(a_j,·): λ ≤ λ′ ≤ (9/8)λ for family pairs, and for every
pair with a ≥ a_j, ε/2 ≤ λ′ ≤ R₁: N ≤ M₁λ′^{1/2+γ₁} (if λ < ε/2 enlarge the pair to old label length ε/2 ≤ λ′, on either
side inside [a_j,b_E], and use Fact 0.1); and c ≥ 4R₁/9 for λ′ > R₁ by (CA). So (ST_end) holds with a′ = γ₁, C₀ = M₁,
λ₀ = R₁, c_sep = 4R₁/9: the class is closed under restarting, with γ = γ₁/2.

---------------------------------------------------------------------------------------------------------------------

## §3. Lemma P7.A — passive far phase

> **Lemma P7.A.** Let P be any 1-Lipschitz path, Γ a label interval, [t′,t″] a time interval and ρ₀: [t′,t″] → [ε,∞)
> continuous with dist(P(t), conv{x_s(t): s ∈ Γ}) ≥ ρ₀(t) for all t. Put Λ(t) := v∫_{t′}^{t} dτ/ρ₀(τ) and assume
> l_{t′}(Γ) e^{Λ(t)} ≤ ρ₀(t)/4 on [t′,t″]. Then for every pair (a,b) ⊂ Γ and t ∈ [t′,t″]:
>  (i) l_{t′}(a,b) ≤ l_t(a,b) ≤ e^{Λ(t)} l_{t′}(a,b), c(a,b;t) ≥ c(a,b;t′);
>  (ii) N(a,b;t) ≤ e^{1.375Λ(t)} [ N(a,b;t′) + 2.5 v l_t(a,b)^{3/2} ∫_{t′}^{t} dτ/ρ₀(τ)² ].
> In particular for constant ρ₀ and T := t − t′: N(t) ≤ e^{1.375vT/ρ₀}[N(t′) + 2.5vT l_t^{3/2}/ρ₀²], whence
> E(t) ≤ e^{2.75vT/ρ₀}[2E(t′) + 6.25 v²T² l_t³/ρ₀⁴].

*Proof.* (i) Monotonicity is Lemma VC. On Γ, ρ ≥ ρ₀ ≥ ε, so T·AT ≤ 1/ρ₀ and l′ = v∫T·AT ≤ (v/ρ₀)l. (ii) The hull of
the arc of (a,b) is contained in that of Γ, so ρ_m ≥ ρ₀ ≥ max(ε, 4l_t(Γ)) ≥ max(ε,4l) and [B, Lemma 3(e)] applies with
α ≤ 1.375v/ρ₀ and β = 2v l^{3/2}|p_a|/ρ_m³. Since x_a lies in the hull of the arc, whose diameter is ≤ l,
|p_a| ≤ ρ_a ≤ ρ_m + l ≤ 1.25ρ_m; so β ≤ 2.5v l^{3/2}/ρ_m² ≤ 2.5 v l_t^{3/2}/ρ₀(τ)² (l is non-decreasing). Insert, and bound
exp(∫_τ^t α) ≤ e^{1.375Λ(t)}. The E-form is (x+y)² ≤ 2x² + 2y². ∎

The additive term is a curvature increment ≈ vT/ρ₀² (exponent 3/2 in N): it never spoils a bound N ≤ Cλ^{1/2+γ}, γ ≤ 1.

---------------------------------------------------------------------------------------------------------------------

## §4. Theorem P7.D — tangential (collinear) departure from an end

**Setting.** P is a 1-Lipschitz path, t_E a time, E a label with P(t_E) = x_E(t_E), û a unit vector, D > 0, and
 P(t) = P(t_E) − (t − t_E)û for t ∈ [t_E, t_E + D]  (τ := t − t_E).
Consider an arc of the front starting at E (on one side), labelled by its arclength u ∈ [0,U_E] at time t_E measured
from x_E, U_E ≥ ε/2; λ := u_b − u_a; μ_t(a,b) := μ_û(a,b) at time t (Fact 0.2); ū := max(u, ε/2).
**Hypotheses**, with γ ∈ (0,1/4], ϑ₀ > 0:
 (D1) μ_{t_E}(a,b) ≤ ϑ₀² λ u_b^{2γ} for all pairs 0 ≤ u_a < u_b ≤ U_E with λ ≥ ε/2;
 (D2) ϑ₀ (U_E + D)^γ ≤ 1/20;  (D3) v ≤ 10⁻⁵ and v ≤ γ/7.
((D1) says: seen at scale λ at distance u_b from the end, the arc is aligned with the line of departure up to a tilt
ϑ₀u_b^γ. By Fact 0.2, (D1) contains N(a,b;t_E) ≤ ϑ₀λ^{1/2}u_b^γ and |e_{ab} − û| ≤ 1.01ϑ₀u_b^γ.)

> **Theorem P7.D.** Under (D1)–(D3), for every t = t_E + τ ∈ [t_E, t_E + D] and every pair with λ ≥ ε/2:
> (i) *exact laws:* x_E(t) = P(t) + σ(t)û with σ′ = 1 + vf(σ), σ(t_E) = 0; for every label s, y_s := û × (x_s − P)
>  satisfies y_s′ = v (f(ρ_s)/ρ_s) y_s, and z_s := (x_s − P)·û satisfies z_s′ ≥ 1 − v;
> (ii) μ_t(a,b)^{1/2} ≤ 1.01 ϑ₀ λ^{1/2} u_b^γ (1 + τ/max(λ,u_a))^{7v};
> (iii) λ ≤ l_t(a,b) ≤ 1.03λ and c(a,b;t) ≥ c(a,b;t_E) ≥ 0.998λ;
> (iv) *near pairs* (u_a < 64λ): N(a,b;t) ≤ 2.9 ϑ₀ λ^{1/2+γ} (1 + τ/λ)^{7v};
> (v) *far pairs* (u_a ≥ 64λ): N(a,b;t) ≤ (1 + τ/u_a)^{1.39v} [ N(a,b;t_E) + 0.2 vϑ₀λ^{1/2+γ} ].
> In particular, if also N(a,b;t_E) ≤ M₀λ^{1/2+γ} for all pairs (M₀ ≤ ϑ₀ without loss), then for all pairs and all
> τ ≤ D: N(a,b;t) ≤ 2.9ϑ₀ (λ + τ)^{7v} λ^{1/2+γ−7v}: **the exponent is lowered by at most 7v, the constant is worse by
> a bounded factor**, uniformly in ε.

*Proof.* **(i)** r_s′ = vF(r_s) + û. For E the ansatz r = σû solves this iff σ′ = vf(σ) + 1; uniqueness. Next
y_s′ = û × (vF(r_s) + û) = v(f(ρ_s)/ρ_s)(û × r_s), and z_s′ = v f(ρ_s)(z_s/ρ_s) + 1 ≥ 1 − v.

**Geometry at t_E.** By Fact 0.2(ii), (D1), (D2): for u_s ≥ ε/2, z_s(t_E) = (x_s − x_E)·û = u_s − μ_{t_E}(E,s)/2 ≥
u_s(1 − 1/800). For u_s < ε/2, with s′ the label u = ε/2: z_s ≥ z_{s′} − |x_{s′} − x_s| ≥ (ε/2)(1 − 1/800) − (ε/2 − u_s). So
z_s(t_E) ≥ u_s − ū_s/800 for all s, and by (i): z_s(t) ≥ u_s − ū_s/800 + (1−v)τ. Consequently (X := u_s + τ: if X ≤ ε use
ε ≥ (X+ε)/2; if X > ε, ρ_s ≥ z_s ≥ 0.998X ≥ 0.499(X+ε))
 max(ρ_s(t), ε) ≥ 0.49 (u_s + τ + ε), hence a*(ρ_s) ≤ 2/max(ρ_s,ε) ≤ 4.1/(u_s + ε + τ), (4.1)
 A_s(t) := exp(v∫_{t_E}^t a*(ρ_s)) ≤ ((u_s + ε + τ)/(u_s + ε))^{4.1v} ≤ (1 + τ/u_s)^{4.1v}. (4.2)
Also, by Fact 0.2(ii) applied to (E, s⁺), s⁺ the label max(u_s, ε/2): |y_s(t_E)| ≤ (ū_s · ϑ₀²ū_s^{1+2γ})^{1/2} = ϑ₀ū_s^{1+γ}; and by (i),
f(ρ)/ρ ≤ a*(ρ):
 |y_s(t)| ≤ ϑ₀ ū_s^{1+γ} A_s(t). (4.3)

**Pointwise bound.** Work in the label u (du = ds at t_E), w̃ := w/w(t_E) (so l_t(J) = ∫_J w̃ du) and
χ̃(u,t) := w̃^{1/2}|T − û| (so μ_t(J) = ∫_J χ̃² du). By Fact 0.3 (divide by w(t_E)^{1/2}), w̃ ≤ A_s, (4.1), (4.3), Lemma V(iii):
 χ̃(u,t) ≤ A_s(t)χ̃(u,t_E) + vA_s(t)∫_0^τ A_s^{−1/2} |y_s|/max(ρ_s,ε)² dτ′
  ≤ A_sχ̃(u,t_E) + vA_s^{3/2} ϑ₀ū_s^{1+γ} ∫_0^∞ 4.17 dτ′/(u_s+ε+τ′)² ≤ A_s(t)χ̃(u,t_E) + 4.17 vϑ₀ A_s(t)^{3/2} ū_s^γ. (4.4)

**Two integrals over J = (a,b), λ ≥ ε/2.** Let Z := 1 + τ/max(λ,u_a) and p ∈ [1, 3.3].
 (α) ∫_J A_s^p du ≤ 1.001 λ Z^{4.1pv}. Indeed A_s ≤ (1 + τ/u)^{4.1v}, decreasing in u; if u_a ≥ λ bound it by its value at
 u_a; otherwise ∫_{u_a}^{u_a+λ}(1 + τ/u)^η du ≤ ∫_0^λ((λ+τ)/u)^η du = λ^{1−η}(λ+τ)^η/(1−η), η = 4.1pv ≤ 1.4·10⁻⁴.
 (β) ∫_J A_s^p χ̃(u,t_E)² du ≤ 1.001 ϑ₀² λ u_b^{2γ} Z^{4.1pv}. If u_a ≥ λ: A_s^p ≤ (1 + τ/u_a)^{4.1pv} on J and (D1). If u_a < λ: let
 K ≥ 0 be the integer with 2^{−K}λ ∈ [ε/2, ε), J_K := (u_a, u_a + 2^{−K}λ], J_k := (u_a + 2^{−k−1}λ, u_a + 2^{−k}λ] for 0 ≤ k < K: all
 have label length ≥ ε/2 and right end ≤ u_b, so μ_{t_E}(J_k) ≤ ϑ₀²2^{−k−1}λu_b^{2γ} (k < K), μ_{t_E}(J_K) ≤ ϑ₀²2^{−K}λu_b^{2γ}. On J_k,
 u ≥ 2^{−k−1}λ, so A_s ≤ (1 + 2^{k+1}τ/λ)^{4.1v} ≤ (2^{k+1}(1+τ/λ))^{4.1v}; on J_K, by (4.2), A_s ≤ ((ε+τ)/ε)^{4.1v} ≤ (2^K(1+τ/λ))^{4.1v}.
 With η = 4.1pv and q := 1 − η: the sum is ≤ ϑ₀²λu_b^{2γ}(1+τ/λ)^η [Σ_{i=1}^K 2^{−iq} + 2^{−Kq}] and
 Σ_{i=1}^K 2^{−iq} + 2^{−Kq} ≤ 1/(2^q − 1) ≤ 1/(1 − 2η ln 2) ≤ 1.001 (the bracket equals 1/(2^q−1) − 2^{−Kq}(1/(2^q−1) − 1)).

**(ii).** By (4.4) and Minkowski in L²(J,du), then (β) with p = 2 and (α) with p = 3 (ū_s ≤ u_b on J):
μ_t(J)^{1/2} ≤ (1.001)^{1/2}ϑ₀λ^{1/2}u_b^γZ^{4.1v} + 4.17vϑ₀u_b^γ(1.001λ)^{1/2}Z^{6.15v} ≤ 1.01ϑ₀λ^{1/2}u_b^γZ^{7v}.

**(iii).** Chords are non-decreasing, and c(a,b;t_E) ≥ (x_b − x_a)·û = λ − μ_{t_E}(a,b)/2 ≥ λ(1 − 1/800). For the length:
w̃_t = v w̃ T·AT and T·AT ≤ 2(T−û)·A(T−û) + 2û·Aû ≤ 2a*|T−û|² + 2û·Aû, so w̃_t ≤ 2v a* χ̃² + 2v w̃ û·Aû.
First part: by (4.1), (4.4) and v log X ≤ X^v/e with X := (u_s+ε+τ)/(u_s+ε) (so v log X ≤ A_s^{1/4.1}/e):
∫_0^τ 2v a*χ̃² ≤ 8.2 v log X · [A_sχ̃(u,t_E) + 4.17vϑ₀A_s^{3/2}ū_s^γ]² ≤ 6.04A_s^{2.25}χ̃(u,t_E)² + 106v²ϑ₀²A_s^{3.25}ū_s^{2γ}; integrating
over J by (β) (p = 2.25), (α) (p = 3.25): ≤ (6.05 + 107v²)ϑ₀²λu_b^{2γ}Z^{14v}. Now u_b ≤ 2X₀, X₀ := max(λ,u_a), and 2γ ≥ 14v, so
u_b^{2γ}Z^{14v} ≤ 2^{2γ}X₀^{2γ−14v}(X₀+τ)^{14v} ≤ 1.42(U_E + D)^{2γ}; with (D2) the first part is ≤ 6.06·1.42λ/400 ≤ 0.0216λ.
Second part: where ρ_s ≥ ε, û·Aû = (û × ρ̂)²/ρ = y_s²/ρ_s³ ≤ 8.5ϑ₀²ū_s^{2+2γ}A_s²/(u_s+ε+τ′)³ by (4.1), (4.3), and
∫_0^τ 2v w̃ û·Aû ≤ 2vA_s³·8.5ϑ₀²ū_s^{2+2γ}/(2(u_s+ε)²) ≤ 8.5vϑ₀²A_s³u_b^{2γ}; where ρ_s < ε (only if τ′ < 1.05ε, by (4.1), and then
A_s ≤ 1.001) û·Aû ≤ 2/ε contributes ≤ 4.21v. Integrating over J: ≤ (8.6·1.42/400 + 4.21)vλ ≤ 4.3vλ.
So l_t(J) − λ ≤ 0.0216λ + 4.3vλ ≤ 0.03λ.

**(iv).** N² ≤ μ_t (Fact 0.2), u_b ≤ 65λ, 65^γ ≤ 2.84, max(λ,u_a) ≥ λ: N ≤ 1.01·2.84ϑ₀λ^{1/2+γ}(1+τ/λ)^{7v}.

**(v).** Let g := u_a ≥ 64λ ≥ 32ε. For s ∈ [a,b]: z_s(t′) ≥ u_s(1 − 1/800) + (1−v)τ′ ≥ 0.99(g + τ′); z is a linear functional
of norm 1, so dist(P, hull of the arc) = ρ_m ≥ 0.99(g + τ′) ≥ max(ε, 4l) (l ≤ 1.03λ, g ≥ 64λ ≥ 32ε). So [B, Lemma 3(e)]
applies on [t_E,t] with α ≤ 1.375v/ρ_m ≤ 1.39v/(g+τ′), β = 2v l^{3/2}|p_a|/ρ_m³. Decomposing r_a along û, û^⊥:
|p_a| = |r_a × e_{ab}| ≤ ρ_a|û × e_{ab}| + |y_a|. By Fact 0.2(i), (ii), (iii): |û × e_{ab}| ≤ |e_{ab} − û| ≤ (μ_{t′}/c)^{1/2} ≤
1.012ϑ₀u_b^γ(1+τ′/g)^{7v} ≤ 1.02ϑ₀g^γ(1+τ′/g)^{7v}; ρ_a(t′) ≤ ρ_a(t_E) + (1+v)τ′ ≤ 1.001(g+τ′); |y_a| ≤ ϑ₀g^{1+γ}(1+τ′/g)^{4.1v} by
(4.3), (4.2). So |p_a| ≤ 2.03ϑ₀g^γ(g+τ′)(1+τ′/g)^{7v} and
β ≤ 2(1.03)^{3/2}·2.03/0.99³ · vϑ₀λ^{3/2}g^{γ−7v}(g+τ′)^{7v−2} ≤ 4.4vϑ₀λ^{3/2}g^{γ−7v}(g+τ′)^{7v−2}. Lemma 3(e):
N(t) ≤ ((g+τ)/g)^{1.39v}N(t_E) + 4.4vϑ₀λ^{3/2}g^{γ−7v}(g+τ)^{1.39v}∫_0^∞(g+τ′)^{5.61v−2}dτ′ ≤ (1+τ/g)^{1.39v}[N(t_E) + 4.41vϑ₀λ^{3/2}g^{γ−1}],
and g^{γ−1} ≤ 64^{−3/4}λ^{γ−1}. The final sentence of the theorem follows from (iv), (v) and
(1+τ/λ)^{7v} = (λ+τ)^{7v}λ^{−7v}, (1+τ/u_a)^{1.39v} ≤ (1+τ/λ)^{7v}, M₀ + 0.2vϑ₀ ≤ 2.9ϑ₀. ∎

> **Proposition P7.D′ (the loss of exponent is real).** In the setting of Theorem P7.D, for every label s with
> u_s ≥ 1.01ε and every τ ∈ [0,D], the angle ∠_s(t) between û and the chord from x_E to x_s satisfies
>  sin ∠_s(t_E+τ) ≥ 0.96 · sin ∠_s(t_E) · (1 + (1+v)τ/u_s)^{v/(1+v)}.
> Hence if the chord tilts at t_E satisfy sin∠_s ≥ k u_s^γ (e.g. an arc of curvature ≈ 2k: γ = 1), then at time t_E + τ
> they are ≥ 0.96 k τ^{v/(1+v)} u_s^{γ − v/(1+v)}: **the tilt exponent at the end drops by v/(1+v); "same exponent, bounded
> factor" is false.** (It becomes γ − v/(1+v); for γ = 1 this is N7's a′ = 1/(1+v).)

*Proof.* x_E stays on the axis (Theorem P7.D(i)), so û × (x_s − x_E) = y_s and sin∠_s = |y_s|/c(E,s). ρ_s ≥ 0.998u_s ≥ ε on
[t_E,t] (proof above), so y_s′ = (v/ρ_s)y_s; and ρ_s(t′) ≤ ρ_s(t_E) + (1+v)τ′ ≤ u_s + (1+v)τ′ (|r_s′| ≤ 1+v). Hence
|y_s(t)| ≥ |y_s(t_E)| exp(v∫_0^τ dτ′/(u_s + (1+v)τ′)) = |y_s(t_E)|(1 + (1+v)τ/u_s)^{v/(1+v)}. Finally
c(E,s;t) ≤ l_t(E,s) ≤ 1.03u_s and c(E,s;t_E) ≥ 0.998u_s (Theorem P7.D(iii)). ∎

> **Lemma P7.H (hand-over: the invariants of Theorem P7.B imply (D1)).** Let (J1), (J2) of Theorem P7.B hold (constants
> γ₁, R₁, M₁ = (γ₁/50)R₁^{−γ₁}, first-pass labels u⁽¹⁾ ∈ [0,U⁽¹⁾]), let t_E := t_j be a leg start with j > j_s, E := a_j,
> û := the direction of leg j, and assume U⁽¹⁾ − u⁽¹⁾_E ≥ R₁. Let u := l_{t_E}(E,·) be the arclength at t_E on the arc ahead
> of E, and U_E ≤ R₁/2. Then (D1) holds on [0,U_E] with γ = γ₁ and ϑ₀ := 48M₁/γ₁ = 0.96R₁^{−γ₁}, and moreover
> N(a,b;t_E) ≤ M₁λ^{1/2+γ₁} for all pairs in [0,U_E] with λ ≥ ε/2. (D2) then reads U_E + D ≤ R₁·20^{−1/γ₁}.

*Proof.* Let (a,b) be a pair in [0,U_E] with λ = l_{t_E}(a,b) ≥ ε/2, and λ⁽¹⁾ ≤ λ its first-pass label length. If
λ⁽¹⁾ ≥ ε/2 put (a⁺,b⁺) := (a,b); otherwise enlarge it (to the right; there is room) to first-pass length ε/2 ≤ λ.
Then (a⁺,b⁺), I := (a_{j−1},b⁺) and (a_{j−1},a_j) belong to 𝔉(t_j) as pairs of leg j (first points ≥ a_j, resp. = the base
a_{j−1}; λ⁽¹⁾(a_{j−1},a_j) ∈ [ε/2,ε] by Theorem P7.B(b); λ⁽¹⁾_I ≤ u_b + ε/2 + ε ≤ R₁). By Lemma C(2),
x_{a_j} − x_{a_{j−1}} = σû with σ > 0 at t_j, i.e. e_{(a_{j−1},a_j)} = û. By (TL) twice, |e_{a⁺b⁺} − û| ≤ 2C_TLM₁(λ⁽¹⁾_I)^{γ₁}, and
λ⁽¹⁾_I ≤ u_b + 1.5ε ≤ 4u_b (u_b ≥ λ ≥ ε/2). By Fact 0.1 and (J2), N(a,b)² ≤ N(a⁺,b⁺)² ≤ M₁²max(λ⁽¹⁾,ε/2)^{1+2γ₁} ≤ M₁²λ^{1+2γ₁}.
If the pair was enlarged, [B, Lemma 4(a)] with c(a,b) = λ − E(a,b) ≥ λ − ½M₁²(ε/2)^{1+2γ₁} ≥ 0.99λ gives
|e_{ab} − e_{a⁺b⁺}| ≤ [λ^{1/2}M₁(ε/2)^{1/2+γ₁} + ½M₁²(ε/2)^{1+2γ₁}]/(0.99λ) ≤ 1.1M₁u_b^{γ₁}. So
|e_{ab} − û| ≤ (2·4^{γ₁}C_TL + 1.1)M₁u_b^{γ₁} ≤ 2.86C_TLM₁u_b^{γ₁}, and by Fact 0.2(i) (c ≤ λ)
μ_{t_E}(a,b) ≤ M₁²λ^{1+2γ₁} + λ(2.86C_TLM₁)²u_b^{2γ₁} ≤ (2.87C_TLM₁)²λu_b^{2γ₁}, 2.87·16.5 ≤ 48. ∎

---------------------------------------------------------------------------------------------------------------------

## §5. Corollary P7.T — two-pass transport (first pass → departure → far phase → data for the restart)

> **Corollary P7.T.** Let a first pass satisfy the conclusions of Theorem P7.B with (γ₁, R₁, M₁); let t_E = t_j (j > j_s),
> E = a_j, û as in Lemma P7.H, U⁽¹⁾ − u⁽¹⁾_E ≥ R₁. Suppose that, instead of continuing, Harry
>  (1) walks straight back, P(t) = P(t_E) − (t − t_E)û, for t ∈ [t_E, t_E + D]; and
>  (2) on [t_E + D, t₁] follows any 1-Lipschitz path with dist(P(t), conv Γ(t)) ≥ ρ₀ ≥ ε, where Γ is the arc ahead of E of
>   t_E-arclength U_Γ ≥ ε.
> Assume D ≤ 1/2, U_Γ + D ≤ R₁·20^{−1/γ₁}, U_Γ ≤ ρ₀/5, v ≤ min(10⁻⁵, γ₁/7) and vT ≤ ρ₀/200, T := t₁ − t_E − D. Then at
> time t₁, with λ₁ := l_{t₁}(a,b), for every pair (a,b) ⊂ Γ with λ₁ ≥ ε/2:
>  N(a,b;t₁) ≤ 2.9 R₁^{−γ₁} λ₁^{1/2+γ₁−7v} + 2.8 (vT/ρ₀²) λ₁^{3/2},  0.95λ₁ ≤ c(a,b;t₁) ≤ λ₁.
> So on Γ the data at t₁ satisfy (E1) of (ST_end) with a′ = γ₁ − 7v, C₀ = 2.9R₁^{−γ₁} + 2.8vT/ρ₀², for scales up to U_Γ, and
> Corollary P7.E can be applied to a second pass that approaches E from the other side, **provided (E1), (E2) are also
> verified on the rest of its arc A and for pairs not contained in Γ** (design-dependent).

*Proof.* Lemma P7.H gives (D1) on [0,U_Γ] with ϑ₀ = 0.96R₁^{−γ₁}, and (D2) holds. Let (a,b) ⊂ Γ with t_E-arclength
λ_E ≥ ε/2. Theorem P7.D (final sentence, M₀ = M₁ ≤ ϑ₀, τ = D ≤ 1/2, λ_E ≤ 1/2): N(t_E + D) ≤ 2.9ϑ₀λ_E^{1/2+γ₁−7v}, and
l_{t_E+D} ≤ 1.03λ_E, c ≥ 0.998λ_E. For phase (2) apply Lemma P7.A with constant ρ₀: l_{t_E+D}(Γ)e^{vT/ρ₀} ≤ 1.03·1.006U_Γ ≤ ρ₀/4.
So l_{t₁} ≤ 1.036λ_E and N(t₁) ≤ e^{1.375/200}[2.9ϑ₀λ_E^{1/2+γ₁−7v} + 2.5vT l_{t₁}^{3/2}/ρ₀²]. Since λ_E ≤ λ₁ = l_{t₁} and
2.9·0.96·1.007 ≤ 2.9, 2.5·1.007 ≤ 2.6, the bound follows (with 2.6); c(t₁) ≥ 0.998λ_E ≥ 0.998λ₁/1.036. If λ₁ ≥ ε/2 but
λ_E < ε/2, enlarge the pair inside Γ to a pair (a⁺,b⁺) of t_E-arclength ε/2 ≤ λ₁ and use Fact 0.1:
N(a,b;t₁) ≤ N(a⁺,b⁺;t₁), where l_{t₁}(a⁺,b⁺) ≤ 1.036·ε/2 ≤ 1.036λ₁ (this turns 2.6 into 2.6·1.036^{3/2} ≤ 2.8); and
c(a,b;t₁) = λ₁ − E(a,b;t₁) ≥ λ₁ − E(a⁺,b⁺;t₁) ≥ λ₁ − (1.036 − 0.998)ε/2 ≥ 0.96λ₁. ∎

---------------------------------------------------------------------------------------------------------------------

## §6. Proposition P7.C — transversal departure: the exact profile is a hook, not a rigid rotation

**Setting (model).** ê ⊥ n̂ unit vectors. At time 0 Harry is at the origin and the front contains the straight segment
{rê : ε ≤ r ≤ r₀}. Harry moves along P(τ) = τn̂, τ ≥ 0. (Each of these candidates has ρ ≥ r ≥ ε for all τ ≥ 0, see the
proof; so true and virtual candidates coincide and ε plays no further role.)

> **Proposition P7.C.** For θ ∈ (0, π/2] let t := tan(θ/2), J(θ) := (1 − t^{1−v})/(1−v) and
>  G(θ) := [cot θ · t^{−v} + vJ(θ)]/(1+v)  (strictly decreasing from +∞ to 0).
> For the candidate starting at rê let θ = θ(τ/r) be the solution of G(θ) = τ/r. Then at time τ:
> (i) its position is X(r,τ) = r t^{−v} ê + v(rJ(θ) − τ) n̂; the angle at Harry between −n̂ and the candidate is θ, and
>  ρ = r/(sin θ · t^v);
> (ii) the tangent of the front is ∂_rX = D₁ê + D₂n̂ with
>  D₁ = [t^{−v}(1 + v − v cos θ) − v²J sin θ]/(1+v),  D₂ = v[J(1 + v cos θ) − t^{1−v}cos θ]/(1+v);
> (iii) the tilt Θ := angle from ê to ∂_rX satisfies, with μ = v/(1−v),
>  μ t^v (1 − 2t^{1−v})/(1+v) ≤ tan Θ ≤ μ(1+v) t^v/(1 − vμ),  where (1+v)τ/r = (1 − t²)t^{−1−v}/2 + vJ(θ).
>  Hence, as r/τ → 0: t = (2(1+v)τ/r)^{−1/(1+v)}(1 + o(1)) and Θ = c_v (r/τ)^{v/(1+v)}(1 + o(1)),
>  c_v = μ(1+v)^{1/(1+v)} 2^{−v/(1+v)}.
> So the tangent near the end is **not** rotated rigidly by ≈ v: the rotation at distance r is ≈ c_v(r/τ)^{v/(1+v)}, it
> tends to 0 at the end, with the slow exponent v/(1+v) in r (exponent v in the arclength of the image, which is
> ∝ r^{1/(1+v)}). A transversally left end is a hook of amplitude ≈ v and tilt exponent a′ = v < v/(1−v).

*Proof.* Write r⃗ = x − P = ρ(sin θ ê − cos θ n̂); r⃗′ = vρ̂ − n̂. Then ρ′ = v + cos θ and ρθ′ = −n̂·(cos θ ê + sin θ n̂) = −sin θ.
Initially θ = π/2, ρ = r; θ decreases and stays in (0,π/2], so ρ′ ≥ v > 0 and ρ ≥ r ≥ ε. Since d ln t/dθ = 1/sin θ,
d/dτ ln(ρ sin θ t^v) = (v + cos θ)/ρ − cos θ/ρ − v/ρ = 0: ρ sin θ t^v = r. Then dθ/dτ = −sin²θ t^v/r, so τ/r = ∫_θ^{π/2}dϑ/(sin²ϑ
tan^v(ϑ/2)). This integral equals G(θ): G(π/2) = 0 (t = 1, J = 0) and, using dt/dθ = (1+t²)/2 = 1/(1+cos θ) = t/sin θ, hence
J′ = −t^{−v}/(1+cos θ) = −t^{−v}(1 − cos θ)/sin²θ and (t^{−v})′ = −v t^{−v}/sin θ,
(1+v)G′ = −t^{−v}/sin²θ − v cos θ t^{−v}/sin²θ − v t^{−v}(1 − cos θ)/sin²θ = −(1+v)t^{−v}/sin²θ.
(i) X = τn̂ + ρ(sin θ ê − cos θ n̂) = r t^{−v}ê + (τ − r cot θ t^{−v})n̂ and τ − r cot θ t^{−v} = r(G − cot θ t^{−v}) = vr(J − G) = v(rJ − τ).
(ii) At fixed τ, differentiating G(θ) = τ/r: ∂_rθ = −(τ/r²)/G′(θ) = (τ/r²) sin²θ t^v. So ∂_r(r t^{−v}) = t^{−v} − v(τ/r) sin θ and
∂_r(v r J) = vJ + v r J′∂_rθ = vJ − v(τ/r)(1 − cos θ). Insert τ/r = G, sin θ cot θ = cos θ and (1 − cos θ)cot θ = t cos θ.
(iii) 0 ≤ J ≤ 1/(1−v). Upper bound: D₂ ≤ vJ(1 + v cos θ)/(1+v) ≤ μ, D₁ ≥ [t^{−v} − vμ]/(1+v) ≥ t^{−v}(1 − vμ)/(1+v). Lower bound:
D₂ ≥ v(J − t^{1−v})/(1+v) ≥ μ(1 − 2t^{1−v})/(1+v) (J − t^{1−v} = (1 − (2−v)t^{1−v})/(1−v)), D₁ ≤ t^{−v}. The relation for τ/r is
(1+v)G with cot θ = (1−t²)/(2t). As r/τ → 0: t → 0, (1+v)τ/r ∼ t^{−1−v}/2, tan Θ ∼ μ(1+v)t^v. ∎

*Remark.* To first order in v the formula gives the "rigid rotation by v" of L-7 (F2): (r/τ)^{v/(1+v)} = 1 − O(v log(τ/r)).
The differential rotation per e-fold of scale is ≈ v²(r/τ)^{v/(1+v)}: second order in v, but not summable over scales
with room: Corollary P7.E needs a′ ≥ γ + 22v with v ≤ 2·10⁻¹¹γ², which a′ = v cannot satisfy.
