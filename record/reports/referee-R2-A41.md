# Referee report R2-A41: Lemma A4.1 (vanishing vision radius) and Lemma 4 (compactness)

Scope: `paper/main.tex`, Lemma `lem:A41` (lines 235-250) and everything its proof uses: Lemma `lem:limit` (lines 204-233),
including the Claim, the continuation condition `e + ||H_N - H|| < c/4`, the convention on caught trajectories, and the
standard ODE facts (Section 2, Section 11 preamble at lines 505-512). I read Sections 1-5 and the definitions in Section 11.
I did not read any other referee report.

**Overall verdict: OK with fixes.** I found no gap or false step. The argument is correct. The fixes below make explicit
four points the proof currently leaves implicit, and they sharpen the remark on nestedness into an actual counterexample.

## Claim-by-claim verdicts

| # | Claim | Verdict |
|---|-------|---------|
| 1 | The limit path `H` exists on `[0,T]`, `H(0)=0`, and is 1-Lipschitz (so `|H'|<=1` a.e.) | OK with fix F1 |
| 2 | Trajectories under a continuous `H` are unique, and they end before `T` only at a catch | OK with fix F2 |
| 3 | Claim: Lipschitz constant `8v/c`, Grönwall bound, continuation (clopen) argument | OK |
| 4 | `lem:limit`: every `alpha` in the union of the `D_N` is caught by `H` | OK with fixes F3, F4 |
| 5 | `lem:limit`: directions outside the union of the `D_N` are caught (openness plus density) | OK |
| 6 | `lem:A41`: replacing "caught at `t_N`" by "`rho_N(t_N) <= eps_N`" | OK with fix F5 |
| 7 | `lem:A41`: nestedness is needed (the single-direction remark) | OK; the remark can be strengthened (F6) |
| 8 | Remark after `lem:A41` ("exact capture follows from any bounded-time eps-strategy") | OK |

## Detailed checks

**1. Limit path.** The `H_N` are 1-Lipschitz with `H_N(0)=0`, so they are uniformly bounded by `T` and equicontinuous on
`[0,T]`. Arzelà–Ascoli gives a uniformly convergent subsequence, and its limit is 1-Lipschitz, so `|H'|<=1` a.e. by
Rademacher. The limit need not be unique, but only existence is claimed. `lem:A41` states explicitly that `H_N` is defined on
`[0,T]`; `lem:limit` only says "by time T" (fix F1). Passing to the subsequence is harmless: because the `D_N` are nested, the
union over the subsequence is the same dense set, and every `alpha` in `D_M` belongs to every later `D_N` of the subsequence.
This is the first use of nestedness.

**2. ODE conventions.** For continuous `H`, the right-hand side `v(S-H(t))/|S-H(t)|` is continuous in `(t,S)` and locally
Lipschitz in `S` on `{S != H(t)}`, so the solution is unique. Since `|S'|=v` and `|rho'|<=1+v` (from `rho' = v - rhat.H'`, as
in eq:P0), the maximal solution extends continuously to the end of its interval. Its interval ends before `T` only if
`rho -> 0` there, which is exactly "caught" with `S` extended by continuity. So the catch time is the first zero of `rho`, and
it is well defined. The paper states this in Section 11 (lines 505-509) but not in `lem:limit` (fix F2). The convention that a
caught trajectory stops being defined does no harm: every use of the Claim yields `rho >= c/4 > 0`, and that bound carries
existence of the trajectory with it.

**3. The Claim.**
- `rho >= c/2` on `[0, tau+delta]` with `delta = c/(2(1+v))`: this is correct, since `rho(tau) >= c` and `|rho'| <= 1+v`. The
  trajectory of `alpha` under `H` exists on `[tau, min(tau+delta,T)]` because `rho` stays at least `c/2 > 0` there.
- Lipschitz constant: for `|x|,|y| >= a`,
  `|x/|x| - y/|y|| <= |x-y|/|x| + |y|*||y|-|x||/(|x||y|) <= 2|x-y|/a`. With `a = c/4` this gives `8/c`, and multiplying by `v`
  gives `8v/c` for each of `S` and `H`. The bound holds pointwise and needs no convexity of the domain. Correct.
- Grönwall: with `Delta = |S^N_{alpha'} - S_alpha|`, we have `Delta' <= L(Delta + ||H_N-H||)` where `L = 8v/c`, so
  `Delta(t) <= Delta(0)e^{Lt} + ||H_N-H||(e^{Lt}-1) <= (Delta(0) + L T ||H_N-H||)e^{LT}`. This matches the paper's bound.
- Continuation: the set `{s : S^N_{alpha'}` is defined and `rho_N >= c/4` on `[0,s]}` contains 0, because
  `rho_N(0) = d >= c`. It is closed, because `rho_N` bounded below means the trajectory extends. It is relatively open, because
  on that set `rho_N >= c/2 - e - ||H_N-H|| > c/4` strictly. So it is the whole of `[0, min(tau+delta,T)]`. Correct.
- `U` and `N_0` exist: `|S_{alpha'}(0) - S_alpha(0)| = d|e^{i alpha'} - e^{i alpha}| -> 0`, and `||H_N-H|| -> 0` along the
  subsequence. Correct.

**4. Directions in the union.** Fix `alpha` in `D_M`. Suppose `H` does not catch `alpha` on `[0,t*]`. Then the trajectory is
defined there with `rho > 0`, so `rho >= c > 0` by compactness; this step is not written out (fix F3). The Claim with
`alpha' = alpha` and `tau = t*` gives `rho_N >= c/4` on `[0, min(t*+delta, T)]`. For large `N`, `t_N` lies in that interval,
because `t_N -> t*` and `t_N <= T`, but `rho_N(t_N) = 0`. This is a contradiction, so `alpha` is caught by time
`t* <= T`. Taking a further subsequence for `t_N` does not change `H`, which was fixed earlier. Using `liminf t_N` would also
work. Fix F4 makes the use of nestedness explicit.

**5. Directions outside the union.** If `alpha` is uncaught on `[0,T]`, then `rho >= c > 0` on `[0,T]`. The Claim with
`H_N = H` (so `||H_N-H|| = 0`) and `tau = T` shows that every `alpha'` in `U` is uncaught on `[0,T]`. So the uncaught set is
open, the caught set is closed, and the caught set contains a dense set, so it is the whole circle. Correct.

What about a direction whose trajectory under `H` passes very close to `H` before `T` without being caught? This is harmless.
Then `c = min rho` is tiny, and `U` shrinks roughly like `c e^{-8vT/c}`, but the argument only needs `c > 0`.

What about a direction caught early, say at `t_c < T`? It is not involved in the openness step. For `alpha` in the union, a
catch under `H` at some time `<= t*` is all that is needed. The catch need not happen at `t*`.

**6. `lem:A41`.** Take `t_N` to be the first time with `rho_N <= eps_N`. This time exists whenever `alpha` is seen, because
`rho_N` is continuous, and a catch is itself a time with `rho_N = 0 <= eps_N`. So the trajectory under `H_N` is defined on
`[0,t_N]`, which settles the question of trajectories being undefined after a catch. Any time at which the trajectory is
defined would in fact do: the Claim shows the trajectory is defined, with `rho_N >= c/4`, on all of `[0, min(t*+delta,T)]`.
For large `N`, `t_N` lies in that interval and `eps_N < c/4`, which contradicts `rho_N(t_N) <= eps_N`. So `eps_N -> 0`
together with `t_N -> t*` suffices. The proof does not use `eps_N < d` or `eps_N > 0`. Step 5 depends only on `H`, so "the
rest is unchanged" is accurate.

**7. Nestedness.** The proof uses nestedness only to ensure that each `alpha` in a dense set lies in `D_N` for all large `N`
of the Arzelà–Ascoli subsequence. A weaker hypothesis would do: each `alpha` in a dense set lies in all but finitely many
`D_N`. The paper's remark is right that some such hypothesis is needed, and in fact dropping it makes the statement false (not
merely unproved). Take `D_N = {alpha_N}` with `(alpha_N)` dense, `H_N` the straight run at `alpha_N`, `eps_N = 0`, and
`T = d/(1-v)`. All other hypotheses hold. But no path catches two directions by time `d/(1-v)`. By eq:P0,
`rho(T) = d + int rho' >= d - (1-v)T = 0`, with equality only if `H' = rhat_alpha` a.e. on `[0,T]`. Two different directions
have different `rhat` near `t = 0`, so both cannot be caught. Theorem `thm:E5` gives the same conclusion. See fix F6.

**8. Remark after `lem:A41`.** If, for a sequence `eps_k -> 0`, there are strategies that see all directions by a time
`T(eps_k) <= T`, then any nested finite dense family `D_N` satisfies the hypotheses. The remark is correct. Combined with
`thm:E5`, it also implies that any such uniform bound satisfies `T >= d/(1-v) + 2 pi d/(1-v)^{3/2}`. The authors may wish to
note this.

**Backward uniqueness.** `lem:A41` and `lem:limit` do not use it. It sits in Proposition 5(1) (`prop:length`; the brief calls
it Prop 6(1), but propositions have their own counter, so `prop:length` is number 5) and in `lem:E1`. I checked it anyway, and
it is OK: two candidates at the same point `!= H(t)` at time `t` both have `rho > 0` on `[0,t]`. The field is Lipschitz in `S`
on a compact neighbourhood of the two trajectories that stays away from `H`, so the trajectories coincide backwards.

## Fixes (exact replacement text)

**F1** (`lem:limit`, statement). Replace
`there is a path $H_N$ with $|H_N'|\le1$ that catches every direction in $D_N$ by time $T$`
with
`there is a path $H_N$ with $|H_N'|\le1$ on $[0,T]$ that catches every direction in $D_N$ by time $T$`

**F2** (`lem:limit`, proof). Replace
`so each candidate has a unique trajectory until $\rho\to0$.`
with
`so each candidate has a unique trajectory until $\rho\to0$. Since $|S'|=v$ and $|\rho'|\le1+v$, the maximal trajectory has a limit at the end of its interval, and that interval ends before $T$ only if $\rho\to0$ there, i.e.\ the candidate is caught; its catch time is the first zero of $\rho$.`

**F3** (`lem:limit`, proof). Replace
`If $H$ did not catch $\alpha$ on $[0,t^*]$ the Claim`
with
`If $H$ did not catch $\alpha$ on $[0,t^*]$, its trajectory would be defined on $[0,t^*]$ with $\rho>0$, hence $\rho\ge c$ for some $c>0$ by compactness, and the Claim`

**F4** (`lem:limit`, proof). Replace
`Now fix $\alpha\in D_M$. For $N\ge M$ it is caught by $H_N$`
with
`Now fix $\alpha\in D_M$. By nestedness, for every $N\ge M$ in the subsequence it is caught by $H_N$`

**F5** (`lem:A41`, proof). Replace
`replaced by ``$\rho\le\varepsilon_N$ under $H_N$ at $t_N$''.`
with
`replaced by ``$\rho\le\varepsilon_N$ under $H_N$ at $t_N$'', where $t_N\le T$ is the first such time (the trajectory under $H_N$ is defined on $[0,t_N]$, since a catch is itself such a time).`

**F6** (`lem:A41`, proof, optional strengthening). Replace
`(with $D_N$ a single direction and $H_N$ a straight run at it, every direction is seen infinitely often but nothing follows)`
with
`(with $D_N=\{\alpha_N\}$ for a dense sequence $(\alpha_N)$ and $H_N$ the straight run at $\alpha_N$, all other hypotheses hold with $\varepsilon_N=0$ and $T=d/(1-v)$, yet no path catches two directions by time $d/(1-v)$: by \eqref{eq:P0} that would force $H'=\rhat_\alpha$ a.e.\ for both directions, and these differ near $t=0$; compare Theorem~\ref{thm:E5})`

## Numerical sanity checks (`code/referee/A41b/`)

- `check_claim.py` tests the Claim on random 1-Lipschitz piecewise-linear `H`, with perturbations `H_N` satisfying
  `||H_N - H|| = eta` and nearby directions `alpha'`, chosen so that `e + eta < c/4`. Result: 120 checks and 0 failures. In
  every case `rho_N >= c/4` and the trajectory gap is at most the Grönwall bound `e`.
- `check_claim.py` also runs a straight run at `alpha = 0`. Direction `alpha = 0` reaches `rho ≈ 0` at `d/(1-v)`; the
  remaining `3e-5` is the integration step. For `alpha = 0.001, 0.01, 0.5, pi`, the minimum of `rho` stays at least `0.019`,
  consistent with `prop:ray` and with F6.
- `check_nearpass.py` tests the regime where `H` runs at heading `alpha + theta`, passing close to `S_alpha`
  (`c` from 0.20 to 0.68). Result: 16 checks and 0 failures.
- The Grönwall bound is very conservative (gaps of `1e-16` to `1e-5` against `e ~ 1e-2`), as expected from `e^{8vT/c}`. This
  affects only the size of `U`, not correctness.
