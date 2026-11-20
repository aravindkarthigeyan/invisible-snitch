# Q2-claims (version 1): the assembly without hand-over — statements and full proofs

Stream Q2, round 7. Replaces §§ "Departure", "Heading", "Stage A / hand-over", "Main theorem" of `paper/sec_T2.tex` by:
Theorem Q2.E′ (end theorem with an excused tail), Lemma Q2.H (heading up to base label W₁), Theorem Q2.D (departure,
shifted data, pointwise O(v) growth near Harry), Theorem Q2.M (main theorem). Constants: `code/Q2/assembly_constants.py`.

**Status labels.** PROVED = every step written below, using only refereed statements of `paper/sec_B.tex`,
`paper/sec_E.tex`, `paper/sec_T1.tex`, `paper/sec_T2.tex` (Lemma T2-W) and, where marked **[End\*]**, Theorem End\* /
Corollary End\* of stream Q1 as stated in `reports/Q1-1.md` §§1–5 (not yet refereed; proof by Q1) together with the
structural facts (F1)–(F4) of §1.2 (checked here on the refereed proof of thm:End; to be confirmed by Q1 on End\*).
Everything is stated for both cores: **core = old** (thm:End, cor:End, Remark E-restart(1) of sec_E; fully refereed)
and **core = End\*** (Q1). NUMERICAL = computed by the script in 50-digit arithmetic.

Notation: as in sec_B/sec_E/sec_T2. d = 1, μ = v/(1−v), μ_T := 3v/(1+v), a\*(ρ) = 1/ρ (ρ ≥ ε), 2/ε (ρ < ε).
"Core parameters" means the parameter list of End\* (Q1-1 §1):
(γ, R, m, s₀, f, κ₁, c_A, K_R, K_f, K_ε, η, q, ν, d, δ₁, A₀), M = mR^{−γ}, with derived C_A, C_B, C_TL, c₆, …, and
LHS(P7) := exp(vχU/(c_η R) + B₅I₅vm²) + vκ₁τ_I. For **core = old** read: c_A = 1/2, K_R = 32, K_f = 64, K_ε = 64,
s₀ = 1/8, m = γ/50, κ₁ = 9/8 in (J1) but leg advance ≥ ε/2 (write κ_adv = 2; for End\* κ_adv = κ₁), δ₁ = 2,
ν = 22v, C_A m = C_B m = C_TL m = 0.33, LHS(P7) := 1.00001 with threshold 1.01 (Step 5 and (Imp) of thm:End), the
range conditions γ ≤ 1/4, v ≤ 2·10⁻¹¹γ², v(4U+2) ≤ 10⁻⁶γR in place of (P0)–(P7), and T_stop ≤ t_s + 2U/(1−v).

-------------------------------------------------------------------------------------------------------------------
## 1. Theorem Q2.E′ (end theorem with an excused tail)

### 1.1 Statement

**Setting.** A working front (sec_T2, Definition before Lemma T2-W), Construction C from a leg start (t_s, a_s) cut at
b_E, labels u ∈ [0,U] = arclength at t_s from x_{a_s}, u′ := U − u, λ := u_b − u_a, family F(t) and gap g as in sec_E
(End\*: far iff g ≥ K_f λ). Fix W₁ ≥ 0 with U ≥ 2W₁ + R + ε. Call a pair (a,b)
* **body** if u′_b ≥ W₁, **tail** if u′_b < W₁;
* **bad** if u_a < W₁ and u′_b < W₁ (then λ > U − 2W₁ ≥ R), **good** otherwise.

Let j_w be the first index j ≥ j_s with u_{a_j} ≥ W₁ and t_w := t_{j_w} (if the construction reaches it).

**Hypotheses.** Core parameters satisfying (P0)–(P7) with this U (core = old: the range conditions), and
* (S1′) (S1\*) for all good pairs: c(a,b;t_s) ≥ c_A min(λ, K_R R) whenever λ ≥ ε/2 and the pair is good;
* (S2′) (S2\*) for all body pairs with ε/2 ≤ λ ≤ R;
* (S3\*) ε ≤ R/K_ε;
* (TW) if t_w exists: every tail pair with ε/2 ≤ λ ≤ R satisfies, with g_w := u_a − u_{a_{j_w}},
  g_w ≥ K_f λ, l_{t_w}(a,b) ≤ (1+δ_T)λ, and N(a,b;t_w) ≤ s₀Mλ^{1/2+γ} min(1, K_f λ / min(g_w, K_R R))^ν;
* (PT) (1+δ_T)·LHS(P7) < κ₁ (core = old: (1+δ_T)·1.00001 ≤ 1.01).

**Conclusions.**
* (a′) For every t from t_s until the construction stops: (J1\*) l_t(a,b) ≤ κ₁λ and (J2\*) N(a,b;t) ≤ Mλ^{1/2+γ}
  for all **body** pairs of F(t); t_w exists, and for t ≥ t_w (J1\*), (J2\*) hold for **all** pairs of F(t).
  (CA′) c(a,b;t) ≥ c_A min(λ, K_R R) for all good pairs with λ ≥ ε/2 and all t ≥ t_s.
* (b′) = End\*(b) (core old: thm:End(b)): every non-final leg advances the base by [ε/κ_adv, ε]; the construction
  stops at T_stop ≤ t_s + κ_adv U/(1−v); l(a_J, b_E) ≤ ε at T_stop; the direction of every true label of [a_s, b_E]
  is seen by T_stop (working front, Lemma T2-W(c)(3′)).
* (d′) End\*(d) (tilts) at time t for family pairs J ⊂ I with I a body pair, and for all family pairs J ⊂ I if t ≥ t_w.
* (e′) (E-star\*) at t in leg j+1 for every label s with w_s = u_s − u_{a_j} ≥ 0 and (u′_s ≥ W₁ or u_{a_j} ≥ W₁):
  ρ_s ≥ c_A min(w_s, K_R R) − δ₁ε.

For W₁ = 0 there are no tail pairs and Q2.E′ is End\* (resp. thm:End).

### 1.2 Structural facts used (checked on the refereed proof of thm:End, sec_E lines 167–440)

(F1) *Locality.* In the proof of (Imp) for a pair (a,b) ∈ F(t) (Steps 1–5) the following are used, at times t′ ≤ t
with base a_{j(t′)}: (i) the family bounds (J1),(J2) for pairs (a″,b″) ∈ F(t′) with
[a″,b″] ⊂ [a_{j(t′)}, max(b, a_{j(t′)+1})]
[Step 2 tilt lemma, sub-arcs (A),(B),(C) of I ⊂ (a_j, b); Step 3 pairs (a′,a), (a,b), (a′,b), a′ ∈ {a_j, a_{j+1}};
Step 4 sub-arcs J_y ⊂ (a,b), J₀ ⊂ (a′,b), and I = (a_j,a_{j+1}) in the case a_{j+1} > b; Step 5 J_y]; (ii) (CA) for those family pairs
(tilt lemma, c(J₁) ≥ c_A λ_{J₁}) and for the pairs (a_{j(t′)}, s), s ∈ [a,b], through (E-star) at the labels
s ∈ [a,b] [Step 1(d); Step 3: ρ_m via the hull in B(x_a,l) and (E-star); Step 4: ρ̄, Term I (ρ_s<y ⇒ w_s<…),
Term II (|q| for w_s ≤ / > K_R R); Step 5 near part]; (iii) Lemma B-C(2),(4), Lemma B-3, B-4, E-facts, geometry;
(iv) start data at t_s: N(t_s) (Step 3, first term), E(t_s) of pairs near at t_s (Step 4), l(t_s) = λ (Step 5).
Nothing else about other pairs or labels enters.

(F2) *Far pairs with a later start.* In Step 3 the start time enters only as the left end t_s of the integrals of α and
β and through N(t_s). If a pair is far on [t′, t] (t′ ≥ t_s a leg start) and the family bounds hold on [t′, t] for the
pairs of (F1)(i), the computation of Step 3 on [t′,t] gives the far-pair bound of End\* (N ≤ fMλ^{1/2+γ}, which is
what (P5) encodes; old: N ≤ (3/8)Mλ^{1/2+γ}) provided N(t′) ≤ s₀Mλ^{1/2+γ} min(1, K_fλ/min(g(t′), K_R R))^ν. (Old: Step 3 "First term" with
g_s := g(t′), "Second/Third term" over [t′,t] ⊂ [t_s, t]: both are bounded by the same integrals.)

(F3) *Length with a later start.* Step 5 bounds l(t) by l(t′)·exp(∫ far growth) + (near increase), the near increase
being ≤ vκ₁τ_I λ (old: 3618vλ) and computed from (J1) for sub-arcs, not from l(t′). Hence l(t′) ≤ (1+δ_T)λ gives
l(t) ≤ (1+δ_T)·LHS(P7)·λ < κ₁λ under (PT) (old: ≤ (1+δ_T)·1.00001λ ≤ 1.01λ).

(F4) Step 1(a) uses (J1) at a leg start t_j only for (a_j, s) with u_s = u_{a_j} + ε/2 and, in case (β), for
(a_{j−1}, b_E); Step 1(b) counts legs.

For core = End\* these four facts are the interface items (P1)–(P4) of `reports/Q2-1.md` (interim); Q1 re-derives
thm:End step by step (Q1-1 §4), so they transfer; **Q1 is asked to confirm (F1)–(F4) for End\***.

### 1.3 Proof

*Step 0 (separation).* By (S1′) and monotonicity of chords (Lemma T2-W(a)), (CA′) holds. For t in leg j+1 and a
label s with w_s ≥ 0: if λ(a_j,s) < ε/2 then ρ_s ≥ −δ₁ε trivially; otherwise, if u′_s ≥ W₁ or u_{a_j} ≥ W₁, the pair
(a_j,s) is good, and Step 1(d) of End\* (|P − x_{a_j}| ≤ δ₁ε, Lemma B-C(4)) gives (e′).

*Every pair with λ ≤ U − 2W₁ is good* (a bad pair has u_a < W₁, u_b > U − W₁). In particular all pairs of length
≤ R (all family pairs) are good, so (CA′) holds for every family pair.

*Part 1: t ∈ [t_s, t_w].* Let T₁ := sup{t′ ≤ T_end: u_{a_j} < W₁ for every leg start t_j ≤ t′}. Run the continuity
argument of End\*(a) on [t_s, T₁] with the family replaced by the body family F_b(t) := {(a,b) ∈ F(t): u′_b ≥ W₁}
(F_b(t) shrinks in t like F(t)). Let (a,b) ∈ F_b(t). For t′ ≤ t in Part 1, u′_{a_{j(t′)+1}} ≥ U − W₁ − ε ≥ W₁, so every
pair [a″,b″] ⊂ [a_{j(t′)}, max(b, a_{j(t′)+1})] has u′_{b″} ≥ min(u′_b, u′_{a_{j(t′)+1}}) ≥ W₁: it is a body pair: the family bounds of (F1)(i) are the assumed bounds for F_b. Every label s ∈ [a_{j(t′)}, b] has
u′_s ≥ W₁, so (E-star) holds at s by Step 0; all family pairs satisfy (CA). The start data of (F1)(iv) are (S2′) and
l = λ. Hence the proof of (Imp) of End\* applies verbatim to (a,b), and the closing argument of End\*(a) (which uses
only |E′| ≤ (4v/ε)l, l′ ≤ (2v/ε)l and the bounds of (Imp) for pairs of the family at t\*) gives (J1\*),(J2\*) for
F_b on [t_s, T₁]. Legs: at a leg start t_j < T₁ (u_{a_j} < W₁), Step 1(a) applies (F4): the pair (a_j, s),
u_s = u_{a_j} + ε/2, has u′_s ≥ U − W₁ − ε/2 ≥ W₁ (as U ≥ 2W₁ + ε), a body pair; case (β) (U − u_{a_j} < ε/2) is
impossible since u_{a_j} < W₁. So leg j+1 is final or advances by [ε/κ_adv, ε], and it is not final: a final leg
needs l_{t_j}(a_j,b_E) ≤ ε, hence U − u_{a_j} ≤ ε, contradicting u_{a_j} < W₁ ≤ U − W₁ − ε. The proviso of Lemma
T2-W(c) holds: (a_j, a_{j+1}) has λ ≥ ε/κ_adv ≥ ε/2 and is a body pair, so c > 0 by (CA′). By Lemma B-C(0) the base
reaches W₁ after finitely many legs: t_w exists, T₁ = t_w, and (J1\*),(J2\*) hold for body pairs on [t_s, t_w].

*Part 2: t ≥ t_w.* At t_w every pair of F(t_w) satisfies the strict bounds: body pairs by Part 1 ((Imp) bounds at
t_w), tail pairs by (TW) (s₀ < 1, so N < Mλ^{1/2+γ}; and (1+δ_T) < κ₁ by (PT), LHS(P7) ≥ 1). Run the continuity
argument of End\*(a) on [t_w, T_end] for the whole family F(t). Let t ∈ [t_w, t\*], (a,b) ∈ F(t), base a_{j(t′)} with
u_{a_{j(t′)}} ≥ W₁ for t′ ≥ t_w.
* Body pair: by Part 1 its history on [t_s, t_w] satisfies everything (F1) asks; on [t_w, t] the family bounds of
  (F1)(i) are the continuity hypothesis, and (E-star) holds at all labels s ≥ a_{j(t′)} (u_{a_{j(t′)}} ≥ W₁, Step 0).
  The proof of (Imp) applies verbatim.
* Tail pair: by (TW) it is far at t_w (g_w ≥ K_fλ), hence far on [t_w, t_n) where t_n is the time it becomes near
  (gaps are non-increasing). On [t_w, t] ∩ far: (F2) with t′ = t_w and (TW) gives the far bound of Step 3. When it
  becomes near, Step 4 applies verbatim with the start value given by Step 3 at that time (it was far at t_w, so the
  start datum E(t_s) of (F1)(iv) is not needed). Step 5: (F3) with t′ = t_w. (E-star) at its labels: u_{a_{j(t′)}} ≥ W₁ (Step 0). Family bounds of sub-pairs:
  continuity hypothesis.
Hence (Imp) holds on [t_w, t\*], and the closing argument gives (J1\*),(J2\*) for F(t) up to T_end. Step 1(a)
including case (β) (pairs (a_{j−1}, b_E) at the end, t ≥ t_w) now holds as in End\*, so (b′) follows exactly as
End\*(b) (with Lemma T2-W(c)(3′) for "seen"). (d′) is Step 2 at the time t for pairs with bounds. ∎

*No circularity.* Part 1 does not use (TW). (TW) is a statement about the configuration at t_w, which depends only on
P|[0, t_w]; in the assembly it is proved from Lemma Q2.H and Theorem Q2.D, which use stage A (an independent
application of End\*) and not Q2.E′.

-------------------------------------------------------------------------------------------------------------------
## 2. Lemma Q2.H (heading of the first legs up to base label W₁)

**Setting.** Working front; Construction C from (t_s, a_s) = (t_td, u=0) cut at b_A (label U_A); stage-A
conclusions of End\*(a),(b),(d),(e) [old: thm:End(a),(b),(d), (E-star)] hold on [t_s, t_j] for the leg starts
considered (causality, Remark E-B(4) / its End\* analogue), with constants (γ₁, R₁, m₁, c_{A1}, K_{R1}, δ₁, κ_adv)
and tilt bounds |e_J − e_I| ≤ C_{A1}m₁(λ_I/R₁)^{γ₁} (J ⊂ I, same left end), C_{B1}m₁(λ_I/R₁)^{γ₁} (same right end). Let n̂ be a unit vector,
0 < γ_h ≤ γ₁, 0 < δ₀ ≤ R₁/2, W₁ > 0, G_f := W₁ + ε + δ₀ ≤ U_A − ε, and assume the forward data
(F1\*) |T(u, t_s) − n̂| ≤ K_fw u^{1−μ} for u ≤ G_f, with σ̄ := K_fw G_f^{1−μ} ≤ 1/2 and γ_h ≤ 1 − μ.
Put θ_f := K_fw G_f^{1−μ−γ_h}, k_σ := (1+σ̄/2)/(1−σ̄²/2), C₃m₁ := 2C_{B1}m₁ + C_{A1}m₁,
ρ\* := c_{A1}(R₁ − δ₀ − ε) − δ₁ε (assume ρ\* ≥ ε), c_τ := 1/(1 − m₁²/2) (assume m₁² < 2),
K_rot := (κ_adv/(1−v))·[2R₁/(c_{A1}δ₀) + (W₁+ε)/ρ\*],
ω₀ := C_{A1}m₁(δ₀/R₁)^{γ₁} + k_σσ̄ + vK_rot,
θ_{h1} := C_{A1}m₁R₁^{−γ₁}δ₀^{γ₁−γ_h} + 2^{γ_h}k_σθ_f + v·(4κ_adv C₃m₁/(c_{A1}(1−v)))·2^{γ₁}R₁^{−γ₁}δ₀^{γ₁−γ_h},
θ_h := c_τ^{γ_h} max(θ_{h1}, ω₀δ₀^{−γ_h}).

**Lemma Q2.H.** Let j ≥ j_s with u_{a_j} < W₁ and leg j+1 non-final (û_{j+1} its direction). Then for all t in leg
j+1, τ := t − t_s:
  |û_{j+1} − n̂| ≤ h(τ) := min(θ_h(τ+ε)^{γ_h}, ω₀).

**Proof.** Λ := u_{a_j} + ε (< W₁ + ε), λ_I := min(Λ, δ₀) ∈ [ε, δ₀], b the label with u_b = u_{a_j} + λ_I ≤ G_f ≤ U_A,
I := (a_j, b). Since ε/2 ≤ λ_I ≤ R₁ and its first point is the base, I ∈ F_A(t_j).

*Step 1 (t_j).* J := (a_j, a_{j+1}) ∈ F_A(t_j) (advance in [ε/κ_adv, ε] ⊂ [ε/2, R₁]), J ⊂ I with the same left end,
e_J(t_j) = û_{j+1} (Lemma B-C(2)). Tilts: |û_{j+1} − e_I(t_j)| ≤ C_{A1}m₁(λ_I/R₁)^{γ₁}.

*Step 2 (t_s).* With σ := sup_I |T(·,t_s) − n̂| ≤ K_fw u_b^{1−μ} ≤ σ̄ (u_b ≤ G_f) and l = λ_I at t_s:
c e_I − l n̂ = ∫_I (T − n̂) ds, c ≥ ∫_I T·n̂ ≥ l(1 − σ²/2), so
|e_I − n̂| ≤ (l/c)σ + (l−c)/c ≤ σ(1+σ/2)/(1−σ²/2) ≤ k_σσ. Moreover σ ≤ θ_f u_b^{γ_h} (as u_b ≤ G_f) and
σ ≤ σ̄; u_b ≤ u_{a_j} + Λ ≤ 2Λ.

*Step 3 (rotation of e_I on [t_s, t_j]).* From c_I e_I = x_b − x_a and x′ = vF(r): c_I|e_I′| = v|e_I × (F(r_b) − F(r_a))|.
Let t be in leg i+1, j_s ≤ i ≤ j−1; by Lemma B-C(2), P = x_{a_{i+1}} − ρ′û_{i+1}, ρ′ ≥ 0, û_{i+1} = e_{(a_i,a_{i+1})}(t).
Put W := u_{a_j} − u_{a_{i+1}} ≥ 0 and κ_W := m₁((W + λ_I + ε)/R₁)^{γ₁}.

(α) *Close case W + λ_I + ε ≤ R₁.* If i ≤ j−2: K₁ := (a_{i+1}, a_j), K₂ := (a_{i+1}, b), K₃ := (a_i, a_{i+1}),
K₄ := (a_i, b) and I are in F_A(t) (first points a_i or ≥ a_{i+1}; lengths ≥ ε/κ_adv ≥ ε/2 and
≤ ε + W + λ_I ≤ R₁). Tilts (stage A): I ⊂ K₂ ⊂ K₄ share the right end; K₁ ⊂ K₂ and K₃ ⊂ K₄ share the left end; all
lengths ≤ W + λ_I + ε. So |e_I − e_{K₂}| ≤ C_{B1}κ_W, |e_I − e_{K₁}| ≤ |e_I − e_{K₂}| + |e_{K₂} − e_{K₁}| ≤ (C_{A1}+C_{B1})κ_W ≤ C₃κ_W,
|e_I − û_{i+1}| = |e_I − e_{K₃}| ≤ |e_I − e_{K₄}| + |e_{K₄} − e_{K₃}| ≤ (C_{B1} + C_{A1})κ_W ≤ C₃κ_W
(C₃ := 2C_{B1} + C_{A1}; κ_W as in the setting of (α), so C₃κ_W = C₃m₁((W+λ_I+ε)/R₁)^{γ₁}).
Now r_a = c(K₁)e_{K₁} + ρ′û_{i+1}, r_b = c(K₂)e_{K₂} + ρ′û_{i+1} with non-negative coefficients; |e × e′| ≤ |e − e′|
gives |e_I × r_a| ≤ C₃κ_W(c(K₁)+ρ′); and if x := C₃κ_W ≤ 1, ρ_a ≥ r_a·e_I ≥ (1 − x²/2)(c(K₁)+ρ′); likewise for b.
If i = j−1: r_a = ρ′û_j, and (a_{j−1}, a_j), (a_{j−1}, b), I are in F_A(t) (lengths ≤ ε + λ_I ≤ R₁):
|e_I − û_j| ≤ |e_I − e_{(a_{j−1},b)}| + |e_{(a_{j−1},b)} − e_{(a_{j−1},a_j)}| ≤ (C_{B1} + C_{A1})κ_W ≤ C₃κ_W, and
r_b = c_I e_I + ρ′û_j. In both cases |e_I × r̂_a|, |e_I × r̂_b| ≤ ψ(C₃κ_W), ψ(x) := min(1, x/(1−x²/2)) ≤ min(1, 2x)
(the bound 1 is trivial). As |e × F(r)| = f(ρ)|e × r̂| ≤ |e × r̂| and c_I ≥ c_{A1}λ_I (CA, λ_I ≤ R₁):
|e_I′| ≤ 2vψ(C₃κ_W)/(c_{A1}λ_I).

(β) *Far case W + λ_I + ε > R₁.* Then w_{a_j} := u_{a_j} − u_{a_i} ≥ W > R₁ − δ₀ − ε and w_b ≥ w_{a_j}; stage-A
(E-star) gives ρ_a, ρ_b ≥ c_{A1} min(R₁ − δ₀ − ε, K_{R1}R₁) − δ₁ε = ρ\* ≥ ε (K_{R1} ≥ 1). So F(r) = r̂ at a, b
(Lemma B-V(i)); with p := e_I × r_a = e_I × r_b (r_b − r_a = c_I e_I):
|e_I × (r̂_b − r̂_a)| = |p|·|1/ρ_b − 1/ρ_a| ≤ |p| c_I/(ρ_aρ_b) ≤ c_I/max(ρ_a,ρ_b) (|p| ≤ min(ρ_a,ρ_b)). Hence
|e_I′| ≤ v/ρ\*.

*Durations.* Each non-final stage-A leg lasts ≤ ε/(1−v) and advances the base by ≥ ε/κ_adv. All legs i+1 ≤ j occupy
time ≤ κ_adv u_{a_j}/(1−v) ≤ κ_adv Λ/(1−v). The close-case legs have u_{a_{i+1}} ∈ [u_{a_j} − (R₁ − λ_I − ε), u_{a_j}],
so their number is ≤ κ_adv(R₁ − λ_I − ε)/ε + 1 and their total time ≤ κ_adv R₁/(1−v); thus close-case time
≤ κ_adv min(Λ, R₁)/(1−v). For W + λ_I + ε ≤ u_{a_j} + λ_I + ε ≤ 2Λ: κ_W ≤ m₁ min(1, 2Λ/R₁)^{γ₁}.

*Rotation bound.* If Λ ≤ δ₀ (≤ R₁/2): λ_I = Λ, W + λ_I + ε ≤ 2Λ ≤ R₁, only the close case occurs, and
|e_I(t_j) − e_I(t_s)| ≤ (2v·2C₃m₁(2Λ/R₁)^{γ₁}/(c_{A1}Λ))·κ_advΛ/(1−v) = v(4κ_adv C₃m₁/(c_{A1}(1−v)))(2Λ/R₁)^{γ₁}.
In all cases (ψ ≤ 1, min(Λ,R₁)/λ_I ≤ max(1, R₁/δ₀) = R₁/δ₀, far time ≤ κ_adv Λ/(1−v) ≤ κ_adv(W₁+ε)/(1−v)):
|e_I(t_j) − e_I(t_s)| ≤ vK_rot.

*Step 4 (sum).* |û_{j+1} − n̂| ≤ C_{A1}m₁(λ_I/R₁)^{γ₁} + k_σσ + rot. (i) Always: ≤ C_{A1}m₁(δ₀/R₁)^{γ₁} + k_σσ̄ +
vK_rot = ω₀. (ii) If Λ ≤ δ₀: using Λ^{γ₁} ≤ δ₀^{γ₁−γ_h}Λ^{γ_h}, σ ≤ θ_f(2Λ)^{γ_h}:
≤ θ_{h1}Λ^{γ_h}. (iii) If Λ > δ₀: ω₀ ≤ ω₀δ₀^{−γ_h}Λ^{γ_h}. So |û_{j+1} − n̂| ≤ max(θ_{h1}, ω₀δ₀^{−γ_h})Λ^{γ_h} always.
*Time.* Each stage-A leg i+1 lasts ≥ c(a_i,a_{i+1};t_i) (closing speed ≤ 1, Lemma B-C(2): ρ′ = −1 + vf ≥ −1), and
c = l − E ≥ λ − ½M₁²λ^{1+2γ₁} ≥ λ(1 − m₁²/2) by (J2\*), λ ≤ ε ≤ R₁. So t_j − t_s ≥ (1 − m₁²/2)u_{a_j} and, for
τ ≥ t_j − t_s, Λ ≤ c_τ(τ + ε). Hence |û_{j+1} − n̂| ≤ θ_h(τ+ε)^{γ_h}, and ≤ ω₀ by (i). ∎

-------------------------------------------------------------------------------------------------------------------
## 3. Theorem Q2.D (departure from near an end; shifted data; O(v) growth near Harry)

**Setting** as in thm:T2-D (sec_T2): working front, time t_E, end label E, unit vector û, duration D, τ := t − t_E,
labels u ∈ [0, U_E] = arclength at t_E from x_E, r_s = x_s − P = z_s û + y_s û^⊥ (z_s := r_s·û, y_s := û × r_s),
X_s(τ) := u_s + z₀ + τ. Parameters γ ∈ (0,1), θ₀, θ_y, θ_h ≥ 0, ω̄ ∈ (0, 1/2], ω₀ ≤ ω̄, k > 0.
**Hypotheses.**
* (D0) x_E(t_E) − P(t_E) = z₀û + y₀û^⊥, z₀ ≥ ε/ζ, |y₀| ≤ θ_y z₀^{1+γ};
* (D1) |T(u,t_E) − û| ≤ θ₀(u + z₀)^γ, u ∈ [0, U_E];
* (D2) a.e. τ ∈ [0,D]: |P′| = 1, P′·û < 0, |û × P′| ≤ h(τ) := min(θ_h(τ+ε)^γ, ω₀);
* (D3) with X\* := U_E + z₀ + D: θ₀X\*^γ ≤ ω̄, ω̄_y := θ_yX\*^γ ≤ ω̄, and ζ := (1 − ω̄²)^{1/2} − v > 0,
  η := v/ζ ≤ γ/2, ω_T := Θ₀X\*^γ ≤ 1/2, k ≥ 4(1+δ_t)/ζ (Θ₀, δ_t below).
Put θ_{0y} := max(θ₀, θ_y), η_N := 1.375v/ζ,
Θ₀ := θ₀ + vθ_{0y}/ζ² + vθ_h/(ζ²(1−η)(γ−η)),
x_c := (ω₀/θ_h)^{1/γ}, L_h := 1/(2γ) + log⁺((D+ε)/x_c),
K_w := (Θ₀ + θ_{0y}/ζ)²X\*^{2γ}/(γζ) + 2ω₀²L_h/(ζ³(1−η)²), δ_t := e^{vK_w} − 1,
Θ_b := Θ₀ + θ_{0y}/ζ + θ_h/(ζ(1−η)), c_n := (1+δ_t)^{1/2}k^γ/(γζ),
Θ_p := (1 + ω̄_y + v)(1+1/k)^γΘ₀/(1 − ω_T²/2) + θ_{0y} + θ_h/(1−η), c_β := 2(1+δ_t)^{3/2}k^{γ−1}/(ζ³(1−γ)).

**Theorem Q2.D.** For τ ∈ [0,D] and labels s of the arc:
* (i) z_s ≥ ζX_s(τ), ρ_s ≥ ζX_s(τ) ≥ ε; hence a\*(ρ_s) ≤ 1/(ζX_s) and exp(v∫_{τ′}^{τ}a\*(ρ_s)) ≤ (X_s(τ)/X_s(τ′))^η.
* (ii) |y_s(τ)| ≤ X_s(τ)[θ_{0y}X_s(0)^γ + h(τ)/(1−η)].
* (iii) |T(u_s,t) − û| ≤ Θ₀X_s(τ)^γ ≤ ω_T.
* (iv) 1 ≤ w̃ ≤ 1 + δ_t; λ ≤ l_t(a,b) ≤ (1+δ_t)λ for all pairs.
* (v) For every pair with ε/2 ≤ λ: c(a,b;t) ≥ (1 − ω_T²/2)l_t(a,b) and
  N(a,b;t) ≤ (1 + τ/(kλ))^{η_N}[N(a,b;t_E) + v(c_nΘ_b + c_βΘ_p)λ^{1/2+γ}].

**Proof.** (i) z_s′ = v f(ρ_s)z_s/ρ_s − P′·û ≥ −v + (1 − h²)^{1/2} ≥ ζ (|z| ≤ ρ, f ≤ 1, P′·û < 0, |P′|=1).
At t_E: z_s = z₀ + ∫_0^{u_s} T·û du ≥ z₀ + (1 − ω̄²/2)u_s (T·û = 1 − ½|T−û|², (D1),(D3)); 1 − ω̄²/2 ≥ ζ. So
z_s ≥ ζX_s ≥ ζz₀ ≥ ε. Then ρ_s ≥ z_s ≥ ε, a\* = 1/ρ_s ≤ 1/(ζX_s), and ∫ v/(ζX_s) dτ = η log(X(τ)/X(τ′)).
(ii) As ρ_s ≥ ε, F(r_s) = r_s/ρ_s and y_s′ = (v/ρ_s)y_s − û × P′, so |y_s|′ ≤ va\*|y_s| + h a.e., and
|y_s(τ)| ≤ (X(τ)/X(0))^η|y_s(0)| + ∫_0^τ (X(τ)/X(τ′))^η h(τ′)dτ′. At t_E,
y_s(0) = ∫_0^{u_s} û × (T − û)du + y₀, so |y_s(0)| ≤ θ₀u_s X_s(0)^γ + θ_y z₀^{1+γ} ≤ θ_{0y}X_s(0)^{1+γ}. In the
integral X(τ′) ≥ τ′ + z₀ and h is non-decreasing: ∫ ≤ X(τ)^η h(τ)(τ+z₀)^{1−η}/(1−η) ≤ X(τ)h(τ)/(1−η). Finally
(X/X₀)^η X₀^{1+γ} ≤ X·X₀^γ. More precisely, for 0 ≤ τ′ ≤ τ,
(∗) |y_s(τ′)| ≤ (X(τ′)/X(0))^η θ_{0y}X(0)^{1+γ} + X(τ′)^η(τ′+z₀)^{1−η}h(τ′)/(1−η).
(iii) Lemma B-1(ii): T_t = v(AT − (T·AT)T); with 𝔭 := 1 − T·û: ∂_t𝔭 = v[(T−û)·AT − (T·AT)𝔭] ≤ v(T−û)·AT ≤
v[a\*δ² + δ|q_û|], δ := |T − û|, |q_û| ≤ |y_s|/ρ_s² ≤ |y_s|/(ζX)² (Lemma B-V(iii), E-facts(c)). Regularising
(δ_κ = (2𝔭+κ²)^{1/2}) and by variation of constants:
δ(τ) ≤ (X/X₀)^ηδ(0) + (v/ζ²)∫_0^τ (X(τ)/X(τ′))^η|y_s(τ′)|X(τ′)^{−2}dτ′. Insert (∗): the first part gives
≤ (v/ζ²)θ_{0y}X₀^{1+γ}(X/X₀)^η∫X^{−2} ≤ (v/ζ²)θ_{0y}X₀^γ(X/X₀)^η; the second gives
≤ (v/(ζ²(1−η)))X^η∫_0^τ(τ′+z₀)^{−1−η}θ_h(τ′+ε)^γdτ′ ≤ (vθ_h/(ζ²(1−η)(γ−η)))X^η(τ+z₀)^{γ−η}
≤ (vθ_h/(ζ²(1−η)(γ−η)))X^γ (ε ≤ z₀, γ > η). With δ(0) ≤ θ₀X₀^γ and (X/X₀)^ηX₀^γ ≤ X^γ (η ≤ γ):
δ ≤ Θ₀X^γ ≤ Θ₀X\*^γ = ω_T.
(iv) w̃_t = vw̃T·AT (Lemma B-1(i)); T·AT = sin²φ/ρ with sin φ = |T × r̂| ≤ δ + |y|/ρ ≤ (Θ₀ + θ_{0y}/ζ)X^γ +
h/(ζ(1−η)) by (ii),(iii) and ρ ≥ ζX. With (a+b)² ≤ 2a² + 2b² and ρ ≥ ζX ≥ ζ(τ+ε):
∫_0^τ T·AT ≤ (2/ζ)(Θ₀+θ_{0y}/ζ)²∫X^{2γ−1} + (2/(ζ³(1−η)²))∫_0^D h(τ′)²/(τ′+ε)dτ′ ≤
(Θ₀+θ_{0y}/ζ)²X\*^{2γ}/(γζ) + 2ω₀²L_h/(ζ³(1−η)²) = K_w, because ∫_0^D min(θ_h²(τ′+ε)^{2γ}, ω₀²)(τ′+ε)^{−1}dτ′ ≤
∫_0^{x_c}θ_h²y^{2γ−1}dy + ∫_{x_c}^{D+ε}ω₀²y^{−1}dy ≤ ω₀²L_h. So 1 ≤ w̃ ≤ e^{vK_w} (w̃ ≥ 1: Lemma T2-W(a)).
(v) *Chord:* c ≥ (x_b − x_a)·û = ∫T·û ds ≥ (1 − ω_T²/2)l. Let g̃ := u_a + z₀ and τ₀ := max(0, kλ − g̃).
*Phase τ ≤ τ₀.* Lemma B-3(b): E′ ≤ vN‖AT‖_{L²(ds)}; with N_κ := (N²+κ²)^{1/2}, N_κ′ ≤ v‖AT‖, κ → 0. On the arc
ρ ≥ ε, |AT| = sin φ/ρ ≤ [(Θ₀ + θ_{0y}/ζ)X^γ + θ_h(τ+ε)^γ/(ζ(1−η))]/(ζX) ≤ Θ_bX_s^{γ−1}/ζ ≤ Θ_b(g̃+τ)^{γ−1}/ζ
(X_s ≥ g̃ + τ ≥ τ + ε, γ < 1). So ‖AT‖ ≤ (1+δ_t)^{1/2}λ^{1/2}Θ_b(g̃+τ)^{γ−1}/ζ and
N(τ₀) ≤ N(0) + v(1+δ_t)^{1/2}(Θ_b/ζ)λ^{1/2}(g̃+τ₀)^γ/γ = N(0) + vc_nΘ_bλ^{1/2+γ} (g̃ + τ₀ = kλ if τ₀ > 0).
*Phase τ ≥ τ₀.* The hull of the arc of (a,b) lies in {x: (x − P)·û ≥ min_s z_s}, so ρ_m ≥ ζ(g̃+τ) ≥ ζkλ ≥
4(1+δ_t)λ ≥ 4l, and ρ_m ≥ ζz₀ ≥ ε. Lemma B-3(e) on [τ₀,τ]: α ≤ 1.375v/ρ_m ≤ η_N/(g̃+τ′),
β = 2vl^{3/2}|p_a|/ρ_m³ with |p_a| ≤ ρ_a|û × e_ab| + |y_a| (p_a = z_a(û × e) + y_a(û^⊥ × e)), where
|û × e_ab| ≤ (l/c)sup δ ≤ Θ₀X_b^γ/(1 − ω_T²/2), X_b = g̃ + λ + τ′ ≤ (1 + 1/k)(g̃ + τ′);
ρ_a(τ′) ≤ u_a + z₀ + |y₀| + (1+v)τ′ ≤ (1 + ω̄_y + v)(g̃+τ′) (|y₀| ≤ ω̄_y z₀);
|y_a| ≤ (g̃+τ′)^{1+γ}(θ_{0y} + θ_h/(1−η)) by (ii) (X_a = g̃ + τ′, h ≤ θ_h(τ′+ε)^γ, ε ≤ g̃).
So |p_a| ≤ Θ_p(g̃+τ′)^{1+γ} and β ≤ 2v(1+δ_t)^{3/2}λ^{3/2}Θ_p(g̃+τ′)^{γ−2}/ζ³. Lemma B-3(e) and
∫_{τ₀}^∞(g̃+τ′)^{γ−2} ≤ (kλ)^{γ−1}/(1−γ) give N(τ) ≤ ((g̃+τ)/(g̃+τ₀))^{η_N}[N(τ₀) + vc_βΘ_pλ^{1/2+γ}], and
(g̃+τ)/(g̃+τ₀) ≤ 1 + τ/(kλ). ∎

*Remarks.* (1) Compared with thm:T2-D: shifted data (D1) (no ε/2-floor; this is the form actually proved in sec_T1),
general γ < 1, heading bound that need not be small in Hölder form for large τ (only min(…, ω₀)), and in (v) no
re-bound through the tilt for pairs close to Harry: N(t_E) enters with factor 1 and the growth is O(v)·λ^{1/2+γ}
(the old N\* = 1.9Θ₀λ^{1/2+γ} cost a factor ≈ 4 and forced γ ≤ 1/4 through 13^γ). (2) (D0) z₀ ≥ ε/ζ keeps the whole arc
outside the ε-disc; for design T z₀ ≈ √(2ε).

-------------------------------------------------------------------------------------------------------------------
## 4. Theorem Q2.M (main theorem, new assembly)

### 4.1 Touch-down data used (thm:HT of sec_T1 including its "sharper forms actually proved")

(H_T\*) for v ≤ v_T, ε ≤ ε_T: t_td ≤ T₂; x⁰: [0,U] → R², U ∈ [U_min, U_max], (T0) as in (H_T);
(T1\*) N ≤ C₀λ^{1/2+a′} (ε/2 ≤ λ ≤ λ₀), C₀λ₀^{a′} ≤ 1; (T2) c ≥ min(c_sep, κ₂(u_a + u′_b)) for λ > λ₀;
(T3\*) |T(u) − n̂| ≤ K_fw u^{1−μ}, u ≤ G_T; (T4\*) |T(u) − n̂| ≤ K_tl(ξ_e + u′)^{1−μ_T}, u′ ≤ G_T, with z₀ ≥ κ_zξ_e;
(T5\*) c_zlo ε^{1/(2−2v)} ≤ z₀ ≤ c_zhi ε^{1/(2−2v)}, |y₀| ≤ c_y ε^{1−v/2}.
Round 6 (D₁ = 1): v_T = 10⁻⁶, ε_T = 10⁻³, T₂ = 3.74, U ∈ [1, 6.5], λ₀ = 1/40, c_sep = 0.024, κ₂ = 1/2, K_fw = 1.69,
K_tl = 1.647, κ_z = 0.9939 (Prop. T1-arcs(2): z_E ∈ [−1.00013ξ_e, −0.9939ξ_e], z₀ = −z_E), c_zlo = 1.269,
c_zhi = 1.567, c_y = 1.000003 (proof of (T5)), G_T = 0.05; (a′, C₀) = (1/2, 0.86) as stated, or any
a′ ≤ 1 − 3v_T with C₀ = 5.4λ₀^{1−3v_T−a′} (sharper (T1)).

Q3 data (reports/Q3-1.md final, Theorem Q.H / HT′, referee/Q3-claims.md; not yet refereed): for every column
(v̄, η, ε̄ = 10⁻³) of code/Q3/constants.py and all v ≤ v̄: C₀ = c_Nλ₀^{1−μ̄_T−a′}, κ₂ = kap2, K_fw = θ_v,
(T4\*) in the form |T − n̂| ≤ c_T4(u′+z₀)^{1−μ̄_T} (K_tl = c_T4, κ_z = 1), c_zlo = h_t·xe_lo, c_zhi = zcoef, U_min = 1,
and |y₀| ≤ c_y(z₀+ε)^{2−μ̄_T} in place of the ε-form of (T5\*). All exponents are used with μ̄ := v̄/(1−v̄),
μ̄_T := 3v̄/(1+v̄) (valid for every v ≤ v̄). (v̄, η) = (10⁻⁶, 0.1) is Theorem HT′.

Converted data. For γ_D ≤ 1 − μ_T and u′ + z₀ ≤ X\*: by (T4\*), ξ_e ≤ z₀/κ_z,
|T − n̂| ≤ K_tlκ_z^{−(1−μ_T)}(u′+z₀)^{1−μ_T} ≤ θ₀(u′+z₀)^{γ_D}, θ₀ := K_tlκ_z^{−(1−μ_T)}X\*^{1−μ_T−γ_D}. By (T5\*),
ε ≤ (z₀/c_zlo)^{2−2v}, so if 1 + γ_D ≤ (2−2v)(1−v/2) and z₀ ≤ c_zlo: |y₀| ≤ c_y(z₀/c_zlo)^{(2−2v)(1−v/2)} ≤
θ_y z₀^{1+γ_D}, θ_y := c_y c_zlo^{−(1+γ_D)} (with the Q3 form: since ε ≤ z₀, (z₀+ε)^{2−μ̄_T} ≤ 2^{2−μ̄_T}z₀^{2−μ̄_T}, so
θ_y := c_y2^{2−μ̄_T}(z₀^max)^{1−μ̄_T−γ_D}, if 1+γ_D ≤ 2−μ̄_T, z₀ ≤ z₀^max ≤ 1). And z₀ ≥ ε/ζ follows from c_zlo ε^{1/(2−2v)} ≥ ε/ζ.

### 4.2 Parameters, derived constants, side conditions

Free: core parameters p (γ, R, m, s₀, f, κ₁, c_A, K_R, K_f, K_ε, η, q, A₀; d = 1/(1−v₀), δ₁ = e^{2v₀/(1−v₀)},
ν = c_amp v₀ — old core: γ, R), and ω̄ ∈ (0,1/2], k_fac ≥ 1, δ₀ ∈ (0, R/2].
Derived: ζ = (1−ω̄²)^{1/2} − v₀, η_N = 1.375v₀/ζ, γ_D := γ + ν + η_N (= γ₁ = γ_h), stage-A parameters p_A := p with
γ ↦ γ_D; W₁ := c_AK_RR/κ₂; U_A := W₁ + δ₀ + R; U_E := W₁ + R; D := (κ_adv W₁ + ε)/(1−v₀);
ε_\* := min(ε_T, R/K_ε, (R/(100c_zhi))²); z₀ ≤ c_zhi ε^{1/2} =: z₀^max; X\* := U_E + z₀^max + D; G_f := W₁ + ε + δ₀;
Lemma Q2.H constants with (γ₁, R₁, m₁, …) := stage-A values and γ_h := γ_D; Theorem Q2.D constants with γ := γ_D,
k := k_fac·4(1+δ_t)/ζ; and
(TS) := (1 + D/(kR))^{η_N}[C₀R^{a′} + v₀(c_nΘ_b + c_βΘ_p)R^{γ_D}].
Side conditions (all checked by the script, left sides non-decreasing in v and ε):
* [main core] (P0)–(P7) with U = U_max; [main cor] (C1)–(C6) and C₀λ₀^{a′} ≤ 1 (old: R ≤ min(λ₀/32, c_sep/16),
  C₀R^{a′} ≤ γ/400, γ + 22v ≤ a′, and the old ranges);
* [stage A core] the same for p_A with U = U_A and c_sep^A := min(c_sep, κ₂(U_min − U_A));
* U_min − U_A ≥ W₁; H: G_f ≤ G_T, δ₀ ≤ R/2, σ̄ ≤ 1/2, ρ\* ≥ ε, m₁² < 2, γ_D ≤ 1 − μ, U_A ≥ W₁ + 2ε + δ₀;
* D: X\* ≤ 1, ζ > 0, θ₀X\*^{γ_D} ≤ ω̄, θ_yX\*^{γ_D} ≤ ω̄, ω₀ ≤ ω̄, ω_T ≤ 1/2, η ≤ γ_D/2, γ_D ≤ 1−μ_T, γ_D < 1,
  1 + γ_D ≤ (2−2v)(1−v/2), c_zlo ε^{1/(2−2v)} ≥ ε/ζ, z₀^max ≤ c_zlo, U_E ≤ G_T;
* TW: γ_D ≤ a′; (TS) ≤ s₀m·min(1, K_f/K_R)^ν; max(K_f, K_R)R ≤ U_min − U_E − W₁ − ε; (1+δ_t)LHS(P7) < κ₁;
* v₀ ≤ v_T, ε_\* ≤ ε_T.
T₀ := T₂ + κ_adv U_max/(1−v₀). With Q3's parametric data, (v̄, η) are additional free parameters and v₀ ≤ v̄ = v_T.

### 4.3 Statement

**Theorem Q2.M.** Assume (H_T\*) and let the parameters satisfy all side conditions of §4.2 at (v₀, ε_\*). For every
v ∈ (0, v₀] and ε ∈ (0,1), the path P_{v, min(ε,ε_\*)} (design T on [0, t_td]; Construction C on the working front
from (t_td, u=0) cut at u = U; constant after it stops) is fixed in advance, starts at 0, has speed ≤ 1, and every
direction is seen by time T₀. Status: PROVED for core = old; PROVED modulo [End\*] and (F1)–(F4) for End\* for
core = End\*.

### 4.4 Proof

Let ε ≤ ε_\* (a path that sees with radius ε_\* sees with every larger radius; true candidates do not depend on ε),
v ≤ v₀. All side conditions hold at (v, ε) by monotonicity. Labels u, u′, λ refer to t_td.

1. *Stage A.* On [0, U_A]: (T1\*) gives (E1); a pair in [0,U_A] with λ > λ₀ has u′_b ≥ U − U_A, so by (T2)
   c ≥ min(c_sep, κ₂(U_min − U_A)) = c_sep^A: (E2). Corollary End\* (old: cor:End with Remark E-restart(1)) applies with
   (a′, C₀, λ₀, c_sep^A), U = U_A, parameters p_A (γ_D + ν ≤ γ + 2ν + η_N ≤ a′ is (C5) for p_A). So End\*(a),(b),(d),(e)
   hold for the construction cut at b_A := label U_A, on working fronts by Lemma T2-W(d).
2. *Common legs, t_w, D.* While u_{a_j} < W₁: l_{t_j}(a_j, b_A) ≥ U_A − u_{a_j} > δ₀ + R > ε, so a_{j+1} is the same
   for the cuts at b_A and at b_E (maximality rule), the leg is non-final in both (as in Lemma T2-StA(b)). Each advances
   by ≥ ε/κ_adv: j_w exists, u_{a_{j_w}} ∈ [W₁, W₁+ε], at most κ_adv W₁/ε + 1 legs of duration ≤ ε/(1−v):
   D := t_w − t_td ≤ (κ_adv W₁ + ε)/(1−v). By causality P|[t_td, t_w] is the stage-A path.
3. *Heading.* Lemma Q2.H with n̂ of (H_T), K_fw (T3\*), G_f ≤ G_T: |P′ − n̂| ≤ h(τ) on [t_td, t_w] (speed 1 on
   non-final legs).
4. *Departure.* Apply Theorem Q2.D to the tail arc {u′ ≤ U_E} labelled by u′, with t_E := t_td, E := label U,
   û := −n̂, z₀, y₀ of (T5) (x_E − P = −(z₀n̂ + y₀n̂^⊥) = z₀û + y₀û^⊥), D of step 2, γ := γ_D, θ₀, θ_y of §4.1, θ_h,
   ω₀ of step 3. (D0),(D1): §4.1 (the tangent in the direction of increasing u′ is −T, |−T − û| = |T − n̂|,
   U_E ≤ G_T). (D2): |û × P′| = |n̂ × (P′ − n̂)| ≤ h, P′·û = −1 + |P′−n̂|²/2 < 0 (h ≤ ω̄ ≤ 1/2). (D3): side conditions.
5. *(TW).* A tail pair (a,b) of Q2.E′ (u′_b < W₁, ε/2 ≤ λ ≤ R) lies in the departure arc (u′_a < W₁ + R = U_E); in
   departure labels its first point is b, g̃ = u′_b + z₀. At t_w (τ = D): l ≤ (1+δ_t)λ (D(iv)); g_w = u_a − u_{a_{j_w}} ≥
   U − U_E − W₁ − ε ≥ max(K_f,K_R)R ≥ K_fλ, so min(g_w, K_RR) = K_RR. By D(v) with N(t_td) ≤ C₀λ^{1/2+a′} (T1\*) and
   1 + D/(kλ) ≤ (R/λ)(1 + D/(kR)) (λ ≤ R):
     N(t_w) ≤ (1+D/(kR))^{η_N}(R/λ)^{η_N}λ^{1/2}[C₀λ^{a′} + vKλ^{γ_D}],   K := c_nΘ_b + c_βΘ_p.
   The target is s₀Mλ^{1/2+γ}min(1, K_fλ/(K_RR))^ν ≥ s₀mR^{−γ}λ^{1/2+γ}min(1,K_f/K_R)^ν(λ/R)^ν. The ratio of the bound
   to this target is ≤ (1+D/(kR))^{η_N}[C₀R^{a′}(λ/R)^{a′−η_N−γ−ν} + vKR^{γ_D}(λ/R)^{γ_D−η_N−γ−ν}]/(s₀m min(1,K_f/K_R)^ν)
   ≤ (TS)/(s₀m min(1,K_f/K_R)^ν) ≤ 1, since both exponents are ≥ 0 (γ_D = γ + ν + η_N ≤ a′) and λ ≤ R.
   (PT) is the side condition with δ_T := δ_t.
6. *Q2.E′ on the whole arc.* (S1′): a good pair with λ ≤ λ₀ has c ≥ λ(1 − ½(C₀λ^{a′})²) ≥ c_A min(λ, K_RR) by (C2),
   (C3) (λ ↦ λ − ½C₀²λ^{1+2a′} is concave, so its minimum on [K_RR, λ₀] is at an end); with λ > λ₀, by (T2),
   c ≥ min(c_sep, κ₂(u_a + u′_b)) ≥ min(c_sep, κ₂W₁) ≥ c_AK_RR (C4, definition of W₁). (S2′) for all pairs: as in the
   proof of Cor. End\* from (T1\*) and (C6). (S3\*): ε ≤ R/K_ε. (P0)–(P7) with U ≤ U_max (monotone in U).
   U ≥ 2W₁ + R + ε: from the far condition. Q2.E′ (on a working front: its proof uses only what Lemma T2-W(d) lists)
   gives: the construction stops at T_stop ≤ t_td + κ_adv U/(1−v) ≤ T₀, every true label's direction of [0, U] is seen.
7. *Directions.* By (T0) every other direction is seen during [0, t_td]. The path is design T on [0, t_td], 1-Lipschitz
   afterwards (Lemma B-C(0)), constant after T_stop, and depends only on (v, ε). ∎

**Corollary Q2.X (exact capture).** As cor:Exact of sec_T2 with (v₀, T₀) of Theorem Q2.M (the proof is unchanged:
Lemma A41 with D_N dyadic, ε_N = 2^{−N}ε_\*).

-------------------------------------------------------------------------------------------------------------------
## 5. What is not claimed / open items
* For core = End\*: Theorem End\*, Corollary End\* and (F1)–(F4) for End\* are Q1's (not refereed at the time of
  writing); the script replicates the INTERIM formulas of Q1-1 and must be re-run against code/Q1/optimise.py.
* Q3's extended touch-down data are used only PROVISIONALLY (mapping of code/Q3/constants.py names, see the script).
* Lemma T2-A (passive), Prop. T2-I (hand-over), Lemma T2-StA, thm:T2-D, lem:T2-H are not used any more.
