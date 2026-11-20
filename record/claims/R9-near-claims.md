# R9-near claims (stream R-near, round 9)

Full statements and proofs: `r9/near/prop_near.tex`. Labels follow that file. Base: `r9/base_short/` (refereed). Summary:
`reports/R9-near.md`.

| # | claim | status | depends on |
|---|---|---|---|
| N-D | Lemma D: D(s) ≥ λφ_θ(x+σ); a*(ρ_s) ≤ λ⁻¹[φ_θ⁻¹ + θ⁻¹1{x+σ < c₆θ}] | PROVED | lem:dist (first form), lem:local(ii), (P0) K_f+1 ≤ K_R |
| N-B | Lemma B: Ω ≤ μ²λ min(1, C_μA λ_σ); G ≤ ∫\|T−e\| ≤ μλ(κλ_σ Ω̄)^{1/2} | PROVED | (E-μ) of lem:tilt(ii) [or R-tilt T(ii) with C_μ], (J1), (J2), static(b) |
| N-L | Lemma L (layer cake) | PROVED | measure theory |
| N-S | Lemma S (split tilt, J ⊂ I′ sharing an end) | PROVED (re-proof of R-tilt Lemma S(i),(iii)) | static(b) |
| N-O | Lemma O: offsets (i) short-type 𝔭 via 3 routes; (ii) any time 𝔭_L via (CA)+(J1) on (a′,b); (iii) g = 0: P₀; (iv) gap facts | PROVED | Lemma S, lem:tilt(i) [C_A, C_B], (CA), (J1), (J2), lem:local, lem:legs, (N1) K_ε ≥ 2 |
| N-A | Lemma A: leg time averages ∫(1−s) ≤ d_Lε/2, ∫s ≤ (3d_L−2)ε/2 | PROVED | lem:chase(1), lem:sep(c), (P1) |
| N-Σ | Lemma Σ: discrete and integral leg sums | PROVED | lem:gapint preamble, lem:legs |
| N-P | Proposition 4.3″: E(t) ≤ ½f_F²M²λ^{1+2γ} + v𝒟(θ,r)M²λ^{1+2γ} ≤ ½θ̄M²λ^{1+2γ}, θ̄ = f_F² + 2v₀D′ | PROVED | all of the above, lem:excess(iii), lem:field(iii) |
| N-E | Lemma E: D′ ≤ 34.99 (R-tilt constants C_T = 2.9108574), D′ ≤ 42.40 (Def 3.3 constants) at the main tuple p | PROVED modulo floating point (computer-assisted upper sums; `near_const.py`, `near_const.out`) | N-P definitions; the monotonicities listed in its proof |
| N-X | Cross-check: cell bounds exceed an independent scipy.quad evaluation of 𝒟(θ,r) by 0.2–2% at 6 test points | NUMERICAL | `check_independent.py` |
| N-Sim | Simulated near growth max ΔE/(vM²λ^{1+2γ}) = 0.0035–0.0052 ≤ D′(K_ε=20) = 45.8 | NUMERICAL | `sim_out/` |

## Points for the referee to check first
1. **Lemma O(ii)**. The pair (a′,b) can be longer than R. It is good, and (CA) holds for it because Λ < (K_f+1)λ ≤ K_R R. Its
   length is ≤ κΛ by covering it with ⌈Λ/R⌉ equal admissible pieces. Their first points are ≥ a′ + R/2 ≥ β⁺, and this needs
   **(N1)**. Hence N(a′,b)² = 2E ≤ 2(κ − c_A)Λ. This route replaces the old 1/D bound in the long case.
2. **Lemma A**. P(τ) = (1−s)x_β + s x_{β⁺} with s = σ/(σ+ρ), and σ+ρ = c(β,β⁺;τ) ≥ c₀ by chord monotonicity. The per-leg
   bound uses ∫|p_a| ≤ (ε/2)(d_L Y_β + d_L′ Y_{β⁺}), with Y_{β⁺} evaluated at the next gap, which is ≤ g − ε/κ.
3. **Per-leg minima**. For each leg the proof takes the smaller of several bounds that are each valid for that whole leg. The
   short or long type is constant on a leg because g is.
4. **Lemma E monotonicities**. The key one is that θ/φ_θ(w) is non-decreasing in θ, so terms carrying a factor θ can use θ_h. The
   bottom cell uses max(θ, c_Aw − δ₁θ) ≥ w/c₆ and closed-form majorants on (0, 10⁻⁷].

## Gaps
- No interval arithmetic in Lemma E.
- With R-tilt's constants, the result depends on R-tilt's Lemma T, which is unrefereed.
- The simulation does not probe the worst case.
