# R9-tilt claims: sharper tilt bounds and the near-pair constant D (statements and full proofs)

Stream R-tilt, round 9 (plan: `reports/L-9.md`, item R2, with R3 for the L¹/L² uses). Base text: `r9/base_short/`
(sec2–sec4, Definition 3.3 = `def:param`). Constants: `r9/tilt/tilt_constants.py` → `r9/tilt/tilt_constants.out`;
sanity checks: `r9/tilt/sanity_curves.py` → `r9/tilt/sanity_curves.out`. Summary and use-by-use table: `reports/R9-tilt.md`.

**Status labels.** PROVED: every step is written below and uses only refereed statements of `r9/base_short`
(Lemma 2.x = sec2, Lemmas legs/gapint/dist/local, Theorem `thm:end` (CA) = sec3). NUMERICAL: a script value or experiment
that is not a proof. Numerical *evaluations* of PROVED formulas use rigorous upper bounds (monotone pieces, upper Riemann
or grid sums at 40 digits). Those are marked "PROVED formula, evaluated rigorously".

Notation as in sec3–sec4: M = mR^{-γ}, χ = χ_g = κd_L, c₆ = (1+δ₁)/c_A, ξ := ε/λ ∈ (0,2], x := g/λ. Throughout, V_K := x_β − x_α
for an arc K = (α,β), so V_K = c(K)e_K = ∫_K T ds. Also u×v := u₁v₂ − u₂v₁, and ϑ := T·e^⊥ (sec2's \vsig).

---------------------------------------------------------------------------------------------------------------------
## 0. New derived constants (to be added to Definition 3.3)

q := q_c (the chain ratio, a free parameter as before). We recommend q = 2.42. All formulas below hold for every q > 1.

  s(r) := (κ^{1/2}/c_A)·(r/2 if 1 ≤ r ≤ 2;  (r−1)^{1/2} if r ≥ 2)          (continuous and increasing)
  ω_r := (1 − m²r/(4c_A))^{−1/2},   r_* := max(q, 2q/(q−1)),   ω_* := ω_{r_*}
  **C_T := ω_*·max(σ_q s(q), s(2q/(q−1)))**          (replaces C_A, C_B and C_TL)
  **C_μ := 1 + κC_T²**                               (replaces C_μA; C_1A is no longer used)
  Profiles, for ζ > 0 and C = C_μ:
    Φ_α(ζ) := ∫_ζ^∞ η^{-3} min(1,η) min(1,Cη) dη,
    Φ_l(ζ) := ∫_ζ^∞ η^{-2} (min(1,η) min(1,Cη))^{1/2} dη,
    Φ_β(ζ) := ∫_ζ^∞ η^{-3} (min(1,η) min(1,Cη))^{1/2} dη,
    B(x)  := x^{1/2}(1+x)^γ(1+κx/c_A) Φ_β(x),
    S₀    := sup_{0<ξ≤2} ξ·(min(ξ,1) min(Cξ,1))^{1/2}·Φ_β(c₆ξ).
  **D_I′ := T_I + c₆χ log C_μ**
  Π_α := c₆²κ[d_L/c₆ + χ(2 + log C_μ − 1/(2K_f))],   Π₀ := d_L·max(2c₆²κS₀, κ²2^γ/c_A),   Π_β := 2c₆²κχ∫₀^{K_f}B,
  **D_IIs′ := Π_α + Π₀ + Π_β**
  T_l := d_L/c₆ + χ(3 + log K_f − C_μ^{−1/2}),   **D_IIl′ := c₆(K_f+1)^γ κ^{1/2} T_l / m**                      (drop-in)
  S(μ) := c₆²κ[d_L/c₆ + χ∫₀^{μ−1}Φ_α] + Π₀ + 2c₆²κχ∫₀^{μ−1}B,
  Λ(μ) := (c₆κ^{1/2}μ^γ/m)[d_L/c₆ + χ∫_{μ−1}^{K_f}Φ_l],   **D_IIl″ := sup_{1≤μ≤K_f+1}(S(μ)+Λ(μ))**     (split long case)
  **C_p′ := κ^{1/2}(1+1/K_f)^{1/2+γ}K_f^{−1/2} + κC_T(1+1/K_f)^γ**  (replaces C_p in B₃, B₅)
  θ̄ := f_F² + 2v₀[D_I′ + max(D_IIs′, D_IIl′)]   (or with D_IIl″ in place of D_IIl′ when §6.4 is used).

**Side conditions (T-side)**, all with large slack at the current parameters (values in `tilt_constants.out`):
(T1) m²r_* < 4c_A;  (T2) C_μ ≥ (1+2γ)κ/c_A;  (T3) γ ≤ c_A/κ;  (T4) K_f(2γ−1) ≤ 3c_A/κ.
(K_f ≥ 1 and C_μK_f ≥ 1 follow from (P0) and C_μ ≥ 1.)
**Removed conditions.** "κ ≤ C_TL²(4−κ²)" and "c_t(3) ≥ √3" (Appendix A "extra") are no longer used.

---------------------------------------------------------------------------------------------------------------------
## 1. Lemma S (split tilt; static): PROVED

*Let u ↦ x_u be a regular C¹ (or piecewise C¹) curve, I = (a,b) a label interval with c(I) > 0, J = (α,β) ⊂ I with
c(J) > 0 and J ≠ I, and l_c := l(I) − l(J) > 0. Put Z := |V_J × e_I|.*
*(i) Z² ≤ N(I)²·l(J)·l_c / l(I).*
*(ii) If N(I)² < 4c(J), then |e_J − e_I| ≤ (Z/c(J))·(1 − N(I)²/(4c(J)))^{−1/2}.*
*(iii) |V_I × e_J| = (c(I)/c(J))·Z. If J shares the right end of I and L := I∖J = (a,α), then
|V_L × e_J| = |V_I × e_J| ≤ (1 + c(L)/c(J))·Z, and also |V_L × e_J| ≤ Z + c(L)|e_I − e_J|.*

*Proof.* (i) V_J × e_I = ∫_J T × e_I ds = ∫_J (T − e_I) × e_I ds, and |(T−e_I)×e_I| ≤ |T−e_I|; so by Cauchy–Schwarz
Z² ≤ l(J)∫_J|T−e_I|². Since V_I × e_I = 0 and V_I = V_J + V_{I∖J} (the complement is one or two arcs),
V_J × e_I = −V_{I∖J} × e_I = −∫_{I∖J}(T − e_I)×e_I ds, so Z² ≤ l_c∫_{I∖J}|T−e_I|². Adding Z²/l(J) + Z²/l_c ≤
∫_I|T−e_I|² = N(I)² (Lemma 2.static(b) with û = e_I), and 1/l(J) + 1/l_c = l(I)/(l(J)l_c).
(ii) Put d := e_J − e_I, cos θ := e_J·e_I. Then |d|² = 2 − 2cos θ and |d|²(1 − |d|²/4) = (2−2cos θ)(1+cos θ)/2 =
sin²θ = |e_J × e_I|² = Z²/c(J)². By Lemma 2.static(b) on J with û = e_I and additivity/non-negativity of V_{e_I},
c(J)|d|² ≤ V_{e_I}(J) ≤ V_{e_I}(I) = N(I)², so |d|²/4 ≤ N(I)²/(4c(J)) < 1, and |d| = (Z/c(J))(1 − |d|²/4)^{−1/2} ≤ the claim.
(iii) |V_I × e_J| = c(I)|e_I × e_J| and Z = c(J)|e_J × e_I|. If J = (α,b), then V_J × e_J = 0 and V_L × e_J = V_I × e_J; and
c(I) ≤ c(L) + c(J). For the last form: V_L × e_J = V_L × e_I + V_L × (e_J − e_I), where V_L × e_I = −V_J × e_I has modulus Z,
and |V_L × (e_J − e_I)| ≤ c(L)|e_J − e_I|. ∎

---------------------------------------------------------------------------------------------------------------------
## 2. Lemma T (Tilts; drop-in replacement of `lem:tilt`): PROVED

*Hypotheses exactly as in `lem:tilt`: t ≤ T_def in leg j+1, I = (a,b) a pair of the family of leg j+1, and (J1), (J2) hold
at t for every pair of that family contained in [a_j, max(b, a_{j+1})]. Assume (T1).*
*(o) (one step) For pairs J ⊂ I of that family, J ⊂ I, with λ_I ≤ rλ_J and 1 ≤ r < 4c_A/m²:
|e_J − e_I| ≤ ω_r s(r) Mλ_I^γ.*
*(i) For pairs J ⊂ I of that family: |e_J − e_I| ≤ C_T Mλ_I^γ = C_T m(λ_I/R)^γ. This holds whatever ends J and I share, so
C_T replaces C_A, C_B and C_TL.*
*(ii) (E-μ′) For a < s ≤ b and λ_s := max(s−a, ε/2):*
  ∫_a^s|T − e_ab|² ds ≤ M²λ^{2γ}·min(C_μλ_s, λ),   ∫_a^s|T − e_ab| ds ≤ Mλ^γ·(κλ_s·min(C_μλ_s, λ))^{1/2}.

*Proof.* All pairs used lie in [a_j, max(b,a_{j+1})] and in the family, so (J1), (J2) and (CA) apply to them
(same locality as the original proof).
(o) If J = I there is nothing to prove. Otherwise Lemma S(i) gives Z² ≤ N(I)² f(l(J)), where f(ℓ) := ℓ(1 − ℓ/l(I)). Here f
increases in l(I) for fixed ℓ, l(I) ≤ κλ_I (J1), and ℓ = l(J) ≤ κλ_J (J1). So f(l(J)) ≤ max_{0<ℓ≤κλ_J} ℓ(1 − ℓ/(κλ_I)),
which is κλ_I/4 if κλ_J ≥ κλ_I/2, and κλ_J(1 − λ_J/λ_I) otherwise. With ρ := λ_I/λ_J this is κλ_J·ρ̃(ρ),
where ρ̃(ρ) = ρ/4 for ρ ≤ 2 and 1 − 1/ρ for ρ ≥ 2. Then (J2) and (CA) (c(J) ≥ c_Aλ_J) give
Z/c(J) ≤ Mλ_I^{1/2+γ}(κλ_Jρ̃)^{1/2}/(c_Aλ_J) = (κ^{1/2}/c_A)(ρρ̃(ρ))^{1/2}Mλ_I^γ = s(ρ)Mλ_I^γ ≤ s(r)Mλ_I^γ, because
ρρ̃(ρ) = ρ²/4 resp. ρ−1, s is increasing and ρ ≤ r. Further N(I)²/(4c(J)) ≤ M²λ_I^{1+2γ}/(4c_Aλ_J) ≤ m²r/(4c_A) < 1
(Mλ_I^γ ≤ MR^γ = m). Lemma S(ii) gives the claim.
(i) Let J = (a′,b′) ⊂ I = (a,b), λ_k := λ_Iq^{−k} and K := min{k ≥ 1 : λ_k ≤ λ_J}.
*Case A: a ≥ a_{j+1}, or a′ = a, or λ_I(1 − 1/q) ≥ ε.* For 0 ≤ k ≤ K−1 put α_k := min(a′, b − λ_k), I_k := (α_k, α_k + λ_k),
and I_K := J.
(1) J ⊂ I_k ⊂ I. Indeed α_k ≥ min(a′, b−λ_I) = a and α_k ≤ a′. The right end is min(a′+λ_k, b), which is ≤ b, and it is
≥ b′ because λ_k > λ_J for k ≤ K−1.
(2) The chain is nested. α_k is non-decreasing in k and the right end is non-increasing, so I_{k+1} ⊂ I_k; also J ⊂ I_{K−1}.
(3) Each I_k is in the family. Its length λ_k ∈ (λ_J, λ_I] ⊂ [ε/2, R]. Its first point is a′ (admissible, being the first
point of the family pair J) or b − λ_k < a′. In the second case k ≥ 1 (I_0 = I), and b − λ_k ≥ b − λ_I/q = a + λ_I(1−1/q).
This is ≥ a ≥ a_{j+1} if a ≥ a_{j+1}, and ≥ a_j + ε ≥ a_{j+1} if λ_I(1−1/q) ≥ ε (Lemma legs: a_{j+1} − a_j ≤ ε). If a′ = a,
then α_k = a for all k.
(4) Ratios. λ(I_k)/λ(I_{k+1}) = q for k+1 ≤ K−1, and λ(I_{K−1})/λ_J ∈ [1, q).
By (o) with r = q, |e_{I_{k+1}} − e_{I_k}| ≤ ω_q s(q)Mλ_k^γ, and summing,
|e_J − e_I| ≤ ω_q s(q)Mλ_I^γ Σ_{k=0}^{K−1}q^{−kγ} < ω_* σ_q s(q) Mλ_I^γ ≤ C_T Mλ_I^γ.
*Case B: a = a_j, a′ > a and λ_I(1 − 1/q) < ε.* Then λ_I/λ_J < (εq/(q−1))/(ε/2) = 2q/(q−1) ≤ r_*, and (o) with
r = 2q/(q−1) gives |e_J − e_I| ≤ ω_* s(2q/(q−1))Mλ_I^γ ≤ C_T Mλ_I^γ.
(ii) As in the original: J := (a, a+λ_s) is a family pair (first point a, length in [ε/2, λ]) and J ⊂ I. By Lemma 2.static(b)
with û = e := e_ab, (J2), (J1) and (i): ∫_a^s|T−e|² ≤ ∫_J|T−e|² = N(J)² + c(J)|e_J − e|² ≤ M²λ_s^{1+2γ} + κλ_sC_T²M²λ^{2γ}
≤ C_μM²λ^{2γ}λ_s. Also ∫_a^s|T−e|² ≤ ∫_I|T−e|² = N(I)² ≤ M²λ^{1+2γ}. For the L¹ bound, Cauchy–Schwarz on (a,s) and
l(a,s) ≤ l(J) ≤ κλ_s. ∎

*Remark (a) of the brief, the direct bound.* With J ⊂ I, Lemma 2.static(b) alone gives c(J)|e_J − e_I|² ≤ N(I)², i.e.
|e_J−e_I| ≤ c_A^{−1/2}(λ_I/λ_J)^{1/2}Mλ_I^γ. Lemma S(i) improves this by the factor s(r)/(r/c_A)^{1/2} =
(κρ̃(r)/c_A)^{1/2} (≈ 0.72 at r = q_c). It is used per step in the chain. A one-step bound with ratio r beats the chain for
s(r) < C_T, i.e. r ≲ 1 + (c_AC_T)²/κ ≈ 9.2.

---------------------------------------------------------------------------------------------------------------------
## 3. Lemma G′ (gap–time integral without boundary term): PROVED

*Let t′ be as in Lemma legs, a a label, and 𝒯 ⊂ [t_td, t′] a set of times on which g(τ) = a − a_{j(τ)} ≥ ε/κ. If h ≥ 0
is non-increasing on (0,∞), then ∫_𝒯 h(g(τ))dτ ≤ χ∫_0^∞ h(y)dy.*

*Proof.* The gap is constant on each leg, and its values on distinct legs differ by at least ε/κ (Lemma gapint, preamble).
So each value is taken on one leg only, for a time ≤ d_Lε (Lemma legs(iv)). Let g_1 > … > g_n ≥ ε/κ be the values. Then
h(g_i) ≤ (κ/ε)∫_{g_i−ε/κ}^{g_i}h, and these intervals are disjoint and lie in [0,∞). So the integral is
≤ d_Lε Σ h(g_i) ≤ d_Lκ∫_0^∞h. ∎

---------------------------------------------------------------------------------------------------------------------
## 4. Lemma O (offsets |p_a|): PROVED

Setting of Propositions 4.2/4.3 (standing assumptions of sec4): τ in a leg with base β, next base β⁺, (a,b) the pair,
e = e_ab, g = a − β, p_a = (x_a − P)×e. Since P ∈ [x_β, x_{β⁺}] and y ↦ |(y − x_a)×e| is convex,
|p_a| ≤ max_{a′∈{β,β⁺}} Y_{a′} with Y_{a′} := |(x_a − x_{a′}) × e| (and Y_{a′} = 0 if a′ = a).

*(O1) Near, g > 0, g + λ ≤ R:* |p_a| ≤ κ^{1/2}Mλ^{1+γ}·x^{1/2}(1+x)^γ(1+κx/c_A),  x = g/λ.
*(O2) g = 0:* if β⁺ ≤ b, |p_a| ≤ Mλ^{1+γ}(κ min(ξ,1) min(C_μξ,1))^{1/2}. If β⁺ > b, then 1 ≤ ξ ≤ 2 and
|p_a| ≤ (κ^{3/2}/(2c_A))ξ^{2+γ}Mλ^{1+γ}.
*(O3) Far, g ≥ K_fλ, g ≤ η₁R:* |p_a| ≤ C_p′Mg^{1+γ}.

*Proof.* (O1) Since g > 0, a ≥ β⁺, the leg is non-final, and g ≥ β⁺−β ≥ ε/κ ≥ ε/2 (κ ≤ 4/3). Fix a′ with g′ := a − a′ > 0
(so g′ ≤ g), and put I′ := (a′,b), J := (a,b), L := (a′,a). I′ is a family pair: first point β or β⁺, length
g′+λ ∈ [ε/2, R], contained in [β, max(b,β⁺)]. If g′ ≥ ε/2, L is a family pair and l(L) ≤ κg′. Otherwise
L ⊂ L₀ := (a′, a′+ε/2) ⊂ I′ (as ε/2 ≤ λ), which is a family pair, and l(L) ≤ κε/2. In both cases l(L) ≤ κg. By Lemma S(iii),
Y_{a′} = |V_L × e| ≤ (1 + c(L)/c(J))Z′ with Z′ := |V_J × e_{I′}|. By Lemma S(i) (complement L),
Z′² ≤ N(I′)²l(J)l(L)/(l(J)+l(L)). The map (y,z) ↦ yz/(y+z) increases in both arguments, and l(J) ≤ κλ, l(L) ≤ κg,
N(I′) ≤ M(g′+λ)^{1/2+γ} ≤ M(g+λ)^{1/2+γ}. Hence Z′² ≤ κM²(g+λ)^{2γ}gλ, and with c(L) ≤ l(L) ≤ κg, c(J) ≥ c_Aλ:
Y_{a′} ≤ (1 + κg/(c_Aλ))κ^{1/2}M(g+λ)^γ(gλ)^{1/2}, which is the claim.
(O2) Here a = β, x_a is on the line, and |p_a| ≤ |(x_{β⁺} − x_a)×e|. If β⁺ ≤ b, this equals |∫_a^{β⁺}(T−e)×e| ≤ ∫_a^{β⁺}|T−e|.
By Lemma T(ii) with λ_u := max(β⁺−a, ε/2) ≤ min(ε, λ) = λ min(ξ,1) (β⁺ − β ≤ ε, β⁺ ≤ b), this is
≤ Mλ^γ(κλ_u min(C_μλ_u,λ))^{1/2} ≤ Mλ^{1+γ}(κ min(ξ,1)min(C_μξ,1))^{1/2}.
If β⁺ > b, then I₀ := (β,β⁺) is a family pair (first point β, λ_{I₀} ∈ [ε/κ, ε] ⊂ [ε/2,R]) containing J = (a,b) with the same
left end. So λ ≤ ε, i.e. ξ ≥ 1. By Lemma S(iii), |(x_{β⁺}−x_a)×e| = |V_{I₀}×e_J| = (c(I₀)/c(J))Z₀ with Z₀ := |V_J × e_{I₀}|. By
Lemma S(i), Z₀² ≤ N(I₀)²l(J)l_c/l(I₀) ≤ N(I₀)²l(I₀)/4, as l(J)+l_c = l(I₀). With c(I₀) ≤ l(I₀) ≤ κε, N(I₀) ≤ Mε^{1/2+γ},
c(J) ≥ c_Aλ: |p_a| ≤ (κε)^{3/2}Mε^{1/2+γ}/(2c_Aλ) = (κ^{3/2}/(2c_A))ξ^{2+γ}Mλ^{1+γ}.
(O3) As in the original proof of Prop 4.2: g ≥ K_fλ, so a > β⁺, and for a′ ∈ {β,β⁺} we have g′ ≥ g − ε ≥ (K_f−2)λ ≥ ε/2.
Then L = (a′,a), I′ = (a′,b) and J are family pairs with λ(I′) ≤ g+λ ≤ η₁R(1+1/K_f) ≤ R. By Lemma S(iii) (last form) and
Lemma S(i): Y_{a′} ≤ Z′ + c(L)|e_{I′} − e| with Z′ ≤ N(I′)l(J)^{1/2} ≤ M(g′+λ)^{1/2+γ}(κλ)^{1/2}. By Lemma T(i),
|e_{I′}−e| ≤ C_TM(g′+λ)^γ, and c(L) ≤ κg′. With g′ ≤ g, λ ≤ g/K_f, g′+λ ≤ g(1+1/K_f):
Y_{a′} ≤ [κ^{1/2}(1+1/K_f)^{1/2+γ}K_f^{−1/2} + κC_T(1+1/K_f)^γ]Mg^{1+γ} = C_p′Mg^{1+γ}. ∎

---------------------------------------------------------------------------------------------------------------------
## 5. Lemma P (profile functions): PROVED

Let C = C_μ ≥ 1. By direct integration over η ∈ (0,1/C), (1/C,1), (1,∞), where the factor min(1,η)min(1,Cη) equals Cη², η, 1:
  Φ_α(z) = C log(1/(Cz)) + C − 1/2 (z ≤ 1/C);  1/z − 1/2 (1/C ≤ z ≤ 1);  1/(2z²) (z ≥ 1).
  Φ_l(z) = C^{1/2}(log(1/(Cz)) + 2) − 1 (z ≤ 1/C);  2z^{−1/2} − 1 (1/C ≤ z ≤ 1);  1/z (z ≥ 1).
  Φ_β(z) = C^{1/2}/z − C^{3/2}/3 − 1/6 (z ≤ 1/C);  (2/3)z^{−3/2} − 1/6 (1/C ≤ z ≤ 1);  1/(2z²) (z ≥ 1).
All three are positive, continuous and decreasing.
(P1) zΦ_α(z) ≤ 1 and zΦ_l(z) ≤ 1 for all z > 0. For z ≥ 1 they are 1/(2z) and 1. On [1/C,1] they are 1 − z/2 and
2z^{1/2} − z ≤ 1. For w := Cz ≤ 1 they are w(1 − log w) − w/(2C) ≤ 1, and C^{−1/2}w(2 − log w) − w/C ≤ 2C^{−1/2} − 1/C ≤ 1,
since w ↦ w(2−log w) increases on (0,1].
(P2) Φ_β(z) ≤ C^{1/2}/z for all z. This is clear for z ≤ 1/C. On [1/C,1], (2/3)z^{−3/2} ≤ C^{1/2}z^{−1} iff z ≥ 4/(9C). On
[1,∞), 1/(2z²) ≤ 1/z ≤ C^{1/2}/z.
(P3) For K ≥ 1, by Tonelli (∫_0^K Φ(x)dx = ∫_0^∞ min(K,η)·φ(η)dη):
∫_0^KΦ_α = 1 + log C + (1 − 1/K) + 1/(2K) = 2 + log C − 1/(2K), and
∫_0^KΦ_l = C^{−1/2} + 2(1 − C^{−1/2}) + log K + 1 = 3 + log K − C^{−1/2}.
(P4) Under (T2)–(T4), B is non-increasing on (0, K_f]. Write B = P·u with P(x) := (1+x)^γ(1+κx/c_A) and
u := x^{1/2}Φ_β(x) > 0. Then (log P)′ = γ/(1+x) + 1/(c_A/κ + x) ≤ (1+γ)/(x + c_A/κ), as c_A/κ ≤ 1. B′ ≤ 0 iff
(log P)′u ≤ −u′.
  On (0,1/C]: u = C^{1/2}x^{−1/2} − c₀x^{1/2} (c₀ = C^{3/2}/3+1/6), so −u′ ≥ ½C^{1/2}x^{−3/2}. It suffices that
  (1+γ)C^{1/2}x^{−1/2}/(x+c_A/κ) ≤ ½C^{1/2}x^{−3/2}, i.e. (1+2γ)x ≤ c_A/κ, which follows from x ≤ 1/C and (T2).
  On [1/C,1]: u = (2/3)x^{−1} − x^{1/2}/6, so −u′ ≥ (2/3)x^{−2}. It suffices that (1+γ)(2/3)x^{−1}/(x+c_A/κ) ≤ (2/3)x^{−2},
  i.e. γx ≤ c_A/κ, which follows from (T3).
  On [1,K_f]: B = P(x)x^{−3/2}/2, and (log B)′ ≤ (1+γ)/(x+c_A/κ) − 3/(2x) ≤ 0 iff (2γ−1)x ≤ 3c_A/κ, which follows from (T4).
B is continuous, so it is non-increasing on (0,K_f].
(P5) ∫_0^{K_f}B < ∞, since B ~ C^{1/2}x^{−1/2} at 0.

---------------------------------------------------------------------------------------------------------------------
## 6. Proposition 4.3′ (near pairs; same statement, new constants): PROVED

*If (a,b) is near at t, then E(a,b;t) ≤ ½θ̄M²λ^{1+2γ}, with θ̄ := f_F² + 2v₀[D_I′ + max(D_IIs′, D_IIl′)]. The variant
with D_IIl″ in place of D_IIl′ is also valid (§6.4).*

The start value, the splitting E′ ≤ I + II (Lemma excess(iii), q̄ = 0) and the conclusion are as in the original. Below,
F(u) := ∫_a^u|T−e|ds for u ∈ [a,b]. It is absolutely continuous in arclength with F′ = |T−e| ≥ |ϑ|. By Lemma T(ii):
  (F)  F(u)² ≤ κM²λ^{2γ}λ_u min(C_μλ_u, λ),  λ_u := max(u−a, ε/2).
For y ≥ c₆ε put u_y := min(b, β+y), so the labels s ∈ (a,b) with w_s < y are exactly those of (a, u_y) (empty if y ≤ g). Then
u_y − a ≤ min(λ, y), and since ε/2 ≤ min(λ,y), λ_{u_y} ≤ min(λ,y). Hence, using C_μ ≥ 1,
  (F′) F(u_y)² ≤ κM²λ^{2γ}min(λ,y)min(C_μy, λ), for y ≥ c₆ε.

### 6.1 Term I (all near pairs)
ω(y) := ∫_{ρ_s<y}|T−e|². For y ≥ ε: if (y+δ₁ε)/c_A ≤ K_RR, the set lies in (a, a+λ_y) as in the original, with
λ_y ≤ min(λ, c₆y) and λ_y ≥ ε/2. Lemma T(ii) gives ω(y) ≤ M²λ^{2γ}min(C_μλ_y, λ) ≤ M²λ^{2γ}min(C_μc₆y, λ). Otherwise c₆y > K_RR ≥ λ
and ω(y) ≤ N² ≤ M²λ^{1+2γ} = M²λ^{2γ}min(C_μc₆y, λ). So for all y ≥ ε:
  ω(y) ≤ M²λ^{2γ}min(λ, C_μc₆y).
*Piece ω(ε)/ε.* It is non-zero only if g < c₆ε (original argument), and then it is ≤ M²λ^{2γ}min(λ, C_μc₆ε)/ε. At most κc₆+1
legs have g < c₆ε (Lemma gapint(iii)), each lasting ≤ d_Lε. So the contribution is ≤ (κc₆+1)d_L λ·vM²λ^{2γ}.
*Piece ∫_ρ̄^∞ωy^{−2}dy* (ρ̄ := max(ε, min ρ)). Substituting z = C_μc₆y, it is ≤ M²λ^{2γ}C_μc₆h₁(C_μc₆ρ̄) (Lemma int, h₁). As in the
original, c₆ρ̄ ≥ max(c₆ε, min(g,K_Rλ)), and h₁ is non-increasing, so it is ≤ M²λ^{2γ}C_μc₆h₁(C_μ max(c₆ε, min(g,K_Rλ))), a
non-increasing function of g. Apply Lemma gapint(i) (g₀ = 0, cut at g < K_fλ, K_f ≤ K_R). Since z h₁(z) ≤ λ and
∫_0^{Kλ}h₁ = λ(2+log K) for K = C_μK_f ≥ 1, the time integral is
≤ v M²λ^{2γ}[d_Lε C_μc₆h₁(C_μc₆ε) + χc₆∫_0^{C_μK_fλ}h₁] ≤ vM²λ^{1+2γ}[d_L + c₆χ(2 + log K_f + log C_μ)].
*Total:* ∫_{t_n}^t I ≤ v[d_L(κc₆+2) + c₆χΨ_I + c₆χ log C_μ]M²λ^{1+2γ} = vD_I′M²λ^{1+2γ}.

### 6.2 Term II, short case (K_f+1)λ ≤ R
As in the original: |q(s)| ≤ |p(s)|/D(s)², p(s) = (x_s−x_a)×e + p_a, |(x_s−x_a)×e| = |∫_a^s(T−e)×e| ≤ F(s), and
D(s) ≥ max(w_s,c₆ε)/c₆ (Lemma dist, w_s < (K_f+1)λ ≤ K_RR). Put Φ(s) := c₆²/max(w_s,c₆ε)² = ∫_{max(w_s,c₆ε)}^∞2c₆²y^{−3}dy;
it is ≥ D(s)^{−2}. Then
  II ≤ v∫_a^b|ϑ|FΦ ds + v|p_a|∫_a^b|ϑ|Φ ds =: II_α + II_β.
By Tonelli, ∫_a^b hΦ ds = ∫_{c₆ε}^∞2c₆²y^{−3}(∫_{(a,u_y)}h ds)dy for h ≥ 0. With h = |ϑ|F, the inner integral is
≤ ∫_{(a,u_y)}FF′ = F(u_y)²/2. With h = |ϑ|, it is ≤ F(u_y). Both vanish for y ≤ g. Let y₀ := max(c₆ε, g). By (F′) and the
scaling y = λη:
  II_α ≤ vc₆²κM²λ^{2γ}Φ_α(y₀/λ),   II_β ≤ 2c₆²κ^{1/2}v|p_a|Mλ^{γ−1}Φ_β(y₀/λ).
*II_α in time.* h(g) := Φ_α(max(c₆ξ, g/λ))·1{g < K_fλ} is non-increasing. Lemma gapint(i) (g₀ = 0), together with
ξΦ_α(c₆ξ) ≤ 1/c₆ (P1) and (P3), gives ∫II_α ≤ vc₆²κM²λ^{2γ}·λ[d_L/c₆ + χ(2 + log C_μ − 1/(2K_f))] = vΠ_αM²λ^{1+2γ}.
*II_β, g = 0* (one leg, duration ≤ d_Lε = d_Lξλ; y₀ = c₆ε). If β⁺ ≤ b, by (O2):
II_β ≤ 2c₆²κvM²λ^{2γ}(min(ξ,1)min(C_μξ,1))^{1/2}Φ_β(c₆ξ). Times d_Lξλ, this is ≤ 2c₆²κd_LS₀·vM²λ^{1+2γ}.
If β⁺ > b, use instead ∫|ϑ|Φ ≤ F(b)∫_{c₆ε}^∞2c₆²y^{−3}dy = F(b)/ε² and F(b)² ≤ l(a,b)N(a,b)² ≤ κM²λ^{2+2γ}. With (O2):
II_β ≤ v(κ²/(2c_A))ξ^γM²λ^{2γ}, and times d_Lξλ (ξ ≤ 2) this is ≤ d_Lκ²2^γ/c_A·vM²λ^{1+2γ}.
So the g = 0 leg contributes ≤ vΠ₀M²λ^{1+2γ}.
*II_β, g > 0* (g ≥ ε/κ, x = g/λ < K_f, g + λ ≤ (K_f+1)λ ≤ R). (O1) and Φ_β(y₀/λ) ≤ Φ_β(x) give
II_β ≤ 2c₆²κ vM²λ^{2γ}B(x). By (P4), h(g) := B(g/λ)·1{g < K_fλ} is non-increasing on (0,∞). Lemma G′ then gives
∫II_β ≤ 2c₆²κχλ∫_0^{K_f}B·vM²λ^{2γ} = vΠ_βM²λ^{1+2γ}.
*Total:* ∫_{t_n}^tII ≤ v(Π_α + Π₀ + Π_β)M²λ^{1+2γ} = vD_IIs′M²λ^{1+2γ}.

### 6.3 Term II, long case (K_f+1)λ > R, drop-in form
As in the original: |q| ≤ 1/D, D(s) ≥ max(w_s,c₆ε)/c₆ (w_s < (K_f+1)R ≤ K_RR), so II ≤ v∫|ϑ|φ₁(w_s)ds with
φ₁(w) = ∫_{max(w,c₆ε)}^∞c₆y^{−2}dy. By Tonelli and (F′),
II ≤ v∫_{c₆ε}^∞c₆y^{−2}F(u_y)dy ≤ vc₆κ^{1/2}Mλ^γΦ_l(y₀/λ). Lemma gapint(i) with h(g) := Φ_l(max(c₆ξ,g/λ))1{g<K_fλ},
ξΦ_l(c₆ξ) ≤ 1/c₆ (P1) and (P3) give ∫II ≤ vc₆κ^{1/2}T_lMλ^{1+γ}. As Mλ^γ > m(K_f+1)^{−γ}, this is ≤ vD_IIl′M²λ^{1+2γ}.

### 6.4 Term II, long case, split form (gives D_IIl″)
Let μ := R/λ ∈ [1, K_f+1). Split the near times into 𝒯₁ := {g ≤ (μ−1)λ} and 𝒯₂ := {g > (μ−1)λ}.
On 𝒯₁, g + λ ≤ R. So in (O1) the pair I′ = (a′,b) is a family pair, and the derivation of 6.2 applies verbatim: it used
(K_f+1)λ ≤ R only through D(s) ≥ max(w_s,c₆ε)/c₆, which holds here as well, and through (O1). The time integrals over 𝒯₁ use
h(g)·1{g ≤ (μ−1)λ}, still non-increasing. They are ≤ v[c₆²κ(d_L/c₆ + χ∫_0^{μ−1}Φ_α) + Π₀ + 2c₆²κχ∫_0^{μ−1}B]M²λ^{1+2γ}
= vS(μ)M²λ^{1+2γ}. Note μ−1 < K_f, and the g = 0 leg lies in 𝒯₁.
On 𝒯₂, use 6.3: II ≤ vc₆κ^{1/2}Mλ^γΦ_l(max(c₆ξ, g/λ)). Lemma gapint(i) with g₀ := (μ−1)λ (h non-increasing on [g_min,∞))
gives ∫_{𝒯₂}II ≤ vc₆κ^{1/2}Mλ^{1+γ}[d_L/c₆ + χ∫_{μ−1}^{K_f}Φ_l]. Since 1/(Mλ^γ) = μ^γ/m, this is ≤ vΛ(μ)M²λ^{1+2γ}.
So ∫_{t_n}^tII ≤ v(S(μ)+Λ(μ))M²λ^{1+2γ} ≤ vD_IIl″M²λ^{1+2γ}. ∎

---------------------------------------------------------------------------------------------------------------------
## 7. Proposition 4.2′ (far pairs) and Proposition 4.4 (length): PROVED

In the proof of Prop 4.2, case g ≤ η₁R, replace the bound |p_a| ≤ C_pMg^{1+γ} by (O3): |p_a| ≤ C_p′Mg^{1+γ}. Everything else is
verbatim, with B₃′ := 2κ^{3/2}C_p′/c_ρ³ in (P5). Prop 4.4 uses C_p only through Prop 4.2, so it holds with
B₅′ := (2/c_ρ)[(C_p′ + κ^{1/2}K_f^{−1−γ})²/c_ρ² + K_f^{−2γ}] in L_J.

## 8. Theorem `thm:end`(c) and §5: PROVED
(c) now reads |e_J − e_I| ≤ C_T m(λ_I/R)^γ for all pairs J ⊂ I of FamS(t). The proof is as before (Lemma local(i) + Lemma T(i)).
In §5 (stage A, tuple p_A) replace C_A^A and C_B^A by C_T^A (C_T computed with γ = γ_D). So C₃ := 2C_B^A + C_A^A becomes
3C_T^A, and ω₀, θ_h1 use C_T^A. Every use there is "J ⊂ I family pairs sharing an end", which is covered by Lemma T(i).

---------------------------------------------------------------------------------------------------------------------
## 9. Values (PROVED formulas, evaluated rigorously; `r9/tilt/tilt_constants.out`)

Current INPUTS (q = q_c = 2.05829), main tuple p | stage A p_A:

| constant | old | new |
|---|---|---|
| C_A / C_B / C_TL | 6.3937 / 9.8636 / 16.257 | C_T = 2.9109 (all three) |
| C_μA → C_μ | 42.532 | 9.6082 |
| C_1A | 6.5734 | not used (the L¹ bound is (κλ_s min(C_μλ_s,λ))^{1/2}) |
| k₀ | 9.9434 | not used (Π₀ = 1.876) |
| D_I | 485.64 | D_I′ = 16.034 |
| D_IIs (727 + 5585 + 525) | 6837.1 | D_IIs′ = Π_α 19.37 + Π₀ 1.876 + Π_β 68.51 = 89.75 |
| D_IIl | 2960.8 | D_IIl′ = 528.88 (drop-in);  D_IIl″ = 182.20 (split) |
| **D** | **7322.76** | **544.91 (drop-in, ×13.4);  198.23 (split, ×36.9)** |
| C_p / B₃ / B₅ | 12.641 / 413.25 / 5162.0 | 3.855 / 126.03 / 493.5 |
| C_A^A, C_B^A (p_A) | 6.3923, 9.8637 | C_T^A = 2.9094 |

With q = 2.42: C_T = 2.8822, C_μ = 9.4397, D = 544.56 (drop-in) / 198.05 (split).
∫₀^{K_f}B: rigorous upper bound 8.2305 (mp.quad 8.2256). S₀ ≤ 0.22896. Side conditions (T1)–(T4) hold:
0.0031 < 1; 9.61 ≥ 2.27; 0.614 ≤ 0.980; 1.15 ≤ 2.94.

## 10. Sanity checks (NUMERICAL; `r9/tilt/sanity_curves.out`)
There were 36 random polygons (18 smooth Fourier, 18 rough self-similar with amplitude ~ scale^γ), stretch w ≥ 1 (κ up to 1.06),
with 4000 random samples per check and per curve. Constants were set to their sharp empirical values per curve. Worst LHS/RHS:
S(i) 0.99999, S(ii) 1.0000 (an identity up to the a-priori factor), S(iii) 1.0000 (an identity), T(o) 0.847,
T(i) 0.536, T(ii)-L² 0.979, T(ii)-L¹ 0.890, (O1) 0.899. The empirical sup of |e_J−e_I|/(Mλ_I^γ) was 0.95–1.63, against
C_T ≈ 2.9–3.5 (old C_TL ≈ 16–18). No violation.

## 11. Gaps / caveats (precise)
G1. None in the proofs above, to my knowledge. The new side conditions (T1)–(T4) must be added to Appendix A and checked by
verify_constants. S₀ and ∫B are evaluated by rigorous upper sums. A referee may prefer the closed-form bound
∫₀^{1/C}B ≤ P(1/C)(2 − (2/3)c₀C^{−3/2}), which is coarser: Π_β = 70.31 and D_IIs′ = 91.56. D is unaffected, since D_IIl
binds.
G2. D is now bound by the long case (D_IIl′ or D_IIl″, through Λ(1) = 175.3 = c₆κ^{1/2}[d_L/c₆+χ(3+log K_f−C_μ^{−1/2})]/m at
λ = R). That term comes from |q| ≤ 1/D for pairs with g+λ > R, where no family tilt bound exists. It is not a tilt question
(R5). The obvious substitute N(I′)² ≤ 2(κ−c_A)λ_{I′} (from (J1)+(CA)) gives no gain (checked: comparable rates).
G3. Using the chain bound for |p_a| at very small x (x ≲ 0.03) would lower Π_β by ≈ 5%. It is omitted, since D_IIs′ does
not bind.
