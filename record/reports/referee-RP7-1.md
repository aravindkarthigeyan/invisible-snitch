# Referee report RP7-1 on `referee/P7-claims.md` (version 1)

Independent adversarial check. Read: `referee/P7-claims.md` in full, `paper/sec_B.tex` in full (assumed correct; every
citation checked against its hypotheses). Not read: `reports/P7-1.md`, `code/P7/`. Own code: `code/referee/P7_1/`.

## 0. Summary of verdicts

| Claim | Verdict |
|---|---|
| Facts 0.1, 0.2, 0.3 | **OK** |
| Theorem P7.B (a),(b),(c),(d) | **OK** (two cosmetic fixes F1, F2; no gap in the proof, all constants recomputed) |
| Remark (1) "cubic bound never used structurally" | **OK** (fix F3 to one sentence) |
| Corollary P7.E | **OK with fixes** (F4: quantifiers of (ST_end)) |
| Remark "same-side restart" | **OK with fix** (F5: one uncovered corner case) |
| Lemma P7.A | **OK** |
| Theorem P7.D (i)-(v), incl. (4.4), (alpha), (beta), (iii) | **OK with fixes** (F6: one inequality in (iii) is used in the wrong direction; repaired by a change of notation, constants unchanged; F7) |
| Proposition P7.D' | **OK** |
| Lemma P7.H | **OK** |
| Corollary P7.T | **OK with fix** (F8: the hypothesis `v <= gamma_1/7` allows `a' = gamma_1 - 7v = 0`; needs `v <= gamma_1/14`) |
| Proposition P7.C | **OK with fixes** (F9: (iii) upper bound needs `v*mu < 1`; lower bound is proved only for `2 t^(1-v) <= 1`) |

No FALSE statement and no GAP that affects a conclusion was found. Everything is uniform in epsilon. The numerical tests
in the admissible range of Theorem P7.B (`v <= 1.25e-12`) are necessarily weak (the front does not move); the verdict on
P7.B rests on the line-by-line check, not on the simulations.

## 1. Theorem P7.B, step by step against [B, Theorem B]

Nothing is asserted "as in Theorem B" without the argument being either written out or literally identical. Per step:

**Set-up / Lemma C with the cut at b_E.** C(0): the bound `|d_theta x| <= e^{2vT/eps}` holds for any 1-Lipschitz path, so no
accumulation. C(2): unchanged (ansatz on the leg). C(3): `rho_theta(t_j) <= l_{t_j}(a_j,theta) <= eps` on `[a_j,a_{j+1}]`,
unchanged; the covering is now of `[a_s,b_E]`. C(4): unchanged, for non-final legs. A non-final leg has `a_{j+1} < b_E` and
`l_{t_j}(a_j,a_{j+1}) = eps` exactly as in C. The stopping time is the end of the last non-final leg, so every time
`t <= T_stop` lies in a non-final leg and C(2), C(4), (*) are available at all times used. Theorem R is not used for the
leg count (the count comes from the label advance), only its Claim is used in (c); see below.
Implicit hypotheses that should be stated: `P(0) = 0` (so that Lemma VC(c) gives "seen") and `b_E - a_s < 2 pi` (stated).

**Continuity argument.** Correct. `F(t)` shrinks, bounds at `t*` hold by continuity, the extension by `delta` is uniform because
`lambda >= eps/2`; `|E'| <= (4v/eps) l` is right (the `8v/eps` of [B] was wasteful). At a switching time both legs count and the
leg-(j+1) family is contained in the leg-j family.

**Step 1(a).** (alpha): `(a_j,s)` with `u_s = u_{a_j} + eps/2 <= U` is a family pair (first point = base), (J1) gives
`l <= 9 eps/16 <= eps`, so `a_{j+1} >= s`. OK. (beta): verified. For `j > j_s` leg j was non-final, so (beta) did not apply at
`t_{j-1}` (it would have made leg j final), hence (alpha) did and `lambda_1 in [eps/2, eps]`; `(a_{j-1}, b_E)` has label length
in `[eps/2, 3 eps/2]`, is a leg-j pair, and `t_j` belongs to leg j, so (J1) applies:
`l_{t_j}(a_j,b_E) <= (9/8)(lambda_1+lambda_2) - lambda_1 < eps/8 + 9 eps/16 = 11 eps/16`. This is where the sharpened (J1) is needed
(with the old `l <= 2 lambda` one would get `lambda_1 + 2 lambda_2 < 2 eps`, not enough). The "induction" is not really an
induction; the argument is complete. **Answer to "what is the target when fewer than eps of arc remains":** there is none; the
construction stops at that leg start with `l(a_J,b_E) <= eps`, and all of `[a_J,b_E]` is within eps of P at that instant
(C(3)), so every remaining label is seen. No pair is ever beyond the arc.
(b), (c) (B-1c), (d) (*): unchanged and correct; (*) uses (S1) for all pairs `lambda >= eps/2`, including `lambda > R`.

**Step 2 (TL).** Re-proved with exponent gamma. `2 (9/8)^{1/2} 3^{1/2+gamma} + m <= 4.8406 <= 4.85`; concavity bound
`S <= 1.5714/gamma` correct (tight at gamma = 1/4); total `4.85(2S+1) <= 16.46/gamma`. (A), (B), (C) chains consist of family
pairs (checked first points and lengths). (Mu), `C_mu <= 613/gamma^2`, `C_1 = 1.6 C_TL` correct.

**Step 3 (far).** Hull distance, Lemma 3(e) hypothesis `rho_m >= max(eps,4l)` on the whole far period: OK (uses only
`l <= 2 lambda`). Forcing for `g <= R/2`: three family pairs, `|p_a| <= 2.26 C_TL M g^{1+gamma}`, `beta <= 346 ...`: OK. Result:
second term `<= 0.0408 M lambda^{1/2+gamma}`, third `<= 6.9e-9 M lambda^{1/2+gamma}`; the weight in (S2) exactly cancels the
amplification of the first term. `h(g) = g^{nu+gamma-2}` is non-increasing. Total `<= (3/8) M`. See F1 for a harmless
imprecision inherited from [B].

**Step 4 (near).** All four cases of Term II re-derived with the new constants: `C_TL 65^gamma <= 46.86/gamma <= C_theta`;
case `0 < g' < eps/2`: `0.75 (4.5 + C_theta^-2)^{1/2} = 1.59 <= 3`; case `a_{j+1} > b`: `(1.0607 + 1.125 C_TL) 2^gamma <= 23.3/gamma`.
(There `lambda < eps <= R/64` does not imply `65 lambda <= R`; the bound `<= theta eps` still holds with `theta = 2`.)
Term I, time integrals (272, 536), `Delta E <= 4.48e9 v M^2 lambda^{1+2gamma}/gamma^2 <= 0.0896 M^2 lambda^{1+2gamma}`: OK. The margin
in `v <= 2e-11 gamma^2` is 0.5% (worst case of `Delta E`: 0.9946 of the allowed 0.09) - correct but with no slack.

**Step 5 ((J1)).** `661`, `(2.02/gamma) R^{2 gamma}` (checked for all `eps/R <= 1/64`, all gamma), `146 v/gamma`, `3618 v lambda`:
OK; `l <= 1.00001 lambda`.

**(b).** OK. **(c).** (F_b), (S) OK. The Claim in the proof of [B, Theorem R] is applicable with `b* = b_E`, `K_T = 0`: it uses
(F_b), (S), C(2), C(4), Lemma 3(d), 4(b) and `l_t(a_{j+1},b_E) <= e^{2mu} R_j`, nothing about labels beyond `b*`.
`K~ <= 16.0000 + 0.00025 + 18.0000 U/R`. See F2. **(d).** OK.

**Does cutting at E change Lemma C / Theorem R?** No. The only use of "the target stays in the arc" in [B] was to guarantee
that all pairs used are in the labelled arc; with the cut, base, target and all sub-arcs used for a pair (a,b) lie in
`[a_j, b]`, `b <= b_E`.

## 2. Other points requested

* **Uniformity in epsilon.** Verified for every constant of sections 1-5; eps enters only through `eps <= R/64`, `lambda >= eps/2`
  (P7.B, P7.E), `lambda >= eps/2`, `U_E >= eps/2` (P7.D), `rho_0 >= eps` (P7.A).
* **Non-circularity.** P7.B is one closed bootstrap. P7.D is direct (no bootstrap: (4.1)-(4.4) -> (ii) -> (iii) -> (v)).
  P7.H uses the output of P7.B at one time; P7.T = H + D + A; P7.E = P7.B. No loop.
* **Ranges.** Non-empty and mutually consistent, except F8. Note the quantitative price: Lemma H gives (D2) only for
  `U_E + D <= R_1 20^{-1/gamma_1}` (= R_1/160000 for gamma_1 = 1/4); in P7.T `rho_0 <= (1+v)D + ...` is then of that size, so
  `C_0` can be as large as `2.9 R_1^{-gamma_1} + 0.014/rho_0`, and P7.E applied to it gives
  `R_2 <= (gamma_2/(400 C_0))^{1/a'}`, at best about `1e-16 R_1` when gamma_1 = 1/4. Epsilon-independent, but each pass halves
  gamma and shrinks R by a huge factor; only finitely many passes are affordable. Not an error.
* **"The cubic bound in (ST) is never used structurally."** Confirmed by the complete re-proof: (ST) enters only via (CA),
  the start value of near pairs, and `N(t_s)` in the first term of Step 3 (where [B] used the exponent 3/2 to absorb
  `(R/lambda)^nu`; here the weight in (S2) does it).
* **Is (ST_end) checkable?** Yes in substance: arc `A = [a_s,b_E]`; pairs = all label pairs `a < b` in A (including `a = a_s`,
  `b = b_E`); lambda = arclength at `t_s`; (E1) `N <= C_0 lambda^{1/2+a'}` for `eps/2 <= lambda <= lambda_0`, no gap weight;
  (E2) chord separation `c >= c_sep` for `lambda > lambda_0`. Missing: see F4. Remark for users: (E1) at scales `lambda ~ eps`
  next to `b_E` is the demanding part; a kink of angle Theta at scale eps needs `Theta <~ C_0 eps^{a'}`, so ends created by
  first contact or a transversal departure are excluded (consistent with P7.C and [B, Remark N2]).

## 3. Fixes (exact text)

**F1 (P7.B Step 3, inherited from [B]).** The display `exp(int alpha) <= A_0 (min(g_1,32R)/g_2)^nu` is not justified as written when
`g_2 > 32R` (then `(min(g_1,32R)/g_2)^nu < 1` and the right side can be below the true factor, which is only `<= A_0`). Replace `g_2` by `g^_2 := min(g_2,32R)` there and in
the amplification factors of the *Result*, and add: "if `g_2 > 32R` the first term is `<= A_0 N(t_s) <= (M/4) lambda^{1/2+gamma}`
directly, and `(32R/g^_2)^nu = 1 <= (R/lambda)^nu`." The conclusion `N <= (3/8) M lambda^{1/2+gamma}` is unchanged.

**F2 (P7.B proof of (c)).** Replace "split `[a_j,b_E]` into consecutive family pairs ..., the first starting at `a_j`" by:
"the first pair is `(a_j,a_{j+1})`, the others start at labels `>= a_{j+1}`; if `0 < U - u_{a_{j+1}} < eps/2` use the single pair
`(a_j,b_E)` (label length < 3 eps/2 <= R)".

**F3 (Remark (1) of section 1).** "Theorem P7.B with gamma = 1/4 is [B, Theorem B] under a relaxed start" -> "is the analogue of";
the ranges differ (`v <= 1.25e-12`, `v(4U+2) <= 2.5e-7 R`, `m = 1/200`), so neither statement contains the other.

**F4 (Corollary P7.E).** State the quantifiers: "Fix `a' in (0,1]`, `C_0`, `lambda_0`, `c_sep`, `U_max`, independent of (v, eps).
Let (v, eps) satisfy `eps <= R/64`, `v <= v_0`, and let the configuration produced with this (v, eps) satisfy (E1), (E2) at a
leg start `t_s` with `P(t_s) = x_{a_s}(t_s)`, `b_E - a_s < 2 pi`, `U <= U_max`. Then ..." (As written, "for all eps <= R/64 and all
v <= v_0, (ST_gamma) holds" reads as if (ST_end) were epsilon-free.) `lambda_0/32` in R can be `lambda_0` (harmless).

**F5 (Remark, same-side restart).** The enlargement "inside `[a_j,b_E]`" is impossible when `U - u_{a_j} < eps/2`. Add
"for leg starts with `U - u_{a_j} >= eps/2` (otherwise the construction stops at `t_j`)".

**F6 (Theorem P7.D (iii), first part).** "`v log X <= X^v/e` ... (so `v log X <= A_s^{1/4.1}/e`)" is the wrong direction:
`A_s <= X^{4.1v}` gives `X^v >= A_s^{1/4.1}`. Fix: in (4.2)-(4.4), (alpha), (beta), (ii), (iii), (v) let `A_s(t)` *denote the majorant*
`((u_s+eps+tau)/(u_s+eps))^{4.1v}`. Every use is an upper bound that the majorant satisfies: `w~ <= A_s`;
`exp(v int_{tau'}^{tau} a*) <= A_s(tau)/A_s(tau')`; (4.3); (alpha), (beta) are proved for the majorant anyway. Then
`X^v = A_s^{1/4.1}` exactly, `v log X <= A_s^{1/4.1}/e` is true, and all constants (6.04, 106, 0.0216, 4.3) stand.

**F7 (Theorem P7.D, last sentence).** "(M_0 <= theta_0 without loss)" -> "assume `M_0 <= theta_0`; otherwise replace `2.9 theta_0` by
`2.9 max(theta_0, M_0)`". ((D1) gives `N(t_E) <= theta_0 lambda^{1/2} u_b^gamma`, not `<= theta_0 lambda^{1/2+gamma}`, for far pairs.)

**F8 (Corollary P7.T).** With `v <= gamma_1/7` only, `a' = gamma_1 - 7v` may be 0, and it depends on v while `v_0` of P7.E is
supposed to depend on `a'`. Replace the hypothesis by `v <= min(1e-5, gamma_1/14)` and the conclusion by "(E1) holds with
`a' = gamma_1/2`" (legitimate: `lambda_1 <= 1` and `gamma_1 - 7v >= gamma_1/2`).

**F9 (Proposition P7.C (iii)).** Upper bound: add "for `v mu < 1`" (for `v >= 0.618` the right side is negative or infinite, the
bound is false as written). Lower bound: the proof (`D_2 >= L`, `D_1 <= t^{-v}`) gives `tan Theta >= L t^v` only when `L >= 0`,
i.e. `2 t^{1-v} <= 1`; add this restriction (or prove `D_2 >= 0`, which holds numerically for all v <= 0.95, theta in (0, pi/2]).
The asymptotics and the conclusion "exponent v/(1+v)" are unaffected.

## 4. Remaining checks of sections 3-6 (all confirmed)

* P7.A: `rho_m >= rho_0 >= 4 l_t(Gamma)`; `|p_a| <= 1.25 rho_m`; Duhamel with a majorant of alpha is legitimate.
* P7.D (4.1): both cases checked incl. `u_s < eps/2` (`z_s(t_E) >= u_s - eps/1600`). (4.3): via `(E, s^+)`. (4.4): Fact 0.3 divided by
  `w(t_E)^{1/2}`, weights `A(t) A(t')^{-1/2} * A(t')`, `1/0.49^2 = 4.165`, `int = 1/(u_s+eps)`, `u-bar <= u_s + eps`. Correct.
  (beta): dyadic pieces all have label length `>= eps/2` and right end `<= u_b`; bracket `= 1/(2^q-1) - 2^{-Kq}(1/(2^q-1)-1) <= 1.001`.
  Correct. (ii), (iv), (v) (`4.374 <= 4.4`, exponent bookkeeping `gamma - 7v + 5.61v + 1.39v - 1`): correct.
* P7.D': correct (`0.998/1.03 = 0.969`).
* P7.H: three leg-j family pairs, `e_{(a_{j-1},a_j)} = u-hat` at `t_j`, `2.87 * 16.5 = 47.4 <= 48`. Correct.
* P7.T: `1.03 e^{1/200} = 1.0352`, `0.207 rho_0 <= rho_0/4`, `2.803 <= 2.9`, `2.74 <= 2.8`, `0.962`. Correct. The proviso that
  (E1), (E2) must still be verified outside Gamma is correctly flagged; P7.T alone does not give a two-pass theorem.
* P7.C (i), (ii): confirmed analytically and against ODE integration.

## 5. Numerical work (`code/referee/P7_1/`)

* `constants.py` -> `constants.out`: all constants of sections 1, 2, 4, 5 on a gamma-grid (1e-6..1/4), worst v: 0 failures;
  tightest: `Delta E` (0.9946), `S` (0.99994), TL total (0.9972). P7.E (S1)/(S2) from (E1)/(E2) on 2e5 random parameter sets: 0 failures.
* `sim_end.py` -> `sim_end.out`, `sim_hook.out`: Construction C cut at an end, C^1 field, 1000-2000 legs, pairs sampled at all
  scales including all pairs ending at `b_E`. In range (`v = 1e-12`, `eps = 3e-5`, gamma = 1/4, R = 0.00213 found from the data,
  three end offsets; also a power-law hook `psi = k (U-u)^{0.2} cos(3 log(U-u))` at the end with (S2) at 0.992 of its bound):
  advance in [0.9,1] eps, stop with remaining length 0.1-1.0 eps, 0 unseen labels, `l/lambda = 1.0000000`,
  (J2) ratio 0.015 (= start value, no growth), (CA) 2.00, tilt ratio 0.003, `K~ <= 0.30` (bound 283), Lemma H ratio 2e-6.
  Out-of-range stress (`v = 1e-3, 0.01, 0.05`): same picture, `l/lambda <= 1.072`, (J2) ratio <= 0.015; (beta) case exercised
  (`U - u < eps/2` at a leg start, `l(a_j,b_E) = 0.49 eps`). At `v = 0.1` (J1) fails (`l/lambda = 1.153 > 9/8`): the smallness of v
  is genuinely needed for the sharpened (J1), not a counterexample. (Three runs at `v = 0.2` aborted: the head-on tip
  stretches the grid beyond eps; irrelevant here.)
* `dep_tan.py` -> `dep_tan.out`: P7.D, D' for three shapes, eps = 1e-4, 1e-5, 1e-6, gamma = 0.25, 0.05, v = 1e-5 (in range):
  (i) exact to 1e-15; (4.1) min 1.02; (4.3) <= 0.81; (ii) <= 0.990; `l/lambda <= 1.000006`; (iv) <= 0.27; (v) <= 0.99996; identical for
  the three eps. Out of range (v = 1e-3, 0.03, 0.2): the measured tilt exponent at the end drops by 0.0010, 0.0283, 0.162
  (`v/(1+v)` = 0.0010, 0.0291, 0.167): P7.D' is real. (iii) `l <= 1.03 lambda` fails only at v = 0.2.
* `dep_trans.py` -> `dep_trans.out`: P7.C: `G` = integral to 1e-15, position vs ODE to 1e-12, tangent to 1e-7, (iii) on a
  (v, theta) grid: 0 violations (with the restriction of F9 for the upper bound), `Theta/(c_v (r/tau)^{v/(1+v)}) -> 1`.
* `passive.py` -> `passive.out`: Facts 0.1-0.3 and Lemma P7.A on 300 random arcs/paths, v up to 0.8: 0 violations.
