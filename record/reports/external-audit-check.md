# Check of the external audit (A, B, C)

Paper files were only read; `short/` is unchanged. The scripts written for this check are in `code/audit/ext/`:
- `sc_grid.py` evaluates `touchdown()` from `short/verify_constants.py` at (v, eps) on an 18 x 6 grid (v/vbar from 1e-9 to 1, eps/epsbar from 1e-9 to 1), checks every side condition there, and checks that every constant is monotone in v and in eps.
- `sens.py` and `sens_U.py` run rough sensitivity checks for part C by monkeypatching an import of the script. The script itself is not modified.

## A. Lemma 7.2 (lem:mono), last sentence of the proof

**Verdict: no gap.** The sentence is too broad, as the audit says. It also misses two cases, (SC12) and (SC33), so nine conditions are affected, not seven. Every one of the nine holds for all 0 < v <= vbar and 0 < eps <= epsbar by a one-line bound. So the statement of Lemma 7.2 ("every side condition other than (SC44) implies the same inequality at (v, eps)") is true; only the justification is wrong. Theorem 7.12 and the main theorem are unaffected for v < vbar and eps < epsbar.

### (i) Classification of the conditions that are not preserved
Recall the terms: an upper constant increases with v and eps, and a lower constant decreases. "Preserved" means the inequality at (vbar, epsbar) automatically implies the same inequality at (v, eps).

| SC | statement | type | preserved? | holds for all v, eps because |
|---|---|---|---|---|
| 12 (missed by the audit) | b_lo < 2 | lower < number | no | R_0 >= 1, so rho_max >= 1, Lambda_min <= 4, b_lo <= 1 |
| 16, second part | h_f <= 1 - vbar^2 | lower <= lower | no | h_f is a lower constant, so h_f(v) <= h_f at v = 0, which is 0.991518 < 1 - vbar^2 <= 1 - v^2 |
| 18 | Q >= 1 | upper >= number | no | h_f <= A_min <= 1 and rho_max >= R_R >= 1, so Q >= 1 |
| 23 | gb > C_lo | upper > lower | no | C_lo <= rho_min b_lo <= 1/rho_max <= 1/sqrt3 < 1 <= gamma_max(v) |
| 32 | b_l <= pi/6 - e_beta | lower <= lower | no | b_l <= eta^2 b_lo <= eta^2, and eta^2 + 2 e_beta(vbar) = 0.041 < pi/6 |
| 33 (missed by the audit) | pi/3 + 2e_beta <= pi - b_l | upper <= upper | no | same bound as (SC32) |
| 34 | T_b >= 1 | upper >= number | no | H_b >= 3 and y_b tan(b_l/2) < 1, so T_b > 6 |
| 42 | Delta_0 <= eta | lower <= number (the audit wrote ">=") | no | W_x >= W_v >= 1 and Lhat >= 1, so Delta_0 <= lambda_0 <= eta/2 (SC39) |
| 46 | u_v >= 1/2 | upper >= number | no | W_v >= 1, so u_v >= xi_1 = 1.16 |

Every other condition is correctly upper-vs-lower or upper/lower-vs-number in the preserved direction. I checked all 41 by hand: (SC1)-(SC11), (SC13)-(SC15), (SC16a), (SC17), (SC19)-(SC22), (SC24)-(SC31), (SC35)-(SC41), (SC43), (SC45), (SC47) and (SC48). (SC44) is excluded by the lemma itself.

Numerical cross-check (`sc_grid.py`):
- All 52 inequalities held at every grid point. This covers (SC1)-(SC48) with their a/b parts, (SC44) included.
- Every constant came out monotone in v and in eps, in the direction Lemma 7.2 states. The only flag was czlo = h_t xi_-. That is a derived product of two lower constants, so it is a lower constant too; it was flagged only because the lemma's list does not name it. There is no real violation.

### (ii) Every use of the nine conditions
| SC | where it is cited | what the use needs |
|---|---|---|
| 12 | sec7a l.128 (rule (1), base of T_t^v), l.141 (C_lo step) | the v-expression, so it must hold at the actual v. It does (see the table above). |
| 12 | sec7a l.315 (Lemma 7.4(c), C bound) | the fixed b_lo |
| 16b | sec7a l.363 (Lemma 7.5(a): "h_f <= 1-vbar^2 <= 1-v^2") | the fixed h_f |
| 18 | sec7a l.129 (rule (1), Q^mu), l.142 (Ybar, theta_f Q^mubar) | Q(v) >= 1 at the actual v. It holds trivially. |
| 18 | sec7a l.369 (Lemma 7.5(c)) | the fixed Q |
| 23 | sec7a l.129 (rule (1), base of xi_+) | the actual v. It holds trivially. |
| 23 | sec7b l.37 (tail lemma (a)) | the fixed gb and C_lo |
| 32, 33 | sec7b l.130 (bulk lemma, sigma_beta range, sin sigma_beta >= sin b_l) | the fixed b_l and e_beta |
| 34 | sec7b l.138 (bulk lemma) | the fixed T_b; rule (1) (T_b^v) also uses T_b(v) >= 1, which holds trivially |
| 42 | sec7b l.323 (Theorem 7.12 (T2)), l.358 (Lemma 7.13) | the fixed Delta_0 (as the proof of Lemma 7.2 itself notes for (T2)) |
| 46 | sec7b l.253 (Lemma 7.11, near X_0) | the fixed u_v |

The audit's claim ("every citation in 7.5-7.13 uses the fixed constants") is correct. It does not mention the citations inside the proof of Lemma 7.2 itself: (SC12), (SC18) and (SC23) at l.128-142, and (SC34) implicitly through T_b^v. These need the v-expression, and the trivial bounds above cover them.

### Replacement for the last sentence of the proof of Lemma 7.2 (sec7a l.144-145)
> Each side condition other than \hyptag{SC12}, the second part of \hyptag{SC16}, \hyptag{SC18}, \hyptag{SC23}, \hyptag{SC32}--\hyptag{SC34}, \hyptag{SC42} and \hyptag{SC46} compares an upper with a lower expression (or a number) in the direction that is preserved when $(\vbar,\epsbar)$ is replaced by $(v,\eps)$. The exceptions hold for every $v\in(0,\vbar]$ and $\eps\in(0,\epsbar]$ directly. Since $R_0\ge1$ we have $\sr_{\max}\ge1$, hence $b_{\mathrm{lo}}\le\Lambda_{\min}/4\le1$ \hyptag{SC12}, $b_{\mathrm l}\le\eta^2$, and $C_{\mathrm{lo}}\le\sr_{\min}b_{\mathrm{lo}}\le1/\sr_{\max}\le1/R_R<1\le\gb$ \hyptag{SC23}. Since $h_{\mathrm f}\le\sA_{\min}\le1$, $Q\ge\sr_{\max}\ge1$ \hyptag{SC18}. The bound $\eta^2+2e_\beta<\pi/6$ gives \hyptag{SC32} and \hyptag{SC33}. Since $y_{\mathrm b}\tan(b_{\mathrm l}/2)<1<H_{\mathrm b}$, $T_{\mathrm b}>1$ \hyptag{SC34}. Since $W_x,\hat L\ge1$, $\Delta_0\le\lambda_0<\eta$ \hyptag{SC42}. Since $W_{\mathrm v}\ge1$, $u_{\mathrm v}\ge\xi_1>\frac12$ \hyptag{SC46}. Finally, the lower constant $h_{\mathrm f}$ is at most its value $0.99152$ at $v=0$, which is $<1-\vbar^2\le1-v^2$ (second part of \hyptag{SC16}).

## B. Minor correctness items

1. **sec1 l.19-20.** The current text is not false: "≲" hides a constant. It is imprecise, and the constant 1+2pi is correct. Starting at the origin, the path reaches d e^{i alpha} by time (1+2pi)d. By then the Snitch, moving at speed v, is within (1+2pi)vd of its start. (If it was caught earlier, it was also seen.) Proposed text:
   > A path that runs straight to the circle of radius $d$ and once around it sees every direction when $(1+2\pi)vd\le\eps$: it passes $de^{i\alpha}$ before time $(1+2\pi)d$, when the Snitch is still within $(1+2\pi)vd$ of that point.
2. **Lemma 2.8(b), (d).** e_J is defined only when c > 0 (Def. 2.7), so the gap is in presentation only.
   - The identity V = 2[l - (x_b - x_a)·û] and the bound N^2 <= V hold for all c >= 0. Only the terms that contain e_J need c > 0.
   - Applications of (b): split tilt (i), (ii) (hypotheses c(I), c(J) > 0); lem:excess (ii) (hypothesis c(a,b;t) > 0); sec3 l.306, sec4 l.95 and sec4 l.239 (family pairs, c >= c_A lambda > 0 by eq:CA); sec7b l.254 (only N^2 <= V with û = n̂, no e_J). Every application satisfies c > 0.
   - **(d) is never cited** (grep finds no `lem:static}(d`), so it can simply be deleted.
   - Proposed text for (b): "... $=N(J)^2+c(J)|e_J-\uhat|^2$ if $c(J)>0$. Hence $N^2\le\Vu$; if $c(J)>0$ also $|e_J-\uhat|^2\le\Vu/c$ and $\int_J|T-e_J|^2ds=N(J)^2$; ...". For (d), if kept: "for $a\le a'<b'\le b$ with $c(a,b),c(a',b')>0$".
3. **Lemma 2.12, the Claim.** This is cosmetic. |S̃ - S| is Lipschitz, so the bound holds a.e. and integral Grönwall applies. Suggested wording: "$|\tilde S-S|(t)\le|\tilde S-S|(0)+(8v/c)\int_0^t(|\tilde S-S|+\|G_k-G\|_\infty)$, since $|\tilde S'-S'|\le\dots$ while ...; Grönwall gives ...". On openness: the Claim's neighbourhood is in terms of |e^{iα'} - e^{iα}|, so it is a circle neighbourhood. The final step is valid both on S^1 and in [0,2pi) with the subspace topology (an open set disjoint from a dense set is empty). Writing "open in $\R/2\pi\Z$" would make this explicit.
4. **Lemma 3.6(iii).** Already correct in the current text: the proof (sec3 l.236) says "$[0,x)$", which includes g = 0. Nothing to change; the audit appears to have read an older version.
5. **Lemma 4.11, bottom cell.** The audit is correct that the script handles both boundary terms and that the paper does not say how.
   - θH_0 is `TH0`, formed from the atoms ≤ C_mu θ_b/2, κC_mu θ_b²/4 and (κC_mu)^{1/2}θ_b/2 (`verify_constants.py` l.974-987).
   - θH_r^*(θ/κ) is bounded by `max(T_cr, THst[0])`. Here `T_cr = κ x_1 H(x_1)` bounds sup_{y <= x_1} θH(y) using θ <= κy and the fact that y times each closed-form majorant is non-decreasing. `THst[0]` covers y >= x_1 (l.1036-1038, `_crude`).
   - I did not re-derive this line by line. Suggested addition after "only the integral form is used": "the boundary terms are bounded by $\theta H_0\le\theta_bH_0$, with the atoms above, and $\theta H_r^*(\theta/\kappa)\le\max(\kappa\sup_{y\le x_1}yH_r(y),\,\theta_b\sup_{y\ge x_1}H_r(y))$, using $\theta\le\kappa y$ and the majorants below, for which $yH_r(y)$ is non-decreasing on $(0,x_1]$".

## C. Proposed improvements

**Gain model.** The "v0 gain" figures below use a deliberately crude model. Only (P5) and (P6) are moved, and fF is shared by p and p_A. Everything else stays frozen: J_k, D', the touch-down constants (which in reality worsen as vbar rises), dL, delta_1 and nu. The binding condition is (P6) for p_A, where D'_A = 64.64 sets the limit. These are indicative upper estimates, not certified values.

| # | claim | status | rough effect |
|---|---|---|---|
| C1 | ∫_0^l abs(δ) <= l^{3/2}N/(2√3) | **Correct.** For s = sgn δ and any antiderivative S of s, ∫δs = -∫δ'(S - mean S), because δ(0) = δ(l) = 0. A 1-Lipschitz S has variance at most l²/12. Only the |p_a| forcing term (β_f, B'_{2U}, B*_{2η}, B'_3) gains the factor π/(2√3) = 0.9069; the δ² and length terms still need Wirtinger. | fF needed 0.500225 → 0.48275; **v0 about +1.9%** |
| C2 | abs(e_J - e_I) <= sqrt((κr - c_A)/(c_A(κ - m²/4)))·Mλ_I^γ | **Correct as stated**, derivation checked. c_L(e_L - e_I) = -c_J d - (c_J + c_L - c_I)e_I, and its component perpendicular to e_I has length c_J|d|(1 - |d|²/4)^{1/2}. So N(I)² >= c_J x + c_J² x(1 - x/4)/c_L with x = abs(d)². Then use c_L <= κλ_I - c_J, the fact that the bound is increasing in c_L, c_J x <= N² <= m², and c_J >= c_A λ_I/r. If J is interior, combine the two pieces of I∖J by Cauchy-Schwarz. | C_T 3.833 → 3.626 (p) and 3.637 → 3.441 (p_A); recertified D'(p) 63.068 → 62.508, but **D'(p_A) unchanged (64.6356)**; **v0 about +0.4%** |
| C3 | Prop 4.2: ∫_{η1R}^{K_R R} y^{-2} = 1/(η1 R) - 1/(K_R R) | **Correct** (the paper uses only 1/(η1 R)) | B*_{2η} -10%; **v0 about +0.8%** |
| C4 | Prop 4.12: keep sin²φ in the near phase | **Plausible but unchecked.** Valid only where ρ >= ε (A = Π/ρ). For ρ < ε the virtual field's Jacobian has a radial part, so the a*(ρ) bound must stay there. | Affects only T_I in LJ: slack in (P7)/(PT), allows a smaller κ. Not quantified; probably small. |
| C5 | Section 5: Minkowski instead of (a+b)² <= 2a²+2b²; h_H inside the integral in Thm 5.2(ii); free K instead of K = 4 in 5.2(v); log integral in Lemma 5.1 | Minkowski: **correct** (always at least as sharp). The other three: **plausible but unchecked**. | Acts on ω_0 (A4, slack 0.26%) and TS (slack 2%). The lever on v0 is lowering γ_D, which lowers D'_A. (A5) γ_D >= γ+ν+η_N already has 3% slack; free K only lowers aD*(4) = 1.092 toward 1. Guess: up to about +1%. |
| C6 | Lemma 7.11: concave-power curvature integration to cut c_N | **Correct in principle, but no effect**: c_N = c_near = 3.412, while c_far = k*/√12 = 1.998 (c_tail = 2.806). Cutting c_far leaves c_N unchanged. | **0** unless c_near is also improved |
| C7 | split W_b to reduce U | **Plausible** (T_b^vbar = 1.087 is a worst case over the whole bulk) | U_max -5..10% leaves P5 unchanged; (P4) improves 0.0014-0.003, so A_0 improves about 0.2% and **v0 about +0.1-0.2%**. The real benefit is T0: T# = T2 + κU_max/(1-v0), about -0.4 per 5% of U. |

**Combined C1 + C2 + C3 in the same model: v0 about +3.0%** (5.80e-3 → about 5.97e-3, before re-tuning and before the touch-down constants are recomputed at the larger vbar).

Side observation: (A5) (TS) has 1.96% slack, which seems unused. If nothing else ties s0, lowering s0 by that amount lowers fF by about 0.006, worth about +0.65% in v0 in the same model.
