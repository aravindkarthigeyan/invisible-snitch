# Referee report RP6e-1 — `referee/P6e-claims.md` (Lemmas E1–E3, Proposition E4, Theorem E, Corollaries E5–E7) and its unrefereed inputs

Referee: independent, adversarial. Not read before the verdict: `reports/P6e-1.md`, `code/P6e/`.
Read in full: `referee/P6e-claims.md`, `referee/P6a2-claims.md` (Corollary N), `referee/P6c2-claims.md` (Claim 14),
`referee/P6c-claims.md` §0, Claim 1, Lemma G, Claim 8; `referee/P6d-claims.md`; `paper/sec_B.tex` (all), `paper/sec_ST.tex`
(statements and the proof of Theorem ST / Corollary ST). Assumed (doubly refereed): Theorem B and Construction C, the front
at first contact, start S, Theorem ST.
Code of this report: `code/referee/P6e_1/` (`e3_test.py`, `e1_check.py`, `e4_window.py`, `sim_arm.py`, `front.py`, outputs `*.out`, `out_*.txt`, `sim_*.json`).

## 0. Verdict

| Claim | Verdict |
|---|---|
| Lemma E1 (arm at t_0) | **OK** (all constants re-computed; numerically the true constants are ≈ 0.50, 0.50, 1.00, 1.001 against 0.51, 0.63, 1.13, 1.133) |
| Lemma E2 (heading modulus) | **OK** (given Theorem B for the path "start S + legs"; uses the proof-internal (TL), Step 1(a) of Theorem B — see fix F3) |
| Lemma E3 (law of η, ζ) | **OK** — re-derived by hand; confirmed numerically to 6·10⁻³⁶ (40-digit arithmetic, kinked paths, arbitrary labels) |
| Proposition E4 (window, saturated propagator) | **OK with one cosmetic fix** (F4: 0.633 → 0.6332; no effect on any conclusion) |
| Theorem E | **OK with fixes F1–F3** (wording/justification only; statement and constants stand) |
| Corollary E5, E6, E7 | **OK** |
| Corollary N (P6a2), as used | **OK with fix F2** (reading of t_0, O for the start S; constant K) |
| Claim 14(a) (P6c2), as used | **OK** (re-derived; confirmed numerically to 10⁻³⁶) |
| "G2 computation" (P6c), case η = 0, as used | **OK** (re-computed: ρ(0.2) − ρ(0.1) ≥ 0.0671; numerically 0.0997) |
| Validity of the refereed inputs for C_cut | **OK**, by the coincidence argument F1; nothing has to be re-proved for Theorem E |

No FALSE statement and no GAP found. I could not break the central mechanism (no r^{−cv} loss, uniformity in ε); see §3.
Caveat on scope (not a defect of the proof): the theorem's non-trivial regime (Case II, r < r_2 ≈ 10⁻¹² v⁵, i.e. ε ≲ 10⁻⁷³ at
v = 10⁻¹²) is inaccessible to direct simulation; it was tested only through the scaled window problem (§4.3).

## 1. Fixes (exact text)

**F1 (C_cut; add to §0 of P6e-claims, replacing the sentence "Then the legs of construction C … with end label b_e").**
> *Lemma (C and C_cut coincide up to the entry time).* Let the legs after t_s be run with end label 2π (construction C) or
> with end label b_e = 2π − α_s (C_cut). The leg rule a_{j+1} = max{θ ∈ [a_j, end] : l_{t_j}(a_j, θ) ≤ ε} gives the same
> a_{j+1} for both as long as l_{t_j}(a_j, b_e) > ε. Since |∂_θx| ≥ 1 (Lemma B-VC(a)), l_{t_j}(a_j, b_e) ≤ ε forces
> a_j ≥ b_e − ε ≥ 2π − 3.1ε > 2π − δ/2. Hence the two paths (and therefore all virtual candidates) coincide on [0, t_J],
> where t_J is the first leg start with a_J ≥ 2π − 3.1ε; in particular on [0, t_e], and on every leg with u_{a_{j+1}} ≤ U
> (U = l_{t_s}(α_s, 2π − δ/2)). Consequently Lemma B-C(2),(4), Theorem B with Steps 1, 2 of its proof, Theorem ST and
> Corollary N hold verbatim for C_cut on these legs, and Theorem E is a statement about "start S + construction C" as
> well. (Theorem R for C_cut is **not** covered by this argument and is not used here.)

Checked: every refereed result invoked in P6e (Lemma B-VC, Lemma B-1(i),(ii),(iii), Lemma B-C(2),(4), Theorem B: (I1),
(I2), (CA), (IC2) at t_s, Step 1(a),(b), Step 2 (TL); Theorem ST items 1–6; Lemma ST-D1, ST-D3 Step 2) is used only for
t ≤ t_e or for legs with u_{a_{j+1}} ≤ U − R, where the two constructions are literally the same path. Theorem B for the
path "start S, then legs" (rather than construction C from t = 0) is the general-path reading already refereed in the
proof of Corollary ST ("their proofs use the path only on [t_s, ∞)"); I re-read Steps 1–5 of Theorem B with this in mind
and agree.

**F2 (Corollary N for the start S; replace the first Input bullet on P6a2 by).**
> Corollary N of P6a2 is applied with t_0 := 1/(1 − v), O := P(t_0), r_a := |x_a(t_0) − O| (in P6a2 these symbols denote
> the end of leg 0 of construction C; the proof uses them only through t_s − t_0 ≤ mε, r_{a_{j_s}} ≤ mε, |x_a'| ≤ v and the
> triangle inequality c(a_{j_s}, a_j; t_0) ≤ r_{a_j} + r_{a_{j_s}}). For the start S: t_s − t_0 ≤ 1.402ε and
> r_{a_{j_s}} = ρ_s ≤ 1.4ε (Theorem ST, item 2), so m = 2; (ST) holds at t_s on [α_s, 2π − δ/2] (Theorem ST), v ≤ 10⁻¹²,
> v(4U + 2) ≤ 2.94·10⁻¹¹ ≤ 10⁻⁶R. K = max(2, U/(16R)) ≤ 6.85/0.016 = **428.125** (not "≤ 428.2": with 428.2 the formula gives
> C_A = 2584.05 > 2584), so C_A = 2.01·K·3 + 2 ≤ 2583.6 ≤ 2584. The clause "for j ≤ j_s" of Corollary N is void for the
> start S (there are no legs before j_s; the connector is treated separately in Theorem E).

So the hypothesis "(ST) holds at a leg start within mε of first contact" **is met by the start S verbatim** (m = 2). I
re-checked the proof of Corollary N line by line: (i) uses (I1) for the family pair (a_i, s), u_s = u_{a_i} + ε/2 ≤ U at
t_i (inside the range of Theorem B since u_{a_{i+1}} ≤ u_{a_j} ≤ U); (ii) uses (CA) for u ≤ 32R and (IC2) for u > 32R;
(iii) is the speed bound. Correct. It is applied in P6e only to leg starts with base ≤ 2π − 0.2, where u_{a_j} ≤ U − 0.15.

**F3 (Lemma E2; add one sentence).**
> (TL) and Step 1(a) are statements inside the proof of Theorem B (made there under the bootstrap hypothesis (I1), (I2));
> since Theorem B is proved, (I1), (I2), (CA) hold at all times of the legs considered, hence so do (TL) and Step 1(a).

(Recommendation for the paper: state (TL), Step 1(a),(b) and (∗) as a corollary of Theorem B.)

**F4 (Proposition E4(v), cosmetic).** 0.63/0.996/(1 − ν) = 0.63316 for v = 10⁻³; write "0.6332 r" instead of "0.633 r"
(twice; Corollary E7 likewise). The next line becomes (1.133 r + 0.6332 vr + …)/(3.7v) ≤ 0.3064 r/v + …, still ≤ 0.307 r/v.

**F5 (editorial).** (i) The header lists Corollary E5 twice. (ii) Lemma E1(b): the proof gives 0.503 ρ; the statement 0.51 ρ
is fine. (iii) Theorem E, "never were in the ε-disc": add "the same holds for all labels with r ≥ 4ε (ρ ≥ 0.99(D + r) − 2ε
> ε), so a label-neighbourhood of every point with r ≥ 16ε consists of true candidates and the front is C^∞ there."
(iv) Proposition E4 assumes "unit speed" but uses only |P'| ≤ 1 and (H1).

## 2. Line-by-line check (what was verified)

**Lemma E1.** (a) g(0.1) ≤ 0.10287, g(β) ≥ 0.997 → ρ(0.1) ≤ 0.1032. (b) −(cos β + v) = g(β) tan^{1+v}(α/2) ≤ 0.5013ρ;
β − θ* ≤ 0.503ρ. (c) Lemma ST-D1 (refereed). (d) the eight terms: 0.51403, 0.02638, 0.52186, 0.00528, 0.00522, 0.02664,
0.00135, 0.02705; sum 1.1278; ×1.0022 = 1.1303 ≤ 1.133. (e) orientation: T is the direction of increasing r (= increasing
α = decreasing label on the left arm); ψ = −β − φ_0, φ(0) = φ_0, b_∞ − ψ = 2 arcsin v + (β − θ*) + φ_0. All correct.
Numerics (`e1_check.out`, 40 digits, α ∈ [10⁻¹⁵, 0.1], v ∈ {10⁻¹³, 10⁻¹², 10⁻⁶, 10⁻³, 10⁻²}): sup(β − θ*)/ρ = 0.5002,
sup m/ρ = 0.5006, sup|κ| = 1.0000, sup|Q_0|/ρ = 1.0013; identity (e) to 10⁻²⁰…10⁻³¹; Claim 1(b) (A, B) against numerical
differentiation of the closed form: 1.7·10⁻¹⁹; ρ monotone.

**Lemma E2.** (a) Membership of every pair in the family 𝔉(t) at the time used was checked: (1) I = (a_i, a_{j+1}), J_i, J_j
at t_i; (2) I' = (a_j, b') at t_i (first label ≥ a_{i+1}, u_{b'} ≤ U by u_{a_{j+1}} + R ≤ U); (4) I' at t_j; (3) at t in
leg k+1, I'' = (a_k, b') (length ≤ 2λ ≤ R/50), J_k, (a_{k+1}, a) and I' are family sub-pairs of I''. θ = 182M(2λ)^{1/4} ≤ 0.489;
|Π_e r̂| ≤ θ/(1 − θ²/2) ≤ 1.14θ; |e'| ≤ 4.6vθ/λ; t_j − t_i ≤ 4λ; rotation ≤ 18.4vθ ≤ 3.4·10³ v M λ^{1/4} ≤ Mλ^{1/4}. Sum 365.
(b) 0.9ε (ST-D3, Step 2; φ_s is the angle between u and T_{α_s}) + 2.25ε (Theorem ST item 3 on an arc of length ε) and
0.51·1.4ε. (c) legs last ≥ c ≥ ε/4 by (CA); 365·4^{1/4} = 516.2; 3.87ε ≤ 3.8M(2ε)^{1/4} iff ε ≤ 0.0169. Correct.
Simulation (§4.2): the first headings deviate from u_0 by ≈ 0.5ε, 1.5ε, 2.5ε, 3.5ε (claimed ≤ 0.72ε, ≤ 3.87ε, …) and
sup|P' − u_0|/(τ + ε) ≈ 0.96–1.0 over the whole sweep, i.e. the true modulus is Lipschitz; the claimed 520M(τ+2ε)^{1/4}
is ≥ 13 times larger everywhere.

**Lemma E3.** Re-derivation: with 𝔇 = r∂_r + τ∂_τ, [∂_τ, 𝔇] = ∂_τ; y = x − P; ∂_τ(𝔇x) = (v/ρ)Π(𝔇x − τP') + v r̂;
𝔇x − τP' = η + y − p, Πy = 0 ⇒ ∂_τη = (v/ρ)Π(η − p). For ψ: ∂_τψ = Ψ(y, ψ) = −(v/2|y|) sin 2(arg y − ψ), ∂_ψΨ = (v/ρ) cos 2φ,
∇_yΨ = (v/2ρ²) sin 2φ r̂ − (v/ρ²) cos 2φ n, ∇_yΨ·y = −Ψ ⇒ ∂_τζ = (v/ρ) cos 2φ ζ + ∇_yΨ·(η − p); |∇_yΨ| ≤ v/ρ². Initial values
correct. Only P' (not P'') enters, η and ζ contain no P': continuous across kinks. **Numerical test** (`e3_test.py`,
`e3_test.out`): x, ∂_r x, ∂_r²x integrated with the true flow and its first and second variational equations (derived
independently), together with η, ζ (claimed laws) and Q (Claim 14(a)); Bulirsch–Stoer in 40-digit arithmetic; path with
curvature and a kink at τ = 0.4; three initial curves (one with a label that is not a radius); v ∈ {0.3, 0.05, 10⁻³};
36 comparisons of "definition" against "integrated law": **worst discrepancy 5.9·10⁻³⁶** (η: ≤ 9·10⁻³⁷, ζ: ≤ 1.2·10⁻³⁶,
Q: ≤ 5·10⁻³⁷). (A first run showed 10⁻¹⁹; this was my own inconsistent binary constant 0.52 ≠ 0.4·1.3 in P', i.e. the test
does detect a 10⁻¹⁷ error in P'.)

**Proposition E4.** (i) −cos(β + θ*) ≥ 0.99999; (x − P)·(−u_0) ≥ τ(1 − 1.025v) + 0.99999r ≥ 0.998(r + τ); ν = 1.0021v ≥ v/0.998.
(ii) ℓ_x' = (v/ρ)(ℓ_x − ℓ_P), ρ sin e = −(ℓ_x − ℓ_P); the constants 2.0006, 39.8, 2.0047, 0.0252, 0.02506, 0.03136 and
0.0880 are right. (iii) Phase A: Δ ≤ 4.05v(32^ν − 1) ≤ 14.1v²; phase B: sub-/super-solutions c ∈ [1.98v, π/2 − e_0) and
π/2 + e_0 are correct (2c + 2e ∈ (3.78v, π)). **One-sidedness (φ ≥ 1.89v > 0, "Harry never crosses the tangent line") is
claimed and proved only for τ ≥ τ_1 = 31r**; on [0, τ_1] the proof gives only φ ≥ −0.06v (no sign), and nothing more is needed
there (only ∫a ≤ N(0, τ_1) ≤ 3.48v is used). (iv) S_1: cos 2φ ≤ cos(2φ̄ − 2e_0), sin 2φ ≥ sin(2φ̄ − 2e_0) (concavity, φ̄ ≤ π/4),
so a ≤ (log sin(2φ̄ − 2e_0))' (also when cos 2φ < 0, as the right side is ≥ 0); S_2: ≤ 0.033v²; S_3: a ≤ 0; S_1, S_2, S_3
are consecutive by the barrier property. e^{3.48v+0.04v²}/(3.7799v) ≤ 0.2655/v ≤ 1/(3.7v). The bound holds for every
sub-interval [s, τ]. (v) |p(τ)| ≤ 2τϑ̄(τ); |η| bound; I ≤ 0.6332r + 0.202v² + 0.201v; |ζ| ≤ 0.307r/v + 0.055v; |Q − ζ| ≤ 0.5011v.
(vi) trivial. All correct.

**Theorem E.** *Distances:* sin of both bearings ≥ 0.99494; ρ_b ≥ 0.9949(D + r) − 2ε ≥ 0.865(D + r) for r ≥ 16ε; B: ≥ 0.066.
*Times:* m(y) ≤ C_A(y + 3ε); the two layer-cake integrals are in fact log(1 + Y/r) + 3ε/r and 1/r − 1/(r + Y) + 3ε/r²
(≤ log(1 + Y/r) + 0.19 and ≤ 1.19/r), better than the stated 1.4 and 2.4/r. *Case I:* log(1/r_2) ≤ 5 log(1/v) + 27.6;
N_I ≤ 5.1·10⁻⁷; additive term (3.22·2584 + 706)v ≤ 9.1·10⁻⁹. *Case II:* hypotheses of E4: 2ε ≤ r/8 ≤ τ_3; ϑ̄(τ_3) ≤ 520M(2τ_3)^{1/4}
= v/40 exactly; (H3): for r ≥ 2ε, ϑ̄(s)/(r + s) ≤ 520M(s + 2ε)^{−3/4}, integral ≤ 4ϑ̄(τ_3) = v/10. After the window:
D ≥ 0.99τ_3; ρ ≥ 0.48(τ_3 + τ/C_A); N_C ≤ 7.5·10⁻⁷; ∫ρ⁻² ≤ 4.35C_A/τ_3 + 6773; r w ≤ 1.0024 vτ_3; |Q| ≤ 0.56v + 1.13·10⁻⁸v. Correct.

**Corollaries E5–E7.** E5: ∫Q dr/r, cone argument (needs osc ψ < π; the stated condition "bracket ≤ π/2" suffices). E6:
Case I φ̄(0) ∈ [0, 0.119], drift ≤ N_I/2; Case II [1.98v, π/2 + 0.09v] ± N_C/2. E7: (a) 0.3064 + 2.18ϑ̄; (c) coefficient
1.003 ≤ 1.01; entry-time formula with |θ_1| ≤ 1.1·10⁻⁶, |θ_2| ≤ 1.14·10⁻⁸v. Correct.

**Claim 14(a).** ∂_s(−(v/2ρ) sin 2φ) with ∂_sρ = cos φ, ∂_sφ = −k − sin φ/ρ (Lemma B-1(iii), refereed) gives
(v/ρ) cos 2φ·k + (v/ρ²) sin φ(3cos²φ − 1); multiply by r w. Correct, and independent of the orientation of the label.
|sin φ(3cos²φ − 1)| ≤ 1. Parts (b), (c) of Claim 14 and Claim 15 are not used by P6e and were not refereed here.

**G2 computation (η = 0).** ρ_α ≥ ρ(cos α − v)/sin α, ρ ≥ g(α) ≥ sin 0.1 on [0.1, 0.2] ⇒ ρ(0.2) − ρ(0.1) ≥ 0.0998·0.970·log 2
= 0.0671; r ≥ 1 for α ∈ [arccos v, π]; mirror labels by symmetry; r_b ≤ 0.104, r_a ≤ 0.206 on R. Correct.

## 3. The points I was asked to attack hardest

1. **Is the tiny window τ ≤ τ_3 ≈ 10⁻¹² v⁴ enough? What controls Q for τ > τ_3 and r < vτ_3?** Yes. The window is needed
   only while Harry is within ~r/v of the point. At τ_3 Harry's base is at D ≥ 0.99τ_3 ≥ 0.99 r/v, and from then on
   ρ ≥ 0.48(τ_3 + τ/C_A) **independently of r and ε**. The crude amplification after the window is
   exp((vC_A/0.48) log(1 + 29.5/(C_Aτ_3)) + 447v) with log(1/τ_3) = 4 log(1/v) + O(1): this is e^{O(v C_A log(1/v))} ≤ e^{10⁻⁶},
   a function of v alone. The forcing is v·(r w)·∫ρ⁻² ≤ v·1.0024vτ_3·4.35C_A/τ_3 = 4.4C_A v², again free of r and ε; the only
   r^{−ν} that appears (w ≤ 1.0022((r+τ_3)/r)^ν) is multiplied by r and r^{1−ν} is increasing, so it is bounded by its value
   at r_2. Likewise Case I (r ≥ r_2) pays exp(1.157 vC_A log(1/r_2)) with r_2 polynomial in v. **I find no r^{−cv} loss and no
   hidden ε-dependence**: ε enters only through r ≥ 16ε (so that 2ε ≤ τ_3, 3.5ε ≤ 0.01τ_3, 3ε ≤ 3r/16 and ϑ̄(0) = 520M(2ε)^{1/4}
   is integrable against ds/(r + s)), and through the hypotheses of Theorems B and ST.
2. **Propagator 1/(3.7v).** Proved as stated, and essentially sharp: for a straight path the propagator is
   sin 2φ̄(τ)/sin 2φ̄(s) → 1/sin(4v) ≈ 1/(4v) (numerically 0.926/(3.7v), §4.3). It is harmless only because it multiplies
   Q_0 + v∫|G| ≤ 1.133r + O(v²) with r ≤ vτ_3: the restriction r ≤ vτ_3 of the window is essential, and it is respected.
3. **Dini integrability.** Correct, uniformly in ε, because r ≥ 2ε (see above). Without r ≳ ε the integral would be
   ~ ϑ̄(0) log(τ_3/r).
4. **Circularity with Theorem B.** None. Theorem E uses (TL) only for family pairs with u_b ≤ 8τ_3 + 2ε ≤ U − R at times
   ≤ t_0 + τ_3, and (I1), (CA), (IC2), Step 1 only for legs with base ≤ 2π − 0.2 (u ≤ U − 0.15); no arm label beyond
   2π − δ/2 is ever a family label, and the proof of Theorem B does not use the arm (Remark B-B(2)). Theorem E is not fed
   back into Theorem B.
5. **r < 16ε.** Nothing is claimed there (Theorem E and E5–E7 are restricted to r ≥ 16ε; pairs in E5 must have both radii
   ≥ 16ε). The core [ρ_s, 16ε) of the arm (t_0-length ≤ 14.7ε) can enter the ε-disc during the connector, where Claim 14(a)
   does not apply; Theorem ST's remark reports curvature ≈ v²/(2ε) there. Any user of Theorem E (e.g. for (FS)) must treat
   the core separately. Also nothing is claimed after t_e.
6. **Practical content.** For every ε that can be simulated the theorem is used only in Case I, where it says
   |Q| ≤ 1.000001|Q_0| + 9·10⁻⁹; saturation (φ̄ of order 1) needs (τ/r)^v ~ 1/(2v), i.e. log(1/ε) ≳ (1/v) log(1/v). The
   value of the theorem is the uniformity as ε → 0, which is proved.

## 4. Numerics

### 4.1 Lemma E3 / Claim 14(a): see §2 (5.9·10⁻³⁶). Lemma E1: see §2.

### 4.2 Simulation of start S + legs (= C_cut up to t_e): `sim_arm.py`
Phase 1 in closed form (arm samples and their first and second α-derivatives in 40-digit arithmetic, coordinates
relative to O); connector and every leg with the exact 1-d law ρ' = −1 + v f(ρ); front ahead of Harry by nodes (C¹
virtual field, RK4, updated when Harry has moved 2 % of the distance, the nearest nodes at every leg), target on a cubic
through the base and the next three nodes at arclength ε. [Approximation: the O(vε) tangential compression of the front
inside the ε-disc between nodes is not resolved; it changes headings by O(κvε). Changing the node cap from 2·10⁻³ to
5·10⁻⁴ changed no printed digit.] Arm: 161 labels with r log-spaced in [16ε, r(0.1)], true flow with first and second
variational equations, Q = r ψ_α/r_α; sup over all RK steps up to t_e.

| v | ε | legs | sup \|Q\|/(1.134r + 0.57v) | sup (\|Q\| − 1.134r)/v | sup \|Q − Q_0\|/v (all r; r ≤ 10⁻²) | min ρ_b/(D+r), base in R (≥ 0.865) | min ρ_b, base in B (≥ 0.066) | b_∞ − ψ ∈ | sup (t_j − t_0)/(r_{a_j} + ε) (≤ 2584) |
|---|---|---|---|---|---|---|---|---|---|
| 10⁻² | 10⁻⁴ | 62 160 | 0.8133 | −0.039 | 0.114; 0.030 | 0.9507 | 0.1038 | [0.0214, 0.1274] | 30.57 |
| 10⁻² | 10⁻⁵ | 621 602 | 0.8133 | −0.0045 | 0.114; 0.030 | 0.9507 | 0.1039 | [0.0201, 0.1274] | 30.57 |
| 10⁻³ | 10⁻⁵ | 609 628 | 0.8755 | −0.024 | 0.101; 0.012 | 0.9506 | 0.1003 | [0.0022, 0.1027] | 30.48 |
| 10⁻⁴ | 10⁻⁵ | 608 449 | 0.8822 | −0.217 | 0.100; 0.010 | 0.9506 | 0.1000 | [0.0004, 0.1003] | 30.47 |
| 10⁻⁶ | 10⁻⁴ | 60 831 | 0.8829 | −214 | 0.100; 0.010 | 0.9506 | 0.1000 | [0.0016, 0.1000] | 30.45 |
| 10⁻³ | 2·10⁻⁶ | 3 048 143 | 0.8755 | −0.0049 | 0.101; 0.012 | 0.9506 | 0.1003 | [0.0020, 0.1027] | 30.48 |
| 10⁻² | 10⁻⁷ (partial: base label ≤ 0.02, τ ≤ 0.021) | 210 194 | 0.8133 (r ≤ 10⁻³: ≤ 0.154) | +0.021 (at r = 16ε; still < 0.57) | 0.0215 | 0.9507 | – | [0.0200, 0.1180] | – |
| 10⁻³ | 10⁻⁷ (partial, same) | 200 994 | 0.8755 (r = 16ε: 0.0027) | −0.0003 | 0.0020 | 0.9506 | – | [0.0020, 0.1018] | – |

Reading. (1) sup|Q|/(1.134r + 0.57v) ≤ 0.883 in every run, attained at the outer end r ≈ 0.1 at τ = 0 (it is |Q_0|/(1.134r)
≈ 1.001/1.134); **no trend in ε**. The bound without the term 10⁻⁸ holds even at v = 10⁻², far outside the hypotheses.
(2) Q hardly moves: |Q − Q_0| ≤ (r + 2v + o(1))·v; at small r, Q → +2.1v² (v = 10⁻², ε = 10⁻⁷, r = 1.6·10⁻⁶: Q_0 = −1.2·10⁻⁶,
Q(t) = +2.1·10⁻⁴ = 0.021v), which is the hook term (vτ/2ρ) sin 2φ ≈ v·2v of the self-similar model — the mechanism of
Lemma E3 is visible, with ζ small (sup|ζ|/v ≈ 0.01 at r = 16ε). The proved bound 0.57v is 27 times larger here, as it must be
(it is sharp only after saturation). (3) The geometric inputs hold with margin: ρ_b/(D + r) ≥ 0.9506; (A1) holds with
30.6 (≈ 1.0 while the base is on the right arm) instead of 2584; the tangent cone of E6 is observed as [2v + 1.0 r_min, 0.1 + 2.7v].
(4) v = 10⁻¹² itself is not simulated in double precision (Q − Q_0 ~ 10⁻¹³); the runs show Q − Q_0 is linear in v with
coefficient ≤ 0.1, so at v = 10⁻¹² the margin against 1.134r + 10⁻⁸ is enormous.

### 4.3 Proposition E4 in the saturation regime: `e4_window.py` (`e4_window.out`)
Log-time integration (s = log(1 + τ/r)) of (ρ, β, ψ, w, Q), r = τ_3 e^{−S}, τ_3 = v/1000, heading P' = u_0 e^{iθ} with
|θ| ≤ ϑ̄(τ) = (v/40)(τ/τ_3)^{1/4} ((H1), (H3) with equality at τ_3), six sign patterns of θ (0, +, −, fast and slow
alternation, random blocks), v ∈ {10⁻³, 3·10⁻⁴}, S from 5 to 3·(1/v) log(1/2v) (= 18 644 resp. 74 186 e-folds).
Results (all patterns): sup|e|/v = 1.992 at τ = 0 (≤ 2.04); sup_{τ ≥ 31r}|e|/v ≤ 0.076 (≤ 0.09); min φ̄/v = 2.005 (≥ 1.98);
max φ̄ = 1.570796 (≤ π/2 + 0.09v), monotone; **max propagator × 3.7v = 0.926 (≤ 1)**; sup|ζ|/v ≤ 2·10⁻⁵ (≤ 0.056);
**sup|Q|/v = 0.4995 resp. 0.49985 (≤ 0.56)**, reached once S ≳ (1/v) log(1/2v). So E4 is confirmed and its two main
constants (1/(3.7v), 0.56v) are within 8 % and 12 % of the truth; the allowance for ζ is not attained by these patterns
(the proof bounds the forcing by the worst propagator).

## 5. Summary for the editor
Theorem E and all its parts stand, with constants as stated. Required edits are F1–F3 (justification text) and the
cosmetic F4–F5. The C_cut issue raised as gap G1 in RP6d-1 does **not** affect Theorem E: up to t_e, C and C_cut are the
same path. What Theorem E does not give: anything for r < 16ε, anything after t_e, and Theorem R / the final stretch for
C_cut.
