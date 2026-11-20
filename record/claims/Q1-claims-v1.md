# Q1-claims (version 1): Theorem End* and Corollary End* — the end theorem with every constant a parameter

Stream Q1, round 7. Author: Q1 (restarted instance). Status labels: **PROVED** (every step written below or cited
verbatim with label), **NUMERICAL** (explicit inequalities checked by `code/Q1/optimise.py` in 50-digit mpmath),
**CONJECTURE** (none in this file).

Sources: `paper/sec_E.tex` (thm:End, cor:End, lem:E-facts, Construction C cut at b_E), `paper/sec_B.tex`
(lem:B-V, lem:B-VC, lem:B-1, lem:B-2, lem:B-3, lem:B-4, lem:B-C, thm:R and the Claim in its proof, Steps 1–5 of the
proof of thm:Bulk, which thm:End quotes). Referee reports RP7-1, RP7-2 (constants of thm:End all recomputed there).

**What is new against thm:End.** Nothing in the method. Every numerical threshold of the proof of thm:End is a parameter;
the side conditions (P0)–(P7) are exactly what each step of the proof needs; three estimates are written with finer
bookkeeping (the frozen-direction identity lem:E-facts(b) in place of 2N²+2l|Δe|² in (E-mu); the far forcing for
g > ηR integrated against the gap via (E-1c) instead of over the whole time T_B; Term II of the near step split into a
part from the sub-arc and a part from the base point). Each of these is written out in full below. The cap γ ≤ 1/4 and
the exponent halving of cor:End are removed (only γ + ν ≤ a′, γ + ν < 1 is used).

Every step of the proof of thm:End and of the quoted steps of thm:Bulk whose constants change is written out in full
(§4). Statements cited **verbatim** (constants unchanged, hypotheses checked) are listed in §4.0.

---------------------------------------------------------------------------------------------------------------------

## 1. Parameters and derived constants

Setting, notation and construction exactly as in sec_E §"The bulk bootstrap on an arc that ends": d = 1 (unit vision
distance), the field F of sec_B, A = DF, a*(ρ) = 1/ρ (ρ ≥ ε), 2/ε (ρ < ε), virtual candidates x_θ, r = x − P, ρ = |r|;
l, c, e, E, N = (2E)^{1/2}; μ = v/(1−v). Construction C from (t_s, a_s), cut at the end label b_E (b_E − a_s < 2π,
P(t_s) = x_{a_s}(t_s), P(0) = 0). Labels u ∈ [0,U]: arclength at time t_s along [a_s, b_E] from x_{a_s},
U := l_{t_s}(a_s, b_E); λ := u_b − u_a (label length).

**Free parameters** (old value of thm:End in brackets):

| name | range | role | old |
|---|---|---|---|
| γ | γ > 0, γ + ν < 1 | invariant exponent, N ≤ Mλ^{1/2+γ} | ≤ 1/4 |
| R | (0, 1] | scale cap of the family | same |
| m | m > 0; M := m R^{−γ} | normalisation of (J2) | γ/50 |
| s0, f | 0 < s0 ≤ f < 1 | start factor in (S2*); far-pair factor | 1/8, 3/8 |
| κ1 | (1, 4/3] | (J1): l ≤ κ1 λ | 9/8 |
| c_A | (0, 1] | chord constant in (S1*), (CA*) | 1/2 |
| K_R | ≥ 1 | separation scale K_R R in (S1*) | 32 |
| K_f | ≥ 3 | far iff g ≥ K_f λ | 64 |
| K_ε | ≥ 3/2 | (S3*): ε ≤ R/K_ε | 64 |
| η | 0 < η ≤ K_f/(K_f+1) | far forcing via the tilt lemma iff g ≤ ηR | 1/2 |
| q | > 1 | ratio of the chains in the tilt lemma | 2 (with ratio-3 bound) |
| ν | ≥ 0 | amplification exponent bound | 22v |
| d, δ1, A0 | ≥ 1 | majorants: leg duration ≤ dε; e^{2μ} ≤ δ1; far prefactor | 2, 2, 2 |

**Derived constants** (all explicit; q1const.py implements exactly these lines):

```
M      := m R^{−γ}
χ      := κ1 d                                         (gap–time constant of (E-1c*))
c_6    := (1+δ1)/c_A                                   ((E-star*); old 6)
c_t(r) := (κ1^{1/2} r^{1/2+γ} + m/2)/c_A               (one-step tilt, ratio ≤ r)
S_q    := 1/(1 − q^{−γ})
C_A    := S_q c_t(q)          (tilt constant, J ⊂ I with the same LEFT end)
C_B    := C_A + c_t(3)        (tilt constant, J ⊂ I with the same RIGHT end)
C_TL   := C_A + C_B           (general tilt constant; old 16.5/γ)
CμA    := 1 + κ1 C_A² ,   C1A := (κ1 CμA)^{1/2}
c_ρ    := c_A − (2δ1+κ1)/K_f ,   c_R := c_A K_R − δ1/K_ε − κ1
K_1    := c_ρ K_f/κ1 ,  K_2 := c_R/κ1 ,  a_i := 1 + 1/K_i + 2/K_i²   (old a = 1.375)
c_amp  := a_1 χ / c_ρ                                  (old 22)
B_2U   := 2 κ1^{3/2} (1+1/K_2)/c_R²
B_2η   := 2 κ1^{3/2} (1+1/K_1)/c_ρ² · (χ/η + d/(K_ε η²))
r_f    := 1 + 1/(K_f − 2) ,   C_p := κ1 [ c_t(r_f) + C_B (1+1/K_f)^γ ] ,   B_3 := 2 κ1^{3/2} C_p / c_ρ³
Ψ      := 2 + log min(K_f,K_R) + (K_f − K_R)^+ / K_R
τ_I    := d (κ1 c_6 + 2) + c_6 χ Ψ
τ_α    := d/c_6 + χ (2 + log K_f)
τ_β    := 2^γ [ 2d + χ ( 3/4 + (K_f^γ − 1)/(2γ) ) ]
τ_n    := χ K_f + 2d
k_0    := max( C1A , κ1 2^γ C_A )
ι      := 1 if K_f + 1 > K_R, else 0
D_I    := CμA τ_I
D_IIs  := c_6² C1A² τ_α + 2 c_6² κ1 C_TL C1A τ_β + 4 d c_6 C1A k_0
D_IIl  := (c_6 (K_f+1)^γ / m) [ C1A τ_α + ι κ1^{1/2} τ_n / K_R ]
B_5    := (2/c_ρ) [ (C_p + κ1^{1/2} K_f^{−1−γ})² / c_ρ² + K_f^{−2γ} ]
I_5    := χ (η + 1/K_ε)^{2γ} / (2γ) + d max(1, (2/K_f)^{1−2γ}) K_ε^{−2γ}
X_far  := v [ χU/(c_R R) + ( d/(K_ε η) + χ log(K_R/η) ) / c_ρ ]
r_1    := R (c_A/κ1 − δ1/K_ε)
```

## 2. Hypotheses

**Start hypothesis (ST\*)** at t_s:
- (S1\*) c(a,b;t_s) ≥ c_A min(λ, K_R R) for all pairs in [a_s,b_E] with λ ≥ ε/2;
- (S2\*) N(a,b;t_s) ≤ s0 M λ^{1/2+γ} · min(1, K_f λ / min(u_a, K_R R))^ν for all pairs with ε/2 ≤ λ ≤ R (last factor 1 if
  u_a = 0);
- (S3\*) ε ≤ R/K_ε.

**Side conditions.**
```
(P0) the ranges of the table of §1, and 0 < v < 1
(P1) 1/(1−v) ≤ d ,   e^{2v/(1−v)} ≤ δ1
(P2) c_ρ K_f ≥ 2 ,   c_R K_ε ≥ 1 ,   c_6 ≤ K_R K_ε
(P3) c_amp v ≤ ν
(P4) v [ 2 a_1 d/(c_ρ K_f) + a_2 χ U/(c_R R) ] ≤ log A0
(P5) A0 [ s0 + max(1, K_R/K_f)^ν (v/m)( B_2U χU/R + B_2η ) + B_3 K_f^{γ−1} ( 2d/K_f + χ/(1−γ−ν) ) v ] ≤ f
(P6) f² + 2 v [ D_I + max(D_IIs, D_IIl) ] < 1
(P7) exp( X_far + B_5 I_5 v m² ) + v κ1 τ_I < κ1
(Pc) [only for conclusion (c)]   m² ≤ 1/2   and   r_1 > 0
```
*Monotonicity.* With (γ,R,m,s0,f,κ1,c_A,K_R,K_f,K_ε,η,q,ν,d,δ1,A0) fixed, every left side is non-decreasing in v and in U
(by inspection: v and U enter only as positive factors, via exp, or via 1/(1−v)); ε enters only through (S3*). So
(P0)–(P7) for (v0, U_max) imply them for all v ≤ v0, U ≤ U_max.

## 3. Statements

**Theorem End\*.** Assume (ST\*) and (P0)–(P7). Then:
- **(a)** For every t from t_s until the construction stops and every pair of the family F(t):
  (J1\*) l_t(a,b) ≤ κ1 λ (in fact ≤ L_J λ, L_J := exp(X_far + B_5 I_5 v m²) + vκ1τ_I);
  (J2\*) N(a,b;t) ≤ M λ^{1/2+γ}. Moreover (CA\*) c(a,b;t) ≥ c_A min(λ, K_R R) for all pairs with λ ≥ ε/2, t ≥ t_s.
- **(b)** Every non-final leg advances the base label by u_{a_{j+1}} − u_{a_j} ∈ [ε/κ1, ε]. The construction stops at a
  leg start T_stop = t_J with J − j_s ≤ κ1U/ε and T_stop ≤ t_s + κ1U/(1−v); l_{T_stop}(a_J, b_E) ≤ ε; every label of
  [a_s, b_E] has been seen by T_stop; |P(T_stop) − x_{b_E}(T_stop)| ≤ ε.
- **(c)** If also (Pc): for every non-final leg j+1 > j_s and every t in it, (F_b) and (S) of thm:R hold with b* = b_E,
  γ, r_0 = R, c_0 = m²/2, c_1 = 0, r_1; and K̃(t) := ∫_{a_{j+1}}^{b_E} T·AT ds ≤ 16δ1 + 2m²(1+1/γ) + 2δ1κ1U/r_1.
- **(d)** (Tilts) At any time t ≤ T_stop, for pairs J ⊂ I of F(t): |e_J − e_I| ≤ C_TL M λ_I^γ = C_TL m (λ_I/R)^γ; with
  C_A (resp. C_B) in place of C_TL if J and I have the same left (resp. right) end.
- **(e)** (E-star\*) For t in leg j+1 and a label s with w_s := u_s − u_{a_j} ≥ 0: ρ_s ≥ c_A min(w_s, K_R R) − δ1ε, and
  max(ρ_s, ε) ≥ min(w_s, K_R R)/c_6.

No constant depends on ε. The invariants at time t depend only on P|[0,t] (causality, rem:E-B(4), unchanged).

**Corollary End\*.** Data (a′, C0, λ0, c_sep) with a′ ∈ (0,1], C0 > 0, λ0 ∈ (0,1], c_sep > 0, and hypothesis (ST_end) of
sec_E verbatim: (E1) N(a,b;t_s) ≤ C0 λ^{1/2+a′} for pairs in A = [a_s,b_E] with ε/2 ≤ λ ≤ λ0; (E2) c(a,b;t_s) ≥ c_sep for
pairs in A with λ > λ0. Let U ≤ U_max. If the parameters satisfy (P0)–(P7) with U = U_max and
```
(C0) C0 λ0^{a′} ≤ 1
(C1) R ≤ λ0
(C2) 1 − ½ (C0 min(K_R R, λ0)^{a′})² ≥ c_A
(C3) if K_R R < λ0:   λ0 (1 − ½ (C0 λ0^{a′})²) ≥ c_A K_R R
(C4) c_sep ≥ c_A K_R R
(C5) γ + ν ≤ a′
(C6) C0 R^{a′} ≤ s0 m min(1, K_f/K_R)^ν
```
and ε ≤ R/K_ε, then (ST\*) holds, hence (a), (b), (d), (e) of Theorem End\*, and (c) if also (Pc).

(Against the interim statement of reports/Q1-1.md: (C1)–(C3) are weakened — K_R R ≤ λ0 is no longer required.)

---------------------------------------------------------------------------------------------------------------------

## 4. Proof of Theorem End*

### 4.0 Cited verbatim (constants unchanged; hypotheses checked)

| item | where used | hypothesis check |
|---|---|---|
| lem:B-V (i)–(iii) | throughout | none |
| lem:B-VC (a),(b),(c) | monotonicity of l, c; "seen" | P(0) = 0 (sec_E) |
| lem:B-1(i), lem:B-2 (i)–(iii) | l′, E′ | none |
| lem:B-3 (a), (c) | Steps 3–5 | (c): ρ_m ≥ ε, checked in Step 3 |
| lem:B-4 (a), (b) | tilt lemma; Claim of thm:R | none |
| lem:B-C (0),(2),(3),(4) for the cut construction | legs | sec_E, "Construction C … cut at b_E" (verbatim) |
| lem:E-facts (a), (b) | (E-mu*), Term II | none |
| Claim in the proof of thm:R (with K_T = 0, b* = b_E, 2π ↦ b_E in R_j, K̃) | (c) | as in sec_E proof of (c) |
| rem:E-B(4) causality | scope | unchanged |
| the continuity scheme of thm:End(a) | (a) | written out in 4.2 with parametric bounds |

Lemma B-3(e) is restated with a general ratio in Lemma 4.1 (its proof is the proof of B-3(e)).

### 4.1 Three auxiliary lemmas

**Lemma 4.1 (Duhamel form of B-3(c), general ratio).** Fix labels a < b. If on [t_1,t_2] the convex hull of the arc stays at
distance ρ_m(t) ≥ ε from P, then with α := (v/ρ_m)(1 + l/ρ_m + 2l²/ρ_m²) and β := 2v l^{3/2}|p_a|/ρ_m³,
N(t_2) ≤ exp(∫_{t_1}^{t_2} α) N(t_1) + ∫_{t_1}^{t_2} exp(∫_t^{t_2} α) β(t) dt.
In particular if ρ_m ≥ K l then α ≤ (1 + 1/K + 2/K²) v/ρ_m.

*Proof.* By lem:B-3(c), E′ ≤ αN² + βN. With N_η := (N² + η²)^{1/2}, η > 0: N_η N_η′ = E′ ≤ αN_η² + βN_η, so
N_η′ ≤ αN_η + β; variation of constants, then η → 0. (Literally the proof of lem:B-3(e), with the bound 1 + 1/4 + 2/16
not yet inserted.) ∎

**Lemma 4.2 (gap–time integrals; replaces (E-1c)).** Assume that every non-final leg advances the base label by at least
ε/κ1 and lasts at most dε (shown in Step 1 under the continuity hypothesis). Fix a label a and a time interval 𝒯 on
which the pair under consideration is in the family; g(t) = u_a − u_{a_{j(t)}} is constant on each leg and the attained
values (one per leg) are spaced by ≥ ε/κ1.
- (i) If h ≥ 0 is non-increasing on [g_min, ∞), where g_min is the smallest attained gap ≥ g0 in 𝒯, then
  ∫_{t∈𝒯: g(t) ≥ g0} h(g(t)) dt ≤ dε h(g_min) + χ ∫_{g_min}^∞ h(g) dg.
- (ii) If h ≥ 0 is non-decreasing on [0, G] and all attained gaps in 𝒯 are ≤ G, then ∫_𝒯 h(g(t)) dt ≤ χ ∫_0^{G+ε/κ1} h.
- (iii) The number of legs of 𝒯 with gap in [0, x) is ≤ κ1 x/ε + 1.

*Proof.* (i) Order the attained gaps ≥ g0 as g_1 > g_2 > … > g_n = g_min. For i < n: g_i − ε/κ1 ≥ g_{i+1} ≥ g_min,
and h(g_i) ≤ (κ1/ε) ∫_{g_i − ε/κ1}^{g_i} h (h non-increasing); the intervals (g_i − ε/κ1, g_i] are disjoint and lie in
[g_min, ∞). Each leg lasts ≤ dε, so the integral is ≤ dε Σ_i h(g_i) ≤ dε h(g_min) + dκ1 ∫_{g_min}^∞ h.
(ii) Same with h(g_i) ≤ (κ1/ε) ∫_{g_i}^{g_i+ε/κ1} h, intervals disjoint in [0, G + ε/κ1]. (iii) Spacing. ∎

**Lemma 4.3 (two elementary integrals).** For λ > 0 put h1(z) := ∫_z^∞ min(λ,y) y^{−2} dy and h3(z) := ∫_z^∞ min(λ,y) y^{−3} dy.
Then h1(z) = 1 + log(λ/z) for z ≤ λ, = λ/z for z > λ; h3(z) = 1/z − 1/(2λ) for z ≤ λ, = λ/(2z²) for z > λ. Both are
non-increasing; z·h1(z) ≤ λ for all z > 0; ∫_0^{Kλ} h1 = λ(2 + log K) for K ≥ 1; and z h3(z) = G(z/λ) with G(x) = 1 − x/2
(x ≤ 1), 1/(2x) (x > 1).

*Proof.* Direct integration. z h1(z) = λ x(1 + log(1/x)) ≤ λ for x = z/λ ≤ 1 (the function x(1 − log x) increases on
(0,1] to 1), and = λ for z > λ. ∫_0^λ (1 + log(λ/z)) dz = 2λ, ∫_λ^{Kλ} λ/z dz = λ log K. ∎

### 4.2 Step 0: consequences of (P1), (S1*); the continuity argument

*Legs.* By lem:B-C(2) every non-final leg lasts ≤ c(a_j,a_{j+1};t_j)/(1−v) ≤ ε/(1−v) ≤ dε (P1). By lem:B-C(4), for t in
leg j+1, |P(t) − x_{a_j}(t)| ≤ e^{2μ}ε ≤ δ1 ε (P1), and P(t) ∈ [x_{a_j}(t), x_{a_{j+1}}(t)] (lem:B-C(2)).

*(CA\*).* Chords are non-decreasing in t (lem:B-VC(b)), so (S1*) gives c(a,b;t) ≥ c_A min(λ, K_R R) for t ≥ t_s, λ ≥ ε/2.
Lengths are non-decreasing: l_t(a,b) ≥ λ.

*Family.* As in sec_E with 64 ↦ K_f: for t in leg j+1, F(t) = pairs (a,b) with u_b ≤ U, ε/2 ≤ λ ≤ R, (a = a_j or
a ≥ a_{j+1}); at a switching time t_j (j > j_s), F(t_j) is the family of leg j (it contains that of leg j+1). Gap
g := u_a − u_{a_j} ≥ 0; far iff g ≥ K_f λ, near otherwise. F(t) shrinks and g is non-increasing in t.

*Continuity argument.* Let T_end be the stopping time (or ∞), t* the supremum of t′ ≤ T_end such that (J1*), (J2*) hold
for all t ∈ [t_s, t′] and all pairs of F(t). At t_s, l = λ < κ1 λ and N ≤ s0 M λ^{1/2+γ} < M λ^{1/2+γ} (s0 < 1). We prove
(Steps 1–5):

> **(Imp\*)** if (J1*), (J2*) hold on [t_s, t*), then for every t ≤ t* (t < ∞) and every pair of F(t):
> l_t ≤ L_J λ and E ≤ ½ θ M² λ^{1+2γ}, where L_J < κ1 by (P7) and θ := max(f², f² + 2v[D_I + max(D_IIs, D_IIl)]) < 1
> by (P0), (P6).

Given (Imp*), exactly as in thm:End(a): the bounds hold at t* by continuity; for t ∈ [t*, t*+δ], l_t ≤ e^{2vδ/ε} l_{t*}
and |E′| ≤ v∫|T−e||AT| ≤ (4v/ε) l, so E(t) ≤ ½θM²λ^{1+2γ} + δ(4v/ε)κ1λ·e^{2vδ/ε}; both stay below κ1λ resp.
½M²λ^{1+2γ} for some δ > 0 depending only on (v, ε, M, γ, κ1, θ, L_J), uniformly in the pair because λ ≥ ε/2;
F(t) ⊂ F(t*). With lem:B-C(0), t* = T_end. Below, (J1*), (J2*) ("family bounds") are assumed on [t_s, t*) and, by
continuity, at t*; all times are ≤ t*.

### 4.3 Step 1 (legs, the end, times, distances)

**(a) Dichotomy at a leg start t_j.** (α) If U − u_{a_j} ≥ ε/2, then leg j+1 is final or u_{a_{j+1}} − u_{a_j} ∈ [ε/κ1, ε].
(β) If U − u_{a_j} < ε/2, then l_{t_j}(a_j, b_E) ≤ ε, i.e. leg j+1 is final.

*Proof.* Always u_{a_{j+1}} − u_{a_j} ≤ l_{t_j}(a_j,a_{j+1}) ≤ ε. (α): the label s with u_s = u_{a_j} + ε/2 is ≤ U; the pair
(a_j, s) has λ = ε/2 ≤ R (K_ε ≥ 3/2) and first point a_j, so it is in F(t_j); (J1*) gives l_{t_j}(a_j,s) ≤ κ1ε/2 ≤ ε
(κ1 ≤ 2), so a_{j+1} ≥ s by maximality: the advance is ≥ ε/2. If leg j+1 is non-final, a_{j+1} < b_E and, by maximality
and continuity of l in the label, l_{t_j}(a_j,a_{j+1}) = ε; the pair (a_j,a_{j+1}) has ε/2 ≤ λ ≤ ε ≤ R and is in F(t_j),
so (J1*) gives ε ≤ κ1 λ: the advance is ≥ ε/κ1.
(β): for j = j_s, l_{t_s}(a_s,b_E) = U < ε/2. For j > j_s: leg j was not final, so (β) did not apply at t_{j−1} (by
induction it would have made leg j final); so (α) applied, λ_1 := u_{a_j} − u_{a_{j−1}} ∈ [ε/κ1, ε], and
l_{t_{j−1}}(a_{j−1},a_j) = ε. With λ_2 := U − u_{a_j} < ε/2, the pair (a_{j−1}, b_E) has λ_1 + λ_2 ∈ [ε/2, 3ε/2] ⊂ [ε/2, R]
(K_ε ≥ 3/2) and belongs to F(t_j) (family of leg j, first point a_{j−1}). By (J1*) and l_{t_j}(a_{j−1},a_j) ≥ ε
(lengths non-decreasing):
l_{t_j}(a_j, b_E) ≤ κ1(λ_1 + λ_2) − ε < κ1·(3ε/2) − ε ≤ ε, since κ1 ≤ 4/3. ∎

**(b)** Every non-final leg after j_s advances the base by ≥ ε/κ1 and the advances sum to ≤ U; so there are at most
κ1U/ε non-final legs after j_s, each lasting ≤ dε, and every time t considered satisfies t − t_s ≤ χU (=: T_B; also
≤ κ1U/(1−v)).

**(c)** Lemma 4.2 holds (its hypotheses are (b) and Step 0).

**(d) (E-star\*).** For t in leg j+1 and s with w_s ≥ 0: if w_s ≥ ε/2, ρ_s ≥ c(a_j,s;t) − |P − x_{a_j}| ≥
c_A min(w_s, K_R R) − δ1 ε by (CA*) and Step 0; if w_s < ε/2 the bound is negative (δ1 ≥ 1 > c_A/2), hence trivial.
Second form: put y := min(w_s, K_R R). If c_A y − δ1ε ≥ y/c_6 done; otherwise y(c_A − 1/c_6) < δ1ε, and since
c_A − 1/c_6 = c_A δ1/(1+δ1) > 0 this gives y < δ1ε(1+δ1)/(c_Aδ1) = c_6 ε, i.e. ε > y/c_6. ∎
This is conclusion (e).

### 4.4 Step 2 (tilt lemma): conclusion (d), and (E-mu*)

**One step.** Let J_1 ⊂ I_1 be family pairs (at the same time) with λ_{I_1} ≤ r λ_{J_1}. By lem:B-4(a), (J1*), (J2*) and
(CA*) (c(J_1) ≥ c_A λ_{J_1}, as λ_{J_1} ≤ R ≤ K_R R):
|e_{J_1} − e_{I_1}| ≤ [ (κ1λ_{J_1})^{1/2} M (rλ_{J_1})^{1/2+γ} + ½M²λ_{J_1}^{1+2γ} ] / (c_A λ_{J_1})
= M λ_{J_1}^γ [κ1^{1/2} r^{1/2+γ} + ½ M λ_{J_1}^γ]/c_A ≤ c_t(r) M λ_{J_1}^γ, since Mλ_{J_1}^γ ≤ MR^γ = m.

**Chains.** Let J = (a′,b′) ⊂ I = (a,b) be family pairs at t in leg j+1.
(A) b_k := min(u_{a′} + q^kλ_J, u_b), k = 0..k_1, b_{k_1} = b. The arcs (a′,b_k) have first point a′ (a family first
point), λ ∈ [λ_J, λ_I] ⊂ [ε/2, R]: family pairs. For k < k_1, λ(a′,b_k) = q^kλ_J ≤ λ_I and λ(a′,b_{k+1}) ≤ q λ(a′,b_k).
Sum of one-step tilts ≤ Σ_{k<k_1} c_t(q) M (q^kλ_J)^γ ≤ c_t(q) M λ_I^γ Σ_{i≥0} q^{−iγ} = C_A M λ_I^γ.
(B) If a′ > a: a° := a if a ≥ a_{j+1}, a° := a_{j+1} if a = a_j (then a′ ≥ a_{j+1}); a′_k := max(u_b − q^kλ(a′,b), u_{a°}).
The arcs (a′_k, b) start at labels ≥ a_{j+1} (or = a): family pairs; same sum ≤ C_A M λ_I^γ.
(C) If a = a_j ≠ a°: (a_{j+1}, b) ⊂ (a_j, b) with λ(a_j,b) ≤ λ(a_{j+1},b) + ε ≤ 3λ(a_{j+1},b) (advance ≤ ε,
λ(a_{j+1},b) ≥ λ_J ≥ ε/2): one step ≤ c_t(3) M λ_I^γ.
If J, I have the same left end only (A) is needed: C_A. Same right end: (B) and (C): C_A + c_t(3) = C_B. In general
C_A + C_B = C_TL. This is (d), with C_TL M λ_I^γ = C_TL m (λ_I/R)^γ. ∎

**(E-mu\*).** Let (a,b) ∈ F(t) and J ⊂ (a,b) a family pair with the same left end a (label length λ_J; a shorter arc
starting at a is enlarged to label length ε/2 inside (a,b) where used). By lem:E-facts(b) with û = e_ab:
∫_J |T − e_ab|² ds = N(J)² + c(J)|e_J − e_ab|² ≤ M²λ_J^{1+2γ} + κ1λ_J C_A² M² λ^{2γ} ≤ CμA M² λ^{2γ} λ_J,
and by Cauchy–Schwarz ∫_J |T − e_ab| ds ≤ (κ1λ_J · CμA M²λ^{2γ}λ_J)^{1/2} = C1A M λ^γ λ_J. ∎
(Old: 2N² + 2l|Δe|², C_μ = 2 + 2.25C_TL²; the exact identity removes the factor 2.)

### 4.5 Step 3 (far pairs): N ≤ f M λ^{1/2+γ}

Let (a,b) ∈ F(t) be far, t in leg j+1: g ≥ K_f λ ≥ K_f ε/2 > ε ≥ (advance), so a > a_{j+1}; since g is non-increasing
and F shrinks, the pair has been in the family and far on all of [t_s, t]. Put ĝ := min(g, K_R R).

**Distance.** The hull of the arc lies in the ball B(x_a, l), l ≤ κ1λ. By (E-star*) at s = a, ρ_m ≥ c_A ĝ − δ1ε − κ1λ.
- If g ≤ K_R R: with ε ≤ 2λ and λ ≤ g/K_f, ρ_m ≥ c_A g − (2δ1 + κ1)λ ≥ c_ρ g ≥ c_ρ K_f λ.
- If g > K_R R: with ε ≤ R/K_ε and λ ≤ R, ρ_m ≥ c_A K_R R − δ1R/K_ε − κ1R = c_R R ≥ c_R λ.
So ρ_m ≥ ε in both cases (c_ρK_f ≥ 2 and ε ≤ 2λ; c_R K_ε ≥ 1), and ρ_m ≥ K_1 l, resp. ≥ K_2 l (l ≤ κ1λ). Lemma 4.1 applies
on [t_s, t], with α ≤ a_1 v/(c_ρ g) while g ≤ K_R R and α ≤ a_2 v/(c_R R) while g > K_R R.

**Amplification.** Claim: for t_s ≤ τ ≤ t, exp(∫_τ^t α) ≤ A0 (min(g(τ), K_R R)/ĝ(t))^ν.
Proof: the times with g > K_R R form an initial segment (g non-increasing) of length ≤ T_B = χU: there
∫α ≤ a_2 vχU/(c_R R). On the times of [τ,t] with g ≤ K_R R (present only if g(t) ≤ K_R R), Lemma 4.2(i) with
h(g) = g^{−1}·1{g ≤ min(g(τ),K_R R)} (non-increasing; g_min = g(t) ≥ K_f λ ≥ K_f ε/2) gives
∫α ≤ (a_1v/c_ρ)[dε/g(t) + χ log(min(g(τ),K_RR)/g(t))] ≤ 2a_1 d v/(c_ρK_f) + c_amp v log(min(g(τ),K_RR)/g(t)).
By (P4) and (P3) (the ratio is ≥ 1), exp(∫α) ≤ A0 (min(g(τ),K_RR)/ĝ(t))^ν. ∎

**Forcing** β = 2v l^{3/2}|p_a|/ρ_m³, |p_a| = dist(P, line(x_a,x_b)).
- *g > ηR.* |p_a| ≤ ρ_a ≤ ρ_m + l ≤ ρ_m(1 + 1/K_i). If ηR < g ≤ K_RR: β ≤ 2vκ1^{3/2}λ^{3/2}(1+1/K_1)/(c_ρ g)²; if
  g > K_RR: β ≤ 2vκ1^{3/2}λ^{3/2}(1+1/K_2)/(c_R R)². Integrating: the second regime lasts ≤ χU; for the first, Lemma 4.2(i)
  with g0 = ηR, h(g) = g^{−2}1{g ≤ K_RR} (g_min ≥ ηR, ε ≤ R/K_ε) gives ∫ g^{−2} dt ≤ dε/(ηR)² + χ/(ηR)
  ≤ (d/(K_εη²) + χ/η)/R. Hence
  ∫_{g>ηR} β dt ≤ v λ^{3/2} [ B_2U χU/R² + B_2η/R ].
- *g ≤ ηR.* P ∈ [x_{a_j}, x_{a_{j+1}}], so |p_a| ≤ max_{a′∈{a_j,a_{j+1}}} dist(x_{a′}, line(x_a,x_b))
  = c(a′,a)|e_{a′a} × e_ab| ≤ c(a′,a)(|e_{a′a} − e_{a′b}| + |e_{a′b} − e_ab|). The pairs (a′,a), (a′,b), (a,b) are
  family pairs: first points a′ and a; λ(a′,a) ≥ g − ε ≥ (K_f/2 − 1)ε ≥ ε/2 (K_f ≥ 3); λ(a′,b) ≤ g + λ ≤ ηR(1 + 1/K_f) ≤ R
  (η ≤ K_f/(K_f+1)). Since λ(a′,b) = λ(a′,a) + λ and λ(a′,a) ≥ g − ε ≥ (K_f − 2)λ, the ratio is
  λ(a′,b)/λ(a′,a) ≤ 1 + 1/(K_f − 2) = r_f: one step, |e_{a′a} − e_{a′b}| ≤ c_t(r_f) M λ(a′,a)^γ ≤ c_t(r_f) M g^γ.
  (a,b) ⊂ (a′,b) have the same right end: |e_{a′b} − e_ab| ≤ C_B M (g+λ)^γ ≤ C_B(1+1/K_f)^γ M g^γ. And
  c(a′,a) ≤ κ1 λ(a′,a) ≤ κ1 g. So |p_a| ≤ C_p M g^{1+γ}, and with ρ_m ≥ c_ρ g (g ≤ ηR ≤ K_RR):
  β ≤ 2v(κ1λ)^{3/2} C_p M g^{1+γ}/(c_ρ g)³ = B_3 v M λ^{3/2} g^{γ−2}.

**Result.** g_2 := g(t), ĝ_2 := min(g_2, K_RR), g_s := u_a (gap at t_s). By Lemma 4.1 and the amplification claim:
N(t) ≤ A0 (min(g_s,K_RR)/ĝ_2)^ν N(t_s) + A0 (K_RR/ĝ_2)^ν ∫_{g>ηR} β + A0 ∫_{g≤ηR} (g(τ)/g_2)^ν β(τ) dτ.

*First term.* If g_2 ≤ K_RR: by (S2*), (min(g_s,K_RR)/g_2)^ν min(1, K_fλ/min(g_s,K_RR))^ν = (min(min(g_s,K_RR), K_fλ)/g_2)^ν
≤ (K_fλ/g_2)^ν ≤ 1; if g_2 > K_RR the ratio is 1 and the weight ≤ 1. So the term is ≤ A0 s0 M λ^{1/2+γ}.

*Second term.* (K_RR/ĝ_2)^ν ≤ max(1,K_R/K_f)^ν (R/λ)^ν (if g_2 ≤ K_RR: K_RR/g_2 ≤ (K_R/K_f)(R/λ) and the left side ≥ 1,
R/λ ≥ 1; if g_2 > K_RR it is 1). λ^{3/2}(R/λ)^ν = λ^{1/2+γ}λ^{1−γ−ν}R^ν ≤ λ^{1/2+γ}R^{1−γ} (γ + ν < 1, λ ≤ R). So the term
is ≤ A0 max(1,K_R/K_f)^ν v [B_2UχU/R + B_2η] R^{−γ} λ^{1/2+γ} = A0 max(1,K_R/K_f)^ν (v/m)(B_2UχU/R + B_2η) Mλ^{1/2+γ}.

*Third term* (present only if g_2 ≤ ηR; then g(τ) ≤ ηR on the integration set and min(g(τ),K_RR) = g(τ)).
It is ≤ A0 B_3 v M λ^{3/2} g_2^{−ν} ∫ g^{ν+γ−2} dt; h(g) = g^{ν+γ−2} is non-increasing (ν + γ < 2), and Lemma 4.2(i)
(g_min = g_2) gives ∫ ≤ dε g_2^{ν+γ−2} + χ g_2^{ν+γ−1}/(1−γ−ν). So the term is
≤ A0 B_3 v M λ^{3/2} g_2^{γ−1}[dε/g_2 + χ/(1−γ−ν)] ≤ A0 B_3 K_f^{γ−1}(2d/K_f + χ/(1−γ−ν)) v M λ^{1/2+γ}
(g_2 ≥ K_fλ, ε ≤ 2λ, γ < 1).

By (P5): N ≤ f M λ^{1/2+γ}, i.e. E ≤ ½ f² M² λ^{1+2γ} for far pairs. ∎

### 4.6 Step 4 (near pairs): E ≤ ½ θ M² λ^{1+2γ}

Let (a,b) ∈ F(t) be near (g < K_fλ). When it becomes near (at the switching time where its gap drops below K_fλ, Step 3
applies at that time as a far pair of the family of the previous leg), or at t_s if near there (E(t_s) ≤ ½s0²M²λ^{1+2γ}),
E ≤ ½ f² M² λ^{1+2γ}; E is continuous at switches. The near period is a final segment of [t_s, t]. We bound the increase
ΔE while near by integrating lem:B-3(a) with q̄ = 0: E′ ≤ I + II, I := v∫_a^b a*(ρ)|T−e|² ds, II := v∫_a^b |τ||q| ds,
e := e_ab, τ = T·e^⊥, q = e^⊥·Ae. Notation: σ_s := u_s − u_a, w_s = g + σ_s, D(s) := max(ρ_s, ε).

**Term I.** a*(ρ) = ε^{−1}1{ρ<ε} + ∫_{max(ρ,ε)}^∞ y^{−2}dy, so I = v[ω(ε)/ε + ∫_ε^∞ ω(y)y^{−2}dy] with
ω(y) := ∫_{s∈(a,b): ρ_s<y} |T−e|². For y ≥ ε: if (y + δ1ε)/c_A ≤ K_RR, then by (E-star*) ρ_s < y forces
w_s < (y+δ1ε)/c_A ≤ c_6 y, so these s lie in the sub-arc J_y of (a,b) starting at a with label length
max(min(λ, (y+δ1ε)/c_A − g), ε/2) ≤ min(λ, c_6 y), a family pair with left end a, and by (E-mu*)
ω(y) ≤ CμA M²λ^{2γ} min(λ, c_6y); if (y + δ1ε)/c_A > K_RR then c_6y > K_RR ≥ λ and trivially
ω(y) ≤ N² ≤ M²λ^{1+2γ} ≤ CμA M²λ^{2γ} min(λ, c_6y). Also ω(y) = 0 for y ≤ min ρ.
*Piece ω(ε)/ε:* non-zero only if min_{[a,b]} ρ < ε; then for some s, c_A min(w_s,K_RR) − δ1ε < ε, i.e.
min(w_s,K_RR) < c_6ε ≤ K_RR ((P2), ε ≤ R/K_ε), so g ≤ w_s < c_6ε. It is ≤ CμA M²λ^{2γ} min(λ,c_6ε)/ε.
*Piece ∫:* with ρ̄ := max(ε, min ρ) it is ∫_{ρ̄}^∞ ω y^{−2} ≤ CμA M²λ^{2γ}∫_{ρ̄}^∞ min(λ,c_6y)y^{−2}dy
= CμA M²λ^{2γ} c_6 h1(c_6ρ̄) (substitute z = c_6y). Now c_6ρ̄ ≥ c_6ε and, by (E-star*) for s ∈ [a,b] (w_s ≥ g),
c_6ρ̄ ≥ min(g, K_RR) ≥ min(g, K_Rλ). So c_6ρ̄ ≥ z(g) := max(c_6ε, min(g, K_Rλ)), non-decreasing in g, and
h1(c_6ρ̄) ≤ h1(z(g)) =: h̄(g), non-increasing in g.
*Time integral.* Piece 1: by Lemma 4.2(iii) at most κ1c_6 + 1 legs have g < c_6ε, each ≤ dε: contribution
≤ (κ1c_6+1) dε·min(λ,c_6ε)/ε ≤ d(κ1c_6+1)λ (in units v CμA M²λ^{2γ}). Piece 2: Lemma 4.2(i) (g0 = 0; h = c_6h̄ times
1{g < K_fλ}, non-increasing) gives ≤ c_6[dε h̄(g_min) + χ∫_0^{K_fλ} h̄] ≤ c_6 dε h1(c_6ε) + c_6χ∫_0^{K_fλ} h1(min(g,K_Rλ))dg
≤ dλ + c_6χλΨ, by Lemma 4.3 (c_6ε h1(c_6ε) ≤ λ; ∫_0^{min(K_f,K_R)λ} h1 = λ(2 + log min(K_f,K_R)), and on
[K_Rλ, K_fλ] (if K_f > K_R) h1(K_Rλ) = 1/K_R). Total:
∫_near I dt ≤ v CμA τ_I M² λ^{1+2γ} = v D_I M²λ^{1+2γ}.

**Term II.** By lem:B-V(iii), |q(s)| ≤ |p(s)|/D(s)², p(s) := (x_s − P) × e. Write p(s) = (x_s − x_a)×e + p_a,
p_a := (x_a − P)×e. Since x_s − x_a = ∫_a^s T and e×e = 0, |(x_s − x_a)×e| ≤ ∫_{(a,s)}|T−e| ≤ C1A Mλ^γ max(σ_s, ε/2)
by (E-mu*). Since P is a convex combination of x_{a_j}, x_{a_{j+1}}, |p_a| ≤ max_{a′∈{a_j,a_{j+1}}} |(x_a − x_{a′})×e|.
Let Ψ_τ(y) := ∫_{s∈(a,b): w_s<y} |τ| ds. For y ≤ g it is 0; for y > g, {w_s < y} is the sub-arc from a of label
length min(λ, y−g), so by (E-mu*) (|τ| ≤ |T−e|), Ψ_τ(y) ≤ C1A Mλ^γ min(λ, max(y−g, ε/2)) ≤ C1A Mλ^γ min(λ, y) for
y ≥ ε/2.

*Short case:* (K_f + 1)λ ≤ R. Then w_s ≤ g + λ < (K_f+1)λ ≤ R ≤ K_RR, so D(s) ≥ max(w_s/c_6, ε) by (E-star*).

(i) Bound on |p_a|. *g = 0* (a = a_j): x_{a_j} = x_a lies on the line. If a_{j+1} ≤ b,
|(x_{a_{j+1}} − x_a)×e| ≤ ∫_{(a,a_{j+1})}|T−e| ≤ C1A Mλ^γ max(adv, ε/2) ≤ C1A Mλ^γ ε. If a_{j+1} > b, I_0 := (a_j,a_{j+1})
is a family pair (ε/κ1 ≤ λ_{I_0} ≤ ε ≤ R) containing (a,b) with the same left end, and
|(x_{a_{j+1}} − x_a)×e| = c(I_0)|e_{I_0} × e_ab| ≤ c(I_0)|e_{I_0} − e_ab| ≤ κ1ε · C_A M ε^γ ≤ κ1 2^γ C_A M λ^γ ε
(ε ≤ 2λ). So |p_a| ≤ k_0 Mλ^γ ε.
*g > 0* (a ≥ a_{j+1}; g ≥ advance ≥ ε/κ1 ≥ ε/2). For a′ ∈ {a_j, a_{j+1}}, g′ := u_a − u_{a′} ≤ g. If g′ = 0 the term is
0. If g′ ≥ ε/2: (a′,a), (a′,b), (a,b) are family pairs (λ(a′,b) = g′+λ ≤ g + λ < (K_f+1)λ ≤ R), and
|(x_a − x_{a′})×e| = c(a′,a)|e_{a′a}×e_ab| ≤ κ1 g′ (|e_{a′a} − e_{a′b}| + |e_{a′b} − e_ab|) ≤ κ1 g (C_A + C_B) M (g+λ)^γ.
If 0 < g′ < ε/2 (a′ = a_{j+1}): J_0 := (a′, label u_{a′}+ε/2) ⊂ (a′,b) is a family pair, (a′,a) ⊂ J_0, and by
Cauchy–Schwarz and lem:E-facts(b): |(x_a − x_{a′})×e| ≤ l(J_0)^{1/2}(N(J_0)² + c(J_0)|e_{J_0} − e_ab|²)^{1/2}
≤ (κ1ε/2)^{1/2}(ε/2)^{1/2} M [ (ε/2)^{2γ} + κ1 C_TL² (g+λ)^{2γ} ]^{1/2} ≤ (κ1^{1/2}ε/2)(1 + κ1C_TL²)^{1/2} M (g+λ)^γ
(|e_{J_0} − e_ab| ≤ |e_{J_0} − e_{a′b}| + |e_{a′b} − e_ab| ≤ C_TL M(g′+λ)^γ; ε/2 ≤ λ). Since ε ≤ κ1 g and
(κ1^{1/2}/2)(1 + κ1C_TL²)^{1/2} ≤ C_TL [⇔ κ1 ≤ C_TL²(4 − κ1²), true as κ1 ≤ 4/3 and C_TL ≥ c_t(3) ≥ 3^{1/2}], this is
≤ κ1 C_TL M (g+λ)^γ g. So |p_a| ≤ κ1 C_TL M (g+λ)^γ g.

(ii) Split. With max(σ_s, ε/2) ≤ c_6 D(s) (σ_s ≤ w_s ≤ c_6D; ε/2 ≤ D):
II ≤ v C1A Mλ^γ c_6 ∫|τ|/D + v|p_a| ∫|τ|/D² =: II_α + II_β.
1/D ≤ φ_1(w_s), φ_1(w) := c_6/max(w, c_6ε) = ∫_{max(w,c_6ε)}^∞ c_6 y^{−2}dy; 1/D² ≤ φ_2(w) := φ_1(w)² =
∫_{max(w,c_6ε)}^∞ 2c_6² y^{−3}dy. By Fubini, ∫|τ|φ_1(w_s)ds = ∫_{c_6ε}^∞ c_6y^{−2}Ψ_τ(y)dy and similarly for φ_2.
Put y_0 := max(c_6ε, g).
- II_α ≤ v C1A Mλ^γ c_6 · c_6 C1A Mλ^γ ∫_{y_0}^∞ min(λ,y)y^{−2}dy = v c_6² C1A² M²λ^{2γ} h1(y_0)
  ≤ v c_6²C1A² M²λ^{2γ} h2(g), h2(g) := h1(max(c_6ε, g)) (non-increasing).
- II_β, g = 0: Ψ_τ(y) ≤ C1A Mλ^γ y (y ≥ c_6ε ≥ ε/2), ∫_{c_6ε}^∞ 2c_6² y^{−2} dy = 2c_6/ε; so
  II_β ≤ v k_0 Mλ^γ ε · 2c_6 C1A Mλ^γ/ε = 2 c_6 C1A k_0 v M²λ^{2γ}.
- II_β, g > 0: ∫_{y_0}^∞ 2c_6² y^{−3} C1A Mλ^γ min(λ,y) dy = 2c_6²C1A Mλ^γ h3(y_0) ≤ 2c_6²C1A Mλ^γ h3(g); with (i),
  II_β ≤ 2c_6² κ1 C_TL C1A v M²λ^γ (g+λ)^γ g h3(g) = 2c_6²κ1C_TL C1A v M²λ^{2γ} (1+x)^γ G(x), x := g/λ (Lemma 4.3).
  Majorant: (1+x)^γ G(x) ≤ H(x) := 2^γ(1 − x/2) for x ≤ 1, (1+x)^γ/(2x) for x > 1; H is non-increasing (on x > 1,
  (1+x)^γ/x is decreasing as γ < 1; H is continuous at 1) and H(0) = 2^γ.
*Time integrals (short case).* II_α: Lemma 4.2(i) (g0 = 0, h = h2·1{g < K_fλ}): ≤ dε h1(c_6ε) + χ∫_0^{K_fλ}h1(g)dg ≤
dλ/c_6 + χλ(2 + log K_f) = τ_α λ (Lemma 4.3). II_β with g = 0: one leg, ≤ dε ≤ 2dλ. II_β with g > 0: Lemma 4.2(i)
(g0 ∈ (0, ε/κ1], h = H(g/λ)1{g < K_fλ}): ≤ dε 2^γ + χλ∫_0^{K_f} H ≤ 2^γ 2dλ + χλ 2^γ[3/4 + (K_f^γ − 1)/(2γ)] = τ_β λ,
using ∫_0^1 2^γ(1−x/2)dx = (3/4)2^γ and (1+x)^γ ≤ (2x)^γ on [1,K_f]: ∫_1^{K_f}(2x)^γ/(2x)dx = 2^{γ−1}(K_f^γ−1)/γ.
Total: ∫_near II dt ≤ v [c_6²C1A²τ_α + 2c_6²κ1C_TL C1A τ_β + 4dc_6C1A k_0] M²λ^{1+2γ} = v D_IIs M²λ^{1+2γ}.

*Long case:* (K_f + 1)λ > R. Use |p(s)| ≤ ρ_s ≤ D(s), so |q| ≤ 1/D(s). For w_s ≤ K_RR, 1/D ≤ φ_1(w_s); for w_s > K_RR,
1/D ≤ c_6/(K_RR) by (E-star*). Hence
II ≤ v∫|τ|φ_1(w_s) + v (c_6/(K_RR)) ∫_{w_s>K_RR}|τ| ≤ v c_6 C1A Mλ^γ h2(g) + v (c_6/(K_RR)) κ1^{1/2} Mλ^{1+γ}·1{g+λ > K_RR}
(∫_a^b|τ| ≤ ∫_a^b |T−e| ≤ (l N²)^{1/2} ≤ κ1^{1/2}Mλ^{1+γ}). The last indicator vanishes unless K_f + 1 > K_R (as g + λ <
(K_f+1)λ ≤ (K_f+1)R), i.e. it is ≤ ι. Time integrals: the first as II_α, ≤ τ_α λ; the second over the whole near period,
whose duration is ≤ dε(κ1K_fλ/ε + 1) ≤ τ_n λ (Lemma 4.2(iii), ε ≤ 2λ), and λ/(K_R R) ≤ 1/K_R. So
∫_near II dt ≤ v c_6 Mλ^{1+γ}[C1A τ_α + ι κ1^{1/2}τ_n/K_R]. Finally Mλ^γ = m(λ/R)^γ > m(K_f+1)^{−γ}, so
Mλ^{1+γ} ≤ ((K_f+1)^γ/m) M²λ^{1+2γ}, and ∫_near II dt ≤ v D_IIl M²λ^{1+2γ}.

**Conclusion.** E ≤ ½f²M²λ^{1+2γ} + v[D_I + max(D_IIs, D_IIl)]M²λ^{1+2γ} ≤ ½θM²λ^{1+2γ} for near pairs. With Step 3 this
is the E-part of (Imp*). ∎

### 4.7 Step 5 ((J1*): l ≤ L_J λ)

l(t_s) = λ and l′ = v∫T·AT ≤ v∫a*(ρ) (lem:B-2(i), lem:B-V(ii)).
- *Far, g > ηR:* ρ ≥ ρ_m ≥ ε on the arc, so (log l)′ ≤ v/ρ_m ≤ v/(c_R R) (g > K_RR) or v/(c_ρ g) (ηR < g ≤ K_RR). The first
  lasts ≤ χU; for the second, Lemma 4.2(i) with g0 = ηR, h = g^{−1}1{g ≤ K_RR}: ∫dt/g ≤ dε/(ηR) + χ log(K_R/η) ≤
  d/(K_εη) + χ log(K_R/η). Total increase of log l ≤ X_far.
- *Far, g ≤ ηR:* lem:B-3(c): l′ ≤ (2v/ρ_m)[l(|p_a| + l^{1/2}N)²/ρ_m² + N²], with |p_a| ≤ C_pMg^{1+γ} (Step 3),
  l^{1/2}N ≤ κ1^{1/2}Mλ^{1+γ} ≤ κ1^{1/2}K_f^{−1−γ}Mg^{1+γ}, ρ_m ≥ c_ρ g, N² ≤ M²λ^{1+2γ} ≤ l M²(g/K_f)^{2γ}. So
  (log l)′ ≤ B_5 v M² g^{2γ−1}. Integral over the times with g ≤ ηR (gaps ≥ K_fλ ≥ K_fε/2): if γ ≤ 1/2, Lemma 4.2(i)
  (h = g^{2γ−1}1{g ≤ ηR}): ≤ dε(K_fε/2)^{2γ−1} + χ(ηR)^{2γ}/(2γ) = d(2/K_f)^{1−2γ}ε^{2γ} + χη^{2γ}R^{2γ}/(2γ);
  if γ > 1/2, Lemma 4.2(ii) (G = ηR): ≤ χ(ηR + ε/κ1)^{2γ}/(2γ). Both are ≤ I_5 R^{2γ} (ε ≤ R/K_ε). Total ≤ B_5 I_5 v m².
- *Near:* l′ ≤ v[m̃(ε)/ε + ∫_ε^∞ m̃(y)y^{−2}dy], m̃(y) := |{s∈(a,b): ρ_s < y}| ≤ l(J_y) ≤ κ1 min(λ, c_6y) (J_y as in Term I,
  (J1*)), m̃ ≤ l ≤ κ1λ for large y, m̃(ε) > 0 only if g < c_6ε. This is Term I with CμA M²λ^{2γ} replaced by κ1, so the
  increase while near is ≤ vκ1τ_I λ.
The far phase precedes the near phase, so l_t ≤ λ exp(X_far + B_5I_5vm²) + vκ1τ_Iλ = L_J λ < κ1 λ by (P7). This completes
(Imp*), hence (a). ∎

### 4.8 Proofs of (b), (c), (d), (e)

**(b)** Step 1 is now valid up to T_end: at most κ1U/ε non-final legs after j_s, so the construction stops, at a leg start
T_stop = t_J ≤ t_s + (κ1U/ε)·ε/(1−v), with a_{J+1} = b_E, i.e. l_{T_stop}(a_J,b_E) ≤ ε. By lem:B-C(3) (for the cut
construction) every θ ∈ [a_j, a_{j+1}] is seen by t_j, j ≤ J, and these intervals cover [a_s, b_E]. |P − x_{b_E}| =
c(a_J,b_E) ≤ l ≤ ε at T_stop. ∎

**(c)** Let leg j+1 > j_s be non-final, t in it, s ∈ (a_{j+1}, b_E]. By Step 1, λ(a_j,s) ≥ ε/κ1 ≥ ε/2. If l := l_t(a_j,s) ≤ R:
λ ≤ l ≤ R, so (a_j,s) ∈ F(t) and E ≤ ½M²λ^{1+2γ} ≤ ½m² l (l/R)^{2γ}: (F_b) with c_0 = m²/2, c_1 = 0 (c_0 + c_1 ≤ 1/4 by
(Pc)). If l > R: then λ > R/κ1 (if λ ≤ R, (J1*) gives λ ≥ l/κ1), and by (E-star*) (min(λ, K_RR) ≥ R/κ1 as K_R ≥ 1):
ρ_s ≥ c_A R/κ1 − δ1R/K_ε = r_1 > 0: (S). (Hypotheses of thm:R: γ ∈ (0,1], r_0 = R ∈ (0,1], r_1 ∈ (0,1].)
K̃: the Claim in the proof of thm:R, applied with b* = b_E, K_T = 0, 2π ↦ b_E (sec_E proof of (c), verbatim), gives
K̃ ≤ 16e^{2μ} + 4c_0(1+1/γ) + 2e^{2μ}L_s/r_1 whenever R_j := l_{t_j}(a_j,b_E) ≤ L_s. Here R_j ≤ κ1(U − u_{a_j}) ≤ κ1U =: L_s:
for j = j_s, R_j = U; for j > j_s cover [a_j, b_E] by consecutive pairs of the family of leg j+1 (⊂ F(t_j)): (a_j,a_{j+1})
(label length in [ε/κ1, ε]), then pairs of label length ε starting at labels ≥ a_{j+1}, a last piece shorter than ε/2
merged with its predecessor (label length < 3ε/2 ≤ R); if 0 < U − u_{a_{j+1}} < ε/2 the single pair (a_j,b_E) (label
length < 3ε/2 ≤ R); (J1*) on each. With e^{2μ} ≤ δ1: K̃ ≤ 16δ1 + 2m²(1+1/γ) + 2δ1κ1U/r_1. ∎

**(d)** Step 2 (valid up to T_end). **(e)** Step 1(d). ∎

## 5. Proof of Corollary End*

(S3*) is assumed. Since U ≤ U_max and (P0)–(P7) are monotone in U, they hold for U.
(S2*): let ε/2 ≤ λ ≤ R (≤ λ0 by (C1)). By (E1), (C6), (C5) and λ/R ≤ 1:
N ≤ C0λ^{1/2+a′} = C0R^{a′}(λ/R)^{a′}λ^{1/2} ≤ s0 m min(1,K_f/K_R)^ν (λ/R)^{γ+ν}λ^{1/2}
= s0 M λ^{1/2+γ} · min(1,K_f/K_R)^ν (λ/R)^ν.
And min(1,K_f/K_R)(λ/R) ≤ min(1, (K_f/K_R)(λ/R)) ≤ min(1, K_fλ/min(u_a,K_RR)) (if (K_f/K_R)(λ/R) ≥ 1 the middle term is 1;
otherwise it equals (K_f/K_R)(λ/R) ≥ min(1,K_f/K_R)(λ/R); and min(u_a,K_RR) ≤ K_RR). So (S2*) holds (also when u_a = 0).
(S1*): at t_s, l = λ, so c = λ − E. For ε/2 ≤ λ ≤ λ0, by (E1), c ≥ λ(1 − ½(C0λ^{a′})²) =: φ(λ), and φ ≥ 0 since
C0λ^{a′} ≤ C0λ0^{a′} ≤ 1 (C0).
- λ ≤ min(K_RR, λ0): c ≥ λ(1 − ½(C0 min(K_RR,λ0)^{a′})²) ≥ c_Aλ by (C2).
- K_RR < λ ≤ λ0 (only if K_RR < λ0): φ is concave on [0,∞) (φ″ = −½C0²(1+2a′)2a′λ^{2a′−1} ≤ 0), so on [K_RR, λ0] it is
  ≥ min(φ(K_RR), φ(λ0)) ≥ c_AK_RR by (C2) (φ(K_RR) ≥ c_AK_RR) and (C3).
- λ > λ0: c ≥ c_sep ≥ c_AK_RR by (E2), (C4).
In all cases c ≥ c_A min(λ, K_RR). ∎

The proof uses the choice of γ only through γ + ν ≤ a′ (C5) and γ + ν < 1 (P0): the cap γ ≤ 1/4 and the choice
γ = a′/2 of cor:End are not needed.

## 6. Structural facts requested by stream Q2 (reports/Q2-1.md, items (P1)–(P4))

Notation: in the proof of (Imp*) for a pair (a,b) ∈ F(t) (t in leg j+1), call a pair *used* if a family bound (J1*),
(J2*) or (CA*) of that pair is invoked.

**Lemma Q1.L1 (uses of (S1\*)). PROVED.** In the proof of (a), (b), (d), (e), hypothesis (S1*) enters only through (CA*)
at times τ ∈ [t_s, t], for: (i) family pairs of F(τ) contained in [a_{j(τ)}, max(b, a_{j(τ)+1})] (one-step tilt,
c(J_1) ≥ c_Aλ_{J_1} with λ_{J_1} ≤ R); (ii) the pairs (a_{j(τ)}, s), s ∈ [a,b], via (E-star*) (Step 3 at s = a; Terms
I, II and Step 5 at s ∈ (a,b)); these pairs can be long (w_s up to and beyond K_RR). In (c), additionally the pairs
(a_j, s), s ∈ (a_{j+1}, b_E].
*Proof.* (CA*) is invoked exactly in: Step 2 one-step bound (pairs of the chains (A), (B), (C), all inside
[a°, b] ⊂ [a_j, b], and in Term II the pair I_0 = (a_j,a_{j+1}) ⊂ [a_j, a_{j+1}]); Step 1(d) (E-star*) for the pair
(a_j, s); and nowhere else (Step 1(a) uses (J1*) only; Steps 3–5 use (CA*) only through Steps 1(d), 2). ∎
*Comparison with Q2's (P1):* TRUE, with "c ≥ λ/2 for λ ≤ R" read as (i) and "(E-star) at labels of the pair under
estimate and the current base" read as (ii). Note (ii) needs (CA*) for the possibly long pairs (a_j, s).

**Lemma Q1.L2 (localisation). PROVED.** The bound (Imp*) for (a,b) at time t uses family bounds only (i) at times
τ ∈ [t_s, t], for pairs of F(τ) contained in [a_{j(τ)}, max(b, a_{j(τ)+1})]; (ii) at leg starts t_i ≤ t, for the
base pairs (a_i, a_{i+1}), (a_i, s_i) (u_{s_i} = u_{a_i} + ε/2) and (a_{i−1}, b_E) of Step 1(a), which enter only through
the leg structure (advances ≥ ε/κ1, leg count, Lemma 4.2, T_B).
*Proof.* List of invoked pairs: Step 2 chains (inside [a_j,b]); (E-mu*) sub-arcs of (a,b) from a; Step 3: (a′,a), (a′,b)
with a′ ∈ {a_j,a_{j+1}}, a′ ≤ a (inside [a_j,b]); Term I: J_y ⊂ (a,b); Term II: (a′,a), (a′,b), J_0 ⊂ [a_j,b] and, only
when a = a_j and a_{j+1} > b (then λ < ε), I_0 = (a_j,a_{j+1}); Step 5: J_y. ∎
*Comparison with Q2's (P2):* TRUE after enlarging [a_j, b] to [a_j, max(b, a_{j+1})] (relevant only for λ < ε) and adding
(ii). Whether "body pairs" are closed under (i)–(ii) depends on Q2's geometry (which end the tail is at); Q2 must check
it against this list.

**Lemma Q1.L3 (start data enter per pair, monotonically; restart of a far pair). PROVED.** (1) For a fixed pair (a,b),
data at t_s enter the proof of (Imp*) for that pair only through N(a,b;t_s) (Step 3 first term; Step 4 initial value if
near at t_s), l_{t_s}(a,b) = λ (Step 5) and the labels/U; all three monotonically (N(t_s) linearly with coefficient
A0(·)^ν; E(t_s) additively; l(t_s) multiplicatively). (2) Let t_w ≥ t_s, suppose (a,b) is far at t_w
(g_w := g(t_w) ≥ K_fλ), the used pairs satisfy the family bounds and (CA*) on [t_w, t], and
N(a,b;t_w) ≤ s0Mλ^{1/2+γ}min(1, K_fλ/min(g_w,K_RR))^ν, l_{t_w}(a,b) ≤ (1+δ)λ. Then for t ≥ t_w the conclusions of Steps
3–5 for (a,b) hold under (P5), (P6) and
(P7_δ) (1+δ) exp(X_far + B_5I_5vm²) + vκ1τ_I < κ1.
*Proof.* (1) by inspection of 4.5–4.7. (2) Lemma 4.1 on [t_w, t] ⊂ [t_s, t]; the amplification claim holds for
t_w ≤ τ ≤ t verbatim; first term: A0(min(g_w,K_RR)/ĝ_2)^ν N(t_w) ≤ A0 s0 Mλ^{1/2+γ}(min(min(g_w,K_RR),K_fλ)/ĝ_2)^ν ≤
A0s0Mλ^{1/2+γ}; the forcing integrals over subsets of [t_s, t] are bounded as before. Step 4 starts from Step 3. Step 5:
l(t_w) ≤ (1+δ)λ multiplied by the far factors, plus the near increase. ∎
*Comparison with Q2's (P3):* TRUE.

**Lemma Q1.L4 (room in (J1*)). PROVED** (given (P7_δ)). (Imp*) gives l ≤ L_J λ with L_J < κ1; a start stretch
l(t_w) ≤ (1+δ_tail)λ is admissible iff (P7_δ) holds with δ = δ_tail. Since κ1 is a free parameter, room is bought by
raising κ1 (cost: c_t, C1A ∝ κ1^{1/2}, c_ρ, c_R decrease by the increase of κ1). At the unconstrained optimum (P7) is
binding, so δ_tail ≈ 0 there; the optimiser therefore also optimises under (P7_δ) with δ_tail = 2·10⁻⁵ (runs marked
"delta_tail"); the cost in v is a few per cent (NUMERICAL, see reports/Q1-1.md).
*Comparison with Q2's (P4):* TRUE (as (P7_δ)).

**Cap γ ≤ 1/4.** Not needed (γ + ν < 1 suffices; Step 5 treats γ > 1/2 by Lemma 4.2(ii)). PROVED (by the proof above).

## 7. Corrections against the interim statement (reports/Q1-1.md, interim version)

| item | interim | final | reason |
|---|---|---|---|
| B_2 (far forcing, g > ηR) | B_2 = 2κ1^{3/2}max(...)·vχU/(Rm) | B_2U χU/R + B_2η | tightening, written in 4.5 (gap integral for ηR < g ≤ K_RR) |
| (P7) far part | vχU/(c_η R) | X_far | tightening, written in 4.7 |
| D_IIs | C_q C1A τ_II with C_q = c_6(c_6C_1 + c_bC1A), τ_II = … | c_6²C1A²τ_α + 2c_6²κ1C_TLC1Aτ_β + 4dc_6C1Ak_0 | the interim formula had no written derivation; replaced by the derived one (4.6) |
| CμA, C1A, r_f, C_p, B_3, Ψ, τ_I, τ_n, D_I, D_IIl, B_5, I_5, c_amp, c_6, c_ρ, c_R, K_1, K_2, a_i | as interim | unchanged | confirmed line by line |
| (C1)–(C3) | K_RR ≤ λ0 required | R ≤ λ0; (C2) with min(K_RR,λ0); (C3) only if K_RR < λ0 | weakening, proved in §5 |
| (C0) | implicit | C0λ0^{a′} ≤ 1 listed | used in §5 |
| (b) advance | [ε/κ1, ε] | same | confirmed (Step 1(a)) |

## 8. Numerical status

The side conditions are explicit inequalities between elementary functions of the parameters; `code/Q1/optimise.py`
evaluates them in 50-digit mpmath at the reported parameter values (v reduced by a relative 10⁻⁶ and every dependent
quantity d, δ1, ν, A0, f inflated by a relative 10⁻³⁰). That every condition holds at the reported values is
NUMERICAL (exact arithmetic up to 50 digits on explicit formulas); that the conditions imply the theorem is PROVED above.
