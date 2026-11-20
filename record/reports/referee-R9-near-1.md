# Referee report R9-near-1: Proposition 4.3'' (near pairs) and Lemma E (D' <= 34.99)

**Object under review.** `r9/near/prop_near.tex`, the full statements and proofs that `referee/R9-near-claims.md` summarizes.
**Also read.** `r9/near/near_const.py` and `.out`, which define and evaluate 𝒟(θ,r) and D'. From the base: `r9/base_short/sec2–sec4`,
Def 3.3, (P0)–(P7) and the end-theorem completion. Also `verify_constants.out` (INPUTS) and `referee/R9-tilt-claims.md`, whose
statements I assume as instructed.
**Not read.** `reports/R9-near.md`.
The first version of this report was written under a brief that withheld `r9/near/`. It is superseded by this version.
**Certification code.** `code/referee/R9near_1/cert_Dprime.py`. Its outputs are `cert_p.out`, `cert_pA.out` and `cert_p_old.out`.

## Verdict summary

| claim | verdict |
|---|---|
| N-D Lemma D (distance, a*) | **OK** |
| N-B Lemma B (budgets) | **OK** |
| N-L Lemma L (layer cake) | **OK** |
| N-S Lemma S (split tilt) | **OK** |
| N-O Lemma O (i)–(iv) | **OK**, given (N1). (N1) must be added to (P0) and to verify_constants. |
| N-A Lemma A (leg time averages) | **OK** |
| N-Σ Lemma Σ (leg sums) | **OK** |
| N-P Prop 4.3'' | **OK with fixes F1–F3**: the proof is correct and covers every near-phase case, but the Def 3.3 edits as written break Prop length / (P7). |
| N-E Lemma E: D' <= 34.99 at p | **OK, now certified**: D'(p) <= **34.98732** (mpmath.iv plus directed rounding, C_T = 2.911 rounded up). |
| N-E Lemma E: D' <= 42.40 (Def 3.3 constants) | **OK, certified**: D'(p) <= **42.39796**. |
| (new) D' at the stage-A tuple p_A | **Needed and missing (F4)**. Certified: D'(p_A) <= **35.00458**, which is *above* 34.99. The bound 34.99 must not be quoted for p_A. (P6) holds at p_A regardless: θ̄ <= 0.022960. |
| N-X, N-Sim | NUMERICAL. Consistent with the above. Not used. |

Resulting θ̄ = f_F² + 2v₀D' <= **0.022958** at p and <= **0.022960** at p_A. (P6) needs θ̄ < 1, so the slack is huge (it was 0.8975).

## 1. Line-by-line check of prop_near.tex

**Definitions (lines 7–45).** θ = ε/λ ∈ (0,2] since λ >= ε/2. r = R/λ >= 1, and ε <= R/K_ε gives r >= K_εθ. So the domain of the
sup in D' contains every pair that actually occurs. The Stieltjes convention (atom Φ(0) at 0) matches Lemma L. Two points:
- C* = C_A + C_B is the route-3 constant. With R-tilt it is 2C_T, matching near_const.py (`CTL = 2*CT`).
- C_V = (1+κC_B²)^{1/2}.

**Lemma D.** w_s <= g+λ < (K_f+1)λ <= (K_f+1)R <= K_R R ((P0), λ <= R), so lem:dist gives D >= max(ε, c_A w_s − δ₁ε) = λφ_θ.
If ρ < ε, then a* = 2/ε = 1/D + 1/ε, and c_A w − δ₁ε <= ρ < ε gives w < c₆ε. Correct for short-type and long-type times alike.
lem:local(ii) supplies the hypotheses of lem:dist, including tail pairs after t_W (τ > t_W, base ≥ a_{jW} ≥ W_e) and pairs ending at
the cut b = U.

**Lemma B.** (a, a+λ_s) is a family pair (first point a, length in [ε/2, λ]) inside [β, max(b,β⁺)], so it is admissible.
(E-μ) (or R-tilt T(ii)) together with static(b)+(J2) gives Ω <= μ²λΩ̄. Then Cauchy–Schwarz with l(a,s) <= κλ_s, and |ϑ| <= |T−e|. OK.

**Lemma L.** The level sets of a non-increasing ψ are initial segments [0,σ_t) or [0,σ_t]. ν([0,σ_t)) <= Φ(σ_t−) follows by
monotone limits. OK.

**Lemma S.** V_{I'}×e_{I'} = 0 gives Z = |∫_J (T−e_{I'})×e_{I'}| = |∫_L ...|. Cauchy–Schwarz twice, then add the two bounds with
static(b) (û = e_{I'}). V_J×e_J = 0 gives V_L×e = V_{I'}×e, and c(I') <= c(L)+c(J). OK.

**Lemma O.**
- (iv): a near pair with g > 0 has a ≠ β, so a >= β⁺. Lemma legs(i) gives β⁺−β >= ε/κ for a non-final leg. A final leg has
  β⁺ = U > a, so no g > 0 pair exists there. OK.
- Lengths, case g' < ε/2: then a' = β⁺, since a' = β with 0 < g < ε/2 is impossible by (iv). (a', a'+ε/2) ⊂ [β, b] because
  b = a+λ >= β⁺+ε/2. OK.
- Lengths, case g' > R (long-type only): the covering pieces start at a' or at >= a'+R/2 >= β+ε >= β⁺, which needs **(N1) K_ε >= 2**.
  They lie in [β,b] and are admissible. The same covering gives l(I') <= κΛ. OK.
- (i): I' is a family pair (Λ <= g+λ <= R).
  - Route 1: static(b) gives ∫_{I'}|T−e|² <= (1+κC_B²)M²Λ^{1+2γ}.
  - Route 2: Lemma S with (u,v) ↦ uv/(u+v) increasing.
  - Route 3: |e_L×e| <= |e_L−e|, the two tilts with C_A (same left end) and C_B (same right end), and L a family pair when
    g' >= ε/2.
  Normalizing by μλ gives the three entries of 𝔭 exactly. OK.
- (ii): I' is good. For a' = β use local(ii) with s = b. For a' = β⁺ use U−b >= W_e for body pairs, and β >= a_{jW} >= W_e for tail
  pairs. Λ ∈ [ε/2, K_R R) gives (CA) c >= c_AΛ, so N² = 2(l−c) <= 2(κ−c_A)Λ. Route 2 then gives λ𝔭_L. OK.
- (iii), g = 0 with β⁺ <= b: G(σ⁺) with σ⁺ <= min(θ,1). OK.
- (iii), g = 0 with β⁺ > b: then θ > 1 and I₀ = (β,β⁺) is a family pair.
  - (a) is the C_A tilt with λ_{I₀} <= ε.
  - (b) uses x_b−x_a ∥ e, l(b,β⁺) <= κε−c_Aλ, and ∫_{I₀}|T−e|² <= C_μM²ε^{1+2γ}.
  - (c) is Lemma S with l(J)l(L)/l(I₀) <= l(I₀)/4.
  Normalizations check. P₀ takes the max over both sub-cases. OK.

**Lemma A.** By chase(1), s = σ/(σ+ρ), and σ+ρ = c(β,β⁺;τ) >= c₀ by lem:sep(c).
- 1−s <= ρ/c₀ <= 1−(1−v)τ'/c₀, which integrates to c₀/(2(1−v)) <= d_Lε/2.
- s <= min(1, (1+v)τ'/c₀), which integrates over [0, c₀/(1−v)] to c₀(1+3v)/(2(1−v²)) <= c₀(1+2v)/(2(1−v)) = c₀(3/(1−v)−2)/2
  <= (3d_L−2)ε/2.
- Partial legs: the integrands are non-negative. The final leg is not walked (s ≡ 0). I re-derived both bounds independently.
- The Y-bounds used against these averages are uniform in τ over the leg, since they depend only on g, which is constant on legs.
  This was the flag in my first version; it is resolved.

**Lemma Σ.** Gap values on distinct legs differ by >= ε/κ (gapint preamble), and at most one leg has g = 0. In increasing order,
z_k >= kθ/κ and z_n < K_f, so n <= k*. With H* non-increasing, both the discrete form and the integral form follow. OK.

**Prop 4.3''.**
- Start value: the same two cases as the original. Case 1 is [t_td, t] (tail pairs are far at t_W by (TW), so only body pairs) with
  (S2). Case 2 is Prop far at t_n, or (TW) if t_n = t_W.
- Term I: Lemmas D, B, L with ψ_I non-increasing.
- Term II offset route: lem:field(iii), |p(s)| <= G(σ)+|p_a|, d(G²/2) = G dG, Lemma L twice.
- Term II 1/D route: |p| <= ρ, and μ = m r^{-γ}.
- Per leg: duration <= d_Lε = d_Lθλ (legs(iv)), plus Lemma A for |p_a|. Short/long type is constant on a leg. A min of valid
  leg bounds is valid. The g = 0 leg gives H₀. Sum by Lemma Σ.

All algebra and normalizations were checked. **Case coverage is complete:**

| case | how it is covered |
|---|---|
| start values | the two cases above |
| tail pairs after t_W | Lemma D and O(ii) |
| g = 0 leg, β⁺ <= b and β⁺ > b | O(iii) and H₀ |
| a = β⁺ (y⁺ = 0) | 𝔭*(0) = 0 |
| short and long legs | S_r, L_r, and r >= K_f+1 is all short-type |
| the cut (b <= U = b_c) | lem:dist hypotheses via local(ii) |
| final leg | s ≡ 0, and no g > 0 pair exists |
| partial last leg | integrands non-negative |

### Fixes required (exact text)

- **F1 (error in "Changes to Definition 3.3").** Line 8 deletes T_I, but T_I is still used by Prop length
  (`l_t <= ... + v₀κT_Iλ`) and by L_J(U₀), which (P7) checks. Replace line 8 by: "Delete T_α, T_β, k₀, D_I, D_IIs, D_IIl. Keep
  Ψ_I and T_I (used in Proposition 4.4 and in L_J(U₀))."
- **F2 (dangling reference).** Prop length's "Near" paragraph says "As in Term I of Proposition prop:near, with (J1) for
  (a, a+λ_y) in place of (E-μ)". That ω-argument no longer exists. Insert the old Term-I set inclusion verbatim into Prop length:
  "for y >= ε, if (y+δ₁ε)/c_A <= K_RR then by Lemma dist ρ_s < y forces w_s < c₆y, so these s lie in (a, a+λ_y),
  λ_y := min(λ, max(c₆y−g, ε/2)) <= min(λ, c₆y); otherwise c₆y > K_RR >= λ; and ω̃(ε) > 0 only if g < c₆ε."
  The constant T_I is unchanged.
- **F3 (θ̄ and side conditions).** In Def 3.3, replace θ̄ by f_F² + 2v₀D', with D' as boxed on line 41. Replace K_ε >= 3/2 by
  **(N1) K_ε >= 2** in (P0). In `verify_constants.py`, check (N1) and recompute θ̄ (P6) from a certified D' at **both** tuples.
- **F4 (Lemma E scope).** verify_constants checks (P6) at p and at p_A (γ ↦ γ_D), but Lemma E evaluates D' only at p. Add:
  "At p_A, D' <= 35.01 (certified, C_T^A <= 2.911)". Do not reuse 34.99 for p_A.
- **F5 (Lemma E wording).** Replace "Floating-point rounding is not controlled by interval arithmetic" by a citation of the
  certified evaluation (Section 3).

## 2. Audit of the reductions used to bound sup 𝒟 (Lemma E(i)–(iii), near_const.py)

Each reduction below is **proved** (P) or **refuted** (R). None was refuted. "T-weighted" means the term carries a factor θ.

| # | reduction | status / proof |
|---|---|---|
| M1 | φ_θ(w) >= max(θ_l, c_Aw − δ₁θ_h) on [θ_l, θ_h] | P: trivial |
| M2 | θ/φ_θ(w) is non-decreasing in θ, so it is <= θ_h/φ_{θ_h}(w) | P: it equals 1 if c_Aw−δ₁θ <= θ, else θ/(c_Aw−δ₁θ); both pieces increase in θ |
| M3 | Ω̄, Q̄, Ḡ non-decreasing in θ (via λ_σ = max(σ,θ/2)) | P. Lemma L only needs the cumulative bound Ω <= μ²λΩ̄_θ <= μ²λΩ̄_{θ_h}, so using Φ_{θ_h} as the Stieltjes integrator is valid. |
| M4 | 𝔭 non-decreasing in θ | P: ℓ increases. Entries 1 and 2 increase in ℓ (ℓ/(1+ℓ) increases). Entry 3 drops out as θ grows, and a min over fewer entries is larger. |
| M5 | 𝔭 non-decreasing in y on [θ/2, ∞) (needed for evaluation at x_r) | P: each entry increases. Non-bottom cells have x >= θ_l/κ >= θ_h/2, because 1.03κ < 2. |
| M6 | 𝔭* formula | P: 𝔭 increases on (0, θ/2) (ℓ fixed) and on [θ/2, ∞), with a possible drop at θ/2, so sup_{[0,z]} = max(left limit, 𝔭(z)). This is near_const.py's `pstar`. |
| M7 | 𝔭_L increasing in y and θ | P |
| M8 | P₀ non-decreasing in θ | P: on (0,1], Ḡ_θ(θ) = (κθ min(1, C_μθ))^{1/2}. At θ = 1 the left limit is κ^{1/2} <= the right value. For θ > 1 each min-entry increases, since κ > c_A. |
| M9 | 1{w < c₆θ} non-decreasing in θ | P. The H-version carries 1/θ, which is bounded by 1/θ_l (`IND_T/th_lo`). |
| M10 | k*(θ) <= k*(θ_l) and H*(kθ/κ) <= H*(kθ_l/κ) | P: H* is non-increasing and is built from a θ-uniform majorant. |
| M11 | Kernels taken at the left x-end, increasing factors at x_r | P: φ_θ(x+σ) increases in x, and 1{x+σ < c₆θ} decreases in x. |
| M12 | r-direction: r^γ <= r_h^γ (short); r^γ < (1+x)^γ (long); mixed cells take the max; r >= K_f+1 is all short-type with the 𝔭_L entry dropped | P: dropping a min-entry only enlarges the bound. This covers r -> ∞ uniformly. |
| M13 | Inner integrals by upper Riemann–Stieltjes sums | P: the kernel is non-increasing in σ, the integrator Φ is continuous on (0,1], and the atom is counted with ψ(0). |
| M14 | Bottom cell: φ_θ >= max(w/c₆, c_Aw − δ₁θ_b) | P: if w <= c₆θ, use θ >= w/c₆; else c_Aw − δ₁θ >= c_Aw − δ₁w/c₆ = w/c₆. |
| M15 | Bottom cell budgets: F(max(σ,θ/2)) <= F(σ) + F(θ/2) | P. The atoms (C_μθ/2, κC_μθ²/4, C_1Aθ/2) paired with θ/φ <= M_x are each checked. |
| M16 | Bottom gap-0 first σ-cell replaced by 2κC_μc₆s₁ | P: θ/φ² <= c₆/σ and dQ_c = 2κC_μσ dσ (s₁ = 1e-15 <= 1/C_μ). |
| M17 | Closed-form majorants on (0, x₁] for 𝔦, 𝔮, 𝔧₂, 𝔧₁ | P, each re-derived: atom + ∫₀^{u_c} + ∫_{u_c}^1 with 1/φ <= c₆/w. |
| M18 | 𝔭 <= (1+x)^{γ+1/2}κC*x and 𝔭* <= (1+x)^{γ+1/2}C_V(κx)^{1/2} on (0, x₁] | P: uses x >= θ/κ >= θ/2 and ℓ <= x (κ <= 2). |
| M19 | ∫(a_l x + b_l√x)(c/x + d) <= the code's I_cr; T_cr bounds θH*(θ/κ) | P: d·x is replaced by d·x₁ to make it monotone. z ↦ zH_crude(z) is increasing (z log(1+u/z) increases), so κzH(z) <= κx₁H(x₁). |
| M20 | ∫₀^x log(1+u/t) dt = x log(1+u/x) + u log(1+x/u) | P: differentiate. |

I found no bugs in near_const.py's logic: every printed cell value is an upper bound, apart from floating-point rounding.

## 3. Certified evaluation (code/referee/R9near_1/cert_Dprime.py)

**Method.** The cell scheme is the same as in near_const.py (q = 1.03, n_x = 500, n_s = 700, dr = 0.05; 570 θ-cells), with every
quantity bounded rigorously:
- **Constants.** The parameters, taken as decimal strings from the INPUTS line of verify_constants.out, are evaluated in
  **mpmath.iv**: C_T = 2.911 (rounded up from 2.9108574), C_μ = 1 + κC_T² ∈ [9.6089953, 9.6089954] (rounded up, as the brief
  required), C_V, C_1A, c₆, P₀, all bottom-cell closed forms (logs, powers) and r_h^γ. Each is converted to float64 with one
  outward ulp.
- **(1+y)^γ.** Majorized by a table T_j >= (1+jh)^{γ_hi}, h = 2^-15, computed with mpmath.iv and read at j = ceil(y/h).
- **Arrays.** IEEE float64 (+, −, ×, ÷, sqrt are correctly rounded), each result pushed one ulp outward with np.nextafter.
  Denominators and subtracted terms use lower bounds. max and min are exact.
- **Sums.** All dot products and sums have non-negative terms and at most 5·10⁴ of them. They are inflated by (1+10⁻¹¹), which
  exceeds γ_n (Higham Thm 3.1; valid for any summation order, with or without FMA).
- **Grid endpoints.** Cell endpoints are exact shared floats, covering θ ∈ (0, 2] and r ∈ [max(1, K_ε θ_l)↓, (K_f+1)↑] plus the
  r >= K_f+1 region. The x-grid runs from (θ_l/κ)↓ to K_f↑.

**Results** (runtime about 150 s each):

| tuple / constants | certified D' <= | float value (near_const.out) | θ̄ <= |
|---|---|---|---|
| p, R-tilt (C_T <= 2.911) | **34.98732** | 34.987 (C_T = 2.9108574) | 0.0229571 |
| p_A (γ_D = 0.614666), C_T^A <= 2.911 | **35.00458** | not computed by author | 0.0229592 |
| p, Def 3.3 constants | **42.39796** | 42.398 | 0.0238464 |

The worst cell at p is θ ∈ [0.005620, 0.005789], r ∈ [5.620, 5.670]: long-type, and close to the r >= K_εθ edge.

So **34.99 is a rigorous upper bound at p** under R-tilt's C_T <= 2.911. That still depends on R-tilt Lemma T, which is refereed
separately. With base constants, 42.40 is rigorous unconditionally. At p_A, the certified bound is 35.005 > 34.99 (F4).

**Residual assumptions.**
- IEEE-754 round-to-nearest for float64 basic operations and sqrt (standard on x86-64).
- mpmath.iv correctness.
- C_T <= 2.911 at p and C_T^A <= 2.911 at p_A, taken from R-tilt (2.91086 and 2.9094).

**Cross-check.** The certified values exceed near_const.py's float values by less than 10⁻³ relative, as expected from rounding
C_T up.

## 4. Points kept from the first version
- (N1) K_ε >= 2 is required by Lemma O's covering (lengths for g' > R, and l(I') <= κΛ). prop_near.tex states it (line 45); it must
  be added to (P0) and verify_constants (F3).
- The brief's C_μ = 9.608 was rounded down (true value 9.60815). The certified run uses 9.608995..., from C_T = 2.911.
