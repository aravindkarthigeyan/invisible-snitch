# R9-far: far pairs and length — sharper Prop 4.2 / Prop 4.4 (round 9, stream R-far)

Base text: `r9/base_short/` (sec2–sec4, sec7b, sec8; `verify_constants.py`). Script: `r9/far/far_opt.py` (+ `far_opt_mode*.out`),
sanity test `r9/far/check_lemmaE.py`. Claims for refereeing: `referee/R9-far-claims.md`.
Labels: **PROVED** (every step written below, or a cited label of the base text), **NUMERICAL** (float computation in the
scripts), **CONJECTURE** (none).

## 0. Summary

| # | new statement | replaces | status | effect |
|---|---|---|---|---|
| E* | far inequality with the **arc distance** ρ_* = min_s ρ_s instead of the hull distance ρ_m; integration by parts + Wirtinger | Lemma 2.6(v) (`lem:excess`(v)) | PROVED | factor 1/π on the forcing; aD(K) → aD*(K) = 1+1/(πK)+2/(π²K²); length bound with one square (B_5: factor ≈ 1/2) |
| Du* | Duhamel lemma with ρ_*, aD* | Lemma 2.7 (`lem:duhamel`) | PROVED | drop-in for Prop 4.2 **and** Theorem 5.2(v): η_N = aD*(4)v0/ζ, c_β → c_β/π |
| GI(iv) | gap–time integral for unimodal weights | new item of Lemma 3.6 (`lem:gapint`) | PROVED | needed for (S1G) |
| T2* | global chord bound at touch-down: c ≥ min(k_c d_c, 2 sin(½ min(π, min(λ,d_c)/(W_x L̂)))) for λ > λ0 | strengthens (T2) of Thm 7.12 | PROVED (from `lem:len`, `lem:bulk`(c), (SC41)–(SC44)) | optional hypothesis (S1G) |
| S1G | (S1G) holds for both tuples (from (T1), T2*) | addendum to `lem:start` | PROVED | |
| F* | far pairs: distance c_ρ* = c_A − 2δ1/K_f (was c_A − (2δ1+κ)/K_f), c_η, c_R* = c_AK_R − δ1/K_eps (was −κ more); C_p* = min(C_p, C_p^V); Ĉ(x) = min(C_p*, C_ar x^{1/2}); integrals J_1, J_2 | Prop 4.2 (`prop:far`) | PROVED | B_3: 413 → 38.5; B_2η: 23.9 → 1.07; c_amp: 5.18 → 1.92 (base point) |
| L* | length with c_η in the middle regime, B_5*, J_1 | Prop 4.4 (`prop:length`) | PROVED | X_far: 0.0128 → 0.0121 (S1 only) / 0.00088 (with S1G) at the base point |
| — | optimiser over all side conditions, D free | — | NUMERICAL | Section 5 |

**Tilt constants.** Following the coordinator, all numbers below use stream R-tilt's constants (`reports/R9-tilt.md`,
unrefereed): C_T = ω_* max(σ_q s(q), s(2q/(q−1))) in place of C_A = C_B = C_TL, C_μ = 1 + κC_T², and R-tilt's
C_p' = κ^{1/2}(1+1/K_f)^{1/2+γ}K_f^{−1/2} + κC_T(1+1/K_f)^γ in place of C_p (conditions (T1)–(T4) of R-tilt added, the two
deleted "extra" conditions dropped). My proofs use C_B and C_p only through Lemma 3.8 (same right end) and bound 1 of
Prop F*(iv); both are covered by R-tilt's Lemma T(i) and Lemma O(O3), so every formula below holds with C_B → C_T, C_p → C_p'.
Values in brackets [·] are with the old (base) tilt constants.

At the printed base point (v0 = 6e-5, all base parameters, D = 545) the new formulas give: c_ρ* = 0.599 (old c_ρ 0.397), c_amp* = 1.92 (5.18),
B_3' = 18.5 [38.5] (old B_3 = 413, R-tilt's B_3' = 126; B_3' already contains the factor K_f^{−ν}(…) — the comparable old
quantity B_3K_f^{γ−1}(2d_L/K_f + χ/(1−γ−ν)) is 500 [R-tilt: 152]), B_2η* = 1.07 (23.9), B_5* = 77.1 [735] (old 5162, R-tilt 493.5),
J_1 = 198 (S1 only; old χU0/(c_RR) = 204) resp. J_1 = 10.9 (S1G), L_J = 1.0129 (S1) / 1.0016 (S1G) (old 1.0143).

**The decisive point for v0 ~ 1e-3 is (P7).** Without new input, the length factor contains
v0·χU0/(c_R R) ≈ 200 v0 (time χU ≈ 6.4 spent at distance ≥ c_RR ≈ 0.032), so (P7) forces v0 ≲ log κ/(200 κ) — 8e-5 at
κ = 1.016 and at best 1.1e-3 at κ = 4/3. This is not an artefact of the far-pair estimate: (S1) only knows chords up to K_RR < λ0.
The new touch-down Lemma T2* (proved from existing lemmas) gives chords ≳ (2/π)·min(λ, d_c) at all scales; with it J_1 drops from
≈ 200 to ≈ 11–17 and (P7) allows v0 ~ 1e-2. See Section 5: best honest joint point (R-tilt + R-near D′(p) + this stream, with (S1G)) **v0 ≈ 4.15e-3** (a lower bound for the joint optimum), binding (PT), (TS), (A4)/(A5) ranges; (S1)-only ceiling ≈ 2e-3; the fixed-D = 35 value 6.7e-3 is not honest (D′ ≈ 110 at the κ − c_A it uses).

---------------------------------------------------------------------------------------------------------------------

## 1. Notation (additions to Def 2.5 / Def 3.3)

* For a virtual flow, labels a < b, time t: **ρ_*(t) := min_{s∈[a,b]} ρ_s(t)** (arc distance). Since every x_s lies in the convex
  hull, ρ_* ≥ ρ_m. ρ_* is continuous in t (minimum over a compact label set of the jointly continuous function |x(s,t) − P(t)|).
* **aD*(K) := 1 + 1/(πK) + 2/(π²K²)** (decreasing in K; aD*(K) ≤ aD(K)).
* In Section 4 (far pairs): g, ĝ, β = β(τ), β⁺, σ_s, w_s, t_∘ exactly as in the standing assumptions of sec4.tex.
* New constants (Def 3.3 additions; ★ = changed formula, ✚ = new symbol) — collected in Section 3.

---------------------------------------------------------------------------------------------------------------------

## 2. New statements and proofs

### 2.1 Lemma E* (replaces Lemma 2.6(v)) — PROVED

**Lemma E\*.** For a virtual flow, fixed labels a < b and a time t with c(a,b;t) > 0, suppose ρ_* = min_{s∈[a,b]} ρ_s(t) ≥ ε.
Let l := l(a,b), N := N(a,b), e := e_{ab}, p_a := r_a × e. Then
```
(a)  E' ≤ (v/ρ_*)·(1 + l/(πρ_*) + 2l²/(π²ρ_*²))·N² + 2v l^{3/2} |p_a| N / (π ρ_*³),
(b)  l' ≤ (v/ρ_*)·[ N + (l^{1/2}|p_a| + lN/π)/ρ_* ]².
```
Since ρ_* ≥ ρ_m, (a) implies the first inequality of Lemma 2.6(v) (with better constants), and (b) implies the second one
(by (x+y)² ≤ 2x² + 2y² and l^{1/2}|p_a| + lN/π ≤ l^{1/2}(|p_a| + l^{1/2}N)).

*Proof.* Fix t; parametrise the arc by arclength σ ∈ [0,l] (σ = 0 at a), so dx/dσ = T and r(σ) = x(σ) − P.

*Step 0 (field on the arc).* Since ρ ≥ ρ_* ≥ ε on the arc, Lemma 2.2(ii) gives A(r) = Π(r)/ρ there; hence 0 ≤ A ≤ I/ρ ≤ I/ρ_*,
e·Ae ≥ 0, and q = e^⊥·A(r)e = −(r·e)(r·e^⊥)/ρ³ = Q(r) with Q(y) := −(y·e)(y·e^⊥)/|y|³ (as in the proof of Lemma 2.6(v)).
In the coordinates y_1 = y·e, y_2 = y·e^⊥ (y ≠ 0), as computed there:
∂_{y1}Q = −y_2(y_2² − 2y_1²)/|y|⁵, ∂_{y2}Q = −y_1(y_1² − 2y_2²)/|y|⁵, hence
|∂_{y2}Q| ≤ |y|^{−2} (since max_{|z|≤1}|z(3z²−2)| = 1) and |∂_{y1}Q| ≤ 2|y_2|/|y|³ (since |y_2² − 2y_1²| ≤ 2|y|²).

*Step 1 (the function δ).* Put ς := (T − e)·e^⊥ = T·e^⊥ and δ(σ) := ∫_0^σ ς = (x(σ) − x_a)·e^⊥. δ is C¹ on [0,l] with
δ' = ς, δ(0) = 0 and δ(l) = (x_b − x_a)·e^⊥ = c e·e^⊥ = 0. Also |ς| ≤ |T − e|, so ∫_0^l ς² ≤ ∫_0^l |T − e|² = N² (Lemma 2.5(b)).

*Step 2 (Wirtinger).* For δ ∈ C¹[0,l] with δ(0) = δ(l) = 0: ∫_0^l δ² ≤ (l/π)² ∫_0^l δ'² (Wirtinger's inequality, e.g.
Hardy–Littlewood–Pólya, *Inequalities*, Thm 257). Proof: the odd 2l-periodic extension δ̃ of δ is continuous and piecewise C¹,
so it is absolutely continuous with derivative in L², and its Fourier series contains only sine terms:
δ̃ = Σ_{k≥1} b_k sin(kπσ/l), δ̃' = Σ_k (kπ/l) b_k cos(kπσ/l) in L²(−l,l). Parseval on [−l,l] and evenness/oddness give
∫_0^l δ² = (l/2)Σ b_k² and ∫_0^l δ'² = (l/2)Σ (kπ/l)² b_k² ≥ (π/l)²(l/2)Σ b_k². ∎ Consequently
```
∫_0^l δ² ≤ (l/π)² N²,      ∫_0^l |δ| ≤ l^{1/2}(∫δ²)^{1/2} ≤ l^{3/2} N/π .
```

*Step 3 (integration by parts).* By Lemma 2.6(ii), ∫ ς dσ = 0, so ∫ ς q dσ = ∫_0^l δ'(σ) G(σ) dσ with
G(σ) := Q(r(σ)) − Q(r(0)). Q is C^∞ on R²∖{0} and r(σ) ≠ 0, so G is C¹ with G' = ∇Q(r)·T and G(0) = 0. Since δ(l) = 0,
```
∫_0^l ς q dσ = [δG]_0^l − ∫_0^l δ ∇Q(r)·T dσ = −∫_0^l δ ∇Q(r)·T dσ .
```

*Step 4 (bound).* ∇Q(r)·T = ∂_{y1}Q (T·e) + ∂_{y2}Q (T·e^⊥) = ∂_{y1}Q (T·e) + ∂_{y2}Q ς, with |T·e| ≤ 1. The coordinate
y_2 of r(σ) is r(σ)·e^⊥ = r_a·e^⊥ + δ(σ), and |r_a·e^⊥| = |r_a × e| = |p_a|. With Step 0 and ρ ≥ ρ_*:
```
|∫ ς q| ≤ ∫ |δ||ς|/ρ² + 2∫ |δ|(|p_a| + |δ|)/ρ³
        ≤ ρ_*^{-2} (∫δ²)^{1/2}(∫ς²)^{1/2} + 2ρ_*^{-3}( |p_a| ∫|δ| + ∫δ² )
        ≤ lN²/(πρ_*²) + 2|p_a| l^{3/2} N/(πρ_*³) + 2 l² N²/(π² ρ_*³)          (Steps 1, 2).
```

*Step 5 (a).* By Lemma 2.6(ii), E' = v∫(T−e)·A(T−e) − (v/2)∫(e·Ae)|T−e|² + v∫ςq. By Step 0 the first term is
≤ (v/ρ_*)∫|T−e|² = vN²/ρ_*, the second is ≤ 0. Add v·(Step 4). This is (a).

*Step 6 (b).* By Lemma 2.6(i) and Step 0, l' = v∫T·AT = v∫ sin²φ/ρ (T·ΠT = 1 − cos²φ). Now ρ|sin φ| = |T × r| and
T × r = e × r + (T − e) × r with |e × r| = |r·e^⊥| = |r_a·e^⊥ + δ| ≤ |p_a| + |δ| and |(T−e) × r| ≤ |T − e|ρ. Hence
|sin φ|ρ^{−1/2} ≤ (|p_a| + |δ|)ρ_*^{−3/2} + |T − e|ρ_*^{−1/2} pointwise, and by Minkowski's inequality in L²(dσ),
```
(∫ sin²φ/ρ)^{1/2} ≤ ρ_*^{-3/2}( |p_a| l^{1/2} + (∫δ²)^{1/2} ) + ρ_*^{-1/2} N ≤ ρ_*^{-3/2}( |p_a| l^{1/2} + lN/π ) + ρ_*^{-1/2} N .
```
Square and multiply by v. ∎

NUMERICAL check (`r9/far/check_lemmaE.py`, 2999 random arcs/points): max E'/(bound (a)) = 0.989, max l'/(bound (b)) = 0.9995 —
both bounds are essentially sharp (the leading term vN²/ρ is attained when P is far and on the chord line); the identity of
Step 3 is reproduced to discretisation accuracy.

### 2.2 Lemma Du* (replaces Lemma 2.7) — PROVED

**Lemma Du\*.** Let a < b be labels of a virtual flow with c(a,b;t_1) > 0, and suppose ρ_*(t) ≥ ε on [t_1,t_2]. With
α := (v/ρ_*)(1 + l/(πρ_*) + 2l²/(π²ρ_*²)), β := 2v l^{3/2}|p_a|/(πρ_*³),
N(t_2) ≤ e^{∫_{t_1}^{t_2}α} N(t_1) + ∫_{t_1}^{t_2} e^{∫_t^{t_2}α} β(t) dt. If moreover ρ_* ≥ K l on [t_1,t_2], then α ≤ aD*(K) v/ρ_*.

*Proof.* Word for word the proof of Lemma 2.7, with Lemma E*(a) in place of Lemma 2.6(v): c > 0 on [t_1,t_2] by Lemma 2.4(c);
α, β are continuous (ρ_* is continuous and ≥ ε > 0; l, |p_a| are continuous); N_η := (N² + η²)^{1/2} is C¹ and
N_ηN_η' = E' ≤ αN² + βN ≤ αN_η² + βN_η; Grönwall; η → 0. The last claim is l/ρ_* ≤ 1/K. ∎

**Drop-in for Theorem 5.2(v).** Its proof applies Lemma 2.7 with K = 4 on an interval where (hull) ρ_m ≥ ζ(g̃+τ) ≥ 4l and
ρ_m ≥ ε; as ρ_* ≥ ρ_m, Lemma Du* applies with α ≤ aD*(4)v/ρ_m and β ≤ (1/π)·(the β used there). Hence Theorem 5.2(v) holds with
```
η_N := aD*(4) v0/ζ  (aD*(4) = 1.09223, was aD(4) = 1.375),     c_β := 2(1+δ_t)^{3/2} k_D^{γ−1} / (π ζ³ (1−γ))  (was without 1/π).
```
(No other change in Section 5; the far-pair bound of Section 4 is the other user of Lemma 2.7.)

### 2.3 Lemma GI(iv) (new item of Lemma 3.6) — PROVED

**Lemma 3.6(iv).** In the setting of Lemma 3.6 let 𝒯 ⊂ [t_dd,t'] be a set of times on which g(τ) ∈ (g_0, Y], and let H ≥ 0 be
non-increasing on (0, Y/2] and non-decreasing on [Y/2, ∞), with H ≤ H_max on (g_0, Y]. Then
```
∫_𝒯 H(g(τ)) dτ ≤ 2 d_L ε H_max + χ_g ( ∫_{g_0}^{Y/2} H + ∫_{Y/2}^{Y} H )     (an integral over an empty range is 0).
```
*Proof.* Let g_1 > … > g_n be the values of g on 𝒯 (each held during at most one leg, of duration ≤ d_Lε; consecutive values
differ by ≥ ε/κ, Lemma 3.6). *Values ≤ Y/2.* For each such value except the smallest, H(g_i) ≤ (κ/ε)∫_{g_i−ε/κ}^{g_i} H (H is
non-increasing on (0, Y/2] and g_i − ε/κ ≥ g_{i+1} > g_0); these intervals are disjoint and lie in (g_0, Y/2]. *Values > Y/2.*
For each such value except the largest, H(g_i) ≤ (κ/ε)∫_{g_i}^{g_i+ε/κ} H (H non-decreasing on [Y/2,∞), g_i + ε/κ ≤ g_{i−1} ≤ Y);
the intervals are disjoint and lie in [Y/2, Y]. The two exceptional values contribute ≤ 2d_LεH_max; the rest
≤ d_Lε(κ/ε)(∫_{g_0}^{Y/2}H + ∫_{Y/2}^{Y}H). ∎

### 2.4 Lemma T2* (touch-down: global chords) — PROVED

**Lemma T2\*.** In the setting of Theorem 7.12 (touch-down), let u_a < u_b be labels of x^∘ with λ = u_b − u_a > λ0, and put
d_c := u_a + U − u_b. Then, with W_x, L̂ = (8/λ0)^{2v̄}/(1−2v̄) and k_c of Definition 7.1,
```
c(a,b) ≥ min( k_c d_c , 2 sin( ½ min(π, min(λ, d_c)/(W_x L̂)) ) ).
```
*Proof.* Let Θ_a < Θ_b be the labels (directions) and Δ := Θ_b − Θ_a. By Lemma 7.10 (`lem:len`), λ > λ0 implies Δ > Δ0, where
Δ0 = λ0/(W_xL̂) (Definition 7.1). Two cases, as in the proof of (T2).

*Case A: Δ ≤ 2π − Δ0.* As in the proof of (T2), x^∘(u_a), x^∘(u_b) are positions at t_dd as in Lemma 7.9(c) (`lem:bulk`(c)),
with initial points e^{iΘ_a}, e^{iΘ_b} at distance 2 sin(Δ/2) = 2 sin(Δ̃/2), Δ̃ := min(Δ, 2π−Δ) ∈ [Δ0, π]; since
2 sin(Δ̃/2) ≥ 2 sin(Δ0/2) = c_sep > 2ε̄ ≥ 2ε ((SC42), (SC43)), Lemma 7.9(c) gives c ≥ 2 sin(Δ̃/2).
*Lower bound for Δ̃.* By the proof of Lemma 7.10, w ≤ W_x(2/|θ|_∘)^{2v} at every label θ ≠ 2π (|θ|_∘ = circular distance to 0),
and the integral of (2/|θ|_∘)^{2v} over any arc of length Δ' ≤ 2π is ≤ Δ'(4/Δ')^{2v}/(1−2v) (the arc bound). For Δ' ≥ Δ0:
(4/Δ')^{2v} ≤ (4/Δ0)^{2v} ≤ (8/λ0)^{2v} (as 4/Δ0 = 4W_xL̂/λ0 ≤ 8/λ0 by (SC41)), and (8/λ0)^{2v}/(1−2v) ≤ L̂ (v ≤ v̄, 8/λ0 ≥ 1);
so the integral of w over such an arc is ≤ W_xL̂Δ'. (i) λ = ∫_{Θ_a}^{Θ_b} w dθ ≤ W_xL̂Δ, i.e. Δ ≥ λ/(W_xL̂).
(ii) d_c = ∫_{α_0}^{Θ_a} w + ∫_{Θ_b}^{2π+b_e} w, with b_e = α_0 − ξ_e < α_0 (Lemma 7.6(a), `lem:tail`). Modulo 2π both label
sets lie in the arc [Θ_b, Θ_a + 2π] of length 2π − Δ ≥ Δ0 (because Θ_b ≤ 2π + b_e < 2π + α_0 ≤ 2π + Θ_a), and they are
disjoint; the pointwise bound depends only on θ mod 2π; so d_c ≤ W_xL̂(2π − Δ). Hence Δ̃ ≥ min(λ, d_c)/(W_xL̂), and since
Δ̃ ≤ π and x ↦ 2 sin(x/2) is increasing on [0,π], c ≥ 2 sin(½ min(π, min(λ,d_c)/(W_xL̂))).
*Case B: Δ > 2π − Δ0.* The proof of (T2) (second case; uses (SC44)) gives c ≥ k_c(u_a + U − u_b) = k_c d_c. ∎

### 2.5 Hypothesis (S1G) and its verification — PROVED

Let 𝒢 : [0,∞) → [0,∞) be non-decreasing. Add to Setting (H) the optional hypothesis
* **(S1G)** c(a,b;t_dd) ≥ 𝒢(min(λ, a + U − b)) for all pairs with λ > K_RR.

(Without (S1G) put 𝒢 ≡ 0; all statements below then reduce to (S1).) For the assembly take
```
𝒢(y) := min( c_0' y , k_c y , 2 sin(½ min(π, y/(W_xL̂))) ),     c_0' := 1 − ½ (C_0 λ0^{a'})².
```
**Lemma (start, addendum).** Under the hypotheses of Lemma 8.2 (`lem:start`) and Theorem 7.12, (S1G) holds for every pair of
[0,U] (main tuple, U the full length) and for every pair of [0,U_A] with U replaced by U_A (stage A).
*Proof.* Let λ > K_RR. If λ ≤ λ0: by the proof of Lemma 8.2, c ≥ φ(λ) = λ(1 − ½C_0²λ^{2a'}) ≥ c_0'λ ≥ c_0'y ≥ 𝒢(y), where
y := min(λ, a + U − b) ≤ λ. If λ > λ0: here y = min(λ, d_c) with d_c = a + U − b, and Lemma T2* gives
c ≥ min(k_c d_c, 2 sin(½min(π, y/(W_xL̂)))) ≥ min(k_c y, 2 sin(½min(π, y/(W_xL̂)))) ≥ 𝒢(y) (d_c ≥ y; 𝒢 is the minimum of three
branches, two of which are these). For stage A, the true d_c = a + U − b ≥ a + U_A − b
and 𝒢 is non-decreasing. ∎

**Lemma 3.7(iii) (distance, far regime).** Under (H) + (S1G): for t in leg j+1, base β = a_j, and a label s ≥ β with
(U − s ≥ W_e or β ≥ W_e) and w := s − β > K_RR,
ρ_s(t) ≥ max(c_A K_RR, 𝒢(min(w, β + U − s))) − δ_1 ε.
*Proof.* As in Lemma 3.7: ρ_s ≥ c(β,s;t) − |P − x_β| ≥ c(β,s;t_dd) − δ_1ε (chords non-decreasing, Lemma 2.4(c);
|P − x_β| ≤ e^{2μ}ε ≤ δ_1ε). The pair (β,s) is good, so c(β,s;t_dd) ≥ c_AK_RR by (S1), and ≥ 𝒢(min(w, β+U−s)) by (S1G). ∎

### 2.6 Proposition F* (replaces Prop 4.2, `prop:far`) — PROVED

Constants (Section 3): c_ρ* = c_A − 2δ_1/K_f, c_η = c_A − δ_1/(K_εη_1), c_R* = c_AK_R − δ_1/K_ε, K_1 = c_ρ*K_f/κ,
K_2 = c_R*/κ, and J_1(U_0), J_2(U_0) as in (3.1) below.

**Proposition F\*.** If (a,b) is far at t, it is far on [t_∘,t] and N(a,b;t) ≤ 𝔣Mλ^{1/2+γ}. Moreover, at every τ ∈ [t_∘,t],
with g = g(τ) and ρ_* = ρ_*(τ):
(i) ρ_* ≥ c_ρ* g and ρ_* ≥ K_1 l if g ≤ K_RR; (ii) ρ_* ≥ c_η g if η_1R < g ≤ K_RR; (iii) ρ_* ≥ c_R*R and ρ_* ≥ K_2 l if g > K_RR,
and under (S1G) ρ_* ≥ ρ_G(min(g, U−λ−g)) with ρ_G(y) := max(c_AK_RR, 𝒢(y)) − δ_1R/K_ε;
(iv) if g ≤ η_1R: |p_a| ≤ Ĉ(g/λ) M g^{1+γ}, Ĉ(x) := min(C_p*, C_ar x^{1/2}).

*Proof.* The gap is non-increasing, so the pair is far on [t_∘,t]. Fix τ; g ≥ K_fλ ≥ K_fε/2 > ε (K_f ≥ 3), so a > β⁺
(β⁺ − β ≤ ε).

*Distance.* For s ∈ [a,b], w_s = g + σ_s ≥ g, and Lemma 3.7 applies at s with base β (locality, standing assumptions):
ρ_s ≥ c_A min(w_s, K_RR) − δ_1ε ≥ c_A min(g, K_RR) − δ_1ε. Taking the minimum over s:
if g ≤ K_RR, ρ_* ≥ c_Ag − δ_1ε; with ε ≤ 2λ ≤ 2g/K_f this is ≥ c_ρ*g, and if g > η_1R, with ε ≤ R/K_ε < g/(K_εη_1), it is
≥ c_ηg. If g > K_RR, ρ_* ≥ c_AK_RR − δ_1R/K_ε = c_R*R; under (S1G), Lemma 3.7(iii) at each s ∈ [a,b] with
w_s ≥ g and β + U − s ≥ β + U − b = U − λ − g, and monotonicity of 𝒢, gives ρ_* ≥ ρ_G(min(g, U−λ−g)). Arc distance ≥ ε:
c_ρ*g ≥ c_ρ*K_fε/2 ≥ ε by (P2*), and c_R*R ≥ c_R*K_εε ≥ ε by (P2*). Ratios: c_ρ*g ≥ c_ρ*K_fλ ≥ (c_ρ*K_f/κ) l = K_1 l by (J1);
c_R*R ≥ c_R*λ ≥ K_2 l. (Compared with Prop 4.2 the hull loss "−l" disappears: Lemma Du* needs only the arc.) So Lemma Du*
applies on [t_∘,t] (c(a,b;t_∘) > 0 by (CA)), with α ≤ aD*(K_1)v/(c_ρ*g) while g ≤ K_RR and α ≤ aD*(K_2)v/ρ_* while g > K_RR.

*Amplification.* Claim: exp∫_τ^t α ≤ A_0 (min(g(τ),K_RR)/ĝ)^ν for t_∘ ≤ τ ≤ t. The times with g > K_RR contribute
≤ aD*(K_2) v ∫_{𝒯_3} dτ/ρ_* ≤ aD*(K_2) v J_1(U_0), where 𝒯_3 := {τ ∈ [t_∘,t]: g(τ) > K_RR}, by Lemma (J) below. The times of
[τ,t] with g ≤ K_RR give, exactly as in Prop 4.2 (Lemma 3.6(i), h(y) = y^{-1}1{y ≤ min(g(τ),K_RR)}, g_min = g(t) ≥ K_fε/2),
≤ (aD*(K_1)v/c_ρ*)[d_Lε/g(t) + χ_g log(min(g(τ),K_RR)/g(t))] ≤ 2aD*(K_1)d_Lv/(c_ρ*K_f) + c_amp* v log(min(g(τ),K_RR)/g(t)).
As v ≤ v0 and J_1 is non-decreasing in U_0 ≥ U, (P4*) and (P3*) give the claim.

*Lemma (J).* ∫_{𝒯_3} ρ_*^{−k} dτ ≤ J_k(U_0) (k = 1,2), where
```
(3.1)  J_k(U_0) := min{ χ_g U_0 (c_R*R)^{−k} ,  2d_L R/(K_ε (c_R*R)^k) + χ_g [ ∫_{K_RR}^{U_0/2} ρ_G^{−k} + ∫_0^{U_0/2} ρ_G^{−k} ] }
```
(the second entry only under (S1G); ρ_G ≥ c_R*R > 0). *Proof.* First entry: 𝒯_3 is an initial segment of length ≤ T_B = χ_gU
(Lemma 3.5(iv)) and ρ_* ≥ c_R*R there. Second entry: on 𝒯_3, ρ_*^{−k} ≤ H(g) := ρ_G(min(g, Y−g))^{−k} with Y := U − λ (extend
ρ_G(y) := ρ_G(0) for y < 0); g ≤ Y on 𝒯_3 (g ≤ a ≤ U − λ for body pairs, g ≤ g_W ≤ a for tail pairs); H is non-increasing on
(0, Y/2] and non-decreasing on [Y/2,∞) (𝒢 non-decreasing); H ≤ (c_R*R)^{−k}. Lemma 3.6(iv) with g_0 = K_RR, ε ≤ R/K_ε, and the
substitution y = Y − g on [Y/2, Y] give ≤ 2d_LR(c_R*R)^{−k}/K_ε + χ_g[∫_{K_RR}^{Y/2} + ∫_0^{Y/2}]ρ_G^{−k}, and Y/2 ≤ U_0/2. ∎

*Forcing* β* = 2v l^{3/2}|p_a|/(πρ_*³).
*Case g > η_1R.* |p_a| = dist(P, line(x_a,x_b)) ≤ ρ_a ≤ ρ_* + l ≤ ρ_*(1 + 1/K), K = K_1 (g ≤ K_RR) resp. K_2 (g > K_RR), since
|x_a − x_s| ≤ l for the minimising s. So β* ≤ 2vκ^{3/2}λ^{3/2}(1+1/K)/(πρ_*²). On 𝒯_3, Lemma (J) (k = 2) gives
∫_{𝒯_3}β* ≤ B_2U' vλ^{3/2} J_2(U_0), B_2U' := 2κ^{3/2}(1+1/K_2)/π. On η_1R < g ≤ K_RR, ρ_* ≥ c_ηg and Lemma 3.6(i)
(g_0 = η_1R, h(y) = y^{−2}1{y ≤ K_RR}) gives ∫g^{−2}dτ ≤ d_Lε/(η_1R)² + χ_g/(η_1R) ≤ (d_L/(K_εη_1²) + χ_g/η_1)/R; so this part is
≤ B_2η* vλ^{3/2}/R, B_2η* := 2κ^{3/2}(1+1/K_1)(χ_g/η_1 + d_L/(K_εη_1²))/(πc_η²).
*Case g ≤ η_1R.* As in Prop 4.2, P ∈ [x_β, x_{β⁺}] and the distance to a line is convex, so |p_a| ≤ max_{a'∈{β,β⁺}} |(x_a − x_{a'}) × e|;
the pairs (a',a), (a',b), (a,b) lie in [β,b], belong to the family of the leg, λ(a',a) ≥ g − ε ≥ (K_f−2)λ ≥ ε/2,
λ(a',b) ≤ g + λ ≤ η_1R(1+1/K_f) ≤ R; so (J1), (J2), (CA) and Lemma 3.8 apply to them. Three bounds for |(x_a − x_{a'}) × e|:
1. (Prop 4.2) ≤ c(a',a)(|e_{a'a} − e_{a'b}| + |e_{a'b} − e|) ≤ C_p M g^{1+γ}.
2. By Lemma 2.5(b) with û = e: ≤ ∫_{a'}^{a}|T − e| ≤ (l(a',a)V_e(a',a))^{1/2}; V_e(a',a) ≤ V_e(a',b) (additivity, V ≥ 0)
   = N(a',b)² + c(a',b)|e_{a'b} − e|² ≤ M²(g+λ)^{1+2γ} + κ(g+λ)C_B²M²(g+λ)^{2γ} ((J2), (J1), Lemma 3.8 same right end);
   l(a',a) ≤ κg; with g + λ ≤ (1+1/K_f)g: ≤ C_p^V M g^{1+γ}, C_p^V := κ^{1/2}(1+κC_B²)^{1/2}(1+1/K_f)^{1/2+γ}.
3. Put u := e_{a'b}. Since (x_b − x_a) × e = 0, (x_a − x_{a'}) × e = (x_b − x_{a'}) × e = c(a',b) u × e, and
   c(a,b)(u × e) = u × (x_b − x_a) = ∫_a^b u × (T − u), so c(a,b)|u × e| ≤ ∫_a^b |T − u| ≤ (l(a,b)V_u(a,b))^{1/2} ≤ (κλ)^{1/2}N(a',b)
   (V_u(a,b) ≤ V_u(a',b) = N(a',b)², Lemma 2.5(b) with û = e_{a'b}). With c(a,b) ≥ c_Aλ, c(a',b) ≤ κ(g+λ), N(a',b) ≤ M(g+λ)^{1/2+γ}:
   ≤ (κ^{3/2}/c_A) M (g+λ)^{3/2+γ} λ^{−1/2} ≤ C_ar M g^{1+γ}(g/λ)^{1/2}, C_ar := κ^{3/2}(1+1/K_f)^{3/2+γ}/c_A.
Hence (iv), and β* ≤ (2κ^{3/2}/(πc_ρ*³)) vMλ^{3/2} g^{γ−2} Ĉ(g/λ).

*Result.* Lemma Du* on [t_∘,t] and the amplification bound give, as in Prop 4.2,
N(t) ≤ A_0(min(g(t_∘),K_RR)/ĝ)^ν N(t_∘) + A_0(K_RR/ĝ)^ν ∫_{g>η_1R}β* + A_0∫_{g≤η_1R}(g(τ)/g)^ν β*(τ)dτ.
*First term.* By (S2) (g(t_∘) = a, body pairs) resp. (TW) (g(t_∘) = g_W, tail pairs), and as g(t_∘) ≥ g > 0,
N(t_∘) ≤ s_0Mλ^{1/2+γ} min(1, K_fλ/min(g(t_∘),K_RR))^ν. So the weight of s_0Mλ^{1/2+γ} is
A_0(min(g(t_∘),K_RR,K_fλ)/ĝ)^ν, which is ≤ A_0(K_fλ/g)^ν ≤ A_0 if g ≤ K_RR (then ĝ = g ≥ K_fλ) and ≤ A_0 otherwise
(then ĝ = K_RR ≥ min(g(t_∘),K_RR)). The term is ≤ A_0s_0Mλ^{1/2+γ}.
*Second term*: (K_RR/ĝ)^ν ≤ (K_R/K_f)^ν(R/λ)^ν and λ^{3/2}(R/λ)^ν ≤ λ^{1/2+γ}R^{1−γ} (verbatim), so it is
≤ A_0(K_R/K_f)^ν vλ^{1/2+γ}R^{1−γ}(B_2U'J_2 + B_2η*/R) = A_0(K_R/K_f)^ν (v/m)(B_2U' R J_2(U_0) + B_2η*) Mλ^{1/2+γ}.
*Third term* (only if g ≤ η_1R): ≤ A_0(2κ^{3/2}/(πc_ρ*³)) vMλ^{3/2} g^{−ν}∫h(g(τ))dτ with
h(y) := y^{ν+γ−2}Ĉ(y/λ)1{y ≤ η_1R}, non-increasing (y^{ν+γ−2} and y^{ν+γ−3/2} are decreasing as ν+γ < 1, the minimum of two
non-increasing functions and the indicator are non-increasing). Lemma 3.6(i) (g_min = g): ∫h ≤ d_Lε h(g) + χ_g∫_g^∞ h. With
y = λx, x_0 := g/λ ≥ K_f, ε ≤ 2λ:
g^{−ν}∫h ≤ λ^{γ−1}·Φ(x_0), Φ(x_0) := x_0^{−ν}[2d_L x_0^{ν+γ−2}Ĉ(x_0) + χ_g∫_{x_0}^∞ x^{ν+γ−2}Ĉ(x)dx].
Φ is non-increasing (x_0^{−ν}·x_0^{ν+γ−2}Ĉ(x_0) = x_0^{γ−2}Ĉ(x_0) is non-increasing; x_0^{−ν}∫_{x_0}^∞(…) is a product of
non-negative non-increasing functions), so Φ(x_0) ≤ Φ(K_f) and the term is ≤ A_0 B_3' v Mλ^{1/2+γ},
B_3' := (2κ^{3/2}/(πc_ρ*³)) Φ(K_f). (With Ĉ ≡ C_p this is the old B_3K_f^{γ−1}(2d_L/K_f + χ_g/(1−γ−ν)) times c_ρ³/(πc_ρ*³).)
With v ≤ v0, U ≤ U_0, (P5*) gives N ≤ 𝔣Mλ^{1/2+γ}. ∎

### 2.7 Proposition L* (replaces Prop 4.4, `prop:length`) — PROVED

**Proposition L\*.** With δ := 0 for body pairs and δ_t for tail pairs,
l_t(a,b) ≤ (1+δ)exp(X_far*(U_0) + B_5* I_5 v0 m²)λ + v0κT_Iλ ≤ (1+δ)L_J*(U_0)λ < κλ.

*Proof.* As Prop 4.4, regime by regime. l(t_∘) ≤ (1+δ)λ.
*Far, g > K_RR.* l' = v∫sin²φ/ρ ≤ vl/ρ_* (Lemma 2.6(i), Step 0 of Lemma E*), so (log l)' ≤ v/ρ_*; by Lemma (J) (k = 1) the
increase of log l is ≤ v J_1(U_0).
*Far, η_1R < g ≤ K_RR.* (log l)' ≤ v/ρ_* ≤ v/(c_ηg) (Prop F*(ii)); Lemma 3.6(i) (g_0 = η_1R, h(y) = y^{−1}1{y≤K_RR}) gives
∫dτ/g ≤ d_L/(K_εη_1) + χ_g log(K_R/η_1); increase ≤ v(d_L/(K_εη_1) + χ_g log(K_R/η_1))/c_η.
*Far, g ≤ η_1R.* Lemma E*(b): (log l)' ≤ (v/ρ_*)[N/l^{1/2} + (|p_a| + l^{1/2}N/π)/ρ_*]². With ρ_* ≥ c_ρ*g, |p_a| ≤ C_p*Mg^{1+γ}
(Prop F*(iv), Ĉ ≤ C_p*), N/l^{1/2} ≤ Mλ^{1/2+γ}/λ^{1/2} = Mλ^γ ≤ K_f^{−γ}Mg^γ (l ≥ λ), l^{1/2}N ≤ κ^{1/2}Mλ^{1+γ} ≤
κ^{1/2}K_f^{−1−γ}Mg^{1+γ}: (log l)' ≤ B_5* vM²g^{2γ−1}, B_5* := (1/c_ρ*)[(C_p* + κ^{1/2}K_f^{−1−γ}/π)/c_ρ* + K_f^{−γ}]².
These times form a final segment of the far period with g ≤ η_1R; y ↦ y^{2γ−1} is non-decreasing (γ > 1/2), so
Lemma 3.6(ii) (ḡ = η_1R) gives ∫g^{2γ−1}dτ ≤ χ_g(η_1R + ε/κ)^{2γ}/(2γ) ≤ I_5R^{2γ} (ε ≤ R/K_ε); with M²R^{2γ} = m² the
increase of log l is ≤ B_5*I_5vm².
*Near* (unchanged from Prop 4.4). l' ≤ v[ω̃(ε)/ε + ∫_ε^∞ω̃(y)y^{−2}dy], ω̃(y) := |{s∈(a,b): ρ_s < y}| (arclength), since
a*(ρ) = ε^{−1}1{ρ<ε} + ∫_{max(ρ,ε)}^∞y^{−2}dy. By Lemma 3.7 (second form) ρ_s < y forces w_s < c_6y, so with (J1) for
(a, a+λ_y): ω̃(y) ≤ κ min(λ, c_6y), and ω̃(ε) > 0 only if g < c_6ε. Exactly as for Term I of Prop 4.3 (with κ in place of
C_μAM²λ^{2γ}): at most κc_6+1 legs have g < c_6ε (Lemma 3.6(iii)), each ≤ d_Lε long, contributing ≤ v d_L(κc_6+1)κλ; and
Lemma 3.6(i) with Lemma 4.1 gives ≤ vκ(d_Lλ + c_6χ_gΨ_Iλ). In total the increase while near is ≤ vκT_Iλ
(T_I = d_L(κc_6+2) + c_6χ_gΨ_I). (R-near may supply a smaller T_I; any valid near-length constant can be used.)
So l_t ≤ (1+δ)λ exp(X_far* + B_5*I_5v0m²) + v0κT_Iλ, X_far* := v0[J_1(U_0) + (d_L/(K_εη_1) + χ_g log(K_R/η_1))/c_η];
< κλ by (P7*) resp. (PT). ∎

---------------------------------------------------------------------------------------------------------------------

## 3. New constants and side conditions (Def 3.3 notation)

Unchanged: M, χ_g, c_6, c_t, σ_q, C_A, C_B, C_TL, C_μA, C_1A (tilt constants kept as symbols — R-tilt), r_f, Ψ_I, T_I, T_a, T_b,
k_0, D_I, D_IIs, D_IIl (near pairs — R-near), I_5.

| symbol | new formula | old formula | base point (v0 = 6e-5) new / old |
|---|---|---|---|
| c_ρ ★ | c_A − 2δ_1/K_f | c_A − (2δ_1+κ)/K_f | 0.5989 / 0.3972 |
| c_η ✚ | c_A − δ_1/(K_εη_1) | (c_ρ used) | 0.9949 |
| c_R ★ | c_AK_R − δ_1/K_ε | c_AK_R − δ_1/K_ε − κ | 31.82 / 30.81 |
| K_1, K_2 | c_ρK_f/κ, c_R/κ (with ★ values) | same | 2.97 / 1.97; 31.3 / 30.3 |
| aD* ✚ | 1 + 1/(πK) + 2/(π²K²) | aD(K) = 1+1/K+2/K² | aD*(K_1) = 1.130 / aD(K_1) = 2.02 |
| c_amp ★ | aD*(K_1)χ_g/c_ρ | aD(K_1)χ_g/c_ρ | 1.917 / 5.178 |
| J_1(U_0) ✚ | (3.1), k = 1 | (χ_gU_0/(c_RR)) | 198.1 (S1) / 10.9 (S1G); old 204 |
| J_2(U_0) ✚ | (3.1), k = 2 | (χ_gU_0/(c_RR)²) | 6140 (S1) / 95.7 (S1G) |
| B_2U' ✚ | 2κ^{3/2}(1+1/K_2)/π, enters as B_2U' R J_2 | B_2U χ_gU_0/R, B_2U = 2κ^{3/2}(1+1/K_2)/c_R² | B_2U'RJ_2 = 4.13 (S1) / 0.064 (S1G); old 14.2 |
| B_2η ★ | 2κ^{3/2}(1+1/K_1)(χ_g/η_1 + d_L/(K_εη_1²))/(πc_η²) | …/c_ρ² (no π) | 1.074 / 23.88 |
| C_p^V ✚ | κ^{1/2}(1+κC_T²)^{1/2}(1+1/K_f)^{1/2+γ} (C_T for C_B) | — | 3.823 [12.32] |
| C_p* ✚ | min(C_p', C_p^V) (C_p' of R-tilt) | C_p | 3.823 [12.32] / 12.64 |
| C_ar ✚ | κ^{3/2}(1+1/K_f)^{3/2+γ}/c_A | — | 1.53 |
| Ĉ(x) ✚ | min(C_p*, C_ar x^{1/2}) | C_p | |
| B_3' ✚ | (2κ^{3/2}/(πc_ρ³))K_f^{−ν}[2d_LK_f^{ν+γ−2}Ĉ(K_f) + χ_g∫_{K_f}^∞x^{ν+γ−2}Ĉ(x)dx] | B_3K_f^{γ−1}(2d_L/K_f + χ_g/(1−γ−ν)), B_3 = 2κ^{3/2}C_p/c_ρ³ | 18.5 [38.5] / 500 |
| B_5 ★ | (1/c_ρ)[(C_p* + κ^{1/2}K_f^{−1−γ}/π)/c_ρ + K_f^{−γ}]² | (2/c_ρ)[(C_p+κ^{1/2}K_f^{−1−γ})²/c_ρ² + K_f^{−2γ}] | 77.1 [735] / 5162 |
| X_far ★ | v0[J_1(U_0) + (d_L/(K_εη_1) + χ_g log(K_R/η_1))/c_η] | v0[χ_gU_0/(c_RR) + (…)/c_ρ] | 0.0121 (S1), 0.00088 (S1G) / 0.0128 |
| η_N ★ (Sec. 5/8) | aD*(4)v0/ζ | aD(4)v0/ζ | |
| c_β ★ (Sec. 5) | 2(1+δ_t)^{3/2}k_D^{γ−1}/(πζ³(1−γ)) | without 1/π | 1.054 / 3.310 |
| 𝒢, ρ_G, c_0' ✚ | Sec. 2.5, Prop F*(iii) | — | |

Closed form of the integral in B_3' (p := ν+γ−2, x_* := (C_p*/C_ar)²): if x_* > K_f,
∫_{K_f}^∞ x^pĈ = C_ar(x_*^{p+3/2} − K_f^{p+3/2})/(p+3/2) + C_p* x_*^{p+1}/(−p−1), and Ĉ(K_f) = C_ar K_f^{1/2};
otherwise ∫ = C_p*K_f^{p+1}/(−p−1), Ĉ(K_f) = C_p*.

**Side conditions** (★ changed; others unchanged):
* (P0) unchanged.
* (P1) unchanged.
* (P2★) c_ρ*K_f ≥ 2 (⇔ c_AK_f ≥ 2 + 2δ_1, i.e. K_f ≥ ≈ 4.0 instead of ≈ 5.0), c_R*K_ε ≥ 1, c_6 ≤ K_RK_ε.
* (P3★) c_amp* v0 ≤ ν.
* (P4★) v0[2aD*(K_1)d_L/(c_ρ*K_f) + aD*(K_2) J_1(U_0)] ≤ log A_0.
* (P5★) A_0[s_0 + (K_R/K_f)^ν (v0/m)(B_2U' R J_2(U_0) + B_2η*) + B_3' v0] ≤ 𝔣.
* (P6) unchanged (θ̄ = 𝔣² + 2v0D).
* (P7★) L_J*(U_0) := exp(X_far*(U_0) + B_5*I_5v0m²) + v0κT_I < κ; (PT) (1+δ_t)L_J*(U_max) < κ.
* With (S1G): Setting (H) gets (S1G) with 𝒢 of Section 2.5 — verified by the addendum to Lemma 8.2 for both tuples, no new
  numerical condition (T2* needs only (SC41)–(SC44), already checked).

### κ trade-off (formulas)
κ enters only through (J1). Larger κ helps (P7★) directly: (P7★) ⇔ X_far* + B_5*I_5v0m² < log(κ − v0κT_I), and
X_far* = v0κ d_L[𝒥 + log(K_R/η_1)/c_η] + O(v0/K_ε), with 𝒥 := J_1/χ_g (≈ U_0/(c_RR) ≈ 195 under (S1); ≈ 10–17 under (S1G)).
So the (P7★)-limit is v0 ≲ log κ /(κ(𝒥 + log(K_R/η_1)/c_η)), increasing in κ on (1, e) — from κ = 1.016 to κ = 4/3 the limit
grows by the factor (log(4/3)/(4/3))/(log 1.016/1.016) ≈ 13.6. The costs of κ (all monotone increasing in κ):
c_t ∝ κ^{1/2} ⇒ C_A, C_B, C_TL ∝ ≈κ^{1/2}, C_μA = 1+κC_A² ∝ ≈κ², C_1A ∝ ≈κ^{3/2}; near pairs D_I ∝ ≈κ³, D_IIs ∝ ≈κ⁴, D_IIl ∝ ≈κ^{5/2}
(so D ∝ ≈κ⁴, (P6) v0 < (1−𝔣²)/(2D)); far pairs K_1 ∝ 1/κ, B_2U', B_2η* ∝ κ^{3/2}, C_p ∝ κ^{3/2}, C_ar ∝ κ^{3/2}, B_3' ∝ κ³;
legs: Lemma 3.5(ii) needs κ ≤ 4/3; Lemma 8.x: catch time T_♯ = T_2 + κU_max/(1−v0) (the main theorem's time T_0 must grow:
κ = 4/3 gives T_♯ ≈ 12.3); assembly: D̄ ∝ κ, K_rot ∝ κ, C_3 ∝ κ^{1/2}. The optimiser (Section 5) includes all of these except the
D(κ) dependence (D is an input). With R-tilt's constants C_T ∝ κ^{1/2}, C_μ = 1+κC_T² ∝ ≈κ², and D enters through log C_μ and
profile shapes (R-tilt §3), so D(κ) is much flatter than the base ≈κ⁴; the reported optimal κ must be fed back to R-near/R-tilt.

---------------------------------------------------------------------------------------------------------------------

## 4. What each refinement buys (base point, v0 = 6e-5)

1. **Hull → arc** (Lemma E*): removes the κ/K_f loss in c_ρ (0.397 → 0.599) and κ from c_R; enters c_ρ³ in B_3, c_ρ² in B_5.
2. **Integration by parts + Wirtinger** (Lemma E*): the q-variation term no longer costs l/ρ: aD(K_1) = 2.02 → aD*(K_1) = 1.13,
   forcing ÷π. c_amp 5.18 → 1.92; (P3) is now harmless (ν = c_amp*v0 ≈ 2v0).
3. **c_η** in the middle regime (g > η_1R, where ε/g ≤ 1/(K_εη_1) ≈ 10⁻³): c_ρ → c_η ≈ 0.995 in B_2η and X_far.
4. **C_p^V, C_ar**: with the old tilt constants C_p* is 2.5% below C_p and Ĉ uses the direct-tilt bound for g/λ ≤ x_* ≈ 65
   (B_3' 47.6 → 38.5). With R-tilt's C_T, C_p^V = 3.82 ≈ C_p' = 3.85, x_* ≈ 6.3 ≈ K_f, so Ĉ gains little; the main gains on
   B_3/B_5 then come from c_ρ* and the 1/π (B_3: R-tilt 126 → 18.5 here).
5. **(S1G)**: J_1 204 → 10.9, J_2 6200 → 96. This is what unlocks (P7) and the B_2U-term at v0 ~ 1e-3.
6. **Departure drop-in**: η_N ÷ 1.26, c_β ÷ π: (TS) v0-term 286 → ≈ 208 (×R^{γ_D}) with old heading constants.

The (K_R/K_f)^ν factor: with ν = c_amp*v0 ≈ 2v0 it is (K_R/K_f)^{2v0} ≤ 1.01 for v0 ≤ 1e-3 — no further work needed.
A0: A_0 = exp(v0[2aD*(K_1)d_L/(c_ρK_f) + aD*(K_2)J_1]) ≈ 1 + 1.03 v0 J_1: 1 + 200v0 under (S1), 1 + 12v0 under (S1G).

---------------------------------------------------------------------------------------------------------------------

## 5. Optimisation with D as a free input (NUMERICAL)

Script `r9/far/far_opt.py` (outputs `far_opt_mode0.out` with (S1G), `far_opt_mode1.out` (S1) only), `r9/far/joint_near.py`
(fixed D ∈ {100, 50, 35}: `joint_near_fixedD.log`; joint with R-near's D′: `joint_near.out`). NUMERICAL, float.
What is optimised: all 18 free parameters (γ, R, m, κ, c_A, K_R, K_f, K_ε, η_1, q_c, γ_D − γ − ν − η_N, ω̄, c_k, δ_0/R and the
touch-down parameters ξ_1, η, λ_0, G_T); derived at their optimal values: d_L = 1/(1−v0), δ_1 = e^{2v0/(1−v0)}, ν = c_amp*v0,
A_0 = exp(P4*-lhs), 𝔣 = (1 − 2v0D)^{1/2}, s_0 = max allowed by (P5*) for both tuples. Conditions: (P0)–(P7) with the new
formulas, (N1) K_ε ≥ 2 (R-near), (T1)–(T4) (R-tilt), (C1)–(C6), (A2)–(A6), (TS), (PT), (SC1)–(SC48) at v̄ = v0 (touch-down
constants recomputed exactly at v̄ = v0, not outward-rounded), the "extra" conditions except the two deleted by R-tilt.
Dropped: T_♯ ≤ 10.13 (T_0 is reported as an output). Tilt constants: R-tilt. Bisection in log v0 (≤ 2% resolution).

### 5.1 D as a fixed input

| D | v_max with (S1G) | v_max with (S1) only |
|---|---|---|
| 7300 | 6.79e-5 | 6.79e-5 |
| 1000 | 4.95e-4 | 4.95e-4 |
| 545 | 9.13e-4 | 9.10e-4 |
| 500 | 9.97e-4 | 9.94e-4 |
| 300 | 1.66e-3 | 1.61e-3 |
| 200 | 2.48e-3 | 2.11e-3 |
| 100 | 4.63e-3 | 1.85e-3 – 2.36e-3 |
| 50 | 6.38e-3 | 2.01e-3 |
| 35 | **6.69e-3** | (run stopped) |

(Two runs at D = 100 without (S1G): 2.36e-3 in the D-sweep, 1.85e-3 with (N1) added; the optimiser is a multistart local search,
so values are lower bounds of the true maximum.) Down to D ≈ 300 (P6) binds in both modes. Below that:
* **with (S1G)**, at D = 35, v0 = 6.69e-3: binding (relative slack ≤ 6e-4): (PT) (1+δ_t)L_J < κ, (TS), κ ≤ 4/3, η_1 ≤ K_f/(K_f+1),
  K_f + 1 ≤ K_R, and (P6) (by construction). Parameters: γ 0.5904, R 2.254e-3, m 0.1285, κ 1.33257, c_A 0.99575, K_R 9.090,
  K_f 8.085, K_ε 1.92e4, η_1 0.8894, q_c 2.451, γ_D 0.6299, ν 0.01301, A_0 1.1474, s_0 0.3759, 𝔣 0.7293, ω̄ 0.4168, c_k 1.0081,
  δ_0/R 0.3132, ξ_1 1.0430, η 0.1641, λ_0 0.0531, G_T 0.0304; c_ρ* 0.745, c_amp* 1.95, J_1 19.2, B_3' 19.5, B_5* 75, X_far 0.149,
  L_J 1.312; touch-down at v̄ = 6.69e-3: c_N 3.36, μ̄_T 0.0199, k_c 0.924, U_max 7.26; T_♯ = 13.5.
* **(S1) only**: v0 saturates at ≈ 2e-3 for D ≤ 100: (P7)/(PT) with κ → 4/3 binds (J_1 ≈ 100–113, X_far ≈ 0.22), together
  with (C2), κ ≤ 4/3, c_k ≥ 1, γ_D ≥ γ + ν + η_N.

**Caveat (important): D = 35 is R-near's value at κ − c_A = 0.0198.** The fixed-D optimum above has κ − c_A = 0.337, where
R-near's D′ is ≈ 105–120, not 35. So 6.69e-3 is NOT an honest joint value. See 5.2.

### 5.2 Joint optimum with R-near's D′(p)

D′ grows with κ − c_A (R-near's offset route 𝔭_L ∝ √(κ − c_A), capped by the 1/D route). R-near's code (quick resolution, ≥ the
fine value) at the base values of the other parameters:

| κ − c_A | 0.004 | 0.008 | 0.0198 | 0.04 | 0.08 | 0.15 | 0.3 |
|---|---|---|---|---|---|---|---|
| D′ | 29.96 | 30.18 | 35.42 | 48.69 | 70.60 | 86.09 | 104.29 |

`joint_near.py` optimises with D = F·table(κ − c_A), re-evaluates D′ with R-near's code at the optimised parameter vector
(all of γ, R, m, κ, c_A, K_R, K_f, K_ε, q_c, d_L, δ_1), raises F and repeats until D′(p_opt) ≤ D used; the final point is
re-checked at R-near's fine resolution.

**Result (with (S1G)), best honest point found: v0 = 4.146e-3.** One iteration sufficed: D used = 98.68 (= table value at
κ − c_A = 0.2457), D′(p_opt) by R-near's code = 65.76 (quick) / **60.63 (fine)** ≤ 98.68, so (P6) holds with the true D′
(f² + 2v0·60.63 = 0.684 < 1). Because D used exceeds the true D′ by 60%, this is a lower bound for the joint optimum; another
iteration with F ≈ 0.62 would raise v0 (not run — wrap-up requested). The (S1)-only joint run was stopped before finishing;
by 5.1 it is capped at ≈ 2e-3 anyway.
Full parameter vector (main tuple; stage A has γ → γ_D):
γ 0.535802, R 3.71314e-5, m 0.20266, κ 1.24215, c_A 0.996499, K_R 9.7615, K_f 8.76065, K_ε 54.9022, η_1 0.516085,
q_c 1.9347, γ_D 0.547994, ν 0.00719246, A_0 1.13138, s_0 0.264317, 𝔣 0.426366, d_L = 1/(1−v0), δ_1 = e^{2v0/(1−v0)};
assembly ω̄ 0.405167, c_k 1.00009, δ_0 = 0.0506271R, ε_S = 4e-11; touch-down (v̄ = v0) ξ_1 2.42695, η 0.131449, ε̄ 1e-3,
λ_0 0.010607, G_T 4.16113e-4.
Derived: c_ρ* 0.766, c_η 0.961, c_R* 9.71, c_amp* 1.73, J_1 28.2, J_2 1.14e4, B_2U' 0.994, B_2η* 2.81, C_p' 5.31, B_3' 11.2,
B_5* 68.7, X_far 0.133, L_J 1.2274; touch-down c_N 6.41, μ̄_T 0.0124, k_c 0.955, U_max 6.90, W_xL̂ 1.162; T_♯ = 12.36.
**Binding conditions** (relative slack ≤ 2e-3): γ_D ≥ γ + ν + η_N (A5) 4.5e-5; **(PT)** (1+δ_t)L_J < κ 5.8e-5;
K_f + 1 ≤ K_R (P0) 8.7e-5; c_k ≥ 1 (A4) 9.4e-5; **(TS)** 1.5e-4; ω_0 ≤ ω̄ (A4) 1.6e-4; U_E ≤ G_T (A4) 2.0e-3; and by
construction (P4*), (P5*) (A_0, s_0 saturated). Not binding: (P6) with the true D′ (slack 0.32), (P2*), (P3*), (C2).
So after E*/F*/L*/T2* the obstruction is the **length condition (PT)/(P7) together with the assembly's (TS)** and the range
conditions of the departure/heading (A4), (A5); κ settles at 1.24 because D′ grows with κ − c_A.
Caveats: float arithmetic; touch-down constants exact at v̄ = v0 but not outward-rounded; D′ from R-near's double-precision
code (their certified interval value exists only at the base parameters) — a proof at this point needs R-near's interval
evaluation at this parameter vector and the outward-rounded verify_constants run (stream Opt). The point is extreme in places
(R = 3.7e-5, G_T = 4.2e-4, ξ_1 = 2.43); v0 = 4.1e-3 with rounder parameters should be re-derived by Opt.
(For comparison, the user's target 6.7e-3 is the fixed-D = 35 value of 5.1, which assumes κ − c_A ≈ 0.02 while using
κ − c_A = 0.34; it is not supported by the joint computation.)

### 5.3 Which new lemmas the result needs
* Every v0 above 8e-5 needs **E*, Du*, F*, L*** (without them (P5) and (P7) bind near 1e-4: old B_3 = 413, c_amp = 5.2,
  X_far ≈ 204v0·…, see §0).
* **(S1)-only route** (no new touch-down input): needs E*, Du* (incl. the departure drop-in), Lemma 3.7 (first form), F*, L*,
  R-tilt, R-near. Ceiling ≈ 2e-3, set by (P7)/(PT): X_far ≥ v0χ_gU_0/(c_RR) with κ ≤ 4/3.
* **(S1G) route** (v0 beyond ≈ 2e-3): additionally Lemma T2*, the (S1G) addendum to Lemma 8.2, Lemma 3.7(iii), Lemma 3.6(iv)
  and Lemma (J). Then (P7)/(PT) still bind (κ → 4/3) together with (TS), (P6) and parameter-range conditions.
* Not needed at the optimum: the Ĉ refinement (bound 3 of Prop F*(iv)) and C_p^V change B_3' by < 10% with R-tilt's C_T;
  they can be dropped for a simpler text (then B_3' = (2κ^{3/2}C_p'/(πc_ρ*³))K_f^{γ−1}(2d_L/K_f + χ_g/(1−γ−ν))).


---------------------------------------------------------------------------------------------------------------------

## 6. Scope, caveats, coordination

* **Interfaces.** Prop F* and Prop L* have the same role and statement shape as Prop 4.2/4.4 (the lower bounds on the hull
  distance ρ_m become bounds on the arc distance ρ_* ≥ ρ_m; Prop L* uses only Prop F*(i)–(iv)). Lemma E*/Du* replace
  Lemma 2.6(v)/2.7 everywhere (Prop 4.2, Theorem 5.2(v)). Lemma 3.6(iv), Lemma 3.7(iii), (S1G), T2* are additions.
* **Coordination with R-near** (`reports/R9-near.md` did not exist when this was written): I used only the first form of
  Lemma 3.7 (ρ_s ≥ c_A min(w,K_RR) − δ_1ε) and its new item (iii); a two-regime bound of R-near changes nothing here. The
  near-pair constants (c_6, T_I, D) enter (P7★) only through v0κT_I.
* **Coordination with R-tilt**: C_A, C_B, c_t(r_f) appear only in C_p, C_p^V (symbols).
* **Not done**: (a) a sharper bound of |p_a| for g > η_1R (needs front geometry at scale > R); (b) a sharper first term
  v∫(T−e)·A(T−e) − (v/2)∫(e·Ae)|T−e|² (the NUMERICAL test shows bound (a) is attained to 1% in the worst case, so little is
  left in Lemma E* itself); (c) the touch-down constants in the script are exact values at v̄ = v0, not outward-rounded, and
  the touch-down parameters (ξ_1, η, λ_0, G_T) are re-optimised — ξ_1 = 1.007 violates (SC17) for v̄ ≳ 3e-4.
