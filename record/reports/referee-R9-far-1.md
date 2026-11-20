# Referee report R9-far-1 (independent, adversarial) on `referee/R9-far-claims.md`

Base text: `r9/base_short/` sec2–sec8 (read in full where relevant). Assumed as given: R-tilt statements (C_T, C_μ, C_p′;
`referee/R9-tilt-claims.md` §0) and R-near's Prop near (`r9/near/prop_near.tex`). I did not read `reports/R9-far.md` (except
§5.2, after the proof check) or `r9/far/`. Code and output: `code/referee/R9far_1/recompute.py`, `recompute.out`,
`jparts.py`, `jvariants.py`.

## Verdicts

| claim | verdict |
|---|---|
| F1 Lemma E* (replaces Lemma 2.6(v)) | **OK** |
| F2 Lemma Du* (replaces Lemma 2.7), drop-in for Thm 5.2(v) | **OK** |
| F3 Lemma 3.6(iv) | **OK** (one convention fix, below) |
| F4 Lemma T2* | **OK** |
| F5 (S1G), addendum to Lemma 8.2, Lemma 3.7(iii) | **OK** |
| F6 Prop F* incl. Lemma (J) (replaces Prop 4.2) | **OK with fixes** (empty-range convention in J_k) |
| F7 Prop L* (replaces Prop 4.4) | **OK with fixes** (interface with R-near: T_I and the "Term I" cross-reference) |
| F8 side conditions (P2*)–(P5*), (P7*), (PT) | **OK** (each is exactly what the proofs use) |
| F9 numerical point (v0 = 4.146e-3) | **NOT CONFIRMED.** J_1 and J_2 recomputed from the stated formula (3.1) come out 0.7 % and 11 % above the reported values. With them (P4*), (P5*) and (PT) fail at the printed vector (details in §4). |

## 1. Line-by-line proof check

**F1 (Lemma E\*).** Step 0: ρ ≥ ρ_* ≥ ε holds on the arc, so A = Π/ρ there (Lemma 2.2(ii)). Q and its partial derivatives are
correct. |∂₂Q| = |z(3z²−2)|/|y|² with z = y₁/|y|, and the maximum of that factor is 1, attained at z = ±1. Also
|y₂² − 2y₁²| ≤ 2|y|². Step 1: δ is C¹ (T is continuous in arclength), δ(0) = δ(l) = 0, and ∫ς² ≤ N². Step 2 uses the
standard Wirtinger constant (l/π)². Step 3: the boundary terms vanish (G(0) = 0, δ(l) = 0), and G′ = ∇Q·T because P is
fixed at fixed t. Step 4: y₂ = r_a·e^⊥ + δ, so |y₂| ≤ |p_a| + |δ|, and the three terms are bounded as stated. Step 5: the
coefficients of (a) check out exactly. Step 6: ρ sin φ = T × r. Applying Minkowski and squaring gives (b) exactly. Both
implications back to the old (v) are correct, using ρ_* ≥ ρ_m and (x+y)² ≤ 2x² + 2y². The key gain is that pointwise bounds
are now needed only on the arc, not on the convex hull, and every pointwise bound in Steps 0, 4 and 6 is taken at points
r(σ) of the arc. Correct.

**F2 (Lemma Du\*).** ρ_* is continuous because x is jointly continuous and the label set is compact. The rest of the proof
is the Grönwall argument verbatim. Since α* ≤ α and β* ≤ β whenever ρ_m ≥ ε, Du* implies the old Lemma 2.7 outright, so
every old use stays valid. There are only two uses (grep `lem:duhamel`): Prop 4.2 (replaced) and Thm 5.2(v), sec5 l.236–251.

In Thm 5.2(v), ρ_m ≥ ζ(g̃+τ) ≥ 4l and ρ_m ≥ ε, so ρ_* ≥ 4l. That gives α* ≤ aD*(4)v/ρ_m ≤ η_N*/(g̃+τ′) with
η_N* = aD*(4)v0/ζ, and β* ≤ β/π, hence c_β → c_β/π. η_N and c_β enter only Thm 5.2(v), (A5) (γ_D ≥ γ+ν+η_N) and (TS). All
of these are monotone in the favourable direction, so the smaller values are a valid drop-in.

**F3 (Lemma 3.6(iv)).**
- Each gap value occurs on exactly one leg (preamble of Lemma 3.6).
- For values ≤ Y/2: [g_i − ε/κ, g_i] ⊂ [g_{i+1}, g_i] ⊂ (g_0, Y/2], and H is non-increasing there.
- For values > Y/2: [g_i, g_i + ε/κ] ⊂ [g_i, g_{i−1}] ⊂ (Y/2, Y], and H is non-decreasing there.
- The two exceptional values contribute ≤ 2 d_L ε H_max.

Correct. *Fix (convention):* when g_0 ≥ Y/2 the first integral is 0. This is stated, but see F6 for the consequence in (3.1).

**F4 (Lemma T2\*) — checked hardest; correct.**
- *Case A* (Δ ≤ 2π − Δ0). Every position x°(u) is a virtual candidate, a true candidate, or Z_s (label 2π). These are
  exactly the three alternatives of Lemma 7.9(c). Its hypothesis |e^{iΘ_b} − e^{iΘ_a}| = 2 sin(Δ̃/2) ≥ c_sep > 2ε̄ ≥ 2ε
  holds by (SC42), (SC43) and Δ0 ≤ Δ̃ ≤ π. Lemma 7.9(c) then gives c ≥ 2 sin(Δ̃/2) itself, not only c_sep.
- *Lower bound on Δ̃.* The pointwise bound w ≤ W_x(2/|θ|_∘)^{2v} holds at every label ≠ 2π (proof of Lemma 7.10). On the
  forward and tail zones W_v, W_t ≤ W_x and |θ|_∘ < 2. The arc bound is the centred-arc rearrangement and is correct:
  2∫_0^{Δ′/2}(2/χ)^{2v}dχ = Δ′(4/Δ′)^{2v}/(1−2v).
  - For Δ′ ≥ Δ0, (4/Δ′)^{2v} ≤ (8/λ0)^{2v} by (SC41) (it is ≤ 1 if 4/Δ′ < 1), and (8/λ0)^{2v}/(1−2v) ≤ L̂ for v ≤ v̄.
  - (i) λ ≤ W_xL̂Δ.
  - (ii) For d_c, the label sets are [α0, Θ_a] + 2π and [Θ_b, 2π + b_e]. Both lie in [Θ_b, Θ_a + 2π], because
    2π + b_e < 2π + α0 ≤ 2π + Θ_a. They are disjoint, and the arc length is 2π − Δ ≥ Δ0 (Case A). So d_c ≤ W_xL̂(2π − Δ).
- *Hole and wrap pairs.*
  - Pairs straddling the hole (Θ_a < 2π < Θ_b ≤ 2π + b_e) are covered: the λ-arc contains the integrable singularity at
    2π, and the d_c-arc [Θ_b − 2π, Θ_a] does not.
  - X0-side/E_Y-side wrap pairs with 2π − Δ ≥ Δ0 are Case A.
  - Pairs with 2π − Δ < Δ0 are Case B, which is the (T2) proof verbatim and gives c ≥ k_c d_c.
- *Uniformity.* All constants are upper or lower constants (Lemma 7.2); no ε enters. λ > λ0 is used only to obtain
  Δ > Δ0.

**F5.**
- 𝒢 is non-decreasing and ≥ 0. c_0′ > 0 follows from (C3): λ0 c_0′ ≥ c_AK_RR > 0.
- λ ≤ λ0 branch: K_RR ≥ K_RK_εε ≥ ε/2, so (T1) applies and c ≥ φ(λ) ≥ c_0′λ ≥ c_0′y.
- λ > λ0 branch: T2* with d_c ≥ y.
- Stage A: a + U − b ≥ a + U_A − b, and every branch is non-decreasing in its argument.
- Lemma 3.7(iii): c(β,s;t) ≥ c(β,s;t_dd) by Lemma 2.4(c), and |P − x_β| ≤ δ_1ε. (S1G) is a t_dd-hypothesis on a pair
  inside [0,U], so it introduces no circularity in the continuity scheme.

All correct.

**F6 (Prop F\*).** Checked every inequality.
- *Distance.* Lemma 3.7 holds at every s ∈ [a,b] (locality, Lemma 3.9(ii)) with w_s ≥ g. This gives c_ρ*, c_η, c_R* as
  stated. Under (S1G), min(w_s, β+U−s) ≥ min(g, U−λ−g), which is (iii). ρ_* ≥ ε follows from (P2*), and K_1, K_2 from (J1).
- *Amplification.* Same as Prop 4.2, with the 𝒯_3 contribution replaced by aD*(K_2)vJ_1, together with (P3*) and (P4*).
- *Lemma (J).*
  - First entry: T_B = χ_gU.
  - Second entry: H(g) = ρ_G(min(g, Y−g))^{−k} has the required monotonicity, H ≤ (c_R*R)^{−k}, and g ≤ Y on 𝒯_3 (body:
    g ≤ a ≤ U−λ; tail: g ≤ g_W ≤ a). The substitution y = Y − g is correct.
- *Forcing.*
  - g > η_1R: |p_a| ≤ ρ_a ≤ ρ_* + l, so B_2U′ and B_2η* are correct (c_η may be used on (η_1R, K_RR]).
  - g ≤ η_1R: the three offset bounds are correct.
    - Bound 2: V additivity and (J2), plus C_T for the same-right-end tilt of (a′,b) ⊃ (a,b), both family pairs of the leg.
    - Bound 3: (x_a − x_{a′}) × e = c(a′,b) u × e. Then c(a,b)|u × e| ≤ (l(a,b)V_u(a,b))^{1/2} ≤ (κλ)^{1/2}N(a′,b), and
      c(a,b) ≥ c_Aλ by (CA).
- *Result.*
  - First term: weight ≤ A_0.
  - Second term: the exponent bookkeeping is correct (R^{−γ} = M/m).
  - Third term: h is non-increasing (ν+γ < 1), Lemma 3.6(i) applies with g_min = g, Φ is non-increasing, and the closed
    form of ∫x^pĈ is correct (it matches quadrature to 30 digits).

*Fix (exact text) for (3.1):* replace "∫_{K_RR}^{U_0/2} ρ_G^{−k}" by "∫_{K_RR}^{max(K_RR, U_0/2)} ρ_G^{−k}". As written,
the signed integral is negative if U_0 < 2K_RR. (This is harmless at the reported point: K_RR = 3.6e-4 ≪ U_0/2 = 3.45.)

*Drop-in.* The old Prop 4.2 is used by:
- (1) the start value of Prop near: only N ≤ 𝔣Mλ^{1/2+γ}, supplied; R-near uses only this, see `prop_near.tex` l.172;
- (2) sec 4.4: the E bound, supplied;
- (3) Prop 4.4: replaced, and Prop L* uses only F*'s ρ_* items.

No other file uses c_ρ, c_R, ρ_m or the bounds of Prop 4.2 (grep sec1, sec5–8).

**F7 (Prop L\*).**
- Far regimes:
  - g > K_RR: (log l)′ ≤ v/ρ_*, then J_1.
  - (η_1R, K_RR]: c_η, then Lemma 3.6(i).
  - g ≤ η_1R: E*(b) divided by l. The bounds N/l^{1/2} ≤ K_f^{−γ}Mg^γ and l^{1/2}N ≤ κ^{1/2}K_f^{−1−γ}Mg^{1+γ} give
    B_5* exactly, and then I_5.
- Near: the increment v κ T_I λ is re-derived correctly, as d_L(κc_6+1) + d_L + c_6χ_gΨ_I.
- The final combination (1+δ)e^X + v0κT_I ≤ (1+δ)L_J* is correct.

*Fixes (interface with R-near):*
- (a) `prop_near.tex` l.8 deletes T_I from Def 3.3, but Prop L* (and also R-tilt's D_I′) uses T_I. Replace that line by
  "Delete T_a, T_b, k_0, D_I, D_IIs, D_IIl; keep Ψ_I and T_I (used in Proposition L*)."
- (b) In Prop L*, "Near", replace "Exactly as for Term I of Prop 4.3 (with κ in place of C_μAM²λ^{2γ})" by: "With
  ρ̄ := max(ε, min_s ρ_s), ∫_ε^∞ω̃y^{−2}dy ≤ κc_6h_1(c_6ρ̄) ≤ κc_6h_1(max(c_6ε, g)) (Lemma 3.7, second form; Lemma 4.1)."
  Prop 4.3's Term I text no longer exists after R-near's replacement.
- (c) Notational: in Lemma 3.9 (Imp), its proof, the sec4 standing assumptions (l.7) and (A1)/(A5) of sec8, read L_J* for
  L_J and (P0)–(P7*) for (P0)–(P7). L_J* ≥ 1 still holds, as Lemma 3.9 needs.

## 2. Drop-in summary (each replaced label, each use)

- `lem:excess`(v): used in `lem:duhamel` and `prop:length`, both replaced. E* implies the old (v).
- `lem:duhamel`: used in `prop:far` (replaced) and Thm 5.2(v) (OK with η_N*, c_β*). Du* implies the old lemma.
- `lem:gapint`: only an item is added.
- `lem:dist`: only (iii) is added.
- `lem:start`: addendum only.
- `prop:far`: uses checked above.
- `prop:length`: used in sec 4.4 and Lemma 3.9 via (Imp)/L_J (fix (c)).
- (S1G) is optional. Without it 𝒢 ≡ 0, J_k reduces to its first entry, and everything reduces to (S1).

## 3. Points B1–B4 of the claims file

B1 is confirmed (§1 F4). B2 is confirmed. B3 is confirmed, and in fact Du* implies the old lemma. B4: not re-run; it is not
needed, since the proof of E* is complete.

## 4. Constants at the parameter vector of R9-far.md §5.2 (`recompute.out`)

Touch-down at (v̄ = v0, η 0.131449, ε̄ 1e-3, ξ_1 2.42695, λ0 0.010607, G_T 4.16113e-4): **all (SC1)–(SC48) hold.**

| constant | recomputed | reported |
|---|---|---|
| c_N | 6.4132 | 6.41 |
| μ̄_T | 0.012387 | — |
| k_c | 0.95516 | 0.955 |
| U_max | 6.8966 | 6.90 |
| W_xL̂ | 1.16243 | 1.162 |
| c_ρ* | 0.76630 | 0.766 |
| c_η | 0.96091 | 0.961 |
| c_R* | 9.7090 | 9.71 |
| c_amp* | 1.73489 | 1.73 |
| B_2U′ | 0.99409 | 0.994 |
| B_2η* | 2.81144 | 2.81 |
| C_p′ | 5.3076 | 5.31 |
| C_p^V | 5.3063 | — |
| C_ar | 1.7312 | — |
| B_3′ | 11.192 | 11.2 |
| B_5* | 68.663 | 68.7 |
| I_5 | 0.59462 | — |
| T_I | 15.006 | — |
| aD*(4) | 1.092243 | — |
| **J_1** | **28.410** | **28.2** |
| **J_2** | **12634** | **1.14e4** |
| X_far* | 0.13376 | 0.133 |
| **L_J*** | **1.22836** | **1.2274** |

J_1 and J_2 use (3.1) with 𝒢 = min(c_0′y, k_c y, 2 sin(½min(π, y/(W_xL̂)))), c_0′ = 0.99741, a′ = 1 − μ̄_T. J was
checked piecewise (`jparts.py`) and against the analytic sine-branch integral. The sine branch binds for all y beyond the
plateau, because 1/(W_xL̂) = 0.860 < k_c.

At v0 = ν/c_amp* = 4.14578e-3 ((P3*) tight; the printed 4.146e-3 violates (P3*) by 5e-5 relative, which is rounding):
- **(P4\*)** 0.124293 > log A_0 = 0.123438 (fails by 0.7 %);
- **(P5\*)** 0.427462 > 𝔣 = 0.426366 (fails by 0.26 %);
- (P2*) holds with large slack, and (P7*) L_J* = 1.22836 < κ holds;
- **(PT)**: my reconstruction of δ_t (assembly formulas of `verify_constants.py` with C_T for the stage-A tilts and
  η_N = aD*(4)v0/ζ) gives δ_t = 0.011943. Then (1+δ_t)L_J* = 1.24304 > κ = 1.24215, which **fails** (by 7e-4 relative).
  With the reported L_J = 1.2274 it would pass with ≈ 6e-5 slack, which matches the reported (PT) slack. So the failure
  comes from J_1.
- (A5) γ_D ≥ γ+ν+η_N holds (slack 2.4e-5); ω_0 ≤ ω̄ and U_E ≤ G_T hold.

The reported values J_1 ≈ 28.2 and J_2 ≈ 1.14e4 are not reproduced by any reading of 𝒢 I tried. 𝒢 without the sine branch
gives J_1 = 25.19 and J_2 = 11034 (`jvariants.py`). So the R-far code evaluates something other than the stated (3.1),
or uses different touch-down numbers. Since (P4*), (P5*) and (PT) are binding, the point **v0 = 4.146e-3 is not verified**.
The proofs are unaffected. A re-optimisation with (3.1) as stated should move v0 by roughly 1 % (≈ 4.1e-3); I have not
computed this. Also not verified here: D′ (R-near) and outward rounding.
