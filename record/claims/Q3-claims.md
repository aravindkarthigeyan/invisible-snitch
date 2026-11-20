# Q3 — claims: the touch-down theorem with every constant an explicit function of v̄ (design T, D₁ = 1)

**Version 2** (reconciles the fixes of `reports/referee-RQ3-1.md` and `reports/referee-RQ3-2.md`; version 1 is kept verbatim as
`referee/Q3-claims-v1.md`). Both referees: no false statement, no gap in Q1–Q7, Q.H, Q.T, HT′; "OK with fixes".
Typeset as `paper/sec_HTp.tex` (Section "The touch-down data for larger v", label sec:HTp).

**Changelog v1 → v2** (each referee fix applied once; location in this file in brackets):
* (C1) RQ3-1 §3, first bullet: new side condition **(SC51) z_T x̄_e + ε̄ < 1 and G + z_T x̄_e ≤ 1**, added to §0.4, to the hypothesis
  of Theorem Q.H (§8) and cited at the two places that use it: (T4′) "(u′ + z₀)^{1−μ_T} ≤ (u′ + z₀)^{1−μ̄_T}" and (T5′) "(z₀ + ε < 1)".
  It holds in every column of the table (z_T x̄_e + ε̄ ≤ 0.0667, G + z_T x̄_e ≤ 0.212; values in §9) and in the column
  (6·10⁻⁵, 0.1) used downstream (0.0506, 0.0996).
* (C2) RQ3-1 §3, second bullet: (T1′) near X₀, "u_b ≤ max(2λ₀, 2u₁ε̄) ≤ η" now cites (SC39) and (SC40) [§8].
* (C3) RQ3-1 §3, third bullet: §0.2 range of η is (0, π/6] (forced by (SC4)) [§0.2].
* (C4) RQ3-2 §3 (Lemma Q5), optional: the tacit A_max ≤ 2 in Q5(b) is stated and proved (A_max = W_w ≤ e^{v̄t̄₁/sin ½} < 1.6 by
  (SC3), (SC35)) [§5].
* (C5) RQ3-2 §4: threshold wording in §10.2 replaced by the referee's text (ε ≲ 10^{−57570} at v = 10⁻⁶, x_e in place of ε) [§10.2].
* (C6) RQ3-1 §6 / RQ3-2 §4: §10.2 now records that `paper/sec_T1.tex` has already been repaired (proof of thm:HT (T1): the author's
  split, near-E_Y case; prop:T1-arcs(2): RQ3-1's integrated-curvature device, which keeps the constant 0.36, so the replacement 4.15
  of v1 is superseded there); see rem:T1-status. The repair is not repeated in sec_HTp, only cited.
* (C7) Status lines (this header, §9 Corollary Q.T, §10.1): (SC51) is checked in addition to "ALL OK (50)" of `constants.py`
  (which does not contain (SC51)); RQ3-1 checked it as keys `i1`, `i2`, `code/Q4/final.py` as (SC51a,b).
* (C8) No change of any formula, constant or table value. RQ3-1 §3 fourth bullet (Q1(c) tilt term) and §7 (minor remarks) and
  RQ3-2 §5 remark (sec_T2 caps v₀) require no action.

**Unreconciled / for the coordinator** (not fixable in this file):
* (U1) `paper/sec_T1.tex`, rem:T1-status, says the reversed inequality is "relevant only for astronomically small ε, below about
  10^{−6000} at v = 10^{−6}". RQ3-2 §4 gives the actual threshold ε ≲ 10^{−57577} (the v1 necessary condition was ε < 10^{−28000}).
  "Below 10^{−6000}" is a true but loose statement; the number 6000 does not appear in either report. Not edited (not part of this task).
* (U2) `reports/Q4-1.md` §3 rounds the touch-down constants to the nearest 6th digit, not outward: T₂ 3.73246 (exact 3.7324640…),
  U_max 6.29319 (6.2931948…), c_N 2.72159 (2.7215935…), θ_v 1.07002 (1.0700235…), c_T4 1.04262 (1.0426250…), c_zhi 1.56562
  (1.5656236…). As Q4-1 says, its verification used exact inputs, so nothing downstream changes; sec_HTp prints outward-rounded values.
* (U3) RQ3-1's table (§4) uses its own x₁, G choices; it agrees with `code/Q3/out/table.txt` where the parameters coincide
  (e.g. (10⁻², 0.1), (10⁻², 0.2)); RQ3-2 checked all 18 columns of `table.txt` with the printed parameters (≤ 7·10⁻⁴ relative).
  The paper's table is `table.txt` (re-generated 2026-11-19 by `constants.table`, identical).

Stream Q3, round 7. **Only statements claimed PROVED, with proofs.** Source: `referee/P8a-claims.md` v3 (= `paper/sec_T1.tex`,
refereed: `reports/referee-RP8a-1.md`, `-2.md`). Same method (exact transport lemmas on the two straight runs), same design T, same
curve x⁰, same 𝒢. Constants script (one formula per named constant below, same names): `code/Q3/constants.py`; numerical
verification (not part of any proof): `code/Q3/scan.py`, `code/Q3/mono_check.py`, outputs in `code/Q3/out/`.

**Claimed PROVED.**
* Lemmas Q1–Q7 (§§1–7) and **Theorem Q.H** (§8): for every parameter tuple (v̄, η, ε̄, x₁, λ₀, G) satisfying the side conditions
  (SC) of §0.4, hypothesis (H_T) = hyp:HT of `paper/sec_T2.tex` (items (T0)–(T5), 𝒢 ⊂ [0,U)) holds for design T with D₁ = 1 for
  **all v ∈ (0, v̄] and ε ∈ (0, ε̄]**, with the constants of §0.3 evaluated at (v̄, η, ε̄, x₁, λ₀, G), together with the sharper forms
  (T1′)–(T5′).
* **Corollary Q.T** (§9): (SC) hold for the parameter columns of the table in `reports/Q3-1.md` §3 (= `code/Q3/out/table.txt`) (each (SC) is
  one inequality between explicit numbers, evaluated in 50-digit arithmetic by `constants.py`, which prints "ALL OK (50)" per column). In particular (H_T) holds for
  v̄ = 2·10⁻², 10⁻², 10⁻³, …, 10⁻⁶ (ε̄ = 10⁻³) with the constants of that table.
* **Theorem HT′** (§10): the sharper forms requested by Q2 at v ≤ 10⁻⁶, ε ≤ 10⁻³ (the row v̄ = 10⁻⁶, η = 0.1 of §9), and the
  P8a-constant forms; plus a **repair** of the proof of (T1) in thm:HT / Theorem P8a.H (a far-case step is wrong as written for
  astronomically small ε; the statement is true; §10.2).

**Not claimed.** Anything after t_s. The virtual front on seen labels. P8a Lemma 4(d) (θ_s), Lemma 10 (hole edges), Proposition
P8a.1 — not needed for (H_T), not re-proved here. D₁ ≠ 1 (explored numerically only, §9 Remark). v̄ beyond the table: the proof
is the same, but (SC) fail (first failures listed in §9).

**Unchanged, cited (statements and proofs exactly as in P8a v3 / sec_T1):** P8a Lemma 1 (lem:T1-coord), Lemma 2 (lem:T1-first), Lemma 3
(lem:T1-second, with the two-time relation), Remark (i) after Lemma 3 (rem:T1-tilt), Lemma 5(a) (lem:T1-tang(a)), lem:T1-elem (= [D, Lemma D0(c)] and
[P7, Fact 0.2(i)]) — all exact for every v ∈ (0,1); Lemma 4(a) (seen in run 1; exact) and Lemma 11(d) (convention).
**Changed (re-proved below with v̄-dependent constants):** Lemma 4(b),(c),(e) → Q1; Lemma 5(b),(c) → Q2; Lemma 6 → Q3; Lemma 8 → Q4;
Lemma 7 → Q5; Lemmas 9, 11(a)–(c) → Q6; new chord lemma Q7; Theorem P8a.H → Theorem Q.H.

External inputs as in P8a: [I] (integrals C = ρg(β), h = ρ(cos β + v), h′ = −(1−v²)); [B] (field F, f, a* ≤ 2/ε, virtual candidates,
|x_θ′| ≤ v, w ≥ 1 non-decreasing, w_t ≤ v a* w, chords of virtual candidates non-decreasing, Lemma VC; true-flow laws
w_t/w = v sin²φ/ρ, ψ_t = −(v/ρ) sin φ cos φ, k_t = (v/ρ)(1 − 3 sin²φ)k + (v/ρ²) sin φ(3cos²φ − 1)); [D] Lemma D0(a),(c); [P7] Fact 0.2(i).

---------------------------------------------------------------------------------------------------------------------

## §0. Setting, parameters, constants, side conditions

### 0.1 Setting
D₁ = 1, design T exactly as def:T: t₁ = 1/(1−v) + 1 = 2 + μ, α₀ = arccos(v + 1/t₁), û = e^{iβ*}, t_a, t_s, t₂ = t₁ + ρ₀/(1−v).
μ := v/(1−v), μ_T := 3v/(1+v); g(β) = sin β/tan^v(β/2), g_max = g(arccos v). x := |θ − α₀|; the **window** is
I_η := [α₀ − η, α₀ + η]; δ(t) := t₂ − t. Frames, (r(θ), b(θ)), τ_b = tan(b/2), C, a, c, A = ∂_θ r as in P8a §3; (ρ₁, β₁, τ₁) as in P8a §2.

### 0.2 Parameters
v̄ ∈ (0, 1/10], η ∈ (0, π/6] [v2, C3: (SC4) forces η ≤ π/6], ε̄ ∈ (0, 1), x₁ > 0, λ₀ ∈ (0, 1/4], G > 0. Throughout, **0 < v ≤ v̄ and 0 < ε ≤ ε̄**.

### 0.3 The constants (all formulas evaluated with v := v̄, μ := μ̄ := v̄/(1−v̄), μ_T := μ̄_T := 3v̄/(1+v̄))
Rule (M). Each constant below is used in the proofs as an upper bound (U) or a lower bound (L) for a quantity that depends on
the actual v ≤ v̄. In every case the formula is obtained from the corresponding v-formula by monotone substitutions that are valid
for v ≤ v̄: v ↦ v̄ in increasing positive terms (1+v, v t₁, 1/(1−v), …), in bases ≥ 1 raised to the power v, μ, μ_T (resp. bases ≤ 1
raised to 1−v, 1−μ, 1−μ_T, 1/(1+v)), and in lower bounds through decreasing terms; the few non-obvious cases are pointed out in the
proofs. Hence each (U)-constant is ≥, each (L)-constant ≤, the value the proof needs at the actual v.

*Basic.* t̄₁ := 2 + μ̄; g_b := g_max(v̄) = (1−v̄²)^{1/2}((1+v̄)/(1−v̄))^{v̄/2} (g_max is increasing in v: d log g_max/dv = artanh v > 0;
g_max ≥ g(π/2) = 1); α̲ := arccos(1/2 + v̄); Δ_a := π/3 − α̲; d₁ := v̄t̄₁ + μ̄; e_ρ := v̄t̄₁ + Δ_a + μ̄;
T₂ := t̄₁ + (√3 + e_ρ)/(1−v̄); d_s := v̄T₂; d_P := max(μ̄, d_s + Δ_a).

*Run 1.* ρ_m := sin(1/2); W₁(ρ) := e^{v̄t̄₁/ρ}, ω₁(ρ) := v̄t̄₁/(2ρ), κ₁(ρ) := (2/ρ + 1/ρ²)v̄t̄₁e^{2v̄t̄₁/ρ};
k_arm := (1+v̄)/(cos ½ − v̄) + 2v̄/(1−v̄²); d_arm := (1+v̄)/((1−v̄)(cos ½ − v̄)) + v̄/(1−v̄²);
e₁ := (2 − cos ½)(1 + tan²¼) + (1+v̄)tan(¼)^{1−v̄}, E₁ := max(1, e₁/(1−v̄)), W_arm := E₁^{v̄}/(1−v̄);
k_all := max(k_arm, 1 + κ₁(ρ_m)), W_all := max(W_arm, W₁(ρ_m)(π/2)^{2v̄}).

*Window.* θ_L := α̲ − η, θ_R := π/3 + η, R₀(θ) := (5 − 4cos θ)^{1/2} = |e^{iθ} − 2|, R_L := R₀(θ_L), R_R := R₀(θ_R),
r_min := R_L − d₁, r_max := R_R + d₁; ρ_w := sin θ_L, W_w := W₁(ρ_w), ω_w := ω₁(ρ_w), κ_w := κ₁(ρ_w); ι := 1 + v̄t̄₁/sin θ_L;
q_min := sin(α̲ + η/2)/R_R, q_max := sin(π/3 − η/2)/R_L; rΛ_min := 4q_min/(1 + d₁/R_L), rΛ_max := 2t̄₁ι q_max/(1 − d₁/R_L);
Λ_min := 4 sin(α̲ − η/2)/r_max², Λ_max := 2t̄₁ι sin(π/3 + η/2)/r_min²;
m₀ := max(|1 − 2cos θ_L|, |1 − 2cos θ_R|)/R_L, ω_p := arcsin(d₁/R_L), ang := arcsin m₀ + ω_w + ω_p, A_min := cos(ang), A_max := W_w;
b_lo := Λ_min(1 − η²/48)/4, b_hi := Λ_max/4, b̄ := b_hi η², e_τ := tan(b̄/2)/(b̄/2) − 1, β₂ := b_hi(1+e_τ)/2;
C_hi := 2r_max β₂^{1−v̄}, C_lo := 2r_min(b_lo/2)/(1 + tan²(b̄/2));
aux := rΛ_max b̄ η/2, a_min := A_min cos b̄ − aux, a_max := A_max(1+v̄) + aux;
L_C := 2Λ_max/Λ_min + ηA_max/r_min, L_lo := 2(cos b̄ − v̄)(Λ_min/Λ_max)(1 − η²/32);
S₁ := rΛ_max(r_max a_max L_C + (1+v̄)η)/(2(1−v̄²)r_min).

*Forward arc.* h_f := A_min − r_max b_hi²η³/2, ρ_c := h_f/(1+v̄), Q := (1+v̄)r_max/h_f, y_f := 2r_maxβ₂;
Y₁ := (rΛ_max/2 + A_max b_hi(1+e_τ)η)/a_min, Ȳ := Y₁η^{1−μ̄}Q^{μ̄}, θ_f := max((1+v̄)Y₁, v̄y_f/ρ_c)/(1 − v̄ − v̄Ȳ),
W_f := a_max[(1 + v̄ + v̄Ȳ)² + ((1+v̄)Ȳ + v̄)²]^{1/2}/(1−v̄²); δ₁ := v̄/(3(1−v̄)²x₁), τ_f := β₂Q^{1+μ̄}, τ̄_f := τ_fη^{1−μ̄},
ρ_u := ((1+v̄)A_max + δ₁)/(1 − 2τ̄_f²), S₂ := (2τ_f + θ_fQ^{μ̄})(ρ_u a_max L_C + 1 + v̄)/((1−v̄²)ρ_c), K_f := Q^{μ̄}(1 + κ_w + S₁v̄) + S₂v̄.

*Virtual labels.* θ_v := Q^{μ̄}e^{μ̄}(θ_f + μ̄e^{2μ̄}y_f x₁), W_v := W_f e^{2μ̄}, u₁ := W_v x₁.

*Tail.* xe_lo := C_hi^{−1/2}, xe_hi := (g_b/C_lo)^{1/(2−2v̄)}, x̄_e := xe_hi ε̄^{1/2}; δ₂ := (1+v̄)v̄/(3(1−v̄)xe_lo), h_t := A_min − δ₂,
h_T := (1+v̄)A_max + r_max b_hi²η³/2; m_τ := (2h_t/C_hi)η^{−(1−2v̄)}, τ_t := m_τ^{1/(1+v̄)}, e_t := (1+v̄)/(m_ττ_t^{1−v̄});
y_c := 2(1+e_t)h_T/(1−v̄), y_T := C_hi^{1/(1+v̄)}max(1,y_c)^{v̄}; T_t := (max(1, y_c/C_lo)·2/b_lo)^{v̄};
Y₂ := T_t rΛ_max/(2a_min), Ȳ₂ := Y₂η^{1−μ̄_T}, θ_t := Y₂ + v̄y_T/h_t; z_T := (h_T + v̄y_Tη^{1−μ̄_T})/(1−v̄),
ρ_T := z_T(1 + (y_Tη^{1−μ̄_T}/h_t)²)^{1/2}; W_t := a_max[(1 + v̄ + v̄Ȳ₂)² + ((1+v̄)Ȳ₂ + v̄)²]^{1/2}/(1−v̄²);
S₃ := (y_T/h_t + θ_t)(ρ_T a_max L_C + 1 + v̄)/((1−v̄²)h_t), K_t := T_t(1 + κ_w + S₁v̄) + S₃v̄;
x₂ := 1/(3(1−v̄)A_min); h_a := 1 − A_max/2 − r_max b_hi²ε̄³/32, Q_a := (1+v̄)r_max/h_a, τ_a := β₂Q_a^{1+μ̄}ε̄^{1−μ̄}/4.

*Bulk and hole.* e_β := arcsin(e_ρ/√3), b_l := b_lo η², y_b := sin b_l, H_b := 3 + d₁ + (1+v̄)(√3 + e_ρ)/(1−v̄),
T_b := 2H_b/(y_b tan(b_l/2)), S_b := (3+v̄)/(2(1−v̄)y_b), K_b := T_b^{v̄}(k_all + S_bv̄) + S_bv̄, W_b := ((1+v̄)/(1−v̄))T_b^{v̄};
r_B := 0.005 + v̄t̄₁, ρ_h := 1/2 − d_P − r_B − v̄T₂.

*Assembly.* W_x := max(W_v, W_t, W_bW_all); U_max := (W_v + W_t)η + W_bW_all(2π − 2η)/(1 − 2v̄);
L̂ := (8/λ₀)^{2v̄}/(1−2v̄), Δ₀ := λ₀/(W_xL̂), c_sep := 2 sin(Δ₀/2), κ₂ := min(cos(θ_vΔ₀^{1−μ̄}), h_t/W_t);
K_* := max(K_fW_v^{μ̄}, K_tW_t^{μ̄_T}, K_b); c_far := K_*/√12, c_near := θ_v((12u₁² + 6u₁ + 1)/(3 − 2μ̄))^{1/2},
c_tail := θ_t(19/(3 − 2μ̄_T))^{1/2}, c_N := max(c_far, c_near, c_tail);
ϑ₃ := θ_vG^{3/4−μ̄}, ϑ₄ := θ_t(x̄_e + G)^{1/2−μ̄_T}(2^{1/4}xe_hi^{1/2} + G^{1/4}), c_y := y_T/h_t², ϑ₅ := 2^{1/4}c_y max(1, z_T xe_hi),
ϑ_T := max(ϑ₃, ϑ₄, ϑ₅); C_z := z_T xe_hi ε̄^{1/4}; c_T4 := θ_t/h_t.

### 0.4 Side conditions (SC) (the names are the keys of `cond` in `constants.py`)
(SC1) √3 − e_ρ > ε̄. (SC2) cos ½ > v̄. (SC3) θ_L ≥ 1/2. (SC4) θ_R ≤ π/2. (SC5) η ≤ π/3. (SC6) cos θ_L < 4/5.
(SC7) cot(α̲ − η/2)/2 < s(θ_R), s(θ) := 2 sin θ/(5 − 4cos θ). (SC8) d₁ < R_L. (SC9) ang < π/2. (SC10) b̄ < π/2. (SC11) β₂ < 1.
(SC12) b_lo < 2. (SC13) a_min > 0. (SC14) cos b̄ > v̄. (SC15) L_lo > ηA_max/r_min. (SC16) 0 < h_f ≤ 1 − v̄². (SC17) ρ_cx₁ > 1.
(SC18) Q ≥ 1. (SC19) 1 − v̄ − v̄Ȳ > 0. (SC20) 1 − 2τ̄_f² > v̄. (SC21) C_hi < 1. (SC22) C_loη² > ε̄g_b. (SC23) g_b > C_lo.
(SC24) x̄_e < η. (SC25) h_t > 0. (SC26) m_τ > 1. (SC27) x₂v̄ ≤ 1/2. (SC28) xe_lo ≥ 1/2. (SC29) h_a > 0. (SC30) 1 − 2τ_a² > 0.
(SC31) A_min > 4τ_a². (SC32) b_l ≤ π/6 − e_β. (SC33) π/3 + 2e_β ≤ π − b_l. (SC34) T_b ≥ 1. (SC35) v̄ ≤ 1/10.
(SC36) ρ_h > 0. (SC37) 2g_bε̄ < θ_L and g_bε̄ ≤ 1. (SC38) 2 − 2d_s ≥ 1. (SC39) 2λ₀ + min(x̄_e, λ₀) ≤ η. (SC40) 2u₁ε̄ ≤ η.
(SC41) λ₀ ≤ 1/4. (SC42) W_xL̂ ≤ 2. (SC43) Δ₀ ≤ η. (SC44) c_sep > 2ε̄. (SC45) θ_vΔ₀^{1−μ̄} ≤ π/2. (SC46) κ₂ ≥ 1/2.
(SC47) K_*λ₀^{1−μ̄_T} ≤ π. (SC48) u₁ ≥ 1/2. (SC49) c_Nλ₀^{1−μ̄_T} ≤ 1. (SC50) G > 0 and x̄_e + G ≤ η.
(SC51) [v2, C1] z_T x̄_e + ε̄ < 1 and G + z_T x̄_e ≤ 1 (not in `constants.py`; checked separately, §9).
Each (SC) evaluated at v̄ implies the same inequality at every v ≤ v̄ where the proof uses it (by rule (M)); this is used tacitly.

---------------------------------------------------------------------------------------------------------------------

## §1. Run 1 (replaces P8a Lemma 4(b),(c),(e))

**Lemma Q1.** (a) *(exact; = P8a Lemma 4(a))* A true candidate α ∈ (−π, π] is seen during [0,t₁] iff |α| ≤ α_s, where g(α_s) = εg_max;
α_s ≤ 2g_bε (so α_s < θ_L by (SC37)); for α ∈ [α_s, 2π − α_s], ρ_α ≥ ε on [0,t₁]. Every candidate (true or virtual) satisfies
|S(t) − e^{iα}| ≤ vt.
(b) *Middle.* For α ∈ [1/2, 2π − 1/2]: ρ_α(t) ≥ ρ_m on [0,t₁]; for α ∈ [1/2, π/2] (and the mirror labels), ρ_α(t) ≥ sin α on [0, t₁].
If ρ_α ≥ ρ on [0,t₁] then at t₁: 1 ≤ w₁ ≤ W₁(ρ), |arg ∂_αS_α(t₁) − (α + π/2)| ≤ ω₁(ρ), |k₁ − 1| ≤ κ₁(ρ).
(c) *Arm.* For α ∈ (0, 1/2]: ρ₁ ≥ 1 + v, τ₁ > 1, y(α,t₁) ≥ sin α; |k₁| ≤ k_arm; the tangent at t₁ is e^{i(π/2+δ)} with
0 ≤ δ ≤ tan δ ≤ d_arm·y(α,t₁); w₁ ≤ W_arm(2/α)^{2v}; and y(α,t₁) ≤ 2E₁ tan(α/2)^{(1−v)/(1+v)}.
(d) For all α ∈ (0,2π), χ := min(α, 2π−α): |k₁| ≤ k_all, 1 ≤ w₁ ≤ W_all(2/χ)^{2v}; ρ₁ ≥ 1 + v.

*Proof.* (a) P8a Lemma 4(a), whose proof is exact; α_s ≤ 2τ_s ≤ 2(εg_max)^{1/(1−v)} ≤ 2εg_max ≤ 2g_bε (εg_max ≤ g_bε̄ ≤ 1).
Speed ≤ v: |S′| ≤ v ([I], [B]).
(b) As in P8a Lemma 4(b) (the argument is exact): for α ∈ [1/2, π/2], y′ = vy/ρ ≥ 0, so ρ ≥ y ≥ sin α ≥ sin ½; for α ∈ [π/2, π],
X := Re S has X − t ≤ cos α ≤ 0 and X ≤ cos α, y ≥ sin α, so ρ² ≥ X² + y² ≥ 1; mirror for the lower half. With the true-flow laws [B]:
(log w)_t = v sin²φ/ρ ∈ [0, v/ρ] gives 1 ≤ w₁ ≤ e^{vt₁/ρ}; |ψ_t| ≤ v/(2ρ) gives the tangent bound; and with |1 − 3sin²φ| ≤ 2,
|sin φ(3cos²φ − 1)| ≤ 1 (max of |s(2 − 3s²)| on [−1,1] is 1): |k − 1|_t ≤ (2v/ρ)|k − 1| + 2v/ρ + v/ρ², so by Gronwall (k(0) = 1)
|k₁ − 1| ≤ (2/ρ + 1/ρ²)vt₁e^{2vt₁/ρ}. Since t₁ ≤ t̄₁ and v ≤ v̄, these are ≤ W₁(ρ), ω₁(ρ), κ₁(ρ).
(c) h₁ = cos α + v − (1−v²)t₁ = −(1−v²) − (1 − cos α) < 0, so cos β₁ + v < 0, i.e. cos β₁ < −v, β₁ > π/2, τ₁ > 1; and
|h₁| = ρ₁|cos β₁ + v| ≤ ρ₁(1 − v) gives ρ₁ ≥ (1−v²)/(1−v) = 1 + v. y = Cτ^v is non-decreasing, y(0) = sin α.
*Curvature.* P8a Lemma 4(c) proof, exact part: with t′ = 0, 𝔖′ = 0 and k₁ = 𝒯/w₁³ − 𝔖₁, 𝒯 := (τ₁/τ_α)^v ≥ 1, and (Lemma 2)
(1+v)w₁ ≥ ImΞ = (cos α − v)𝒯, w₁ ≥ 1: 0 ≤ 𝒯/w₁³ ≤ (1+v)/(cos α − v) ≤ (1+v)/(cos ½ − v). For 𝔖₁: a = −sin α and ∂_α log C =
(cos α − v)/sin α, so |ρ₁a∂_α log C/w₁²| ≤ ρ₁(cos α − v) ≤ ρ₁, and |𝔖₁| ≤ (v/((1−v²)ρ₁))[ρ₁ + v + 1] = v/(1−v²) + v/((1−v)ρ₁) ≤ 2v/(1−v²).
*Tilt.* P8a Lemma 4(c) proof (exact formula): tan δ ≤ (1+v)sin α/((1−v)(cos α − v)𝒯) + v sin β₁/(1 + v cos β₁), and 1 + v cos β₁ ≥ 1 − v,
𝒯 ≥ 1, sin α ≤ y, sin β₁ = y/ρ₁ ≤ y/(1+v): tan δ ≤ d_arm·y (with v ≤ v̄, cos α ≥ cos ½).
*Stretch.* |Ξ|² = sin²α + (cos α − v)²𝒯² ≤ 𝒯², so w₁ ≤ 𝒯/(1−v). By Lemma 1(d) (h₁ < 0) and τ₁ > 1:
(1−v)τ₁^{1+v} = 2|h₁|/C + (1+v)τ₁^{v−1} ≤ 2|h₁|/C + 1 + v, with |h₁| ≤ 2 − cos ½, C = g(α) = 2τ_α^{1−v}/(1+τ_α²) ≥ 2τ_α^{1−v}/(1 + tan²¼)
and 1 + v ≤ (1+v)tan(¼)^{1−v}/τ_α^{1−v} (τ_α ≤ tan ¼). So τ₁^{1+v} ≤ (e₁/(1−v))τ_α^{−(1−v)} ≤ E₁τ_α^{−(1−v)}, τ₁/τ_α ≤ E₁^{1/(1+v)}τ_α^{−2/(1+v)},
𝒯 ≤ E₁^{v/(1+v)}τ_α^{−2v/(1+v)} ≤ E₁^{v}(2/α)^{2v} (E₁ ≥ 1; τ_α ≥ α/2, 2/α > 1). Hence w₁ ≤ W_arm(2/α)^{2v} (E₁, (1−v)^{−1} increase with v).
*Size of y.* y = Cτ₁^v ≤ 2τ_α^{1−v}·(E₁τ_α^{−(1−v)})^{v/(1+v)} ≤ 2E₁τ_α^{(1−v)/(1+v)}.
(d) (b) with ρ = ρ_m for χ ≥ 1/2: k₁ ≤ 1 + κ₁(ρ_m), and w₁ ≤ W₁(ρ_m) = W₁(ρ_m)(π/2)^{2v}(2/π)^{2v} ≤ W_all(2/χ)^{2v} (χ ≤ π);
(c) and the mirror symmetry for χ < 1/2 (k₁ is mirror invariant, w₁ too). ρ₁ ≥ 1 + v: the argument of (c) uses only h₁ ≤ −(1−v²). ∎

---------------------------------------------------------------------------------------------------------------------

## §2. Tangency and the data at t₁ on the window (replaces P8a Lemma 5(b),(c))

**Lemma Q2.** (a) *(exact; = P8a Lemma 5(a))* ∂_θb = Λ(θ) sin((θ − α₀)/2), Λ = 2t₁ sin β₁ sin((θ+α₀)/2)/(ρ₁ sin θ) > 0 on (0,π); b ≥ 0
has its unique zero at α₀ on (0, π) and b ∈ (0,π) on the lower half; the front at t₁ is tangent at S_{α₀}(t₁) to the ray of run 2.
(b) α₀ ∈ [α̲, π/3]; |ρ₀ − √3| ≤ e_ρ; t_s ≤ t₂ ≤ T₂ and 0 < t₂ − t_s ≤ vε/(3(1−v)²); t_s − t_a ≤ ε/(1−v); |x_θ(t) − e^{iθ}| ≤ vt ≤ d_s for
t ≤ t_s (every true or virtual candidate); P([t₁,t_s]) lies within d_P of 𝒮₀ := [2, e^{iπ/3}]; P(t_s) = x_{α₀}(t_s); ρ_{α₀}(t_a) = ε.
(c) On I_η (⊂ [θ_L, θ_R] ⊂ [1/2, π/2]), with x = |θ − α₀|:
 r_min ≤ r ≤ r_max; Λ_min ≤ Λ ≤ Λ_max; rΛ_min ≤ rΛ ≤ rΛ_max; A_min ≤ A ≤ A_max; 1 ≤ w₁ ≤ W_w; |k₁ − 1| ≤ κ_w;
 b_lo x² ≤ b ≤ b_hi x² ≤ b̄; τ_b ≤ β₂x²; C_lo x^{2−2v} ≤ C ≤ C_hi x^{2−2v}; a_min ≤ a ≤ a_max; |∂_θ log C| ≤ L_C/x;
 for θ < α₀: ∂_θ log C ≤ −(L_lo − ηA_max/r_min)/x < 0 (so C is strictly increasing in x on the tail side);
 the quantity 𝔖 of Lemma 3 at t₁ (frame of run 2) satisfies |𝔖| ≤ S₁v;
 τ_b^v ∂_θC = 2τ_bA/(1+τ_b²) + r∂_θb·(cos b − v), hence 0 < τ_b^v∂_θC ≤ x(rΛ_max/2 + A_max b_hi(1+e_τ)η) for θ > α₀ and
 |τ_b^v∂_θC| ≤ r|∂_θb| ≤ rΛ_max x/2 for θ < α₀.

*Proof.* (a) P8a Lemma 5(a) (exact, all v).
(b) cos α₀ = v + 1/t₁ = v + (1−v)/(2−v), and 0 ≤ v + (1−v)/(2−v) − 1/2 = v(3 − 2v)/(2(2−v)) ≤ v ≤ v̄; so α₀ ∈ [α̲, π/3].
|S_{α₀}(t₁) − P(t₁) − (e^{iπ/3} − 2)| ≤ vt₁ + |e^{iα₀} − e^{iπ/3}| + |t₁ − 2| ≤ vt₁ + Δ_a + μ ≤ e_ρ. t₂ = t₁ + ρ₀/(1−v) ≤ T₂, and ρ₀ ≥ √3 − e_ρ > ε (SC1), so t_a > t₁. The rest is the
exact part of P8a Lemma 5(b): t₂ − t_s = ∫₀^ε v(1−f)/((1−v)(1−vf))dσ ∈ (0, vε/(3(1−v)²)] (f(σ) = (σ/ε)(2 − σ/ε) < 1 on [0,ε)),
t_s − t_a = ε∫₀¹dσ/(1 − vσ(2−σ)) ≤ ε/(1−v), P(t_s) = x_{α₀}(t_s) ([D, Claim D3(a)]), ρ_{α₀}(t_a) = ε (the candidate α₀ stays on the ray, b = 0).
P(t₁) = 2 + μ; P(t_s) = x_{α₀}(t_s) is within vt_s + Δ_a ≤ d_s + Δ_a of e^{iπ/3}; P is a segment, so it lies within d_P of 𝒮₀ (convexity).
(c) I_η ⊂ [θ_L, θ_R] ⊂ [1/2, π/2] by (b) and (SC3), (SC4); window labels are ≥ θ_L > α_s, so Q1(a),(b) apply with ρ = sin θ_L = ρ_w
(sin increasing on [θ_L, π/2]): w₁, k₁, and the tangent ∂_θS_θ(t₁) = w₁e^{iψ₁} with |ψ₁ − (θ + π/2)| ≤ ω_w.
*r.* p := S_θ(t₁) − P(t₁) = e^{iθ} − 2 + d, |d| ≤ vt₁ + μ ≤ d₁; R₀ is increasing on (0,π), so r ∈ [R_L − d₁, R_R + d₁].
*Λ.* sin β₁/ρ₁ = Im p/r² with Im p = Im S_θ(t₁) ∈ [sin θ, sin θ + vt₁] (y non-decreasing in run 1; speed ≤ v), so
Λ = 2t₁(Im p/sin θ) sin((θ+α₀)/2)/r², 1 ≤ Im p/sin θ ≤ ι, t₁ ∈ [2, t̄₁]; (θ+α₀)/2 ∈ [α₀ − η/2, α₀ + η/2] ⊂ [α̲ − η/2, π/3 + η/2] ⊂ (0, π/2]
(SC5), where sin is increasing. This gives Λ_min ≤ Λ ≤ Λ_max.
*rΛ.* rΛ = 2t₁(Im p/sin θ)q̃(θ)·(R₀/r), q̃(θ) := sin((θ+α₀)/2)/R₀(θ). d log q̃/dθ = cot((θ+α₀)/2)/2 − s(θ) with s = R₀′/R₀ = 2 sin θ/(5 − 4cos θ);
s′ has the sign of 5cos θ − 4 < 0 on the window (SC6), so s ≥ s(θ_R) there, and cot((θ+α₀)/2)/2 ≤ cot(α̲ − η/2)/2; by (SC7) q̃ is
decreasing on I_η. Hence q̃(θ) ∈ [q̃(α₀+η), q̃(α₀−η)] ⊂ [sin(α̲ + η/2)/R_R, sin(π/3 − η/2)/R_L] = [q_min, q_max] (R₀(α₀+η) ≤ R_R,
R₀(α₀−η) ≥ R_L). And R₀/r ∈ [1/(1 + d₁/R_L), 1/(1 − d₁/R_L)] (SC8). So rΛ ∈ [rΛ_min, rΛ_max].
*A.* A = ∂_θS_θ(t₁)·r̂ = w₁cos∠(e^{iψ₁}, r̂). With p₀ := e^{iθ} − 2: ie^{iθ}·p₀ = 2 sin θ > 0 and ie^{iθ} × p₀ = 2cos θ − 1, so
∠(ie^{iθ}, p₀) = arcsin(|2cos θ − 1|/R₀(θ)) ≤ arcsin m₀ (|2cos θ − 1| is maximal at an end of [θ_L, θ_R], R₀ ≥ R_L); ∠(p₀, p) ≤ arcsin(|d|/|p₀|) ≤ ω_p.
So ∠(e^{iψ₁}, r̂) ≤ ang < π/2 (SC9) and A ∈ [cos(ang), W_w].
*b.* b(α₀ ± x) = ∫₀^xΛ(α₀ ± x′) sin(x′/2)dx′ ∈ [Λ_min, Λ_max]·4sin²(x/4), and (x²/4)(1 − x²/48) ≤ 4sin²(x/4) ≤ x²/4. τ_b = tan(b/2) ≤ (b/2)(1+e_τ)
(tan s/s increasing on (0, π/2), b ≤ b̄ < π/2 (SC10)), so τ_b ≤ β₂x²; τ_b ≥ b/2.
*C.* C = rg(b) = 2rτ_b^{1−v}/(1+τ_b²). Upper: C ≤ 2r_max(β₂x²)^{1−v} ≤ 2r_maxβ₂^{1−v̄}x^{2−2v} (β₂ < 1, (SC11)). Lower:
C ≥ 2r_min(b_lo x²/2)^{1−v}/(1 + tan²(b̄/2)) ≥ C_lo x^{2−2v} ((b_lo/2)^{−v} ≥ 1 by (SC12)).
*a.* a = ∂_θ[r(cos b + v)] = A(cos b + v) − r sin b ∂_θb, and |r sin b ∂_θb| ≤ b̄·rΛ_max·x/2 ≤ aux (sin b ≤ b̄, |∂_θb| ≤ Λ sin(x/2) ≤ Λx/2, x ≤ η).
So a ∈ [A_min cos b̄ − aux, A_max(1+v) + aux].
*∂_θ log C* = A/r + (g′/g)(b)∂_θb = A/r + (cos b − v)∂_θb/sin b. Write |∂_θb|/b = Λ(θ) sin(x/2)/∫₀^xΛ sin(x′/2)dx′ ∈
[Λ_min/Λ_max, Λ_max/Λ_min]·cot(x/4)/2 (since sin(x/2)/(4sin²(x/4)) = cot(x/4)/2). For 0 < y ≤ 1: 1/y − y/2 ≤ cot y ≤ 1/y (the function
y cos y − sin y + (y²/2) sin y vanishes at 0 and has derivative (y²/2)cos y ≥ 0), so (2/x)(1 − x²/32) ≤ cot(x/4)/2 ≤ 2/x. Moreover
(cos b − v)/sin b·b ∈ [cos b − v, b cot b] ⊂ [cos b̄ − v, 1]. Hence (cos b − v)|∂_θb|/sin b ∈ [L_lo/x, 2Λ_max/(Λ_min x)], and 0 < A/r ≤ A_max/r_min ≤
(ηA_max/r_min)/x. For θ > α₀ (∂_θb > 0) both terms are positive and ∂_θ log C ≤ L_C/x. For θ < α₀: ∂_θ log C ≤ A_max/r_min − L_lo/x ≤
−(L_lo − ηA_max/r_min)/x < 0 (SC15) and ≥ −2Λ_max/(Λ_min x) ≥ −L_C/x.
*τ_b^v∂_θC.* ∂_θC = g(b)A + rg′(b)∂_θb and g′ = g(cos b − v)/sin b, τ_b^vg(b) = 2τ_b/(1+τ_b²), τ_b^vg(b)/sin b = 1. On the forward side
both terms are positive: 2τ_bA/(1+τ_b²) ≤ 2β₂x²A_max = A_max b_hi(1+e_τ)x², r∂_θb ≤ rΛ_max x/2. On the tail side ∂_θC < 0 (shown above), so
|τ_b^v∂_θC| = r|∂_θb|(cos b − v) − 2τ_bA/(1+τ_b²) ≤ r|∂_θb| ≤ rΛ_max x/2.
*𝔖 at t₁.* In the frame of run 2 the tangent is (A + ir∂_θb)e^{ib}, so |sin φ| = r|∂_θb|/w₁ ≤ rΛ_max x/2; with ρ = r, w₁ ≥ 1,
|𝔖| ≤ (v|sin φ|/((1−v²)r))[r a_max|∂_θ log C| + 1 + v] ≤ (v rΛ_max x/(2(1−v²)r_min))[r_max a_max L_C/x + 1 + v] ≤ S₁v (x ≤ η). ∎

---------------------------------------------------------------------------------------------------------------------

## §3. Run 2: the forward arc (replaces P8a Lemma 6)

In run 2, h(t) = (1+v)(r − ρ₀) − r(1 − cos b) + (1−v²)δ(t) (P8a §4; exact).

**Lemma Q3 (θ = α₀ + x, 0 < x ≤ η; true flow).** For every t ∈ [t₁, t₂):
(a) h(t) ≥ h_f x + (1−v²)δ(t) ≥ h_f(x + δ(t)) > 0, ρ ≥ h/(1+v) ≥ ρ_c(x + δ(t)); in particular ρ > 0 and 0 < β < π;
(b) τ ≤ τ_b((1+v)r/h)^{1+μ}, (τ/τ_b)^v ≤ (Q/(x+δ))^μ, and 0 < y ≤ y_f x²(Q/(x+δ))^μ;
(c) 0 < Y_r := y∂_θ log C/a ≤ Y₁x(Q/(x+δ))^μ ≤ Ȳ, |ψ| ≤ |tan ψ| ≤ θ_f x(Q/(x+δ))^μ ≤ θ_f Q^{μ̄}x^{1−μ}, 1 ≤ w ≤ W_f;
(d) for 0 < x ≤ η, at t = t_s: τ ≤ τ_f x^{1−μ} ≤ τ̄_f and ρ(t) ≥ ρ(t_s) ≥ ρ_c x for all t ∈ [t₁, t_s]; ρ ≥ ε on [0,t₁]. Hence every
label with ρ_c x > ε — in particular every x ≥ x₁ε and a neighbourhood of x = x₁ε (ρ_c x₁ > 1 is strict) — has ρ > ε on [t₁,t_s]: it is true up
to t_s, virtual = true there, and the front is C^∞ near it. For x₁ε ≤ x ≤ η moreover ρ(t_s) ≤ ρ_u x and |k| ≤ K_f x^{−μ};
(e) the true front at every t ∈ [t₁,t₂) is tangent to û at the candidate α₀.

*Proof.* (a) r − ρ₀ = ∫_{α₀}^θA ≥ A_min x; r(1 − cos b) ≤ r_max b²/2 ≤ r_max b_hi²x⁴/2 ≤ (r_max b_hi²η³/2)x. So h ≥ (1+v)A_min x − (r_max b_hi²η³/2)x
+ (1−v²)δ ≥ h_f x + (1−v²)δ ≥ h_f(x+δ) (h_f ≤ 1 − v̄² ≤ 1 − v², (SC16)). h = ρ(cos β + v) ≤ (1+v)ρ. ρ > 0 and Lemma 1 give 0 < β < π.
(b) Lemma 1(d): τ ≤ ((1+v)C/(2h))^{1/(1−v)} and C ≤ 2rτ_b^{1−v}: τ ≤ ((1+v)rτ_b^{1−v}/h)^{1+μ} = τ_b((1+v)r/h)^{1+μ}. Raising to the power v
(v(1+μ) = μ): (τ/τ_b)^v ≤ ((1+v)r/h)^μ ≤ (Q/(x+δ))^μ by (a). y = Cτ^v ≤ 2rτ_b^{1−v}τ_b^v((1+v)r/h)^μ = 2rτ_b((1+v)r/h)^μ ≤ y_f x²(Q/(x+δ))^μ.
(c) By Lemma 2, Y_r = cτ^v/a = (τ/τ_b)^v τ_b^v∂_θC/a, and Lemma Q2(c): 0 < Y_r ≤ (Q/(x+δ))^μ x(rΛ_max/2 + A_max b_hi(1+e_τ)η)/a_min =
Y₁x(Q/(x+δ))^μ ≤ Y₁Q^μx^{1−μ} ≤ Y₁Q^{μ̄}η^{1−μ̄} = Ȳ (Q ≥ 1 (SC18), x ≤ η < 1). In rem:T1-tilt (exact), tan ψ = N_ψ/D_ψ with
N_ψ = (1 + v cos β)Y_r − v sin β ∈ [−v sin β, (1+v)Y_r] and D_ψ = 1 − v cos β − v sin β Y_r ≥ 1 − v − vȲ > 0 (SC19); the real part of
x_θ is aD_ψ/(1−v²) > 0, so |ψ| < π/2 and |ψ| ≤ |tan ψ|. sin β = y/ρ ≤ y_f x²(Q/(x+δ))^μ/(ρ_c(x+δ)) ≤ (y_f/ρ_c)x(Q/(x+δ))^μ. Hence
|tan ψ| ≤ max((1+v)Y₁, v y_f/ρ_c)x(Q/(x+δ))^μ/(1 − v − vȲ) ≤ θ_f x(Q/(x+δ))^μ. w = a|D_ψ + iN_ψ|/(1−v²) ≤ W_f (|D_ψ| ≤ 1 + v + vȲ,
|N_ψ| ≤ (1+v)Ȳ + v); w ≥ 1 by [B].
(d) By (b) with h ≥ h_f x: τ(t_s) ≤ β₂x²(Q/x)^{1+μ} ≤ τ_f x^{1−μ} ≤ τ̄_f, so cos β = (1−τ²)/(1+τ²) ≥ 1 − 2τ̄_f² > v (SC20). τ is increasing
in time (Lemma 1(b)), so cos β > v on [t₁, t_s] and ρ is decreasing there (Lemma 1(c)): ρ(t) ≥ ρ(t_s) ≥ ρ_c(x + δ) ≥ ρ_c x by (a); for x ≥ x₁ε
this is > ε (SC17). In run 1, ρ ≥ ε since θ ≥ θ_L > α_s (Q1(a)). Now let x ≥ x₁ε; then δ(t_s) ≤ vε/(3(1−v)²) ≤ δ₁x (Q2(b)). Upper bound: ρ = h/(cos β + v) ≤
h/(1 − 2τ̄_f²), h ≤ (1+v)(r − ρ₀) + (1−v²)δ ≤ (1+v)A_max x + δ₁x; so ρ ≤ ρ_u x.
*Curvature.* Lemma 3 (two-time relation, t′ = t₁, t″ = t_s; the label is true on [t₁,t_s] with 0 < β < π):
k″ = (τ″/τ_b)^v(w′/w″)³(k₁ + 𝔖′) − 𝔖″, w′/w″ ≤ 1, (τ″/τ_b)^v ≤ (Q/x)^μ ≤ Q^{μ̄}x^{−μ}, |k₁| ≤ 1 + κ_w, |𝔖′| ≤ S₁v. For 𝔖″:
|sin φ| = |sin(β − ψ)| ≤ sin β + |ψ| ≤ 2τ + θ_fQ^{μ}x^{1−μ} ≤ (2τ_f + θ_fQ^{μ̄})x^{1−μ}, ρ ≥ ρ_c x, ρa|∂_θ log C|/w² ≤ ρ_u x a_max L_C/x:
|𝔖″| ≤ (v|sin φ|/((1−v²)ρ))(ρ_u a_max L_C + 1 + v) ≤ S₂v x^{−μ}. So |k| ≤ Q^{μ̄}x^{−μ}(1 + κ_w + S₁v) + S₂v x^{−μ} = K_f x^{−μ} (x^{−μ} ≥ 1).
(e) P8a Lemma 6(e) (exact): let x → 0 in (c) with δ(t) > 0 fixed. ∎

---------------------------------------------------------------------------------------------------------------------

## §4. The virtual labels next to X₀ (replaces P8a Lemma 8)

**Lemma Q4.** At t_s, for every θ = α₀ + x, 0 ≤ x ≤ η, the virtual front has tangent e^{iψ} relative to û with
**|ψ(θ,t_s)| ≤ θ_v x^{1−μ}**, and 1 ≤ w ≤ W_v. ψ(α₀, t_s) = 0. For x ≥ x₁ε the virtual front is the true one.

*Proof.* For x₁ε ≤ x ≤ η: Lemma Q3(c),(d) at t_s (θ_fQ^{μ̄} ≤ θ_v, W_f ≤ W_v). Let 0 < x < x₁ε (≤ η by (SC40)). On [0,t₁] the label is true with
ρ ≥ ε (Q1(a)); on [t₁, t_a]: h_θ(t) − h_{α₀}(t) = (1+v)(r − ρ₀) − r(1 − cos b) ≥ h_f x > 0 (proof of Q3(a)), and h_{α₀}(t) = (1+v)ρ_{α₀}(t)
≥ (1+v)ε (α₀ is on the ray), so (1+v)ρ_θ ≥ h_θ > (1+v)ε. Hence virtual = true on [0, t_a] ([B, Lemma VC(c)]), and by Q3(b),(c) at t_a
(δ(t_a) = ε/(1−v) ≥ ε): |ψ(t_a)| ≤ θ_f x(Q/(x+ε))^μ, 0 ≤ y(t_a) ≤ y_f x²(Q/(x+ε))^μ, w(t_a) ≤ W_f.
On [t_a, t_s] (length I ≤ ε/(1−v), so vI/ε ≤ μ) the virtual field acts: in the frame of run 2, r′ = vF(r) − û, so y′ = v(f(ρ)/ρ)y with
0 ≤ f/ρ ≤ 2/ε, hence 0 ≤ y(t) ≤ y(t_a)e^{2μ}. By [D, Lemma D0(a)], |ψ_t| ≤ v|p|/m(ρ)², p = y cos ψ − z sin ψ, |p| ≤ y + ρ|ψ|, ρ/m² ≤ 1/ε,
1/m² ≤ 1/ε²: |ψ|′ ≤ (v/ε)|ψ| + vy/ε² a.e. Gronwall:
|ψ(t_s)| ≤ e^{μ}[|ψ(t_a)| + (vI/ε²)e^{2μ}y(t_a)] ≤ e^{μ}[θ_f + μe^{2μ}y_f(x/ε)](Q/x)^μ x ≤ e^{μ̄}Q^{μ̄}(θ_f + μ̄e^{2μ̄}y_f x₁)x^{1−μ} = θ_v x^{1−μ}
(x/ε < x₁). [B]: w(t_s) ≤ w(t_a)e^{va*I} ≤ W_f e^{2μ̄} = W_v; w ≥ 1. For x = 0: ψ(t_a) = 0 = y(t_a) and the same inequality gives ψ ≡ 0. ∎

---------------------------------------------------------------------------------------------------------------------

## §5. Run 2: the tail, the end E_Y, the labels seen (replaces P8a Lemma 7)

**Lemma Q5.** (a) There is a unique b_e = α₀ − x_e, x_e ∈ (0, η), with C(b_e) = εg_max, and
 **xe_lo ε^{1/(2−2v)} ≤ x_e ≤ xe_hi ε^{1/(2−2v)} ≤ x̄_e**; also x_e ≥ xe_lo ε ≥ ε/2.
(b) Every true candidate θ ∈ [b_e, α₀] is seen by t_s.
(c) *Tail at t_s, θ = α₀ − x, x_e ≤ x ≤ η* (true candidates, never caught; frame of run 2 at t_s):
 h < 0, h_t x ≤ |h| ≤ h_T x; τ ≥ τ_t > 1; **−z_T x ≤ z ≤ −h_t x**; 0 < y ≤ y_T x^{2−μ_T}; ρ ≤ ρ_T x; (τ/τ_b)^v ≤ T_t x^{−μ_T};
 **−θ_t x^{1−μ_T} ≤ ψ < 0**; 1 ≤ w ≤ W_t; **|k| ≤ K_t x^{−μ_T}**.
(d) E_Y := x_{b_e}(t_s) = X₀ + z_Eû + iy_Eû with −z_T x_e ≤ z_E ≤ −h_t x_e and 0 < y_E ≤ y_T x_e^{2−μ_T}.

*Proof.* (a) By Q2(c), x ↦ C(α₀ − x) is continuous and strictly increasing on (0, η], C(α₀ − x) ≤ C_hi x^{2−2v} → 0 (x → 0), and
C(α₀ − η) ≥ C_loη² > ε̄g_b ≥ εg_max (SC22). So b_e exists and is unique, and C_lo x_e^{2−2v} ≤ εg_max ≤ C_hi x_e^{2−2v}. Hence
x_e ≥ (ε/C_hi)^{1/(2−2v)} ≥ C_hi^{−1/2}ε^{1/(2−2v)} (C_hi < 1 (SC21), g_max ≥ 1) and x_e ≤ (g_b/C_lo)^{1/(2−2v)}ε^{1/(2−2v)} ≤ xe_hi ε^{1/(2−2v)}
(g_b/C_lo > 1 (SC23); the exponent increases with v). ε^{1/(2−2v)} ≤ ε^{1/2} ≤ ε̄^{1/2} and ≥ ε; xe_lo ≥ 1/2 (SC28); x̄_e < η (SC24).
(c) *h.* ρ₀ − r = ∫_θ^{α₀}A ∈ [A_min x, A_max x]; 0 ≤ r(1 − cos b) ≤ r_max b_hi²η³x/2; 0 ≤ (1−v²)δ(t_s) ≤ (1+v)vε/(3(1−v)) ≤ δ₂x (ε ≤ x/xe_lo by (a)).
So h = −(1+v)(ρ₀ − r) − r(1 − cos b) + (1−v²)δ(t_s) ≤ −(A_min − δ₂)x = −h_t x < 0 (SC25), and |h| ≤ (1+v)A_max x + r_max b_hi²η³x/2 = h_T x.
The candidate is never caught: ρ ≥ C/g_max > 0 in run 2 (Lemma 1(c)), and in run 1 by Q1(a).
*τ.* Lemma 1(d) (h < 0): τ^{1+v} ≥ 2|h|/((1−v)C) ≥ 2h_t x/(C_hi x^{2−2v}) ≥ (2h_t/C_hi)η^{−(1−2v)} ≥ m_τ > 1 (SC26), so τ ≥ m_τ^{1/(1+v)} ≥ τ_t > 1. Then
(1+v)Cτ^{v−1}/(2|h|) ≤ (1+v)τ_t^{v̄−1}/m_τ ≤ e_t (τ ≥ τ_t ≥ 1), and Lemma 1(d) gives 2|h|/C ≤ (1−v)τ^{1+v} ≤ (1+e_t)2|h|/C.
*y.* y = Cτ^v = C(τ^{1+v})^{v/(1+v)} ≤ C^{1/(1+v)}(2(1+e_t)|h|/(1−v))^{v/(1+v)} ≤ C_hi^{1/(1+v)}x^{(2−2v)/(1+v)}(y_c x)^{v/(1+v)} ≤ y_T x^{(2−v)/(1+v)},
and (2−v)/(1+v) = 2 − μ_T. (C_hi^{1/(1+v)} ≤ C_hi^{1/(1+v̄)} as C_hi < 1; y_c^{v/(1+v)} ≤ max(1,y_c)^{v̄}.)
*τ/τ_b.* τ^{1+v} ≤ (1+e_t)2|h|/((1−v)C) ≤ y_c x/(C_lo x^{2−2v}) and τ_b ≥ b/2 ≥ b_lo x²/2, so
τ/τ_b ≤ (y_c/C_lo)^{1/(1+v)}x^{−(1−2v)/(1+v)}·2/(b_lo x²) ≤ max(1, y_c/C_lo)(2/b_lo)x^{−3/(1+v)}, and (τ/τ_b)^v ≤ T_t x^{−μ_T}.
*ψ.* Y_r = (τ/τ_b)^vτ_b^v∂_θC/a < 0 with |Y_r| ≤ T_t x^{−μ_T}·rΛ_max x/(2a_min) = Y₂x^{1−μ_T} ≤ Ȳ₂ (Q2(c)). cos β < −v (h < 0), so in
rem:T1-tilt: N_ψ = (1 + v cos β)Y_r − v sin β < 0 with |N_ψ| ≤ |Y_r| + v sin β, D_ψ = 1 − v cos β − v sin β Y_r ≥ 1, and Re x_θ > 0;
so ψ ∈ (−π/2, 0) and |ψ| ≤ |tan ψ| ≤ |Y_r| + v sin β. ρ ≥ |h| (|cos β + v| ≤ 1 − v ≤ 1) ≥ h_t x and sin β = y/ρ ≤ y_T x^{1−μ_T}/h_t:
|ψ| ≤ (Y₂ + v y_T/h_t)x^{1−μ_T} = θ_t x^{1−μ_T}.
*z, ρ.* z = h − vρ < 0, |z| ≥ |h| ≥ h_t x; ρ ≤ |z| + y gives (1−v)|z| ≤ |h| + vy ≤ (h_T + v y_Tη^{1−μ_T})x, so |z| ≤ z_T x;
ρ ≤ |z|(1 + (y/|z|)²)^{1/2} ≤ ρ_T x (y/|z| ≤ y_T x^{1−μ_T}/h_t ≤ y_Tη^{1−μ_T}/h_t).
*w.* w = a|D_ψ + iN_ψ|/(1−v²) ≤ W_t (|D_ψ| ≤ 1 + v + vȲ₂, |N_ψ| ≤ (1+v)Ȳ₂ + v); w ≥ 1.
*k.* Lemma 3 (t′ = t₁, t″ = t_s): |k| ≤ (τ/τ_b)^v(1 + κ_w + S₁v) + |𝔖″|, and |𝔖″| ≤ (v|sin φ|/((1−v²)ρ))(ρa|∂_θ log C| + 1 + v) with
|sin φ| ≤ sin β + |ψ| ≤ (y_T/h_t + θ_t)x^{1−μ_T}, ρ ≥ h_t x, ρa|∂_θ log C| ≤ ρ_T x·a_max L_C/x: |𝔖″| ≤ S₃v x^{−μ_T}. So |k| ≤ K_t x^{−μ_T}.
(d) (c) at x = x_e (E_Y = x_{b_e}(t_s) = S_{b_e}(t_s): the label b_e has ρ ≥ C/g_max = ε throughout run 2 and ≥ ε in run 1, so virtual = true).
(b) *Seen.* Label α₀: ρ_{α₀}(t_a) = ε. *Labels x ∈ [x₂vε, x_e]:* C(α₀ − x) ≤ C(b_e) = εg_max (monotonicity) and
h(t_s) ≤ −(1+v)A_min x + (1+v)vε/(3(1−v)) ≤ 0 (x ≥ x₂vε), so cos β(t_s) ≤ −v < v, while at t₁, cos β = cos b ≥ cos b̄ > v (SC14): by
Lemma 1(b),(c) the minimum of ρ, C/g_max ≤ ε, is attained during (t₁, t_s): seen. *Labels x ∈ (0, ε/2]* (this covers (0, x₂vε) by (SC27)):
at t_a, δ(t_a) = ε/(1−v) and h(t_a) = (1+v)ε − (1+v)(ρ₀ − r) − r(1 − cos b) ∈ [h_aε, (1+v)(ε − A_min x)] (lower bound: (1+v)(ε − A_max x) ≥ (1 − A_max/2)ε
[v2, C4: this uses x ≤ ε/2 and A_max ≤ 2; indeed A_max = W_w = e^{v̄t̄₁/sin θ_L} ≤ e^{0.2112/sin ½} < 1.6 by (SC3), (SC35)]
and r(1 − cos b) ≤ r_max b_hi²x⁴/2 ≤ r_max b_hi²ε̄³ε/32; h_a > 0 (SC29)). By Lemma 1(d) as in Q3(b): τ(t_a) ≤ τ_b((1+v)r/h)^{1+μ} ≤ β₂x²(Q_a/ε)^{1+μ}
≤ β₂Q_a^{1+μ}ε^{1−μ}/4 ≤ τ_a, and also τ² ≤ τ_a·β₂Q_a^{1+μ}x²ε^{−1−μ}. Then cos β + v ≥ 1 + v − 2τ² > 0 (SC30) and
ρ(t_a) = h/(cos β + v) ≤ (1+v)(ε − A_min x)/(1 + v − 2τ²) < ε ⇔ 2τ²ε < (1+v)A_min x ⇐ 2τ²ε ≤ 2τ_aβ₂Q_a^{1+μ}x²ε^{−μ} ≤ τ_aβ₂Q_a^{1+μ}ε^{1−μ}x ≤ 4τ_a²x < A_min x
(x ≤ ε/2; (SC31)). So ρ(t_a) < ε: seen. (x_e ≥ ε/2 and x₂vε ≤ ε/2 make the three ranges cover [b_e, α₀].) ∎

---------------------------------------------------------------------------------------------------------------------

## §6. Bulk and hole (replaces P8a Lemmas 9, 11(a)–(c))

**Lemma Q6.** (a) For every θ ∈ (0, 2π) \ {α₀} the true trajectory S_θ exists on [0, t_s] and never meets Harry; for θ = 2π (≡ 0) it is
caught at t₀ = 1/(1−v) < t₁ (no trajectory afterwards).
(b) Let θ ∈ (0, 2π), θ ∉ I_η, χ := min(θ, 2π − θ). In the frame of run 2: b(θ) ∈ [b_l, π/3 + 2e_β], y(θ,t) ≥ y_b for t ∈ [t₁, t_s], and at t_s
the true front near θ is C^∞ with **|k| ≤ K_b** and **w ≤ W_bW_all(2/χ)^{2v}**.
(c) *(hole)* Z₁ := lim_{α→0±}S_α(t₁) exists, equals P(t₁) − (1+v); Γ₁ := {S_α(t₁): 0 < |α| ≤ 0.005} ∪ {Z₁} is a C¹ arc of finite length with
tangent i at Z₁. Let Φ be the flow map from t₁ to t_s of the true field x ↦ v(x − P(t))/|x − P(t)|. On B(1, r_B), Φ is a C^∞ diffeomorphism
onto its image, Γ₁ ⊂ B(1, r_B), Z_s := Φ(Z₁) = lim_{α→0±}S_α(t_s), and Γ_s := Φ(Γ₁) is a C¹ arc through Z_s that is the true front for α ≠ 0
and whose unit tangent is K_b-Lipschitz in arclength.

*Proof.* (a) P8a Lemma 11(a) (exact): in run 1, C = g(α) > 0 for α ∉ {0, π}, so ρ ≥ C/g_max > 0; α = π stays on the axis behind Harry
(ρ ≥ 1); in run 2, b ∈ (0, π) for θ ≠ α₀ (Q2(a); on the lower half b ∈ (π − β*, 2π − 2β*] ⊂ (0,π) because β* > π/2, see (b)), so C = rg(b) > 0.
α = 0: on the axis ahead of Harry, ρ′ = −(1−v), ρ(0) = 1.
(b) *b.* β* = arg(S_{α₀}(t₁) − P(t₁)) and arg(e^{iπ/3} − 2) = 5π/6, |S_{α₀}(t₁) − P(t₁) − (e^{iπ/3} − 2)| ≤ e_ρ, |e^{iπ/3} − 2| = √3: so
|β* − 5π/6| ≤ e_β and π − β* ∈ [π/6 − e_β, π/6 + e_β]. Upper half, θ ∉ I_η: β₁ is monotone on each side of α₀ (Q2(a)), so b = β₁ − β* ≥
min(b(α₀ − η), b(α₀ + η)) ≥ b_lo η² = b_l, and b < π − β* (β₁ < π); θ = π: b = π − β*; lower half: b ∈ (π − β*, 2π − 2β*]. So
b ∈ [b_l, π/3 + 2e_β] ((SC32): π − β* ≥ b_l), and by (SC33) sin b ≥ sin b_l. *y.* r = ρ₁ ≥ 1 + v ≥ 1 (Q1(d)), so y(t₁) = r sin b ≥ y_b; y = Cτ^v is
non-decreasing in run 2 (τ increasing), so y ≥ y_b on [t₁, t_s]; in particular ρ ≥ y_b > 0 and 0 < β < π throughout run 2.
*τ.* τ(t₁) = τ_b ≥ tan(b_l/2); at t_s, τ = tan(β/2) = (ρ − z)/y ≤ 2ρ/y_b and ρ(t_s) ≤ r + (1+v)(t_s − t₁) ≤ (|e^{iθ} − 2| + d₁) + (1+v)(√3 + e_ρ)/(1−v) ≤ H_b.
So 1 ≤ τ(t_s)/τ_b ≤ T_b and (τ(t_s)/τ_b)^v ≤ T_b^{v̄} (T_b ≥ 1 (SC34)).
*𝔖.* With Ξ = a + iτ^vc (Lemma 2), ∂_θ log C = c/C = ImΞ/y (C = yτ^{−v}), and |ReΞ·ImΞ| ≤ |Ξ|²/2 ≤ (1+v)²w²/2, so
|ρa∂_θ log C|/w² ≤ (1+v)²ρ/(2y), and |𝔖| ≤ (v|sin φ|/((1−v²)ρ))[(1+v)²ρ/(2y) + 1 + v] = (v|sin φ|/(1−v))[(1+v)/(2y) + 1/ρ] ≤ v(3+v)/(2(1−v)y) ≤ S_bv
(ρ ≥ y ≥ y_b), at t₁ and at t_s.
*k, w.* Lemma 3 (t′ = t₁, t″ = t_s): |k(t_s)| ≤ (τ″/τ_b)^v(|k₁| + |𝔖′|) + |𝔖″| ≤ T_b^{v̄}(k_all + S_bv̄) + S_bv̄ = K_b (Q1(d)). Lemma 2: Ξ″ = a + iτ″^vc,
|Ξ″| ≤ (τ″/τ_b)^v|Ξ′| (τ″ ≥ τ_b), so w″ ≤ |Ξ″|/(1−v) ≤ ((1+v)/(1−v))T_b^{v̄}w₁ ≤ W_bW_all(2/χ)^{2v}. The front is C^∞ near θ since ρ > 0 on [0,t_s].
(c) *Γ₁.* By Q1(c), for 0 < α ≤ 1/2: y(α,t₁) ≤ 2E₁tan(α/2)^{(1−v)/(1+v)} → 0; z = h₁ − vρ₁ < 0 and ρ₁ ≤ |z| + y give
(1−v)|z| ≤ |h₁| ≤ (1−v)|z| + vy, |h₁| = (1−v²) + (1 − cos α), so ||z| − (1+v)| ≤ (1 − cos α + vy)/(1−v) → 0: S_α(t₁) → P(t₁) − (1+v), and by the
mirror symmetry the same from below. The tangent at α ∈ (0, 1/2] is e^{i(π/2+δ)} with 0 ≤ δ ≤ arctan(d_arm y) → 0, at the mirror label
e^{i(π/2−δ)}: both → i. Length: w₁ ≤ W_arm(2/|α|)^{2v} is integrable (2v < 1). Hence the arclength parametrisation of Γ₁ is continuous,
C^∞ off Z₁ with unit speed, and its derivative extends continuously (by i) to Z₁: Γ₁ is C¹ (a continuous map, differentiable off one point,
whose derivative extends continuously, is C¹). *Φ.* For X(t₁) ∈ B(1, r_B) and t ∈ [t₁, t_s]: |X(t) − 1| ≤ r_B + vT₂ (speed ≤ v), while
P(t) is within d_P of 𝒮₀ and dist(1, 𝒮₀) = 1/2 (the foot (5/4, √3/4) of the perpendicular from 1 is the midpoint of 𝒮₀); so
|X(t) − P(t)| ≥ ρ_h > 0 (SC36): the field is C^∞ with bounded derivatives along these trajectories, and Φ is a C^∞ diffeomorphism of B(1, r_B)
onto its image. |S_α(t₁) − 1| ≤ |e^{iα} − 1| + vt₁ ≤ 0.005 + v̄t̄₁ = r_B, and Z₁ is the limit, so Γ₁ ⊂ B(1, r_B) (closed ball). Γ_s = Φ(Γ₁) is
C¹ (image of a C¹ arc by a diffeomorphism), Φ(Z₁) = lim Φ(S_α(t₁)) = lim S_α(t_s), and off α = 0 it is the true front, whose curvature is
bounded by K_b (part (b): the labels 0 < |α| ≤ 0.005 are not in I_η). The tangent angle of Γ_s is continuous and has derivative bounded
by K_b off one point: it is K_b-Lipschitz. ∎

---------------------------------------------------------------------------------------------------------------------

## §7. Chords (new; replaces the use of |x_θ − e^{iθ}| ≤ 3.74·10⁻⁶ in P8a's (T2))

**Lemma Q7.** Let X_a, X_b: [0, t_s] → ℂ be two trajectories with X(0) = e^{iθ_a}, e^{iθ_b}, each solving X′ = vV(X − P) with V = F (virtual
candidate) or V = T(x) := x/|x| (true candidate, not caught on [0,t_s]). If |e^{iθ_b} − e^{iθ_a}| > 2ε, then |X_b(t) − X_a(t)| ≥
|e^{iθ_b} − e^{iθ_a}| for all t ∈ [0,t_s]. The same holds if one of them is replaced by the limit point Z_s of Lemma Q6(c) (with θ = 0).

*Proof.* F and T are monotone: T = ∇|x| with |x| convex; F = ∇Φ(|x|) with Φ′ = f ≥ 0 non-decreasing ([B]; this is the fact behind "chords of
virtual candidates are non-decreasing"). F = T outside the open disc D_ε of radius ε. Put D := X_b − X_a, p_• := X_• − P. Then
(|D|²)′ = 2v(V_b(p_b) − V_a(p_a))·(p_b − p_a). If V_a = V_b this is ≥ 0. If V_a ≠ V_b and (say) p_b ∉ D_ε, then V_b(p_b) = V_a(p_b) and again
(|D|²)′ = 2v(V_a(p_b) − V_a(p_a))·(p_b − p_a) ≥ 0; similarly if p_a ∉ D_ε. So (|D|²)′ ≥ 0 at every time at which |D| ≥ 2ε (then p_a, p_b
are not both in D_ε). Let c₀ := |D(0)| > 2ε and suppose |D(t)| < c₀ for some t; let t* := inf{t: |D(t)| < c₀}. Then |D| ≥ c₀ > 2ε on [0,t*]
and, by continuity, |D| > 2ε on [t*, t* + σ) for some σ > 0, where |D|² is non-decreasing; so |D| ≥ |D(t*)| ≥ c₀ there, contradicting the
definition of t*. The limit point: Z_s = lim S_α(t_s) and |e^{iα} − e^{iθ}| → |1 − e^{iθ}|; pass to the limit in the inequality (for |1 − e^{iθ}| > 2ε
the hypothesis holds for α small). ∎

---------------------------------------------------------------------------------------------------------------------

## §8. Theorem Q.H — (H_T) with constants as functions of (v̄, η, ε̄, x₁, λ₀, G)

**The curve x⁰** (as in P8a §9 / sec_T1 §"The curve x⁰", with 1.02ε replaced by x₁ε): for α ∈ [α₀, 2π + b_e],
Y(α) := x_α(t_s) (virtual) if α ∈ [α₀, α₀ + x₁ε]; Y(α) := S_α(t_s) (true) if α ∈ [α₀ + x₁ε, 2π + b_e], α ≠ 2π; Y(2π) := Z_s.
x⁰ := Y reparametrised by arclength u ∈ [0,U] from Y(α₀) = X₀; Θ(u) := its label;
𝒢 := {u: Θ(u) = 2π} ∪ {u: Θ(u) ∈ [α₀, α₀ + x₁ε) and the true candidate Θ(u) was within ε of Harry at some time ≤ t_s}.
𝒢 ⊂ [0,U) and 0 ∈ 𝒢, exactly as in P8a §9 (Θ(0) = α₀, ρ_{α₀}(t_a) = ε; Θ(U) = 2π + b_e).

> **Theorem Q.H.** Assume (SC1)–(SC51) [v2, C1] for (v̄, η, ε̄, x₁, λ₀, G). Then for design T with D₁ = 1, for all v ∈ (0, v̄] and ε ∈ (0, ε̄],
> hypothesis (H_T) of sec_T2 (hyp:HT) holds with
>  **v_T := v̄, ε_T := ε̄, T₂, U_max, λ₀, c_sep, γ_T := 1/4, ϑ_T, G_T := G, C_z** (formulas §0.3), **any a′ ∈ (0, 1 − μ̄_T]**,
>  **C₀ := c_N λ₀^{1−μ̄_T−a′}** (so C₀λ₀^{a′} = c_Nλ₀^{1−μ̄_T} ≤ 1),
> with n̂ := û and the curve x⁰ and set 𝒢 above (x⁰ is C¹, |∂_ux⁰| ≡ 1, 1 ≤ U ≤ U_max, t_s ≤ T₂). Moreover the sharper forms hold:
>  **(T1′)** N(a,b) ≤ c_N λ^{3/2−μ_T} ≤ c_N λ^{3/2−μ̄_T} for all pairs with ε/2 ≤ λ ≤ λ₀;
>  **(T2′)** for all pairs with λ > λ₀: c(a,b) ≥ c_sep, or c(a,b) ≥ κ₂(u_a + u′_b); hence c ≥ min(c_sep, κ₂(u_a + u′_b));
>  **(T3′)** |T(u) − n̂| ≤ θ_v u^{1−μ} ≤ θ_v u^{1−μ̄} for u ≤ G;
>  **(T4′)** |T(u) − n̂| ≤ θ_t(x_e + u′)^{1−μ_T} ≤ c_T4 (u′ + z₀)^{1−μ̄_T} for u′ ≤ G;
>  **(T5′)** h_t xe_lo ε^{1/(2−2v)} ≤ z₀ ≤ z_T xe_hi ε^{1/(2−2v)} ≤ z_T xe_hi ε^{1/2}, and |y₀| ≤ y_T x_e^{2−μ_T} ≤ c_y z₀^{2−μ_T} ≤ c_y (z₀ + ε)^{2−μ̄_T}.

*Proof.* t_s ≤ t₂ ≤ T₂ (Q2(b)); T₂ ≥ 1. Ranges required by hyp:HT: v̄, ε̄ ∈ (0,1); U_max ≥ U ≥ 1; a′ ∈ (0,1]; C₀, C_z > 0; λ₀ ∈ (0, 1/4]
(SC41); c_sep ∈ (0,1] (Δ₀ ≤ η ≤ π/3); γ_T = 1/4; ϑ_T > 0; G ∈ (0, 1] ((SC50), G ≤ η < 1).

*x⁰ is C¹, |∂_ux⁰| = 1.* Y is C¹ in the label with |∂_αY| ≥ 1 on [α₀, 2π) and (2π, 2π + b_e]: on [α₀, α₀ + x₁ε] it is the virtual front
([B, Lemma VC(a)]); on [α₀ + x₁ε, 2π + b_e] \ {2π} the true front (C^∞ by Q3(d), Q5(c), Q6(a),(b); w ≥ 1); the two coincide on a neighbourhood
of α₀ + x₁ε (Q3(d)). Near 2π, Y is the arc Γ_s (Q6(c)). So the arclength parametrisation is C¹ with unit speed.
*Length bounds.* w ≤ W_v on the forward window [α₀, α₀ + η] (Q4), w ≤ W_t on the tail [2π + α₀ − η, 2π + b_e] (Q5(c)), w ≤ W_bW_all(2/χ)^{2v} on the
bulk (Q6(b)); hence U ≤ W_vη + W_tη + W_bW_all∫_{bulk}(2/χ)^{2v} ≤ U_max, because ∫₀^{2π}(2/χ)^{2v}dθ = 2π(2/π)^{2v}/(1−2v) ≤ 2π/(1−2v) and the window
contributes ≥ 2η ((2/χ)^{2v} ≥ 1 there, χ ≤ π/2), so the bulk integral is ≤ 2π/(1−2v) − 2η ≤ (2π − 2η)/(1−2v). U ≥ |Y(α₀ + π) − X₀| ≥
|e^{i(α₀+π)} − e^{iα₀}| − 2d_s ≥ 1 (SC38). Since (2/χ)^{2v} ≥ 1 on the window, w ≤ W_x(2/χ)^{2v} at every label ≠ 2π; for labels Θ_a < Θ_b at distance
Δ := Θ_b − Θ_a (≤ 2π), by the rearrangement inequality for the symmetric-decreasing function θ ↦ (2/χ)^{2v} of the circular distance χ to 0,
 **l(a,b) ≤ W_x·2∫₀^{Δ/2}(2/χ)^{2v}dχ = W_xΔ(4/Δ)^{2v}/(1−2v).**  (8.1)
If Δ ≤ Δ₀ then l ≤ W_xΔ₀(4/Δ₀)^{2v}/(1−2v) ≤ W_xΔ₀(8/λ₀)^{2v}/(1−2v) ≤ W_xΔ₀L̂ = λ₀ (4/Δ₀ = 4W_xL̂/λ₀ ≤ 8/λ₀ by (SC42)). Hence
 **λ > λ₀ ⟹ Δ > Δ₀.**  (8.2)

*(T0).* x⁰(0) = x_{α₀}(t_s) = P(t_s) (Q2(b)). Let u ∉ 𝒢. If Θ(u) ∉ [α₀, α₀ + x₁ε) and Θ(u) ≠ 2π: x⁰(u) = S_Θ(t_s) with S_Θ defined on [0,t_s]
(Q6(a)). If Θ(u) ∈ (α₀, α₀ + x₁ε) and the true candidate was never within ε of Harry on [0,t_s]: it has had ρ ≥ ε throughout, so it equals
the virtual one ([B, Lemma VC(c)] and its proof), S_Θ is defined on [0,t_s] and x⁰(u) = S_Θ(t_s). So every u ∉ 𝒢 is true. Directions:
[−α_s, α_s] are seen in run 1 (Q1(a)); [b_e, α₀] in run 2 (Q5(b)); θ ∈ (α₀, α₀ + x₁ε) is seen if its label is in 𝒢 (definition) and is the
direction of a true label otherwise; all other θ ∈ [0, 2π) are directions of true labels.

*Pointwise bounds on x⁰.* Forward zone: ξ := Θ − α₀ ∈ [0, η], where ξ ≤ u ≤ W_vξ (1 ≤ w ≤ W_v) and |T − n̂| = |e^{iψ} − 1| ≤ |ψ| ≤ θ_vξ^{1−μ} (Q4).
Tail: ξ := α₀ + 2π − Θ ∈ [x_e, η], where ξ − x_e ≤ u′ ≤ W_t(ξ − x_e), and −θ_tξ^{1−μ_T} ≤ ψ < 0, |k| ≤ K_tξ^{−μ_T} (Q5(c)).
On {u ≥ u₁ε}: the label is ≥ α₀ + x₁ε on the forward zone (u ≤ W_vξ), so the tangent angle of x⁰ is locally Lipschitz in u with a.e. derivative
k: |k| ≤ K_fξ^{−μ} on the forward zone (Q3(d)), |k| ≤ K_tξ^{−μ_T} on the tail, |k| ≤ K_b elsewhere (Q6(b), across the label 2π by Q6(c)).

*(T1′), (T1).* Let ε/2 ≤ λ ≤ λ₀. Three cases.
*Near X₀: u_a < max(λ, u₁ε).* If λ ≥ u₁ε, [u_a, u_b] ⊂ [0, 2λ); otherwise u_a < u₁ε ≤ 2u₁λ (ε ≤ 2λ), so [u_a,u_b] ⊂ [0, (2u₁+1)λ), and u_b < 2u₁ε ≤ η
(SC40). In both cases [u_a,u_b] is an interval of length λ in [0, (2u₁+1)λ] (u₁ ≥ 1/2 (SC48)) and inside the forward zone (u_b ≤ max(2λ₀, 2u₁ε̄) ≤ η
by (SC39), (SC40) [v2, C2], and
ξ ≤ u). By lem:T1-elem(b) with n̂ and |T − n̂| ≤ θ_vξ^{1−μ} ≤ θ_vu^{1−μ}:
 N² ≤ θ_v²∫_{u_a}^{u_b}u^{2−2μ}du ≤ θ_v²λ^{3−2μ}((2u₁+1)^{3−2μ} − (2u₁)^{3−2μ})/(3−2μ) ≤ θ_v²λ^{3−2μ}(12u₁² + 6u₁ + 1)/(3−2μ̄),
since the integrand is increasing (the right-most interval of length λ maximises the integral) and s ↦ A^s − B^s is non-decreasing for
A > B ≥ 1. So N ≤ c_nearλ^{3/2−μ}.
*Near E_Y: u′_b < λ and x_e < λ* (then u′_a = u′_b + λ < 2λ ≤ 2λ₀, the pair lies in the tail zone: ξ ≤ x_e + u′ < λ₀ + 2λ₀ ≤ η by (SC39), using also
x_e ≤ x̄_e, i.e. ξ < min(x̄_e, λ₀) + 2λ₀). There |T − n̂| ≤ θ_tξ^{1−μ_T} ≤ θ_t(x_e + u′)^{1−μ_T}, and as u runs over [u_a,u_b], s := x_e + u′ runs over an
interval of length λ inside [0, 3λ]. So N² ≤ θ_t²λ^{3−2μ_T}(3^{3−2μ_T} − 2^{3−2μ_T})/(3−2μ_T) ≤ 19θ_t²λ^{3−2μ_T}/(3−2μ̄_T), N ≤ c_tailλ^{3/2−μ_T}.
*Far: otherwise* (u_a ≥ max(λ, u₁ε), and u′_b ≥ λ or x_e ≥ λ). On [u_a,u_b]: forward-zone labels have ξ ≥ u/W_v ≥ λ/W_v, so |k| ≤ K_fW_v^{μ̄}λ^{−μ};
tail labels have ξ ≥ x_e + u′/W_t ≥ max(x_e, u′_b/W_t), so ξ ≥ λ/W_t (W_t ≥ 1) and |k| ≤ K_tW_t^{μ̄_T}λ^{−μ_T}; elsewhere |k| ≤ K_b. As λ < 1 and μ ≤ μ_T,
the tangent angle is K-Lipschitz on [u_a,u_b] with K := K_*λ^{−μ_T}, and Kλ ≤ K_*λ₀^{1−μ̄_T} ≤ π (SC47). lem:T1-elem(a): N ≤ (K/√12)λ^{3/2} = c_farλ^{3/2−μ_T}.
Hence N ≤ c_Nλ^{3/2−μ_T} in all cases (λ^{3/2−μ} ≤ λ^{3/2−μ_T}), ≤ c_Nλ^{3/2−μ̄_T}; and for a′ ≤ 1 − μ̄_T,
N ≤ c_Nλ^{1−μ̄_T−a′}λ^{1/2+a′} ≤ c_Nλ₀^{1−μ̄_T−a′}λ^{1/2+a′} = C₀λ^{1/2+a′}; C₀λ₀^{a′} = c_Nλ₀^{1−μ̄_T} ≤ 1 (SC49).

*(T2′), (T2).* Let λ > λ₀; by (8.2) Δ := Θ_b − Θ_a ∈ (Δ₀, 2π − x_e]. *If Δ ≤ 2π − Δ₀:* x⁰(u_a), x⁰(u_b) are endpoints of two trajectories as in
Q7 (virtual, true, or Z_s) starting at e^{iΘ_a}, e^{iΘ_b}, and |e^{iΘ_b} − e^{iΘ_a}| = 2|sin(Δ/2)| ≥ 2 sin(Δ₀/2) = c_sep > 2ε (Δ₀ ≤ η ≤ π/3, (SC44)); by
Q7, c ≥ c_sep. *If Δ > 2π − Δ₀:* ξ_a := Θ_a − α₀ ≥ 0 and ξ_b := α₀ + 2π − Θ_b ≥ x_e satisfy ξ_a + ξ_b < Δ₀ ≤ η (SC43): a is in the forward zone, b in the
tail. In the frame (X₀; û, iû): z_a = ∫₀^{u_a}cos ψ du ≥ cos(θ_vΔ₀^{1−μ̄})u_a (|ψ| ≤ θ_vξ^{1−μ} ≤ θ_vΔ₀^{1−μ̄} ≤ π/2 on [0,u_a], (SC45)),
z_b ≤ −h_tξ_b ≤ −(h_t/W_t)u′_b (Q5(c); u′_b ≤ W_t(ξ_b − x_e)). So c ≥ z_a − z_b ≥ κ₂(u_a + u′_b) ≥ (u_a + u′_b)/2 (SC46).

*(T3′), (T3).* For u ≤ G (≤ η): ξ ≤ u ≤ η, |T − n̂| ≤ θ_vξ^{1−μ} ≤ θ_vu^{1−μ} ≤ θ_vG^{3/4−μ̄}u^{1/4} ≤ ϑ₃max(u, ε/2)^{1/4} (u ≤ G < 1; 3/4 − μ ≥ 3/4 − μ̄ > 0).
*(T4′), (T4).* For u′ ≤ G: ξ ≤ x_e + u′ ≤ x̄_e + G ≤ η (SC50), |T − n̂| ≤ θ_tξ^{1−μ_T} ≤ θ_t s^{1−μ_T} with s := x_e + u′ ≤ s̄ := x̄_e + G < 1. By (d) of Q5,
z₀ = −z_E ≥ h_t x_e, so s ≤ (u′ + z₀)/h_t and θ_ts^{1−μ_T} ≤ (θ_t/h_t)(u′ + z₀)^{1−μ_T} ≤ c_T4(u′ + z₀)^{1−μ̄_T}
(h_t ≤ 1; the last step needs u′ + z₀ ≤ 1, which holds since z₀ ≤ z_T x_e ≤ z_T x̄_e and u′ ≤ G: (SC51) [v2, C1]). For (T4):
s^{1−μ_T} ≤ s̄^{1/2−μ̄_T}s^{1/2}, s^{1/2} ≤ x_e^{1/2} + u′^{1/2}, x_e^{1/2} ≤ xe_hi^{1/2}ε^{1/(4−4v)} ≤ xe_hi^{1/2}ε^{1/4} = 2^{1/4}xe_hi^{1/2}(ε/2)^{1/4},
u′^{1/2} ≤ G^{1/4}u′^{1/4}: |T − n̂| ≤ ϑ₄max(u′, ε/2)^{1/4}.
*(T5′), (T5).* x⁰(U) = E_Y (Θ(U) = 2π + b_e) and P(t_s) − x⁰(U) = −z_Eû − y_E iû, i.e. z₀ = −z_E, y₀ = −y_E. By Q5(d),(a):
h_t x_e ≤ z₀ ≤ z_T x_e, which gives the bounds on z₀ (ε^{1/(2−2v)} ≤ ε^{1/2}); in particular 0 ≤ z₀ ≤ z_T xe_hi ε^{1/2} ≤ C_zε^{1/4}.
|y₀| = y_E ≤ y_T x_e^{2−μ_T} ≤ y_T(z₀/h_t)^{2−μ_T} ≤ (y_T/h_t²)z₀^{2−μ_T} (h_t ≤ 1) ≤ c_y(z₀ + ε)^{2−μ̄_T} (z₀ + ε ≤ z_T x̄_e + ε̄ < 1 by (SC51) [v2, C1]). For (T5):
z₀^{1−μ_T} ≤ (z_T xe_hi)^{1−μ_T}ε^{(1−μ_T)/2} ≤ max(1, z_T xe_hi)ε^{1/4} (μ_T ≤ 1/2), so |y₀| ≤ c_y z₀·max(1, z_T xe_hi)2^{1/4}(ε/2)^{1/4} ≤ ϑ₅(z₀ + ε)(ε/2)^{1/4}. ∎

---------------------------------------------------------------------------------------------------------------------

## §9. Corollary Q.T — the table (side conditions evaluated by `code/Q3/constants.py`)

> **Corollary Q.T.** For each column of the table in `reports/Q3-1.md` §3 (parameters v̄, η, ε̄ and the printed x₁, λ₀, G), (SC1)–(SC51)
> hold; hence Theorem Q.H applies with the printed constants (upper bounds rounded up, lower bounds rounded down in the 4th digit).

*Proof.* Each (SC) is an explicit inequality between closed-form numbers (finitely many evaluations of elementary functions), evaluated by
`constants.py` in 50-digit arithmetic; the script prints "ALL OK (50)" for every column of the table. [v2, C7] (SC51) is evaluated from
the same `chain()` output (z_T·x̄_e + ε̄, G + z_T·x̄_e): for ε̄ = 10⁻³ the values are ≤ 0.0667 and ≤ 0.2115 (largest at (2·10⁻², 0.2),
resp. (10⁻³, 0.3)); for ε̄ = 10⁻⁶, z_T x̄_e ≤ 0.0022 and G ≤ 0.15. ∎

*Column used downstream [v2].* `reports/Q4-1.md` uses the column (v̄, η, ε̄) = (6·10⁻⁵, 0.1, 10⁻³), x₁ = 1.007, λ₀ = 0.0333, G = 0.05
(not in the table above): `constants.chain` gives "ALL OK (50)" and (SC51) = (0.050509, 0.099509); constants (exact to 10 digits):
T₂ = 3.732464046, U_max = 6.293194844, c_sep = 0.03305914661, κ₂ = 0.988089123, c_N = c_near = 2.721593485, μ̄_T = 1.799892006·10⁻⁴,
θ_v = 1.070023505, c_T4 = 1.042625000, h_t·xe_lo = 1.270254458, z_T·xe_hi = 1.565623623, c_y = 0.6197969295, ϑ_T = ϑ₅ = 1.15396938,
C_z = 0.2784116253, K_b = 1.212766047.

*Remark (where the extension stops; NUMERICAL facts about the formulas, not claims about (H_T)).* With ε̄ = 10⁻³: the first (SC) to fail
when η grows is (SC21) C_hi < 1 (η ≥ 0.35 for v̄ ≤ 10⁻³; η ≥ 0.3 for v̄ = 10⁻²), then (SC7) (η ≈ 0.4). When v̄ grows at fixed η the
constants degrade smoothly up to v̄ = 2·10⁻² (K_b ∝ v̄/η² is the fastest-growing one; at v̄ = 10⁻², η = 0.1 it makes c_far the largest term of
c_N). At v̄ = 3·10⁻² (η ∈ [0.15, 0.25]) the first (SC) to fail is (SC42) W_xL̂ ≤ 2 (W_x ≈ 1.6–1.9; it is a convenience condition of (8.2) and
could be relaxed), together with (SC21) for η ≥ 0.2; at v̄ = 5·10⁻² also (SC47), (SC49) fail (c_N ≈ 11–18, K_b ≈ 26–61). So the proof as
written reaches v̄ = 2·10⁻²; beyond, the constants (not the method) break down. D₁: evaluating the same formulas with the geometry of overshoot D₁ ∈ {0.25, 0.5, 0.75} (the definition allows
D₁ ∈ (0,1]) gives uniformly worse λ₀, c_sep, c_N (D₁ = 0.25 fails (SC18) or (SC3)); D₁ = 1.5, 2 (outside def:T) improve c_N by ≤ 3% at
η = 0.1 and ≤ 14% at η = 0.3. So D₁ = 1 is kept and nothing is re-proved for D₁ ≠ 1.

---------------------------------------------------------------------------------------------------------------------

## §10. Theorem HT′ (interface for Q2; v ≤ 10⁻⁶, ε ≤ 10⁻³) and the repair of thm:HT (T1)

### 10.1 Statement
> **Theorem HT′.** For design T with D₁ = 1, all v ∈ (0, 10⁻⁶], ε ∈ (0, 10⁻³], with the curve x⁰, 𝒢 and n̂ of Theorem Q.H (parameters
> v̄ = 10⁻⁶, η = 0.1, ε̄ = 10⁻³, x₁ = 1.007, λ₀ = 0.0333, G = 0.05), (H_T) holds with T₂ = 3.733, U_max = 6.285, λ₀ = 0.0333, c_sep = 0.0330,
> γ_T = 1/4, ϑ_T = 1.153, G_T = 0.05, C_z = 0.2783, a′ ∈ (0, 1 − 3·10⁻⁶], C₀ = 2.72·λ₀^{1−3·10⁻⁶−a′} (a′ = 1/2: C₀ = 0.4962; a′ = 0.9: 1.935),
> and:
>  (T1′) N ≤ 2.72 λ^{3/2−3v} (≤ 5.4 λ^{3/2−3v});
>  (T2′) c ≥ min(c_sep, 0.9883(u_a + u′_b)) for λ > λ₀;
>  (T3′) |T − n̂| ≤ 1.070 u^{1−μ} ≤ 1.69 u^{1−3·10⁻⁶} for u ≤ 0.05;
>  (T4′) |T − n̂| ≤ 1.043 (u′ + z₀)^{1−3·10⁻⁶} (≤ 1.66 (u′ + z₀)^{1−3·10⁻⁶}) for u′ ≤ 0.05;
>  (T5′) z₀ ≤ 1.565 ε^{1/2} (≤ 1.567 ε^{1/2}), |y₀| ≤ 0.6194 (z₀ + ε)^{2−3·10⁻⁶} (≤ 0.63 (z₀+ε)^{2−3·10⁻⁶}).
*Proof.* Corollary Q.T, column (10⁻⁶, 0.1, 10⁻³) ((SC51): 0.050485, 0.099485); μ̄_T = 3v̄/(1+v̄) ≤ 3·10⁻⁶ and μ_T ≤ 3v. Constants are those printed by `constants.py`
(c_N = 2.7190…, κ₂ = 0.98840…, θ_v = 1.06937…, c_T4 = 1.04197…, z_T·xe_hi = 1.56486…, c_y = 0.61929…, ϑ_T = 1.15246…,
C₀(½) = 0.496180…, C₀(0.9) = 1.93491…), rounded outward. ∎
(The forms with the old constants 5.4, 0.979, 1.69, 1.66, 1.567, 0.63 also follow from P8a v3 directly — see `reports/Q3-1.md` §1 —
once the (T1) proof there is repaired as in 10.2.)

### 10.2 A gap in the proof of (T1) in thm:HT / Theorem P8a.H (statement true) and its repair
In the far case of (T1), P8a uses on the tail |k| ≤ 1.0001ξ^{−μ_T} ≤ 1.0001ε^{−μ_T} and then "ε^{−μ_T} ≤ (2λ)^{−μ_T} ≤ λ^{−μ_T}". Since λ ≥ ε/2, the
middle inequality is reversed: ε^{−μ_T} ≥ (2λ)^{−μ_T}. The constant K = 1.22λ^{−3v} is therefore not justified for far pairs ending near E_Y
when x_e ≪ λ [v2, C5: wording of RQ3-2 §4] (the proved tail bound 1.0001ξ^{−μ_T} exceeds 1.22λ^{−3v} at ξ = x_e only if (λ/x_e)^{3v} > 1.22,
i.e. x_e < λe^{−0.199/(3v)}; with x_e ≥ 1.27ε^{1/2} this needs ε < 10^{−57570} at v = 10⁻⁶ (numerically the actual curvature at E_Y is
≈ x_e^{−μ_T}, so the bound K is then genuinely false); the numerical checks, down to ε = 10⁻⁷⁰⁰, could not see it). The same step occurs in
Proposition P8a.1(2) (for (E1) on A₂).

[v2, C6] **Status in the paper.** `paper/sec_T1.tex` has already been repaired (rem:T1-status, "After the reports"): the proof of
thm:HT (T1) contains the split below (cases "Near E_Y" / "Far"), and the proof of prop:T1-arcs(2) uses RQ3-1 §6's device (the
curvature bound 1.22·min(σ,1)^{−μ_T} in the arclength σ to E_Y is integrated from the midpoint), which keeps the stated constant
0.36 (N ≤ 0.3522λ^{3/2−μ_T}). So the "4.15" for Prop. P8a.1(2) below is superseded in the paper; sec_HTp cites the repaired sec_T1 and
does not repeat the repair.
*Repair (P8a constants).* Split the far case of thm:HT (T1) as in Theorem Q.H: (i) if u′_b ≥ λ or x_e ≥ λ, tail labels of the pair have
ξ ≥ x_e + u′/1.015 ≥ λ/1.015, so |k| ≤ 1.0001·1.015^{μ_T}λ^{−μ_T} ≤ 1.22λ^{−3v} and the far-case bound 0.353λ^{3/2−3v} stands; (ii) if u′_b < λ and x_e < λ
("near E_Y"), u′_a < 2λ ≤ 1/20, ξ ≤ x_e + u′ < 3λ ≤ 0.075, and by (ii) of the thm:HT proof and lem:T1-elem(b):
N² ≤ 1.647²∫(x_e + u′)^{2−2μ_T}du ≤ 1.647²·19λ^{3−2μ_T}/(3−2μ_T), N ≤ 1.647·2.5166λ^{3/2−μ_T} ≤ 4.15λ^{3/2−3v}. Hence N ≤ 5.4λ^{3/2−3v} as stated
(near X₀: 5.3; the sharper near-X₀ bound of `reports/Q3-1.md` §1 gives 4.39). Prop. P8a.1(2): the same split with K = 1.22 on A₂ away from
the end and the tail-near case gives N ≤ 4.15λ^{3/2−μ_T} there (the claimed 0.36 is not justified for pairs ending near E_Y when ε is
astronomically small; Prop. P8a.1 is not used by thm:HT).
