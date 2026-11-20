# Referee report RD2b on referee/D2-claims.md (independent second referee)

Scope: Theorem D2, Claims 1–5, Construction W, Corollary D2.1, and the optimality remark. I read only
`referee/D2-claims.md` and `paper/main.tex` Sections 2–4. I did not read reports/D2-1.md, code/D2 or referee-RD2a.md.
Code: `code/referee/D2b/constants.py` (every constant) and `code/referee/D2b/sim.py` (an independent simulation of
Construction W plus a check against the true equation).

**Formulation check.** The claims use the exact problem. P is 1-Lipschitz with P(0)=0 and depends only on (v, ε) after
scaling d=1, through ℓ = ε/v and the virtual flow. It does not depend on α. "Seen" means |S_α − P| ≤ ε at some t, and the
true ODE is used for that check (Claim 2c). The threshold v ≤ 1/(22 log(d/ε)+28) is scale-invariant. I found no silent
change to the problem.

## 1. Dependency graph and bootstrap logic

```
Claim 1 (F monotone, 1/ε-Lip; 1b) ──► Claim 2a,b,d
Claim 2a ──► W well defined (Γ_j Lipschitz ⇒ rectifiable, σ_j continuous)
Claim 2c ──► Claim 4a ──► Claim 4c (needs termination)
Construction W (unconditional geometry) ──► Claim 4b, connector durations ≤ ε/(1−v), τ'_1 ≤ 1/(1−v)
Claim 2d + Claim 3 + (B_j) ──► Γ_j Λ-Lipschitz ──► a_{i+1}−a_i ≥ ℓ/Λ, w_i ≤ Λ(a_{i+1}−a_i)
Claim 2b + 4b + [Λ-Lip of walks 1..j] ──► (B_{j+1})
(B_j) ∀ j that occur ──► termination + time bound (Claim 5) ──► Theorem D2 (Λ=2)
Corollary D2.1 ◄── termination paragraph + Claim 4c
```

**No circularity.** The bootstrap is a finite induction on the walk index j. It is not a continuous-time continuation
argument, so no open/closed or first-failure-time argument is needed.

- (B_j) is a statement about [0, τ'_j], and τ'_j is fully determined by the construction up to then.
- To prove (B_{j+1}) on [0, τ'_{j+1}], the proof uses three things:
  - (i) unconditional facts about the construction on [τ'_1, τ'_{j+1}]: Claim 4b, and connector durations ≤ ε/(1−v);
  - (ii) Λ-Lipschitz fronts for walks 1..j, which come from (B_1..B_j) because Γ_i is frozen at τ'_i ≤ τ'_j;
  - (iii) the spacing a_{i+1} − a_i ≥ ℓ/Λ for i ≤ j, which also comes from (B_i).
- Nothing about Γ_{j+1} is used.
- Termination: every walk that occurs satisfies its (B_j). Then N·ℓ/Λ ≤ a_{N+1} − a_1 ≤ 2π for the number N of
  non-final walks, so N is finite and walk N+1 is final. The induction is valid.

## 2. Regularity of the front and of the walk

The proof is stronger than it claims here. By Claim 2b, |Γ_j(θ) − Γ_j(φ)| ≥ χ(θ, φ) > 0 for θ ≠ φ (mod 2π). Consequences:

- Γ_j is injective on [a_j, 2π), and Γ_1 is a Jordan curve. **No self-intersection is possible.**
- Γ_j is Lipschitz (Claim 2a), so it is rectifiable and absolutely continuous, with length ∫|∂_φ Γ_j| dφ. The proof only
  uses length as total variation, so this formula is not needed.
- Γ_j is locally bi-Lipschitz, with 1 ≤ |∂_φ Γ_j| ≤ Λ a.e. under (B_j). Hence σ_j(φ) − σ_j(θ) ≥ φ − θ, so **σ_j is
  strictly increasing.**
- So the arclength walk is never degenerate. The clause "well defined since Γ_j is constant on intervals where σ_j is"
  is vacuous, and θ*(s) = σ_j^{-1}(s − τ'_j) is continuous.
- This settles the measurability of ψ in the layer-cake step. Measurability is also immediate without this, since θ* is
  monotone on each walk and constant on each connector.
- A "fold-back" of the front is allowed: arclength counts it, and the length bound covers it. The path P may cross itself
  across different walks, which is harmless.

## 3. Termination and time

- **What stops a walk:** σ_j reaches ℓ, or the parameter reaches 2π (the final walk).
- **What stops the construction:** the final walk.
- **Why every direction is seen:** the intervals [a_j, a_{j+1}] cover [0, 2π]. Each φ is seen at
  s_φ = τ'_j + σ_j(φ) ≤ τ_{j+1}, because ρ_φ(s_φ) ≤ v σ_j(φ) ≤ ε (Claim 2c).
- **Time:** T = τ'_1 + Σ_i w_i + Σ_i c_i, where
  - τ'_1 ≤ 1/(1−v);
  - Σ_i w_i ≤ Λ Σ_i (a_{i+1} − a_i) ≤ 2πΛ, which includes the final walk, since w_final = σ(2π) − σ(a) ≤ Λ(2π − a);
  - Σ_i c_i ≤ N ε/(1−v) ≤ (2πΛ/ℓ) ε/(1−v) = 2πΛ v/(1−v).
- Summing gives T ≤ (1 + 2πΛ)/(1−v). Correct.

## 4. Optimality for the method

The "limiting remark" is **not present** in referee/D2-claims.md (the file ends at Corollary D2.1). I checked the
statement as given in the brief, J ≥ log(1/ε)/(1+v):

- **True, and in fact for every walked base point.** ρ_{a_j}(0) = 1 and ρ_{a_j}(τ'_j) = 0, and |ρ'| ≤ 1 + v a.e. (|P'| ≤ 1,
  |S̃'| ≤ v). The coarea / change of variables on {ε ≤ ρ ≤ 1} gives
  J_{a_j}(τ'_j) ≥ (1+v)^{-1} ∫_ε^1 dr/r = L/(1+v).
- So the Gronwall factor exp(vJ) at φ = a_j is ≥ ε^{-v/(1+v)}. A bounded Λ through this route needs v ≤ (1+v) log Λ / L.
  **The order v ≍ 1/log(1/ε) is therefore optimal for the Gronwall/J method. The constant 22 is not.**
  - The lower bound would allow about log 2/L at Λ = 2.
  - The method's own upper estimate, with (2 + 2πΛ)L as the leading term, is best at Λ ≈ 3.02, giving leading
    constant ≈ 18.98 instead of 21.01 at Λ = 2 (constants.py).
- This shows that the *bound* fails for larger v, not that the *front* has a large Lipschitz constant. Numerically the true
  front Lipschitz constant is far below exp(vJ): at ε=0.01, v=0.15 it is 4.1 against 16.1.
- **Required wording:** "optimal in order for any argument that bounds the front's Lipschitz constant by
  exp(v J_φ); not optimal in the constant, and not a statement about the construction itself."

## 5. Verdicts

**Claim 1 — OK.** π_ε = εx/max(|x|, ε). Firm non-expansiveness gives (a). The identity
|x−y|² − |x||y||x̂−ŷ|² = (|x|−|y|)² gives (b).

**Claim 2 — OK.**
- (a) Global Lipschitz in S plus Gronwall, with D(0) = χ ≤ |θ−φ|.
- (b) Exact derivative identity.
- (c) ρ_θ(0) = 1 > ε, so t0 > 0. Uniqueness of the true equation on {S ≠ P(t)} holds with P only continuous in t
  (Carathéodory/Picard with continuity in t and local Lipschitz in S).
- (d) D > 0 by (b). The bound uses min(|x|, |y|) ≥ ρ_θ − D. The dominated-convergence limit is valid: a_φ ≤ 1/ε, and
  sup D → 0 by (a).

**Claim 3 — OK.** The standard sup argument. The two-sided limsup from 2d suffices on [a_j, 2π].

**Construction W — OK with fixes.**
- (i) Connector j+1 when ρ_{a_{j+1}}(τ_{j+1}) = 0: u is undefined. Add "(if ρ_{a_{j+1}}(τ_{j+1}) = 0 the connector is
  empty, c_{j+1} = 0)".
- (ii) "All objects below are computed from P on earlier times only": the connector is defined implicitly. Replace with
  "Each walk is computed from P on earlier times; each connector is the unique straight run solving the implicit
  definition, by the ansatz below."
- (iii) Optional simplification: "σ_j is strictly increasing because |Γ_j(θ) − Γ_j(φ)| ≥ χ(θ, φ) (Claim 2b), so
  P(τ'_j + s) = Γ_j(σ_j^{-1}(s))."

**Claim 4 — OK.**
- (a) ρ_φ(s_φ) ≤ v σ_j(φ) ≤ ε.
- (b) On walk j, θ*(s) ∈ [a_j, a_{j+1}] and |P − S̃_{θ*}| ≤ v(s − τ'_j) ≤ ε. On connectors, ρ_{a_j} decreases from ≤ ε.
- (c) Covering of [0, 2π].

**Claim 5 — OK with a minor fix.** I rederived every inequality independently:
- phase-1 J^{(1)} = (2/(1−v))(1 + log(2/((1−v)ε)));
- ψ ≥ max(ε, χ/2);
- the layer cake;
- m(y) ≤ (2πΛy + 2ε)/(1−v) for y ≤ 1 and ≤ 2πΛ/(1−v) for y > 1;
- 4 arcsin y ≤ 2πy;
- the connector count 2 + 2πyΛ/ℓ.

Fix: the walk-time estimate should state the intersection explicitly. Replacement: "on walk i, θ*(s) ∈ [a_i, a_{i+1}];
hence |{s ∈ walk i : θ*(s) ∈ I}| ≤ Λ |I ∩ [a_i, a_{i+1}]| for any interval I, and summing over i and the ≤ 2 intervals
of A_y gives ≤ Λ|A_y|."

**Theorem D2 — OK with a cosmetic numeric fix.**
- (22L+28)(27/28) = 21.2143L + 27, not 21.215L + 27. Rounding the denominator *up* is the wrong direction. The conclusion
  survives.
- Replacement text: "= (14.567 L + 18.028)/(21.2142 L + 27) ≤ max(14.567/21.214, 18.028/27) = max(0.68667, 0.66770)
  < 0.6931 < log 2."
- All other constants check:
  - 2 + 4π = 14.5664 ≤ 14.567;
  - 4 + 4π + 2 log 2 + 2/27 = 18.0267 ≤ 18.028;
  - (1+4π)·28/27 = 14.0688 < 14.07.
- A direct evaluation of vJ*(2) at v = v_2(ε) over L ∈ (0, 40] has maximum 0.66754, tending to 0.6621 as L → ∞, which is
  < log 2.

**Corollary D2.1 — OK.** It uses only w_i ≤ Λ(a_{i+1} − a_i) on the walked parts, the connector bound ≤ ε/(1−v), and
τ'_1 ≤ 1/(1−v).

**Limiting / optimality remark — not in the file.** As stated in the brief (J ≥ log(1/ε)/(1+v)) it is TRUE, by the proof
in §4 above. "Optimal for this method" holds in order only. Use the wording in §4.

## 6. Numerical corroboration (sim.py, RK4, N grid directions)

Bound column: (1+4π)/(1−v). "Lip meas." is the measured Lipschitz constant of the walked fronts; "exp(v max J)" is the
Gronwall bound from the method.

| ε | v | walks | T | bound | Lip meas. | exp(v max J) | min_j J_{a_j}(τ'_j) | L/(1+v) | 200 true α seen |
|---|---|---|---|---|---|---|---|---|---|
| 0.1 | v_2 = 0.01271 | 1 | 7.37 | 13.74 | 1.04 | 1.04 | 3.36 | 2.27 | yes |
| 0.01 | v_2 = 0.00772 | 5 | 7.42 | 13.67 | 1.07 | 1.11 | 5.67 | 4.57 | yes |
| 0.01 | 0.05 | 35 | 8.35 | 14.28 | 1.55 | 2.24 | 5.89 | 4.39 | yes |
| 0.01 | 0.15 | 133 | 11.31 | 15.96 | 4.12 | 16.1 | 6.55 | 4.00 | yes |

In every run:
- all grid directions are seen;
- the stop time is within the bound;
- the measured Lipschitz constant is ≤ the Gronwall bound;
- J_{a_j}(τ'_j) ≥ L/(1+v), as §4 predicts.
