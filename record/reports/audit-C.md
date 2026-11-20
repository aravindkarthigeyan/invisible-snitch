# audit-C: end-to-end audit of the improved main theorem (thm:Main2, cor:Exact2)

Scope: paper/sec_HTp.tex (thm:HTp, cor:HTp-used) -> paper/sec_Estar.tex (thm:Estar, cor:Estar, lem:Estar-L1..L4, proof text)
-> paper/sec_T3.tex (lem:T3-W, thm:T3-E, lem:T3-H, thm:T3-D, prop:T3-cond, thm:Main2, cor:Exact2) -> main.tex lem:A41.
Compared against: sec_T2 (lem:T2-W, hyp:HT), reports/Q4-1.md (§2 interface check), referee-RQ2-1/2 (old-core assumptions).
Code (new, independent of code/Q1/q1const.py and code/Q4/final.py; formulas transcribed from the typeset text):
`code/audit/C/audit_C_constants.py` (+ `.out`), `code/audit/C/sweep.py` (+ `.out`), `code/audit/C/td_crosscheck.py` (+ `.out`).
The paper was not edited.

## Verdict: **CHAIN CLOSED**

No false statement and no mathematical gap was found on the path
(H_T') <= thm:HTp/cor:HTp-used; End* (thm:Estar, cor:Estar, L1-L4) -> lem:T3-W -> thm:T3-E, lem:T3-H, thm:T3-D -> prop:T3-cond -> thm:Main2 -> cor:Exact2 (lem:A41).
Every one of the 130 numerical conditions I check (the 114 of tab:T3-side plus structural ones) holds in 50-digit arithmetic at
exactly the printed digits, with the exact touch-down constants, with the outward-rounded constants of cor:HTp-used, and with the
nearest-rounded constants of tab:T3-const. The interface items below need only **text** amendments (T1-T9); none changes a proof
step, a statement or a constant.

## 1. Interface: assembly <-> End* (top priority; Q4-1 §2 was unrefereed)

Old-regime facts. I searched sec_T3 for every place where the RQ2 referees' verification relied on old-core numbers (they used
K_f = 64, separation 32R, W1 = 32R, U >= 2W1+65R+eps, kappa1 = 9/8, A0 <= 2, "(1+delta_t)*1.00001 < 9/8", gamma_D = 1/4, near time
<= 264 lambda, small tilts). Each is replaced in the typeset text by its parametric counterpart, and each counterpart is either a side
condition I verified or is proved in sec_Estar's proof text for general parameters:

| use in sec_T3 | needs from End* | where provided (sec_Estar) | status |
|---|---|---|---|
| T3-E Step 0: (CA*) for family pairs; (e') | (S1*) only via (CA*); family pairs lambda <= R | Step 0 "Chords"; L1 (CA* used only for window pairs and (a_j,s)); Step 1(d) proof | match; "delta1 >= 1 > c_A/2" holds (c_A = 0.996) |
| T3-E Part 1: body family closed | (Imp*) for (a,b) uses family bounds only in window [a_{j(t')}, max(b,a_{j(t')+1})] | L2(i); verified against the list in L2's proof and against Steps 2-5 (chains A/B/C inside [a_j,b], (a',a),(a',b), J_y, J_0, I_0 only if a_{j+1}>b) | match; window pairs are body pairs since u'_{a_{j+1}} >= U-W1-eps >= W1 |
| T3-E Part 1: (E-star*) at s in [a,b] | (CA*) for (a_{j(tau)}, s), possibly long (w_s > K_R R) | L1(ii); Step 3 (s=a), Term I, Term II short/long case, Step 5 near | match; (a_j,s) good since u'_s >= u'_b >= W1 |
| T3-E Part 1 legs (F4) | Step 1(a) uses (J1*) for (a_i,s_i), (a_i,a_{i+1}), (a_{i-1},E_bE) only | L2(ii); Step 1(a) text | match (Q4 amendment A2 is typeset); case (beta) impossible while u_{a_j} < W1 |
| T3-E start data (F1)(iv) | data at t_s enter only via N(t_s), E(t_s), l(t_s)=lambda of the pair, labels, U | L3(1) | match |
| T3-E Part 2 tail pairs (F2) | restart of a far pair at t_w with N(t_w) <= s0 M lambda^{1/2+gamma} min(1,K_f lambda/min(g_w,K_R R))^nu | L3(2) and its proof (amplification bound from tau = t_w, forcing over subsets) | match (formula identical); see note N1 on g_w at a switching time |
| T3-E Part 2 near phase | Step 4 from the far value at the switching time | Step 4 first sentence; unchanged-steps table ("start value of near pairs") | match |
| T3-E length (F3), (PT) | (P7_delta): (1+delta)exp(X_far+B5 I5 v m^2) + v kappa1 tau_I < kappa1 | L3(2), L4, Step 5 ("far phase precedes near phase") | (PT) => (P7_delta) holds algebraically; both verified (slack 0.162%) |
| T3-E (b') | Step 1(a),(b), proof of (b) | proof of (b); Step 1(b) | match; kappa1 = 1.01594 <= 4/3 needed by case (beta) |
| L_J in eq:T3-LJ | L_J = exp(X_far + B5 I5 v m^2) + v kappa1 tau_I | "Derived constants", (P7) | identical (Q4 amendment A1 typeset) |
| gamma > 1/2 (gamma = 0.614) | Step 5 far g <= eta R with gamma > 1/2 | Step 5 uses lem:Estar-gap(ii) for gamma > 1/2; I5 covers both cases | correct for gamma = 0.614 and gamma_D = 0.6147 |
| lem:T3-H (stage A) | (a),(b),(d),(e), (J2*), tilt constants C_A, C_B (no smallness) | (d) = Step 2 (exact geometric sum, no cap); (e) = Step 1(d) | match; tilts > 1 handled by psi <= min(1,2x) (Q4 amendment A4 typeset); C_A^A m (delta0/R)^{gamma_D} = 0.112 enters omega0 only |
| prop Step 1, Step 6 | cor:Estar (C0)-(C6); (S1*) via concavity, (C2),(C3),(C4) | cor:Estar proof | match; C3 applies (K_R R = 0.0324 < lambda0 = 0.0333) |
| stage A | cor:Estar with U = U_A (its "U_max" is U_A), gamma -> gamma_D, c_sep^A | cor:Estar statement | match |

lem:T3-W (working-front version of End*). It is proved, by reference to the argument of lem:T2-W(d), and is a faithful analogue:
same replacement of lem:B-VC(c) by lem:T2-W(b), of lem:B-C(3) by (3'), same proviso, with c >= c_A min(lambda, K_R R) in place of
(1/2)min(lambda,32R) and advance in [eps/kappa1, eps] subset [eps/2, R]. Its list of cited items omits (harmless, covered by the
T2-W(d) argument it invokes) the pieces of the proof of thm:End reused verbatim by End* (continuity scheme, near-pair start value,
proof of End(b), which in turn quote the closing of the Bulk continuity argument) and Remark E-B(2) (scope only). Text amendment T6.

Q4-1 §2 re-checked item by item: items 1-15 are correct; amendments A1-A4 are all present in the typeset sec_T3.

Notes (no gap):
* N1 (switching convention). In L3(2), g_w := g(t_w); at a switching time t_w = t_W the family convention makes g(t_W) the gap of
  leg j_W (base a_{j_W-1}), while (TW) is stated with g_W = u_a - u_{a_{j_W}} (leg j_W+1). The amplification bound from tau = t_W is
  valid with the right-hand value g_W (the attained gaps after t_W are <= g_W), and in the assembly g_W >= K_R R so
  min(g_W, K_R R) = min(g(t_W), K_R R) = K_R R anyway. Text amendment T5 (one clause).
* N2 (proviso in Part 2). thm:T3-E Part 2 does not say explicitly that legs stay defined; it follows from (CA'), since (a_j,a_{j+1})
  is good once u_{a_j} >= W1. Text amendment T5.
* N3 (monotonicity paragraph). "v, eps, U enter only as positive factors" is not literally true for k = k_fac 4(1+delta_t)/zeta
  (k enters c_n increasingly and c_beta decreasingly). The argument is correct if k, theta_h, omega0 (like eps_*, Dbar, X_*, z0max)
  are kept at their (v0, eps_*) values, which (D3) allows since 4(1+delta_t)/zeta is increasing in v. Independently, my sweep
  (`sweep.py`: 164 points, v from 6e-5 down to 6e-15, eps in {4e-11, 1e-15, 1e-30, 1e-60}, ALL derived quantities recomputed)
  finds no failure; the minimum slack of every condition is attained at (v0, eps_*). Text amendment T4.

## 2. Interface: assembly <-> touch-down

| item | sec_T3 needs (hyp:T3-HT) | cor:HTp-used / thm:HTp provides | status |
|---|---|---|---|
| ranges | v <= vbar = 6e-5, eps <= epsbar = 1e-3 (used eps <= 4e-11) | v_T = 6e-5, eps_T = 1e-3 | match |
| eta | window eta = 0.1 | eta = 0.1, xi1 = 1.007, lam0 = 0.0333, G_T = 0.05 | match |
| (T0), t_td <= T2, 1 <= U <= U_max | from hyp:HT | thm:HTp | match |
| (T1') N <= c_N lambda^{3/2 - muT_bar} | a' = 1-muT_bar, C0 = c_N | N <= c_N lambda^{3/2-mu_T} <= c_N lambda^{3/2-muT_bar} | match (a' = 0.99982 also allowed) |
| (T2') c >= min(c_sep, kappa2 (u_a+u'_b)) | | same | match |
| (T3') theta_v u^{1-mu_bar} | | theta_v u^{1-mu} <= theta_v u^{1-mu_bar} (u <= 0.05) | match |
| (T4') c_T4 (u'+z0)^{1-muT_bar} | | same, uses (SC51) | match |
| (T5') c_zlo eps^{1/(2-2v)} <= z0 <= c_zhi eps^{1/2}, abs(y0) <= c_y (z0+eps)^{2-muT_bar} | c_zlo = h_t xi_-, c_zhi = z_T xi_+ | same, uses (SC51) | match |
| (SC51) | z_T xbar_e + epsbar < 1, G + z_T xbar_e <= 1 | 0.0505094, 0.0995094 | holds |
| curve x^0, ghost set | "of Section sec:touch" (threshold 1.02 eps) | thm:HTp: curve of sec:HTp-curve (threshold xi1 eps = 1.007 eps) | same curve and same ghost set (labels with xi in [1.007eps, 1.02eps] are never within eps before t_td, so virtual = true there, lem:HTp-fwd(d)); not said in the text: amendment T2 |

Numbers. `code/Q3/constants.py chain('6e-5','0.1','1e-3', x1='1.007', lam0='0.0333', G='0.05')`: (SC1)-(SC50) all hold,
(SC51a,b) hold. **Independent confirmation** (`td_crosscheck.py`): the two referees' own constants codes
(`code/referee/Q3_1/consts.py`, `code/referee/Q3_2/consts.py`, written from the claims text) run at this row give no failed side
condition and reproduce T2, U_max, c_sep, kappa2, c_N, theta_v, c_T4, c_y, C_z, theta_T, h_t, xi_-, xi_+, z_T to all 14 printed
digits. So the row vbar = 6e-5 is not only "evaluated by the same code" (sec_HTp's status says "independently in code/Q4/final.py",
which is inaccurate: final.py imports chain() unchanged): amendment T8.

Outward rounding of cor:HTp-used checked against the 50-digit values: all 12 displayed bounds are on the safe side
(T2 3.73247 >= 3.7324640, U_max 6.29320 >= 6.2931948, c_sep 0.0330591 <= 0.03305915, kappa2 0.988089 <= 0.98808912,
C0 2.72160 >= 2.7215935, theta_v 1.07003 >= 1.0700235, c_T4 1.04263 >= 1.0426250, c_zlo 1.27025 <= 1.2702545,
c_zhi 1.56563 >= 1.5656236, c_y 0.619797 >= 0.61979693, muT_bar 1.79990e-4 >= 1.79989e-4, mu_bar 6.00037e-5 >= 6.00036e-5;
a' = 0.99982 <= 1-muT_bar = 0.99982001).
Caveat (text only): tab:T3-const prints the touch-down constants rounded to NEAREST, so several printed values are below the true
constants (theta_v, c_T4, C0, c_zhi, T2, U_max). The sentences "(H_T') holds with the constants of Table tab:T3-const" (sec_T3 l.506-507
and proof of thm:Main2 l.782-783) are therefore literally false for the printed digits, although all conditions also hold with the
outward values (verified). Amendment T3.

## 3. Constants (50-digit mpmath, printed digits)

Script `code/audit/C/audit_C_constants.py`, output `audit_C_constants.out`. Inputs: exactly the digits of tab:T3-const
(gamma 0.614267, R 0.001014, m 0.0561202, s0 0.0543222, kappa1 1.01594, c_A 0.996095, K_R 31.9496, K_f 5.03588, K_eps 999.98,
eta1 0.834088, q_c 2.05829, d_L 1.0000602, delta1 1.0001202, nu 3.10668e-4, A0 1.01292, f_F 0.136962, gamma_D 0.614666,
omega_bar 0.338254, k_fac 1.21399, delta0/R 0.149785, v0 6e-5, eps_* 4e-11). These are identical to `code/Q4/out/final.json`, so the
"printed vs exact input" rounding question does not arise for the core/assembly parameters: the verified inputs ARE the printed ones.

Result: **130 conditions, ALL HOLD** in each touch-down variant (EXACT 50-digit / OUT = cor:HTp-used / NEAR = tab:T3-const).
Tight conditions at the printed values (EXACT variant; OUT in brackets where different):

| condition | left | right | rel. slack | paper says |
|---|---|---|---|---|
| (P1) 1/(1-v) <= d_L | 1.000060003600 | 1.0000602 | 1.96e-7 | 2.0e-7 |
| (P1) e^{2v/(1-v)} <= delta1 | 1.000120014402 | 1.0001202 | 1.86e-7 | 1.9e-7 |
| (P3) c_amp v <= nu | 3.1066770e-4 | 3.10668e-4 | 9.71e-7 | 9.7e-7 |
| (P5) main | 0.13696188121 (0.13696189369) | 0.136962 | 8.67e-7 (7.76e-7) | 8.7e-7 (7.8e-7) |
| gamma_D >= gamma+nu+eta_N | 0.6146653412 | 0.614666 | 1.07e-6 | 1.1e-6 |
| (C2) | 0.996095 | 0.9961081 | 1.32e-5 | 1.3e-5 |
| (P2) c_rho K_f >= 2 | 2 | 2.0000345 | 1.72e-5 | 1.7e-5 |
| (P4) main | 0.0128336 | 0.0128372 | 2.81e-4 | 2.8e-4 |
| eta1 <= K_f/(K_f+1) | 0.834088 | 0.8343241 | 2.83e-4 | 2.8e-4 |
| T0 = T2+kappa1 U_max/(1-v0) <= 10.13 | 10.1263560 (10.1263672) | 10.13 | 3.6e-4 | 10.12636 (10.12637) |
| (PT) (1+delta_t) L_J < kappa1 | 1.0142971 | 1.01594 | 1.62e-3 | 1.62e-3 |
| (P7) main | 1.0142744 | 1.01594 | 1.64e-3 | 1.64e-3 |
| (TS) | 3.011540e-3 | 3.046823e-3 | 1.16e-2 | 1.16e-2 |
| (P6) main / stage A | 0.8974896 / 0.8974714 | 1 | 0.103 | 0.103 |

All ~1e-6 conditions hold at the printed digits; none is destroyed by rounding. Last-digit sensitivity (each printed parameter moved
by one unit in its last printed digit, worst direction): the chain fails for gamma +1 (P5, gamma_D), R -1 (P4, P5), kappa1 +1, c_A -1,
K_f -1, nu -1 (P3/P5), A0 +-1 (P5 / P4), f -1 (P5), gamma_D -1; everything else survives. So the printed digits are exactly
sufficient (as stated: dependent quantities rounded up, R down), and any re-typesetting must keep every digit.

Derived constants: all 25 core and 36 assembly values of tab:T3-const are reproduced to the printed 6 digits (max rel. difference
3.1e-6 for C_p, B_2U printed to 4 digits). Touch-down (SC1)-(SC51): hold (52 conditions). Monotonicity: spot checks at
(3e-5, 4e-11), (6e-8, 4e-14), (6e-5, 1e-30), (1e-9, 4e-11) and the 164-point sweep all pass.
eps_*: the value used, 4e-11, is <= min(epsbar, R/K_eps, (R/(100 c_zhi))^2) = 4.1947e-11 (text says ":=", amendment T4).

## 4. Statement-level checks

* Every direction seen: (T0) gives every direction seen on [0,t_td] or the direction of a true label of [0,U]; thm:T3-E(b') (via
  lem:T2-W(c)(3')) sees every true label's direction by T_stop. Correct.
* Path fixed in advance: design T on [0,t_td] and Construction C on the working front depend only on (v, min(eps, eps_*)); causality
  (Rem E-B(4)) for the coincidence of the stage-A cut and the full cut up to t_W. Correct. Same path as thm:Main (curve identity: T2).
* Speed <= 1: design T unit speed; lem:B-C(0) on working fronts; constant after T_stop. Correct.
* Time: T_stop <= t_td + kappa1 U/(1-v) <= T2 + kappa1 U_max/(1-v0) = 10.12636 <= 10.13. Correct.
* Scaling: path dP(t/d) with P the path for (v, eps/d), vision radius min(eps/d, 4e-11); eps in (0,d) => eps/d in (0,1) as
  prop:T3-cond requires. Correct.
* cor:Exact2 via lem:A41: D_N dyadic nested dense; eps_N = 2^{-N} 4e-11 -> 0 and min(eps_N, 4e-11) = eps_N; H_N = P_{v,eps_N},
  1-Lipschitz on [0,10.13], H_N(0)=0; proximity by time 10.13 independent of N; H(0)=0 from the Arzela-Ascoli limit in the proof of
  lem:limit. All hypotheses of lem:A41 are literally met. Correct.

## 5. Text amendments (none changes a statement, proof step or constant)

* T1 rem:T3-status (sec_T3 l.833-834): replace "This substitution, the typeset text of this section and the interface with
  Sections~\ref{sec:Estar} and~\ref{sec:HTp} have not been refereed; an audit of the typeset chain is to follow." by
  "This substitution, the typeset text of this section and the interface with Sections~\ref{sec:Estar} and~\ref{sec:HTp} have not
  been refereed; they were audited end to end afterwards (report \texttt{audit-C.md}: chain closed; all side conditions re-verified
  at the printed digits by independent code in \texttt{code/audit/C/})." In the status table, row "interface ...; final constants":
  "\texttt{Q4-1.md}, \texttt{audit-C.md} (not referee reports)".
* T2 "The path" (sec_T3 l.510-512), append: "Here $x^0$ is the curve of Subsection~\ref{sec:HTp-curve} with $\xi_1=1.007$; it
  coincides with the curve of Section~\ref{sec:touch}, and the ghost sets coincide, because the labels with
  $\xi\in[\xi_1\varepsilon,1.02\,\varepsilon]$ are never within $\varepsilon$ of Harry before $\Mtd$, so their virtual and true positions agree
  (Lemma~\ref{lem:HTp-fwd}(d))." Likewise in hyp:T3-HT replace "of Section~\ref{sec:touch}" by "of Section~\ref{sec:HTp}
  (equivalently, of Section~\ref{sec:touch})".
* T3 sec_T3 l.506-507: "\TzHT\ holds with the constants of Table~\ref{tab:T3-const}" -> "\TzHT\ holds with the constants of
  Corollary~\ref{cor:HTp-used} (shown rounded to nearest in Table~\ref{tab:T3-const}; the check uses their $50$-digit values and
  also passes with the displayed outward-rounded ones)"; same change in the proof of thm:Main2 (l.782-783).
* T4 eq:T3-const: "\varepsilon_*:=\min(\dots)" -> "\varepsilon_*\le\min(\dots)" (the value used is $4\cdot10^{-11}<4.19\cdot10^{-11}$).
  Monotonicity paragraph (l.560): "with $\varepsilon_*$, $\TzDb$, $X_*$, $z_0^{\max}$" -> "with $\varepsilon_*$, $\TzDb$, $X_*$, $z_0^{\max}$,
  $k$, $\vartheta_h$, $\omega_0$ and $\rho_*$"; and drop "by inspection ... positive factors" for $k$ (k enters c_beta with a negative power).
* T5 thm:T3-E proof, Part 2: after "Run the continuity argument ... for the whole family", add "Legs stay defined: for $u_{a_j}\ge\TzW$
  the pair $(a_j,a_{j+1})$ is good, so $c>0$ by (CA$'$)." and in the tail-pair item: "(F2) with $t'=\TztW$ and $g(t')$ the gap in the
  family of leg $\TzjW+1$, i.e.\ $g_W$".
* T6 lem:T3-W proof: after the list of cited lemmas add "and the parts of the proof of Theorem~\ref{thm:End} listed in
  Table~\ref{tab:Estar-unch} (with the computations of the proof of Theorem~\ref{thm:Bulk} that they quote), which hold on a working
  front by the argument of Lemma~\ref{lem:T2-W}(d)".
* T7 sec_Estar rem:Estar-status, "Use": "Lemmas~\ref{lem:Estar-L1}--\ref{lem:Estar-L3}" -> "Lemmas~\ref{lem:Estar-L1}--\ref{lem:Estar-L4}"
  (sec_T3 uses L4 in (F3)); "(... report \texttt{Q4-1.md}, not refereed.)" -> "(... reports \texttt{Q4-1.md}, \texttt{audit-C.md}; not refereed.)".
* T8 sec_HTp l.989-990: "(evaluated by the same code, and independently in \texttt{code/Q4/final.py})" -> "(evaluated by
  \texttt{code/Q3/constants.py}, which \texttt{code/Q4/final.py} calls unchanged; reproduced to all digits, with no failed side condition,
  by the two referees' independent codes \texttt{code/referee/Q3\_1/consts.py}, \texttt{code/referee/Q3\_2/consts.py}, report \texttt{audit-C.md})".
* T9 cosmetic: sec_T3 l.19 `\providecommand{\ESX}{\ESX}` is self-referential (infinite loop if sec_Estar.tex is absent); use
  `\providecommand{\ESX}{X_{\mathrm{far}}}`.

## 6. Stale sentences (Theorem Main2: v0 = 6e-5, T0 = 10.13) with replacement text

main.tex
1. Abstract l.24-29: "\emph{Main result:} for every vision radius $\varepsilon>0$ and every $v\le v_0=4\cdot10^{-51}$ ... by time
   $19.69\,d$ ... (Theorem~\ref{thm:Main}) ... ($\varepsilon=0$) by time $19.69\,d$ (Corollary~\ref{cor:Exact}); ... The constant $v_0$ is
   tiny because the proof is wasteful:" ->
   "\emph{Main result:} for every vision radius $\varepsilon>0$ and every $v\le v_0=6\cdot10^{-5}$, an explicit path fixed in advance sees
   every direction by time $10.13\,d$; neither $v_0$ nor the time depends on $\varepsilon$ (Theorem~\ref{thm:Main2}, which supersedes
   Theorem~\ref{thm:Main}: $v\le4\cdot10^{-51}$, time $19.69\,d$). Consequently, for every $v\le v_0$ a single path of speed at most $1$
   catches every direction exactly ($\varepsilon=0$) by time $10.13\,d$ (Corollary~\ref{cor:Exact2}); this is the first unconditional
   exact-capture result for this problem in these notes. The constant $v_0$ is small because the near-pair estimate of the proof is
   wasteful (the method cannot go much beyond $v\approx10^{-4}$): numerical experiments suggest that the same construction works up to
   $v\approx0.2$, but nothing is proved beyond $v_0$."
2. Abstract l.40-41: "(beyond the tiny range of Corollary~\ref{cor:Exact})" -> "(beyond the range $v\le6\cdot10^{-5}$ of
   Corollary~\ref{cor:Exact2})".
3. Abstract l.45-47: after "...two further audits (Remark~\ref{rem:T2-status})." add "The new links of the chain behind
   Theorem~\ref{thm:Main2} (Sections~\ref{sec:Estar}, \ref{sec:HTp}, \ref{sec:main2}) were each checked by two referees, the assembly with
   the older core; its interface with the new core and the typeset chain were audited end to end (Remark~\ref{rem:T3-status})."
4. Remark after lem:A41, l.262-263: "Such a uniform bound is proved in Section~\ref{sec:main} for $v\le4\cdot10^{-51}$
   (Theorem~\ref{thm:Main}), which gives Corollary~\ref{cor:Exact}." -> "Such a uniform bound is proved in Section~\ref{sec:main2} for
   $v\le6\cdot10^{-5}$ (Theorem~\ref{thm:Main2}; Section~\ref{sec:main} had $v\le4\cdot10^{-51}$), which gives Corollary~\ref{cor:Exact2}."
5. l.269-270: "The main result of these notes, Theorem~\ref{thm:Main} with Corollary~\ref{cor:Exact}, is proved in
   Sections~\ref{sec:bulk}--\ref{sec:main};" -> "The main result of these notes, Theorem~\ref{thm:Main2} with Corollary~\ref{cor:Exact2}, is
   proved in Sections~\ref{sec:bulk}--\ref{sec:main2};" and append to the paragraph (after l.283): "Sections~\ref{sec:Estar},
   \ref{sec:HTp} and~\ref{sec:main2} make every threshold of the end theorem a parameter (Theorem~\ref{thm:Estar}), extend the touch-down
   estimates to larger $v$ (Theorem~\ref{thm:HTp}), and apply the core once to the whole arc, which raises the range from
   $4\cdot10^{-51}$ (Theorem~\ref{thm:Main}) to $6\cdot10^{-5}$ (Theorem~\ref{thm:Main2})."
6. sec:open item 1, l.696-697: "\textbf{Unconditional exact capture for any $v>4\cdot10^{-51}$.} Exact capture is proved for
   $v\le4\cdot10^{-51}$ (Corollary~\ref{cor:Exact}). Open are: a non-negligible range of $v$ (the bootstrap in the proof of
   Theorem~\ref{thm:Main} needs tiny $v$;" -> "\textbf{Unconditional exact capture for any $v>6\cdot10^{-5}$.} Exact capture is proved for
   $v\le6\cdot10^{-5}$ (Corollary~\ref{cor:Exact2}). Open are: a non-negligible range of $v$ (the bootstrap in the proof of
   Theorem~\ref{thm:Main2} needs small $v$ and cannot go much beyond $v\approx10^{-4}$, Remark~\ref{rem:Estar-status};"
7. l.702: "For $v>4\cdot10^{-51}$ everything about exact capture is conditional:" -> "For $v>6\cdot10^{-5}$ ...".
8. l.713: "this is how Corollary~\ref{cor:Exact} is proved, and extending Theorem~\ref{thm:Main} to a realistic range" ->
   "this is how Corollaries~\ref{cor:Exact} and~\ref{cor:Exact2} are proved, and extending Theorem~\ref{thm:Main2} to a realistic range".
9. Item 2, l.715-717: "Theorem~\ref{thm:Main} gives the $\varepsilon$-independent range $v\le4\cdot10^{-51}$; Theorem~\ref{thm:D2} needs
   $v\lesssim1/\log(d/\varepsilon)$, which is larger for every $\varepsilon\ge e^{-10^{49}}d$," -> "Theorem~\ref{thm:Main2} gives the
   $\varepsilon$-independent range $v\le6\cdot10^{-5}$; Theorem~\ref{thm:D2} needs $v\lesssim1/\log(d/\varepsilon)$, which is larger for every
   $\varepsilon\ge e^{-756}d$ (about $10^{-328}d$)," [1/(22*756+28) = 6.0024e-5 > 6e-5; crossover at log(d/eps) = 756.30].
10. Item 5, l.727-728: "(including Corollary~\ref{cor:Exact}; the path of Theorem~\ref{thm:Main} has speed exactly $1$ until it stops)"
    -> "(including Corollaries~\ref{cor:Exact} and~\ref{cor:Exact2}; the path of Theorems~\ref{thm:Main} and~\ref{thm:Main2} has speed
    exactly $1$ until it stops)".
11. Numerics l.777: "(The only proved $\varepsilon$-independent range is $v\le4\cdot10^{-51}$, Theorem~\ref{thm:Main}, by a different
    construction.)" -> "(The only proved $\varepsilon$-independent range is $v\le6\cdot10^{-5}$, Theorem~\ref{thm:Main2}, by a different
    construction.)"

Other sections
12. sec_T2 l.39-40: "The range of $v$ is absurdly small ($v\le4\cdot10^{-51}$);" -> "The range of $v$ is absurdly small
    ($v\le4\cdot10^{-51}$; Section~\ref{sec:main2} raises it to $6\cdot10^{-5}$ for the same path, Theorem~\ref{thm:Main2});".
13. sec_T2 rem:T2-status l.851-854: after "no attempt was made to optimise it" add "here (the optimised assembly is
    Section~\ref{sec:main2})"; l.865-866: "\textbf{Nothing is claimed for $v>4\cdot10^{-51}$}" -> "\textbf{Nothing is claimed in this
    section for $v>4\cdot10^{-51}$} (Theorem~\ref{thm:Main2} proves the range $v\le6\cdot10^{-5}$)".
14. sec_D2 l.179: "An $\varepsilon$-independent range, $v\le4\cdot10^{-51}$, is proved for a different construction in
    Theorem~\ref{thm:Main}." -> "An $\varepsilon$-independent range, $v\le6\cdot10^{-5}$, is proved for a different construction in
    Theorem~\ref{thm:Main2}."
15. sec_E rem. "Use" l.1035-1038: append "Theorem~\ref{thm:Main2} uses from this section Lemma~\ref{lem:E-facts}(a),(b),
    Remark~\ref{rem:E-B}(4) and, through Theorem~\ref{thm:Estar}, the parts of the proof of Theorem~\ref{thm:End} listed in
    Table~\ref{tab:Estar-unch}, but not the statements of Theorem~\ref{thm:End} and Corollary~\ref{cor:End}."
16. sec_B l.709 "The remark is not used by Theorem~\ref{thm:Main}." -> "... by Theorems~\ref{thm:Main} and~\ref{thm:Main2}."; l.772
    "used for Theorem~\ref{thm:Main}" -> "used for Theorems~\ref{thm:Main} and~\ref{thm:Main2}"; l.780 "The unconditional result of
    these notes, Theorem~\ref{thm:Main}, avoids \textup{(T)}" -> "The unconditional results of these notes, Theorems~\ref{thm:Main}
    and~\ref{thm:Main2}, avoid \textup{(T)}".
17. sec_ST l.38 and l.628: "The main theorem (Theorem~\ref{thm:Main}) does not use the start S" -> "The main theorems
    (Theorems~\ref{thm:Main} and~\ref{thm:Main2}) do not use the start S" (sec_HTp also uses Lemma~\ref{lem:ST-D0}(a)).
18. sec_T1 l.45-46: "(stated in the next section, where it is the input of Theorem~\ref{thm:Main} and Corollary~\ref{cor:Exact})" ->
    "(stated in the next section, where it is the input of Theorem~\ref{thm:Main} and Corollary~\ref{cor:Exact}; Section~\ref{sec:HTp}
    proves it with sharper constants for $v\le2\cdot10^{-2}$, and its row $v\le6\cdot10^{-5}$ is the input of Theorem~\ref{thm:Main2})".
19. sec_T3 rem:T3-status, sec_Estar rem:Estar-status, sec_HTp rem:HTp-status: see T1, T7, T8.

## Files
* `code/audit/C/audit_C_constants.py`, `code/audit/C/audit_C_constants.out` (130 conditions x 3 variants, derived-vs-printed table,
  spot checks, last-digit sensitivity)
* `code/audit/C/sweep.py`, `code/audit/C/sweep.out` (164 (v,eps) points, no failure)
* `code/audit/C/td_crosscheck.py`, `code/audit/C/td_crosscheck.out` (touch-down row 6e-5 vs both referees' independent codes)
