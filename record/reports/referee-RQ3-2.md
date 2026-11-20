# Referee report RQ3-2 (second referee) — `referee/Q3-claims.md` (touch-down theorem with v̄-dependent constants)

Angle: independent **rebuild** of the touch-down state from the straight-run integrals, adversarial worst-ratio scan of every
item of (H_T) and of the sharp forms, the paper gap of §10.2, the interface with `hyp:HT`, and hidden small-v assumptions.
`reports/referee-RQ3-1.md`, `reports/Q3-1.md` and `code/Q3/*.py` were **not** read. `code/Q3/out/table.txt` was read only
after the verdict on Theorem Q.H had been formed (to check Corollary Q.T).

All code is in `code/referee/Q3_2/`:
* `consts.py`: my own implementation of every constant of §0.3 and of (SC1)–(SC50), written from the claims text only.
* `front.py`: the exact touch-down curve x⁰ of design T (D₁ = 1). Run 1 and run 2 are composed using the integrals
  C = ρg(β), h = ρ(cos β + v), h′ = −(1−v²), solved for τ = tan(β/2) by safeguarded Newton in log τ. The tangent comes from
  Ξ = a + iτ^v c (a, c independent of time). The hole limit Z_s is the point Z₁ = P(t₁) − (1+v) carried by run 2. The virtual
  labels (α₀, α₀ + x₁ε) use the exact state at t_a, then the field F (f(s) = (s/ε)(2 − s/ε) in the disc) together with its
  variational equation, integrated in variables scaled by ε. x_e solves C(α₀ − x_e) = εg_max. The working precision is
  2.3·log₁₀(1/ε) + 40 digits (178 digits at ε = 10⁻⁶⁰), which resolves b ∼ x² for x down to 10⁻³ε.
* `test_front.py`: validation against direct DOP853 integration of S′ = v(S−P)/|S−P| along the design-T path.
  Positions agree to ≤ 7·10⁻¹⁴ and tangents to finite-difference accuracy. Virtual and true labels agree at x = 1.2ε and
  2ε (to 10⁻¹⁵). The virtual label α₀ reaches X₀ at t_s (P(t_s) = x_{α₀}(t_s)).
* `scan.py`, `run_all.py`: the scan. Results are in `out/*.json`, with summaries in `out/table_referee.txt` and
  `out/summary.txt`. `check_table.py` (output `out/check_table.txt`) checks Corollary Q.T.

N(a,b) is computed without cancellation from N² = 4∫w sin²((ψ−ψ̄)/2)dθ, with ψ̄ the chord direction obtained from ∫w e^{iψ}.
The quadrature is composite Gauss–Legendre, graded toward α₀ and the hole. GL8 and GL16 agree to 10 digits on every item.
Curvature is a central difference of ψ at high precision. A solver bug of mine (premature exit of the Newton loop at one
precision) was found and fixed before the production runs; all results below come from the fixed code.

## 1. What was scanned

* **Parameter sets** (all satisfy all 50 (SC) in my `consts.py`; ε̄ = 10⁻³; parameters are (η, x₁, λ₀, G)):

  | v̄ | (η, x₁, λ₀, G) |
  |---|---|
  | 10⁻⁶ | (0.1, 1.007, 0.0333, 0.05), the HT′ column |
  | 10⁻⁴ | (0.1, 1.0068, 0.0333, 0.0253) |
  | 10⁻³ | (0.1, 1.0081, 0.0333, 0.0252) |
  | 10⁻² | (0.15, 1.0327, 0.0499, 0.048) and (0.1, 1.0217, 0.0333, 0.0243) |
  | 2·10⁻² | (0.2, 1.074, 0.07, 0.05) and (0.12, 1.0447, 0.035, 0.0327) |

  The last 2·10⁻² set sits at W_xL̂ = 1.993, at the edge of (SC42).
* **Actual v and ε.** For each set: v ∈ {v̄, v̄/10} with ε ∈ {10⁻³, 10⁻⁶, 10⁻¹², 10⁻²⁴, 10⁻⁴⁰, 10⁻⁶⁰}, plus v = v̄/1000 with
  ε ∈ {10⁻³, 10⁻¹², 10⁻⁴⁰}. For v̄ = 10⁻⁶ the extra runs use v = 10⁻⁸. Together these cover both orders of limits (ε → 0
  at fixed v, and v → 0 at fixed ε). The constants are always evaluated at v̄, as Rule (M) requires. In total 99
  configurations ran, all to completion.
* **Pairs for (T1′)/(T1).** λ runs from ε/2 to λ₀ (one value per decade, four per decade above 10⁻⁴). For each λ the scan
  places pairs at:
  * X₀ (u_a = 0, ½λ, λ, 2λ, 5λ);
  * the virtual/true junction x₁ε;
  * E_Y (u′_b = 0, ½λ, λ, 2λ, 5λ);
  * across, left of and right of the hole;
  * both window edges, inside the forward and tail windows, the bulk, and θ = π.

  This gives about 27 000 pairs per configuration at ε = 10⁻⁶⁰. Each pair is classified by the proof's own cases (near X₀,
  near E_Y, far).
* **Pairs for (T2′)/(T2) and (8.2).** All mesh pairs with λ > λ₀ (about 2.5·10⁵ per configuration).
* **Pointwise checks** on 170–700 graded mesh labels, down to 10⁻³ε from X₀, from E_Y and from the hole:
  * Q3(d) |k|; Q4 |ψ| and w;
  * Q5(c): sign of ψ, ψ, w, z both sides, y, |k|;
  * Q6(b): |k| and w; the length bound w ≤ W_x(2/χ)^{2v};
  * (T3′), (T3), (T4′) (both forms), (T4);
  * (T5′) (all four inequalities) and (T5);
  * x_e bounds, t_s ≤ T₂, 1 ≤ U ≤ U_max.

## 2. Results (worst ratio actual/claimed over all v, ε of each set; ≤ 1 means the claim holds)

| item | 10⁻⁶ | 10⁻⁴ | 10⁻³ | 10⁻² (η .15) | 10⁻² (η .1) | 2·10⁻² (η .2) | 2·10⁻² (η .12) |
|---|---|---|---|---|---|---|---|
| (T1′) N ≤ c_N λ^{3/2−μ_T} | 0.106 | 0.106 | 0.104 | 0.083 | 0.066 | 0.061 | 0.041 |
| — case near X₀ (c_near) | 0.106 | 0.106 | 0.104 | 0.083 | 0.089 | 0.061 | 0.072 |
| — case near E_Y (c_tail) | 0.111 | 0.111 | 0.110 | 0.096 | 0.099 | 0.081 | 0.086 |
| — case far (c_far) | 0.877 | 0.793 | 0.421 | 0.128 | 0.066 | 0.095 | 0.041 |
| (T2′) c ≥ min(c_sep, κ₂(u_a+u′_b)) | 0.988 | 0.988 | 0.983 | 0.912 | 0.934 | 0.811 | 0.866 |
| (8.2) λ > λ₀ ⇒ Δ > Δ₀ | 0.942 | 0.940 | 0.968 | 0.767 | 0.762 | 0.619 | 0.600 |
| (T3′) θ_v u^{1−μ} | 0.935 | 0.934 | 0.926 | 0.801 | 0.841 | 0.666 | 0.736 |
| (T4′) θ_t(x_e+u′)^{1−μ_T} | 0.966 | 0.965 | 0.956 | 0.844 | 0.870 | 0.717 | 0.767 |
| (T4′) c_T4(u′+z₀)^{1−μ̄_T} | 0.960 | 0.959 | 0.947 | 0.802 | 0.834 | 0.643 | 0.705 |
| (T5′) z₀ ≥ h_t xe_lo ε^{1/(2−2v)} | 0.899 | 0.898 | 0.893 | 0.792 | 0.842 | 0.687 | 0.766 |
| (T5′) z₀ ≤ z_T xe_hi ε^{1/(2−2v)} | 0.904 | 0.903 | 0.898 | 0.802 | 0.845 | 0.705 | 0.772 |
| (T5′) \|y₀\| ≤ c_y z₀^{2−μ_T} | 0.808 | 0.807 | 0.797 | 0.621 | 0.701 | 0.464 | 0.576 |
| (T3)/(T4)/(T5) with ϑ_T, γ_T = ¼ | ≤ 0.26 | ≤ 0.26 | ≤ 0.26 | ≤ 0.18 | ≤ 0.22 | ≤ 0.12 | ≤ 0.17 |
| U ≤ U_max | 0.9998 | 0.998 | 0.979 | 0.819 | 0.806 | 0.684 | 0.657 |
| t_s ≤ T₂ | 0.999999 | 0.9999 | 0.9993 | 0.993 | 0.993 | 0.986 | 0.986 |
| Q3 \|k\| ≤ K_f ξ^{−μ} | 0.99998 | 0.998 | 0.982 | 0.799 | 0.822 | 0.571 | 0.641 |
| Q5 \|k\| ≤ K_t ξ^{−μ_T} | 0.99998 | 0.998 | 0.979 | 0.776 | 0.799 | 0.540 | 0.605 |
| Q6 \|k\| ≤ K_b | 0.877 | 0.793 | 0.421 | 0.129 | 0.067 | 0.096 | 0.042 |
| Q4 \|ψ\| ≤ θ_v ξ^{1−μ} | 0.935 | 0.934 | 0.926 | 0.804 | 0.843 | 0.670 | 0.740 |
| Q5 −ψ ≤ θ_t ξ^{1−μ_T} (and ψ < 0: always) | 0.966 | 0.965 | 0.956 | 0.844 | 0.870 | 0.717 | 0.767 |
| Q5 z ≥ −z_T ξ / z ≤ −h_t ξ | 0.9999/0.996 | 0.9997/0.996 | 0.998/0.995 | 0.981/0.980 | 0.983/0.988 | 0.957/0.952 | 0.964/0.973 |
| w ≤ W_x(2/χ)^{2v} | 0.994 | 0.994 | 0.981 | 0.836 | 0.824 | 0.711 | 0.686 |

**No item exceeds 1 in any of the 99 configurations.** The trivial items u ≥ ξ and u′ ≥ ξ − x_e (from w ≥ 1) reach
1 − 10⁻⁸.

**Where the margins are thin.** The small margins sit at **small** v̄, not at v̄ = 10⁻²–2·10⁻². There the constants are the
exact v = 0 values plus O(v̄). For example, at v → 0 the front at the window is the unit circle, with k = 1 against
K_f = 1.0000181, and t_s → 2 + √3 against T₂ = 3.73206. These margins are legitimate, because every constant is an upper
bound at every v ≤ v̄ and they stay below 1 also at v = v̄/1000 and v = 10⁻⁸.

At v̄ = 2·10⁻² the smallest margins are:

| item | margin |
|---|---|
| t_s ≤ T₂ | 1.4 % |
| Q5 z bounds | 4–5 % |
| (T2′) | 19 % |
| everything else | ≥ 25 % |

**The thin-margin worry at v̄ = 10⁻²–2·10⁻² is refuted.**

**The front at larger v.** At v = 2·10⁻², α₀ = 1.0298 (π/3 = 1.0472) and β* = 2.6119 (5π/6 = 2.6180). The curvature at E_Y
grows like x_e^{−μ_T}:

| ε at v = 2·10⁻² | 10⁻³ | 10⁻²⁴ | 10⁻⁶⁰ |
|---|---|---|---|
| k(E_Y) | 1.07 | 4.58 | 55.1 |

At ε = 10⁻⁶⁰, x_e^{−μ_T} = 62. At ε = 10⁻⁶⁰ the raw ratio N/λ^{3/2} reaches 15.9 near E_Y, so the "front ≈ unit circle" picture
is false. Yet the claimed bounds hold with the margins above, because they carry the right exponents (K_tξ^{−μ_T},
c_N λ^{3/2−μ_T}, θ_t ξ^{1−μ_T}). The proofs do not use the old approximations μ ≈ v, 1/(1−v) ≈ 1, front ≈ unit circle, or
x_e ≈ √2 ε^{1/(2−2v)}: every step I traced carries exact v-dependence through Rule (M). Numerically,
x_e/ε^{1/(2−2v)} = 1.39 at v = 2·10⁻², ε = 10⁻⁶⁰, inside [xe_lo, xe_hi] = [1.03, 1.88].

## 3. Verdicts per claim

* **Lemma Q1 (run 1, middle, arm, hole data): OK.** I checked by hand:
  * the identity h₁ = −(1−v²) − (1 − cos α);
  * ρ₁ ≥ 1 + v;
  * the Gronwall bound for |k₁ − 1|;
  * the arm stretch estimate 𝒯 ≤ E₁^v(2/α)^{2v}.

  The scan confirms w ≤ W_x(2/χ)^{2v} down to |α| = 10⁻³ε at the hole (margin ≥ 0.6 %).
* **Lemma Q2 (window data): OK.** I checked by hand:
  * the angle computation ie^{iθ}·p₀ = 2 sin θ, ie^{iθ} × p₀ = 2cos θ − 1;
  * the cot inequality;
  * the monotonicity of q̃ via (SC6), (SC7);
  * the bounds on a and ∂_θ log C.

  The downstream items that use them all hold numerically.
* **Lemma Q3 (forward arc): OK.** I checked by hand that v(1+μ) = μ, that (1+v)r/h ≤ Q/(x+δ), and the bound on 𝔖″.
* **Lemma Q4 (virtual labels): OK.** I checked the Gronwall step and the use of Q3 at t_a, where δ(t_a) = ε/(1−v). The
  virtual ODE run confirms |ψ| ≤ θ_v x^{1−μ} and w ≤ W_v on [0, x₁ε].
* **Lemma Q5 (tail, E_Y, seen labels): OK.** I checked by hand:
  * the bound on e_t, with τ_t^{v−1} ≤ τ_t^{v̄−1};
  * y ≤ y_T x^{2−μ_T};
  * the exponent −3/(1+v) in τ/τ_b (which needs 2/b_lo ≥ 1, i.e. (SC12));
  * the three seen-ranges in (b), including (1+v)(ε − A_max x) ≥ (1 − A_max/2)ε. This step tacitly needs A_max ≤ 2, which
    holds because A_max ≤ e^{v̄t̄₁/sin θ_L} < 1.6 under (SC3) and (SC35). Stating this in the text is optional.
* **Lemma Q6 (bulk and hole): OK.** I checked by hand:
  * b ∈ [b_l, π/3 + 2e_β] on the lower half, via β₁(2π − α) = −β₁(α) ≤ −β*;
  * τ = (ρ − z)/y ≤ 2ρ/y_b;
  * the bound on 𝔖 via |ReΞ ImΞ| ≤ |Ξ|²/2;
  * Z₁ = 1 + v²/(1−v) ∈ B(1, r_B).
* **Lemma Q7 (chords): OK.** Both T and F = ∇Φ(|x|) are monotone, and F = T off D_ε. The first-exit argument is correct.
  This is exactly what (T2′) needs, and it replaces P8a's 3.74·10⁻⁶ device, which fails at larger v.
* **Theorem Q.H: OK.**
  * I traced every inequality of the proof in §8 and found no gap:
    * the case split of (T1′), together with (SC39) and (SC40);
    * the near-X₀ integral, which needs u₁ ≥ ½ for monotonicity of A^s − B^s;
    * the rearrangement bound (8.1), which equals 2^{4v}Δ^{1−2v}/(1−2v);
    * (8.2), which needs Δ₀ ≥ λ₀/2, i.e. (SC42);
    * both cases of (T2′);
    * (T3)–(T5) from the sharp forms, using μ_T ≤ ½ and (u′ + z₀) < 1.
  * Every quantitative item holds on the rebuilt curve, for all scanned v ≤ v̄ and ε down to 10⁻⁶⁰, with the margins of §2.
* **Corollary Q.T: OK.** I evaluated my independent `consts.py` at all 18 columns of `code/Q3/out/table.txt` (13 with
  ε̄ = 10⁻³ and 5 with ε̄ = 10⁻⁶), using the printed x₁, λ₀ and G.
  * All 50 (SC) hold in every column.
  * c_N, κ₂, c_sep, ϑ_T, C_z and U_max agree with the printed values to ≤ 7·10⁻⁴ relative.
  * The printed values are rounded in the safe direction (upper bounds up, κ₂ and c_sep down).
  * My own parameter search independently reproduces the v̄ = 10⁻⁶ column (c_N 2.7190, κ₂ 0.98841, θ_v 1.06937,
    c_T4 1.04197, z_T·xe_hi 1.56486, c_y 0.61929, ϑ_T 1.15246).
  * It also confirms that at v̄ = 2·10⁻² a column exists only for η ≥ ≈0.12, because (SC42) fails below that. This is
    consistent with the §9 Remark.
* **Theorem HT′: OK.** Its constants are the v̄ = 10⁻⁶ column, and the scan of that column with v = 10⁻⁶ and v = 10⁻⁸ shows
  no violation. The worst (T1′) ratio is 0.106, so N ≤ 0.289 λ^{3/2−3v} on the rebuilt curve against the claimed 2.72.
* **§10.2, gap and repair: OK with a fix to the text (see §4).**

## 4. The gap in the refereed paper (thm:HT (T1), far case; also Prop. P8a.1(2))

**Confirmed: the gap is real.** In `paper/sec_T1.tex`, line 1066 (the proof of thm:HT) and line 948 (Prop. P8a.1(2)) use
ε^{−μ_T} ≤ (2λ)^{−μ_T}. Since λ ≥ ε/2, the true inequality is the reverse, ε^{−μ_T} ≥ (2λ)^{−μ_T}, **for every ε**. The
written chain therefore does not justify K = 1.22λ^{−3v} for far pairs whose tail labels approach E_Y while x_e ≪ λ.

**Is it more than a proof defect?** The scan shows k(E_Y) = 1.0002 at v = 10⁻⁶, ε = 10⁻⁶⁰, against x_e^{−μ_T} = 1.000206.
So the actual curvature at E_Y behaves like ≈ 1.000·x_e^{−μ_T}, and the curvature claim K = 1.22λ^{−3v} is **actually false**
(not merely unproved) once (λ/x_e)^{3v} > 1.22. With λ ≤ 1/40 and x_e ≈ 1.414 ε^{1/2}, this means
x_e < 10^{−28788}, i.e. **ε ≲ 10^{−57577}**.

The claims' statement "fails … only if (λ/ε)^{3v} > 1.22, e.g. ε < 10^{−28000}" is logically correct as a necessary
condition (x_e ≥ ε). It is not the actual threshold, because it has ε where x_e belongs.

**Fix (exact text) for §10.2, line 3:** replace "(it fails as an upper bound for the curvature only if (λ/ε)^{3v} > 1.22,
i.e. ε < λ·e^{−0.199/(3v)}, e.g. ε < 10^{−28000} at v = 10⁻⁶; …)" by "(the proved tail bound 1.0001ξ^{−μ_T} exceeds
1.22λ^{−3v} at ξ = x_e only if (λ/x_e)^{3v} > 1.22, i.e. x_e < λe^{−0.199/(3v)}; with x_e ≥ 1.27ε^{1/2} this needs
ε < 10^{−57570} at v = 10⁻⁶ (numerically the actual curvature at E_Y is ≈ x_e^{−μ_T}, so the bound K is then genuinely
false); …)".

**Is the STATEMENT of thm:HT still true? Yes.** On the rebuilt curve, the worst value of N/(5.4 λ^{3/2−3v}) over all
configurations is **0.0535**. That is, the true worst case is N ≈ 0.289 λ^{3/2−3v}, attained near E_Y (and equally near X₀).
It is stable from ε = 10⁻³ to 10⁻⁶⁰, for v = 10⁻⁶ and v = 10⁻⁸.

In the limit ε → 0 the near-E_Y profile is ψ ≈ −κξ^{1−μ_T} with κ ≈ 1. Therefore N/λ^{3/2−μ_T} stays bounded, tending to
≈ κ/√12 ≈ 0.289; the singular curvature at E_Y is integrable in this sense. Even past ε ≈ 10^{−57577}, the true N stays far
below 5.4 λ^{3/2−3v}.

**Is the repair correct? Yes.** I checked the split of the far case:
* (i) If u′_b ≥ λ or x_e ≥ λ, then every tail label of the pair has ξ ≥ x_e + u′/1.015 ≥ λ/1.015. This gives
  K ≤ 1.0001·1.015^{μ_T}λ^{−μ_T} ≤ 1.22λ^{−3v}, together with the forward bound 1.0002u^{−μ} ≤ 1.0002λ^{−μ} and the
  bulk bound 1.22.
* (ii) If u′_b < λ and x_e < λ, then ξ < 3λ ≤ 0.075 (inside the tail zone ≤ 0.1). The integral bound gives
  1.647·√(19/3) = 4.145 ≤ 4.15, which is below 5.4.

Hence the paper's (T1) constants C₀ = 0.86 (a′ = ½) and C₀ = 5.21 (a′ = 0.99) stand, with the repaired proof.

**Prop. P8a.1(2), the 0.36 bound.** The proof is not justified, for the same reason. Numerically the statement still holds:
near E_Y, N/λ^{3/2−μ_T} → ≈ 0.289 < 0.36 as ε → 0. The claims' replacement 4.15 is correct and safe. As the claims say, the
proposition is not used by thm:HT.

## 5. Interface with `hyp:HT` (verbatim check)

* **Quantifiers.** `hyp:HT` asks for absolute constants such that the items hold "for all v ∈ (0, v_T] and ε ∈ (0, ε_T]".
  Q.H gives exactly this with v_T = v̄ and ε_T = ε̄. The constants depend only on (v̄, η, ε̄, x₁, λ₀, G), and these are fixed
  per column.
* **Ranges.**
  * v̄, ε̄ ∈ (0,1); T₂, U_max ≥ 1; C₀, C_z > 0.
  * λ₀ ≤ ¼ (SC41); c_sep ≤ 1; γ_T = ¼; G ∈ (0,1] (SC50).
  * a′ ∈ (0, 1 − μ̄_T] ⊂ (0,1], with C₀λ₀^{a′} = c_Nλ₀^{1−μ̄_T} ≤ 1 (SC49).
* **Items.**
  * (T1): needs λ^{3/2−μ_T} ≤ λ^{3/2−μ̄_T} and 1 − μ̄_T − a′ ≥ 0, both of which hold.
  * (T2): κ₂ ≥ ½ (SC46).
  * (T3): needs G^{3/4−μ} ≤ G^{3/4−μ̄}, which holds.
  * (T4): needs s̄ < 1 and x_e^{1/2} ≤ 2^{1/4}xe_hi^{1/2}(ε/2)^{1/4}, which hold.
  * (T5): z₀ ≥ h_t x_e > 0, and μ_T ≤ ½.
  * (T0) and 𝒢 ⊂ [0,U): same as in the paper.
* **Monotonicity in v.** Rule (M) was spot-checked by hand at every non-obvious substitution I met:
  * C_hi with β₂ < 1;
  * C_hi^{1/(1+v)};
  * τ_t^{v−1};
  * m_τ with η^{−(1−2v)};
  * Q^μ with Q ≥ 1;
  * (g_b/C_lo)^{1/(2−2v)};
  * L̂ with 8/λ₀ > 1;
  * Δ₀^{1−μ} and η^{1−μ}.

  It was also tested numerically at v = v̄/10 and v̄/1000 (and 10⁻⁸ for v̄ = 10⁻⁶) with constants evaluated at v̄: no
  violation.
* **Role of η.** η is a free design parameter of the proof only; it enters the window, b_l and the (SC); `hyp:HT` never
  sees it. G must satisfy x̄_e + G ≤ η, and the table respects this.
* **ε̄.** The constants x̄_e, C_z, h_a and τ_a use ε̄, and are monotone in ε ≤ ε̄.
* **Remark, not a gap.** `sec_T2` caps v₀ ≤ min(v_T, 2·10⁻¹¹γ_B², …), so downstream any v_T above about 10⁻¹¹ buys
  nothing until `sec_T2` itself is generalised. Q.H therefore matches the interface; its benefit is the explicit
  v̄-dependence of the constants.

## 6. Hidden assumptions carried over from the v ≤ 10⁻⁶ proofs

None found in the claims. The P8a device |x⁰(u) − e^{iΘ}| ≤ 3.74·10⁻⁶, which is false at v = 2·10⁻² because the
displacement there is ≈ vt ≈ 0.07, is correctly replaced by Lemma Q7. The constant 1.02ε is replaced by x₁ε with
ρ_c x₁ > 1 (SC17).

The approximations listed in the brief (1/(1−v) ≈ 1, μ ≈ v, front ≈ unit circle, E_Y ≈ √2 ε^{1/(2−2v)}) do not occur. The
one tacit numerical assumption I met is A_max ≤ 2 in Q5(b), which the (SC) imply (see the Q5 verdict).

## 7. Not covered

* D₁ ≠ 1 (not claimed).
* The external inputs [B] and [D] (accepted as cited).
* Times after t_s.
* ε below 10⁻⁶⁰: the behaviour there is argued through the ε → 0 limit of a fixed-v true front, not computed. The
  10^{−57577} threshold is extrapolated from the computed law k(E_Y) ≈ x_e^{−μ_T}.
