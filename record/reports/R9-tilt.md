# R9-tilt: sharper tilt bounds and the near-pair constant D

Stream R-tilt, round 9 (`reports/L-9.md`, items R2 and R3). Full statements and proofs are in
`referee/R9-tilt-claims.md`, with § references below. Scripts: `r9/tilt/tilt_constants.py` (→ `.out`) and
`r9/tilt/sanity_curves.py` (→ `.out`).

## Headline

| | old (r9/base_short) | new, drop-in | new, + split long case |
|---|---|---|---|
| C_A / C_B / C_TL | 6.394 / 9.864 / 16.257 | **C_T = 2.911** (one constant for all three) | same |
| C_μA (C_1A) | 42.53 (6.573) | C_μ = 9.608, only inside logs/profiles; C_1A gone | same |
| D_I | 485.6 | 16.03 | 16.03 |
| D_IIs | 6837.1 (727 + **5585** + 525) | 89.75 (19.37 + 1.88 + 68.51) | 89.75 |
| D_IIl | 2960.8 | 528.9 | 182.2 |
| **D** | **7322.8** | **544.9 (×13.4)** | **198.2 (×36.9)** |
| C_p / B₃ / B₅ (far, length) | 12.64 / 413.3 / 5162 | 3.855 / 126.0 / 493.5 | same |

Status: all new lemmas are **PROVED** (claims §§1–8). The constant values are PROVED formulas evaluated rigorously (§9).
The curve experiments are NUMERICAL (§10). D now binds through the long case D_IIl. That term comes from |q| ≤ 1/D for
pairs with g+λ > R, which is not a tilt question (claims G2, an R5 item).

## What changed mathematically

1. **Split-tilt identity (static, Lemma S).** For J ⊂ I, Z := |V_J × e_I| satisfies Z² ≤ N(I)²·l(J)·l(I∖J)/l(I). This
   follows from two Cauchy–Schwarz bounds, Z ≤ ∫_J|T−e_I| and Z ≤ ∫_{I∖J}|T−e_I|, added against ∫_I|T−e_I|² = N(I)²
   (the §2 identity). With |e_J−e_I|²(1−|e_J−e_I|²/4) = (Z/c(J))², this gives the one-step bound
   |e_J−e_I| ≤ ω_r s(r)Mλ_I^γ, where s(r) = (κ^{1/2}/c_A)·(r/2 or (r−1)^{1/2}). This beats both the direct bound of brief (a)
   ((r/c_A)^{1/2}) and the old c_t(r)r^{−γ}, and works for J anywhere in I (no common end needed).
2. **Top-down chain with clamped positions (Lemma T(i)).** The chain is I_k = (min(a′, b−λ_Iq^{−k}), ·), nested and
   containing J. It handles same-left, same-right and interior J with one sum ω s(q)σ_q. The only exception is base pairs
   (a = a_j) with λ_I < εq/(q−1), where one direct step of ratio < 2q/(q−1) suffices. So C_A = C_B = C_TL = C_T. The old
   chain also lost a factor q^γ by charging each step at its inner scale.
3. **L²/L¹ uses (brief (b)).** E-μ′ is ∫_a^s|T−e|² ≤ M²λ^{2γ}min(C_μλ_s, λ), and the L¹ bound is Cauchy–Schwarz on (a,s)
   only. In Prop 4.3 the time integrals then see C_μ only through log C_μ (Term I, II_α) or through profile shapes (II_β).
   Term II_α is integrated by parts in the form ∫|ϑ|FΦ ≤ ∫FF′Φ, which keeps F² = L¹² (no C_1A² factor).
4. **Offsets (Lemma O).** |p_a| for near pairs comes from Lemma S(iii):
   |(x_a−x_{a′})×e| = (c(a′,b)/c(a,b))·Z′ ≤ κ^{1/2}Mλ^{1+γ}x^{1/2}(1+x)^γ(1+κx/c_A). This is O(x^{1/2}), and its time
   integral against Φ_β converges at x → 0 with no C_TL·C_1A product. That kills the old 5585 term.
   The g = 0 leg is charged its true duration d_Lε, not 2d_Lλ: 525 → 1.9.
5. **Long case split (optional, §6.4).** For g ≤ R−λ the short-case bounds apply (I′ is a family pair). The 1/D bound is used
   only for g > R−λ, so the (K_f+1)^γ/m loss is charged only where it occurs.

## Use-by-use table (every use of C_A, C_B, C_TL, C_μA, C_1A, k₀ in §3–§5)

| place (r9/base_short) | old | new (notation of claims §0) | covered by |
|---|---|---|---|
| Def 3.3: c_t, σ_q, C_A, C_B, C_TL | chain constants | s(r), ω_*, **C_T = ω_*max(σ_q s(q), s(2q/(q−1)))** | Lemma T(o),(i) |
| Def 3.3: C_μA, C_1A | 1+κC_A², (κC_μA)^{1/2} | **C_μ = 1+κC_T²**; C_1A deleted | Lemma T(ii) |
| Thm `thm:end`(c) | C_TL, C_A, C_B | C_T in all three cases | Lemma T(i) + Lemma local(i) |
| `lem:tilt` (i) | C_TL/C_A/C_B | C_T | Lemma T(i) |
| `lem:tilt` (ii) (E-μ) | C_μA λ_s; C_1A λ_s | min(C_μλ_s, λ); (κλ_s min(C_μλ_s,λ))^{1/2} | Lemma T(ii) |
| Prop 4.2, |p_a| for g ≤ η₁R: c_t(r_f), C_B in C_p | C_p = κ[c_t(r_f)+C_B(1+1/K_f)^γ] | **C_p′ = κ^{1/2}(1+1/K_f)^{1/2+γ}K_f^{−1/2} + κC_T(1+1/K_f)^γ**; B₃, B₅ via C_p′ | Lemma O(O3) |
| Prop 4.3 Term I: ω(y) ≤ C_μA M²λ^{2γ}min(λ,c₆y) | D_I = C_μA T_I | ω(y) ≤ M²λ^{2γ}min(λ, C_μc₆y); **D_I′ = T_I + c₆χ log C_μ** | Lemma T(ii), claims §6.1 |
| Prop 4.3 II, (x_s−x_a)×e ≤ C_1A Mλ^γ max(σ_s,ε/2) | c₆²C_1A²T_a | F(s) with (F′); **Π_α = c₆²κ[d_L/c₆+χ(2+log C_μ−1/(2K_f))]** | Lemma T(ii), §6.2 |
| Prop 4.3 II, Ψ(y) ≤ C_1A Mλ^γ min(λ,y) | (in all II terms) | Ψ(y) ≤ F(u_y) ≤ κ^{1/2}Mλ^γ(min(λ,y)min(C_μy,λ))^{1/2} | (F′), §6.2 |
| Prop 4.3 II_β g=0: k₀ = max(C_1A, κ2^γC_A) | 4d_Lc₆C_1A k₀ | **Π₀ = d_L max(2c₆²κS₀, κ²2^γ/c_A)** | Lemma O(O2), §6.2 |
| Prop 4.3 II_β g>0: \|p_a\| ≤ κC_TL M(g+λ)^γ g (incl. the g′<ε/2 sub-case and the condition κ ≤ C_TL²(4−κ²)) | 2c₆²κC_TL C_1A T_b | **Π_β = 2c₆²κχ∫₀^{K_f}B**; condition deleted | Lemma O(O1), Lemma G′, Lemma P(P4) |
| Prop 4.3 long case | c₆(K_f+1)^γC_1A T_a/m | **D_IIl′ = c₆(K_f+1)^γκ^{1/2}T_l/m**, or D_IIl″ = sup_μ(S(μ)+Λ(μ)) | §6.3 / §6.4 |
| Prop 4.4 (length) | via C_p | via C_p′ (B₅′) | §7 |
| §5 heading: C_A^A, C_B^A, C₃ = 2C_B^A+C_A^A | 6.392, 9.864 | C_T^A = 2.909, C₃ = 3C_T^A | Thm (c) new |
| App. A extra: κ ≤ C_TL²(4−κ²), c_t(3) ≥ √3 | conditions | deleted. New (T1) m²r_* < 4c_A, (T2) C_μ ≥ (1+2γ)κ/c_A, (T3) γ ≤ c_A/κ, (T4) K_f(2γ−1) ≤ 3c_A/κ | claims §0 |

New symbols: s, ω_r, r_*, ω_*, C_T, C_μ, Φ_α, Φ_l, Φ_β, B, S₀, Π_α, Π₀, Π_β, T_l, S(μ), Λ(μ), D_I′, D_IIs′, D_IIl′, D_IIl″,
C_p′. Closed forms for Φ_α, Φ_l, Φ_β and their integrals are in claims §5. q_c stays a free parameter; q = 2.42 is
optimal (C_T 2.882; D 544.6 / 198.0).

## Numbers (current INPUTS; `r9/tilt/tilt_constants.out`)
- Old constants are reproduced exactly (D = 7322.7588 = 485.642 + 6837.117).
- New main tuple p: C_T 2.91086, C_μ 9.60815, D_I′ 16.0343, Π_α 19.3667, S₀ ≤ 0.228958, Π₀ 1.87582,
  ∫B ≤ 8.23049 (quad 8.22558), Π_β 68.5060, D_IIs′ 89.7485, T_l 4.86073, D_IIl′ 528.877, D_IIl″ 182.198 (worst μ ≈ 1.01;
  Λ(1) = 175.30). **D = 544.912 (drop-in) / 198.233 (split).**
- p_A: C_T^A 2.90936, D = 545.273 / 198.224.
- Far/length: C_p′ 3.8549 (old 12.641), B₃′ 126.03 (413.25), B₅′ 493.5 (5162). This also loosens (P5) and (P7)
  (other terms unchanged).
- For Stream Opt: θ̄ = f_F² + 2v₀D. At D ≈ 198 the near-pair term no longer limits v₀ below ≈ 2·10⁻³. (P5), (P7) and the
  long case decide next.

## Sanity checks (NUMERICAL; `r9/tilt/sanity_curves.out`)
36 random polygons (smooth Fourier and rough self-similar with amplitude ∝ scale^γ, stretch w ≥ 1), with the sharp
empirical κ, c_A, M per curve. Worst LHS/RHS: static split bounds 0.99999–1.0000 (identities and near-identities),
one-step T(o) 0.847, chain T(i) 0.536, E-μ′ L² 0.979 / L¹ 0.890, offset (O1) 0.899. No violation. The empirical
sup|e_J−e_I|/(Mλ_I^γ) is ≤ 1.63, against C_T ≈ 2.9 (old C_TL ≈ 16).

## Open / next
- D is now bound by D_IIl (long case, λ ≈ R, g > R−λ: |q| ≤ 1/D). Improving it needs a non-tilt idea (R5).
- Stream Opt: add (T1)–(T4) and the new formulas to verify_constants.py. Delete the two "extra" conditions. Optionally
  re-optimise q.
