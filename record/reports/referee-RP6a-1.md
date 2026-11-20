# Referee report RP6a-1 — referee/P6a-claims.md (Lemmas V, VC, 1–4, C; Theorems R, B; Corollary M)

Independent, adversarial. Read: referee/P6a-claims.md, paper/main.tex (prop:length, lem:limit, lem:A41), paper/sec_D2.tex
(headers only). Not read: reports/P6a-1.md, code/P6a, other referee reports.
Code: `code/referee/P6a_1/lemmas.py` (random tests + all constants), `sim.py` (Construction C, invariants at every leg
start and mid-leg), `st_scaling.py` (curvature ahead of the base vs ε); outputs `out*.txt`, `st_v*.txt` there.

## Summary

| Claim | Verdict |
|---|---|
| Lemma V, VC | OK |
| Lemma 1 (i)–(iv) | OK |
| Lemma 2 | OK |
| Lemma 3 (a)–(d), Duhamel form | OK |
| Lemma 4 | OK |
| Construction C, Lemma C | OK (one cosmetic remark) |
| Theorem R | OK |
| Theorem B, frame (first-failure argument), Steps 1, 2, 5 | OK (cosmetic constants) |
| Theorem B, Step 3 | OK with fixes (one false intermediate assertion, harmless) |
| Theorem B, Step 4 Term II | **GAP (small, repairable with the same constant)** — case b < a_{j+1} |
| Derivation of (F_b), (S) | OK |
| Corollary M | OK as a conditional statement, with two fixes of wording; use of lem:A41 legitimate |
| "NUMERICAL" sentence after Cor. M | **FALSE as stated** ((ST) includes (IC3), which the quoted data violate; and (ST) at a fixed leg index is not uniform in ε) |

No error found that threatens Theorem B. After the fixes F1–F3 below I consider Theorem B proved. The absolute-v₀
goal remains open exactly as the file says; see §7 for what the hypotheses of Corollary M really require.

## 1. Lemmas V, VC, 1, 2, 3, 4 — OK

Checked by hand line by line; all signs and constants reproduce.
* V(iii): f/ρ − f' = ρ/ε² inside, 1/ρ outside; |sin χ cos χ|·ρ/max(ρ,ε)² ≤ |x×e|/max(ρ,ε)². V(ii): eigenvalues f', f/ρ ∈ [0, a*].
* Lemma 1: T = cos φ r̂ − sin φ n is consistent with sin φ := T × r̂ (r̂ × n = +1). κ_t: cos 2φ − sin²φ = 1 − 3 sin²φ,
  cos²φ + cos 2φ = 3 cos²φ − 1. (iv): (Ja) × b = −a·b. (Lemma 1(iii),(iv) are not used later.)
* Lemma 2(iv): X' = vX(1/ρ_a + 1/ρ_b) − P' × (r_b − r_a) and r_b − r_a = x_b − x_a.
* Lemma 3(c): ∂_pQ = −m(m² − 2p²)/|y|⁵ (max of |c(3c² − 2)| on [−1,1] is 1, at c = ±1; interior extremum 0.63),
  ∂_mQ = −p(p² − 2m²)/|y|⁵; the expansion gives exactly (v/ρ_m)(1 + l/ρ_m + 2l²/ρ_m²)N² + 2v l^{3/2}|p_a|N/ρ_m³.
  Duhamel: 1 + 1/4 + 2/16 = 1.375; N_ηN_η' = E' is right.
* Lemma 4(b): the sum telescopes to l(a₁,s) + c(a₀,a₁) − c(a₀,s) ≤ E(a₀,s).
* Numerics (`lemmas.py`): V(iii), V(iv), 0 ≤ A ≤ a*, A = DF on 20000 random points: 0 violations. Identity 2(ii) and
  inequalities 3(a), 3(b), 3(c) (both), 3(d), 4(a), 4(b) on 3000 random arcs/positions (3(c) on 2209 admissible ones):
  0 violations; max E'/bound in 3(c) = 0.87, so 3(c) is not far from sharp. Lemma 1: ψ_t, κ_t formulas vs finite
  differences agree to 5·10⁻⁷ and 3·10⁻⁶ (scale 0.34); 1(iv) to 6·10⁻⁸.

Cosmetic: "c(a,b) > 0 (by VC(b))" fails for (a,b) = (0, 2π) (same point). Never used (excluded by (IC2)); say "for
(a,b) ≠ (0,2π)".

## 2. Construction C, Lemma C — OK

(1) ρ ≥ 1 − (1−v)t ≥ ε on [0,t_ε]; t₀ ≤ t_ε + ε/(1−v) = 1/(1−v). (2) both ansätze verified (β' = 1 + vf(β), ρ' = −1 + vf(ρ)).
(4) l' ≤ (2v/ε)l, duration ≤ ε/(1−v) ⇒ factor e^{2μ}. (5) uses prop:length(2) for t_ε < t₀ = 1/(1−v): legitimate (true
dynamics, straight run, d = 1), 2π + 2πv t_ε < 2π/(1−v).
Sim: target reached to < 10⁻⁶ε at every leg, t₀ = 1/(1−v) − O(ε v).

## 3. Theorem R — OK

Recomputed: near part 8ε₁·(2/ε) = 16e^{2μ}; far part (2/r₁)·e^{2μ}L_s; middle part 2[2c₀ + c₁/4] + 2[2c₀/γ + c₁/2] =
4c₀(1 + 1/γ) + 1.5c₁ ≤ 4c₀(1 + 1/γ) + 2c₁. ρ_s ≥ 3l/4 − ε₁ ≥ l/2 needs l ≥ 4ε₁ (have 8ε₁). Lemma 4(b) applies with
a₀ = a_j, a₁ = a_{j+1} ≤ s₁. Induction and leg count correct (the final "leg" has zero duration). For legs with
a_{j+1} ≥ b*, (F_b), (S) are vacuous and everything is tip — consistent with the max(a_{j+1}, b*) in (T).

## 4. Theorem B

### 4.0 Frame (family, first-failure time, time bound) — OK
* **No pair ever enters the family.** If (a,b) ∈ 𝔉(t), t in leg j+1, then for every earlier leg i+1 (i < j):
  a ≥ a_j ≥ a_{i+1}. So 𝔉(t) ⊂ 𝔉(t') for t' < t. At t = t_{j+1} the two conventions differ (leg j+1 family ⊃ leg j+2
  family); the argument works for either (bounds pass to the closed leg by continuity). Pairs whose first point is
  skipped (a ∈ (a_j, a_{j+1})) leave the family for good; pairs (a_j, b) are kept only during leg j+1. Endpoints
  inside the ε-disc cause no problem because everything is written for the C¹ virtual field.
* **Closedness and strict room.** (Imp) gives √2 and ¼ on [t_s, t*) hence at t* (closed inequalities, 𝔉(t*) ⊂ 𝔉(t));
  the extension uses |l'| ≤ (2v/ε)l, |E'| ≤ (4v/ε)l ≤ (8v/ε)λ and λ ≥ ε/2, so δ = δ(v, ε, M) > 0 uniform over the
  (infinite) family. Correct. The case t* = t_s is covered by the start (1/128 < ¼).
* **Non-circularity of T_B.** Step 1(a) for leg j+1 uses (I1) only at t_j, for the pair (a_j, u_{a_j} + ε/2), which is in
  𝔉(t_j) (needs u_{a_j} + ε/2 ≤ U: this is the leg condition). So for t < t* only legs with t_j < t* are counted:
  ≤ 2U/ε legs, elapsed time ≤ 4U + 2ε ≤ T_B. No circularity.
* **Uniformity in ε.** No constant in Steps 1–5 depends on ε; ε enters only through ε ≤ R/64 (used as: 2ε ≤ R/32,
  16R − 2ε ≥ 15R, 2ε(32ε)^{-1/2} ≤ 0.045R^{1/2}) and λ ≥ ε/2. OK.
* **Ranges.** κR ≤ 1/1584 is exactly κR^{3/4} ≤ M/(8√2) (140·8·√2 = 1583.92). The four conditions are mutually
  consistent and non-empty as constraints (choose R ≤ 1/(1584κ), then ε ≤ R/64, then v). Useful remark to add: (ST) is
  monotone in R: if (IC1), (IC2) hold for R they hold for every R' < R (for λ ∈ (32R', 32R], c ≥ λ(1 − (32κR)²) ≥ 16R').
* Start: κ²λ³ ≤ κ²R^{3/2}λ^{3/2} ≤ M²λ^{3/2}/128. OK. (CA): OK.

Cosmetic (Step 1(a)): in the last considered leg(s) (u_{a_j} > U − ε) a_{j+1} may lie beyond b*, so "u_{a_{j+1}}" is
undefined. Replace by: "u_{a_{j+1}} − u_{a_j} ∈ [ε/2, ε] if a_{j+1} ≤ b*; otherwise no family pair has a ≥ a_{j+1}."

### 4.1 Step 1 — OK
(c): Σ over legs of 2ε h(g_j); for every attained gap g_j > g_min, h(g_j) ≤ (2/ε)∫_{g_j−ε/2}^{g_j} h and these intervals
are disjoint in [g_min, ∞). Correct. (d): three cases verified (16R − 2ε ≥ 15.97R ≥ 5.34R).

### 4.2 Step 2 (TL) — OK
Single step 2√2·3^{3/4} + 1/140 = 6.455 ≤ 6.7. Geometric factor 1/(1 − 2^{-1/4}) = 6.285; 6.7·6.285 = 42.11 (the text
says 42.1 — replace by 42.2); total 90.92 ≤ 91. Family membership of all intermediate arcs checked: in (A) the first
point is α (a first point of a family pair), in (B) all first points are ≥ a° ≥ a_{j+1} (α > a ≥ a_j forces α ≥ a_{j+1}),
(C) uses u_{a_{j+1}} − u_{a_j} ≤ ε and λ(a_{j+1}, b) ≥ λ_J ≥ ε/2. C_μ = 2 + 4·91² = 33126, √(2C_μ) = 257.4 ≤ 258.
"Sharing an endpoint" is not needed for the single step (Lemma 4(a) needs only J' ⊂ I').

### 4.3 Step 3 (far pairs) — OK with fixes
All constants reproduce: 5.5/16 = 0.344, 5.5/32 = 0.172, 2·2^{3/2}·1.125·64 = 407.3, 364·(65/64)^{1/4} = 365.4,
2·2^{3/2}·366·64 = 1.3251·10⁵, (1/16 + 6)·64^{-3/4} = 0.2679, 1.33·10⁵·0.268 = 35644, 408·10⁻⁶·140 = 0.0571 ≤ 1/16.
(32R/g₂)^ν ≤ max(1, R/(2λ))^ν ≤ (R/λ)^ν: OK.

**F1 (false intermediate assertion, harmless).** "in particular ρ_m ≥ 16λ ≥ max(ε, 4l)" is not justified when
g > 32R and λ > 8R/11: there ρ_m ≥ 16R − 2ε − 2λ ≥ 13.96R, which can be < 16λ. Consequently "|p_a| ≤ ρ_m + l ≤
1.125ρ_m" is also unjustified there (l/ρ_m ≤ 0.1432). What is needed survives. Replacement text:

> "… ρ_m ≥ ĝ/2 − 6λ. If g ≤ 32R this is ≥ (1/2 − 6/64)g ≥ 26λ ≥ g/4; if g > 32R it is ≥ 16R − 2ε − 2λ ≥ 13.9R ≥ ĝ/4.
> In both cases ρ_m ≥ ĝ/4 and ρ_m ≥ 13.9λ ≥ max(ε, 4l) (l ≤ 2λ), so Lemma 3(c) applies … *Forcing.* If g > R/2:
> |p_a| ≤ ρ_a ≤ ρ_m + l. For R/2 < g ≤ 32R: l ≤ ρ_m/13 and ρ_m ≥ R/8, so β ≤ 2v(2λ)^{3/2}·(14/13)·64/R² ≤ 390vλ^{3/2}/R²;
> for g > 32R: l ≤ 0.144ρ_m and ρ_m ≥ 13.9R, so β ≤ 2v(2λ)^{3/2}·1.144/(13.9R)² ≤ 0.04vλ^{3/2}/R². Hence β ≤ 408vλ^{3/2}/R²."

### 4.4 Step 4 (near pairs) — one GAP in Term II, otherwise OK

Checked: time near ≤ 256λ + 4ε ≤ 264λ; Term I (layer-cake identity for a*, J_y of label length ≤ min(λ, 6y), the
"6 + 6 log⁺ + 6" bracket, 6ρ̄ ≥ g̃ when g ≤ 32R and log⁺ = 0 when g > 32R); Term II first case (g' ≥ ε/2: 91·65^{1/4} =
258.4 ≤ 260; 0 < g' < ε/2: J₀ ⊂ (a', b) since u_b ≥ u_a + ε/2 > u_{a'} + ε/2, constant √8.0001 = 2.83 ≤ 3);
|p(s)| ≤ ϑ(λ'_s + 4g + 3ε) ≤ ϑ(4w_s + 3.5ε); (5w + 4ε)/max(ε, w/6) ≤ 34; II-integral; time integrals
(264 + 8/e + 4 = 270.9 ≤ 272; at most two, not three, legs have g < ε); 6·536·C_μ = 1.0653·10⁸; 204·272 = 55488;
26.4·140 = 3696; totals 3.89·10⁹ and 3.55·10¹⁰, times 10⁻¹² ≤ 1/8.

**F2 (GAP).** Term II, case "a = a_j and a' = a_{j+1}": the text says the arc between a' and s is "contained in
(a, max(s, a'))" and bounds ∫|T − e| over it by Step 2 (μ). (μ) is only available for sub-arcs of (a,b). But a pair
(a_j, b) of the family may have b < a_{j+1}: the family allows λ ≥ ε/2 while u_{a_{j+1}} − u_{a_j} can be up to ε
(in the simulation it is 0.9–1.0 ε, so every pair (a_j, b) with λ ∈ [ε/2, 0.9ε) is of this kind — this is generic,
not a corner case). Then (a, a') ⊄ (a, b), and |T − e_{ab}| on (b, a') is not controlled by (μ) for the pair (a,b).
The bound claimed, |(x_s − x_{a'}) × e| ≤ ϑ·max(λ'_s, ε), is nevertheless true. Insert:

> "If b < a_{j+1} (possible only when λ < ε; then 65λ ≤ R): put I' := (a_j, a_{j+1}), a family pair with λ_{I'} ≤ ε ≤ 2λ
> containing (a,b). For s ∈ [a,b]: |(x_s − x_{a'}) × e| ≤ ∫_{I'}|T − e_{ab}| ≤ ∫_{I'}|T − e_{I'}| + l(I')|e_{I'} − e_{ab}|
> ≤ (2ε)^{1/2}Mε^{3/4} + 2ε·91Mε^{1/4} ≤ 183.5Mε^{1/4}·ε ≤ 218.2Mλ^{1/4}ε ≤ ϑε, by (I1), (I2) for I' and (TL) for (a,b) ⊂ I'."

(183.5·2^{1/4} = 218.2 ≤ 260.) With this the bound |p(s)| ≤ ϑ·max(λ'_s, ε) and everything after it is unchanged.

Remaining case distinctions for |p(s)| verified exhaustively: a ≥ a_{j+1} ⇒ both a' ≤ a, and g' = 0 (a' = a = a_{j+1}),
g' ∈ (0, ε/2) (only a' = a_{j+1}), g' ≥ ε/2 (a' = a_j always, since g ≥ ε/2); a = a_j ⇒ a' = a_j (g' = 0) or a' = a_{j+1}
(F2). 65λ > R and w_s > 32R branches: trivial bounds correct (6 ≤ 204ϑ; ρ_s ≥ 16R − 2ε ≥ 15R).

### 4.5 Step 5 — OK
8(367²·16 + 1) = 1.724·10⁷; 2ε(32ε)^{-1/2} + 8(R/2)^{1/2} ≤ 5.702R^{1/2}; 12·536 = 6432.
Cosmetic: "1.73·10⁷·5.8 ≤ 10⁸" is false as arithmetic (= 1.0034·10⁸); the exact product is 9.83·10⁷, so write
"1.724·10⁷·5.71 ≤ 10⁸". 10⁸/19600 = 5102 ≤ 5200.

### 4.6 (F_b), (S) — OK
E ≤ ½M²λ^{3/2} ≤ ½M²R^{1/2}·l(l/R)^{1/2}, c₀ = 1/39200; ρ_s ≥ R/4 − R/32 = 7R/32 ≥ R/8. For legs with a_{j+1} ≥ b' the
hypotheses of Theorem R are vacuous, so the restriction "a_{j+1} < b'" loses nothing.

### 4.7 Simulation of Construction C (`sim.py`)
Head-on start, t_s = t₂, labels [0, 0.25], grid ε/10, RK4, target snapped to the grid (step ∈ (0.9ε, ε]); ≈3000–3200
legs (base label up to ≈ 0.14 ≈ 45R); κ, R, M computed from the data at t_s (R := 1/(1584κ)); ≈ 60 first points × 40
label lengths per check, at every leg start and mid-leg.

| v | ε | ε/(R/64) | adv/ε | max l/λ (≤2) | max E/(½M²λ^{3/2}) (≤1) | min c/(min(λ,32R)/2) (≥1) | max tilt/(Mλ_I^{1/4}) (≤91) |
|---|---|---|---|---|---|---|---|
| 10⁻¹² | 4.5·10⁻⁵ | 0.93 | [0.90,1.00] | 1.0000000 | 0.0156 | 2.00 | 0.215 |
| 10⁻³ (out of range) | 5·10⁻⁵ | 1.03 | [0.90,0.91] | 1.0013 | 0.0156 | 2.00 | 0.215 |
| 0.05 (out of range, (ST) violated) | 5·10⁻⁵ | 4.4 | [0.84,0.98] | 1.072 | 6.7·10⁻⁴ | 2.00 | 0.043 |
| 0.1 (out of range, (ST) violated) | 5·10⁻⁵ | 16 | [0.73,0.97] | 1.154 | 1.1·10⁻³ | 2.00 | 0.054 |

In the admissible run (v = 10⁻¹²; κ = 0.2041, R = 0.00309, M = 0.0303, IC2 ratio 2.18, v(4U+2)/(10⁻⁶R) = 10⁻³) all
hypotheses of Theorem B hold and (I1), (I2), (CA), (*), Step 1(a), (TL) hold at every leg (l/λ = 1 against 2; factor 64 of room in (I2), 420 in (TL)). This is
of course a weak test: at v = 10⁻¹² the front does not move. The out-of-range runs show no sign that the structure is
wrong (the invariants hold with large margins even at v = 0.1).

## 5. Corollary M — OK as a conditional statement, with fixes

It is stated as conditional ("Suppose that …"; "What is NOT proved"). K* = 16e^{2μ} + 20c₀ + 16e^{2μ}L_s/R + K_T with
20/39200 = 1/1960; μK* ≤ 0.5(1 + 2·10⁻¹²) ≤ 0.51; 1/((1 − v)·0.49) = 2.041 ≤ 2.1. U ≤ R_{j_s} ≤ L_s gives
v(4U + 2) ≤ 10⁻⁶R. U − u_{2π−δ} ≥ δ/2 ≥ ε/2 by |∂_θx| ≥ 1.

**Use of lem:A41 — legitimate.** Hypotheses of the lemma: nested finite D_N with dense union; ε_N → 0; H_N with
|H_N'| ≤ 1 on [0,T] coming within ε_N of every direction of D_N by T. Take any ε_N ↓ 0, ε_N ≤ ε₀, H_N := path of
construction C for (v, ε_N) (1-Lipschitz, H_N(0) = 0, independent of α), T := T_s + 2.1L_s, D_N arbitrary nested (H_N
sees *all* directions; "seen" refers to the true candidate by Lemma VC(c)). The limit path depends on v only. Note: the
printed proof of lem:A41 in paper/main.tex l.244 has a dropped phrase ("replaced by  If H did not…"); the mathematics
is clear, but the sentence should be repaired in the paper.

**F3 (wording).**
(a) (ST) contains (IC3), i.e. ε ≤ R/64; with R absolute this forces ε₀ ≤ R/64. Replace "let ε₀ ≤ δ" by
"let ε₀ ≤ min(δ, R/64)".
(b) The parenthetical "(or any path … that coincides with construction C from some leg start on)" needs the proviso
of Remark (2) to Theorem R; add: "provided every direction with label in [0, a_{j_s}] has been seen by time t_s".
(c) j_s must be allowed to depend on ε (only t_s ≤ T_s is absolute) — the statement permits this; say so explicitly,
because it is necessary (§7).

## 6. The "NUMERICAL" sentence — FALSE as stated

"(ST) holds from the second leg after first contact (j_s = 2) with κ² ≤ 0.038, 32R = 0.11 … for v = 0.05, 0.1, 0.2
and ε = 0.02 … 0.005."
1. (ST) includes (IC3). With κ² = 0.038, R = 0.11/32: κR = 6.7·10⁻⁴ > 1/1584 = 6.31·10⁻⁴; and ε ≤ R/64 = 5.4·10⁻⁵, whereas
   the tested ε are 100–400 times larger. So at most (IC1), (IC2) were verified, not (ST). (By monotonicity in R one
   can take R = 1/(1584κ) ≈ 0.0032, but then ε ≤ 5·10⁻⁵ is required.)
2. The tested v (0.05–0.2) are 10¹⁰ times outside Theorem B's range, so these numerics say nothing about the
   hypotheses in the regime where the theorem applies.
3. (ST) at a *fixed* leg index is not uniform in ε (`st_scaling.py`, grid ε/20). The head-on contact leaves a rounded
   corner of total turning ≈ 2 arcsin v at label 0; at t₀ the curvature within ε of the base is ≈ 1.7 v/ε
   (v = 0.05: 21.9, 85, 339, 1400, 5561 for ε = 4·10⁻³, 10⁻³, 2.5·10⁻⁴, 6·10⁻⁵, 1.5·10⁻⁵; v = 10⁻³: 1.46, 2.9, 8.6, 33, 127).
   Its tail reaches further (in units of ε) as ε ↓ 0: at leg 2, v = 0.05, sup E/λ³ over pairs ahead of the base with
   λ ≤ 8ε is 0.033, 0.027, 0.021, **0.114, 2.50** for the same ε (max |curvature| 13.4 at ε = 1.5·10⁻⁵; at v = 0.1,
   ε = 5·10⁻⁵: 15.6, κ² ≥ 10). So "κ² ≤ 0.038 from j_s = 2" fails for ε ≲ 10⁻⁴. At leg 8 it holds again for all tested
   ε (0.012–0.034), so j_s must grow as ε ↓ 0.

## 7. What this means for the open goal (not a defect of the proved claims)

* For fixed v > 0, (ST) with absolute κ, R at j_s = 0 is false for small ε: (IC1) forces κ ≳ 0.35 v/ε. Since
  Corollary M / lem:A41 need all ε ≤ ε₀ at fixed v, the start must be taken at a leg j_s(ε) → ∞ (with ε j_s(ε) bounded),
  after the corner tail has left the arc ahead of the base. Proving (ST) therefore requires a quantitative
  description of the corner tail, i.e. an analysis of the first O(j_s(ε)) legs, which Theorem B does not cover.
* (IC1) for λ → 0 is a pointwise curvature bound, stronger than what the proof uses: (IC1) is used only (i) for
  λ ≥ ε/2 (start of (I2) and N(t_s) in Step 3) and (ii) through (CA). The hypothesis can be weakened verbatim to
  "(IC1) for pairs with ε/2 ≤ λ ≤ 32R, and (CA) at t_s for all pairs"; the proof is unchanged. This does not remove the
  corner problem (pairs with λ ≈ ε near the corner have E ≈ v²λ ≫ κ²λ³) but removes an unnecessary requirement.

## 8. List of fixes

* F1 (Step 3): replace "ρ_m ≥ 16λ" and "≤ 1.125ρ_m" as in §4.3.
* F2 (Step 4, Term II): add the case b < a_{j+1} as in §4.4. **This is the only real gap.**
* F3 (Cor. M): ε₀ ≤ min(δ, R/64); proviso for the parenthetical; j_s may depend on ε.
* Cosmetic: 42.1 → 42.2 (Step 2); "1.73·10⁷·5.8" → "1.724·10⁷·5.71" (Step 5); "at most three legs" → two (harmless);
  c(0,2π) = 0; Step 1(a) when a_{j+1} > b*; the claim ρ_m ≥ 16λ in Step 3.
* Rewrite the NUMERICAL sentence (§6): state that only (IC1), (IC2) were checked, at ε ≫ R/64 and v ≫ 10⁻¹², and that
  j_s = 2 is not uniform in ε.
