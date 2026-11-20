# Audit A — end-to-end audit of the typeset chain for Theorem `thm:Main` and Corollary `cor:Exact`

Auditor A, 2026-11-19. Object: `paper/main.tex` + `sec_B.tex`, `sec_ST.tex`, `sec_E.tex`, `sec_T1.tex`, `sec_T2.tex` as typeset
(`main.pdf`, 114 pp., built 17:10; `main.log` has no undefined or multiply defined reference). Nothing in `paper/` was edited.
Script: `code/audit/audit_A_constants.py`, output `code/audit/audit_A_constants.out`.

Scope of what was read line by line: all of `sec_T2.tex`; in `sec_T1.tex` the conventions, Definition `def:T`, Lemmas
`lem:T1-run1`, `lem:T1-tail`, `lem:T1-virt`, `lem:T1-bulk`, `lem:T1-edges`, `lem:T1-hole`, Proposition `prop:T1-arcs`,
Theorem `thm:HT` with proof, and the remarks; in `sec_E.tex` Lemma `lem:E-facts`, the whole of Theorem `thm:End` with
proof (Steps 1–5, (b), (c)), Remark `rem:E-B`, Corollary `cor:End`, Remark `rem:E-restart`, Lemma `lem:E-far`, the status
remark; in `sec_B.tex` everything up to Step 3 of the proof of `thm:Bulk`, Step 4 (head), the remarks, `cor:M`, status; in
`sec_ST.tex` the preamble, `lem:ST-D0`, the status remark; in `main.tex` §1–§6 (through `thm:B`), §open, §numerics.
NOT re-refereed: the interiors of `lem:T1-coord/first/second/tang/fwd` (only their statements were used), and Steps 4–5 of
`thm:Bulk` beyond what `thm:End` cites.

---------------------------------------------------------------------------------------------------------------------

## (i) Verdict

**CHAIN CLOSED.** No mathematical gap was found at any interface on the path

`sec_B` (field, excess calculus, Construction C) → `sec_E` (`thm:End`, `cor:End`) → `sec_T1` (`def:T`, `thm:HT`) →
`sec_T2` (`hyp:HT`, `lem:T2-W`, `lem:T2-A`, `thm:T2-D`, `lem:T2-H`, `lem:T2-StA`, `prop:T2-I`, `prop:T2-cond`, `thm:Main`,
`cor:Exact`) → `main.tex` (`lem:A41`, `lem:limit`).

Every cited hypothesis is available at the citing place with matching notation, constants and ranges; the twelve constants
of (H_T) in `thm:HT` (sec_T1 l.996–997) and in `eq:T2-HTconst` (sec_T2 l.720–721) are identical character for character;
all side conditions hold at exactly v = 4·10⁻⁵¹, vision radius 2·10⁻⁴⁴ (125 checks, all pass; tightest:
v(4.5U_max+2) ≤ 10⁻⁶γ_B R_B used to 96.6 %, ε ≤ R_B/64 used to 61.8 %, C_z ε^{1/4} ≤ W used to 97.7 %,
max(ϑ_T,ϑ_h)(4.2W)^{γ*} ≤ 1/20 with equality by the definition of W).

The following are **defects of the text, not of the mathematics** (none changes a statement or a constant). They should be
fixed before the paper is circulated, because each makes a sentence of the paper literally inaccurate.

| # | Location | Defect | Fix |
|---|---|---|---|
| D1 | `sec_T2.tex` l.116–121, proof of `lem:T2-W`(d): "The proofs of Theorem `thm:End` and Corollary `cor:End` cite Section `sec:bulk` only through Lemmas … and … the Claim in the proof of Theorem `thm:R`" | Incomplete list. The typeset proof of `thm:End` also argues **by reference to the proof of `thm:Bulk`**: `sec_E` l.173 ("we conclude as for Theorem B": the closing of the continuity argument), l.206 (`eq:B-1c`, "with the same proof"), l.213 (`eq:B-star`, "with the same proof"), l.282–285 (forcing β ≤ 408vλ^{3/2}/R² "exactly as in Step 3 of the proof of Theorem B"), l.330–331 and l.402 ("As in Step 4 of the proof of Theorem B": near time ≤ 264λ and the two time integrals). I checked each of the five borrowed pieces against `sec_B` l.422–427, 441–454, 515–520, Step 4: they use only the family bounds, `eq:E-CA`, Lemma `lem:B-C`(0),(2),(4), Lemma `lem:B-3`(e), spacing ≥ ε/2 of gaps and leg duration ≤ 2ε, and l ≤ 2λ — all valid on a working front and under the standing assumptions of `sec_E` (they do not use v ≤ 10⁻¹² nor M = R^{-1/4}/140). Referee RP8b-1 §"Steps 1–5" did go through them. So the conclusion of (d) is right; the sentence is not. | Add after "Lemma `lem:B-4`(b))": "and, by reference, four elementary pieces of the proof of Theorem `thm:Bulk`: the closing of the continuity argument, Step 1(c) (`eq:B-1c`), Step 1(d) (`eq:B-star`), the bound β ≤ 408vλ^{3/2}/R² of Step 3 for g > R/2, and the time count of Step 4. These use only the family bounds, `eq:E-CA`, Lemma `lem:B-C`(0),(2),(4) and Lemma `lem:B-3`(e)." |
| D2 | `sec_T2.tex` l.794–795, `rem:T2-budget`(4): "Not used from Section `sec:bulk`: Theorem `thm:Bulk`, …" | True for the *statement* of `thm:Bulk` only; see D1. | "…: the statements of Theorems `thm:Bulk` and `thm:R` and Corollary `cor:M` (four steps of the proof of Theorem `thm:Bulk` and the Claim in the proof of Theorem `thm:R` are used by reference in Section `sec:end`)." |
| D3 | `sec_T2.tex` l.806–811 (table of links) and l.839–841 ("The earlier head-on start (Section `sec:start`, Theorem `thm:ST`) … are not used") | `sec_ST.tex` **is** on the chain, through three elementary items used by `sec_T1`: Lemma `lem:ST-D0`(a) (cited in the proof of `lem:T1-virt`, sec_T1 l.706), the bound log g_max ≤ v² (sec_ST l.58–61, used as "g_max ≤ e^{v²}", sec_T1 l.72) and the notation m_ε, Γ_ε, α_s. None involves the start S or `thm:ST`. They are refereed (RP6d-1/2; RP8a-2 lists "[D] Lemma D0(a),(c) as cited"), but the table of links does not list them. | Add a row "Section `sec:start`, preliminaries only (Lemma `lem:ST-D0`(a), g_max ≤ e^{v²}) — `referee-RP6d-1.md`, `referee-RP6d-2.md`"; in "Scope" write "Theorem `thm:ST`, Corollary `cor:ST` and the start S are not used (only Lemma `lem:ST-D0`(a) and g_max ≤ e^{v²} of that section are)". |
| D4 | `sec_T2.tex` l.749–750 (caption of Table `tab:T2-const`): the archive script "also re-checks every side condition … with the rounded values v = 4·10⁻⁵¹, ε = 2·10⁻⁴⁴" | `code/P8b/final_constants.py` checks the exact values, (4.1·10⁻⁵¹, 2.1·10⁻⁴⁴) and (10⁻⁵¹, 10⁻⁴⁴), not (4·10⁻⁵¹, 2·10⁻⁴⁴). Harmless (every condition is monotone in v and ε), and now checked literally by `code/audit/audit_A_constants.py`. | Either "with the values (4.1·10⁻⁵¹, 2.1·10⁻⁴⁴), which implies them for all smaller v, ε" or cite the audit script. |
| D5 | `sec_T2.tex` l.448 "(TL)" | Local name "(TL)" for the tilt bound 0.33(λ_I/R)^{γ₁} of `thm:End`(d) collides with the typeset equation tag (TL) of `eq:B-TL` in `sec_B` (91Mλ^{1/4}); similarly `main.log` reports duplicate hyperref destinations for the tagged equations (CA), (∗), (TL). Cosmetic. | Rename to (TL$_{\mathrm E}$) or refer to `eq:E-TL`. |
| D6 | `main.tex` (abstract, remark after `lem:A41`, §`sec:open` items 1–2), status remarks of `sec_ST`, `sec_E`, `sec_B`, `sec_D2` | `main.tex` never mentions `thm:Main` or `cor:Exact`; several sentences are now false. | See (iv). |

Remarks used as lemmas: only Remark `rem:E-B`(4) (causality), cited in `lem:T2-H` (setting) and `lem:T2-StA`(b). It is a
one-line consequence of the structure of the continuity argument and was checked by RP7-2 (F10) and RP8b-1/-2. Remark
`rem:B-relaxed` (unrefereed) is cited only inside Remark `rem:E-B`(1), which is commentary; **it is not on the path**.
Remark `rem:E-restart` is explicitly not used (`rem:T2-budget`(3)); I confirm: c_I = (4/9)Λ_I is derived independently in
(E2_I), not taken from the restart remark (whose 4R₁/9 and the R/4 of the `thm:Bulk` variant are unrelated to the chain).

---------------------------------------------------------------------------------------------------------------------

## (ii) Interface table

Notation dictionary (checked): touch-down time `t_s` (sec_T1, `\Bts`) = `t_td` (sec_T2, `\Mtd`), stated in both places
(`thm:HT` l.993; sec_T2 l.141–146); heading of run 2 `û` (sec_T1) = `n̂` (sec_T2), while in `lem:T2-StA`(d) `û := −n̂`
(local); ghost set 𝒢 (`\TDG` = `\MG`); E_Y = x_{b_e}(t_s) (sec_T1) = x⁰(U) (sec_T2), equal because Θ(U) = 2π+b_e is a
true label; `t_c` (true catch time of α₀, sec_T1) is not used in sec_T2; k = curvature in sec_T1 (clash with k(β) of
`main.tex` Lemma `lem:k`, harmless: only g'/g is taken from there); κ is not used on the chain; labels u = arclength at the
leg start in sec_E, = arclength of x⁰ at t_td in sec_T2 (same thing for stage A since |∂_u x⁰| = 1), u^I = l_{t_I}(a_{j_I},·)
for stage B (as `cor:End` requires).

| # | Citing place | Cited statement | Hypotheses needed → where available | OK |
|---|---|---|---|---|
| 1 | `lem:T2-W`(a) | `lem:B-VC`(a),(b), `lem:B-1`(i),(ii), `lem:B-2`, `lem:B-3`, `lem:B-4`, `lem:E-facts` for a working front | proofs use only x' = vF(x−P), F ∈ C¹, ‖DF‖ ≤ 2/ε, A sym. ≥ 0, `lem:B-V`(iv), |∂_u x⁰| = 1, C¹ curve → all hold; C² parts `lem:B-1`(iii),(iv) not used on a working front (sec_E l.38: "The curvature is not used") | yes |
| 2 | `lem:T2-W`(b) | uniqueness for `eq:snitch` (as `lem:B-VC`(c)) | true label: S_θ defined on [0,t_w], x⁰(u) = S_θ(t_w) | yes |
| 3 | `lem:T2-W`(c) | `lem:B-C`(0),(2),(4), (3)→(3′) | proviso c(a_j,a_{j+1};t_j) > 0 replaces injectivity of θ ↦ e^{iθ} | yes |
| 4 | `lem:T2-W`(d) | `thm:End`, `cor:End` on a working front | P(0)=0 and b_E−a_s<2π used in sec_E only for `lem:B-VC`(c) and c>0 (sec_E l.101) → replaced by (b) and proviso, verified inside the continuity argument via Step 1(a) + `eq:E-CA` | yes; citation list incomplete (D1) |
| 5 | proof of `thm:End` (sec_E) | pieces of the proof of `thm:Bulk`; `eq:B-1c`, `eq:B-star`; Claim in proof of `thm:R` (part (c) only, not used by `thm:Main`) | family bounds (J1),(J2), l ≤ 2λ, `eq:E-CA`, legs ≤ 2ε, gaps spaced ≥ ε/2 → Step 1 of `thm:End` | yes (D1) |
| 6 | `lem:T2-A` | `lem:B-2`(i), `lem:B-3`(e) | ρ_m ≥ ρ₀ ≥ max(ε,4l) from the two displayed assumptions | yes |
| 7 | `thm:T2-D` | `lem:B-1`(ii), `lem:E-facts`(b),(c)(method), `lem:B-3`(e), `lem:T2-W`(a) | (Q0)–(Q4) | yes |
| 8 | `lem:T2-H` (setting) | `thm:End`(a),(b),(d) with (γ₁,R,M), `eq:E-CA`, `rem:E-B`(4) | "hypotheses of `thm:End` hold on this arc" → supplied in `lem:T2-StA`(a); (TL) is `thm:End`(d): 0.33(λ_I/R)^{γ₁} ≤ 0.33(λ_I/R)^γ as γ ≤ γ₁, λ_I ≤ R | yes |
| 9 | `lem:T2-H` Step 3 | `lem:B-C`(2); every non-final leg advances ≥ ε/2 (`thm:End`(b)) | — | yes |
| 10 | `lem:T2-StA`(a) | `cor:End` with (a′,C₀,λ₀,c_A), U_max/2 | (E1) = (T1) on [0,U/2]; (E2) from (T2): c ≥ min(c_sep,u_b′/2) ≥ min(c_sep,U/4) ≥ c_A (U ≥ 1); C₀λ₀^{a′} ≤ 1 from (T1); λ₀ ∈ (0,1]; ε ≤ R_A/64 (`eq:T2-also`); v ≤ min(2·10⁻¹¹γ₁², 10⁻⁶γ₁R_A/(2U_max+2)) (4th entry of v₀; 4·U/2+2 = 2U+2); leg start: P(t_td) = x⁰(0) by (T0). γ, R of `cor:End` = γ₁, R_A; M_A = (γ₁/50)R_A^{−γ₁} | yes |
| 11 | `lem:T2-StA`(b) | `thm:End`(b) (advance ∈ [ε/2,ε]), `rem:E-B`(4) | construction cut at b_A coincides with the one cut at b_E while l(a_j,b_A) > ε; U/2 − W − ε > ε | yes |
| 12 | `lem:T2-StA`(c) | `lem:T2-H` with γ*=γ_*, R=R_A, ϑ_f=ϑ_T, G_f=3W | (F1) ⇐ (T3): 3W ≤ G_T, ū ≤ 1, γ_* ≤ γ_T; ϑ_T(3W)^{γ*} ≤ 1/20; 2Λ ≤ 2.02W ≤ min(3W,R_A,U/2); (2.02W/R_A)^{γ*} ≤ 1/10; v ≤ 10⁻⁴ | yes |
| 13 | `lem:T2-StA`(d) | `thm:T2-D` for the reversed tail, û = −n̂ | (Q0) ⇐ (T5) (signs checked: x⁰(U) − P = z₀(−n̂) + y₀(−n̂)^⊥, z₀ ≥ 0); (Q1) ⇐ (T4), W ≤ G_T; (Q2) ⇐ (c), |P′−n̂| ≤ 1/20; (Q3): A_* ≤ 4.2W (z₀ ≤ C_zε^{1/4} ≤ W, D ≤ 2.1W); (Q4): v ≤ 10⁻⁵γ_* | yes |
| 14 | `prop:T2-I` case (A) | (J2), (J1) of stage A at t_I; `lem:E-facts`(a) | pair in the family of leg j_I: a ≥ a_{j_I}, u_b ≤ U/2, ε/2 ≤ λ ≤ W/40 ≤ R_A | yes |
| 15 | `prop:T2-I` case (P) | `lem:B-C`(4); (T2); (T1); `lem:T2-A` | u_s − u_{a_j} ≥ U/2 − 1.04W > λ₀; ρ₀ = W/5 ≥ ε; 4λe^{vD/ρ₀} ≤ ρ₀; λ ≤ W/40 ≤ λ₀ | yes |
| 16 | `prop:T2-I` case (D) | `thm:T2-D`(iv),(v) via `lem:T2-StA`(d); (T1) | pair inside {u′ ≤ W}, λ ≥ ε/2; K_D ≤ C_I | yes |
| 17 | `prop:T2-I` (E2_I) | (T2), (T1), monotone chords (`lem:T2-W`(a)) | u_a ≥ W ⇒ min(c_sep,W/2) = W/2 ≥ c_I; λ ≥ (8/9)Λ_I ⇒ c ≥ λ/2 ≥ c_I | yes |
| 18 | `prop:T2-cond` | `cor:End` at t_I with (a_I,C_I,Λ_I,c_I), (9/8)U_max | a_I ∈ (0,1], Λ_I ∈ (0,1], C_IΛ_I^{a_I} ≤ 1 (`prop:T2-I`); γ = min(a_I/2,1/4) = γ_B; R = R_B (c_I/16 = Λ_I/36); ε ≤ R_B/64; U^I ≤ (9/8)U ≤ (9/8)U_max; v ≤ min(2·10⁻¹¹γ_B², 10⁻⁶γ_BR_B/(4.5U_max+2)); t_I is a leg start; labels u^I = arclength at t_I, as `cor:End` requires | yes |
| 19 | `prop:T2-cond` | `lem:T2-W`(c)(3′) for legs ≤ j_I; (T0) | intervals [a_j,a_{j+1}], j < j_I, cover [0,a_{j_I}] | yes |
| 20 | `prop:T2-cond` | `lem:B-C`(0) (1-Lipschitz), design T | P continuous at t₁ and at t_td (P(t_td) = X₀ = x⁰(0)) | yes |
| 21 | `thm:Main` | `thm:HT` ⇒ `hyp:HT` | statement of `thm:HT` reproduces (T0)–(T5) verbatim, with n̂ := û, x⁰, 𝒢 ⊂ [0,U), 1 ≤ U ≤ U_max, t_s ≤ T₂; constants identical; ranges v ≤ 10⁻⁶, ε ≤ 10⁻³ ⊃ (4·10⁻⁵¹, 2·10⁻⁴⁴); D₁ = 1 in both | yes |
| 22 | `thm:Main` | `prop:T2-cond`; scaling of `eq:snitch` | vision radius min(ε,2·10⁻⁴⁴) ≤ ε_* = 2.1966·10⁻⁴⁴: the proof of `prop:T2-cond` holds for any radius ≤ ε_*, and seen with a smaller radius ⇒ seen with ε | yes |
| 23 | `cor:Exact` | `lem:A41` | see task 4 below | yes |
| 24 | `lem:A41` | proof of `lem:limit` (Claim, Arzelà–Ascoli) | H_N(0) = 0 (formulation; verified in `cor:Exact`) | yes |
| 25 | `thm:HT` / `lem:T1-virt` | `lem:ST-D0`(a); `lem:B-1`(i), `lem:B-V`(ii), `lem:B-VC`(a) | virtual candidates of a 1-Lipschitz path | yes; sec_ST on the chain (D3) |
| 26 | `sec_T1` conventions | g_max ≤ e^{v²} (sec_ST l.58–61); `prop:integrals`, `eq:polar`, `lem:k` (main.tex); proofs of `lem:B-1`(i)–(iii) for the true front (A = Π/ρ); `lem:B-VC`(c) (virtual = true while ρ ≥ ε) | straight runs; ρ > 0 | yes |
| 27 | `thm:HT` (T1),(T2) | `lem:T1-elem` (re-proof of `lem:ST-D0`(c), `lem:E-facts`(b) for C¹ curves) | x⁰ is C¹ with locally Lipschitz tangent on {u ≥ 1.04ε} | yes |

Ranges of v, ε (all satisfied by v₀ = 4·10⁻⁵¹, ε = 2·10⁻⁴⁴): sec_B standing range v ≤ 10⁻¹² (needed only for the borrowed
proof pieces, which do not use it); `thm:End` v ≤ 2·10⁻¹¹γ² = 1.25·10⁻¹² (stage A, γ₁ = 1/4), 7.8·10⁻¹⁴ (stage B,
γ_B = 1/16); v(4U+2) ≤ 10⁻⁶γR: stage A 6.0·10⁻⁵⁰ ≤ 1.3·10⁻¹³, stage B ratio 0.9656; sec_T1: v ≤ 10⁻⁶, ε ≤ 10⁻³;
sec_T2: v ≤ 10⁻⁵γ_*, 1.39v ≤ γ_*/2, v ≤ W/132 = 1.4·10⁻¹³; ε ≤ R_A/64, R_B/64, W/100, Λ_I/2, (W/C_z)⁴. For ε ∈ (2·10⁻⁴⁴, 1)
the path is the one for vision radius 2·10⁻⁴⁴ (row 22).

### Task 2

`thm:Main` does not use the statement of `thm:Bulk`, `thm:R`, `cor:M`, `thm:ST`, `cor:ST`, `thm:E-dep`, `lem:E-H`, `cor:E-T`,
`thm:End`(c), nor Sections D1–D3, G. It does use, by reference, pieces of the *proof* of `thm:Bulk` (D1/D2) and three
preliminaries of `sec_ST` (D3). Nothing unrefereed is on the path (`rem:B-relaxed` is not).

### Task 3 — statement versus problem

* **Fixed in advance.** P on [0,t_td] is `def:T` (depends on v, ε′ := min(ε,2·10⁻⁴⁴); α₀ and û are computed from run 1);
  x⁰ is determined by P|[0,t_td]; each leg of Construction C is determined by P on earlier times and x⁰. For general d
  the path also depends on d (known to Harry). OK.
* **Speed ≤ 1, junctions.** Run 1 and run 2 have unit speed and share P(t₁); Construction C starts at
  P(t_td) = X₀ = x⁰(0) ((T0)), its legs have unit speed and are joined continuously; P is constant after T_stop. So P is
  continuous, piecewise linear, 1-Lipschitz, P(0) = 0. OK.
* **Every direction** (labels mod 2π; α_s ≤ 2.1ε′, b_e = α₀ − ξ_e):
  - α = 0: caught at t₀ = 1/(1−v) < t₁ on run 1, hence |S₀ − P| ≤ ε′ at an earlier time: *seen* (`lem:T1-run1`(a) is
    "iff |α| ≤ α_s" and includes α = 0; `lem:T1-hole`(d)). On x⁰ it is the ghost label carrying Z_s; nothing is needed there.
  - 0 < |α| ≤ α_s (hole): seen in run 1 (`lem:T1-run1`(a)); on x⁰ they are true labels, also covered by stage B.
  - α ∈ (α_s, b_e) (arc A₂ and the tail Γ): true labels of x⁰ (virtual = true, `lem:T1-tail`(b)); seen in stage B
    (`cor:End` at t_I; the tail is an ordinary part of the arc after the hand-over, (E1_I) case (D)).
  - α = b_e (E_Y): true label u = U ∉ 𝒢; seen in run 2 (distance exactly ε′ at one instant) and again by the final leg
    (l(a_J,b_E) ≤ ε′, (3′)).
  - α ∈ (b_e, α₀]: not on x⁰; seen in run 2 (`lem:T1-tail`(b): ranges ξ ∈ [0.35vε′, ξ_e] and (0, ε′/2] cover (0, ξ_e];
    α₀ itself at t_a).
  - α ∈ (α₀, α₀+1.02ε′): either in 𝒢 (then seen by definition of 𝒢) or true (never within ε′ ⇒ virtual = true) and seen by
    the first legs ((3′)).
  - α ∈ [α₀+1.02ε′, 2π − α_s) (forward arc and bulk): true labels; those with u ≤ u_{a_{j_I}} seen by (3′) in stage A,
    the others in stage B.
  This is exactly the last clause of (T0) plus rows 18–19. OK. "Seen" in `main.tex` is |S_α − H| ≤ ε (closed), which is what
  `lem:T2-W`(b) delivers.
* **Time.** T_stop ≤ t_td + 2.1W + 2.25U_max/(1−v) ≤ 3.74 + 4·10⁻¹¹ + 14.625 = 18.365 ≤ T₀ = 19.69.
* **Scaling.** (S,H,t) ↦ (dS,dH,dt): ε ∈ (0,d) ↔ ε/d ∈ (0,1). OK.

### Task 4 — `cor:Exact` against `lem:A41` (main.tex l.238–249)

| Hypothesis of `lem:A41` | Supplied in `cor:Exact` |
|---|---|
| D₁ ⊂ D₂ ⊂ … finite, dense union | dyadic sets D_N |
| ε_N → 0 | ε_N = 2^{−N}·2·10⁻⁴⁴ (< 2·10⁻⁴⁴, so the path of `thm:Main` for (v,ε_N) is run with vision radius ε_N itself) |
| H_N with |H_N′| ≤ 1 on [0,T], (H_N(0) = 0 by the formulation) | P_{v,ε_N}: 1-Lipschitz on [0,∞), constant after stopping, P(0) = 0 |
| H_N comes within ε_N of every direction of D_N by time T, T independent of N | `thm:Main`: every α ∈ [0,2π), by T₀ = 19.69, independent of the radius; same v for all N |

Conclusion of `lem:A41`: a 1-Lipschitz H catching every direction exactly by T₀; H(0) = 0 because H is a uniform limit of
the H_N (noted in `cor:Exact`). The proof of `lem:A41` as typeset is complete: the phrase "where t_N ≤ T is the first such
time (the trajectory under H_N is defined on [0,t_N], since a catch is itself such a time)" is present; the contradiction
uses ρ_N(t_N) ≤ ε_N < c/4 for large N with t_N → t* and the Claim on [0,min(t*+δ,T)]; openness of the uncaught set is the
Claim with H_N = H. The Claim's Gronwall constant 8v/c is safe (4v/c suffices). One cosmetic point: l.246 writes
"[0,t*+δ]" where the Claim gives "[0,min(t*+δ,T)]"; immaterial since t_N ≤ T. The direction α = 0 (caught by H_N at t₀)
is covered by "a catch is itself such a time".

---------------------------------------------------------------------------------------------------------------------

## (iii) Constants check

`python code/audit/audit_A_constants.py` (mpmath, 80 digits; written from `eq:T2-const` and the proofs in `sec_T2.tex`
only; compared with `code/P8b/out/final_constants.txt` afterwards: all sixteen derived constants agree to the 10 digits
printed there, and the binding entries of every minimum agree).

```
  gamma_1   = 0.25               gamma_*   = 0.25            c_A      = 0.024
  R_A       = 5.28157111952e-7   M_A       = 0.18547236991   theta_h  = 16.7041211539
  W         = 1.91133231268e-11  C_I       = 25.3681935238   a_I      = 0.125
  Lambda_I  = 4.77833078169e-13  c_I       = 2.12370256964e-13   gamma_B = 0.0625
  R_B       = 2.07130413136e-42  v_0       = 4.14260826273e-51   eps_*   = 2.19657581853e-44   T_0 = 19.69
  minima attained at: R_A:(g1/(400C0))^(1/a'); W:(20max)^(-1/gs)/4.2; Lambda_I:W/40;
                      R_B:(gB/(400CI))^(1/aI); v_0:1e-6 gB RB/(4.5Umax+2); eps_*:(W/Cz)^4
  other v_0 entries: 2e-11gB^2=7.8125e-14, stageA=8.8026e-15, W/132=1.448e-13;   RB/64=3.2364e-44
  [ok] 4e-51 <= v_0 (exact)   v_0/4e-51 = 1.0356521
  [ok] 2e-44 <= eps_* (exact) eps_*/2e-44 = 1.0982879
  [ok] T_0 = 19.69 exactly
== side conditions at EXACTLY v = 4.0e-51, eps = 2.0e-44      (excerpt: the tightest ones)
  [ok] v <= 2e-11 g1^2 (thm:End)                       rhs 1.25e-12
  [ok] v(4 U_A+2) <= 1e-6 g1 RA, U_A<=Umax/2           lhs 6.0e-50 rhs 1.32e-13
  [ok] thT (3W)^gs <= 1/20                             = 0.0090809
  [ok] (2.02 W/RA)^gs <= 1/10                          = 0.0924658
  [ok] z0 <= Cz eps^(1/4) <= W                         Cz eps^.25 = 1.86706e-11, W = 1.91133e-11
  [ok] A_* = W+z0+eps+D <= 4.2 W                       A_*/W = 4.07683
  [ok] (Q3) max(thT,thh)(4.2W)^gs <= 1/20              = 0.05   (equality by definition of W)
  [ok] (D): K_D <= C0+1.91 thT+0.01 thh                K_D = 6.270627
  [ok] concl: max(M_A, 1.001(C0+1), K_D) <= C_I        max = 6.270627
  [ok] C_I LI^a_I <= 1                                 = 0.731474
  [ok] eps <= RB/64                                    eps/(RB/64) = 0.617968
  [ok] v <= 2e-11 gB^2                                 rhs 7.812e-14
  [ok] v(4 U^I+2) <= 1e-6 gB RB with U^I <= (9/8)Umax  ratio 0.96557525
  [ok] time: T2+2.1W+2.25Umax/(1-v) <= T_0 = 19.69     bound on T_stop = 18.365
ALL CHECKS PASSED
```

Full list (125 checks, 160 lines) in `code/audit/audit_A_constants.out`. It covers: the ranges required of the (H_T) constants; all
eleven entries of Table `tab:T2-const` to five digits and "minima attained at the entries shown"; `eq:T2-also`; every
hypothesis of the two applications of `cor:End` and the three inequalities inside its proof; all numerical steps of
`lem:T2-H`, `thm:T2-D` (i)–(v), `lem:T2-StA`, `prop:T2-I` (cases (A), (P), (D), stretch, (E2_I)), `prop:T2-cond`.
Observations: (1) C_I = 25.37 is a 4× overestimate of what is needed (6.27); (2) the constant C_z ε^{1/4} in (T5) (true
size √(2ε)) is what makes ε_* ≈ W⁴; neither matters for correctness. (3) In addition I re-checked by hand the arithmetic of
`thm:HT` that produces the twelve constants: 5.4·40^{−1/2+3v} ≤ 0.86; 2 sin(0.0123) − 7.5·10⁻⁶ ≥ 0.0245 ≥ 0.024;
1.647·(1.4882+0.473) = 3.2301 ≤ 3.3; 1.567 ≤ 1.57; 3.3·1.269·2^{−1/4} = 3.52 ≥ 3.5; U ≤ 0.2030+6.2856 = 6.4886 ≤ 6.5;
t_s ≤ 3.7321 ≤ 3.74.

---------------------------------------------------------------------------------------------------------------------

## (iv) Stale or false sentences, with replacement text

"FALSE" = contradicted by `thm:Main`/`cor:Exact`; "STALE" = still literally true but misleading without a pointer.

### `main.tex`

1. **Abstract, l.22–23 (STALE)** "The main question, whether a faster pursuer can always catch the Snitch, is \textbf{not}
   settled." — keep, and insert after it:
   > `\emph{Main result:} for every $v\le4\cdot10^{-51}$ there is an explicit path, fixed in advance and of speed at most $1$, that sees every direction by time $19.69\,d$ for every vision radius $\varepsilon\in(0,d)$, with neither the range of $v$ nor the time depending on $\varepsilon$ (Theorem~\ref{thm:Main}); consequently, for these $v$, a single path of speed at most $1$ catches every direction exactly ($\varepsilon=0$) by time $19.69\,d$ (Corollary~\ref{cor:Exact}). The range of $v$ is an artefact of the method.`

   and in l.34 change "\emph{Conditional results:} exact capture for every $v<v_1\approx0.4748$" to
   > `\emph{Conditional results:} exact capture for every $v<v_1\approx0.4748$ (beyond the tiny range of Corollary~\ref{cor:Exact})`

2. **Remark after `lem:A41`, l.251–253 (FALSE in its last clause)** "Numerically the greedy ε-sweep times converge as ε→0
   (Section numerics), and the greedy controller is linearly stable for v<0.78 (Section linear), but no uniform bound is
   proved." Replace the sentence by:
   > `Such a uniform bound is proved in Section~\ref{sec:main} for $v\le4\cdot10^{-51}$ (Theorem~\ref{thm:Main}), which gives Corollary~\ref{cor:Exact}. For larger $v$ no uniform bound is proved: numerically the greedy $\varepsilon$-sweep times converge as $\varepsilon\to0$ (Section~\ref{sec:numerics}), and the greedy controller is linearly stable for $v<0.78$ (Section~\ref{sec:linear}).`

3. **§`sec:open`, item 1, l.665 (FALSE)** "\textbf{Any unconditional exact-capture theorem.} Theorems B, B2, A23, A35 are
   conditional on …" Replace the first sentence by:
   > `\item \textbf{Unconditional exact capture for any $v>4\cdot10^{-51}$.} Corollary~\ref{cor:Exact} gives exact capture for $v\le4\cdot10^{-51}$; for larger $v$ everything is conditional: Theorems~\ref{thm:B}, \ref{thm:B2}, \ref{thm:A23}, \ref{thm:A35} are`

   and the last sentence, l.675 (STALE) "By Lemma A41, a bound on the greedy ε-sweep time uniform as ε→0 would also
   suffice." by:
   > `By Lemma~\ref{lem:A41}, a bound on an $\varepsilon$-sweep time uniform as $\varepsilon\to0$ also suffices; this is how Corollary~\ref{cor:Exact} is proved, and extending Theorem~\ref{thm:Main} to a realistic range of $v$ (numerically the design works up to $v\approx0.2$, Remark~\ref{rem:T2-status}) is the most concrete open problem.`

4. **§`sec:open`, item 2, l.676 (FALSE)** "For $\varepsilon>0$, a range of $v$ independent of $\varepsilon$. Theorem D2
   needs $v\lesssim1/\log(d/\varepsilon)$, and its method cannot do better …" Replace the first sentence by:
   > `\item For $\varepsilon>0$, a range of $v$ independent of $\varepsilon$ \emph{of reasonable size}. Theorem~\ref{thm:Main} gives the $\varepsilon$-independent range $v\le4\cdot10^{-51}$; Theorem~\ref{thm:D2} needs $v\lesssim1/\log(d/\varepsilon)$, which is larger for every $\varepsilon\ge e^{-10^{49}}d$, and its method cannot do better`

5. **§`sec:open`, item 5, l.684–685 (true; add)** after "all $\varepsilon=0$ results give speed at most $1$" add
   > `(including Corollary~\ref{cor:Exact}; the path of Theorem~\ref{thm:Main} has speed exactly $1$ until it stops).`

6. **§`sec:numerics`, l.732–733 (STALE)** "If such bounds were proved, Proposition D6(c) would give an ε-independent range
   of roughly $v<0.16$; they are not proved." Append:
   > `(The only proved $\varepsilon$-independent range is $v\le4\cdot10^{-51}$, Theorem~\ref{thm:Main}, by a different construction.)`

7. **Theorem B discussion, l.286–290, l.400, l.590 (true)** — no change needed ("(H) is not proved", "only the end phase is
   open", "conditional upper bound of Theorem B" remain correct statements about those theorems).

8. **Abstract l.23** "Every result added since the first version was checked by at least one independent referee, and the
   main theorems by two." — true; no change.

### `sec_B.tex`

9. **Intro, l.20–21 (STALE)** "\textbf{It is conditional}: (ST) is proved for an explicit start in Section start (Theorem
   ST), but (T) is not proved (Remark B-status)." Append:
   > `An unconditional $\varepsilon$-independent sweep is obtained in Section~\ref{sec:main} by a different route (a tangential start and Theorem~\ref{thm:End} in place of Theorem~\ref{thm:R}); it uses the lemmas of this section but neither Corollary~\ref{cor:M} nor \textup{(T)}.`

10. **`rem:B-status`, l.754–755 (STALE)** "Only (T) remains: it is \textbf{not} proved, so the corollary still gives no
    unconditional range of $v$ (Corollary ST)." Replace by:
    > `For Corollary~\ref{cor:M} only \textup{(T)} remains: it is \textbf{not} proved, so this corollary gives no unconditional range of $v$ (Corollary~\ref{cor:ST}). The unconditional result of these notes, Theorem~\ref{thm:Main}, avoids \textup{(T)} altogether.`

### `sec_ST.tex`

11. **Intro, l.36–37 (STALE)** "\textbf{That corollary is still conditional}: (T) is not proved, and nothing is proved here
    about the arm left behind beyond its state at first contact." Append:
    > `The main theorem (Theorem~\ref{thm:Main}) does not use the start S; from this section it uses only Lemma~\ref{lem:ST-D0}(a) and the bound $g_{\max}\le e^{v^2}$.`

12. **`rem:ST-status`, l.615–619 (FALSE as headed)** "\emph{What remains for exact capture at small $v$.} Only hypothesis
    (T) of Corollary ST: … (T) is \textbf{not} proved, so Corollary ST gives no unconditional range of $v$." Replace the
    heading and first words by:
    > `\emph{What remains for the route through Corollary~\ref{cor:ST}.} (Exact capture at small $v$ is proved by a different route, Corollary~\ref{cor:Exact}.) For Corollary~\ref{cor:ST} only hypothesis \textup{(T)} remains:`

    (rest of the paragraph unchanged).

### `sec_E.tex`

13. **Intro, l.33–34 (STALE)** "\textbf{Nothing in this section is a statement about a complete sweep}; what is and is not
    provided is listed in Remark E-status." Append:
    > `The complete sweep is assembled in Section~\ref{sec:main}, which uses Lemma~\ref{lem:E-facts}, Theorem~\ref{thm:End}(a),(b),(d), Corollary~\ref{cor:End} and Remark~\ref{rem:E-B}(4).`

14. **`rem:E-status`, "Intended use", l.1017–1019 (FALSE)** "It is intended for a start with tangential first contact
    (numerical report \texttt{N8-1.md} in the project archive), for which the start data are not yet proved in this paper."
    Replace by:
    > `It is used for the start with tangential first contact (design~T, Definition~\ref{def:T}): the start data are proved in Section~\ref{sec:touch} (Theorem~\ref{thm:HT}), and Section~\ref{sec:main} applies Corollary~\ref{cor:End} twice to obtain Theorem~\ref{thm:Main}.`

15. **`rem:E-status` (c), l.1010–1013 (STALE)** "Nothing is proved about labels beyond $b_E$, about the tip hypothesis (T)
    …, or about an end created by first contact or by a transversal departure" — insert "\emph{in this section}" after
    "Nothing is proved", and append:
    > `(The end $E_Y$ created by the tangential run of design~T is treated in Sections~\ref{sec:touch} and~\ref{sec:main}.)`

### `sec_D2.tex`, `sec_D3.tex`

16. **`rem:D2`, l.177–178 (STALE)** "A range of $v$ independent of $\varepsilon$ would follow from Corollary D2-red and an
    ε-uniform Lipschitz bound on the walked fronts (CONJECTURE for small $v$)." Replace by:
    > `For construction~W, a range of $v$ independent of $\varepsilon$ would follow from Corollary~\ref{cor:D2-red} and an $\varepsilon$-uniform Lipschitz bound on the walked fronts (CONJECTURE for small $v$). An $\varepsilon$-independent range, $v\le4\cdot10^{-51}$, is proved for a different construction in Theorem~\ref{thm:Main}.`

17. **`sec_D3.tex`** l.20 and l.320–321, l.388: statements about hypothesis (O) and the chase LG0 only; still true; no change.

### `sec_T2.tex` (self-consistency; see D1–D5)

18. l.116–121, l.794–795, l.806–811, l.839–841, l.749–750: replacements given in the table of (i).

### Not checked for staleness

`SUMMARY.md`, `STATE.md` (dated round 0), `snitch_proved.tex` — outside the paper; `STATE.md` in particular still lists
goal 1 as open.
