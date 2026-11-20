# P8b — claims for independent referees: assembly of the main theorem for design T

Stream P8b, round 8. Version 1. **Only statements claimed PROVED, with proofs.** Numerical tests (not part of any
proof): `code/P8b/`, summarised in `reports/P8b-1.md`.

## Hypotheses taken from other streams (NOT proved here)

* **[B]** = `paper/sec_B.tex` (doubly refereed): Lemma V, Lemma VC, Lemmas 1–4, Lemma C. Notation of [B] throughout
  (F, A = DF, a*(ρ), r = x − P, ρ = |r|, l, c, e, E = l − c, N = (2E)^{1/2}, a×b = Im(āb), a^⊥ = ia).
* **[P7]** = `referee/P7-claims.md` v1 with the text fixes F1–F13 of `reports/referee-RP7-2.md`: Facts 0.1–0.3,
  **Theorem P7.B** (incl. its Steps 1–2: (CA), the leg dichotomy, the tilt lemma (TL)) and **Corollary P7.E**; the
  causality statement F3 (the invariants at time t depend only on P|[0,t]); the family convention F1 (at a switching
  time t_j the family is that of leg j: pairs with a = a_{j−1} or a ≥ a_j). Lemma P7.A is re-proved below in pairwise
  form (Lemma P8.A). **Not used:** Theorem P7.D, Lemma P7.H, Corollary P7.T, the restart Remark of §2, [B] Theorem B/R.
* **(H_T)** = the touch-down data of design T, stated precisely in §5. To be proved by stream P8a from the exact
  formulas. P8a's interim statement (`reports/P8a-1.md` §0, S0–S7; not yet a refereed claims file) contains (T3)–(T5)
  and (T1), (T2) on each of the two arcs A₁, A₂ separately; **two items of (H_T) are not in it**: (X1) (T2) for pairs
  with one point in A₁ and one in A₂, (X2) (T1) for pairs meeting the ghost hole (the TRUE front through the seen
  labels |α| < α_s). The dictionary and what (X1), (X2) need is in `reports/P8b-1.md` §2. (H_T) was checked
  numerically (`code/P8b/ht.py`).

Everything below is PROVED modulo exactly these three inputs. In particular **Theorem P8.M (§6) is the main theorem
conditional on (H_T)**; it is not claimed unconditionally.

Contents. §1 Lemma P8.W (working fronts; the ghost hole). §2 Lemma P8.A (pairwise passive lemma). §3 Theorem P8.D
(departure from near an end along a curved path, pointwise data). §4 Lemma P8.H (heading of the legs of C).
§5 Hypothesis (H_T), constants. §6 Proposition P8.I (hand-over: (ST_end) at the end of the departure) and
Theorem P8.M (main theorem modulo (H_T)), Corollary P8.X (exact capture via lem:A41).

---------------------------------------------------------------------------------------------------------------------

## §1. Working fronts

**Definition.** Let P be a 1-Lipschitz path on [0,∞), t_w ≥ 0, U > 0 and x⁰: [0,U] → ℝ² a C¹ curve with |∂_u x⁰| ≡ 1.
The *working front* started from x⁰ at t_w is the family x(u,t), t ≥ t_w, of solutions of
 ∂_t x(u,t) = v F(x(u,t) − P(t)),  x(u,t_w) = x⁰(u)  (F the C¹ field of [B]).
A label u is *true, with direction θ*, if the true candidate S_θ is defined on [0,t_w] (not caught before t_w) and
x⁰(u) = S_θ(t_w). Other labels are *ghost* labels. l, c, e, E, N, T, w := |∂_u x|, ρ_u := |x(u,t) − P(t)| as in [B].

> **Lemma P8.W.** For a working front and t ≥ t_w:
> (a) [B, Lemma VC(a),(b)] hold with θ replaced by u (existence, uniqueness, |∂_t x| ≤ v, x(·,t) ∈ C¹,
>  ∂_t∂_u x = vA(r)∂_u x, w non-decreasing in t and ≥ 1, chords non-decreasing), and so do [B, Lemma 1(i),(ii), Lemma 2,
>  Lemma 3, Lemma 4] and [P7, Facts 0.1–0.3].
> (b) If u is true with direction θ and ρ_u(t) ≤ ε for some t ≥ t_w, the true candidate θ is seen by time t.
> (c) Construction C from a leg start (t_s,a_s), t_s ≥ t_w, cut at b_E (as in [P7, §1], on the working front):
>  [B, Lemma C(0),(2),(4)] hold verbatim, and (3′): for every true label u ∈ [a_j,a_{j+1}] its direction is seen by t_j.
> (d) Theorem P7.B and Corollary P7.E hold for Construction C on a working front, with "every label of [a_s,b_E] has
>  been seen" replaced by "the direction of every true label of [a_s,b_E] has been seen".

*Proof.* (a) The proofs of [B, Lemma VC(a),(b)] use only: the ODE x′ = vF(x − P(t)) with F ∈ C¹, ‖DF‖ ≤ 2/ε (global
existence, uniqueness, C¹ dependence on the initial point, variational equation), A symmetric ≥ 0 (monotonicity of
|∂x|), [B, Lemma V(iv)] (chords), and |∂_θ e^{iθ}| = 1, which is here |∂_u x⁰| = 1. The proofs of [B, Lemmas 1(i),(ii),
2, 3, 4] and of [P7, Facts 0.1–0.3] use only the variational equation, Lemma V and Lemma VC(a),(b) at times where
the front is defined. (b) Let t* := inf{s ∈ [t_w,t]: ρ_u(s) ≤ ε}. If S_θ was within ε of Harry at some time ≤ t_w
there is nothing to prove. Otherwise ρ_u(t_w) = |S_θ(t_w) − P(t_w)| > ε, so t* > t_w, and on [t_w,t*] the point
x(u,·) has ρ ≥ ε, where F is the unit radial field: it solves the true equation, and by uniqueness
x(u,s) = S_θ(s) on [t_w,t*]; at t* its distance to Harry is ε. (c) The proofs of [B, Lemma C(0),(2),(4)] use the ODE,
Lemma 1(i), Lemma V(ii), Lemma 2(i) and |∂x| = 1 at the initial time (here t_w; for (0): on [t_w,T],
|∂_u x| ≤ e^{2v(T−t_w)/ε}). (3′): ρ_u(t_j) = c(a_j,u;t_j) ≤ l_{t_j}(a_j,u) ≤ ε, then (b). (d) The proofs in [P7, §§1–2]
cite [B] only through Lemma V, VC(a),(b), Lemmas 1–4, Lemma C(0),(2),(3),(4) and the Claim in the proof of
Theorem R (which uses (F_b), (S), Lemma C(2),(4), Lemma 3(d), Lemma 4(b)); "seen" enters only through Lemma C(3),
here (3′). Labels u = arclength at t_s ≥ t_w are used there exactly as here. ∎

*Use.* In design T the labels of the hole |α| < α_s around the axis are seen during the straight run; their virtual
candidates of [B] carry a dent (N8: a′ ≈ v only). They are replaced by ghost labels carrying the exact smooth
two-integral front; nothing has to be seen there, and Construction C runs through the hole on the working front.

---------------------------------------------------------------------------------------------------------------------

## §2. Pairwise passive lemma

> **Lemma P8.A.** Working front, pair of labels a < b, times t_w ≤ t′ ≤ t″, T := t″ − t′, and ρ₀ ≥ ε a constant such that
> dist(P(t), conv{x(s,t): a ≤ s ≤ b}) ≥ ρ₀ for t ∈ [t′,t″] and 4 l_{t′}(a,b) e^{vT/ρ₀} ≤ ρ₀. Then for t ∈ [t′,t″]:
>  l_t(a,b) ≤ e^{v(t−t′)/ρ₀} l_{t′}(a,b),  N(a,b;t) ≤ e^{1.375v(t−t′)/ρ₀} [ N(a,b;t′) + 2.5 v (t−t′) l_t(a,b)^{3/2}/ρ₀² ].

*Proof.* On the arc ρ ≥ ρ₀ ≥ ε, so T·AT = sin²φ/ρ ≤ 1/ρ₀ and l′ = v∫T·AT ≤ (v/ρ₀)l ([B, Lemma 2(i)]): the first
claim; hence ρ_m ≥ ρ₀ ≥ max(ε, 4l_t(a,b)) on [t′,t″] and [B, Lemma 3(e)] applies with α ≤ 1.375v/ρ₀ and
β = 2v l^{3/2}|p_a|/ρ_m³. As x_a lies in the hull, whose diameter is ≤ l, |p_a| ≤ ρ_a ≤ ρ_m + l ≤ 1.25ρ_m, so
β ≤ 2.5 v l_t^{3/2}/ρ₀² (l is non-decreasing). ∎

(This is [P7, Lemma P7.A] with the hull of the *pair* in place of the hull of an arc Γ; the proof is the same. It has
no restriction on the position of the pair in a longer arc, so there are no "straddling" pairs.)

---------------------------------------------------------------------------------------------------------------------

## §3. Theorem P8.D — departure from near an end, along a curved path, pointwise data

**Setting.** Working front; t_E ≥ t_w; E a label; û a unit vector; D > 0; τ := t − t_E ∈ [0,D]. An arc of the front
starting at E is labelled by its arclength u ∈ [0,U_E] at time t_E measured from x_E (u = 0 at E); T denotes the unit
tangent in the direction of increasing u, w̃ := |∂_u x| (= 1 at t_E), ū := max(u, ε/2), λ := u_b − u_a.
For a label s: r_s = x_s − P, z_s := r_s·û, y_s := û × r_s (so r_s = z_s û + y_s û^⊥).

**Hypotheses**, with γ ∈ (0,1/4], ϑ₀ > 0, ϑ_h ≥ 0:
 (D0) x_E(t_E) − P(t_E) = z₀û + y₀û^⊥ with z₀ ≥ 0 and |y₀| ≤ ϑ₀ (z₀ + ε)(ε/2)^γ;
 (D1p) |T(u,t_E) − û| ≤ ϑ₀ ū^γ for all u ∈ [0,U_E];
 (DP) for a.e. τ ∈ [0,D]: |P′| = 1, P′·û < 0 and |û × P′| ≤ ϑ_h (τ + ε)^γ;
 (D2) ϑ₀ a_*^γ ≤ 1/20 and ϑ_h a_*^γ ≤ 1/20, where a_* := U_E + z₀ + ε + D;
 (D3) v ≤ 10⁻⁵ γ.
Put a_s(τ) := u_s + z₀ + ε + τ, η := 4.1v, Θ := 1.0001ϑ₀ + (4.2v/γ)ϑ_h, Θ_p := 4.1ϑ₀ + 1.6ϑ_h.

(Harry starts at distance z₀ "behind" the end E on the line of the arc, up to the offset y₀, and walks away from the
arc along a path whose heading deviates from −û by at most ϑ_h(τ+ε)^γ. For z₀ = y₀ = 0, ϑ_h = 0 this is the setting
of [P7, Theorem P7.D] with pointwise instead of L² data.)

> **Theorem P8.D.** Under (D0)–(D3), for every τ ∈ [0,D] and every label s of the arc:
> (i) z_s ≥ 0.998 (u_s + z₀ + τ) and max(ρ_s, ε) ≥ 0.49 a_s(τ);
> (ii) |y_s| ≤ a_s(τ) [ 2ϑ₀ ū_s^γ + ϑ_h (τ+ε)^γ ];
> (iii) |T(u_s,t) − û| ≤ (a_s(τ)/a_s(0))^η · 1.0001 ϑ₀ ū_s^γ + (4.2v/γ) ϑ_h a_s(τ)^γ ≤ Θ a_s(τ)^γ ≤ 0.0501;
> (iv) 1 ≤ w̃(u_s,t) ≤ e^{1.26v/γ} ≤ 1.00002; hence λ ≤ l_t(a,b) ≤ 1.00002 λ for all pairs;
> (v) for every pair 0 ≤ u_a < u_b ≤ U_E with λ ≥ ε/2: c(a,b;t) ≥ 0.998 l_t(a,b), and
>   N(a,b;t) ≤ (1 + τ/(5λ))^{1.39v} [ N_* + 0.9 v Θ_p λ^{1/2+γ} ],
>  where N_* := N(a,b;t_E) if u_a + z₀ ≥ 5λ, and N_* := 1.9 Θ λ^{1/2+γ} otherwise.
> No constant depends on ε.

*Proof.* All labels below are in the arc. By (D2), ū_s ≤ a_* and τ + ε ≤ a_*, so ϑ₀ū_s^γ ≤ 1/20, ϑ_h(τ+ε)^γ ≤ 1/20.

**(i)** r_s′ = vF(r_s) − P′ and F(r)·û = f(ρ) z/ρ, so z_s′ = v f(ρ_s) z_s/ρ_s − P′·û ≥ −v − P′·û. By (DP),
−P′·û = (1 − (û×P′)²)^{1/2} ≥ (1 − 1/400)^{1/2} ≥ 0.9987, so z_s′ ≥ 0.998 a.e. At t_E:
z_s = z₀ + (x_s − x_E)·û = z₀ + ∫₀^{u_s} T·û du and T·û = 1 − |T − û|²/2 ≥ 1 − 1/800 by (D1p). Hence
z_s(t) ≥ 0.998 X, X := u_s + z₀ + τ. If X ≤ ε: max(ρ_s,ε) ≥ ε ≥ (X + ε)/2. If X > ε: ρ_s ≥ z_s ≥ 0.998X ≥ 0.499(X+ε).
Consequently a*(ρ_s) ≤ 2/max(ρ_s,ε) ≤ 4.1/a_s(τ), and for 0 ≤ τ′ ≤ τ
 𝒜(τ,τ′) := exp( v∫_{τ′}^{τ} a*(ρ_s) ) ≤ (a_s(τ)/a_s(τ′))^η. (3.1)

**(ii)** y_s′ = û × (vF(r_s) − P′) = v (f(ρ_s)/ρ_s) y_s − û × P′, and f/ρ ≤ a*; so (|y_s| is Lipschitz)
|y_s|′ ≤ v a*|y_s| + |û × P′| a.e., and by (DP), (3.1), writing a = a_s:
 |y_s(τ)| ≤ (a(τ)/a(0))^η |y_s(0)| + ϑ_h ∫₀^τ (a(τ)/a(τ′))^η (τ′+ε)^γ dτ′. (3.2)
At t_E: y_s = û × (x_s − x_E) + y₀ and |û × (x_s − x_E)| ≤ ∫₀^{u_s}|û × T| du ≤ u_s ϑ₀ ū_s^γ (for u < ε/2 the integrand
is ≤ ϑ₀(ε/2)^γ = ϑ₀ū_s^γ; in general it is ≤ ϑ₀ū^γ ≤ ϑ₀ū_s^γ for u ≤ u_s). With (D0):
|y_s(0)|/a(0) ≤ ϑ₀ū_s^γ u_s/(u_s + z₀ + ε) + ϑ₀(ε/2)^γ (z₀+ε)/(u_s+z₀+ε) ≤ 2ϑ₀ū_s^γ. (3.3)
In the integral a(τ′) ≥ τ′ + ε, so it is ≤ a(τ)^η ∫₀^τ (τ′+ε)^{γ−η}dτ′ ≤ a(τ)^η (τ+ε)^{1+γ−η} (as 1 + γ − η ≥ 1). So
 |y_s(τ′)| ≤ (a(τ′)/a(0))^η |y_s(0)| + ϑ_h a(τ′)^η (τ′+ε)^{1+γ−η}  (0 ≤ τ′ ≤ τ). (3.4)
Dividing (3.4) at τ′ = τ by a(τ): the first term is ≤ (a(τ)/a(0))^{η−1} · 2ϑ₀ū_s^γ ≤ 2ϑ₀ū_s^γ (η < 1), the second is
ϑ_h (τ+ε)^γ ((τ+ε)/a(τ))^{1−η} ≤ ϑ_h(τ+ε)^γ. This is (ii).

**(iii)** Let D₁ := 1 − T·û = ½|T − û|². By [B, Lemma 1(ii)] (valid by Lemma P8.W), T_t = v(AT − (T·AT)T), so
 ∂_t D₁ = −v[û·AT − (T·AT)(T·û)] = v[(T − û)·AT − (T·AT)(1 − T·û)] ≤ v (T − û)·AT,
because T·AT ≥ 0 and 1 − T·û ≥ 0. As in the proof of [P7, Fact 0.3]:
(T − û)·AT ≤ a*|T − û|² + |T − û||q_û|, q_û := û^⊥·A(r)û, |q_û| ≤ |r × û|/max(ρ,ε)² = |y_s|/max(ρ_s,ε)². For
δ_κ := (2D₁ + κ²)^{1/2} this gives δ_κ δ_κ′ ≤ v a* δ_κ² + v δ_κ|q_û|, i.e. δ_κ′ ≤ v a*δ_κ + v|q_û|; variation of
constants and κ → 0 give, for δ := |T − û| at the label s, with (i) (1/0.49² ≤ 4.17) and (3.1):
 δ(τ) ≤ (a(τ)/a(0))^η δ(0) + 4.17 v ∫₀^τ (a(τ)/a(τ′))^η |y_s(τ′)| a(τ′)^{−2} dτ′.
Insert (3.4). First part: 4.17 v |y_s(0)| (a(τ)/a(0))^η ∫₀^τ a(τ′)^{−2}dτ′ ≤ 4.17 v (a(τ)/a(0))^η |y_s(0)|/a(0)
≤ 8.34 v ϑ₀ ū_s^γ (a(τ)/a(0))^η by (3.3). Second part:
4.17 v ϑ_h a(τ)^η ∫₀^τ (τ′+ε)^{1+γ−η} a(τ′)^{−2} dτ′ ≤ 4.17 v ϑ_h a(τ)^η ∫₀^τ (τ′+ε)^{γ−1−η} dτ′
≤ (4.17v/(γ−η)) ϑ_h a(τ)^η (τ+ε)^{γ−η} ≤ (4.2v/γ) ϑ_h a(τ)^γ
(γ − η ≥ 0.99995γ by (D3); τ + ε ≤ a(τ)). With δ(0) ≤ ϑ₀ū_s^γ and 8.34v ≤ 10⁻⁴:
 δ(τ) ≤ (a(τ)/a(0))^η · 1.0001 ϑ₀ ū_s^γ + (4.2v/γ) ϑ_h a(τ)^γ.
Finally a(0) ≥ ū_s and ū_s ≤ a(τ), so (a(τ)/a(0))^η ū_s^γ ≤ a(τ)^η ū_s^{γ−η} ≤ a(τ)^γ; and Θ a_*^γ ≤ (1.0001 + 4.2·10⁻⁵)/20.

**(iv)** w̃ ≥ 1 by Lemma P8.W(a). w̃_t = v w̃ T·AT and, A being ≥ 0, T·AT ≤ 2(T−û)·A(T−û) + 2û·Aû ≤ 2a*δ² + 2û·Aû. By
(i), (iii): ∫₀^τ 2v a* δ² ≤ 8.2 v Θ² ∫₀^τ a^{2γ−1} ≤ (4.1v/γ) Θ² a(τ)^{2γ} ≤ (4.1v/γ)(0.0501)² ≤ 0.0103 v/γ. Where
ρ_s ≥ ε: û·Aû = (û × r̂)²/ρ = y_s²/ρ_s³ ≤ 8.5 (y_s/a)²/a ≤ 8.5 (3/20)² (a/a_*)^{2γ}/a by (i), (ii), (D2) (ū_s ≤ a,
τ′+ε ≤ a), contributing ≤ 2v · 8.5 · (9/400)/(2γ) ≤ 0.192 v/γ. Where ρ_s < ε: then 0.49a ≤ ε, i.e. τ′ ≤ 1.05ε, and
û·Aû ≤ a* = 2/ε contributes ≤ 4.2v ≤ 1.05v/γ. So log w̃ ≤ 1.26 v/γ ≤ 1.26·10⁻⁵, and l_t(a,b) = ∫ w̃ du.

**(v)** Chord: c ≥ (x_b − x_a)·û = ∫ T·û ds ≥ (1 − 0.0501²/2) l_t ≥ 0.998 l_t. Let g̃ := u_a + z₀ and
τ₀ := 0 if g̃ ≥ 5λ, τ₀ := 5λ otherwise.
*Times τ ≤ τ₀ (only if g̃ < 5λ).* By [P7, Fact 0.2(i)] and (iii), (iv):
N² ≤ ∫_a^b|T − û|² ds ≤ 1.00002 λ Θ² (u_b + z₀ + ε + τ)^{2γ}, and u_b + z₀ + ε + τ ≤ 6λ + 2λ + 5λ = 13λ; so
N ≤ 1.00001 · 13^γ Θ λ^{1/2+γ} ≤ 1.9 Θ λ^{1/2+γ} (13^{1/4} = 1.8988).
*Times τ ≥ τ₀.* For τ′ ≥ τ₀: g̃ + τ′ ≥ 5λ ≥ 2.5ε. z is a linear functional of norm 1 and z_s ≥ 0.998(g̃ + τ′) on the arc of
the pair, so ρ_m := dist(P, hull) ≥ 0.998(g̃+τ′) ≥ max(ε, 4l_t) (4.99λ ≥ 4·1.00002λ). [B, Lemma 3(e)] applies on [τ₀,τ]
with α ≤ 1.375v/ρ_m ≤ 1.39v/(g̃+τ′) and β = 2v l^{3/2}|p_a|/ρ_m³, p_a = r_a × e_{ab} = z_a(û × e) + y_a(û^⊥ × e), so
|p_a| ≤ ρ_a|û × e_{ab}| + |y_a|. Here: |û × e_{ab}| = c^{−1}|∫ û × T ds| ≤ (l/c) sup δ ≤ 1.003 Θ (u_b+z₀+ε+τ′)^γ and
u_b + z₀ + ε + τ′ = g̃ + τ′ + λ + ε ≤ 1.6(g̃+τ′); ρ_a(τ′) ≤ ρ_a(0) + (1+v)τ′ ≤ u_a + z₀ + |y₀| + (1+v)τ′ and
|y₀| ≤ (z₀+ε)/20 ≤ 0.07(g̃+τ′), so ρ_a ≤ 1.08(g̃+τ′); by (ii), |y_a| ≤ 1.4(g̃+τ′)[2ϑ₀(g̃+τ′)^γ + ϑ_h(1.4(g̃+τ′))^γ]. Hence
 |p_a| ≤ (g̃+τ′)^{1+γ}[1.08·1.003·1.6^γ Θ + 2.8ϑ₀ + 1.4^{1+γ}ϑ_h] ≤ Θ_p (g̃+τ′)^{1+γ}
(1.2184Θ + 2.8ϑ₀ + 1.523ϑ_h ≤ 4.02ϑ₀ + 1.524ϑ_h), and β ≤ 2(1.00002)^{3/2} 0.998^{−3} vΘ_p λ^{3/2}(g̃+τ′)^{γ−2}
≤ 2.013 vΘ_p λ^{3/2}(g̃+τ′)^{γ−2}. Lemma 3(e):
 N(τ) ≤ ((g̃+τ)/(g̃+τ₀))^{1.39v} [ N(τ₀) + 2.013 vΘ_p λ^{3/2} (g̃+τ₀)^{1.39v} ∫_{τ₀}^∞ (g̃+τ′)^{γ−2−1.39v} dτ′ ]
  ≤ (1 + τ/(5λ))^{1.39v} [ N(τ₀) + 2.013 · (4/3) · 5^{−3/4} vΘ_p λ^{1/2+γ} ],
using (g̃+τ₀)^{γ−1}/(1−γ+1.39v) ≤ (4/3)(5λ)^{γ−1} ≤ (4/3)5^{−3/4}λ^{γ−1} and (g̃+τ)/(g̃+τ₀) ≤ 1 + τ/(5λ);
2.013·1.3334·0.29907 ≤ 0.81. N(τ₀) = N(t_E) if τ₀ = 0, and ≤ 1.9Θλ^{1/2+γ} otherwise. ∎

**Remarks.** (1) *Exponent loss.* (iii) is a loss of at most η = 4.1v in the pointwise tilt exponent, (v) of 1.39v in
the pair exponent (true value v/(1+v), [RP7-2 §1]). (2) *Curved departure.* The heading deviation ϑ_h(τ+ε)^γ
enters only through the uniformly small rigid-rotation term (4.2v/γ)ϑ_h a^γ: with a Hölder modulus the departure
is as good as a straight one. A heading deviation that does not decay as τ → 0 (ϑ_h(τ+ε)^γ replaced by a
constant ω) is NOT covered: then ∫(τ′+ε)^{−1−η}dτ′ diverges like log(1/ε) — this is the hook of N8 (F1).
(3) Pairs with u_a + z₀ < 5λ need no start bound on N: for them (D1p) alone gives the bound.

---------------------------------------------------------------------------------------------------------------------

## §4. Lemma P8.H — heading of the first legs of Construction C

**Setting.** Working front, Construction C from (t_s,a_s) cut at b_A; labels u ∈ [0,U_A] = arclength at t_s from
x_{a_s}; the hypotheses of Theorem P7.B hold on this arc with constants (γ₁, R, M = (γ₁/50)R^{−γ₁}), so that on
[t_s, t] (t before the construction stops; causality) (CA), (J1), (J2), Theorem P7.B(b) and the tilt lemma
 (TL) |e_J − e_I| ≤ 0.33 (λ_I/R)^{γ₁} for family pairs J ⊂ I
hold. û_{j+1} := the direction of leg j+1 (so P′ = û_{j+1} on (t_j,t_{j+1}) for a non-final leg).
Let n̂ be a unit vector, γ ∈ (0,γ₁], ϑ_f > 0, G_f > 0 with ϑ_f G_f^γ ≤ 1/20 and
 (F1p) |T(u,t_s) − n̂| ≤ ϑ_f ū^γ for all u ∈ [0,G_f].

> **Lemma P8.H.** Let j ≥ j_s, leg j+1 non-final, Λ := u_{a_j} + ε, and assume 2Λ ≤ min(G_f, R, U_A) and
> (2Λ/R)^γ ≤ 1/10. Then
>  |û_{j+1} − n̂| ≤ (0.331 R^{−γ} + 1.23 ϑ_f) Λ^γ,
> and for t ∈ [t_j,t_{j+1}], τ := t − t_s:  Λ ≤ 1.0002(τ + ε), hence |û_{j+1} − n̂| ≤ ϑ_h (τ+ε)^γ with
> **ϑ_h := 0.34 R^{−γ} + 1.24 ϑ_f**.

*Proof.* Let b be the label with u_b = u_{a_j} + Λ = 2u_{a_j} + ε (≤ U_A), I := (a_j,b), κ := (2Λ/R)^γ ≤ 1/10. Since
γ ≤ γ₁ and all label lengths below are ≤ 2Λ ≤ R, (TL) gives |e_J − e_I| ≤ 0.33(λ_I/R)^γ ≤ 0.33κ for the pairs used.
*Step 1 (time t_j).* J := (a_j,a_{j+1}) (label length in [ε/2,ε], Theorem P7.B(b)) and I (label length Λ ≥ ε) are
family pairs of leg j+1 with first point the base, J ⊂ I, and e_J(t_j) = û_{j+1}. (TL): |û_{j+1} − e_I(t_j)| ≤ 0.33(Λ/R)^γ.
*Step 2 (time t_s).* c e_I − l n̂ = ∫_I (T − n̂) ds, so |e_I − n̂| ≤ (l/c) sup_I|T − n̂| + (l − c)/c; by (F1p),
sup_I|T − n̂| ≤ ϑ_f u_b^γ ≤ 1/20, c ≥ ∫ T·n̂ ≥ l(1 − sup²/2), so l/c ≤ 1.0013 and (l−c)/c ≤ 0.026 sup. Hence
|e_I(t_s) − n̂| ≤ 1.03 ϑ_f u_b^γ ≤ 1.03 · 2^γ ϑ_f Λ^γ ≤ 1.225 ϑ_f Λ^γ.
*Step 3 (rotation of e_I on [t_s,t_j]).* c e_I′ = v[(F(r_b) − F(r_a)) − ((F(r_b) − F(r_a))·e_I)e_I] (a := a_j), so
|e_I′| ≤ (v/c_I)(|e_I × F(r_a)| + |e_I × F(r_b)|), and |e × F(r)| = f(ρ)|e × r̂| ≤ |e × r̂| (F(0) = 0). Let t be in
leg i+1, j_s ≤ i ≤ j−1; then P = x_{a_{i+1}} − ρ′û_{i+1} with ρ′ ≥ 0 and û_{i+1} = e_{(a_i,a_{i+1})}(t) ([B, Lemma C(2)]).
– i ≤ j−2. K₁ := (a_{i+1},a_j), K₂ := (a_{i+1},b), K₃ := (a_i,a_{i+1}), K₄ := (a_i,b) are family pairs at t (first
points a_i or ≥ a_{i+1}; label lengths ≥ ε/2 because every non-final leg advances by ≥ ε/2, and ≤ u_b ≤ 2Λ ≤ R), and
I ⊂ K₂ ⊂ K₄, K₁ ⊂ K₂, K₃ ⊂ K₄. By (TL): |e_I − e_{K₂}| ≤ 0.33κ, |e_I − e_{K₁}| ≤ 0.66κ, |e_I − û_{i+1}| =
|e_I − e_{K₃}| ≤ 0.99κ. Now r_a = c(K₁)e_{K₁} + ρ′û_{i+1} and r_b = c(K₂)e_{K₂} + ρ′û_{i+1}, with non-negative
coefficients; for unit vectors e·e′ = 1 − |e − e′|²/2 ≥ 0.995, so ρ_a ≥ r_a·e_I ≥ 0.995(c(K₁)+ρ′) and
|e_I × r_a| ≤ 0.99κ(c(K₁)+ρ′): |e_I × r̂_a| ≤ κ; likewise |e_I × r̂_b| ≤ κ.
– i = j−1. r_a = ρ′û_j, so |e_I × F(r_a)| ≤ |e_I × û_j| ≤ |e_I − e_{(a_{j−1},b)}| + |e_{(a_{j−1},a_j)} − e_{(a_{j−1},b)}| ≤ 0.66κ
((a_{j−1},a_j), (a_{j−1},b), I are family pairs of leg j; λ(a_{j−1},b) ≤ Λ + ε ≤ 2Λ). r_b = c_I e_I + ρ′û_j, so
|e_I × r_b| ≤ 0.66κρ′ and ρ_b ≥ 0.995(c_I + ρ′): |e_I × r̂_b| ≤ 0.67κ.
So |e_I′| ≤ 2vκ/c_I on [t_s,t_j], c_I ≥ Λ/2 by (CA), and t_j − t_s ≤ (2u_{a_j}/ε)·ε/(1−v) ≤ 2.01Λ (at most 2u_{a_j}/ε
legs, each ≤ ε/(1−v)): |e_I(t_j) − e_I(t_s)| ≤ 8.04 vκ ≤ 8.04·2^γ v (Λ/R)^γ ≤ 10⁻³(Λ/R)^γ (v ≤ 10⁻⁴).
Adding Steps 1–3: |û_{j+1} − n̂| ≤ (0.331R^{−γ} + 1.225ϑ_f)Λ^γ.
*Time.* A non-final leg i+1 lasts ≥ c(a_i,a_{i+1};t_i) (closing speed ≤ 1) and c = l − E ≥ λ − ½M²λ^{1+2γ₁} ≥
λ(1 − 10⁻⁴) for the label advance λ ∈ [ε/2,ε] ((J2), MR^{γ₁} ≤ 1/200); so t_j − t_s ≥ 0.9999 u_{a_j}, Λ ≤ 1.0002(τ+ε),
and 1.0002^γ(0.331R^{−γ} + 1.225ϑ_f) ≤ 0.34R^{−γ} + 1.24ϑ_f. ∎

---------------------------------------------------------------------------------------------------------------------

## §5. Hypothesis (H_T) — touch-down data of design T (INPUT from P8a), and the constants

Design T (N8 §2; P8a-1 §0): (T1) P(t) = (t,0) for 0 ≤ t ≤ t₁ := 1/(1−v) + D₁; (T2) P runs at unit speed straight at
the candidate α₀ := arccos(v + 1/t₁) until the touch-down time t₂, at the point X₀ := P(t₂). D₁ ∈ (0,1] is a fixed absolute
constant (P8a: D₁ = 1; numerics here: D₁ = 0.1). **Here t₂ denotes the time called t_s by P8a** (the time at which the
virtual candidate α₀ of [B] is at distance 0 from Harry; it precedes the true catch time by ≤ vε/(3(1−v)²)).

**(H_T).** There are absolute constants v_T, ε_T ∈ (0,1), T₂, U_max ≥ 1, a′ ∈ (0,1], C₀, C_z > 0, λ₀ ∈ (0,1/4],
c_sep ∈ (0,1], γ_T ∈ (0,1/4], ϑ_T > 0, G_T ∈ (0,1] such that for all v ∈ (0,v_T], ε ∈ (0,ε_T]: t₂ ≤ T₂, and there are a
unit vector n̂ and a C¹ curve x⁰: [0,U] → ℝ², |∂_u x⁰| ≡ 1, 1 ≤ U ≤ U_max, with (u′ := U − u; everything at time t₂;
T = tangent of x⁰ in the direction of increasing u; λ := u_b − u_a):
 (T0) x⁰(0) = P(t₂) (= X₀). There is a set 𝒢 ⊂ (0,U) of ghost labels such that every u ∉ 𝒢 is true (§1, t_w = t₂),
   and every direction θ ∈ [0,2π) is seen by Harry during [0,t₂] or is the direction of a true label.
 (T1) N(a,b) ≤ C₀ λ^{1/2+a′} for all pairs with ε/2 ≤ λ ≤ λ₀; and C₀λ₀^{a′} ≤ 1.
 (T2) c(a,b) ≥ min(c_sep, (u_a + u′_b)/2) for all pairs with λ > λ₀.
 (T3) |T(u) − n̂| ≤ ϑ_T max(u, ε/2)^{γ_T} for u ≤ G_T  (forward arc).
 (T4) |T(u) − n̂| ≤ ϑ_T max(u′, ε/2)^{γ_T} for u′ ≤ G_T  (tail next to the end E_Y := x⁰(U)).
 (T5) P(t₂) − x⁰(U) = z₀n̂ + y₀n̂^⊥ with 0 ≤ z₀ ≤ C_z ε^{1/4} and |y₀| ≤ ϑ_T (z₀ + ε)(ε/2)^{γ_T}.

*Intended realisation (to be proved by P8a).* x⁰ = the front at t₂ of the labels α ∈ [α₀, 2π + b_e], parametrised by
arclength from X₀: the virtual candidates of [B] for α ∈ [α₀, α₀ + 1.02ε) (they have been inside the ε-disc, hence
their directions are seen, [B, Lemma VC(c)]), and the TRUE candidates (unit-field trajectories,
exact two-integral formulas) for all other labels, **including the labels of the hole |α − 2π| < α_s**, which were
seen during (T1) but of course keep moving by the true law; the single label α = 2π (caught at t₀) is the limit
point. n̂ = Harry's heading on (T2). 𝒢 = the hole labels and [α₀, α₀ + 1.02ε); the labels (b_e, α₀) are seen during
(T2); E_Y = label b_e. Across the hole the true front is C^{1,1} (P8a S1: curvature ≤ 1.14 at t₁ uniformly up to the
axis; N8 §0.1: a parabola), whereas the VIRTUAL candidates of [B] in the hole carry a dent (N8: only a′ ≈ v) — this is
why the working front is used. (T3)–(T5) are the pointwise form of the exponents (1−2v)/(1−v) (forward),
(1−2v)/(1+v) (behind), |E_Y − X₀| ≈ ε^{1/(2−2v)}. Numerical values (`code/P8b/ht.py`): `reports/P8b-1.md` §3.

**Derived constants** (all depend only on the constants of (H_T)):
 γ₁ := min(a′/2, 1/4); γ_* := min(a′/2, γ_T); c_A := min(c_sep, 1/4);
 R_A := min(1, λ₀/32, c_A/16, (γ₁/(400C₀))^{1/a′}); M_A := (γ₁/50)R_A^{−γ₁};
 ϑ_h := 0.34 R_A^{−γ_*} + 1.24 ϑ_T;
 W := min( G_T/3, (20 max(ϑ_T,ϑ_h))^{−1/γ_*}/4.2, R_A · 10^{−1/γ_*}/2.1 );
 C_I := M_A + 1.01 C₀ + 2ϑ_T + ϑ_h + 1.01; a_I := γ_*/2; Λ_I := min(W/40, C_I^{−1/a_I}); c_I := (4/9)Λ_I;
 γ_B := γ_*/4; R_B := min(Λ_I/36, (γ_B/(400C_I))^{1/a_I});
 **v₀ := min( v_T, 2·10⁻¹¹γ_B², 10⁻⁶γ_B R_B/(4.5U_max + 2), 10⁻⁶γ₁R_A/(2U_max + 2), W/132 )**;
 **ε_* := min( ε_T, R_B/64, (W/C_z)⁴ )**;  **T₀ := T₂ + 2.3 U_max + 1**.
(Then also: v₀ ≤ 10⁻⁵γ_*, 1.39v₀ ≤ γ_*/2, ε_* ≤ W/100, ε_* ≤ Λ_I/2, ε_* ≤ R_A/64.)

---------------------------------------------------------------------------------------------------------------------

## §6. Hand-over and main theorem

**Design T_g** (the path). Assume (H_T), v ≤ v₀, ε ≤ ε_*. P on [0,t₂] is (T1), (T2). For t ≥ t₂, P follows
Construction C on the working front started from x⁰ at t_w = t₂, from (t_s,a_s) := (t₂, u = 0), cut at b_E := (u = U);
after the construction stops P is constant. Each leg is determined by P on earlier times, so P depends only on
(v, ε) and is fixed in advance; it is piecewise linear, continuous, with speed ≤ 1.
Notation: j_I := the first index j with u_{a_j} ≥ W, t_I := t_{j_I} ("end of the departure"), D := t_I − t₂.

> **Proposition P8.I (hand-over).** Assume (H_T), v ≤ v₀, ε ≤ ε_*. Then:
> (a) the legs j+1 ≤ j_I are non-final, j_I exists, D ≤ 2.1W, and for a.e. t ∈ [t₂,t_I]: |P′| = 1 and
>  |P′(t) − n̂| ≤ ϑ_h (t − t₂ + ε)^{γ_*};
> (b) at t_I, on the arc [a_{j_I}, b_E] labelled by u^I := l_{t_I}(a_{j_I},·) ∈ [0,U_I], U_I ≤ (9/8)U, with
>  λ_I := l_{t_I}(a,b): hypothesis (ST_end) of [P7, §2] holds with (a′,C₀,λ₀,c_sep) := (a_I, C_I, Λ_I, c_I), i.e.
>  (E1_I) N(a,b;t_I) ≤ C_I λ_I^{1/2+a_I} for all pairs with ε/2 ≤ λ_I ≤ Λ_I,  (E2_I) c(a,b;t_I) ≥ c_I for λ_I > Λ_I,
>  and C_IΛ_I^{a_I} ≤ 1.

*Proof.* Throughout, u, u′ = U − u, λ are the labels at t₂, and "(T·)" refers to (H_T).

**Stage A.** Put U_A := U/2 ≥ 1/2 and b_A := the label u = U_A. On [0,U_A], (ST_end) holds at t₂ with
(a′, C₀, λ₀, c_A): (E1) is (T1); for a pair in [0,U_A] with λ > λ₀, (T2) gives c ≥ min(c_sep, u′_b/2) ≥ min(c_sep, U/4) ≥ c_A.
By Corollary P7.E (Lemma P8.W(d); ε ≤ R_A/64, v ≤ min(2·10⁻¹¹γ₁², 10⁻⁶γ₁R_A/(4U_A+2))), the hypotheses of Theorem P7.B
hold for Construction C from (t₂,0) cut at b_A with (γ₁, R_A, M_A). As long as l_{t_j}(a_j,b_A) > ε this construction
has the same legs as the one cut at b_E (the rule a_{j+1} = max{θ: l_{t_j}(a_j,θ) ≤ ε} gives the same label). By
Theorem P7.B(b) and (J1), every non-final leg advances u by a number in [ε/2,ε], and l_{t_j}(a_j,b_A) ≥ U_A − u_{a_j} > ε
while u_{a_j} ≤ W + ε. Hence the legs j+1 ≤ j_I are common non-final legs, j_I exists, u_{a_{j_I}} ∈ [W, W+ε], there are
at most 2W/ε + 1 of them, each of duration ≤ ε/(1−v): D ≤ (2W+ε)/(1−v) ≤ 2.1W (ε ≤ W/100). By causality the
conclusions (CA), (J1), (J2), (TL), P7.B(b) of stage A hold on [t₂,t_I].
*(a).* Apply Lemma P8.H with γ := γ_* ≤ γ₁, R := R_A, ϑ_f := ϑ_T, G_f := G_T ((T3) gives (F1p), since ū ≤ 1 and
γ_* ≤ γ_T; ϑ_T G_T^{γ_*} ≤ 1/20 is not assumed in (H_T), so we use G_f := 3W: ϑ_T(3W)^{γ_*} ≤ 1/20 by the definition of
W). For j < j_I: Λ = u_{a_j} + ε ≤ 1.01W, so 2Λ ≤ 2.02W ≤ min(3W, R_A, U_A) and (2Λ/R_A)^{γ_*} ≤ (2.02W/R_A)^{γ_*} ≤ 1/10.
The lemma gives (a) (unit speed on non-final legs).

**Departure of the tail.** Apply Theorem P8.D with t_E := t₂, E := the label u = U, û := −n̂, the arc u′ ∈ [0,U_E],
U_E := W (labelled by u′; its tangent in the direction of increasing u′ is −T), γ := γ_*, ϑ₀ := ϑ_T, ϑ_h, D.
(D0): x_E − P = −z₀n̂ − y₀n̂^⊥ = z₀û + y₀û^⊥, z₀ ≥ 0, and (T5) with (ε/2)^{γ_T} ≤ (ε/2)^{γ_*}. (D1p): (T4) (W ≤ G_T,
|(−T) − û| = |T − n̂|). (DP): (a), with P′·û = −P′·n̂ < 0 because |P′ − n̂| < 1. (D2): z₀ ≤ C_zε^{1/4} ≤ W,
a_* = W + z₀ + ε + D ≤ 4.2W, and max(ϑ_T,ϑ_h)(4.2W)^{γ_*} ≤ 1/20 by the definition of W. (D3): v ≤ 10⁻⁵γ_*.
So (i)–(v) of Theorem P8.D hold for the tail {u′ ≤ W} on [t₂,t_I].

**(b), (E1_I).** Let (a,b) be a pair in [a_{j_I},b_E] with ε/2 ≤ λ_I ≤ Λ_I; then λ ≤ λ_I ≤ W/40. Three cases cover all
such pairs: (D) u′_a ≤ W (the pair lies in the tail); otherwise u′_b ≥ u′_a − λ > W − W/40 ≥ W/2, and either
(A) u_b ≤ U_A, or (P) u_b > U_A, in which case u_a > U_A − W/40.

*Case (A).* (a,b) has a ≥ a_{j_I}, u_b ≤ U_A, λ ≤ R_A. If λ ≥ ε/2 it is a family pair of stage A at t_I and (J2) gives
N ≤ M_Aλ^{1/2+γ₁} ≤ M_Aλ_I^{1/2+γ₁}. If λ < ε/2, enlarge it inside [a_{j_I},b_A] to a pair of label length ε/2 (room:
U_A − u_{a_{j_I}} > ε); by [P7, Fact 0.1] and (J2), N(a,b;t_I) ≤ M_A(ε/2)^{1/2+γ₁} ≤ M_Aλ_I^{1/2+γ₁}.

*Case (P).* Let first λ ≥ ε/2. For t ∈ [t₂,t_I], t in leg j+1 (j < j_I): |P − x_{a_j}| ≤ 2ε ([B, Lemma C(4)], e^{2μ} ≤ 2),
and for a label s with u_s ≥ U_A − W/40 − ε/2 and u′_s ≥ W/2 − ε/2: u_s − u_{a_j} ≥ U/2 − 1.04W > λ₀, so by (T2) and
monotonicity of chords ρ_s(t) ≥ c(a_j,s;t₂) − 2ε ≥ min(c_sep, u′_s/2) − 2ε ≥ W/4 − 2.25ε (W ≤ R_A ≤ c_sep/16). The
hull of the arc of (a,b) lies in B(x_a, l_t(a,b)), so its distance from P is ≥ W/4 − 2.25ε − l_t(a,b). Let
ρ₀ := W/5. As long as l_t(a,b) ≤ W/39 this distance is ≥ W/4 − W/44 − W/39 ≥ ρ₀ ≥ ε; and by Lemma P8.A (first claim,
applied up to the first time where l_t = W/39) l_t ≤ e^{vD/ρ₀}λ ≤ e^{10.5v}W/40 < W/39: so the distance bound holds
on all of [t₂,t_I], 4λe^{vD/ρ₀} ≤ ρ₀, and Lemma P8.A with (T1) (λ ≤ λ₀) gives
 N(a,b;t_I) ≤ e^{14.5v}[C₀λ^{1/2+a′} + 2.5v · 2.1W · (25/W²) λ_I^{3/2}] ≤ 1.001[C₀λ_I^{1/2+a′} + (132v/W)λ_I^{3/2}].
If λ < ε/2: enlarge (a,b) at t₂ to label length ε/2; the enlarged pair satisfies the label conditions just used
(margins ε/2), so the same bound holds for it with λ = ε/2 and l_{t_I} ≤ e^{10.5v}ε/2 ≤ 1.0001λ_I; Fact 0.1 gives
N(a,b;t_I) ≤ 1.001[C₀λ_I^{1/2+a′} + (132v/W)λ_I^{3/2}] again (constants rounded up).

*Case (D).* (a,b) lies in the tail {u′ ≤ W} (u′_b < u′_a ≤ W). Let first λ ≥ ε/2. Theorem P8.D(v) at τ = D, with
N(t₂) ≤ C₀λ^{1/2+a′} ≤ C₀λ^{1/2+γ_*} from (T1) when needed, and 1 + D/(5λ) ≤ 1 + 0.42W/λ ≤ W/λ (λ ≤ W/40):
 N(a,b;t_I) ≤ (W/λ)^{1.39v} K_D λ^{1/2+γ_*},  K_D := max(C₀, 1.9Θ) + 0.9vΘ_p ≤ C₀ + 1.91ϑ_T + 0.01ϑ_h.
Since W ≤ 1 and λ ≤ λ_I ≤ 1 and γ_* − 1.39v ≥ γ_*/2: N ≤ K_D λ_I^{1/2+γ_*/2}. If λ < ε/2: enlarge inside the tail to label
length ε/2 and use Fact 0.1: N(a,b;t_I) ≤ K_D(ε/2)^{1/2+γ_*/2} ≤ K_Dλ_I^{1/2+γ_*/2}.

In all cases, as λ_I ≤ 1, a_I = γ_*/2 ≤ min(γ₁, a′, 1) and 132v/W ≤ 1:
N(a,b;t_I) ≤ max(M_A, 1.001(C₀+1), K_D) λ_I^{1/2+a_I} ≤ C_I λ_I^{1/2+a_I}. And C_IΛ_I^{a_I} ≤ 1 by the definition of Λ_I.

**Stretch.** For every pair (a,b) in [a_{j_I},b_E] with λ ≥ ε/2: l_{t_I}(a,b) ≤ (9/8)λ. Indeed split it into consecutive
pairs of label lengths in [ε/2,ε] (≤ W/40); each is in case (A) ((J1): factor ≤ 9/8), (P) (factor ≤ e^{10.5v}) or
(D) (Theorem P8.D(iv): ≤ 1.00002). In particular U_I ≤ (9/8)U.

**(b), (E2_I).** Let λ_I > Λ_I. Then λ ≥ ε/2 (otherwise, enlarging to label length ε/2, λ_I ≤ (9/8)ε/2 < Λ_I, as
ε ≤ Λ_I/2), so λ ≥ (8/9)Λ_I. If λ > λ₀: by (T2), c(a,b;t_I) ≥ c(a,b;t₂) ≥ min(c_sep, (u_a + u′_b)/2) ≥ min(c_sep, W/2) = W/2,
since u_a ≥ u_{a_{j_I}} ≥ W. If λ ≤ λ₀: by (T1), E(t₂) ≤ ½(C₀λ^{a′})²λ ≤ λ/2, so c(t_I) ≥ c(t₂) ≥ λ/2 ≥ (4/9)Λ_I. Both are ≥ c_I. ∎

> **Theorem P8.M (main theorem, modulo (H_T) and [P7]).** Assume (H_T) and let v₀, ε_*, T₀ be the constants of §5
> (they depend only on the constants of (H_T); v₀ > 0). For every v ∈ (0,v₀] and every ε ∈ (0,1) there is a path
> P: [0,T₀] → ℝ², P(0) = 0, |P′| ≤ 1, depending only on (v,ε) (explicit: design T_g for the vision radius
> min(ε, ε_*)), such that every candidate S_θ, θ ∈ [0,2π), comes within distance ε of P at some time ≤ T₀.

*Proof.* A path that sees every direction with radius ε_* does so with any radius ε ≥ ε_*; so let ε ≤ ε_*. By
Proposition P8.I(b) and Corollary P7.E (Lemma P8.W(d)) applied at the leg start t_I to the arc [a_{j_I},b_E] with
(a_I, C_I, Λ_I, c_I): γ = min(a_I/2,1/4) = γ_B, R = min(1, Λ_I/32, c_I/16, (γ_B/(400C_I))^{1/a_I}) = R_B (c_I/16 = Λ_I/36),
ε ≤ R_B/64, v ≤ min(2·10⁻¹¹γ_B², 10⁻⁶γ_BR_B/(4U_I+2)) (U_I ≤ (9/8)U_max). Hence Construction C from (t_I,a_{j_I}) cut at
b_E — which is the continuation of the construction of design T_g — stops at a time
T_stop ≤ t_I + 2U_I/(1−v) ≤ t₂ + 2.1W + 2.26U_max ≤ T₀, and the direction of every true label of [a_{j_I},b_E] has been
seen by then. The directions of the true labels of [0,a_{j_I}] are seen by Lemma P8.W(c)(3′) (legs j+1 ≤ j_I). By
(T0) every other direction is seen during [0,t₂]. P is 1-Lipschitz ([B, Lemma C(0)]) and constant after T_stop. ∎

> **Corollary P8.X (exact capture, modulo (H_T) and [P7]).** Assume (H_T). For every v ∈ (0,v₀] there is a path H
> with |H′| ≤ 1, H(0) = 0, that catches every direction exactly (ε = 0) by time T₀.

*Proof.* Lemma A4.1 (`paper/main.tex`, lem:A41) with D_N := {2πi/2^N: 0 ≤ i < 2^N} (finite, nested, dense union),
ε_N := 2^{−N}ε_* → 0, T := T₀ and H_N := the path of Theorem P8.M for (v, ε_N): |H_N′| ≤ 1 on [0,T₀] and H_N comes
within ε_N of every direction, in particular of every direction of D_N, by time T₀. ∎

**Remarks.** (1) *What is not needed.* No estimate for the tail during the long sweep, no K̃-bound, no hole
crossing, no final-approach lemma: after t_I the tail is an ordinary part of the arc of Theorem P7.B (its (S1) holds
at t_I because Harry is then at distance ≥ W/2 from it), the hole is ordinary smooth front (ghost labels), and the
last legs into E_Y are Theorem P7.B(b). (2) *Why not Theorem P7.B from t₂ on the whole arc:* (S1) fails at t₂ exactly
for the pairs (a,b) with u_a + u′_b ≲ R (start next to X₀, end next to E_Y; chord ≈ u_a + u′_b + z₀); the proof of
P7.B uses (S1) for such pairs through (∗) of its Step 1(d) (far pairs of the tail while the base is near X₀, and (S) in
part (c)). Proposition P8.I replaces this stretch. (3) *Exponent budget:* (H_T) (a′, γ_T) → stage A: γ₁ = min(a′/2,1/4)
(Cor. P7.E) → heading/departure exponent γ_* = min(a′/2, γ_T), loss 1.39v → a_I = γ_*/2 → γ_B = γ_*/4 (Cor. P7.E);
two applications of Corollary P7.E, one restart. (4) With the numerical constants of N8 (a′ = 1/2, γ_T = 1/4, C₀ = 0.25, λ₀ = 0.1, c_sep = 0.099, ϑ_T = 0.2,
U_max = 8.4): R_A = 6.25·10⁻⁶, ϑ_h ≈ 7.1, W ≈ 3·10⁻¹⁰, C_I ≈ 8.8, Λ_I ≈ 7·10⁻¹², R_B ≈ 10⁻³⁸, v₀ ≈ 1.5·10⁻⁴⁷; with P8a's
interim constants (C₀ = 0.86, λ₀ = 1/40, c_sep = 0.024, ϑ_T = 4.3, U_max = 6.4): W ≈ 1.4·10⁻¹¹, R_B ≈ 8·10⁻⁴³,
v₀ ≈ 1.6·10⁻⁵¹, T₀ ≈ 19.5. These are artefacts of the constants of [P7] (tilt lemma 0.33, R ∝ (γ/400C)^{1/a}); nothing
depends on ε.
