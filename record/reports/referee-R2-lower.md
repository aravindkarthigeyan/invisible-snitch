# Referee report R2: capture-time lower bounds ("Constraints on every path" and `sec_G.tex`)

This is the second, independent referee report. I read only `paper/main.tex` (Sections 1–5 for the model and
the cited results `prop:ray`, `prop:length`, `lem:limit`), the final text of Section `sec:constraints`, and
`paper/sec_G.tex`. I read nothing in `reports/`, `referee/` or `code/` apart from my own scripts in
`code/referee/R2lower/`.

## Scripts and what they check

| script | purpose |
|---|---|
| `code/referee/R2lower/constants.py` | Recomputes every displayed constant: the G2/E5 table, the crossover, the factorised difference, the E5 integration limit, the small-$v$ coefficients, the numbers in the G2$'$ remark, and a comparison of G2$'$ with Prop. E3eps. |
| `code/referee/R2lower/straight_length.py` | Computes the wavefront length at first contact for the straight first run, using the exact $(C,h)$ map. |
| `code/referee/R2lower/sim_checks.py` (output: `sim_checks_output.txt`) | RK4 simulation with 1500 or 960 candidates, $d=1$. |

The simulation covers 10 runs, all with speed $\le1$:

* straight run, then a circle of radius $0.7$, at $v=0.3$, $0.6$, $0.9$;
* zigzag at speed $0.8$ with a pause, at $v=0.3$, $0.6$, $0.9$;
* discrete chases in sweep order and in a bisection-like order, at $v=0.3$ and $0.5$.

It checks the following:

* **E1:** pair distances are monotone (adjacent pairs plus 4000 random pairs, at every step).
* **E2/E3:** the catch map is $\nu$-Lipschitz, at $t=0$ and at snapshot times; $\rho_P(t)\le\nu(\tau_P-t)$.
* **E3eps:** $|P-Q|\le\nu|\Delta\sigma|+2\varepsilon$ with $\varepsilon=0.05$, and $\sigma\ge(d-\varepsilon)/\nu$.
* **E5:** $(L^2)'\ge8\pi^2v\rho_{\min}$, its integrated form, and $\rho_{\min}\ge d-\nu t$.
* **G1:** $H\in K$; $\operatorname{Per}\ge2\pi d+2vt$; $D^+\operatorname{Per}\ge v\operatorname{Per}/\operatorname{diam}$; $L\ge\operatorname{Per}$.
* **G5:** $P'\ge vP/D-2|u|\cos(\gamma/2)$; $P'\ge-2\nu$; $|P'|\le2\pi$.

## Summary of verdicts

| result | verdict |
|---|---|
| Lemma E1 | **OK** (cosmetic: "in particular" needs $[0,t]\subset I$, which holds implicitly) |
| Corollary E2 | **OK** |
| Theorem E3 (extension, (a), (b), (c), (d)) | **OK** |
| Theorem E5 | **OK** |
| Proposition E3eps | **OK** |
| G1 (hull growth) | **OK** |
| G2 ($T\ge(1+2\pi)d/\nu+2vd/\nu^2$), with the remark "beats E5 for $v\ge0.8$" and its table | **OK** |
| G2$'$ ($\varepsilon>0$) | **OK** |
| G3 (measure form) | **OK** |
| G4 | **OK** |
| G5 | **OK**, with two trivial GAPs (fixes below) |
| G6 | **OK**, with a trivial measurability GAP (fix below) |

I found no ERROR. All displayed constants reproduce. All numerical checks pass, up to discretisation error.

---

## Detailed comments

### Lemma E1

* The identity $(\hat r_P-\hat r_Q)\cdot(\rho_P\hat r_P-\rho_Q\hat r_Q)=(\rho_P+\rho_Q)(1-\cos\psi)$ checks out.
* $S_P$ is $C^1$ because $S_P'=v\hat r_P$ is continuous in $t$ ($H$ is continuous). So $f$ is $C^1$ once $f>0$.
* $f>0$ follows from backward uniqueness. This needs both trajectories positive on $[0,t]$, which is automatic
  because a trajectory is only defined up to its capture.
* *Cosmetic:* the "in particular" clause needs $I\supset[0,t]$. It would read better as "on $[0,t]$ for $t<\min(\tau_P,\tau_Q)$".
* **Numerics:** the worst relative decrease of a pair distance was $4\times10^{-14}$ (round-off) over all 10 runs.

### Corollary E2

* Let $\tau(P)\le\tau(Q)$. E1 on $[t,\tau(P))$ plus continuity gives $\rho_Q(\tau(P))\ge|S_P(t)-S_Q(t)|\ge|P-Q|>0$.
  This also excludes $\tau(P)=\tau(Q)$.
* (P0) then gives $\tau(Q)-\tau(P)\ge\rho_Q(\tau(P))/\nu$.
* **Verdict: OK.**

### Theorem E3

**Lipschitz bound on $E=\{t\}\cup\tau(K_t)$.** For $\tau(P)<\tau(Q)$ we have
$|S_P(t)-S_Q(t)|\le\rho_Q(\tau(P))\le\nu(\tau(Q)-\tau(P))$, and $\rho_P(t)\le\nu(\tau(P)-t)$. Both are correct.

**Extension of the catch map.**
* Extending to $\bar E$ by uniform continuity, then to $[t,T]$ by linear interpolation (constant after $\sup\bar E\le T$), keeps the constant $\nu$.
* The paper's argument works: split $[x,y]$ at the nearest points of $\bar E$. Each piece is either inside one gap (linear, slope $\le\nu$) or between points of $\bar E$.
* This is the standard one-dimensional McShane-type extension. **OK.**

**(a)** $\mathcal H^1(c([t,T]))\le\operatorname{length}(c)\le\nu(T-t)$. **OK.**

**(b)**
* Take $t=0$ and $T=1,2,\dots$. The caught starting points form a countable union of subsets of rectifiable curves, so they have zero area.
* Only speed $\le1$ is used, through (P0). **OK.**

**(c)**
* For $t<d/\nu$ nothing is caught yet, so every point of the circle is in $K_t$ and $\Gamma(t)\subset c_t([t,T])$.
* $\Gamma(t)$ is closed and $c_t(t)=H(t)\notin\Gamma(t)$. So the first meeting time $t'$ exists, and the piece on $[t,t']$ has length $\ge|c_t(t')-H(t)|\ge\rho_{\min}(t)$.
* $c_t([t,t'))$ misses $\Gamma(t)$, so $\Gamma(t)\subset c_t([t',T])$. Hence
  $\operatorname{length}(c|_{[t',T]})\ge\mathcal H^1(c_t([t',T]))\ge\mathcal H^1(\Gamma(t))=L(t)$.
* $\Gamma(t)$ is injective (backward uniqueness) and $C^1$ (the variational equation has continuous coefficients). So $\mathcal H^1(\Gamma)$ equals its length.
* Lengths over the two consecutive time intervals add. **OK.**

**(d)** Take (c) at $t=0$: $\rho_{\min}=d$ and $L=2\pi d$. **OK.**

**Numerics.** For the 6 and 8 targets caught in the chases:
* $\max |P-Q|/(\nu|\Delta\tau|)$ lies between $0.40$ and $0.70$.
* At snapshot times $t=0.5,1,2$, $\max|S_P(t)-S_Q(t)|/(\nu\Delta\tau)\le0.91$.
* $\max\rho_P(t)/(\nu(\tau_P-t))=1.000000$, with equality for the target being chased in a straight line, as expected.

### Theorem E5

**Is $L$ really $C^1$ up to $t_1$?**
* It is $C^1$ on $[0,t_1)$, which is all the proof claims and all it needs.
* On $\mathbb S^1\times[0,t]$ with $t<t_1$, $\rho\ge d-\nu t>0$. Together with continuity of $\partial_\alpha S$ (solution of the linear variational equation), this makes $\partial_t|\partial_\alpha S|=(v/\rho)\sin^2\phi\,|\partial_\alpha S|$ jointly continuous. So $L'=\int\partial_t|\partial_\alpha S|$.
* The proof never evaluates $L$ or $L'$ at $t_1$: it integrates on $[0,t]$ and lets $t\uparrow t_1$. **OK.**

**Cauchy–Schwarz step.**
* $\rho|\partial_\alpha\beta|=|\sin\phi||\partial_\alpha S|$, because $H$ does not depend on $\alpha$.
* So $\int|\partial_\alpha\beta|=\int\sqrt{\sin^2\phi|\partial_\alpha S|/\rho}\cdot\sqrt{|\partial_\alpha S|/\rho}$. Squaring gives the displayed product.
* The second factor is $\le L/\rho_{\min}$.
* $\int|\partial_\alpha\beta|\ge2\pi$ follows from winding number 1, which holds by the homotopy argument on $\mathbb S^1\times[0,t]$.
* Result: $LL'\ge4\pi^2v\rho_{\min}$. **OK.**

**Is $\rho_{\min}\ge d-\nu t$ used correctly?** Yes, both times, and in the right direction:
* It is used as a lower bound to weaken $LL'\ge4\pi^2v\rho_{\min}$.
* It is used as a lower bound for the term $\rho_{\min}$ in E3(c).

**Integration.** $L^2(t)\ge4\pi^2d^2+8\pi^2v(dt-\nu t^2/2)$. At $t_1=d/\nu$ this equals $4\pi^2d^2(1+v/\nu)=4\pi^2d^2/\nu$; checked symbolically and numerically.

**Final step.** $T\ge t+(d-\nu t+L(t))/\nu=d/\nu+L(t)/\nu$. Take the supremum over $t<t_1$. **OK.**

**Dense-set clause.**
* $c_t$ is built from the caught dense set. Its image is compact and contains a dense subset of $\Gamma(t)$, hence all of $\Gamma(t)$.
* All directions are still uncaught at $t<t_1$, so $L(t)$ and $\rho_{\min}$ are the same objects as before. **OK.**

**Numerics.**
* $\min(L^2)'/(8\pi^2v\rho_{\min})$ is $1.0003$ to $1.0018$ in every run. The minimum is attained at $t=0$, where the inequality is an *equality*: the circle has $\phi=\pi/2$ and $\rho\equiv d$. The excess is $O(dt)$ from forward differences.
* $\min L^2/(\text{integrated bound})=1.00000$, attained at $t=0$.

**Remark after E5.**
* First-order coefficients: $(1+3\pi)$ for E5 and $(1+4\pi+2\pi^2)$ for Theorem B. Both are confirmed by numerical differentiation ($10.4248$ and $33.3056$).
* G2 has coefficient $3+2\pi=9.283$, so E5 is the better bound at small $v$, consistent with the crossover below.

### Proposition E3eps

**The inequality.**
* For $\sigma(P)\le\sigma(Q)$, E1 applies on $[0,\sigma(P)]$ because both $\rho\ge\varepsilon>0$ there.
* Then $|P-Q|\le\varepsilon+\rho_Q(\sigma(P))$, and $\rho_Q(\sigma(P))\le\rho_Q(\sigma(Q))+\nu(\sigma(Q)-\sigma(P))$.
* $\rho_Q(\sigma(Q))=\varepsilon$ exactly, because $\rho_Q(0)=d>\varepsilon$ and $\rho_Q$ is continuous. **OK.**

**Covering argument at scale $\delta$.**
* Use $k=\max(1,\lceil\ell/\delta\rceil)\le\ell/\delta+1$ intervals.
* The directions seen during one interval have pairwise chord $\le D<d$, so pairwise angle $\le\theta:=2\arcsin(D/2d)<60^\circ$.
* A set of points on the circle with pairwise angular distance $\le\theta<2\pi/3$ lies in a closed arc of length $\theta$: take a point $p$ and its two extreme neighbours at angles $a,b\le\theta$; then $a+b\le2\theta<2\pi-2\theta$, so their angular distance is $a+b\le\theta$.
* So $k\theta\ge2\pi$, and the stated bound follows. **OK.**
* *Remark, not a gap:* $D<\sqrt3\,d$ would suffice instead of $D<d$.

**Numerics.**
* In the sweep chase at $v=0.3$, 153 candidates were sighted. $\max[|P-Q|-(\nu|\Delta\sigma|+2\varepsilon)]=-0.084<0$.
* The minimum sighting time equals $(d-\varepsilon)/\nu$ to 4 digits (the forward ray).

### G1 (hull growth before first contact)

**Is Harry inside the hull?** Yes.
* The winding number of $\Gamma(t)$ about $H(t)$ is $1$, by the homotopy on $\mathbb S^1\times[0,t]$.
* A curve inside an open half-plane that misses $p$ has winding number 0 about $p$. So $H(t)\in K(t)$; in fact $H(t)\in\operatorname{int}K(t)$, since a closed half-plane minus a boundary point is star-shaped.
* Hence $\rho_\alpha\le\operatorname{diam}K$.

**Support function and Danskin.**
* $\phi(\alpha,t)=S_\alpha(t)\cdot e_\theta$ has $\partial_t\phi=v\hat r_\alpha\cdot e_\theta$, jointly continuous on $\mathbb S^1\times[0,t_*)$, and $\mathbb S^1$ is compact.
* So Danskin's theorem gives $D^+g=\max$ over the maximisers. This is correct at every $t<t_*$.
* For a maximiser, $r_\alpha\cdot e_\theta=f\ge0$, where the sign uses $H\in K$. Hence $\hat r\cdot e_\theta=f/\rho_\alpha\ge f/D$.

**Integration over $\theta$.**
* The difference quotients are bounded by $v$, so dominated convergence lets the right derivative pass under $\int d\theta$.
* $\int H\cdot e_\theta\,d\theta=0$, and $D\le\operatorname{Per}/2$. So $D^+\operatorname{Per}\ge2v$.
* $\operatorname{Per}$ is Lipschitz, so it can be integrated. Then use $L\ge\operatorname{Per}$. **OK.**

**Numerics.**
* $H\in K$ held at all times in all 10 runs.
* $\min[\operatorname{Per}-(2\pi+2vt)]=-1.1\times10^{-5}$. This is the polygon defect at $t=0$, $\approx-2\pi\cdot\pi^2/(6M^2)$.
* $\min \operatorname{Per}'/(v\operatorname{Per}/\operatorname{diam})$ ranges from $1.42$ to $1.97$, so the bound is never violated.
* $\min\operatorname{Per}'/v$ ranges from $4.30$ to $6.12$. This agrees with the paper's numerical "rate $\approx4v$" remark.
* $L\ge\operatorname{Per}$ held to $10^{-14}$.

### G2: the passage from G1

* The inequality used is $T\ge t+L(t)/\nu$ for $t<d/\nu$. It is a weakening of E3(c) (drop $\rho_{\min}\ge0$), which is proved.
* It is reproved independently in G3(ii) for all $t$.
* $L(t)$ in G1 is the same object: the length of $\Gamma(t)$.
* Adding back $\rho_{\min}\ge d-\nu t$ gives the same limit, so nothing is lost.
* Then $T\ge t+(2\pi d+2vt)/\nu$, which increases in $t$. As $t\uparrow d/\nu$ the limit is $(1+2\pi)d/\nu+2vd/\nu^2$. **OK.**

**Table (recomputed, $d=1$):**

| $v$ | G2 | E5 |
|---|---|---|
| 0.5 | 18.57 | 19.77 |
| 0.7 | 39.83 | 41.57 |
| 0.8 | 76.42 | 75.25 |
| 0.9 | 252.83 | 208.69 |
| 0.95 | 905.66 | 581.99 |
| 0.99 | 20528.3 | 6383.2 |

All entries match the paper after rounding.

**Crossover.**
* The factorisation $\nu^2(\mathrm{G2}-\mathrm{E5})/d=(2\pi-2)\nu-2\pi\sqrt\nu+2$ was verified on a grid.
* Its roots in $\sqrt\nu$ are $0.466942$ and exactly $1$.
* So G2 > E5 iff $\nu<0.218035$, i.e. $v>0.781965$.
* "Beats E5 for $v\ge0.8$" is true (conservative). "$\sqrt\nu<0.466$" is a valid sufficient condition, and $\sqrt{0.2}=0.447$.

**Numbers in rem:G1-conj.**
* $L(d/\nu)$ from the exact map is $7.6817$, $11.7249$, $50.679$, $443.06$–$443.08$ at $v=0.2$, $0.5$, $0.9$, $0.99$. The paper quotes $7.68$, $11.72$, $50.68$, $443.06$.
* $2\pi+4v/\nu=402.28$ at $v=0.99$. All confirmed.

### G2$'$ ($\varepsilon>0$)

**Step 2 (restart at time $t$).**
* E1 on $[t,\sigma(\alpha)]$ with $\rho\ge\varepsilon>0$ is legitimate.
* $\rho_{\alpha'}(\sigma(\alpha'))=\varepsilon$ uses $d>\varepsilon$.
* $\operatorname{diam}A_i\le\nu\delta+2\varepsilon$. **OK.**

**Step 3.** Consecutive non-empty $A_i$ give $\ell\le2\varepsilon(\#-1)+\nu(s_{\rm last}-s_{\rm first})\le2\varepsilon(k-1)+\nu(T-t)$. **OK.**

**Step 4.**
* $\Gamma(t)\subset c+\bar B(0,D_\delta)$, because no candidate is seen by time $t$ and all are seen by $T$. Hence $K(t)\subset\operatorname{conv}(c)+\bar B(0,D_\delta)$.
* Steiner's formula plus monotonicity of perimeter give the upper bound.
* $\operatorname{Per}\operatorname{conv}(c)=\int_0^\pi\text{width}\le\sum_{\rm seg}|{\rm seg}|\int_0^\pi|\cos|=2\ell$. **OK.**

**Step 5.**
* Halving the perimeter inequality and using $k-1<(T-t)/\delta$ reproduces the display exactly.
* The resulting bound on $T$ has $t$-derivative $1+v/(\nu(1+2\varepsilon/\lambda))>0$.
* Taking $t\uparrow(d-\varepsilon)/\nu\le t_s$ gives the statement. **OK.**

**Asymptotics with $\lambda=d\nu^{-1/2}$.** $2\varepsilon/\lambda=O(\sqrt\nu)$ and $\pi\lambda\nu/(v(d-\varepsilon))=O(\sqrt\nu)$. **OK.**

**Remark numbers ($\varepsilon=0.1$).**

| $v$ | ratio with $\lambda=\nu^{-1/2}$ (paper) | ratio with optimal $\lambda$ (paper) |
|---|---|---|
| 0.99 | 0.6725 (0.67) | 0.8815 (0.88) |
| 0.999 | 0.8877 (0.89) | 0.9522 (0.95) |
| 0.9999 | 0.9635 (0.96) | 0.9838 (0.98) |

* At $v=0.7$, $\varepsilon=0.1$: the optimal $\lambda=0.378$ gives $10.468$ (paper: $10.5$). With $\lambda=\nu^{-1/2}$ the bound is negative and so trivial. The remark evidently uses the optimal $\lambda$; it could say so.
* *Editorial suggestion:* at $v=0.7$, Prop. E3eps itself gives $16.37$ (best $\delta\approx2.40$), which is stronger than G2$'$. At $v=0.99$, G2$'$ gives $7854$ against $491$ for E3eps. A sentence noting this would help. It is not an error.

### G3

* **$U(t)$ is open.** This follows from the Claim of `lem:limit` with $H_N=H$. The Claim only needs $\rho\ge c>0$ on $[0,t]$, which holds by compactness. **OK.**
* **Step 2.** The Lipschitz map $\tau(B)\to F_t(B)$ and the injectivity of $\tau$ on $B$ are correct.
* **Steps 3–4.** Lipschitz maps scale outer $\mathcal H^1$ by at most the constant; the area formula holds for an injective $C^1$ map on a Borel set. **OK.**
* **Step 5.**
  * The left endpoints of the nested dyadic intervals increase to $\tau(\alpha)$.
  * $|\partial_\alpha S|$ is non-decreasing in time, so monotone convergence applies.
  * The integrands are measurable, being piecewise continuous on Borel pieces.
  * The exhaustion $J\cap(1/n,n]$ completes the argument. **OK.**
* **(i) and (ii).** Both are correct.
* *Note:* the remark "catches must be tangential" is heuristic; the $\rho^{-v/\nu}$ growth was checked by linearisation, $y'=vy/\rho$ with $\rho'=-\nu$.

### G4

* $L(t)=\int_{U(t)}|\partial_\alpha S(\cdot,s)|+\mathrm{Str}(s,t)$ holds by Tonelli.
* $\int_{U(s)\setminus U(t)}|\partial_\alpha S(\cdot,s)|\le\nu(t-s)$ is (G3a) with $J=(s,t]$.
* $L(s)<\infty$ because $T<\infty$. So $T\ge s+(L(s)+\mathrm{Str})/\nu$. **OK.**

### G5

**Step 2.** The Hausdorff distance satisfies $d_H(X(t),X(s))\le s-t$; the case of a candidate caught in between, $v(\tau-t)+(s-\tau)\le s-t$, is handled correctly. **OK.**

**Step 3.** The proof's inequality
$\hat r\cdot e_\theta\ge(r(t)\cdot e_\theta-(1+v)h)/(D+(1+v)h)$ needs the numerator to be non-negative. The condition $h<f/(2\nu)$ does not guarantee this.
* **GAP (trivial).** Fix: also require $h<f/(2(1+v))$, i.e. use the bound only for small $h$. Only $h\to0$ is used anyway.

**Step 5.**
* The normal cone at $H$ is $\{f=0\}$, an arc of length $\pi-\gamma$.
* $\min_u\int_Nu\cdot e_\theta=-2|u|\cos(\gamma/2)$.
* Other boundary cases give a null set $N$.
* $D\le\operatorname{diam}K\le P/2$. **OK.**

**(ii) (needle condition).**
* The convex quadrilateral $a,c,b,c'$ and the bound $|ac|+|cb|\ge\sqrt{D_K^2+4h_1^2}$ are correct.
* So is the Jensen step $\Rightarrow P\ge2\sqrt{D_K^2+w^2}$.
* Hence $w/D<\sqrt{1-v^2}/v$.
* Approximations confirmed: $2\arccos v\approx2\sqrt{2\nu}$ and $\sqrt{1-v^2}/v\approx\sqrt{2\nu}$ (e.g. $0.2831$ vs $0.2828$ at $v=0.99$).

**GAP (cosmetic).** The lemma says "assume $U(t)$ is non-empty", but it states the Lipschitz property and $P(T)=0$ on all of $[0,T]$, where $D$ is undefined once $U=\emptyset$.
* Fix: state (G5) for a.e. $t$ with $U(t)\ne\emptyset$, and put $P\equiv0$ when $U(t)=\emptyset$. G6 already does this.

**Numerics.**
* $\min[P'-(vP/D-2|u|\cos(\gamma/2))]$ lies between $-7.5\times10^{-6}$ and $-6\times10^{-7}$. These are $O(dt)$ forward-difference errors; no real violation.
* $P'\ge-2\nu$ and $|P'|\le2\pi$ held in all runs, including the post-contact parts of the chases.

### G6

The case analysis is correct:
* non-needle times give $P'\ge0$;
* needle times give $P'\ge-2\nu$;
* $P(t_1)\ge2\pi d+2vt_1$ follows by continuity of $P$ and G1.

**GAP (trivial).** Measurability of the set of needle times is not shown, because $\gamma(t)$ and $D(t)$ are not shown to be measurable.
* Fix: bound by the measurable set $\{t:P'(t)<0\}$. By G5(ii) it is contained, up to a null set, in the needle times. Then $P(t_1)\le\int(P')^-\le2\nu|\{P'<0\}|\le2\nu|\text{needle times}|^*$ (outer measure).
* Alternatively, state the corollary with outer measure.

---

## Answers to the specific questions

1. **E3(c): length / Hausdorff step and the extension.**
   * The extension of the catch map to a Lipschitz curve is correct.
   * The step "covering $\Gamma(t)$ costs length $\ge L(t)$" is $\operatorname{length}\ge\mathcal H^1(\text{image})\ge\mathcal H^1(\Gamma)$. It is correct, and splitting at the first hitting time $t'$ correctly adds $\rho_{\min}$.
2. **E5.**
   * $L$ is $C^1$ on $[0,t_1)$, not up to $t_1$, and the proof only needs the former.
   * $\rho_{\min}\ge d-\nu t$ is used as a lower bound in both places, in the right direction.
   * The Cauchy–Schwarz step and the integration are correct.
   * The differential inequality is sharp at $t=0$.
3. **G1.**
   * Harry lies in the interior of the hull, by the winding-number argument.
   * The Danskin derivative and the dominated-convergence step are correct.
4. **G1 → G2.**
   * The input is $T\ge t+L(t)/\nu$ for $t<d/\nu$. It is a weakening of the proved E3(c), and is independently proved as G3(ii).
5. **Covering arguments.**
   * The covering in E3eps (arcs of angle $2\arcsin(D/2d)$) is correct.
   * The covering in G2$'$ (polyline plus Steiner plus Cauchy–Crofton) is correct.
6. **Constants.** All reproduce; see `constants.py`. "G2 beats E5 for $v\ge0.8$" is correct: the exact crossover is $v=0.78196$.
