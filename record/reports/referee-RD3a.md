# Referee report RD3a â€” Theorem D3.1 and Proposition D3.2 (`referee/D3-claims.md`)

Independent referee. Read only `referee/D3-claims.md` and `paper/main.tex` (Prop. 2.1, Lemma 2.2, Prop. 2.3,
Prop. 3.3(2), Lemmas A1, A2, A4, Lemma E1, Theorem A). Did **not** read `reports/D3-1.md`, `code/D3/`, other referee
reports, or `paper/sec_D1.tex` (Lemma D3 of sec_D1 and Prop. D6 were therefore re-derived, not checked as cited).
Code: `code/referee/D3a/constants_check.py` (mpmath, 40 digits), `code/referee/D3a/sim_W.py` (simulation of the path),
output `out_sims.txt`.

Problem statement: matches the task exactly (speed â‰¤ 1, H(0) = 0, path fixed in advance depending on v, d, Îµ only;
S' = v(Sâˆ’H)/|Sâˆ’H|, S(0) = e^{iÎ±}; seen iff Ï â‰¤ Îµ at some time; d = 1). No silent change found. The path of D3.1 depends
only on (v, Îµ): each Î“_k is computed from the flow of *all* directions under the already-fixed path on [0, Ï„_k].

## Summary of verdicts

| Item | Verdict |
|---|---|
| Theorem D3.1 (statement) | **OK** (with a remark on its range vs Theorem A) |
| Path definition 1.1 (speed exactly 1, fixed in advance, termination) | OK |
| Lemma W1 (stretch 1 â‰¤ \|âˆ‚_Î¸S\| â‰¤ exp(vâˆ«1/Ï)) | OK |
| Lemma W2 (straight-run occupation) | OK |
| Lemma W3 (a) | OK (re-proved independently below; citation to sec_D1 not checked) |
| Lemma W3 (b), (c) | OK |
| Lemma W4 (chords via E1) | OK |
| Lemma W5 (layer cake) | OK |
| Elementary inequalities | OK |
| Lemma W6 (constants, all Îµ â‰¤ 0.1) | OK with fixes (one mislabelled constant; conclusion unaffected) |
| Proof 1.4 (induction, c_k â‰¤ Îµ, (H_k)â‡’(H_{k+1}), counting, coverage) | OK |
| Prop. D3.2 (a) | OK |
| Prop. D3.2 (b) | OK with fixes (which arc the hypothesis refers to) |
| Prop. D3.2 (c) | OK |
| Prop. D3.2 (d) | OK with fixes (stated as conditional â€” correctly; minor definitional gaps) |

## Theorem D3.1

### Path, speed, fixedness, termination
* Phase 1 and connectors are straight unit-speed runs; walk k is Î“_k parametrised by arclength, and Î“_k is CÂ¹ with
  |âˆ‚_Î¸Î“_k| â‰¥ 1 (W1), so H is CÂ¹ with |H'| = 1 on each walk. Continuity at junctions: connector k ends at Î“_k(b_k), the
  walk ends at X_{k+1} = H(Ï„_{k+1}). Speed is exactly 1 throughout. âœ”
* Fixed in advance: Î“_k(Î¸) = S_Î¸(Ï„_k) is determined by v, Îµ and H|_{[0,Ï„_k]}; no dependence on Î±. âœ”
* Termination: each non-final window increases b by â‰¥ â„“/M + Î· > 0 inside [Î´â‚, 2Ï€ âˆ’ Î´â‚], so at most 1 + 2Ï€M/â„“ windows. âœ”

### Lemma W1 (stretch). OK
F(t,x) = v(x âˆ’ H(t))/|x âˆ’ H(t)| is jointly continuous (H continuous, possibly with kinks) and CÂ¹ in x off {x = H(t)},
so the standard differentiability theorem applies; the variational equation and âˆ‚_t|âˆ‚S| = (v/Ï)sinÂ²Ï†|âˆ‚S| are Prop. 3.3(2).
Lower bound 1 is exact (|âˆ‚_Î¸e^{iÎ¸}| = 1 and the growth rate is â‰¥ 0). The "slightly larger open interval" step is fine:
Ï is jointly continuous and â‰¥ Ï_* on the compact [b_k, 2Ï€âˆ’Î´â‚]Ã—[0, Ï„_k], hence > 0 on a neighbourhood.

### Lemma W2. OK
x = rÂ·u has x' = v rÌ‚Â·u âˆ’ 1 â‰¤ âˆ’(1 âˆ’ v), and {Ï < r} âŠ‚ {|x| < r}. (Holds on connectors too, though the proof only uses it in
Phase 1 and bounds connectors by their duration.)

### Lemma W3. OK
(a) Independent proof (valid for all v â‰¤ 1/2, 0 < Î¸ â‰¤ Î´â‚, Îµ < 1), since I did not read sec_D1: on Phase 1,
h(t_Îµ) = cos Î¸ âˆ’ 1 + (1+v)Îµ/2 âˆˆ (0, (1+v)Îµ/2] (because 1 âˆ’ cos Î¸ â‰¤ Î¸Â²/2 â‰¤ (0.3Îµ)Â²/2), and C = g(Î¸) â‰¤ 2^v Î¸^{1âˆ’v} â‰¤ 2^vÂ·0.3Îµ.
If Ï(t_Îµ) > Îµ then cos Î² + v = h/Ï < (1+v)/2, so Î² âˆˆ (arccos((1âˆ’v)/2), arccos(âˆ’v)), where sin Î² â‰¥ âˆš3/2 and
tan(Î²/2) â‰¤ âˆš((1+v)/(1âˆ’v)) â‰¤ âˆš3; then Ï = C tan^v(Î²/2)/sin Î² â‰¤ 2^{1/2}Â·0.3Â·3^{1/4}Â·(2/âˆš3) Îµ < 0.65Îµ, contradiction.
Î¸ = 0 gives Ï = Îµ/2 exactly. Numerically (exact integrals, `constants_check.py`) max_{0<Î¸â‰¤Î´â‚} Ï_Î¸(t_Îµ)/Îµ = 0.578â€“0.582
at v = v_W(Îµ) for Îµ âˆˆ {0.1, 0.01, 10â»â¶}, and 0.521 at v = 1/2. Recommend replacing the citation by this 4-line proof.
(b) Ï = g(Î¸)/g(Î²) â‰¥ g(Î¸)/g_max; monotonicity of g on (0, arccos v] (Lemma 2.2) and Ï' = v âˆ’ cos Î² â‰¥ 0 once Î² â‰¥ arccos v. âœ”
(c) y' = v y/Ï with Harry on the x-axis. âœ”

### Lemma W4. OK â€” E1 applies to exactly the quantity used
E1 gives |S_Î¸(t) âˆ’ S_Î¸'(t)| non-decreasing on any interval where Ï_Î¸, Ï_Î¸' > 0, hence â‰¥ |e^{iÎ¸} âˆ’ e^{iÎ¸'}| = chord.
In the proof it is used only at window starts Ï„_j, for pairs (Î¸, b_j) or (Î¸, Î¸') with Î¸' âˆˆ [b_j, a_{j+1}], all of which
lie in [b_j, 2Ï€âˆ’Î´â‚] and so have Ï â‰¥ Ï_* > 0 on [0, Ï„_j] by (H_j)(i). The drift after Ï„_j is then bounded crudely by vÂ·(elapsed
time) and Harry's offset from Î“_j(Â·). This is legitimate: no use of E1 is made for already-seen directions or across catches.

### Lemma W5. OK
âˆ«1/Ï = âˆ«_0^âˆž m(r) râ»Â² dr (substitution r = 1/y); the three ranges give A log(R/Ï_*) + B(1/Ï_* âˆ’ 1/R) + T/R.

### Elementary inequalities. OK
Arc {Î¸': chord < x} has measure 4 arcsin(x/2) â‰¤ (2Ï€/3)x for x â‰¤ 1 (arcsin convex on [0,1/2], equality at 1/2).

### Lemma W6 (constants). OK with fixes
Recomputed exactly (mpmath) on Îµ âˆˆ {0.1, 10^{-1.2}, â€¦, 10â»Â³â°â°} Ã— v âˆˆ {v_W, v_W/2, v_W/10}: (C0)â€“(C3) and T_* â‰¤ 22.8 hold at
every grid point. At v = v_W(Îµ): Ï_*/Îµ = Ï_w/Îµ âˆˆ [0.178, 0.190] (binding constraint is Ï_w), vJ_* âˆˆ [0.9526, 1.0081] vs
log 3 = 1.0986 (worst at Îµ = 0.1), T_* â‰¤ 22.13. All quoted numbers reproduced: f â‰¥ 0.8898 (I get 0.89014 with v â‰¤ 0.0118),
g_max(0.015) = 1.000113, Ï_w â‰¥ 0.174957Îµ, A_c = 9.25612, b_c = 4.67918, T_c = 22.79222, additive constant 7.36720,
log 3/A_c = 0.118690, v_W(10â»Â¹, 10â»Â², 10â»â¶, 10â»Â¹Â²) = 0.01173, 0.00950, 0.005395, 0.003273.

*Small-Îµ asymptotics (analytic).* Every bound in W6 is uniform in Îµ: Ï_* â‰¥ 0.17495Îµ, A â‰¤ A_c, B â‰¤ b_c Îµ, T_* â‰¤ T_c, so
v J_* â‰¤ v A_c (log(1/Îµ) + 7.3672) â‰¤ 0.115 A_c (log(1/Îµ)+7.3672)/(log(1/Îµ)+7.5) < 0.115 A_c = 1.0645 < log 3 for every
Îµ âˆˆ (0, 0.1]; the only Îµ-dependence of f is through v log(1/(0.3Îµ)) â‰¤ 0.115, which is exactly what v â‰¤ v_W enforces. As
Îµ â†’ 0, v_W J_* â†’ 0.115(2 + 2Ï€) = 0.9526 (numerics agree: 0.95261 at Îµ = 10â»Â³â°â°). So "for all Îµ â‰¤ 0.1" is genuinely proved.

*Fix (cosmetic).* "T_* â‰¤ T_c = 22.7923 (values at v = v_c, Îµ = 0.1)" â€” 22.7923 is **not** T_* at (v_c, 0.1) (that is 22.7415);
it is t_Îµ bounded by 1/(1âˆ’v_c) plus Îµ bounded by 0.1. Replacement text:
> "T_* â‰¤ T_c := 1/(1âˆ’v_c) + 0.1 + 2Ï€M(1 + v_c/Î») = 22.7923 (using t_Îµ â‰¤ 1/(1âˆ’v), Îµ â‰¤ 0.1, v â‰¤ v_c)."

Also "(all bounds monotone in v, worst case v = v_c)" should read "â€¦ worst case v = v_c, except f, which is bounded via
v log(1/(0.3Îµ)) â‰¤ 0.115".

### Proof 1.4. OK
Checked line by line:
* **c_k â‰¤ Îµ** (k â‰¥ 2): |S_{b_k}(Ï„_k) âˆ’ S_{b_k}(Ï„_{kâˆ’1})| â‰¤ v(c_{kâˆ’1}+â„“) â‰¤ (v+Î»)Îµ; the arc of Î“_{kâˆ’1} over [a_k, b_k] has
  length â‰¤ MÎ· since [a_k, b_k] âŠ‚ [b_{kâˆ’1}, 2Ï€âˆ’Î´â‚] (b_k < 2Ï€âˆ’Î´â‚ because window k exists). (C1): v + Î» + MÎº â‰¤ 0.9818 at v_W(0.1).
* **Connector bounds.** Î¸ âˆ’ b_k â‰¥ â„“/M + Î· requires walk k to be non-final, which holds when window k+1 exists. For k â‰¥ 2,
  b_k â‰¥ Î´â‚ + â„“/M + Î· gives the wrap-around distance. For k = 1 the half-plane argument (W3(c), connector-1 segment in
  {y â‰¥ 0}, y_Î¸(t_Îµ) â‰¤ sin Î¸ â‰¤ âˆ’sin Î´â‚ on (Ï€+Î´â‚, 2Ï€âˆ’Î´â‚]) is correct.
* **Walk bounds.** Î¸ âˆ’ Î¸' â‰¥ b_{k+1} âˆ’ a_{k+1} = Î· and 2Ï€ âˆ’ (Î¸âˆ’Î¸') â‰¥ 2Î´â‚; dist â‰¥ min(Î·, 2Î´â‚) = Î·. âœ”
* **Occupation m(r)** (A, B as stated): walks â‰¤ WM(r + (Î»+v)Îµ) using disjointness of walked Î¸-ranges and |âˆ‚Î“_j| â‰¤ M;
  connectors j â‰¥ 2: b_j's are â‰¥ â„“/M apart, an arc meets [Î´â‚, 2Ï€âˆ’Î´â‚] in â‰¤ 2 intervals, so â‰¤ 2 + W(r+(1+v)Îµ)M/â„“ of them, each
  â‰¤ Îµ; connector 1 â‰¤ Îµ. Arithmetic with ÎµM/â„“ = Mv/Î» gives exactly A and B. (C0) ensures r + (1+v)Îµ â‰¤ 1. âœ”
* **Counting facts.** Î£â„“_j â‰¤ MÂ·2Ï€, #windows â‰¤ 1 + 2Ï€M/â„“, Î£c_j â‰¤ Îµ + 2Ï€Mv/Î» â‡’ Ï„_j â‰¤ T_*. These use (H_j) only for
  j â‰¤ k, so no circularity. âœ”
* **Skip of 0.29Îµ (attack point).** Skipped Î¸ âˆˆ (a_{k+1}, b_{k+1}) are seen **at Ï„_{k+1}** (start of connector k+1), not
  later: Ï_Î¸(Ï„_{k+1}) â‰¤ v(c_k + â„“_k) + M(Î¸ âˆ’ a_{k+1}) â‰¤ (v + Î» + MÎº)Îµ â‰¤ Îµ, using |âˆ‚Î“_k| â‰¤ M on [a_{k+1}, Î¸] âŠ‚ [b_k, 2Ï€âˆ’Î´â‚].
  In the final window with b_{k+1} â‰¥ 2Ï€âˆ’Î´â‚ the skipped set is [a_{k+1}, 2Ï€âˆ’Î´â‚], same estimate. âœ”
* **Walked Î¸** seen at s_Î¸ with Ï â‰¤ (v+Î»)Îµ. **Ends of the sweep:** [âˆ’Î´â‚, Î´â‚] by W3(a) (at t_Îµ); [bâ‚ = Î´â‚, â€¦] contiguous
  through walked/skipped pieces up to 2Ï€ âˆ’ Î´â‚; the start tip and the far end therefore both covered. âœ”
* **Time.** Every Ï„_j â‰¤ T_* â‰¤ 22.8 (actually â‰¤ 22.13 for v â‰¤ v_W, per the exact table). âœ”

### Simulation of the explicit path (`sim_W.py`)
Dense sample: 60 000 equispaced + 6 000 random directions, RK4, Î“_k = polyline through the tracked S_Î¸(Ï„_k), Harry walks it
at unit speed. Results:

| (Îµ, v) | windows | final Ï„ | max c_k/Îµ | max \|âˆ‚Î“_k\| | min Ï (active, at Ï„_k)/Îµ | max vâˆ«1/Ï | unseen | max_Î± min_t Ï/Îµ |
|---|---|---|---|---|---|---|---|---|
| (0.1, v_W = 0.011732), dt 5e-4 | 8 | 7.452 | 0.578 | 1.063 | 0.396 | 0.131 | 0 / 66 000 | 0.294 |
| (0.01, v_W = 0.009500), dt 2e-4 | 60 | 7.464 | 0.581 | 1.073 | 0.397 | 0.178 | 0 / 66 000 | 0.283 |

Every sampled direction is seen (worst closest approach 0.29Îµ), c_1 matches the exact Phase-1 value 0.578Îµ, the stretch
stays â‰¤ 1.07 (the proof's bound 3 is very loose but valid), and all bounds of the proof (Ï_* â‰ˆ 0.18Îµ, vJ_* â‰¤ log 3,
T â‰¤ 22.8) hold with large slack. The simulation discretises Î“_k as a polyline (speed exactly 1 along it) â€” evidence, not proof.

### Remark on the range (not an error)
Theorem A (main.tex) already gives a win for v â‰¤ Îµ/(1+2Ï€). This exceeds v_W(Îµ) for Îµ > 0.0839 (e.g. at Îµ = 0.1:
0.01376 vs 0.01173). So D3.1 is new only for Îµ < 0.084; suggest saying so next to the comparison sentence, e.g.
> "(For Îµ > 0.084 Theorem A gives the larger range; D3.1 improves on it for Îµ < 0.084, by a factor â‰ 1/(Îµ log(1/Îµ)).)"
The comparison with "Theorem D1" was not checked (outside reading scope).

## Proposition D3.2

**Stated as conditional?** Yes: the header says "(d) is a conditional theorem, PROVED as a reduction", and (d) begins
"Suppose (O) holds at every t â‰¥ tâ‚€ of LG0". âœ” (O) is never claimed to hold.

**Definitional fix needed throughout.** Î±*(t) := inf U(t) is not constant during a leg (the target is itself seen, and
directions just above it may be seen, before Ï_{Î±*} reaches Îµ/2), whereas "(Î²(Î±*) = 0)" and the proofs treat Î±* as the
leg's target. Replacement text for the LG0 paragraph:
> "At the start time t_j of each leg set Î±*_j := inf U(t_j) (the target; note Î±*_j âˆ‰ U(t_j) since U is open, but
> Ï_{Î±*_j} â‰¥ Îµ on [0, t_j] by continuity), and run straight at S_{Î±*_j} until Ï_{Î±*_j} = Îµ/2. During that leg,
> Î±*(t) := Î±*_j, Î±_e(t) := sup U(t), and Î›(t) := length of ð’œ(t) = âˆ«_{Î±*(t)}^{Î±_e(t)} |âˆ‚_Î±S(Î±, t)| dÎ±."
(Î› is used in (d) but never defined.)

**(a) OK.** Lemma A1's proof is pointwise in Î±; at tâ‚€ only Î± = 0 has been caught (Prop. 2.3), so all Î± âˆˆ [Î±*, Î±_e] âŠ‚ (0, 2Ï€)
are defined; bearings from the new heading lie in [0, 2 arccos v) âŠ‚ [0, Ï€), strictly increasing.

**(b) OK with fix.** The affine argument is right (k strictly decreasing, C_P, C_Q > 0 for bearings in (0, Ï€), A2 keeps
bearings in (0, Ï€) and the rays invariant). But the conclusion "(O) at every interior time" concerns pairs in
[Î±*, Î±_e(t)], which may contain points that leave the arc before the leg ends; the hypothesis must cover them. Replace
"the bearing order of every pair of arc points is (weakly) correct at the end of the leg" by
> "every pair P < Q in [Î±*, Î±_e(t_start)] has Î²_P â‰¤ Î²_Q at the end of the leg".

**(c) OK.** New bearings are old minus b on [Î±**, Î±_e] âŠ‚ [Î±*, Î±_e]; values in [0, Ï€ âˆ’ b]. ("(O) at the end time as a limit"
must mean strict monotonicity at that time; it is a hypothesis, so fine.)

**(d) OK with fixes (as a conditional reduction).** Checked: no arc point other than the target is caught (Prop. 2.3 + (O));
L_I' â‰¤ vâˆ«_I|âˆ‚_Î±Î²| â‰¤ vÏ€ via sinÂ²Ï†|âˆ‚S|/Ï â‰¤ |âˆ‚_Î±Î²|; Î›(tâ‚‚) âˆ’ Î›(tâ‚) â‰¤ vÏ€(tâ‚‚ âˆ’ tâ‚); Î¨' â‰¤ âˆ’(1 âˆ’ v(1+Ï€)) inside legs; at
switches Î¨_new = Ï_{Î±**} + Î›_new â‰¤ Îµ/2 + |arc(Î±*, Î±**)| + Î›_new = Î¨_old; legs last â‰¥ Îµ/(2(1âˆ’v)) because Ï_{Î±**} â‰¥ Îµ at the
switch (limit of unseen directions); Î¨(tâ‚€) â‰¤ 2Ï€/(1âˆ’v) via Prop. 3.3(2) and Prop. "Angle at first contact" (prop:V) for the piece near Î± = 0.
Fixes:
1. The compact set should be {(Î±, s): Î± âˆˆ [Î±*, Î±_e(tâ‚‚)], s âˆˆ [0, tâ‚‚]} â€” positivity is needed on the whole history for
   âˆ‚_Î±S to exist, and Î± âˆˆ (Î±_e(tâ‚‚), Î±_e(tâ‚)] is not needed. Replacement:
   > "every Î± âˆˆ I := [Î±*, Î±_e(tâ‚‚)] lies in ð’œ(s) for all s â‰¤ tâ‚‚ (Î±* non-decreasing, Î±_e non-increasing), is not the target
   > of any leg before tâ‚‚ except possibly Î± = Î±*, hence by (O) and Prop. 2.3 is never caught on [0, tâ‚‚] (and Ï_{Î±*} â‰¥ Îµ/2);
   > so Ï is continuous and positive on I Ã— [0, tâ‚‚], hence bounded below."
2. Prop. D6(a), (b) are cited from outside main.tex; the two facts used (U open; Ï_{Î±*} â‰¥ Îµ at a leg start; the switch
   inequality) are elementary and re-derived above.
