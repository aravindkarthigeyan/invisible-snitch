# Referee report RQ2-2 on referee/Q2-claims.md (version 1): excused-tail assembly

Second, independent referee. I did not read reports/referee-RQ2-1.md, reports/Q2-1.md or code/Q2.
I read in full: referee/Q2-claims.md; sec_E.tex lines 1–580 (Construction C, thm:End with its whole proof, cor:End,
Rem. E-B, Rem. E-restart); sec_B.tex lines 30–310 (Lemmas B-V, B-VC, B-1, B-2, B-3, B-4, B-C); sec_T2.tex lines 1–225
(working fronts, Lemma T2-W, (H_T)); sec_T1.tex thm:HT with its proof (lines 985–1135).
Own code: `code/referee/Q2_2/` (`consts_old.py` + output `consts_old_out.txt`; `q2sim.py` + `designT.py` (copy of the
RP8b-2 simulator) + `out_*.json`).

## Verdict summary

| Claim | Verdict |
|---|---|
| (F1)–(F4) checked on the refereed proof of thm:End (core = old) | **OK**: I re-derived the list from the proof (see §1). |
| Theorem Q2.E′ (excused tail), core = old | **OK** (one optional wording fix, §2.2) |
| Theorem Q2.E′, core = End\* | conditional on End\* and (F1)–(F4) for End\*, as stated; correctly labelled |
| Lemma Q2.H (heading up to W₁) | **OK with fix**: add the side condition δ₀ ≥ ε (used, not listed) |
| Theorem Q2.D (departure, shifted data) | **OK** |
| Theorem Q2.M, core = old, v₀ = 4.7·10⁻¹⁵ (a′ = ½) / 9.7·10⁻¹³ (a′ = 0.99) | **OK with fixes** (apply Q2.D with the actual duration; δ₀ ≥ ε; list the parameter values; upstream caveat on (T1\*), §5) |
| Separation proved / conditional on End\* / provisional Q3 data | **OK** in the claims file (status lines in §0, §4.3, §5); see §6 for two presentational requests |

No FALSE statement and no GAP in the Q2 logic itself. The one substantive dependency I want flagged in the status line
is upstream: the (T1\*) bound of thm:HT is used *exactly* on the tail pairs (pairs next to E_Y), and the proof of (T1)
in sec_T1 contains a reversed inequality on precisely those pairs (§5).

---------------------------------------------------------------------------------------------------------------------
## 1. Re-derivation of (F1)–(F4) from the proof of thm:End

I went through Steps 1–5 and the closing argument and listed every pair and every label whose bounds enter the proof of
(Imp) for a family pair (a,b) at time t (base a_j at the time t′ ≤ t considered):

* Step 1(d) (E-star) at labels s ∈ [a,b]; it uses (CA) only for the pair (a_j, s) (plus Lemma B-C(4)).
* Step 2 (tilt lemma, J ⊂ I = (a,b)): arcs (a′,b_k) ⊂ I, (a′_k,b) with a′_k ≥ a_{j+1}, (a_{j+1},b) ⊂ (a_j,b); (CA) for
  these (c(J₁) ≥ λ_{J₁}/2). Right ends ≤ b.
* Step 3: ρ_m from (E-star) at a only (hull ⊂ B(x_a,l)); forcing for g ≤ R/2: (a′,a), (a,b), (a′,b), a′ ∈ {a_j,a_{j+1}};
  forcing for g > R/2: geometry only; amplification: gap spacing (E-1c); start datum N(t_s) with the weight of (S2).
* Step 4: (E-star) at all s ∈ [a,b]; J_y ⊂ (a,b); (a′,a),(a′,b); J₀ = (a′, u_{a′}+ε/2) ⊂ (a′,b) (it ends before b since
  u_{a′} < u_a and λ ≥ ε/2); I = (a_j,a_{j+1}) in the case a_{j+1} > b; start datum E at the start of the near period.
* Step 5: far: ρ_m, |p_a| as in Step 3 and (J1),(J2) of (a,b) itself; near: (J1) of J_y.
* Closing argument: |E′| ≤ (4v/ε)l, l′ ≤ (2v/ε)l for the pair itself, F(t) ⊂ F(t\*).
* Step 1(a): (a_j,s) with u_s = u_{a_j}+ε/2 and, in case (β), (a_{j−1},b_E).

So every pair used lies in [a_{j(t′)}, max(b, a_{j(t′)+1})], every label used for (E-star) lies in [a,b], and the start
time enters Steps 3 and 5 only through the left end of the time integrals and the start data. This is (F1)–(F4). For
(F2) I checked that with t′ = t_w the "first term" of Step 3 is A₀(min(g_w,32R)/ĝ₂)^ν N(t_w) ≤ 2·(M/8)λ^{1/2+γ}
(64λ/ĝ₂)^ν, i.e. the same M/4 as in the paper (A₀ ≤ 2 is a bound for the integral over any subinterval of [t_s,T_end]).
For (F3): l(t) ≤ l(t_w)·exp(8·10⁻⁶γ + 146v/γ) + 3618vλ ≤ (1+δ_T)·1.00001·λ (the far rate for g ≤ R/2 uses λ ≤ l and
(J1) with 9/8 of the pair itself, both available under the continuity hypothesis).

## 2. Coverage table (my own; core = old, labels at t_td, W₁ = 32R, U ≥ 2W₁ + 65R + ε)

Times: Part 1 = [t_td, t_w] (base u_{a_j} < W₁ at every leg start before t_w); Part 2 = [t_w, T_stop].
Family = pairs with ε/2 ≤ λ ≤ R and (a = base or a ≥ next base); it only shrinks, so no pair is ever "created".

| Pair class (in F(t)) | Part 1 | at t_w | Part 2 |
|---|---|---|---|
| body–body, u′_a > u′_b ≥ W₁ | body bootstrap (all sub-pairs used have right end ≤ max(b,a_{j+1}), u′ ≥ min(u′_b, U−W₁−ε) ≥ W₁; (E-star) at s∈[a,b] since (a_j,s) good) | Part 1 bounds (strict, (Imp)) | continuity; history on Part 1 from Part 1, on [t_w,t] all pairs from continuity |
| straddling W₁ (u′_a ≥ W₁ > u′_b) — tail by definition | **excused** (nothing claimed or used) | (TW) via Q2.D: l ≤ (1+δ_t)λ, N ≤ s₀Mλ^{1/2+γ}(K_fλ/K_RR)^ν, g_w ≥ 64R ≥ 64λ | (F2) far phase from t_w, then Step 4 from the far value, (F3) |
| tail–tail (u′_a < W₁) | excused | (TW) | as above |
| base pairs (a_j, b), u_{a_j} < W₁ | λ ≤ R ⇒ u′_b ≥ U−W₁−R ≥ W₁: body | body | — |
| (a_{j_w−1}, b) ∈ F(t_w) (switching-time convention) | body (u_a < W₁, λ ≤ R ⇒ u′_b > U−W₁−R ≥ W₁) | body | — |
| base pairs (a_j,b) with u_{a_j} ≥ W₁, b in tail (only near the end) | — | — | were far at t_w (a > W₁+ε), became near later: Step 3 then Step 4, continuity |
| (a_{j−1}, b_E) of Step 1(β) at the very end | — | — | tail pair, continuity hypothesis (J1); (β) arithmetic needs only κ₁ = 9/8 |
| (a_j,s) for (E-star), s in body | good ⇒ (CA′) | good | good |
| (a_j,s) for (E-star), s in tail, u_{a_j} < W₁ | **bad** (λ > U−2W₁): (E-star) unavailable — but never used (s ∉ [a,b] for any body pair, and tail pairs are not estimated in Part 1) | — | base ≥ W₁: good |
| (a_j,a_{j+1}) (proviso of T2-W(c)) | body, good, c > 0 | good | good |
| bad pairs in general | λ > U−2W₁ > R: not in any family; (CA) never claimed for them | — | — |

No pair/time is uncovered. In particular: (i) at t_w the family is still that of leg j_w; its pairs with first point
a_{j_w−1} are body pairs (u′_b ≥ U − W₁ − R ≥ W₁), and its tail pairs all have a ≥ a_{j_w}, so the gap used in (TW),
u_a − u_{a_{j_w}}, is the gap of the family of leg j_w+1, consistent with the convention of sec_E; (ii) no tail pair can
be near at t_w (g_w ≥ U − U_E − W₁ − ε ≥ 64R ≥ 64λ); (iii) a final leg cannot occur in Part 1 (it needs
U − u_{a_j} ≤ ε).

### 2.1 Attempts to break the excused tail
* *Body pair using a tail sub-pair through the tilt lemma*: impossible, all Step-2 arcs have right end ≤ b.
* *Body pair using a tail pair through near Term II*: the only pair outside (a,b) is I = (a_j,a_{j+1}) when a_{j+1} > b;
  in Part 1, u′_{a_{j+1}} ≥ U − W₁ − ε ≥ W₁, body.
* *(E-star) at a tail label*: only labels in [a,b] are used; Step 3 with g > 32R uses (E-star) at a, and (a_j,a) is good
  because u′_a > u′_b ≥ W₁ (this is where a "bad" (a_j,a) could have bitten — it cannot).
* *The base crossing W₁*: handled by the switching-time convention as in (i) above.
* *The tail as the final end*: the end-specific part of thm:End is only Step 1(a)(β) and (b); they use (J1) at leg starts
  for (a_{j−1},b_E) and (a_j,s), which in Part 2 are covered by the continuity hypothesis for *all* pairs. The modified tail
  data enter only through (TW) (strict at t_w since s₀ < 1 and (1+δ_t)·1.00001 < 9/8), so the end-of-arc part applies
  unchanged. There is no separate "end estimate" in thm:End that would need (S1)/(S2) of the tail at t_s.

### 2.2 Wording fix for Q2.E′
Part 1 says "(J1\*),(J2\*) hold for body pairs on [t_s,t_w]"; add "including the pairs of F(t_w) = family of leg j_w
(those with a = a_{j_w−1} are body pairs because λ ≤ R and U ≥ 2W₁ + R + ε)". Optional but helpful.

## 3. Lemma Q2.H
Checked every line: Step 1 (J ⊂ I same left end, e_J(t_j) = û_{j+1} by Lemma B-C(2): x_{a_j}, P, x_{a_{j+1}} collinear with
fixed direction during the leg); Step 2 (|e_I − n̂| ≤ σ(1+σ/2)/(1−σ²/2)); Step 3 (α) the decompositions
r_a = c(K₁)e_{K₁} + ρ′û_{i+1}, r_b = c(K₂)e_{K₂} + ρ′û_{i+1}, the tilt chain with C₃ = 2C_B + C_A, ψ(x) ≤ min(1,2x); (β)
|e_I × (r̂_b − r̂_a)| ≤ c_I/max(ρ_a,ρ_b); durations (close-case time ≤ κ_adv R₁/(1−v) using κ_adv ≥ 1); K_rot,
θ_{h1}, ω₀, θ_h; Step 4 and the time bound t_j − t_s ≥ (1 − m₁²/2)u_{a_j} (closing speed ≤ 1, c ≥ λ(1−m₁²/2)). All correct.
**Fix:** the proof uses λ_I = min(Λ,δ₀) ∈ [ε,δ₀] (so that I ∈ F_A, λ_I ≥ ε/2); this needs **δ₀ ≥ ε** (or ≥ ε/2), which is
not in the H-list of §4.2. It holds with room in the actual choice (δ₀ = R/2 ≈ 2.6·10⁻⁷ vs ε_\* ≈ 1.1·10⁻¹⁷). Add it.

## 4. Theorem Q2.D
Checked (i)–(v) line by line, including: z′ ≥ (1−h²)^{1/2} − v; z_s(0) ≥ z₀ + (1−ω̄²/2)u_s ≥ ζX_s; the y-equation
y′ = (v/ρ)y − û×P′ (ρ ≥ ε); (∗); the 𝔭-equation ∂_t𝔭 = v[(T−û)·AT − (T·AT)𝔭] (Lemma B-1(ii)) and |q_û| ≤ |y|/ρ²;
the two integrals giving Θ₀ (needs ε ≤ z₀ and η < γ); K_w (the min-split at x_c gives ω₀²L_h); Phase 1 via Lemma
B-3(b) (N′ ≤ v‖AT‖, ‖AT‖ ≤ l^{1/2} sup|T×r̂|/ρ); Phase 2 via Lemma B-3(e) with ρ_m ≥ ζ(g̃+τ) ≥ ζkλ ≥ 4(1+δ_t)λ ≥ 4l;
|p_a| ≤ ρ_a|û×e| + |y_a| with |û×e| ≤ (l/c)sup δ; X_b ≤ (1+1/k)(g̃+τ′); ρ_a ≤ (1+ω̄_y+v)(g̃+τ′); c_n, c_β. All correct.
Remark: the hypothesis (D2) must hold on the whole [0,D]; see fix (M1) below for how it is applied.

## 5. Theorem Q2.M (core = old)

### 5.1 Logic
Steps 1–7 check, with these fixes:
* **(M1) Duration.** Step 4 applies Q2.D with "D of step 2", which is the *bound* (κ_adv W₁ + ε)/(1−v) on t_w − t_td.
  Hypothesis (D2) is only available on [0, t_w − t_td] (Lemma Q2.H covers legs with base < W₁; after t_w the heading is not
  controlled). Text fix: "Apply Theorem Q2.D with duration D_act := t_w − t_td ≤ D. All constants of Q2.D (X\*, L_h, K_w,
  δ_t, θ₀ through X\*, Θ_p, and (TS)) are non-decreasing in the duration, so the side conditions at D imply those at D_act,
  and the conclusions at τ = D_act are those used in step 5." (Also in step 5: "1 + D_act/(kλ) ≤ (R/λ)(1 + D/(kR))".)
* **(M2)** add δ₀ ≥ ε to the H-list (from §3).
* **(M3)** Step 5 is fine: tail pairs lie in the departure arc (u′_a < W₁ + R = U_E), g_w ≥ U − U_E − W₁ − ε, the target
  inequality min(1, K_fλ/(K_RR)) ≥ min(1,K_f/K_R)(λ/R) and the exponent bookkeeping (a′ − η_N − γ − ν ≥ 0,
  γ_D − η_N − γ − ν ≥ 0, with η_N, ν at the actual v ≤ v₀ and γ_D fixed at v₀) are right.
* Step 6: (S1′) for good pairs with λ > λ₀: u_a + u′_b ≥ W₁ ⇒ c ≥ min(c_sep, κ₂W₁) = min(0.024, 16R) = 16R. Correct; there
  are no bad pairs with λ ≤ λ₀ (bad ⇒ λ > U − 2W₁ ≥ 1 − 64R).

### 5.2 Constants (independent recomputation, `code/referee/Q2_2/consts_old.py`, 40 digits)
Choice: ω̄ = ½, k_fac = 1, δ₀ = R/2, γ = ¼ − 10⁻⁹, R from C₀R^{a′} = 0.999999·γ/400, v₀ from v(4U_max+2) = 10⁻⁶γR.

| | a′ = ½, C₀ = 0.86 | a′ = 0.99, C₀ = 5.4·40^{−0.009997} = 5.2045 |
|---|---|---|
| R | 5.2816·10⁻⁷ | 1.0962·10⁻⁴ |
| W₁ = 32R, U_E, U_A | 1.69·10⁻⁵, 1.74·10⁻⁵, 1.77·10⁻⁵ | 3.51·10⁻³, 3.62·10⁻³, 3.67·10⁻³ |
| D, X\* | 3.38·10⁻⁵, 5.12·10⁻⁵ | 7.02·10⁻³, 1.06·10⁻² |
| ε_\* | 1.14·10⁻¹⁷ | 4.89·10⁻¹³ |
| ω₀, θ_h | 0.2775, 12.24 | 0.2835, 3.30 |
| θ₀, θ_y, ω̄_y, ω_T | 1.0·10⁻³, 0.742, 0.063, 8.5·10⁻⁵ | 0.0549, 0.742, 0.238, 0.0176 |
| K = c_nΘ_b + c_βΘ_p, k | 118.5, 4.619 | 37.3, 4.619 |
| δ_t | 7.8·10⁻¹⁵ | 2.0·10⁻¹² |
| (TS)/(s₀m) | 0.999999 | 0.999999 |
| **v₀** | **4.7157·10⁻¹⁵** | **9.788·10⁻¹³** (strict inequality needs a hair less) |

Every side condition of §4.2 (main core, stage A, H, D, TW, plus δ₀ ≥ ε) holds; spot checks at v₀/2, 10⁻³v₀ and at
ε = 10⁻³ε_\*, 10⁻¹⁰ε_\* also pass (monotonicity). Binding: v(4U_max+2) ≤ 10⁻⁶γR of the main core with R fixed by
C₀R^{a′} ≤ γ/400, i.e. exactly the cor:End value; (TS) costs only the factor 1 − O(v): **no assembly condition binds**,
as claimed. The claimed 4.7·10⁻¹⁵ and 9.7·10⁻¹³ are confirmed (the latter with slack).

### 5.3 Upstream caveat (affects the status line "PROVED for core = old")
Step 5 uses (T1\*) of thm:HT, N ≤ C₀λ^{1/2+a′} at t_td, on the **tail pairs next to E_Y**. In the proof of thm:HT (sec_T1,
"(T1), far case", line ≈1066) the tail curvature bound 1.0001ε^{−μ_T} is converted by "ε^{−μ_T} ≤ (2λ)^{−μ_T}", which is
reversed (λ ≥ ε/2 gives ε^{−μ_T} ≥ (2λ)^{−μ_T}). I confirm the error (as reported by stream Q3). It bites only for
astronomically small ε, and an obvious repair exists (integrate |k| ≤ 1.0001ξ^{−μ_T} with ξ ≥ ξ_e + u′/1.015 over the pair:
angle oscillation ≲ λ^{1−μ_T}, hence N ≲ λ^{3/2−μ_T}; Q3 reports 4.15 < 5.4), so the constants 0.86 / 5.21 should stand.
But until sec_T1 is corrected the status of Q2.M (core = old) is "PROVED modulo the repair of the (T1) proof of thm:HT".
Please put this in §4.3/§5.

## 6. Proved vs conditional (End\*, Q3)
The claims file is clear: §0 status labels, §4.3 ("PROVED for core = old; PROVED modulo [End\*] and (F1)–(F4) for
End\*"), §5. Two requests: (a) the v₀ values themselves (4.7·10⁻¹⁵, 9.7·10⁻¹³, and the End\*/Q3 values 9.9·10⁻⁷,
3.9·10⁻⁵ quoted in STATE.md) and the parameter choices are not in the claims file; add a table that labels each row
PROVED (old core) / CONDITIONAL (End\*, unrefereed) / PROVISIONAL (Q3 data, unrefereed), so the numbers cannot be quoted
without their status; (b) for the paper, write Q2.E′ for core = old directly (the proof currently reads "End\*" with a
dictionary "for core = old read …"); this is presentation only.

## 7. Uniformity in ε, hidden ε-dependence
All constants are ε-free except through ε_\*-monotone quantities (G_f, ρ\*, D, z₀^max, X\*, L_h), all evaluated at ε_\*.
(D0) z₀ ≥ ε/ζ holds since z₀ ≥ 1.269ε^{1/(2−2v)} ≫ ε. T₀ = T₂ + 2U_max/(1−v₀) is ε-free. The only hidden ε-use I found is
δ₀ ≥ ε (§3). The upstream (T1) issue of §5.3 is an ε-uniformity issue of thm:HT, not of Q2.

## 8. Simulation of design T (code/referee/Q2_2/q2sim.py)
True candidates (sample of ~1000 directions), working front with the field F, ε-legs, mesh h = ε/8; W₁ is a proxy
(0.02–0.05; the real W₁ ≈ 1.7·10⁻⁵ is below resolution), pair lengths ε/2…W₁/4.

| v, ε, W₁ | t_w−t_td (bound κ=2) | max N(t_w)/N(t_td) tail | max ΔN/(vλ^{3/4}) | tail stretch at t_w | min g_w/λ | min z_s/X_s | max |y_s|/X_s | head dev/(u+ε) | unseen at end |
|---|---|---|---|---|---|---|---|---|---|
| 1e-2, 3e-3, 0.05 | 0.053 (0.104) | 0.99993 | 0 | 1.000022 | 503 | 0.997 | 0.073 | ≤ 0.996 | 0 / 0 |
| 1e-3, 1e-3, 0.05 | 0.051 (0.101) | 1.00018 | 1.7e-4 | 1.0000016 | 491 | 0.998 | 0.054 | ≤ 0.992 | 0 / 0 |
| 1e-4, 1e-3, 0.02 | 0.020 (0.041) | 1.00016 | 1.5e-3 | 1.00000004 | 1239 | 0.9994 | 0.035 | ≤ 0.973 | 0 / 0 |
| 1e-5, 5e-4, 0.03 | 0.030 (0.061) | 1.0018 | 0.098 | 1.000000006 | 825 | 0.9993 | 0.035 | ≤ 0.991 | 0 / 0 |

(The 1.0018 ratio at v = 10⁻⁵ comes from pairs of length ≈ ε/2 where N is at the mesh noise level; ΔN/(vλ^{3/4}) = 0.1
is still three orders below K.)

Readings: the tail is transported essentially unchanged to t_w (N ratio 1 ± 2·10⁻⁴, increase ≪ vKλ^{1/2+γ} with K ≈ 37–118);
z_s/X_s ≈ 1 ≥ ζ = 0.866 (Q2.D(i)); |y_s|/X_s well below θ_yX^{γ}; the tail tilt at t_td is ≈ 1.0·X_s (cf. (T4\*)
1.647); the heading deviation grows like u (the front's curvature), consistent with K_fw u^{1−μ} and far below
h(τ) = min(θ_h(τ+ε)^{γ_D}, ω₀); after t_w, sup N/λ^{3/4} over tail pairs is constant to 4 digits up to the end and the
tail stretch stays ≤ 1 + 2v·T_sweep-ish (1.0002 at v = 10⁻⁴); the final approach into E_Y is regular (last l(a_J,b_E)/ε
∈ [0.25, 0.88]), and every true mesh label and every sampled true candidate is seen.
