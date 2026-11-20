# Referee report RP8a-2 — `referee/P8a-claims.md` (v2): design T, touch-down data, Theorem P8a.H = (H_T)

Second (adversarial) referee. Angle: independent rebuild, uniformity, semantics, interface. I did not read
`reports/referee-RP8a-1.md`, `reports/P8a-1.md` or `code/P8a/`. Inputs assumed: the straight-run integrals
(`paper/main.tex`, prop:integrals), `paper/sec_B.tex` (field F, Lemma V, Lemma VC, Lemma 1), `paper/sec_ST.tex`;
[D] Lemma D0(a),(c) and [P7] Fact 0.2(i) as cited.

Code (all mine, nothing of the author's is imported): `code/referee/P8a_2/`
`front.py` (rebuild), `scan.py` (one (v,ε): every inequality), `driver.py`, `driver2.py`, `aggregate.py`
(`aggregate_out.txt`), `exps.py` (exponents), `check_transport.py`, `arm_bigv.py`, `tight.py`; logs `log_v*_e*.txt`,
data `out_v*_e*.json`.

## 0. Verdict

**Theorem P8a.H: OK with fixes.** The mathematical content — (T1)–(T5), the C¹ unit-speed curve x⁰, the
"seen or true" dichotomy of (T0), with the stated constants, for all v ∈ (0,10⁻⁶], ε ∈ (0,10⁻³], D₁ = 1 — is
confirmed: I found no counterexample, no overlooked regime and no ε- or v-non-uniform step. The fixes are textual:

* **F1 (interface, (T0) is not verbatim).** (H_T) of P8b §5 demands "a set 𝒢 ⊂ (0,U) of ghost labels". P8a's 𝒢
  contains u = 0 (the label α₀), and it must: x⁰(0) = P(t_s), whereas the true candidate α₀ is at
  S_{α₀}(t_s) = P(t_s) + (1−v)(t₂−t_s)û with t₂ − t_s > 0 strictly (I get t₂ − t_s = 0.33333·vε). So u = 0 cannot be a
  true label and "𝒢 ⊂ (0,U)" is unsatisfiable for design T. P8a's restatement of (T0) silently drops "⊂ (0,U)".
  Harmless: P8b never uses 0 ∉ 𝒢 (𝒢 occurs only in (T0); P8b's own "intended realisation" lists [α₀, α₀+1.02ε) ⊂ 𝒢).
  *Fix (P8b §5 (T0)):* "There is a set 𝒢 ⊂ [0,U) of ghost labels …". *Fix (P8a §9, after the definition of 𝒢):* "Note
  0 ∈ 𝒢 (Θ(0) = α₀); (H_T)(T0) is proved with 𝒢 ⊂ [0,U) in place of 𝒢 ⊂ (0,U)."
* **F2 (Lemma 4(d), the proof does not give the stated constant).** From "both brackets are in [1, 1+0.6ε]" one gets
  (1+θ_s)^{1+v} ≤ (1+0.6ε)^{2v}, i.e. θ_s ≤ 1.2vε, not θ_s ≤ vε. The statement is true (numerically
  θ_s = 0.750·vε², see §2). *Fix:* "the first bracket is in [1, 1 + 2.3ε²] (α_s ≤ 2.1ε), the second in [1, 1 + 0.5001ε];
  so 1 ≤ (1+θ_s)^{1+v} ≤ (1 + 0.51ε)^v and 0 ≤ θ_s ≤ 0.51vε."
* **F3 (Lemma 11(a), one label missing).** "For every α ∈ (0,2π) … in run 1, C = g(α) > 0" fails at α = π
  (g(π) = 0, β ≡ π, outside Lemma 1). *Fix:* add "for α = π: the candidate is on the axis behind Harry, ρ ≥ 1
  (Lemma 4(b)); in run 2 its b = π − β* ∈ (0,π)."
* **F4 (remark-level, P8b side).** P8b §6 Remark (4) quotes P8a's interim constants (ϑ_T = 4.3, U_max = 6.4); the
  refereed ones are ϑ_T = 3.3, U_max = 6.5, T₂ = 3.74, G_T = 0.05, C_z = 1.57. P8b's numerics used D₁ = 0.1; the
  proof covers D₁ = 1 only (P8a says so in §9 Remark (4) and §10.4). (H_T) as stated ("D₁ ∈ (0,1] a fixed absolute
  constant") is satisfied with D₁ = 1; nothing in P8b depends on the value.

Per claim:

| claim | verdict |
|---|---|
| Lemma 1, 2, 3 (exact, all v) | OK (Lemma 2 and the run-1 form of Lemma 3 reproduced by finite differences to 10⁻²², v = 0.3, 0.05, 10⁻⁶) |
| Lemma 4 (a),(b),(c),(e) | OK |
| Lemma 4 (d) | OK with fix F2 |
| Lemma 5 (a),(b),(c) | OK ((a) reproduced to 10⁻²⁶ relative) |
| Lemma 6 (a)–(e) | OK |
| Lemma 7 (a)–(d) | OK |
| Lemma 8 | OK |
| Lemma 9, 10 | OK |
| Lemma 11 | OK with fix F3 |
| Proposition P8a.1 | OK (superseded by the theorem) |
| Theorem P8a.H = (H_T) | OK with fix F1 (text of (T0)); (T1)–(T5) verbatim |

## 1. REBUILD (independent of the transport lemmas)

Method. S_θ(t₁) from the integrals of run 1 (C = g(α), h = cos α + v − (1−v²)t₁, solve for τ); re-expressed in the
frame of run 2 (r, b), new C = r g(b), h(t) = r(cos b + v) − (1−v²)(t−t₁), solve for τ again: position
z + iy relative to P(t) in the frame (û, iû). Tangent, stretch w and curvature k by central differences in the
label (relative step 10⁻¹²), in mpmath with dps = 2·log₁₀(1/ε) + 110 (116 digits at ε = 10⁻³, 230 at 10⁻⁶⁰, 610 at
10⁻²⁵⁰). Virtual labels α₀ + x, x < 1.02ε: true state and tangent at t_a, then the ODE x′ = vF(x − P) of [B]
with its variational equation on [t_a, t_s] (RK4). Self-checks: the virtual candidate α₀ arrives at P(t_s) with
residual 10⁻²⁴ε (so the closed form of t_s is right); at x = 1.03ε virtual and two-integral state agree to
10⁻²⁰ε with min ρ = 1.0300ε; curvatures down to the label 10⁻¹⁵α_s (ε = 10⁻⁴⁰) agree to 12 digits under dps 260/400 and
steps 10⁻⁶/10⁻¹²/10⁻²⁰.
(A first version of my root finder stopped inside a bisection step at high precision; found by this stability
test, fixed before any run reported here.)

Exponents (`exps.py`, ε = 10⁻⁴⁰; slopes of log–log data over a decade; the exact composition holds for all v):

| v | d log x_e/d log ε | claimed 1/(2−2v) | forward tilt | claimed (1−2v)/(1−v) | forward curvature | claimed −μ | tail tilt | claimed (1−2v)/(1+v) | tail curvature | claimed −3v/(1+v) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.02 | 0.510204082 | 0.510204082 | 0.979591839 | 0.979591837 | −0.0204081633 | −0.0204081633 | 0.941176471 | 0.941176471 | −0.0588235294 | −0.0588235294 |
| 0.1 | 0.555555556 | 0.555555556 | 0.888888954 | 0.888888889 | −0.111111119 | −0.111111111 | 0.727272727 | 0.727272727 | −0.272727273 | −0.272727273 |
| 0.3 | 0.714285714 | 0.714285714 | 0.571429091 | 0.571428571 | −0.428571818 | −0.428571429 | 0.307692308 | 0.307692308 | −0.692307692 | −0.692307692 |
| 10⁻⁶ | 0.5000005 | 0.5000005 | 0.999999 | 0.999999 | −1.000001·10⁻⁶ | −1.000001·10⁻⁶ | 0.999997 | 0.999997 | −2.999997·10⁻⁶ | −2.999997·10⁻⁶ |

All five claimed exponents are confirmed; curvature does blow up like x^{−μ} at X₀ and x^{−μ_T} at E_Y (e.g. v = 0.3:
k = 1.2·10¹⁵ at x = 10⁻³⁶ forward), so a′ = 1 is indeed false and a′ ≤ 1 − 3v is the right form.

Touch-down state for v ≤ 10⁻⁶ (ranges over the 30 runs of §2, ε from 10⁻³ to 10⁻²⁵⁰): α_s/ε ∈ [0.99942, 1.0000002];
x_e/ε^{1/(2−2v)} ∈ [1.41421, 1.41433] (claimed [1.277, 1.566]; the value is √2: the circle leaves the tangent line by
x²/2 = ε); z_E/x_e ∈ [−1.000003, −0.99967]; y_E/ε − 1 ∈ [4·10⁻¹⁵, 2.9·10⁻⁴] (≈ 70v at ε = 10⁻⁶⁰, 289v at 10⁻²⁵⁰:
the factor (x_e/ε)^{v}), positive; tilt ψ/x ∈ [1, 1.00058] on the whole forward arc, virtual labels included (claimed
≤ 1.69x^{−μ}), ψ/x ∈ [−1.00087, −1] on the tail (claimed ≥ −1.647x^{−μ_T}); k ∈ [1, 1.00058] on the forward arc and
[1, 1.00086] on the tail (the maxima at x = 1.02ε resp. x_e for ε = 10⁻²⁵⁰, v = 10⁻⁶: this is x^{−μ}, x^{−μ_T});
in the bulk |k − 1| ≤ 10⁻⁵, w − 1 ∈ [0.83v, 3·10⁻⁶]; t₂ − t_s = 0.33333vε.

Through the hole (true front at t_s, labels α = ±α_s·10⁻ʲ, j = 0…16, and at t₁ down to α_s·10⁻¹⁸): k ∈ [0.99755, 1.00000]
for v ≤ 10⁻⁶ (minimum at ε = 10⁻²⁵⁰; claimed |k| ≤ 1.22; at t₁ claimed ≤ 1.14), the tangent angle is the odd function
(ψ − arg G)/|G| = c·α/α_s with c ∈ [0.4988, 0.5000] (a circular arc of curvature ≈ 1 through Z_s), |S_{+α} − S_{−α}| → 0 linearly
(2.0·10⁻¹⁸·y_s at |α| = 10⁻¹⁸α_s), the projection on G = E₊ − E₋ is strictly increasing in the label, and
|Z_s − 1| = 1.3·10⁻⁶ ≤ 3.74·10⁻⁶. The other regime of the Remark after Lemma 4 ((yα)^{2v} ≪ 1, k₁ → v/(1−v²)) is not
reachable numerically at v ≤ 10⁻⁶; I checked it at larger v (`arm_bigv.py`, α from 0.5 down to 10⁻⁶⁰): k₁ ranges from
the parabola value up to ≈ 1 (v = 0.05: [0.050125, 0.98854], v/(1−v²) = 0.050125; v = 0.3: [0.32967, 0.779]) and
never exceeds 0.98 of the general-v form of the bound of Lemma 4(c), (1+v)/(cos α − v) + v/(1−v²) + v/((1−v)ρ₁).

## 2. UNIFORMITY

### 2.1 Numerical scan

30 runs, all labels and pairs in ≥ 116-digit arithmetic: v ∈ {10⁻⁶, 10⁻⁸, 10⁻¹¹, 10⁻¹⁵} × ε ∈ {10⁻³, 10⁻⁵, 10⁻⁹,
10⁻¹⁸, 10⁻³⁶, 10⁻⁶⁰}, plus (v, ε) = (10⁻⁶, 10⁻⁴), (10⁻⁷, 10⁻⁷), (3·10⁻⁷, 10⁻¹²), (10⁻⁶, 10⁻¹²⁰), (10⁻⁶, 10⁻²⁵⁰),
(10⁻¹⁰, 10⁻²⁵⁰). In addition two reduced runs (coarser grids, 1510 digits) at ε = 10⁻⁷⁰⁰,
v = 10⁻⁶ and v = 10⁻¹⁵: no violation (there k(E_Y) = 1.0024, hole curvature 0.9932, N/λ^{3/2} ≤ 0.2894).
Both orders of limits are in the grid (v = 10⁻¹⁵ ≪ ε = 10⁻³; ε = 10⁻²⁵⁰ ≪ v = 10⁻⁶). Per run: ≈ 110 separate
inequalities, evaluated on logarithmic grids (3 labels per decade from 1.02ε resp. x_e to 0.1 on the forward arc and
the tail, 2 per decade from 10⁻¹⁸α_s to 0.5 on the arm at t₁, from 10⁻³ε on both sides of α₀ for Lemma 5(c), from
10⁻⁶vε to x_e on the seen stretch), 37 bulk labels, 26 hole/axis labels, 11 virtual labels, ≈ 135 pairs for (T1),
≈ 60 for (T2). **No violation in any of the 32 runs.** Worst ratio "actual/bound" over all runs (1 = bound attained;
`aggregate_out.txt` has the full list):

| inequality | worst ratio | where |
|---|---|---|
| **(T1)** N ≤ 0.86 λ, ε/2 ≤ λ ≤ λ₀ | 0.0527 | λ = 0.985λ₀ (any position) |
| (T1) sharp form N ≤ 5.4 λ^{3/2−3v} | 0.0535 | everywhere (N/λ^{3/2} ∈ [0.28801, 0.28893] over 3795 pairs, i.e. 1/√12 = 0.28868) |
| **(T2)** wrap pairs, c ≥ (u_a + u′_b)/2 | 0.5076 | a at x = 0.0245, b = E_Y |
| (T2) other pairs, c ≥ 0.024 | 0.9756 | label gap 0.0246 (c = 0.024599) |
| **(T3)** | 0.0539 | u = 0.1 |
| **(T4)** | 0.0915 | ε = 10⁻³, next to E_Y |
| **(T5)** z₀ ≤ 1.57ε^{1/4}; \|y₀\| ≤ 3.3(z₀+ε)(ε/2)^{1/4} | 0.160; 0.0443 | ε = 10⁻³ (both → 0 as ε → 0) |
| (T5) sharp: z₀/ε^{1/(2−2v)} ∈ [1.269, 1.567] | 0.898 / 0.902 | — |
| L4(c) \|k₁\| ≤ (1+v)/(cos α − v) + 2.0001v | 1 − 35v | α → 0 (slack ≥ 35v, `tight.py`) |
| L4(c) tan δ ≤ 1.1396y; w₁ ≤ 1.0000015(2/α)^{2v} | 0.99991; 0.999999 | α = 0.5 |
| L4(b) w₁, arg, \|k₁−1\| ≤ 2·10⁻⁵, ρ ≥ 0.479 | 0.999997; 0.276; 0.076; 0.392 | — |
| L5(c) r; Λ; A; b/x²; r\|∂b\|/x; C/x^{2−2v}; a; x\|∂log C\| | 0.99994; 0.944; 0.99998; 0.917; 0.840; 0.817; 0.9996; 0.749 | r, Λ, b at the ends of I_η; A, a, C, ∂log C as x → 0 |
| L6(b),(c),(d) y; ψ; ρ/x; τ; \|k\| ≤ 1.0001x^{−μ}; ρ(t) ≥ 1.0136ε | 0.816; 0.593; 0.9981; 0.812; 0.9999; 0.9937 | — |
| L7(a) x_e; (c) z, y, ρ, τ, ψ, w, \|k\| ≤ 1.0001x^{−μ_T} | 0.903; 0.9999; 0.817; 0.998; 0.810; 0.607; 0.985; 0.9999 | — |
| L7(b) ρ(t_a) ≤ ε − 0.89x for x ≤ ε/2 | slack ≥ 0.11x | — |
| L7(b)/(T0) min true distance ≤ ε on (b_e, α₀) | 0.999998 | x → x_e (→ 1 by definition of x_e) |
| L7(d) y_E ∈ [ε, 1.000001ε(2.0023x_e/ε)^{v/(1+v)}] | slack ≥ 4.5·10⁻¹⁵ε; 0.999999 | v = 10⁻¹⁵ (y_E − ε ≈ 4.5vε at ε = 10⁻³) |
| L8 virtual \|ψ\| ≤ 1.69x^{1−μ}; w ≤ 1.0151 | 0.592; 0.985 | — |
| L9/L11 \|k\| ≤ 1.22; w ≤ 1.00036(2/χ)^{2v}; ρ ≥ 0.0049; ρ ≥ 0.497 | 0.820; 0.9996; 0.500; 0.9976 | \|θ − α₀\| = 0.1; hole |
| L10 \|G\|/(2y_s); \|ψ_± − arg G\| ≤ 0.58\|G\| | 0.99999; 0.862 | — |
| (iv) \|x⁰ − e^{iΘ}\| ≤ 3.74·10⁻⁶ | 0.987 | v = 10⁻⁶, θ ≈ 3.34 (= vt_s) |

The entries that print as 1.000000 in floating point (w ≥ 1, ρ₁ ≥ 1+v, y ≥ sin α, δ ≥ 0, ψ < 0 on the tail, z₀ ≥ 0,
t₂ − t_s ≤ vε/(3(1−v)²), θ_s ≥ 0, π/3 − α₀ ≥ 0, |G| ≥ 2y_s) are inequalities that are sharp in the limit v → 0; their
exact slacks are positive and of the expected order (`tight.py`: w − 1 ≥ 0.83v, y − sin α ≥ 2.9vy, ρ₁ − (1+v) ≥ 0.96y²,
δ ≥ 0.999y, θ_s = 0.750vε², π/3 − α₀ = 0.866v, |G|/(2y_s) − 1 = 1.1v, 1 − (t₂−t_s)/(vε/(3(1−v)²)) = 0.6v).

Regimes hunted, with result:
* **λ just above ε/2 at E_Y** (pairs [E_Y − λ, E_Y], [E_Y − 2λ, E_Y − λ], λ = ε/2, ε, 4ε, 100ε, x_e/2, x_e, 10x_e, …):
  N/λ^{3/2} ≤ 0.28893 (the maximum over the whole scan: ε = 10⁻²⁵⁰, λ = ε/2 at E_Y). E_Y is an ordinary point of a C^∞ arc; only the curvature factor x_e^{−μ_T} is special.
* **pairs with one or both labels in the hole, across the hole, ending at E₋, starting next to the ghost label 2π:**
  N/λ^{3/2} ∈ [0.28801, 0.28868], at all λ from ε/2 (pair entirely inside the hole) to λ₀.
* **pairs at X₀ with u_a = 0, λ/2, λ, 2.08λ, 6λ** (virtual labels included, λ from ε/2): N/λ^{3/2} ≤ 0.28885.
* **pairs straddling the X₀ side and the E_Y side:** these have λ > λ₀ and belong to (T2) only (x⁰ runs from X₀
  round the circle to E_Y; the two ends are not adjacent on the curve). c/(u_a + u′_b) ≥ 0.985, against the required 1/2.
* **v ≪ ε and ε ≪ v:** the ratios are essentially independent of (v, ε) — they are those of the unit circle; the only
  drift is the factor x^{−μ}, x^{−μ_T} (≤ 1.0009 at ε = 10⁻²⁵⁰, v = 10⁻⁶), which the claims carry as a power, and the
  (T3)–(T5) ratios, which improve as ε → 0.
* **v → 0:** every quantity converges to that of the unit circle with a straight tangent path (α_s → ε, x_e → √(2ε)-type
  root, k → 1, w → 1, y_E → ε); no bound degenerates. The hole and E_Y do not degenerate in the sense of the claim:
  the bounds are closed inequalities, uniform in v.

### 2.2 Analysis: where ε and v enter

I went through every inequality for dependence on ε (the scan cannot reach ε = e^{−1/v}, where x^{−μ} is of order e).
ε enters the proofs only through the following factors, each of which is carried as a power, never bounded by a
constant:
 (a) x^{−μ}, x^{−μ_T} (tilt, curvature, y near X₀ and E_Y) — absorbed into the exponents 1−μ, 1−μ_T, 3/2−3v; in
 (T1) through ε^{−μ_T} ≤ (2λ)^{−μ_T} (λ ≥ ε/2, x_e ≥ 1.277ε) and u^{−μ} ≤ λ^{−μ} (far case u_a ≥ λ);
 (b) (3.74/ε)^μ in Lemma 7(b) — absorbed by xε^{−μ} ≤ ε^{1−μ}/2;
 (c) (2.0023x_e/ε)^{v/(1+v)} ≤ (3.14ε^{−1/2})^v in y_E — absorbed in (T5) by ε^{1/4−v/2−μ/2} ≤ 1;
 (d) (2/χ)^{2v} in w near the axis — integrable, enters only U and "l ≤ 1.0152 max(Δ, 0.02)";
 (e) e^{2vI/ε}, e^{vI/ε} with I ≤ ε/(1−v) in Lemma 8 — ε cancels.
I re-derived the constants of the steps where a power of x or ε is compared with a number (L6(c): y/x ≤ 0.06125;
L6(d): 0.3081x^{1−μ} ≤ 0.0309, 2.3156x^{−μ}; L7(a): 1.277, 1.566; L7(c): 32.45, 2.002, 4.9064, 39.24, the exponent
identities (2−v)/(1+v) = 2 − μ_T and (1−2v)/(1+v) + 2 = 3/(1+v); L7(b): ρ(t_a) ≤ ε − 0.89x; (T1): 0.353, 5.3,
5.4·40^{−1/2+3v} ≤ 0.86; (T2): 0.0246, 0.0245, 0.999u_a + 0.979u′_b; (T4): 1.2514, 1.4882, 0.473, 3.23 ≤ 3.3; (T5):
3.5ε^{3/4+μ/2}; U ≤ 6.489; Lemma 9(c): 1.000013, 1.0152): all correct and all monotone in the right direction
on 0 < x ≤ 0.1, 0 < ε ≤ 10⁻³. In each of them the worst case is at the *large* end (x = 0.1, ε = 10⁻³, v = 10⁻⁶), which
the scan covers. The (T1) dichotomy "u_a ≥ max(λ, 1.04ε)" / "u_a < max(λ, 1.04ε) ≤ 2.08λ" is exhaustive and the near
case stays in the forward zone (u_b < 3.08λ ≤ 0.077). (T2): pairs with u_a + u′_b < 2c_sep are automatically wrap
pairs (λ = U − u_a − u′_b > λ₀), and the two cases Δ ≤ 2π − 0.0246, Δ > 2π − 0.0246 are exhaustive.
Only slip found: F2.

## 3. SEMANTICS

* **True front through the hole.** Well defined for every label α ≠ 0 (ρ ≥ C/g_max > 0 on both runs; b ∈ (0,π) on
  run 2 — I checked b = β₁ − β* resp. 2π − β₁ − β* numerically on all labels used). At the ghost label the limit
  Z₁ = P(t₁) − (1+v) exists (|S_α(t₁) − Z₁| ≤ 1.01(y + 1 − cos α): ratio 0.9901), the arc is continuous and injective
  (Im ∂_αS > 0 on the upper arm since δ ∈ [0, π/2); numerically strictly monotone projection), C¹ with tangent i at Z₁,
  curvature bounded on both sides — C^{1,1}. The flow map of run 2 is a diffeomorphism near 1 (distance ≥ 0.497 from
  Harry: ratio 0.9976), so the same holds at t_s. Lemma 11 is correct (with F3). The stretch w ∼ (2/|α|)^{2v} is
  unbounded at the ghost label, so x⁰ is not C¹ *in the label* there, only in arclength — which is all (H_T) asks.
* **Hole labels seen.** Exact: min ρ on run 1 is g(α)/g_max, ≤ ε iff |α| ≤ α_s (the minimum point cos β = v is passed
  before t₁ because cos β₁ < −v). OK.
* **Labels strictly between E_Y and α₀.** Seen by t_s: for x ∈ [0.35vε, x_e], C ≤ εg_max and h(t_s) ≤ 0 (the
  minimum point is passed in run 2); for x ∈ (0, ε/2], ρ(t_a) ≤ ε − 0.89x. The two ranges overlap (0.35vε < ε/2 ≤ x_e).
  Scan: min true distance/ε ≤ 0.999998 on a grid from x = 10⁻⁶vε up to x_e(1 − 10⁻⁶). OK.
* **Forward labels (α₀, α₀ + 1.02ε).** (T0) is settled by the definition of 𝒢 (ghost iff the true candidate has been
  within ε); a non-ghost label there has virtual = true by [B, Lemma VC(c)]. Correct, and nothing has to be computed.
  x ≥ 1.02ε never enters the disc (min over run 2 of ρ/ε ≥ 1.0200; claimed ≥ 1.0136).
* **t_s and the path.** t_s = t₁ + (ρ₀−ε)/(1−v) + ε·atan(√(v/(1−v)))/√(v(1−v)) depends on (v, ε) only; P is two unit-speed
  segments, 1-Lipschitz, fixed in advance; û is fixed at t₁ from the exact state of the candidate α₀. The virtual
  candidate α₀ of [B] is at P(t_s) at t_s (ODE residual 10⁻²⁴ε), and 0 < t₂ − t_s ≤ vε/(3(1−v)²).
* **The label u = 0** is necessarily a ghost — see F1.
* **Injectivity of x⁰** is neither claimed nor required by (H_T); it holds ((T1), (T2) give c > 0 for λ ≥ ε/2, and
  on shorter scales the tangent has the moduli (i)–(iii)).

## 4. INTERFACE with (H_T) of `referee/P8b-claims.md` §5, item by item

| item of (H_T) | P8a | finding |
|---|---|---|
| constants v_T, ε_T ∈ (0,1); T₂, U_max ≥ 1; a′ ∈ (0,1]; C₀, C_z > 0; λ₀ ∈ (0,1/4]; c_sep ∈ (0,1]; γ_T ∈ (0,1/4]; ϑ_T > 0; G_T ∈ (0,1] | 10⁻⁶, 10⁻³; 3.74, 6.5; 1/2; 0.86, 1.57; 1/40; 0.024; 1/4; 3.3; 0.05 | all in the admissible ranges |
| t₂ (P8b) = time when the virtual candidate α₀ is at distance 0 | = t_s (P8a); P8a's own t₂ is the true catch time | same object; notation clash only, stated in both files |
| t₂ ≤ T₂ | t_s ≤ 3.7321 | OK |
| n̂ unit vector | û = heading of run 2 | same |
| x⁰ C¹, \|∂_u x⁰\| ≡ 1, 1 ≤ U ≤ U_max | arclength parametrisation of Y; U ∈ [2 − 7.5·10⁻⁶, 6.489] | OK |
| u = arclength from X₀ at t₂; u′ = U − u; λ = u_b − u_a; N = (2E)^{1/2}, E = l − c at time t₂ | same | same |
| (T0) x⁰(0) = P(t₂) | yes | OK |
| (T0) "𝒢 ⊂ (0,U)" | 𝒢 ∋ 0 | **F1** |
| (T0) every u ∉ 𝒢 true; every direction seen or direction of a true label | proved; hole labels are *true* (and seen), only Θ = 2π and the seen part of [α₀, α₀+1.02ε) are ghosts | OK. Differs from P8b's "intended realisation" (𝒢 = hole labels ∪ [α₀, α₀+1.02ε)), which is not part of (H_T); P8a's 𝒢 is smaller, both choices satisfy (T0) |
| (T1) with "C₀λ₀^{a′} ≤ 1" | 0.86·40^{−1/2} = 0.136 | OK |
| (T2) c ≥ min(c_sep, (u_a + u′_b)/2) for λ > λ₀ | same | OK |
| (T3), (T4) with max(·, ε/2)^{γ_T}, for u resp. u′ ≤ G_T | same | OK |
| (T5) P(t₂) − x⁰(U) = z₀n̂ + y₀n̂^⊥ (a^⊥ = ia), 0 ≤ z₀ ≤ C_zε^{1/4}, \|y₀\| ≤ ϑ_T(z₀+ε)(ε/2)^{γ_T} | z₀ = −z_E > 0, y₀ = −y_E < 0 | OK (signs checked against P8b (D0) with û_D = −n̂) |
| D₁ ∈ (0,1] fixed | D₁ = 1 only | restriction, see F4 |

No difference in arcs, scales or constants other than F1. P8b's derived constants are computed from the values above
(P8a §9 Remark (3)); P8b Remark (4) should be updated (F4).

## 5. Small remarks (no action needed)

* Lemma 10 is not used in the proof of the theorem (Lemma 11 supersedes it).
* The constants are far from sharp, as announced: the true values are those of the unit circle (N/λ^{3/2} = 1/√12,
  tilt slope 1, x_e = √2·ε^{1/2}); the only genuinely non-circular features are the exponents −μ, −μ_T of §1.
