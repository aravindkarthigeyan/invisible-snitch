# Second referee report on Theorem D1 (stream D): RD2

Referee: second independent referee. I read only `BRIEF.md`, `paper/main.tex` (model, Prop. 1, Lemma 1 = k decreasing,
Theorem A) and `referee/D-claims.md`. I did not read `reports/D-1.md`, `reports/referee-RD.md`, `code/D/` or
`code/referee/RD/`. As instructed, the first referee's three fixes are part of the statement:
(N1) when v < ε/8, use Theorem A's path; (N2) the connector count in Lemma D4 is "2 + …" for arcs that wrap θ = 0;
(N3) D1 beats Theorem A exactly for ε/d < (1+2π)·10⁻⁴.

Formulation check (rule 5): ε > 0 (vision radius), "seen" means |S − H| ≤ ε, and the path has speed exactly 1. No
compactness is used. Every result below is about this formulation.

**Overall verdict: Theorem D1 holds (PROVED), with one GAP in how the induction is written.** The bootstrap as
written is indexed inconsistently: it claims (H1) "up to τ_{k+1}" before τ_{k+1} ≤ 8 is known, and it re-proves (H2)
for Γ_k although that is already a hypothesis. That is a write-up gap, not a mathematical one. The induction
written out in §2 is non-circular, uses only the lemmas' own constants, and gives the same constants. I found no
ERROR. All constants were re-derived independently (§3). A numerical test that builds the path only from the written
construction, at three boundary points of the range, agrees (§4).

---

## 1. Verdict per step

| Step | Verdict | Comment |
|---|---|---|
| Reduction (A0) and N1 | OK | If v < ε/8 then v < ε/(1+2π) (since 1+2π ≈ 7.283 < 8). Theorem A's path (a segment to (d,0), then the circle of radius d) has speed exactly 1 and sees every candidate by time (1+2π)d < 8d. Otherwise ε/8 ≤ v ≤ 10⁻⁴, and v² ≤ ε/(403+…) gives ε ≥ 403v², because log(3.34/ε) > 0. |
| Lemma D1 (unit vectors) | OK | Standard triangle-inequality argument. |
| Lemma D2 (first-order prediction) | OK | Valid for **any** path with \|P'\| ≤ 1. No regularity is used beyond continuity of P, which gives existence and uniqueness of S_θ while \|S_θ − P\| > ε. Corners between connectors and walks are therefore irrelevant. The integrand of Q_θ needs D_θ > 0: for θ ∈ [δ₁, 2π−δ₁], Phase 1 has D_θ ≥ \|sin θ\| > 0 and Phase 2 has D_θ ≥ 0.48v (H1), so Q_θ is defined everywhere, not just a.e. ∂_θQ formula: (I − wwᵀ) i e^{iθ}/D_θ, norm ≤ 1/D_θ. Identity (*): 1 − e^{iθ}·P = (D² + 1 − \|P\|²)/2. All checked. |
| Lemma D3 (tip seen) | OK | Every step checked: h(t₀) = cos α − 1 + (1+v)ε/2 ∈ [(1+v)ε/4, (1+v)ε/2]; g(β_c) ≥ √3/2; g(α) ≤ 2^v α^{1−v} ≤ √2·0.3ε = 0.4243ε < 0.4330ε = (√3/4)ε; h/C ≥ k(β_c) ⇒ β(t₀) ≤ β_c (k decreasing, main.tex Lemma 1) ⇒ ρ ≤ ε. t₀ ≤ 1/(1−v) ≤ 1+2v needs v ≤ 1/2. The candidate stays in the open upper half-plane (C > 0 is constant), so the (C, h) formulas apply. |
| (P1a) | OK | AM–GM on [0,1] gives c ≥ √(1−s²), whose integral is π/4; on [1, t₁], c ≥ −1. |
| (P1b) | OK | Exact constant: J₁ ≤ 5.3118 + 2.0002 log(1/ε), which is below the claimed 2.91 + 2.0004 log(3.334/ε) = 5.3188 + 2.0004 log(1/ε). The bound ∫₀^{t₁} ds/max(a, \|s−b\|) ≤ 2 + 2 log(t₁/a) needs b = cos θ ∈ [0, t₁] and a ≤ t₁; both hold. v·J₁ ≤ 0.00302 at the worst case v = 10⁻⁴, ε = 403v². |
| Construction (§1.3) | OK | Γ_k depends only on P\|[0, τ_k]. Each walk follows a C¹ curve with \|∂_θΓ_k\| ≥ 0.97 > 0, by arclength, so the speed is exactly 1. Connectors are unit-speed segments; a zero-length connector is harmless. Corners are allowed (the speed is 1 a.e.). θ advances by ≥ ℓ/1.03 per non-final window, so there are finitely many windows, and the walked θ-intervals [a_k, a_{k+1}] tile [δ₁, 2π−δ₁]. Each θ there is passed by exactly one walk, at a time s_θ with P(s_θ) = Γ_k(θ) = Q_θ(τ_k). With D3 covering \|θ\| ≤ δ₁, every direction belongs to some window or to Phase 1. |
| Connector bound c_k ≤ M ≤ 5.41v | OK | c₁ ≤ 3v + 2v² + δ₁ ≤ 5.4002v, using δ₁ ≤ 0.3ε ≤ 2.4v. Recursion c_k ≤ v(c_{k−1} + ℓ) ≤ vM + ε/2 ≤ M because M ≥ ε/(2(1−v)). |
| Upper radius | OK | (1+10v)² − 1 = 20.01v exactly at v = 10⁻⁴. Requires s ≤ 10, which follows from τ ≤ 7.5. |
| Lemma D4 (with N2) | OK | Walking part: chord < r + 8v < 2 ⇒ arc ≤ π(r + 8v), using 2 arcsin(x/2) ≤ πx/2; time ≤ 1.03\|I\|, since the θ'-intervals of distinct windows are disjoint. Connector part: k ≥ 2 starts satisfy \|X_k − e^{ia_k}\| ≤ 8v, the spacing of the a_k is ≥ ℓ/1.03, and k = 1 is counted separately. Re-derived: 3.3232r + 37.88v as written, **3.3232r + 43.29v with N2** (3 connectors + count). Both are ≤ 6.29r + 61.2v. Hypotheses actually used: (H2) for the windows walked inside [t₁, t], c_j ≤ M, and t ≤ 8. (H1) is not used. |
| (H1) margin | OK | Bracket: π/4 − 2v − 6.29·√20.01·√v − 61.2v = 0.49771 ≥ 0.497 at v = 10⁻⁴. Segment: norm ≥ √(A² − M²/4) = 1 + 0.4973v. The c_θ ≥ −1 step is valid because c_θ is a dot product of unit vectors. |
| (H2) | OK | Layer-cake constant 61.2/0.48 + 8/1.9 = 131.71 (claimed 131.8); v·J₂ ≤ 0.01983; v(J₁+J₂) ≤ 0.02285 ≤ 0.024. So \|∂Γ\| ∈ [0.976, 1.024], strictly inside [0.97, 1.03]. Differentiation under the integral sign holds because D_{θ'} is bounded below uniformly near θ. |
| (H3) | OK | τ_final ≤ 7.4354 with 1.024, and ≤ 7.4731 using only the induction hypothesis 1.03. Either way < 7.5 < 8. |
| **Bootstrap logic (indexing)** | **GAP (presentation)** | See §2. As written, "(H1) for window k and connector k+1 … up to τ_{k+1}" needs Γ_{k+1} and D4 on [t₁, τ_{k+1}], hence τ_{k+1} ≤ 8. That bound is only proved later, in (H3). Also, "(H2) … J₂ over [t₁, τ_k] … so (H2)" proves the bound for Γ_k, which the induction already assumed. The fix in §2 reorders the steps: (H3) for k+1, then (H1) on [τ_k, τ_{k+1}], then (H2) for Γ_{k+1}. All constants are unchanged. |
| Error at window start | OK | Layer-cake with φ = min(1, 8v/r) is correct: ∫φ(D) = ∫(−φ')\|{D<r}\| dr. Constant 61.2/8 + 8/1.9 = 11.861 (claimed 11.87). log(0.2375/v) ≤ log(1.9/ε) ≤ L uses v ≥ ε/8. Re-derived E ≤ 2v²[97.80 + 52.32L], against the claimed 97.88 + 52.33L. |
| Seeing | OK | The bound holds for **every** θ of the window: it depends on θ only through J₁(θ) (uniform on [δ₁, 2π−δ₁]) and D4 (uniform in θ). It is not a sampled check. Requirement: v²(401.999 + 209.28L) ≤ ε, implied by 403 + 210 log(3.34/ε). If θ is seen before s_θ there is nothing to prove; otherwise D2 applies on [0, τ_k] and \|S'\| = v on [τ_k, s_θ]. |
| Time bound 8d, scaling | OK | τ_final ≤ 7.45 (or ≤ 1+2π under N1). Scaling (S, H, t) ↦ (λS, λH, λt) preserves speed exactly 1 and replaces ε by ε/d. |
| N3, examples | OK | v_D(ε) = 10⁻⁴ > ε/(1+2π) iff ε < 7.2832·10⁻⁴; the √ branch is far larger there. ε = 10⁻⁶: v_D = 1.677·10⁻⁵, Theorem A gives 1.373·10⁻⁷. Matches the claims. |

## 2. The induction, written without circularity (fix for the GAP)

Let Γ_j(θ) := Q_θ(τ_j) on [a_j, 2π − δ₁]. For k ≥ 1 let **S_k** be the statement:

* (i) Γ₁, …, Γ_k are C¹ with 0.97 ≤ \|∂_θΓ_j\| ≤ 1.03 (so windows 1, …, k are well defined);
* (ii) τ_k ≤ 7.5 and c_j ≤ M for j ≤ k;
* (iii) \|P(s)\| ≥ 1 + 0.48v for s ∈ [t₁, τ_k].

What exists at the start of window k: the path on [0, τ_k] and the curve Γ_k, which is a function of that path.
Window k (connector k from X_k to Γ_k(a_k), then walk k on Γ_k) occupies [τ_k, τ_{k+1}].

**Base, k = 1.** The path on [0, t₁] is Phase 1. J₂ = 0 and vJ₁ ≤ 0.0031, so (i) holds. τ₁ = t₁ and c₁ ≤ 5.4002v, so
(ii) holds. For (iii), \|P(t₁)\| = 1 + 2v.

**Step S_k ⇒ S_{k+1}.** The following are proved in this order.

1. **τ_{k+1} ≤ 7.5.** τ_{k+1} = t₁ + Σ_{j≤k}(c_j + ℓ_j). By (i), Σ_{j≤k} ℓ_j ≤ 1.03·2π. The recursion
   c_{j+1} ≤ v(c_j + ℓ_j) gives Σ c_j ≤ 0.0012. So τ_{k+1} ≤ 7.4731. Also
   c_{k+1} = \|Q_{a_{k+1}}(τ_{k+1}) − Q_{a_{k+1}}(τ_k)\| ≤ v(c_k + ℓ_k) ≤ M. This needs only that Q is defined, not (i)
   for Γ_{k+1}.
2. **Radial bound for each Γ_j, j ≤ k+1.** The bound \|Γ_j(θ)\| ≥ 1 + 0.497v uses (*), (P1a), the upper radius on
   [t₁, τ_j] (by step 1, τ_j ≤ 7.5) and Lemma D4 on [t₁, τ_j]. D4 there needs (i) only for Γ₁, …, Γ_{j−1} (the walks
   inside [t₁, τ_j]), c ≤ M and τ_j ≤ 8. All are available for j ≤ k+1.
3. **(iii) on [τ_k, τ_{k+1}].** Connector k joins X_k = Γ_{k−1}(a_k) (or (t₁, 0) when k = 1) to Γ_k(a_k). Both
   endpoints have norm ≥ 1 + 0.497v by step 2, and the segment estimate gives ≥ 1 + 0.4973v along it. Walk k lies on
   Γ_k, so ≥ 1 + 0.497v there too.
4. **(i) for Γ_{k+1}.** J₂(θ) over [t₁, τ_{k+1}] uses D_θ ≥ 0.48v (from (iii) on [t₁, τ_{k+1}], steps 3 and S_k) and D4
   on [t₁, τ_{k+1}] (needs (i) for Γ₁, …, Γ_k). The result is \|∂Γ_{k+1} − i e^{iθ}\| ≤ 0.0229, which lies inside
   [0.97, 1.03].

No step uses a property of a later curve or a later time. The seeing estimate for θ in window k uses Lemma D2 on
[0, τ_k] and D4 on [t₁, τ_k], both covered by S_k. The recursion stops after the window that reaches 2π − δ₁, which
comes after at most 1 + 6.48/ℓ windows. So the bootstrap is genuinely non-circular. The quantities assumed at the
start of window k are (i)–(iii) of S_k, and they are re-established for k+1 in steps 1–4 above.

**Suggested wording fix for D-claims §1.4.** Replace "Fix k and assume (H1)–(H3) for the path up to τ_k" by S_k as
above, and present the steps in the order 1 → 4. In the (H1) paragraph replace "window k and connector k+1" by
"connector k and walk k". In the (H2) paragraph replace τ_k by τ_{k+1} and Γ_k by Γ_{k+1}.

## 3. Constants re-derived independently

Script: `python code/referee/RD2/constants.py` (mpmath, 30 digits). Each v-dependent bound is increasing in v on
(0, 10⁻⁴], so v = 10⁻⁴ is the worst case.

| Quantity | Claimed | Re-derived |
|---|---|---|
| J₁ | ≤ 2.91 + 2.0004 log(3.334/ε) | ≤ 5.3118 + 2.0002 log(1/ε) (≤ claimed) |
| vJ₁ (ε ≥ 403v²) | ≤ 0.004 | 0.00302 |
| M/v | ≤ 5.41 | 5.4002 |
| M/ℓ | ≤ 0.027 | 0.02685 |
| D4 | 6.29r + 61.2v | 3.3232r + 37.88v as written; 3.3232r + 43.29v with N2 |
| (H1) bracket | ≥ 0.497 | 0.49771; segment ≥ 1 + 0.4973v |
| vJ₂ | ≤ 0.0199 | 0.01983 |
| \|∂Γ − ie^{iθ}\| | ≤ 0.024 | 0.02285 |
| τ_final | ≤ 7.45 | 7.4354 (7.4731 using only the 1.03 hypothesis) |
| E/(2v²) | 97.88 + 52.33L | 97.80 + 52.32L |
| Seeing condition | v²(402.4 + 209.4L) ≤ ε | v²(401.999 + 209.28L) ≤ ε, so **403** and **210** suffice; **3.34** ≥ 3.334 = 1/0.3 |
| Theorem A crossover (N3) | 7.283·10⁻⁴ | (1+2π)·10⁻⁴ = 7.28319·10⁻⁴ |

The time bound 8d holds: 7.45 < 8 in the D1 regime, and 1 + 2π < 8 in the N1 regime.

## 4. Independent numerical test (NUMERICAL)

Script: `python code/referee/RD2/d1_sim.py v eps [Ncand]`. Raw output is in `code/referee/RD2/out_*.txt`.

**How the path is built (only from D-claims §1.2–1.3).**

* Phase 1 is the segment from 0 to (1+2v, 0).
* Γ_k(θ) = e^{iθ} + v∫₀^{τ_k} unit(e^{iθ} − P(s)) ds. Each integral over a polyline segment is evaluated in closed
  form (R₀ − R₁ along the segment, b·Δasinh across it). This was checked against a 2·10⁵-point midpoint rule to
  4·10⁻¹¹.
* Γ_k is sampled on a θ-grid with spacing h = min(10⁻³, √ε/20), plus 600 geometric points refining towards a_k and
  towards 2π − δ₁ (minimum spacing v/200 or δ₁/200).
* The connector is a segment. The walk is the polyline through these exact points of Γ_k, cut at arclength ℓ.

**How the Snitch is simulated.** For each candidate the true Snitch is integrated over sub-steps of length ≤ 10⁻³.
Over each sub-step the Snitch is frozen and its increment is the exact segment integral. The local error is
≲ v²L²/dist, below 10⁻⁹ε. The closest approach on each sub-step comes from the linear relative motion. Candidates
are simulated over the whole path, so the reported minimum is the true min_s \|S − P\|.

**Candidates.** A uniform grid of 3000 directions; for every window start a_k, 12 directions at
a_k + v·{−2, −0.5, 0, 0.1, 0.25, 0.5, 1, 2, 4, 8, 16, 64}; and 10 directions at ±δ₁·{1, 1.001, 1.01, 1.1, 2}.

**Additional checks.** E is measured as the true \|S_θ(τ_k) − Q_θ(τ_k)\| for 47 directions per window. D4 is checked
by computing the exact measure of {D_θ < r} on the Phase 2 polyline for 1200 values of θ and 8 values of r.

| (v, ε) | Where in the range | v²(403+210 log(3.34/ε))/ε | Windows K | τ_final | max c_k/v | \|∂Γ\| on walks | min (\|P\|−1)/v | max_θ min_s\|S−P\|/ε | max \|S−Q\|(τ_k) / E-bound | max D4 ratio (6.29r+61.2v / 3.33r+43.3v) |
|---|---|---|---|---|---|---|---|---|---|---|
| (10⁻⁴, 2.8538·10⁻⁵) | v = 10⁻⁴ cap **and** D1 boundary (equality) | 1.0000 | 45 | 7.2853 | 1.004 | [1.00009, 1.00177] | 0.864 | **0.0242** | 0.035 | 0.419 / 0.792 |
| (10⁻⁴, 8·10⁻⁴) | corner v = ε/8 = 10⁻⁴ (N1 boundary) | 0.027 | 2 | 7.2844 | 3.365 | [1.00007, 1.00097] | 0.807 | 0.354 | 0.031 | 0.419 / 0.792 |
| (1.25·10⁻⁵, 10⁻⁴) | v = ε/8 at small ε (N1 boundary) | 0.004 | 2 | 7.2833 | 3.366 | [1.00001, 1.00015] | 0.807 | 0.354 | 0.032 | 0.419 / 0.792 |

How to read the table:

* Every candidate tested (3022–3538 per case) is seen, and all are seen by time 7.284. The stated bound is 8.
* Every bootstrap quantity lies well inside its claimed range: c_k ≤ 5.41v, \|∂Γ\| ∈ [0.976, 1.024],
  \|P\| − 1 ≥ 0.497v, τ ≤ 7.45, and D4's measure is ≤ 0.42 of 6.29r + 61.2v and ≤ 0.79 of the N2 form.
* At the exact boundary of the D1 range, the proof's budget vM + E-bound is 0.498ε, against the allowance ε/2. The
  true miss distance is only 0.024ε. The true prediction error \|S_θ(τ_k) − Q_θ(τ_k)\| is about 3% of Lemma D2's
  bound in all three cases.
* So the constants are conservative by about a factor of 30 in E. This does not affect validity, but it suggests the
  range could be widened substantially by sharpening D4 and the layer-cake estimates.
* The worst direction in the two ℓ = 4 cases is θ ≈ 3.998. That is the far end of walk 1, where the drift
  v(s_θ − τ_k) is largest; the observed 0.354ε is below the drift bound ε/2.

**Resolution and convergence.** In the first runs, a finite-difference artifact appeared in the \|∂Γ\| diagnostic:
near-duplicate θ nodes produced a spurious 0.976. Dropping nodes closer than 10⁻¹⁰ removed it, and the two quick
cases were re-run. The D1-boundary row comes from the run made before that fix; the fix changes only the diagnostic,
and the path changes negligibly.

Other numerical checks:

* Q is computed in closed form, so the only discretisation errors come from (a) the polyline approximation of Γ_k,
  bounded by κh²/8 ≲ ε/3000, and (b) the frozen-Snitch sub-steps, ≲ 10⁻⁹ε.
* Convergence check: changing the Snitch sub-step from 10⁻³ to 2·10⁻⁴ (400 directions, ε = 8·10⁻⁴) changes
  min\|S−P\|/ε by at most 4.5·10⁻⁶.
* Cost: about 270 s for the boundary case and about 15 s for the other two.

Status: NUMERICAL. This evidence is consistent with D1 and with every intermediate lemma. It does not replace the
proof, which I checked by hand in §1–§3.

## 5. Points I attacked that did not break

* **Is D2 proved for the actual path?** Yes. It is a statement about an arbitrary 1-Lipschitz path. The only
  path-specific inputs are D_θ > 0 (needed for Q to be defined) and the measure bounds of D4, which treat walks and
  connectors separately and count corners nowhere.
* **"Seen" for all θ of a window, not a sample.** The final inequality is uniform in θ ∈ [δ₁, 2π−δ₁]. The θ-dependence
  enters only through J₁(θ), which is bounded uniformly on that range by (P1b), and through τ_θ(r), which is
  bounded uniformly by D4.
* **Directions near the end θ ≈ 2π − δ₁ (= −δ₁).** These are the hardest for J₁, because Phase 1 passes at distance
  ≈ \|sin θ\| from them. They are covered by (P1b), and numerically by the ±δ₁ candidates.
* **Connector 1 starting at (1+2v, 0) inside the margin zone.** It is counted separately in D4 ("plus k = 1"), and
  its norm ≥ 1 + 2v.
* **Speed.** Speed is exactly 1 on [0, τ_final] for both branches: Phase 1, connectors and walks are all unit
  speed, and Theorem A's segment and circle are unit speed. After the last window the path can be continued
  straight; nothing depends on it.
* **The cap v ≤ 10⁻⁴.** It is used in exactly three places: the (H1) bracket, vJ₂ ≤ 0.0199, and 100v² ≤ 0.01v. All
  three hold at v = 10⁻⁴ with the stated margins.

## 6. Minor remarks (no effect on validity)

* §1.4 "(H2)" text says "|{D_θ < r}| ≤ 8 always". It is actually ≤ τ − t₁ ≤ 6.5; either value works.
* "v J₁ ≤ 0.005" (§1.2) and "v J₁ ≤ 0.004" (§1.4) are both true; the actual value is 0.00302.
* With N2 it would be cleaner to quote D4 as 3.33r + 43.3v and keep 6.29r + 61.2v only as "the form used below".
