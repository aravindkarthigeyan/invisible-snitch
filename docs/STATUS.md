# Status of the results

## Proved (checked by AI referees and audits; not yet by a human)

| Result | Where | Checked by |
|---|---|---|
| **Main theorem**: for $v \le 5.8\cdot10^{-3}$ and every $\varepsilon$, every direction is seen by time $13.1\,d$ | `paper/snitch.pdf` (version 2) Thm 1.1 | version 1 refereed twice as a standalone paper; each version-2 refinement refereed twice; two audits of version 2 |
| **Exact capture** at $\varepsilon = 0$ for $v \le 5.8\cdot10^{-3}$ | `paper/snitch.pdf` Cor 1.2 | as above |
| **Main theorem, readable form**: *some* $v_0 > 0$ works for every $\varepsilon$, with exact capture; no computer step | `paper/readable/snitch-readable.pdf` Thm 1.1, Cor 1.2 | built from a user-supplied streamlined outline (one false step found and fixed); refereed twice as a standalone paper; revision audited |
| Earlier versions: $v \le 6\cdot10^{-5}$ (time $10.13\,d$, `record/short-paper-v1.pdf`) and $v \le 4\cdot10^{-51}$ (time $19.69\,d$) | record, Thm "Main" | two referees per piece and two audits |
| $\varepsilon > 0$: every direction seen by $14.07\,d$ when $v \le 1/(22\log(d/\varepsilon)+28)$ | record, Thm D2 | two referees |
| $\varepsilon > 0$: an independent construction, $v \le 0.115/(\log(d/\varepsilon)+7.5)$, time $22.8\,d$ | record, Thm D3.1 | two referees |
| $\varepsilon > 0$: explicit path seeing every direction by $8d$ when $v \lesssim \sqrt{\varepsilon/\log(1/\varepsilon)}$ | record, Thm D1 | two referees |
| Lower bounds: any capture needs time at least $\max\{d/(1-v)+2\pi d/(1-v)^{3/2},\ (1+2\pi)d/(1-v)+2vd/(1-v)^2\}$ | record, §"constraints" | two referees |

## Conditional

- Exact capture for every $v < 0.4748$, assuming one hypothesis about the end phase of a dyadic discrete chase. It is supported numerically but unproved. (record, Thms B2, A2.3, A3.5)

## Open

- Exact capture for $v$ between $5.8\cdot10^{-3}$ and 1. Simulations of the same path succeed up to about $v = 0.2$; this proof framework appears to stop somewhere around $v \approx 0.05$.
- Whether Harry wins for **every** $v < 1$, as the problem's author conjectures, or whether there is a threshold.
- The head-on start (stop at first contact). Simulations say it works, through a self-tuned spiral at the last end, but there is no proof.

## Refuted or corrected along the way

- **"The bearing angle never exceeds π" (hypothesis H):** false for some finite sets of directions. This is a computer-assisted counterexample with interval arithmetic.
- **A capture condition of the form $|\partial_\alpha S| \le C(1+t)$:** false for every $v$, since the stretch is infinite at first contact.
- **Breakdowns seen in early simulations at $v = 1/2$ and $v = 0.8$:** these were properties of the discretisation or rounding error, not of the problem.
- **A gap in a refereed proof.** One step of the round-6 touch-down proof used a reversed inequality. It mattered only for $\varepsilon$ below about $10^{-6000}$; the statement was true, and the proof was repaired and re-refereed.

## How the checking worked

Each new proof was written by one AI agent and sent to two others. Those referees worked independently: one checked line by line, the other rebuilt the argument and tried to break it, usually with high-precision numerical tests. Fixes were applied and recorded. Then two audits read the assembled argument end to end. One checked every interface between sections and recomputed every constant; the other refereed every change made while typesetting. The reports are in [`record/reports/`](../record/reports).

None of this replaces a human referee. The argument is long, the constants are tight, and the checkers were all AI models.
