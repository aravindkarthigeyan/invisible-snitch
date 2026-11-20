# R9-near: a sharper near-pair proposition (stream R-near, round 9)

Plan: `reports/L-9.md` (R1, R3, R4). Built on R-tilt (`reports/R9-tilt.md`, `referee/R9-tilt-claims.md`).
Drop-in text with full proofs: `r9/near/prop_near.tex`. Claims and status: `referee/R9-near-claims.md`.
Scripts: `r9/near/near_const.py` (→ `near_const.out`), `r9/near/check_independent.py`, simulation in `r9/near/sim_out/`.

## Headline (main tuple p, INPUTS line of verify_constants.out)

| | old Prop 4.3 | R-tilt rewrite (split long) | **this Prop 4.3''**, old tilt consts | **this, R-tilt consts** |
|---|---|---|---|---|
| D (replaces D_I + max(D_IIs, D_IIl)) | 7322.8 | 198.2 | **42.40** | **34.99** |
| v0 where (P6) binds, (1 − f²)/(2D) | 6.70e-5 | 2.5e-3 | 1.16e-2 | 1.40e-2 |
| θ̄ at v0 = 6e-5 | 0.8975 | 0.0425 | 0.0239 | 0.0230 |

How the new D′ splits by term. Each term is majorised on its own, so the parts add up to slightly more than the total.

| term | old | new, worst cell overall (θ≈0.0056, r≈5.6, long-type binds) | new, worst short-only cell (θ≈1.7) |
|---|---|---|---|
| I (own excess growth; old D_I) | 485.6 | 5.70 | 6.54 |
| II quadratic forcing (old c6²C1A²T_a) | 726.9 | 2.67 | 0.96 |
| II offset/linear incl. gap-0 leg (old 5585 + 525) | 6110.2 | 28.79 | 21.90 |
| II long case via 1/D (old D_IIl) | 2960.8 | 0 (offset route is smaller everywhere) | n/a |

With old tilt constants: D′ ≤ 42.40 (I 8.68, quad 4.50, lin 31.11). The worst short-only cell is 29.65.

## What is new (all PROVED, `prop_near.tex`)
1. **R1, exact distance profile.** D(s) ≥ λφ_θ(x+σ) with φ_θ(w) = max(θ, c_A w − δ₁θ), θ = ε/λ. This is the first form of
   lem:dist, used directly. Any split at w = Kε gives a weaker bound, and the old max(w, c₆θ)/c₆ is the case K = c₆.
   So no new parameter K is needed. In the far part the factor c₆ ≈ 2 becomes c_A ≈ 1.
2. **R3, budgets.** Ω(σ) ≤ μ²λ·min(1, C_μA λ_σ) uses both the sub-arc L² bound and the total N² ≤ M²λ^{1+2γ}.
   G(σ) ≤ μλ(κλ_σ Ω̄)^{1/2}. The quadratic forcing is written as ∫ψ d(G²/2), which gives a factor ½ and no C_1A·C_1A product.
   All of these enter through a layer-cake lemma (Lemma L), with w = g + σ exactly (the old proof lost y → y − g).
3. **Offsets.** There are three routes for |(x_a − x_{a'})×e|: L² on (a′,b), R-tilt's split identity (Lemma S), and the chord
   route. For the long case there is a fourth, tilt-free route. (CA) and (J1) on the possibly long pair (a′,b) give
   N(a′,b)² ≤ 2(κ − c_A)Λ, and then Lemma S applies (Lemma O(ii)). This replaces the 1/D bound, which is what made the old
   D_IIl ∝ 1/m. On this tuple κ − c_A = 0.0198.
4. **R4, time integrals.**
   - Exact leg sums: at most k* = ⌈κK_f/θ⌉ − 1 legs with positive gap, so H* is evaluated at kθ/κ.
   - Time average of |p_a| on each leg (Lemma A). P moves from x_β to x_{β+}, so each endpoint offset is charged ε/2 instead of ε.
   - Per-time short/long split (g + λ ≤ R or not), with the exact factor r^γ, r = R/λ, instead of (K_f+1)^γ.
5. **D_I re-checked.** Term I goes from 485.6 to about 6 (R-tilt: 16.0). The gain comes from Ω̄ capped at 1, so C_μA enters only
   through a log, and from c_A in place of 1/c₆.

## Formula and side conditions (Def 3.3 notation; full list in prop_near.tex)
D′ := sup{𝒟(θ,r) : 0 < θ ≤ 2, r ≥ max(1, K_ε θ)}, where 𝒟 = θH₀ + θ Σ_{k≤k*} H_r*(kθ/κ). H_r and H₀ are explicit one-dimensional
Stieltjes integrals of φ_θ^{-1}, φ_θ^{-2} against Ω̄, Q̄, Ḡ, times the offset profiles 𝔭, 𝔭_L, P₀. Then θ̄ := f_F² + 2v₀D′.
- Tilt constants enter only as C_A, C_B (same-end tilts), C⋆ = C_A + C_B, C_μA, C_V = (1+κC_B²)^{1/2}. With R-tilt's Lemma T:
  C_A = C_B = C_T, C⋆ = 2C_T, C_μA = C_μ. To use R-tilt's numbers, run `python near_const.py --CT <value>`.
- New side condition: **(N1) K_ε ≥ 2**. It replaces K_ε ≥ 3/2 and is used to chop long pairs into admissible pieces.
- D′ depends on √(κ − c_A) through 𝔭_L. Stream Opt should keep this in mind if κ − c_A grows. The 1/D route caps that part
  at the old-style long bound.
- If R-tilt's constants are used, its conditions (T1)–(T4) are needed. No new free parameter.
- The value of D′ is computer-assisted (Lemma E):
  - Upper Riemann–Stieltjes sums over cells in (θ, r), with adversarial endpoint substitution, which is legitimate because each
    θ-dependence is monotone.
  - A bottom cell θ ≤ 1e-7 handled by θ-free kernels plus closed-form majorants on (0, 1e-7].
  - Double precision only, no interval arithmetic.
  - The cell bounds are 0.2–2% above an independent scipy.quad evaluation (`check_independent.py`).
  - Runtime is about 80 s for both constant sets.

## Simulation (NUMERICAL, `r9/near/sim_out/`)
- Setup: Construction C on a virtual front with `code/referee/Q1_2/sim.py` (unchanged). Main-tuple parameters, but
  K_ε = 20 (ε = R/20) so the runs stay small.
- Runs: 6 runs, v ∈ {6e-5, 1e-3, 1e-2}, bends ±1/0, h/ε ∈ {0.1, 0.2}, 31k–66k near pairs tracked.
- Measured near growth: max over pairs of ΔE_near/(v M²λ^{1+2γ}) is between **0.0035 and 0.0052**.
- Bound at K_ε = 20: D′ ≤ 45.8 (`sim_out/Dprime_Ke20.txt`). The bound holds with a factor of about 10⁴ to spare.
  These generic fronts do not probe the worst case. The slack comes from:
  - the worst-case offset profile;
  - the L² budgets being saturated simultaneously at all scales;
  - the bound being a sup over θ.

## Gaps / caveats (precise)
- G1. Lemma S and Lemma T(ii) come from R-tilt and are not yet refereed. Lemma S is re-proved in prop_near.tex.
  With the old constants, only Lemma S is new.
- G2. Floating-point evaluation is not verified by interval arithmetic. Grid error is about 1%, and rounding is negligible.
- G3. The new proof does not touch the Start value, Proposition 4.2 or Proposition 4.4. Propositions 4.2 and 4.4 still use
  their own constants, which R-tilt updated.
