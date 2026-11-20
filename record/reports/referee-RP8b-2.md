# Referee report RP8b-2 — `referee/P8b-claims.md` (v1): main theorem for design T modulo (H_T)

Second referee (structural / adversarial angle). Not read: `reports/referee-RP8b-1.md`, `reports/P8b-1.md`, `code/P8b/`.
Read: the claims file in full; `referee/P7-claims.md` (§0, §1 incl. proof, §2); `paper/sec_B.tex` (field, Lemmas V, VC,
1–4, C); `paper/main.tex` (lem:limit, lem:A41); `reports/P8a-1.md` §0 (only to compare the intended realisation of (H_T)).
Own code: `code/referee/P8b_2/designT.py`, `summ.py`, outputs `out_*.json`.

## 0. Verdict

| Claim | Verdict |
|---|---|
| Lemma P8.W (working fronts) | **OK** (one wording fix, F2) |
| Lemma P8.A (pairwise passive) | **OK** |
| Theorem P8.D (departure, curved path, pointwise data) | **OK** (cosmetic F4) |
| Lemma P8.H (heading of the first legs) | **OK** |
| §5 (H_T) + derived constants | hypothesis, not a claim; **one text fix needed (F1)**; constants and "Then also" line verified |
| Proposition P8.I (hand-over) | **OK** |
| Theorem P8.M (main theorem modulo (H_T), [P7], [B]) | **OK** (conditional, as stated) |
| Corollary P8.X (exact capture via lem:A41) | **OK** |

No false statement, no gap found in the chain (H_T) ⇒ P8.M ⇒ P8.X. The theorem is exactly as strong as (H_T): everything
delicate about the hole, the hook and the tail has been pushed into (H_T) at the single time t₂, and that is legitimate
(§2, §3 below). Numerically (v ∈ {0.001, 0.01, 0.05, 0.2}, ε from 10⁻² to 5·10⁻⁴, D₁ ∈ {1, 0.1}; far outside the proved
range v ≤ 10⁻⁴⁷, so sanity evidence only) design T_g sees every direction, with T_stop converging as ε → 0 (§5).

## 1. The skeleton, rebuilt (what covers which labels on which time interval)

Labels: u ∈ [0,U] = arclength of x⁰ at t₂; u = 0 is X₀ = P(t₂), u = U is E_Y; the hole sits at u ≈ U − (arc from the axis
to b_e) (numerically u_hole ≈ 5.33 of U ≈ 6.37 for D₁ = 1), i.e. in the second half, at distance ≈ 1 from X₀.
x⁰ is an open arc: its two ends are z₀ ≈ √(2ε) apart, and **no pair ever spans the gap** (pairs are label pairs in [0,U]).
"All the way round" therefore means only: base from u = 0 to within arclength ε of u = U.

| # | statement | time | labels / pairs | source |
|---|---|---|---|---|
| 0 | every direction is seen in [0,t₂] or is the direction of a true label of x⁰ | [0,t₂] | hole \|α\| < α_s, (b_e, α₀), the virtual labels next to α₀ | (H_T)(T0) |
| 1 | true label within ε of P on the working front ⇒ its direction is seen | t ≥ t₂ | all true labels | P8.W(b) |
| 2 | (ST_end) on [0,U_A], U_A = U/2, constants (a′,C₀,λ₀,c_A) | t₂ | pairs in [0,U/2] | (T1), (T2) with u′_b ≥ U/2 |
| 3 | P7.B invariants (J1),(J2),(CA),(TL),(b) for the construction cut at b_A; its legs coincide with those cut at b_E while l(a_j,b_A) > ε | [t₂,t_I] | family pairs in [0,U/2] | Cor. P7.E + causality (P7 Remark (4)) |
| 4 | heading: \|P′ − n̂\| ≤ ϑ_h(τ+ε)^{γ_*}; legs ≤ j_I non-final; D ≤ 2.1W | [t₂,t_I] | — | 3 + (T3) + Lemma P8.H |
| 5 | tail flat, unstretched, at distance ≳ 0.49(u′+z₀+τ) | [t₂,t_I] | u′ ≤ W | (T4),(T5),(T1) + 4 + Theorem P8.D |
| 6 | middle pairs passive (dist ≥ W/5) | [t₂,t_I] | u_b > U/2, u′ > W/2, λ ≤ W/40 | (T1),(T2) + Lemma P8.A |
| 7 | (ST_end) on [a_{j_I}, b_E] with (a_I,C_I,Λ_I,c_I) | t_I | **all** pairs: cases (A) u_b ≤ U/2 [3], (D) u′_a ≤ W [5], (P) rest [6]; (E2_I) from (T1),(T2) + chord monotonicity | Prop. P8.I(b) |
| 8 | construction stops by t_I + 2U_I/(1−v); true labels of [a_{j_I},b_E] seen | [t_I,T_stop] | u ≥ u_{a_{j_I}} | Cor. P7.E at t_I (P8.W(d)) |
| 9 | true labels of [0,a_{j_I}] seen | [t₂,t_I] | u ≤ u_{a_{j_I}} | P8.W(c)(3′), legs ≤ j_I |

Coverage check: the case split (A)/(D)/(P) in row 7 is exhaustive for pairs with λ_I ≤ Λ_I (then λ ≤ W/40, and a pair with
u′_a > W has u′_b > 39W/40); pairs with λ < ε/2 ≤ λ_I are handled by enlargement with the stated ε/2 margins (I checked each
of the three: room U_A − u_{a_{j_I}} > ε; margins "− ε/2" in (P); tail length W ≥ ε/2). Rows 0, 8, 9 cover every direction.
Labels in the seen hole: ghost, nothing claimed, nothing needed. Labels between E_Y and X₀: not on x⁰ at all; covered by row 0.
Labels seen in runs 1–2 but not caught: either ghost or true-and-already-seen (P8.W(b), first sentence). Last legs: P7.B(b)
(dichotomy (α)/(β)), nothing extra. I found no label and no time interval left uncovered.

All numerical side conditions were re-derived: R_A, R_B are exactly the R of Cor. P7.E for (a′,C₀,λ₀,c_A) resp.
(a_I,C_I,Λ_I,c_I) (c_I/16 = Λ_I/36); 4U_A+2 = 2U+2; 4U_I+2 ≤ 4.5U_max+2; a_* ≤ 4.11W; (2.02W/R_A)^{γ_*} ≤ 1/10;
W/4 − 2.25ε − W/39 ≥ W/5 with ε ≤ W/100; 131.25v/W ≤ 132v/W ≤ 1; 1 + 0.42W/λ ≤ W/λ for λ ≤ W/40; C_I ≥ max(M_A, 1.001(C₀+1), K_D);
the "Then also" line of §5; Remark (4)'s numbers (R_A = 6.25·10⁻⁶, ϑ_h = 7.05, W ≈ 3.0·10⁻¹⁰, C_I = 8.81, R_B ≈ 9.7·10⁻³⁹,
v₀ ≈ 1.5·10⁻⁴⁷). T_stop ≤ t₂ + 2.1W + 2.26U_max ≤ T₀.

Theorem P8.D was checked line by line as well (it is new and carries the tail): (i)–(v) hold; the constants 0.49, 4.1,
4.17, 8.34v ≤ 10⁻⁴, 1.26v/γ (0.0103 + 0.192 + 1.05), 13^{1/4}, 1.2184Θ + 2.8ϑ₀ + 1.523ϑ_h ≤ Θ_p, 2.013·(4/3)·5^{−3/4} ≤ 0.81 are
right; [B, Lemma 3(e)] is applicable (ρ_m ≥ 0.998(g̃+τ′) ≥ max(ε, 4l_t)). Lemma P8.H: the family membership of J, I, K₁–K₄
(incl. the switching-time convention F1 and label lengths ≥ ε/2, ≤ 2Λ ≤ R) is correct; 8.04vκ ≤ 10⁻³(Λ/R)^γ; time bound OK.

## 2. The working front — attempts to break it

* **Singular axis label / unbounded α-stretch.** Irrelevant by construction: the working front is parametrised by
  arclength at t₂ and evolves by the C¹ field F for *all* labels from t₂ on; the true (singular) dynamics of hole labels is
  used only to *define the curve x⁰ at the instant t₂*. I re-derived the exact straight-run integrals independently
  (s = tan(φ/2): ρ = (C/2)(s^{v−1}+s^{v+1}), y = Cs^v, t = C[G(s) − G(s₀)], G = s^{1+v}/(2(1+v)) − s^{v−1}/(2(1−v)); **the
  integral has no constant term**, so the pass time is analytic in tan²(α/2)): behind Harry the hole front is
  x_rel = −(1+v)τ − (v/(1−v))·y/s, s ≈ 2ρ/y, i.e. a C^{1,1} arc through the limit point of the caught label, with perturbation
  O(y^{2(1+v)/(1−v)}). So "bounded curvature through the hole" is compatible with the singular label: the singularity is in
  the parametrisation by α (dy/dα ~ α^{−2v/(1+v)}), not in the curve. Numerically no kink at the axis point: N/λ over pairs
  straddling it is ≈ 0.09 down to λ = ε/2 for all ε (a kink of angle θ would give N/λ = θ/(2λ^{1/2}) → ∞).
* **Hole candidates come within ε again when C walks past.** They are ghosts (or true-and-already-seen): P8.W(b) is the
  only bridge between the working front and true candidates, and it is applied only up to the *first* time a true label is
  within ε; after that its direction is seen and the working-front point is just a point of an auxiliary curve. No statement
  about true hole candidates after t₂ is used anywhere. Correct.
* **Monotonicity (Lemma V/VC) for true candidates.** Not available and not used before t₂: no chord or length is
  compared across t₂; (T1)–(T5) are snapshot data. After t₂ all monotonicity is for the F-flow of the working front
  (P8.W(a): needs only F ∈ C¹, A ≥ 0 symmetric, Lemma V(iv), |∂_u x⁰| = 1). Correct.
* **Target rule across the hole.** The rule a_{j+1} = max{l_{t_j}(a_j,·) ≤ ε} is intrinsic to the working front; across the
  hole it sees an ordinary C^{1,1} arc. Simulation: the largest turn between consecutive legs is ≈ ε everywhere, including the
  legs through the hole; sup N/λ ahead of the base does not move when the base crosses the hole.
* **P7.B "verbatim" on a working front.** I checked what the proof of P7.B/P7.E uses of the virtual front of [B]:
  the variational equation, Lemma V, VC(a),(b), Lemmas 1–4, Lemma C(0),(2),(4), labels = arclength at the leg start,
  l(t_s) = λ, and "seen" only through Lemma C(3). All hold for a working front with t_s ≥ t_w. The hypothesis
  "b_E − a_s < 2π" of [P7] has no meaning here and no function (in [B] it only gave c > 0 on the closed front); the
  positivity actually used (target ≠ base) follows from (J1)+(CA) for the pair (a_j,a_{j+1}). See F2.

## 3. The departure from E_Y (tail a distance z₀ ≈ √(2ε) behind Harry)

* **Are the labels between E_Y and X₀ seen at touch-down?** This is (T0), an input. Numerically (true dynamics, exact
  formulas): the labels within ε of Harry before t₂ next to α₀ form one interval (b_e, α₀ + 0.98ε] (0.94ε at v = 0.05),
  z₀/√ε → 1.41, and 0 of 200 000 directions is neither seen by t₂ nor a label of x⁰.
* **May the forward bootstrap ignore the nearby tail?** Yes, and the reason is not a separation estimate: candidates do not
  interact, the legs up to t_I are determined by the forward arc alone, and Theorem P7.B on the arc [0,U/2] is a statement
  about pairs *inside that arc* (P7 Remark (4)). Its (S1) holds there because for pairs in [0,U/2] with λ > λ₀, (T2) gives
  c ≥ min(c_sep, U/4). The naive application on [0,U] fails exactly as Remark (2) of §6 says ((S1) for pairs with
  u_a + u′_b ≲ R), and Proposition P8.I never needs it: on [t₂,t_I] the tail is controlled by Theorem P8.D (input: the
  heading bound from P8.H, which itself only uses stage A), the middle by Lemma P8.A, and (S1)-type separation between base
  and tail is only required *at t_I*, where it is (E2_I): c ≥ min(c_sep, (u_a+u′_b)/2) ≥ W/2 because u_a ≥ W. There is no
  circularity: stage A → P8.H → (DP) → P8.D; stage A does not use the tail.
* **Between t₂ and t_I** the forward legs are controlled by Cor. P7.E on [0,U/2] started at t₂ (stage A); "P7.B from t_I" is
  a second, independent application on [a_{j_I},b_E] with new arclength labels. Both applications satisfy the corollary's
  quantifiers (constants fixed before (v,ε); P(t_s) = x_{a_s}(t_s) at both starts: (T0) resp. leg start t_{j_I}).

## 4. ε-dependence

All derived constants depend on the constants of (H_T) only; j_I, t_I, z₀, y₀, U depend on ε but enter only through the
uniform bounds U ≤ U_max, z₀ ≤ C_zε^{1/4}, (T5). T₀ = T₂ + 2.3U_max + 1 is ε-free. ε ≥ ε_*: the path for ε_* is used;
"within ε_*" implies "within ε"; the path still depends on (v,ε) only. Correct. (Caveat, not an error: the theorem is
"absolute" only once P8a delivers (H_T) with absolute constants for the same D₁; `reports/P8a-1.md` says D₁ = 1 only.)

## 5. End-to-end simulation (independent code)

Exact two-integral formulas for run 1 and run 2 (true candidates, hole and limit point included); F-flow on the last 4ε of
run 2 for the labels near X₀; x⁰ resampled at arclength ε/8; Construction C on the working front (RK4, 12 substeps per leg
within 30ε); "seen" tested (i) for every mesh label via P8.W(b), (ii) independently for ≈ 2000 directions integrated with the
TRUE field along the recorded path. Tangency of run 2 to the front at t₁: |T × n̂| ≈ 10⁻¹¹.

| v | ε | D₁ | U | t₂ | T_stop | legs | unseen mesh / sample | z₀/√ε | (T3) ϑ, u ≤ 0.2 | (T4) ϑ | (T1) sup N/λ | P8.H sup\|û−n̂\|/(τ+ε)^{1/4} |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.001 | 1e-2 | 1 | 6.154 | 3.736 | 9.900 | 703 | 0 / 0 | 1.410 | 0.298 | 0.55 | 0.091 | 0.295 |
| 0.001 | 3e-3 | 1 | 6.219 | 3.736 | 9.965 | 2368 | 0 / 0 | 1.411 | 0.299 | 0.41 | 0.091 | 0.297 |
| 0.001 | 1e-3 | 1 | 6.251 | 3.736 | 10.00 | 7144 | 0 / 0 | 1.411 | 0.299 | 0.37 | 0.091 | 0.299 |
| 0.01 | 1e-2 | 1 | 6.272 | 3.774 | 10.165 | 716 | 0 / 0 | 1.402 | 0.301 | 0.56 | 0.093 | 0.297 |
| 0.01 | 3e-3 | 1 | 6.336 | 3.774 | 10.236 | 2413 | 0 / 0 | 1.396 | 0.301 | 0.41 | 0.093 | 0.300 |
| 0.01 | 1e-3 | 1 | 6.368 | 3.774 | 10.270 | 7277 | 0 / 0 | 1.389 | 0.302 | 0.37 | 0.093 | 0.300 |
| 0.01 | 5e-4 | 1 | 6.381 | 3.774 | 10.284 | 14580 | 0 / 0 | 1.384 | 0.302 | 0.35 | 0.093 | 0.300 |
| 0.05 | 1e-3 | 1 | 6.922 | 3.954 | 11.62 | 7911 | 0 / 0 | 1.281 | 0.316 | 0.38 | 0.099 | 0.309 |
| 0.2 | 3e-3 | 1 | 9.623 | 4.835 | 19.70 | 4572 | 0 / 0 | 0.938 | 0.402 | 0.81 | 0.138 | 0.374 |
| 0.01 | 1e-2 … 1e-3 | 0.1 | 6.22–6.32 | 1.578 | 7.92, 7.99, 8.02 | 710–7219 | 0 / 0 | 1.42–1.40 | 0.297 | 0.55–0.36 | 0.096 | 0.296 |

Reading: T_stop converges (increments 0.071, 0.034, 0.014 for ε: 1e-2 → 3e-3 → 1e-3 → 5e-4 at v = 0.01, i.e. ∝ √ε, the
size of the gap z₀); the (H_T)-type constants and the P8.H heading constant are stable in ε; (T2): min c/min(0.099,
(u_a+u′_b)/2) ≥ 1.01 over (sub-sampled) pairs with λ > 0.1; (T5): |y₀|/((z₀+ε)(ε/2)^{1/4}) = 0.26 → 0.13, decreasing.
Hand-over probe (t_I defined with a numerical W = 0.05): tail stretch ≤ 1.0002 (v ≤ 0.05), tail sup N/λ ≈ 0.03, Harry–tail
distance 0.08–0.19 (D₁ = 1), global sup N/λ ahead of the base unchanged (≈ 0.092) during the whole sweep; stretch of pairs over
the sweep ≈ 1 + 2.3v. Limitations: the simulation cannot reach the constants of the proof (W ≈ 10⁻¹⁰, v₀ ≈ 10⁻⁴⁷); pair
statistics use the polyline (h = ε/8), so excess at λ = ε/2 is accurate to ≈ 6 %; (T1)/(T2) were sampled, not maximised.
First D₁ = 0.1 run had a bug in *my* detection of b_e (search window contained the hole); fixed and rerun — the table shows
the corrected runs.

## 6. Text fixes

* **F1 (needed; §5 (T0)).** Replace "a set 𝒢 ⊂ (0,U) of ghost labels" by "a set 𝒢 ⊂ [0,U) of ghost labels". As stated,
  (T0) forces u = 0 to be a true label, i.e. x⁰(0) = S_θ(t₂) for an uncaught true candidate; but x⁰(0) = P(t₂) is the
  *virtual* candidate α₀ at distance 0, while the true candidate α₀ is at distance (1−v)(t₂^{true} − t₂) > 0 ahead (and no
  true candidate is at distance 0 uncaught). So (T0) as written is false for the intended realisation (and for P8a's
  𝒢 ∋ α₀). Nothing in §§1–6 uses 0 ∉ 𝒢 (P8.W(c)(3′) and P8.M only speak about true labels), so the fix is free.
* **F2 (recommended; Lemma P8.W(d)).** Add: "The hypothesis b_E − a_s < 2π of [P7, §1–2] is void for a working front
  (labels are an interval [a_s,b_E] of an open arc); the target of a non-final leg is distinct from the base because its
  label length is ≥ ε/2 ((J1)) and c ≥ λ/2 ((CA))." Also: P7.E's "U ≤ U_max" is used with (9/8)U_max at t_I — say so.
* **F3 (recommended; §5 header / Theorem P8.M).** State that D₁ is the value for which (H_T) is established (P8a: D₁ = 1);
  the parenthesis "numerics here: D₁ = 0.1" otherwise suggests the theorem covers both.
* **F4 (cosmetic; §3).** "D₁ := 1 − T·û" in the proof of (iii) and "D" (duration) collide with the design constant D₁ of
  §5; rename (e.g. 𝔡 := 1 − T·û).
* **F5 (cosmetic; Corollary P8.X).** H(0) = 0 is not in the statement of lem:A41 but follows from its proof (uniform
  limit of H_N with H_N(0) = 0); say "by the proof of".

## 7. What the conditional theorem rests on (for the record)

Unrefereed inputs: (H_T) (in particular (X1) = (T2) across A₁/A₂ and (X2) = (T1) through the hole, both flagged by the
authors), and [P7] v1 + F1–F13. My numerics support (T0)–(T5) with ε-stable constants at v ≥ 10⁻³, and my independent
derivation supports the C^{1,1} hole front; neither is a proof of (H_T) at v ≤ v_T uniformly in ε.
