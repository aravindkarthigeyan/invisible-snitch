# Referee report RP6a-2 (second, independent, adversarial) on `referee/P6a-claims.md`

Read: `referee/P6a-claims.md` in full; `paper/sec_D2.tex` (Lemmas D2.1–D2.2), `paper/main.tex` (Prop. "Topology, length,
area", Lemma A4.1). Not read: `reports/referee-RP6a-1.md`, `reports/P6a-1.md`, `code/P6a`.
Code: `code/referee/P6a_2/constants.py` (every numerical constant recomputed), `code/referee/P6a_2/kink.py`
(construction C with exact tangents; test of the start hypothesis), output `code/referee/P6a_2/kink_small_eps.txt`.

## 0. Summary of verdicts

| Claim | Verdict |
|---|---|
| Lemma V | OK |
| Lemma VC | OK |
| Lemma 1 (i)–(iv) | OK (not used by R, B, M) |
| Lemma 2 (i)–(iv) | OK ((iv) unused) |
| Lemma 3 (a)–(d), Duhamel | OK ((b) unused) |
| Lemma 4 (a),(b) | OK |
| Construction C / Lemma C | OK with fixes (F1: no accumulation of legs; F2: label 2π) |
| Hypotheses (F_b), (S), (T) | well posed, determined by (v, ε); see scope remarks S2 |
| Theorem R | OK |
| Theorem B | OK with fixes (F3 scope of the last leg — a real but boundary GAP as stated; F4 missing case a = a_j, b < a_{j+1}; F5–F8 cosmetic/constant slips). Uniformity in ε is genuine. |
| Consequence of B ((F_b), (S)) | OK (unaffected by F3) |
| Corollary M | OK with fixes (F9 parenthetical path variant needs "labels < a_{j_s} already seen"; F10 say j_s may depend on (v, ε)) |
| "What is NOT proved" / numerical sentence | **misleading as written**: the quoted numbers do not satisfy (IC3), and (ST) at a *fixed* leg j_s = 2 with ε-independent κ is numerically **false as ε → 0** (kink left by the first contact; §4). Not a defect of any PROVED claim, but it changes what remains to be proved. |

No PROVED statement is FALSE. One statement (Theorem B, last leg) has a gap that is removed by shrinking its scope by one
leg; nothing downstream uses the removed part.

## 1. My dependency graph (rebuilt)

```
V(i,ii,iv) ─► VC(a,b,c) ─► L2(i,ii,iii) ─► L3(a) ─► L3(c)+Duhamel ─┐
V(iii) ───────────────────────────────────────────────────────────┤
L1(i) ─► L2(i) ; L3(d) ; L4(a) ; L4(b)                             │
Prop.length(2) + VC + L2(i) + V(ii) ─► Lemma C(1–5)                │
C(2,3,4,5) + L2(i) + L3(d) + L4(b) + V(ii) + (F_b),(S),(T) ─► Thm R│
VC(b) [(CA), l_t ≥ λ] + C(2),(4) + L2(i) + L3(a),(c) + L4(a) + V(ii),(iii) + (ST) ─► Thm B ─► (F_b),(S)
R + B + (ST) + (T) + [R_{j_s} ≤ L_s, t_s ≤ T_s] + Lemma A4.1 ─► Cor M
```
Unused by the main line: Lemma 1(ii)–(iv), Lemma 2(iv), Lemma 3(b). The single structural fact that makes everything
work is that the variational equation ∂_t∂_θx = vA∂_θx contains no P′: so l, c, E are C¹ in t for fixed labels
(P continuous suffices), there are **no jumps of E at leg switches**, and no a.e. differentiation is needed anywhere
in Lemmas 2–3. Only the *index sets* (base a_j, gap g, family 𝔉) jump, and they jump monotonically (𝔉 shrinks,
g decreases), which is what the bootstrap uses. I confirm this.

## 2. Claim-by-claim

### Lemma V — OK
Rederived: A = f′ r̂r̂ᵀ + (f/ρ)Π, f/ρ − f′ = ρ/max(ρ,ε)², hence (iii). F is C¹ with *Lipschitz* derivative (D²F bounded:
x ↦ |x|x has bounded second derivative; A is continuous and piecewise smooth across ρ = ε), not C². Consequence used
nowhere but worth stating: the front is C^{1,1} in θ with a constant depending on ε; ε-independent curvature bounds are
exactly what (ST) postulates.

### Lemma VC — OK
(a) standard (field continuous in t, C¹ in x, ‖DF‖ ≤ 2/ε). (c) uses ρ_θ(0) = 1 > ε. Remark: c(a,b) > 0 only for
b − a < 2π (c(0,2π) = 0); every use respects this (pairs live in [a_{j_s}, b*] with b* < 2π in Cor. M; if b* = 2π and
a_{j_s} = 0, (IC2) fails, so the statement is vacuous, not wrong).

### Lemma 1 — OK
All four identities re-derived (T = cos φ r̂ − sin φ n, JT = cos φ n + sin φ r̂; κ_t coefficients 1 − 3 sin²φ and
3 cos²φ − 1; ∂_s(T × r) = −κ T·r). Regularity hypothesis in (iii) is the right one (F is only C^{1,1} across ρ = ε).

### Lemma 2 — OK
(i) differentiation under the integral is legitimate (|w_t| ≤ (2v/ε)w); c′ exists because c > 0. (ii),(iii) algebra
checked. (iv) checked.

### Lemma 3 — OK
(c): Q = −mp/|y|³, ∂_pQ = −m(m² − 2p²)/|y|⁵, max|c(3c² − 2)| = 1 (numerically 1.000), |∂_mQ| ≤ 2|p|/|y|³; the segment
r_a + σ(x_s − x_a) lies in K − P; expansion gives exactly (v/ρ_m)(1 + l/ρ_m + 2l²/ρ_m²)N² + 2v l^{3/2}|p_a|N/ρ_m³.
Length inequality and (d) checked. Duhamel: 1 + 1/4 + 2/16 = 1.375; the N_η regularisation is correct (E′ exists
everywhere, α, β are bounded measurable in t).

### Lemma 4 — OK
(a) does not need a shared endpoint. (b) needs a₁ ≤ s₁, which holds where it is applied (s₁ > a_{j+1}).

### Construction C and Lemma C — OK with fixes
Checked: the two ansätze (ρ′ = −1 + vf(ρ); β′ = 1 + vf(β)) solve the virtual equation, so **P(t) ∈ [x_{a_j}(t), x_{a_{j+1}}(t)]
exactly** for t in leg j+1 (collinear, in this order). What this buys: (1) |P − x_{a_j}| ≤ c(a_j,a_{j+1}) ≤ ε₁, i.e. ρ_s ≥
c(a_j,s) − ε₁ for every s (the only source of lower bounds on distances in R and B); (2) Lemma 4(b) in Theorem R;
(3) |p| = dist(P, line) ≤ max over the two chord ends, in Steps 3–4 of B. P is piecewise linear with unit speed, hence
1-Lipschitz; each leg is computed from earlier data, so P depends on (v, ε) only. The front is a regular C¹ closed
curve at each time, rectifiable, with length ∫|∂_θx|dθ and l′ = v∫T·AT ds for *all* t.

**F1 (missing: P is defined for all time).** Nothing excludes an accumulation of leg times t_j ↑ t_∞ < ∞ before the
stop. Add to Lemma C:

> (0) *No accumulation.* On [0, T], |∂_θx| ≤ e^{2vT/ε} (Lemma 1(i), V(ii)). A non-final leg j+1 with t_j ≤ T has
> ε = l_{t_j}(a_j, a_{j+1}) ≤ e^{2vT/ε}(a_{j+1} − a_j); so at most 2πe^{2vT/ε}/ε legs start before T. Hence either the
> construction stops or t_j → ∞, and P is a well-defined 1-Lipschitz path on [0, ∞).

(Theorem R does not need it — its induction is over legs — but "path fixed in advance" and the sup-argument for t* in
Theorem B do.)

**F2.** In the definition of a_{j+1}, add "the target is distinct from P(t_j) because a_{j+1} − a_j < 2π or the
construction stops (x_{2π} = x_0)". Cosmetic.

Lemma C(1)–(5) re-derived; (5): 2π(1 + v t_ε) < 2π/(1 − v), times e^{2μ} for leg 0. The cited Proposition applies
(true dynamics, t_ε < t_0).

### Theorem R — OK
Re-derived independently. Split of (a_{j+1}, b*] by l = l_t(a_j, s) (ds = dl):
near l ≤ 8ε₁: ≤ 8ε₁·2/ε = 16e^{2μ}; far l > r₀: ≤ (2/r₁)·e^{2μ}R_j; middle: ρ_s ≥ 3l/4 − ε₁ ≥ l/2 ≥ 4ε₁ > ε,
G ≤ E(a_j,s) ≤ Φ(l), contribution ≤ 2[2Φ(l₂)/l₂ + 4∫Φ/l²] ≤ 4c₀(1 + 1/γ) + 1.5c₁ (text: 2c₁, fine).
Induction R_{j+1} ≤ R_j − ε(1 − μK*) is correct; the final "leg" is not run (P stops at t_j when a_{j+1} = 2π), so the
count L_s/(ε(1 − μK*)) of non-final legs gives the stated time with no "+1". **No constant depends on ε**: the number
of legs ~1/ε multiplies the per-leg duration ε/(1 − v) only.

### Theorem B — OK with fixes
I re-derived Steps 1–5 from Lemmas 2–4, V, C before comparing. Agreement on every estimate except the points below.
All constants recomputed in `constants.py` (only non-reproduced digits: 42.1 → 42.11, "≤ 10⁸" → 1.0034·10⁸, both
absorbed downstream: 2·42.11 + 6.7 = 90.92 ≤ 91, 5119v ≤ 5200v).

*Bootstrap.* Correct: for a fixed pair, l and E are C¹ in t; 𝔉 only shrinks; (Imp) at t < t* passes to t* by
continuity; the extension step δ is uniform over 𝔉 because λ ≥ ε/2 (δ may depend on ε — harmless, it is only a
continuation step, no estimate is summed over δ-steps). With F1 there are finitely many legs on bounded time intervals.

*Uniformity in ε — genuine.* I looked for hidden ε-dependence in each place where ~U/ε legs are summed:
- T_B = (2U/ε + 1)·2ε ≤ 4U + 2: legs enter only through total time.
- Step 1(c) converts every sum over legs into 2εh(g_min) + 4∫h dg; the three uses (h = 1/g, g^{ν−7/4}, g^{−1/2},
  log⁺(λ/g)) all give ε-free bounds because g_min ≥ 32ε resp. the log is integrable.
- Amplification of far pairs: exp∫α ≤ A₀(32R/g₂)^{22v}; this is a power of a gap ratio, *not* e^{cv·#legs}; since
  g₂ ≥ 64λ it is ≤ (R/λ)^{22v}, which is unbounded as λ ~ ε → 0 but is paid for by lowering the exponent of the
  invariant from λ^{3/2} (data) to λ^{3/4}: (R/λ)^ν λ^{3/2} ≤ R^{3/4}λ^{3/4} for ν ≤ 3/4. Correct and ε-free.
- Near phase: duration ≤ 264λ and ΔE ≤ C v M²λ^{3/2} with C ≤ 3.6·10¹⁰ absolute.
The only ε-entry is λ ≥ ε/2 (used as 2ε ≤ 4λ, 2ε/g₂ ≤ 1/16) and ε ≤ R/64.

**F3 (GAP at the last leg; fix = shrink scope).** The theorem is asserted "up to the end of the last leg whose base has
label ≤ U − ε/2". In a leg with u_{a_j} ∈ (U − ε, U − ε/2] the target a_{j+1} may lie *beyond* b* (label > U), where
(ST) says nothing. Step 4, Term II then uses a′ = a_{j+1} ("(x_s − x_{a′}) × e = ±∫τ over the arc between a′ and s …
≤ ϑ max(λ′_s, ε)"), i.e. flatness of the arc (a_j, a_{j+1}) ⊄ [0, U]: not available. With only the trivial bound
|p| ≤ ρ the increment over that leg is ΔE ≲ 10³ vMλ^{5/4}, which is ≤ M²λ^{3/2}/8 only if λ/R ≳ (10⁶v)⁴ — an
ε-dependent condition (fails for ε/R ≲ 10⁻²⁴ at v = 10⁻¹²). Replace in the statement of Theorem B and in "Family":

> "… up to the end of the last leg **j+1 with u_{a_{j+1}} ≤ U** (target inside the labelled arc)" and
> "For t in leg j+1 (t_j ≤ t ≤ t_{j+1}, j ≥ j_s, **u_{a_{j+1}} ≤ U**) the family 𝔉(t) consists of …".

Step 1(a) then reads "for the legs considered: u_{a_{j+1}} − u_{a_j} ∈ [ε/2, ε]" (the label s = u_{a_j} + ε/2 is ≤ U
because otherwise a_{j+1} would be > U). The Consequence is untouched: it only uses legs with a_{j+1} < b′,
u_{b′} ≤ U − ε/2. Corollary M is untouched.

**F4 (missing case in Step 4, Term II).** For a = a_j and ε/2 ≤ λ < u_{a_{j+1}} − u_{a_j} the target a′ = a_{j+1} lies
*beyond b*, and the arc (s, a′) is not a sub-arc of (a, b), so (μ) of Step 2 does not apply as cited. The bound
survives. Insert:

> "If a′ = a_{j+1} > b, put I := (a_j, a_{j+1}) (a family pair, ε/2 ≤ λ_I ≤ ε ≤ 2λ). Then
> ∫_I |T − e_{ab}| ds ≤ l(I)^{1/2}N(I) + l(I)|e_I − e_{ab}| ≤ (√2 + 182)Mλ_I^{5/4} ≤ 219 Mλ^{1/4} ε ≤ ϑε
> by (I1), (I2) and (TL) applied to (a,b) ⊂ I."

**F5 (false intermediate claim, Step 3).** "in particular ρ_m ≥ 16λ" is wrong when g > 32R and λ is close to R
(then only ρ_m ≥ 16R − 2ε − 2λ ≥ 13.9λ). Replace by "ρ_m ≥ 8λ ≥ max(ε, 4l)", which is all that is used. Likewise
"ρ_a ≤ 1.125ρ_m" should be "ρ_a ≤ ρ_m + l ≤ 1.25ρ_m"; the constant 408 remains valid (for R/2 < g ≤ 32R one has
ρ_m ≥ 0.4g ≥ 13l; for g > 32R, ρ_m ≥ 13.9R makes β ≤ 0.04vλ^{3/2}/R²).

**F6 (statement of (μ)).** "a sub-arc J = (a, s) or any family sub-arc" → "any family sub-arc J ⊂ (a,b) (in
particular J = (a, s) with u_s − u_a ≥ ε/2)"; shorter arcs are always enlarged to label length ε/2 where (μ) is used
(λ′_s, J_y, J₀), correctly.

**F7.** Step 1(d), parenthesis: write m := min(w_s, 32R); "if m ≤ 6ε, ε ≥ m/6; if m > 6ε, m/2 − 2ε ≥ m/6". Step 4: "at
most three legs have g < ε" — at most two (g = 0 and one g ∈ [ε/2, ε)); harmless. Near pairs can have g ∈ (32R, 64R)
(λ > R/2); then 6ρ̄ ≥ 32R ≥ λ and log⁺ = 0 — say so where log⁺(λ/(6ρ̄)) ≤ log⁺(λ/g̃) is used.

**F8 ((ST) is stronger than needed).** (IC1) is only used (i) for family pairs (λ ≥ ε/2) at t_s and (ii) through (CA) in
(*), which is vacuous for w_s < 4ε. So (IC1) may be required only for ε/2 ≤ λ ≤ 32R. This matters for checkability:
as stated, (IC1) for λ → 0 is a pointwise curvature bound |k| ≤ √24 κ on a curve that is only C^{1,1} with
ε-dependent constant.

*Counter-scenario hunt (item 4 of my brief).* I tried to break (I1)/(I2) under (ST):
- **kink at scale ε inside the family** — excluded by (IC1) at t_s; afterwards curvature is generated only
  homogeneously (I: a*|T − e|², II: |τ||q| with |q| ≲ ϑ/max(w, 6ε)), giving ΔE ≤ CvM²λ^{3/2}; no ε^{-1} survives because
  the time a pair spends at gap ≲ ε is O(ε) and a* ≤ 2/ε. Consistent.
- **pairs straddling the ε-disc / one endpoint just seen** — pairs with a ∈ (a_j, a_{j+1}) or a < a_j are simply not in
  𝔉 and never needed again ((F_b) concerns (a_j, s), s > a_{j+1}; sub-arcs J_y, J₀ start at a_j or ≥ a_{j+1}). The
  pair (a_j, b), b < a_{j+1}, lies inside the disc: handled by a* ≤ 2/ε over time ≤ 2ε (and F4).
- **far pair becoming near** — happens at a leg switch; E is continuous there, so E ≤ M²λ^{3/2}/8 is inherited; the
  near budget ΔE is counted from that instant. Correct.
- **Harry leaving the chord line** — impossible within a leg (Lemma C(2)); the direction of the chord (a_j, a_{j+1}) is
  controlled by (TL) *provided a_{j+1} ≤ U*: this is exactly where F3 came from. No other failure found.

### Consequence of Theorem B — OK
γ = 1/4, r₀ = R, c₀ = M²R^{1/2}/2 = 1/39200, c₁ = 0, r₁ = R/8 verified; legs with a_{j+1} ≥ b′ have empty (F_b), (S).

### Corollary M — OK with fixes
K* = 16e^{2μ} + 20c₀ + 16e^{2μ}L_s/R + K_T ≤ 32 + 1/1960 + 32L_s/R + K_T; μK* ≤ 0.51; time ≤ T_s + 2.05L_s. U ≤ L_s
and U − u_{2π−δ} ≥ δ/2 ≥ ε/2 hold. It follows from R + B + (ST) + (T) + (R_{j_s} ≤ L_s, t_s ≤ T_s) + Lemma A4.1 with
no further hidden hypothesis **for construction C itself**. Lemma A4.1 applies (time bound independent of ε; nested
finite direction sets are arbitrary).

**F9.** The parenthetical "(or any path … that coincides with construction C from some leg start on)" needs the
hypothesis of Remark (2) after Theorem R. Replace by:

> "(or any 1-Lipschitz path fixed in advance such that, at some time t_s, P(t_s) = x_{a}(t_s) for a label a =: a_{j_s},
> every label in [0, a_{j_s}] has been seen by t_s, and P follows the legs of construction C from t_s on)".

**F10.** State explicitly that j_s (hence a_{j_s}, t_s) may depend on (v, ε), while κ, R, T_s, L_s, K_T, δ may not;
and that (ST) implicitly forces ε₀ ≤ R/64. (See §4: a fixed j_s cannot work.)

## 3. Scope: what (ST) and (T) say

S1. Both are statements about quantities determined by (v, ε) through construction C: (ST) about the two-point
excess and chords of the arc [a_{j_s}, 2π − δ/2] of the virtual front at the single time t_s; (T) about
∫ T·AT ds over labels > max(a_{j+1}, 2π − δ) for all later t. Both are checkable for given (v, ε), not for "all ε ≤ ε₀".

S2. (T) is not a mild condition: once a_{j+1} > 2π − δ it is the full quantity K̃ on the closing arc (near part
≥ what Theorem R bounds by 16e^{2μ}, plus the meeting with the other half of the first-contact kink at label 2π). The
closing phase is entirely inside (T).

S3. **The numerical sentence does not verify (ST).** With the quoted κ² ≤ 0.038 and 32R = 0.11: κR = 6.70·10⁻⁴ >
1/1584 = 6.31·10⁻⁴ ((IC3) fails), and ε ≤ R/64 = 5.4·10⁻⁵ is violated by all quoted ε ∈ [0.005, 0.02]; also
v ∈ {0.05, 0.1, 0.2} is 11 orders above the range of Theorem B. At best (IC1) and (IC2) were observed. Replace
"(ST) holds from the second leg … with κ² ≤ 0.038, 32R = 0.11" by "(IC1), (IC2) hold … ; (IC3) is not satisfied
by these parameters (it requires R ≤ 1/(1584κ) ≈ 3.2·10⁻³ and ε ≤ R/64)".

## 4. A counter-scenario for the *hypothesis*: (ST) at a fixed leg is not ε-uniform

Mechanism (my own computation). Head-on approach creates curvature near label 0: to first order in v, the curvature at
lateral distance s when Harry is at distance ρ from the front is ±vρ²/(ρ² + s²)^{3/2} (total turning 2v, the corner
of the true front at first contact, bearing arccos(−v)). In the true dynamics it collapses into a corner as ρ → 0;
with the virtual field it is frozen at scale ε: a kink of curvature ~v/ε and width ~ε centred at label 0, with a tail
ahead of Harry. (IC1) on [a_{j_s}, ·] requires this tail to be below √24κ at the base.

Experiment (`kink.py`: construction C, tangents from the variational equation, E = l − c from Hermite arclength; the
only deviation is that a_{j+1} is snapped to a θ-grid of spacing ε/60–ε/80). κ²_needed := sup E/λ³ over pairs ahead of
the base with ε/2 ≤ λ, within arclength 0.11:

| v | ε | j = 1 | j = 2 | j = 3 | j = 4 | j = 5 | background |
|---|---|---|---|---|---|---|---|
| 0.1 | 5·10⁻³ | 0.019 | 0.019 | 0.020 | | 0.020 | 0.019 |
| 0.1 | 1·10⁻³ | 0.077 | 0.019 | 0.019 | | 0.019 | 0.019 |
| 0.1 | 2·10⁻⁴ | 2.6 | **0.40** | 0.019 | | 0.019 | 0.019 |
| 0.1 | 4·10⁻⁵ | 69 | **11.2** | 0.53 | 0.063 | 0.019 | 0.019 |
| 0.1 | 1·10⁻⁵ | 1086 | **190** | 8.8 | 1.2 | (round-off floor ≈ 0.3) | 0.019 |
| 0.2 | 2·10⁻⁴ | 78 | **10.8** | 0.27 | | 0.007 | 0.006 |

(max |curvature| ahead of the base at j = 2: 0.68, 0.73, 4.7, 24, 98 for the five ε at v = 0.1; the same growth is seen
when only pairs with λ ≥ 8ε are admitted: 0.018, 0.019, 0.019, 0.081, 1.49.) So at j_s = 2 the required κ² grows like
ε⁻² once v²/ε ≳ 10, and the claim "κ² ≤ 0.038 from the second leg" is an artefact of ε ≥ 0.005. In ε-units the tail
decays roughly like j^{-3…-3.5}, and its amplitude at fixed j scales like v^{≈2.4}/ε (c₂ := curvature·ε/v ≈ 0.022, 0.0098,
0.0009 at v = 0.2, 0.1, 0.02). Hence the first admissible leg grows like a power of v²/ε: **for fixed v and ε → 0 no
fixed j_s satisfies (ST) with ε-independent κ.**

Caveats: numerical, v ∈ [0.02, 0.2] (extrapolation to v ≤ 10⁻¹² is by the scaling above), double precision limits
ε ≥ 10⁻⁵, a_{j+1} snapped to the grid.

Consequences for the programme (not for the PROVED claims):
1. Corollary M is still a correct conditional statement, but only with j_s = j_s(v, ε) → ∞ as ε → 0; then the
   hypotheses "R_{j_s} ≤ L_s" and "(ST) at t_{j_s}" involve ~j_s legs during which Theorem B gives nothing (Lemma C(4)
   alone gives only R_{j_s} ≤ e^{2μ j_s}Λ₀, harmless for v ≤ 10⁻¹² and j_s ≲ 10¹¹, but not "for all ε").
2. The natural repair is to weaken the start condition to what the proof of Theorem B actually uses at t_s:
   E(a,b; t_s) ≤ M²λ^{3/2}/128 for family pairs (plus (CA)). A kink of turning angle Θ ≲ v at scale ε has
   E ≈ Θ²ε·O(1) ≤ M²(ε/2)^{3/2}/128 iff Θ⁴ ≲ 2·10⁻¹⁴ ε/R (order of magnitude), so for v ≤ 10⁻¹² this weaker condition tolerates the
   kink down to ε/R ~ 10⁻³⁴, yet still not for all ε. A genuinely ε-uniform statement needs an invariant that allows a
   kink of angle O(v) at scale ε near the base (e.g. E ≤ ½M²λ^{3/2} + C v²·min(λ, ε·…)), or a separate treatment of
   the first j_s(v, ε) legs. This "kink passage" is a third unproved ingredient beside (ST) and (T), and the same
   kink reappears in (T) when the sweep closes at label 2π.

## 5. Recomputed constants (`constants.py`)

All inequalities of §§3–6 of the claims reproduce (TL: 6.455 ≤ 6.7, 90.92 ≤ 91; C_μ = 33126, √(2C_μ) = 257.4;
far: 0.344, 0.172, 407.3, 365.4, 1.325·10⁵, 0.2679, 3.56·10⁴; near: 264, 270.9, 534.9, 1.065·10⁸, 55488, 3696,
3.893·10⁹, 3.554·10¹⁰; (I1): 1.724·10⁷, 5.70, 5119, 6432; R/M: 1/39200, 1/1960, 2.04 ≤ 2.1; start margin
κR ≤ 1/1584 < 1/1583.92 — tight but correct). Two rounded figures are not upper bounds (42.1, "10⁸"), with no effect.
