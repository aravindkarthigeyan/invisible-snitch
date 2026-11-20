# Referee report RP6d-1 — `referee/P6d-claims.md` (start S ⇒ (ST)) and Claim 1 of `referee/P6c-claims.md`

Independent, adversarial. Read: `referee/P6d-claims.md` (all), `referee/P6c-claims.md` §0 + Claim 1 (all parts),
`referee/P6a-claims.md` (all; Theorem B assumed), `paper/main.tex` Prop. `prop:integrals`, Lemma `lem:k`,
`referee/P6a2-claims.md` (only the statement of (ST⁺)). Not read: `reports/P6d-1.md`, `reports/P6c-1.md`, `code/P6d`, `code/P6c`.
Own code: `code/referee/P6d_1/` (`front0.py`, `check_claim1.py`, `check_claim1b.py`, `sim_startS.py`, outputs `*.out`, `sim_*.json`).

## Verdicts

| Statement | Verdict |
|---|---|
| P6c Claim 1 (a) | OK |
| P6c Claim 1 (b) | OK |
| P6c Claim 1 (c) | OK |
| P6c Claim 1 (d) | OK |
| P6c Claim 1 (e) | OK with fix F1 (wording: which virtual field) |
| P6c Claim 1 (f) | OK |
| P6c Claim 1 (g) (not cited by P6d) | OK |
| P6d Lemma D0 (a),(b),(c) | OK |
| P6d Claim D1 | OK |
| P6d Claim D2 (a),(b),(c) | OK |
| P6d Claim D3 (a),(b),(c) | OK (fix F2, cosmetic) |
| P6d Theorem D, items 1–6 and "(ST) holds" | OK |
| P6d Corollary D | OK with fix F3 (it uses the general-path clause of Corollary M; say so) |
| P6d Remark (1), "(ST⁺) of Theorem F holds for the start S" | GAP G1 (a remark, not in the PROVED list; not a verbatim match) |

No FALSE statement found. No gap found in anything on the "Claimed PROVED" list.

## 1. Claim 1 of P6c (re-derived from the integrals)

Integrals re-derived from r' = v r̂ − u: ρ' = v − cos β, ρβ' = sin β; h' = (v − cos β)(cos β + v) − sin²β = −(1 − v²);
(log ρg(β))' = 0 with g'/g = cot β − v/sin β. Agrees with `paper/main.tex` (59–92).

* (a) h(0) = cos α + v, (1 − v²)t_0 = 1 + v ⇒ h(t_0) = −(1 − cos α); C = g(α). β ∈ (θ*, π) and ρ ≥ g(α)/g(θ*) follow. OK.
* (b) Differentiated both identities independently; obtained the same ρβ_α = sin β·tan(α/2)/(1 − v) and
  ρ_α = ρ(cos α − v)/sin α + (v − cos β)tan(α/2)/(1 − v). Checked against a direct ODE integration of the true dynamics
  (DOP853, v ∈ {0.3, 0.1, 0.01}, α ∈ {0.05,…,3}): |z_formula − z_ode| ≤ 2.5·10⁻¹⁴, |z_α − FD| ≤ 6.3·10⁻⁹. OK.
* (c), (d): algebra rechecked (2 sin²(α/2)/g(α) = tan^{1+v}(α/2); g(α) = (1 + cos α)tan^{1−v}(α/2)); numbers rechecked
  (0.69982, 1.4289 < 1.43, 0.7223, 1.43·0.533 = 0.762). mp scan (40 digits, α from 5·10⁻¹⁶ to 1/2): 0 violations of the four
  inequalities; sup tan φ/ρ = 0.42 (v = 0.1), 0.515 (v = 10⁻³) ≤ 0.77; α^vσ/limit = 1.000000000000 at α = 5·10⁻¹⁶. OK.
* (e) Proof correct. The candidate α_s touches ρ = ε exactly once (at bearing arccos v), others in (α_s, 2π − α_s) stay
  strictly outside. ODE check: min ρ/ε on [0, t_0] = 0.9990…0.9993, 1.0000000, 1.0007…1.0010 for α = 0.999α_s, α_s, 1.001α_s.
  So the seen set at t_0 is exactly {|α| ≤ α_s}. **Fix F1** below.
* (f) Rechecked: g_max²(1/4) = 1.0652, c_s ≤ 0.357, 1.25^{0.25} = 1.0574, 0.643^{−0.625} = 1.318, product 1.394 < 1.4.
  mp scan (v from 10⁻¹² to 1/4, ε from 10⁻⁹ to 1/20): sup ρ_s/ε = 1.1375, inf ρ_s/ε − 1 > 0 (10⁻¹⁹ at v = 10⁻¹², ε = 10⁻⁹).
* (g) OK (2(π − θ*) = π − 2 arcsin v; bearing strictly increasing confirmed numerically).

**The corner at t_0.** As α → 0±, β → ±θ*: the true front has a corner at O = P(t_0) with turning angle 2 arcsin v, and
σ ~ α^{−v}. All labels |α| < α_s (the corner and the part of both arms inside radius ρ_s) are behind the base. (ST) is
about the arc [α_s, 2π − δ/2] only (Theorem B: labels u ∈ [0, U] measured from the base a_{j_s}); it says nothing about
labels in [0, α_s), which is consistent with Theorem B (every estimate for a pair involves only the arc from the base to b).
At t_0 no label of [α_s, 2π − α_s] is inside the ε-disc (ρ ≥ ρ_s > ε); labels of the arc enter the disc only during the
connector, which Claim D3 treats with the C¹ field.

**Virtual versus true field up to t_0.** Both the field x/max(|x|, ε) of P6c §0 and the C¹ field of P6a equal x/|x| on
{|x| ≥ ε}; by (e) the candidates of [α_s, 2π − α_s] stay in that closed set on [0, t_0], so they solve all three
equations and coincide (uniqueness for the Lipschitz virtual fields). The virtual front is C¹ in the label, so its tangent
at the endpoint α_s is the one-sided tangent of the true arm. Correct.

## 2. Lemma D0, Claims D1, D2

* D0(a): T^⊥·AT = (f' − f/ρ)(T^⊥·r̂)(T·r̂), f/ρ − f' = ρ/ε² inside, 1/ρ outside. OK. (b) DF is globally Lipschitz
  (x xᵀ/|x| is homogeneous of degree 1); OK. (c) OK (needs kl ≤ π, as stated).
* D1, arm: all eight terms recomputed with exact constants: 0.6201, 0.1843, 0.7147, 0.1894, 0.0072, 0.1862, 0.0548,
  0.2146; sum 2.171 < 2.2. The identity for A_α was re-derived (c'² − 1 + v cos α = −sin²α − vc'). Every bound is uniform
  as α → 0 (ρ ≥ g(α) and τ^{2v}, τ^{1+3v}, τ^{2+4v} ≤ 1) and as v → 0 (no lower bound on v is used); ε does not enter
  (statement about the true front). Middle: 2/0.479 = 4.175, 1/0.479² = 4.358, 2.05e^{0.0423} − 1.05 = 1.0886. OK.
  Numerically (mp, 40 digits, α from 10⁻⁴⁰ to π, v ∈ {10⁻¹², 10⁻⁶, 10⁻⁴, 10⁻³, 10⁻²}): sup|κ| = 1.0000 … 0.9913 (the front
  is a v-perturbation of the unit circle), sup tan(ψ − β)/ρ = 0.516 ≤ 0.63. The true constant is ≈ 1, the claimed 2.2 is safe.
* D2: constants recomputed (0.8622, 1.5144 ≤ 1.52, 6.8189 ≤ 6.82, e^{2.109v} ≤ 1.00211). (c): case split and the
  bound 2 sin(Δ/2) − 2.004v ≥ 0.49δ correct. Numerically sup σ(α/2)^v ≤ 1.0000, sup σ (middle) ≤ 1.00104 (v = 10⁻³).

## 3. Claim D3 (connector)

Checked line by line.
* Step 1. h_s formula and |h_s| ≤ 2|sin φ|/m² + k/m correct (|Γ'| ≤ 1/m² on both sides of ρ = ε; Γ/ρ = 1/m²). h is
  Lipschitz in s also through ρ = 0 (degree-1 homogeneous inside the disc) and through ρ = ε (Γ Lipschitz), so the pair
  inequality only needs the a.e. bound; the change of form of the field at ρ = ε costs nothing. (*) and the continuity of K
  are correct (K(t_s) < ∞ by D0(b)).
* Step 2. The mechanism is right: Harry runs along u, which makes the angle |φ_s| ≤ 0.9ε with the arm's tangent at the base,
  and the arm is K-Lipschitz, so |p| ≤ Kl²/2 + d(Kl + |φ_s|) and |sin φ| ≤ (3.6K + 0.9)m(ρ) at all scales, including
  ρ ≪ ε. Constants: cos 1 = 0.5403, 1/0.54 = 1.852, 1.86²/2 + 1.86 = 3.59. Far case: 0.124·2/π = 0.0789, 1/0.07² = 204.1.
* Step 3. 1.402·34.6 = 48.51, 575ε/δ² ≤ 0.09; total ≤ 48.6v ≤ 49v. Bootstrap correct.
* **Fix F2 (cosmetic).** In Step 2 "|φ_s(τ)| ≤ |φ_s(t_0)|e^{1.402v}" add "(|φ'| ≤ vΓ(d)|φ| ≤ (v/ε)|φ| and τ − t_0 ≤ 1.402ε)".

Numerically (below) the slope of ψ against arclength changes during the connector by at most 0.50 v (attained at the base),
against the claimed 49v.

## 4. Theorem D, Corollary D; match with Theorem B

Items 1–6 recomputed: α_s ≤ 2εg_max (sim: α_s/ε ∈ [0.86, 1.0004]); t_s ≤ 1.001001 + 2.8·10⁻⁵ ≤ 1.0011 (uses ε ≤ R/64 ≤ 1.98·10⁻⁵);
2.25²/24 = 0.2109 ≤ κ² = 1/4, 2.25·1.39 ≤ π; (2/π)·0.997·32 = 20.3 ≥ 16 and 0.48δ ≥ 48R; κR ≤ 1/1584; 6.82e^{3v} ≤ 6.841;
tail (2π − α_s, 2π]: w ≤ ε^{−μ}e^{4.82v}, α_s ≤ 2g_max^{1+μ}ε^{1+μ}, length ≤ 2.01ε. OK.

(ST) verbatim: base a_{j_s} = α_s with P(t_s) = x_{α_s}(t_s) (D3(a)); arc [a_{j_s}, b*] with b* = 2π − δ/2; pairs = all pairs
of that arc, λ = l_{t_s}(a,b); (IC1) is proved for all λ ≤ 1.39 ⊃ [ε/2, 32R]; (IC2) for λ > 32R; (IC3). U ≤ 6.85, T_s = 1.0011,
L_s = 6.9 ≥ R_{j_s}; v(4U + 2) ≤ 29.6v ≤ 10⁻⁶R. Corollary M then needs b' = 2π − δ (U − u_{2π−δ} ≥ δ/2 ≥ ε/2: yes) and
ε₀ ≤ min(δ, R/64): yes. Role of δ: only D2(c)/(IC2) (chord ≥ 0.49δ needs b ≤ 2π − δ/2; R ≤ δ/100) and the far case of D3.
The labels (2π − δ/2, 2π] are not covered by (ST) and go entirely into hypothesis (T), which stays unproved (correctly stated).

**Fix F3 (Corollary D).** Replace "This is Corollary M of P6a verbatim" by: "This is Corollary M of P6a in its
general-path form (the clause 'or any 1-Lipschitz path fixed in advance such that …'). Theorem B and Theorem R are stated
for construction C, but their proofs use the path only on [t_s, ∞): Lemma VC, Lemma C(0),(2),(3),(4) for the legs after
j_s, and (ST)." I checked this reading of Steps 1–5 of Theorem B and of Theorem R; nothing before t_s is used.

**Gap G1 (Remark (1) only).** Theorem F of P6a2 is set in construction C_cut, with t₀, O and r_a those of C_cut
(t₀ = 1/(1 − v) − εs₀) and with external inputs (Lemma G, Claim 8 of P6c) proved for that path. Start S is a different
path before t_s, so "(ST⁺) holds for the start S with m = 2" is a statement about a re-read Theorem F, not a verified
hypothesis. Either restate Theorem F for "any path with a corner at O at time t_0 …" and re-prove Lemma G/Claim 8 for
start S (Claim 1 gives the geometry with η = 0), or mark Remark (1) as not proved.

**Fix F1 (P6c Claim 1(e) and P6d external inputs).** Add: "The conclusion x_α = S_α on [0, t_0] holds for every virtual
field equal to x/|x| on {|x| ≥ ε}, in particular for both x/max(|x|, ε) and the C¹ field of P6a."

## 5. Independent simulation of start S (`sim_startS.py`)

Method: front at t_0 from the closed forms in mpmath (40 digits; x = −(cos β + v) solved from
x = tan^{1+v}(α/2)(1 − v − x)^{(1+v)/2}(1 + v + x)^{(1−v)/2}); connector integrated in mpmath RK4 (240 steps) in coordinates
scaled by ε, for position and ∂_αx with the C¹ field; base ends at distance < 3·10⁻¹³ε from Harry. 1116–1259 labels on
[α_s, 2π − δ/2]: geometric from 10⁻³ε (24 per decade), uniform step 0.02ε up to 8ε, uniform step 0.01 in α. Tangent-angle
differences taken in mpmath before conversion; E from E = (2lD − D² − S²)/(l + c), D = ∫(1 − cos θ), S = ∫ sin θ (no
cancellation); all pairs. K = sup slope of ψ against arclength.

| v | ε | δ | ρ_s/ε | K(t_0) | K(t_s) | slope change /v | sup E/λ³, ε/2 ≤ λ ≤ 32R | sup E/λ³, λ < ε/2 | min chord/R, λ > 32R |
|---|---|---|---|---|---|---|---|---|---|
| 10⁻¹² | 10⁻², 10⁻³, 1.5·10⁻⁴, 1.9·10⁻⁵, 10⁻⁶ | 1 | 1.000013 … 1.000000 | 1.00000 | 1.00000 | below float resolution | 0.04167 | 0.04167 | 32.0 |
| 10⁻⁶ | same five | 1 | same | 1.00000 | 1.00000 | 0.499 | 0.04167 | 0.04166–0.04167 | 32.0 |
| 10⁻³ | 10⁻² | 1 | 1.000024 | 0.99913 | 0.99912 | 0.495 | 0.04159 | 0.04159 | 32.0 |
| 10⁻³ | 1.9·10⁻⁵ | 1 | 1.000002 | 0.99913 | 0.99913 | 0.489 | 0.04159 | 0.04038 | 32.0 |
| 10⁻³ | 10⁻⁶ | 1 | 1.000002 | 0.99913 | 0.99913 | 0.486 | 0.04159 | 0.03990 | 32.0 |
| 10⁻⁴ (= 10⁻³δ) | 1.5·10⁻⁶, 10⁻⁶ | 0.1 | 1.000000 | 0.99991 | 0.99991 | 0.498 | 0.04166 | 0.04149 | 32.0 |
| 10⁻¹³ | 10⁻⁶ | 0.1 | 1.000000 | 1.00000 | 1.00000 | below float resolution | 0.04167 | 0.04167 | 32.1 |
| 10⁻² (outside hyp.) | 1.9·10⁻⁵, 10⁻⁶ | 1 | 1.0002 | 0.99125 | 0.99125 | 0.41, 0.38 | 0.04094 | 0.030, 0.027 | 32.0 |

(ε = 10⁻², 10⁻³, 1.5·10⁻⁴ with δ = 1 are above ε₀ = 1.97·10⁻⁵; shown for the trend.) Lengths l_{t_s}(α_s, 2π − δ/2) = 5.783–5.788
(δ = 1), 6.234 (δ = 0.1); with sup σ ≤ 1.00104 the full length is ≤ 6.29 ≤ 6.82. Angle of u to the base tangent at t_0:
0.49–0.50 ε (claimed ≤ 0.882ε).

Reading: measured tangent Lipschitz constant ≈ 1 (claimed ≤ 2.25), sup E/λ³ ≈ 1/24 (claimed ≤ 0.211, needed ≤ 0.25),
chords ≥ 32R (needed ≥ 16R), all uniform in ε down to 10⁻⁶ and in v down to 10⁻¹³, with no feature at the scale ε or at the
disc boundary. Limits of the test: the slope-change column for v ≤ 10⁻¹² is below the float resolution of the stored
slopes (the totals K are reliable); the quadrature of arclength is trapezoidal (chord cross-check relative error ≤ 6·10⁻⁷);
the D2(b) length integral in `check_claim1*.py` returned nan (root bracket near α = π) and was replaced by the simulation
lengths above.

## 6. Summary of required text changes

* F1: sentence on the virtual field in Claim 1(e) / P6d external inputs (above).
* F2: parenthesis in D3 Step 2 (above).
* F3: Corollary D proof wording (above).
* G1: Remark (1), sentence "(ST⁺) of Theorem F there holds for the start S with m = 2" — not established as written.
