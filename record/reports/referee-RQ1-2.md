# Referee report RQ1-2 on referee/Q1-claims.md (Theorem End*, Corollary End*, Q1.L1–L4)

Second, independent referee. I did not read reports/referee-RQ1-1.md, reports/Q1-1.md or code/Q1/*.py.
I read code/Q1/out/optimise.txt and the run_*.json parameter files only after finishing the proof check (§1–§2).
Sources checked against: paper/sec_B.tex (lem:B-V, B-VC, B-1, B-2, B-3, B-4, B-C, thm:R and its Claim, Steps 1–5 of
thm:Bulk) and paper/sec_E.tex (lem:E-facts, Construction C cut at b_E, thm:End, cor:End).
My code: `code/referee/Q1_2/` (consts.py, lemmas.py, sim.py, batch.ps1; outputs in `out/`).

## Verdict summary

| claim | verdict |
|---|---|
| Lemma 4.1 (Duhamel, general ratio) | OK |
| Lemma 4.2 (gap–time integrals (i)–(iii)) | OK (also tested on 2000 random admissible gap sequences) |
| Lemma 4.3 (h1, h3, z·h1 ≤ λ, ∫h1) | OK (closed forms checked by quadrature) |
| Step 0 / continuity scheme (Imp*) | OK |
| Step 1 (dichotomy, advance [ε/κ1, ε], T_B = χU, (E-star*)) | OK; κ1 ≤ 4/3 is exactly what (β) needs |
| Step 2 (tilts C_A, C_B, C_TL; (E-mu*)) | OK |
| Step 3 (far pairs, (P3)–(P5)) | OK |
| Step 4 (near pairs, D_I, D_IIs, D_IIl, (P6)) | OK — rebuilt independently, same constants (§1) |
| Step 5 ((J1*), X_far, B_5, I_5, (P7)) | OK, including γ > 1/2 via Lemma 4.2(ii) |
| Theorem End* (a), (b), (d), (e) | OK |
| Theorem End* (c) | OK as stated; remark: at the optimised parameters μK̃ ≈ 1.11 > 1, so (c) cannot feed thm:R there (§3) |
| Corollary End* ((C0)–(C6), weakened (C1)–(C3)) | OK |
| Q1.L1–Q1.L4, removal of the cap γ ≤ 1/4 | OK |
| Numerical claim v ≈ 5.8·10⁻⁵ … 6.5·10⁻⁵, (P6) binding | OK (reproduced independently, §4); one-ulp fix on R (§4) |
| Simulation prediction "no violation at v ≈ 5·10⁻⁵" | confirmed, with large margins (§5) |

No FALSE item and no GAP found. Fixes requested are cosmetic/numerical only (§6).

## 1. Rebuild of the near-pair estimate (binding (P6))

I rederived E′ ≤ I + II (lem:B-3(a), q̄ = 0) for a near pair (g < K_fλ), from lem:B-V(ii),(iii), lem:E-facts(b),
(E-star*), (E-mu*) and Lemma 4.2, without using the claims' intermediate formulas, then compared.

*Term I.* Layer cake a*(ρ) = ε⁻¹1{ρ<ε} + ∫_{max(ρ,ε)}^∞ y⁻²dy; ρ_s < y ⇒ c_A min(w_s,K_RR) < y + δ1ε; for y ≥ ε,
(y+δ1ε)/c_A ≤ c_6 y, so {ρ<y} ⊂ sub-arc from a of label length ≤ min(λ, c_6 y) (else c_6y > K_RR ≥ λ and the bound is
trivial); (E-mu*) gives ω(y) ≤ (1+κ1C_A²)M²λ^{2γ}min(λ,c_6y). The ε-piece lives only on legs with g < c_6ε (needs
c_6ε ≤ K_RR, i.e. (P2)); count ≤ κ1c_6+1. The integral piece is c_6 h1(c_6ρ̄) with c_6ρ̄ ≥ max(c_6ε, min(g,K_Rλ)), and
Lemma 4.2(i) + Lemma 4.3 give ∫ ≤ λ[d(κ1c_6+2) + c_6χΨ]. **Same as τ_I, D_I = CμA τ_I.**

*Term II, short case.* |q| ≤ |p(s)|/D², p(s) = (x_s−x_a)×e + p_a; first part ≤ C1A Mλ^γ max(σ_s,ε/2) ≤ C1A Mλ^γ c_6 D;
|p_a| ≤ k_0Mλ^γε (g = 0; two sub-cases a_{j+1} ≤ b / > b) and ≤ κ1C_TL M g(g+λ)^γ (g > 0; three sub-cases g′ = 0,
≥ ε/2, ∈ (0,ε/2), the last using κ1 ≤ C_TL²(4−κ1²), which holds with a factor ~800 at the optimum). Fubini with
φ_1 = c_6/max(w,c_6ε), φ_2 = φ_1² and Ψ_τ(y) ≤ C1A Mλ^γ min(λ,y) gives II_α ≤ v c_6²C1A²M²λ^{2γ}h1(max(c_6ε,g)),
II_β(g=0) ≤ 2c_6C1Ak_0 vM²λ^{2γ} (one leg ≤ 2dλ), II_β(g>0) ≤ 2c_6²κ1C_TL C1A vM²λ^{2γ}(1+x)^γG(x), majorant H checked
numerically for γ ∈ {0.05,…,0.95}. Time integrals τ_α, τ_β as claimed. **Same D_IIs.**

*Term II, long case* ((K_f+1)λ > R): |q| ≤ 1/D, φ_1 for w ≤ K_RR, c_6/(K_RR) beyond; ∫|τ| ≤ κ1^{1/2}Mλ^{1+γ}; duration
≤ τ_nλ; Mλ^{1+γ} < ((K_f+1)^γ/m)M²λ^{1+2γ}. **Same D_IIl.** The start value ½f²M²λ^{1+2γ} (Step 3 at the switching
time, family of the previous leg; s0 ≤ f for pairs near at t_s) gives θ = f² + 2v[D_I+max(D_IIs,D_IIl)]. **(P6) is the
right condition.**

Where the constant comes from (round6 a=1/2): 2vD_IIs = 0.885 of the budget 1, of which II_β(g>0) = 6063/7593 = 80%
(|p_a| bounded through the general tilt C_TL = C_A + C_B ≈ 17.4). Comparison with reality: the simulations (§5) give an
empirical near-growth constant max ΔE_near/(vM²λ^{1+2γ}) ≈ 0.03–0.06 (γ ≈ 0.50) and ≈ 0.005 (γ ≈ 0.61), against
D ≈ 8.2·10³ resp. 9.6·10³: the proved bound is conservative by ~10⁵, not wrong.

## 2. Stress test of the optimum regime (γ ≈ 0.5–0.6, K_f ≈ 5, K_R ≈ 32 or 10⁶, κ1 ≈ 1.02, m up to 0.19, K_ε up to 10³)

I looked for every place where the old proof used K_f = 64, K_R = 32, γ ≤ 1/4 or m = γ/50 implicitly:

- **Far/near split, "far stays far".** Only g non-increasing and λ fixed are used. a > a_{j+1} for far pairs needs
  K_fε/2 > ε: K_f ≥ 3. (a′,a) ∈ F needs (K_f/2−1)ε ≥ ε/2: K_f ≥ 3. r_f needs K_f > 2. All explicit in (P0).
- **ρ_m ≫ l was implicit in the old Step 3** (ρ_m ≥ 4l for lem:B-3(e)). Here Lemma 4.1 keeps the general factor
  1 + 1/K + 2/K²; at the optimum K_1 = c_ρK_f/κ1 ≈ 1.96 (a_1 ≈ 2.03). lem:B-3(c) itself needs only ρ_m ≥ ε — rechecked.
  c_ρ > 0, c_R > 0 are forced by (P2). No hidden K ≫ 1.
- **Tilts not small.** C_TL·m = 2.67 (a=1/2), i.e. (d) is vacuous at λ ≈ R (|e_J−e_I| ≤ 2 anyway). I checked that no step
  needs a tilt < 1: they enter only through |e×e′| ≤ |e−e′|, lem:E-facts(b) (an identity) and lem:B-4(a) (an inequality
  for all sizes). Harmless, but worth a sentence in the text (§6).
- **γ > 1/2 / γ near 1−ν.** Uses: ν+γ < 1 (third far term, second-term exponent), γ < 1 (H decreasing), Lemma 4.2(ii)
  in Step 5. All present. Cap γ ≤ 1/4: indeed not used.
- **κ1 up to 4/3.** Step 1(α) needs κ1 ≤ 2, (β) κ1 ≤ 4/3 (with strict inequality from λ_2 < ε/2). OK.
- **m large.** Only via c_t (m/2 term), D_IIl (1/m), (Pc). E ≤ ½m²λ ≤ 0.012λ at the optimum; nothing needs E ≪ λ
  beyond (CA*), which comes from (S1*).
- **K_R small / large.** K_R ≥ 1 gives min(λ,K_RR) = λ for family pairs and min(λ,K_RR) ≥ R/κ1 in (c). K_R = 10⁶
  (run "K_R uncapped") is harmless (regime g > K_RR empty, Ψ uses log min(K_f,K_R)).
- **Length bound.** Far factor exp(X_far + B_5I_5vm²) then additive near increase vκ1τ_I; ordering (far phase precedes
  near phase) correct. At the optimum the margin is L_J/κ1 = 1 − 2.3·10⁻⁸ ((P7) binding; δ_tail ≈ 2·10⁻⁸ as stated in
  Q1.L4).

No implicit use found.

## 3. Remarks on statements (not errors)

- (c): the bound K̃ ≤ 16δ1 + 2m²(1+1/γ) + 2δ1κ1U/r_1 is proved, but at the optimised parameters it is ≈ 1.9·10⁴ and
  μK̃ ≈ 1.11 > 1 (optimise.txt prints this), so (c) cannot be combined with thm:R at v ≈ 6·10⁻⁵ with U = 6.5. (b) does
  not depend on (c). Any downstream use of (c) must re-optimise with the thm:R condition.
- (d) carries no information for λ_I close to R at the optimum (C_TL m > 2).

## 4. Independent recomputation of constants and side conditions (consts.py, mpmath 50 digits)

Written from my own derivation; dependent quantities d, δ1, ν, log A0, f set by equality in (P1), (P3), (P4), (P5).
At the run_00–03 parameters (full precision from run_*.json) every derived constant agrees with optimise.txt to all
printed digits, e.g. round6 a=1/2: C_A = 7.11459, C_TL = 17.3646, C1A = 7.34077, D_I = 607.976, D_IIs = 7592.58
(α 920.568, β 6063.03, g=0 608.979), D_IIl = 993.314, f = 0.210345, L_J = 1.0219610229.

| run | v | (P6) lhs at v | at v(1−10⁻⁶) | (P7) slack | (P2) c_ρK_f−2 |
|---|---|---|---|---|---|
| round6 a=1/2 | 5.8274e-5 | 1 − 1.00e-6 | 1 − 1.99e-6 | 2.3e-8 | 2.2e-8 |
| round6 a=0.99 | 6.4058e-5 | 1 − 1.03e-6 | 1 − 2.03e-6 | 2.4e-8 | 2.2e-8 |
| Q3 a=1/2 | 5.9679e-5 | 1 − 1.00e-6 | 1 − 1.99e-6 | 2.3e-8 | 2.2e-8 |
| Q3 a=0.99 | 6.4957e-5 | 1 − 1.03e-6 | 1 − 2.03e-6 | 2.2e-8 | 2.2e-8 |

All (P0)–(P7), (Pc), (C0)–(C6) hold, **except** that with R taken literally from the JSON double, (C6) (round6 a=1/2,
at v) and (C4) (Q3 a=1/2, independent of v) fail by one ulp (relative −2·10⁻¹⁷, −9·10⁻¹⁷). This is rounding of a
saturated constraint: R ← R(1−10⁻¹²) restores both and changes nothing else visibly. The optimiser's v is sharp for its
parameters: at v(1+10⁻⁵), (P6) = 1.00001 > 1; at 10v, (P6) ≈ 10; at 100v, (P6) ≈ 1.5·10³–6.7·10³.
Extra inequalities used inside the proof (κ1 ≤ C_TL²(4−κ1²), δ1 ≥ 1 > c_A/2, κ1 ≤ 2, K_R ≥ 1/κ1) hold with room.

## 5. Simulation of Construction C (sim.py; out/results.jsonl)

Own simulator: front = polyline (≈12 800–25 600 nodes, h = ε/5 or ε/10) built from a tangent angle
"bend + multiscale roughness (scales 2R … 1.5ε, random phases, amplitude ∝ L^γ)", tuned so that at t_s
max N/(s0Mλ^{1/2+γ}·gap factor) = 0.999 (**(S2*) saturated**) and min c/(c_A min(λ,K_RR)) ≈ 1.002 (**(S1*) nearly
saturated** at λ ≈ K_RR by the bend; one run without bend). Construction C exactly: target inserted at the label with
l_{t_j}(a_j,a_{j+1}) = ε, unit-speed ray, leg duration from ρ′ = −1+vf(ρ), RK4 (≥ 48 steps per leg), measurement at
leg start, mid-leg and leg end for all family pairs on a 34-point λ-grid in [ε/2, R] and every admissible a; (CA*) on
40 scales up to U; (E-star*) at mid-leg. Parameters: run_06 (a=1/2, K_ε ≤ 64, v* = 5.82e-5) and run_09 (a=0.99,
γ = 0.615, v* = 6.40e-5); ε = R/K_ε (also R/(2K_ε)); U = 40R (so g > K_RR occurs); 2 560–5 120 legs.
Ratios reported (theorem predicts ≤ 1 for J1, J2 and ≥ 1 for CA, E*, adv at v ≤ v*):

| run | v | J1 = max l/(κ1λ) | J2 = max N/(Mλ^{1/2+γ}) | CA min | E* min | adv/(ε/κ1) min | legs / κ1U/ε | D_eff |
|---|---|---|---|---|---|---|---|---|
| 06, bend ± / none, ε=R/64 | 5e-5 | 0.9783 | 0.1524 | 1.0020 | 1.0022 | 1.0223 | 2560/2617 | 0.035–0.038 |
| 06, ε = R/128 | 5e-5 | 0.9783 | 0.1523 | 1.0020 | 1.0021 | 1.0223 | 5120/5234 | 0.034 |
| 06, bend ± | 5e-4 | 0.9791 | 0.1527 | 1.0020 | 1.0022 | 1.0221 | 2560/2617 | 0.034–0.037 |
| 06, bend ±, h = ε/5, ε/10 | 5e-3 | 0.9878 | 0.1570 | 1.0019 | 1.0022 | 1.0204 | 2564/2617 | 0.038–0.040 |
| 06, bend ± | 5e-2 | **1.0796** | 0.2026 | 1.0020 | 1.0023 | 1.0028 | 2605/2617 | 0.060–0.064 |
| 09 | 5e-5 | 0.9781 | 0.0604 | 1.0054 | 1.0056 | 1.0224 | 2560/2617 | 0.0049 |
| 09 | 5e-4 | 0.9790 | 0.0605 | 1.0054 | 1.0056 | 1.0223 | 2560/2617 | 0.0047 |
| 09 | 5e-3 | 0.9875 | 0.0616 | 1.0054 | 1.0056 | 1.0207 | 2564/2617 | 0.0052 |
| 09 | 5e-2 | **1.0780** | 0.0816 | 1.0054 | 1.0057 | 1.0046 | 2604/2617 | 0.0075 |

Also: T_stop − t_s ≤ κ1U/(1−v) in all runs (e.g. 0.02863 vs 0.02927); at stop l(a_J,b_E) ≤ 0.72ε and
|P − x_{b_E}| ≤ 0.72ε; |P − target| at leg end ≤ 4·10⁻¹² ε; h = ε/5 vs ε/10 agree to 4 digits.

Reading: at v ≈ 5·10⁻⁵ (just below v*) **no violation**; margins: (J1*) 2.2% (l/λ ≤ 1.00002 against κ1 = 1.022), (J2*)
factor ≈ 6.6 (γ≈0.5) / 16.5 (γ≈0.61) — the start value s0 is essentially preserved, (CA*) and (E-star*) 0.2–0.6%
(saturated by construction of the start), advance ≥ ε/κ1 with 2% room. At 10× and 100× v* nothing is violated either
(the bounds are far from sharp). At ≈ 860× v* (v = 0.05), (J1*) is violated: l/λ reaches 1.104 > κ1 = 1.022, while J2
stays ≤ 0.21 — consistent with (P7) being, after (P6), the next binding constraint; the theorem claims nothing there.
Limitations: U = 40R ≪ U_max = 6.5, adversarial starts limited to bend+roughness; the test cannot probe the (P6)
constant itself, which is ~10⁵ above the observed near growth (D_eff column).

## 6. Requested fixes (exact text)

1. §8 / optimiser output: add "R is rounded down by a relative 10⁻¹² before verification; with the saturated value
   (C4) resp. (C6) fail by one ulp." (or verify at R(1−10⁻¹²)).
2. After Theorem End*(c): add "At the optimised parameters of code/Q1/out the bound of (c) is ≈ 2·10⁴ and μK̃ > 1;
   (c) is stated for use with other parameter choices and is not used in (a), (b), (d), (e)."
3. After (d): add "At the optimum C_TL m > 2, so (d) is informative only for λ_I ≪ R; no step of the proof needs
   C_TL M λ^γ < 1."

Reproduction: `python code/referee/Q1_2/consts.py code/Q1/out/run_0{0,1,2,3}.json`; `python code/referee/Q1_2/lemmas.py`;
`powershell -File code/referee/Q1_2/batch.ps1` (≈ 10 min, 14 processes).
