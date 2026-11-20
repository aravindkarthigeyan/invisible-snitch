# Referee report RQ3-1 on `referee/Q3-claims.md` (touch-down theorem for design T with constants explicit in v̄, η)

Independent referee. I read `referee/Q3-claims.md` in full, `paper/sec_T1.tex` (all of it), hyp:HT in `paper/sec_T2.tex`, and
the cited parts of `sec_B.tex` (Lemma B-VC, definition of F, f, a\*) and `sec_ST.tex` (Lemma ST-D0). I did **not** read
`reports/Q3-1.md` or `code/Q3/`. All my code is in `code/referee/Q3_1/`:

| file | content |
|---|---|
| `consts.py` | my own implementation of every constant of §0.3 and of (SC1)–(SC50) from the claims text, 50 digits, plus two implicit conditions I found (`i1`, `i2`, see §3) |
| `table.py`, `table_out.txt` | constants table vs (v̄, η), ε̄ = 10⁻³, with my own choices of x₁, λ₀, G |
| `mono.py` | direction of every named constant as a function of v̄ (supporting evidence for rule (M)) |
| `ode.py` | direct integration (mpmath Taylor solver, 40 digits) of S′ = v(S−P)/|S−P| for design T together with the first and second variational equations in the label → position, ψ, w, k of the true front at t_s; α₀, ρ₀, β\*, t_s, x_e computed from the ODE only |
| `verify.py`, `verify_v*.txt` | comparison of the ODE data with the bounds of Q3, Q5, Q6 at v̄ = v (worst case allowed by rule (M)), and exactness checks of Lemmas 2, 3 and the tilt formula, for v ∈ {10⁻⁶, 10⁻⁴, 10⁻³, 10⁻², 2·10⁻²} (η = 0.1, and also η = 0.15 at v = 2·10⁻²), ε = 10⁻³ |
| `virt_chord.py`, `vc_*.txt` | Lemma Q4 (virtual labels 0 < x ≤ ε) and Lemma Q7 (chords of mixed virtual/true pairs through the ε-disc), at v = 10⁻³ and 2·10⁻² |

## 0. Summary of verdicts

| claim | verdict |
|---|---|
| Lemma Q1 (run 1) | **OK** |
| Lemma Q2 (data at t₁ on the window) | **OK** |
| Lemma Q3 (forward arc) | **OK** |
| Lemma Q4 (virtual labels near X₀) | **OK** |
| Lemma Q5 (tail, E_Y, seen labels) | **OK** |
| Lemma Q6 (bulk and hole) | **OK** (the bound K_b is valid but very crude for v̄ ≥ 10⁻²; remark only) |
| Lemma Q7 (chords) | **OK** |
| Theorem Q.H | **OK with fixes** (two implicit side conditions to be added to the (SC) list; text fixes in §3) |
| Corollary Q.T | **OK** for the columns I recomputed (I did not see the authors' table; my table of §4 agrees with every number of HT′ and with the remark of §9) |
| Theorem HT′ | **OK** (every constant reproduced to all printed digits, §5) |
| §10.2: gap in the far case of (T1) in thm:HT | **Gap confirmed** (the step is reversed); statement of thm:HT (T1) **true**; author's repair **correct**. Prop. P8a.1(2) = prop:T1-arcs(2) **has the same defect**. A shorter repair that keeps the original constant 0.36 is given in §6. |

No FALSE statement found. No proof rests on a grid of (v, ε): every inequality is either exact in v or obtained from the v̄-value by
a monotone substitution which I checked term by term (§2), and the (SC) are finitely many numerical inequalities at the fixed
parameter tuple.

## 1. The four points the author asked to check first

### (1) The exact tilt formula (θ_v = 1.07 instead of 1.69)
Re-derived. From lem:T1-first, Im Ξ = τ^v c, so Y_r = cτ^v/a = (τ/τ_b)^v·(τ_b^v ∂_θC)/a. With ∂_θC = g(b)A + r g′(b)∂_θb,
g′ = g(cos b − v)/sin b, τ_b^v g(b) = 2τ_b/(1+τ_b²) and τ_b^v g(b)/sin b = 1 one gets exactly
τ_b^v∂_θC = 2τ_bA/(1+τ_b²) + r∂_θb(cos b − v), as claimed in Q2(c). The old proof bounded y·∂_θ log C by (sup y)(sup ∂log C),
i.e. 0.6124 ξ² · 2.7327/ξ, which is the product of two extremal values that are not attained simultaneously (≈ 1.69); the new
bound only loses the factor rΛ_max/2 ≈ 1.03 against the value rΛ/2 = 1 at α₀. The tilt is then exact (rem:T1-tilt), and the
numerator/denominator bounds of Q3(c), Q5(c) are correct (on the tail D_ψ ≥ 1 because cos β < −v and Y_r < 0).
**Numerics** (40-digit ODE, front at t_s): |ψ|/x^{1−μ} on the forward arc = 1.0000 (v = 10⁻⁶), 1.00003 (10⁻⁴), 1.00027 (10⁻³),
1.0027 (10⁻²), 1.0053 (2·10⁻²) for x up to η; bound θ_f Q^{μ̄} = 1.069, …, 1.286; tail −ψ/x^{1−μ_T} ≤ 1.000 vs θ_t = 1.036 … 1.287.
The tilt formula of rem:T1-tilt agrees with arg ∂_θS to 10⁻⁴¹ at v = 2·10⁻² (forward, tail and bulk labels). So 1.07 is right and
essentially sharp (the true constant is 1).

### (2) Bulk curvature via the exact two-time relation (Q6(b))
Correct. Checked: y = Cτ^v is non-decreasing (τ increasing), y(t₁) = r sin b ≥ sin b_l because r = ρ₁ ≥ 1 + v (Q1(d)) and
b ∈ [b_l, π/3 + 2e_β] ⊂ [b_l, π − b_l] ((SC32), (SC33); the monotonicity of β₁ on each side of α₀ is lem:T1-tang(a)); hence
0 < β < π on all of run 2 and lem:T1-second applies between t₁ and t_s. τ(t_s) = (ρ − z)/y ≤ 2ρ/y_b, ρ(t_s) ≤ H_b, τ_b ≥ tan(b_l/2):
(τ″/τ′)^v ≤ T_b^{v̄}. The 𝔖-bound uses ∂_θ log C = c/C = ImΞ/y (C = yτ^{−v}) and |ReΞ·ImΞ| ≤ |Ξ|²/2 ≤ (1+v)²w²/2; the
algebra to v(3+v)/(2(1−v)y) is right. w″ ≤ |Ξ″|/(1−v) ≤ (τ″/τ′)^v|Ξ′|/(1−v) is right (τ″ ≥ τ′). The old Gronwall step (factor
v·1.73/0.0049² ≈ 72 at v = 10⁻³) indeed fails for v ≳ 10⁻³. The two-time relation (eq:T1-k2) itself was re-tested: at
v = 2·10⁻² the ODE curvature at t_s agrees with the right-hand side of eq:T1-k2 (computed from ODE data at t₁ and t_s) to
≤ 10⁻⁴⁰ for forward, tail and bulk labels; a and c are time-independent to 10⁻⁴¹.
*Remark (not an error):* K_b is very crude: at (v̄, η) = (2·10⁻², 0.1) K_b = 33.3 while the true bulk curvature is ≤ 1.015
(ODE); at (10⁻², 0.1) K_b = 15.1. The loss is the factor 1/y_b ≈ 1/(b_lo η²) in 𝔖, which is attained only for labels next to the
window, where y is actually of order rb ≈ √3 b. This is what limits the theorem to v̄ ≈ 2·10⁻²; improving it is optional.

### (3) The chord lemma Q7
Correct. F = ∇Φ(|x|) with Φ′ = f ≥ 0 non-decreasing (f(s) = (s/ε)(2 − s/ε) on [0,ε], 1 beyond: sec_B l.36), so F is monotone;
T = ∇|x| is monotone off 0; F = T off the open disc D_ε. If |D| ≥ 2ε the two relative positions are not both in D_ε, and replacing
the field of the one outside by the other field gives (|D|²)′ = 2v(V(p_b) − V(p_a))·(p_b − p_a) ≥ 0 with one monotone V. The
first-exit argument (t\* := inf{|D| < c₀}) is correct. The limit to Z_s is fine.
**Numerics** (`vc_*.txt`): four mixed pairs (virtual α₀ or α₀ + ε/2, α₀ + 2ε; true α₀ − 3ε, α₀ + 2.5ε, α₀ − 2.2ε, α₀ − 0.3ε)
with initial chord 2.3ε–3ε, where the true candidates pass within 0.005ε–0.02ε of Harry and the virtual ones reach 0: the
chord never drops below its initial value (min |D|/c₀ = 1.0008 at v = 10⁻³, 1.0169 at v = 2·10⁻²).

### (4) The three-case proof of (T1′) and the claimed gap in sec_T1
See §6 for the gap. The three-case proof of Theorem Q.H is correct:
* *Near X₀* (u_a < max(λ, u₁ε)): [u_a,u_b] ⊂ [0,(2u₁+1)λ] ⊂ [0, η] ((SC39), (SC40), (SC48)); |T − n̂| ≤ θ_vξ^{1−μ} ≤ θ_vu^{1−μ}
  (ξ ≤ u since w ≥ 1); the right-most-interval bound and A^s − B^s non-decreasing in s for A > B ≥ 1 are right; 27 − 8 = 19 and
  (2u₁+1)³ − (2u₁)³ = 12u₁² + 6u₁ + 1. OK.
* *Near E_Y* (u′_b < λ, x_e < λ): ξ ≤ x_e + u′ < 3λ ≤ η, s = x_e + u′ ranges over an interval of length λ in [0, 3λ]; OK.
* *Far*: forward labels ξ ≥ u/W_v ≥ λ/W_v and ≥ x₁ε (u ≥ u₁ε = W_vx₁ε), tail labels ξ ≥ x_e + u′/W_t ≥ λ/W_t (because u′_b ≥ λ or
  x_e ≥ λ — this is exactly the condition missing in sec_T1), bulk K_b; K_*λ^{−μ_T} is a valid Lipschitz constant, Kλ ≤ π by (SC47).
  The three cases are exhaustive and N ≤ c_Nλ^{3/2−μ_T}. OK.

## 2. Rule (M) and uniformity in v ≤ v̄, ε ≤ ε̄

I checked every substitution v ↦ v̄ in the proofs, in particular the non-obvious ones:
C_hi = 2r_maxβ₂^{1−v̄} (β₂ < 1), xe_lo = C_hi^{−1/2} (C_hi < 1), xe_hi with exponent 1/(2−2v̄) (base g_b/C_lo > 1), m_τ with
η^{−(1−2v̄)} (η < 1: a lower bound), τ_t^{v̄−1} in e_t (τ_t > 1), y_T with C_hi^{1/(1+v̄)} (C_hi < 1), T_t (base ≥ 1, (SC12)), Ȳ =
η(Q/η)^{μ̄} increasing in μ, θ_fQ^{μ̄}, τ_a with ε̄^{1−μ̄} (ε ≤ ε̄ < 1 and 1 − μ ≥ 1 − μ̄), (T3) G^{3/4−μ̄}, (T4) s̄^{1/2−μ̄_T},
λ₀^{1−μ̄_T}, L̂ with (8/λ₀)^{2v̄}, g_max ≤ g_b (d log g_max/dv = artanh v > 0, verified). Each is in the safe direction. Every use
of ε is through ε ≤ ε̄ in a monotone place, or through exact identities (x_e ≥ xe_lo ε^{1/(2−2v)} ≥ xe_lo ε, ε^{1/(2−2v)} ≤ ε^{1/2}).
Citations of sec_T1 kept "unchanged": Lemmas 1–3, rem:T1-tilt(i), lem:T1-tang(a), lem:T1-elem, the exact part of
lem:T1-run1(a), [B, Lemma VC], [D, D0(a)] are exact for all v ∈ (0,1) (re-read; no smallness of v used). Every place where
sec_T1 used v ≤ 10⁻⁶ numerically (2.1ε, 0.479-Gronwall, 3.74·10⁻⁶ positions, 0.0049-Gronwall, (iv) in (T2)) is replaced in Q1–Q7.
Supporting numerics (`mono.py`, η = 0.1 and 0.15, 54 values of v̄ in [10⁻⁷, 2·10⁻²]): every upper-bound constant is non-decreasing
and every lower-bound constant (A_min, C_lo, Λ_min, r_min, a_min, h_f, h_t, ρ_c, xe_lo, m_τ, τ_t, b_l, y_b, ρ_h, Δ₀, c_sep, κ₂)
is non-increasing in v̄; no constant is non-monotone. And the ODE data at v̄ = v satisfy all bounds of Q3, Q5, Q6 (`verify_*.txt`,
"VIOLATIONS: none" for all six runs), including x_e/ε^{1/(2−2v)} ∈ [xe_lo, xe_hi] (1.382–1.414 vs [1.08, 1.78]),
z₀/ε^{1/(2−2v)} ∈ [h_t xe_lo, z_T xe_hi], |y₀|/z₀^{2−μ_T} ≈ 0.49–0.50 ≤ c_y, |k|x^μ ≤ K_f, |k|x^{μ_T} ≤ K_t, w ≤ W_f, W_t,
W_bW_all(2/χ)^{2v} (hole labels θ = 10⁻³ and 2π − 10⁻² included; at v = 2·10⁻² w = 1.32 at θ = 10⁻³ vs bound 2.11).
Q4 (`vc_*.txt`): virtual labels x ∈ {0.1, 0.5, 0.9, 1}·ε: |ψ|/x^{1−μ} ≤ 1.005 ≤ θ_v (1.08, resp. 1.42), w ≤ 1.034 ≤ W_v.

## 3. Theorem Q.H — fixes (exact text)

The proof is correct. Two inequalities are used without being in the (SC) list:
* (T5′)/(T5): "(z₀ + ε < 1)" and (T4′): "(u′ + z₀)^{1−μ_T} ≤ (u′ + z₀)^{1−μ̄_T}" need **z_T x̄_e + ε̄ < 1** and
  **G + z_T x̄_e ≤ 1**. They are true in every column I computed (keys `i1`, `i2` of `consts.py`), and in fact follow from (SC4)
  (η ≤ π/6) as long as z_T ≤ 1.7, but this is not said. **Fix:** add to §0.4: "(SC51) z_T x̄_e + ε̄ < 1 and G + z_T x̄_e ≤ 1"
  and cite it at the two places.
* §8 (T1′) near X₀: "u_b ≤ max(2λ₀, 2u₁ε̄) ≤ η" — the case λ ≥ u₁ε gives u_b < 2λ ≤ 2λ₀ and the case λ < u₁ε gives
  u_b < 2u₁ε ≤ 2u₁ε̄; please write "(SC39), (SC40)" there (only (SC40) is cited).
* §0.2 lists η ∈ (0, π/3]; (SC4) forces η ≤ π/6. Harmless; suggest "η ∈ (0, π/6]".
* Lemma Q1(c), tilt: "+ v sin β₁/(1 + v cos β₁)" is the correct exact term (sec_T1 printed the cruder v sin β₁/(1 − v)); fine.

## 4. Corollary Q.T: recomputed table (ε̄ = 10⁻³; my parameter choices x₁ = 1.0005/ρ_c rounded up, G = η/2, λ₀ = largest
4-digit value with all (SC) incl. i1, i2)

| v̄ | η | λ₀ | c_sep | κ₂ | θ_v | θ_t | c_T4 | K_b | c_N (dominant) | ϑ_T | C_z | U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10⁻⁶ | 0.10 | 0.0333 | 0.03310 | 0.9884 | 1.0694 | 1.0358 | 1.042 | 1.141 | 2.718 (near) | 1.152 | 0.2783 | 6.285 |
| 10⁻⁶ | 0.20 | 0.0726 | 0.07043 | 0.9459 | 1.1738 | 1.0937 | 1.126 | 1.140 | 3.100 (near) | 1.635 | 0.3082 | 6.295 |
| 10⁻⁴ | 0.10 | 0.0333 | 0.03303 | 0.9879 | 1.0705 | 1.0368 | 1.043 | 1.262 | 2.723 (near) | 1.155 | 0.2785 | 6.299 |
| 10⁻³ | 0.10 | 0.0333 | 0.03215 | 0.9830 | 1.0805 | 1.0463 | 1.053 | 2.376 | 2.765 (near) | 1.178 | 0.2806 | 6.433 |
| 10⁻³ | 0.20 | 0.0725 | 0.06901 | 0.9393 | 1.1877 | 1.1064 | 1.140 | 1.507 | 3.162 (near) | 1.674 | 0.3109 | 6.426 |
| 10⁻² | 0.10 | 0.0333 | 0.02344 | 0.9335 | 1.1889 | 1.1502 | 1.166 | 15.05 | 4.346 (far) | 1.443 | 0.3026 | 7.958 |
| 10⁻² | 0.15 | 0.0499 | 0.03594 | 0.9118 | 1.2479 | 1.1849 | 1.214 | 7.824 | 3.468 (near) | 1.720 | 0.3191 | 7.829 |
| 10⁻² | 0.20 | 0.0715 | 0.05239 | 0.8791 | 1.3233 | 1.2307 | 1.283 | 5.222 | 3.794 (near) | 2.079 | 0.3367 | 7.746 |
| 2·10⁻² | 0.15 | 0.0499 | 0.02581 | 0.8486 | 1.4059 | 1.3344 | 1.386 | 16.57 | 4.782 (far) | 2.189 | 0.3486 | 9.788 |
| 2·10⁻² | 0.20 | 0.0703 | 0.03762 | 0.8105 | 1.5006 | 1.3940 | 1.475 | 10.58 | 4.699 (near) | 2.662 | 0.3689 | 9.572 |

Full table in `code/referee/Q3_1/table_out.txt` (η ∈ {0.1, …, 0.3}). No λ₀ works for: (10⁻², 0.3) [(SC21)], (2·10⁻², 0.1)
[(SC42)], (2·10⁻², 0.25/0.3) [(SC21)], all of v̄ = 3·10⁻² [(SC42), and (SC21) for η ≥ 0.2]. This agrees with the remark of §9.
So (H_T) holds for v̄ ∈ {10⁻⁶, …, 10⁻², 2·10⁻²} with suitable η; the claim of Corollary Q.T "in particular" is confirmed. (I could
not compare column by column with `reports/Q3-1.md` §3, which I was told not to read; the (SC) are per-column numerical facts and
my independent evaluation reproduces the HT′ column exactly, so I expect agreement.)

## 5. Theorem HT′
Column (10⁻⁶, 0.1, 10⁻³, x₁ = 1.007, λ₀ = 0.0333, G = 0.05): all (SC) hold (incl. i1, i2). My values: c_N = 2.71902 (c_near),
κ₂ = 0.988407, θ_v = 1.069373, c_T4 = 1.041965, z_T xe_hi = 1.564861, c_y = 0.619290, ϑ_T = 1.152464 (= ϑ₅), C_z = 0.278276,
c_sep = 0.033098, U_max = 6.28451, T₂ = 3.73206, C₀(½) = 0.496180, C₀(0.9) = 1.934915. All printed constants of HT′ are these
values rounded in the safe direction. Since μ_T = 3v/(1+v) ≤ 3v and λ < 1, c_Nλ^{3/2−μ_T} ≤ 2.72λ^{3/2−3v}; a′ ≤ 1 − 3·10⁻⁶ <
1 − μ̄_T and 2.72λ₀^{1−3·10⁻⁶−a′} ≥ c_Nλ₀^{1−μ̄_T−a′}. **OK.**

## 6. The claimed gap in the existing paper (sec_T1, thm:HT (T1) and prop:T1-arcs(2))

**Verdict: the gap is real; the statements are true.**
* sec_T1 l.1059/1066: on the tail |k| ≤ 1.0001ξ^{−μ_T} ≤ 1.0001ε^{−μ_T} (ξ ≥ x_e ≥ ε, correct), then
  "ε^{−μ_T} ≤ (2λ)^{−μ_T}". Since λ ≥ ε/2, 2λ ≥ ε and (2λ)^{−μ_T} ≤ ε^{−μ_T}: **the inequality is reversed.** The far case puts no
  condition on u′, so a far pair may end at E_Y with λ ≫ x_e, where the tail curvature is ≈ x_e^{−μ_T} (and genuinely so:
  k ≈ (τ/τ_b)^v k₁ with (τ/τ_b)^v ≈ x^{−μ_T}, cf. the ODE value |k|x^{μ_T} ≈ 0.89–1.0), which exceeds 1.22λ^{−3v} only when
  (λ/x_e)^{3v} > 1.22, i.e. for astronomically small ε (≈ 10^{−5·10⁴} at v = 10⁻⁶). So the step is wrong, the constant K is not
  justified for those pairs, and no finite numerical check can see it — a proof gap, not a false statement.
* **The author's repair is correct** (checked line by line in §1(4)): case (i) u′_b ≥ λ or x_e ≥ λ gives ξ ≥ λ/1.015 on tail labels,
  K = 1.0001·1.015^{μ_T}λ^{−μ_T} ≤ 1.22λ^{−3v}, N ≤ 0.353λ^{3/2−3v}; case (ii) gives N ≤ 1.647·(19/(3−2μ_T))^{1/2}λ^{3/2−μ_T} ≤
  4.15λ^{3/2−3v} (u′_a < 2λ ≤ 1/20, ξ < 3λ ≤ 0.075 ≤ η). Hence N ≤ 5.4λ^{3/2−3v} as stated.
* **Prop. P8a.1(2) (= prop:T1-arcs(2), sec_T1 l.946–949) has exactly the same defect**: "x_e^{−μ_T} ≤ ε^{−μ_T} ≤ (2λ)^{−μ_T}".
  It is not used elsewhere in the paper (grep: only its own label and rem:T1-status).
* **A shorter repair keeping the original constants.** Use that the curvature bound is *integrable* rather than a Lipschitz
  constant. On A₂ parametrised by arclength, with σ := distance in arclength to E_Y: tail labels have ξ ≥ σ/1.015, so
  |k| ≤ g(σ) := 1.22·min(σ,1)^{−μ_T} on all of A₂ (bulk: 1.22), and g is non-increasing. For a pair of length λ let m be the tangent
  angle at its arclength midpoint; then |ψ(s) − m| ≤ ∫ over an interval of length |s − s_m| of g ≤ 1.22|s − s_m|^{1−μ_T}/(1−μ_T),
  and by lem:T1-elem(b) with e = e^{im}: N² ≤ ∫|ψ − m|² ≤ (1.22/(1−μ_T))²·2(λ/2)^{3−2μ_T}/(3 − 2μ_T), i.e.
  **N ≤ 0.3522λ^{3/2−μ_T} ≤ 0.36λ^{3/2−μ_T}**, so prop:T1-arcs(2)(E1) holds *as stated*. The same device repairs the far case of
  thm:HT (T1) without a case split (forward part bounded by 1.0002λ^{−μ} since u ≥ u_a ≥ λ, tail part by g): N ≤ 0.71λ^{3/2−3v}.
  Either repair is acceptable; the author's one has the advantage of matching Theorem Q.H.
* Suggested text for rem:T1-status: "After the reports a step in the far case of (T1) in Theorem thm:HT and in
  Proposition prop:T1-arcs(2) was found to be reversed (ε^{−μ_T} ≥ (2λ)^{−μ_T}); both statements are true and the proofs are
  repaired by splitting off pairs with u′_b < λ and x_e < λ (resp. by integrating the curvature bound), see …".

## 7. Minor remarks (no action required)
* §0.3: rΛ_max uses q_max over the whole window (attained on the tail side); on the forward side q̃ ≤ q̃(α₀) would give
  θ_v ≈ 1.04. Fine as is.
* The ODE shows the true constants are θ ≈ 1, |k|ξ^{μ} ≈ 0.97–1, bulk |k| ≤ 1.02 at v = 2·10⁻²: all bounds hold with room;
  the binding constant for v̄ ≥ 10⁻² is K_b (§1(2)).
