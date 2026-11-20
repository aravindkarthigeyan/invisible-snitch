# Referee report: repaired (T1) proof in Thm `thm:HT` and Prop `prop:T1-arcs`(2), `paper/sec_T1.tex`

Scope: I diffed `paper/sec_T1.tex` against the pre-edit copy `sec_T1.orig.tex`. The diff has four hunks: the header comment (lines 2-4), the proof of Prop. `prop:T1-arcs`(2) (new lines 947-971), the (T1) part of the proof of Thm `thm:HT` (new lines 1086-1109), and the closing remark (lines 1184-1186). Nothing else changed. I did not edit the paper.

## Verdicts

| Item | Verdict |
|---|---|
| (A) three-case proof of (T1) in Thm `thm:HT` | **OK** |
| (B) new proof of Prop `prop:T1-arcs`(2) (E1) | **OK** (one optional clarifying sentence) |
| Closing remark, lines 1184-1186 | **OK with fix** (the threshold number is wrong for Prop (2); exact text below) |

## (A) The (T1) proof in Thm `thm:HT`

**The cases are exhaustive.** The near-$X_0$ case is $u_a<\max(\lambda,1.04\varepsilon)$. The other two cases share $u_a\ge\max(\lambda,1.04\varepsilon)$ and split it into ($u'_b<\lambda$ and $\xi_e<\lambda$) versus ($u'_b\ge\lambda$ or $\xi_e\ge\lambda$). Together the three cases cover every pair.

**Near $X_0$.** This is the old near case, unchanged.

**Near $E_Y$.**
- $u'_a=u'_b+\lambda<2\lambda\le1/20$.
- The tail is the set of labels with $\xi\in[\xi_e,0.1]$. Here $\eta=0.1$ (line 377), so Lemma `lem:T1-tail`(c) covers the whole tail.
- In arclength $u'$ the tail has length at least $0.1-\xi_e\ge0.05$, because $w\ge1$ and $\xi_e\le0.05$ (tail (a)). Equivalently, $\xi\le\xi_e+u'<0.1$. So the pair lies in the tail. This "tail length" fact is derived inline, not quoted, and the derivation is correct.
- Tangent bound: $|T-\hat n|=|e^{i\psi}-1|\le|\psi|\le1.647\,\xi^{1-\mu_T}$ by (ii), which is tail (c). The orientation matches: increasing $u$ means decreasing $\xi$, which is the direction of increasing label, the same convention as in tail (c).
- Then $\xi\le s:=\xi_e+u'$, and $s$ ranges over an interval of length $\lambda$ inside $[0,3\lambda)$. For an increasing integrand, the integral over such an interval is at most $\int_{2\lambda}^{3\lambda}$.
- $p\mapsto3^p-2^p$ is increasing (its derivative $3^p\ln3-2^p\ln2$ is positive). So the bracket is at most 19.
- $\sqrt{19/(3-2\mu_T)}\le2.516614\le2.5167$, and $1.647\cdot2.5167=4.1450\le4.15$.
- The case hypothesis $u_a\ge\max(\lambda,1.04\varepsilon)$ is never used here. That is harmless.

**Far.**
- Statement (iii) holds on $\{u\ge1.04\varepsilon\}$. There $\xi\ge u/1.0151>1.02\varepsilon$, so these are true labels.
- Forward zone: $u\ge u_a\ge\lambda$ gives $u^{-\mu}\le\lambda^{-\mu}$.
- Tail: $u'\le1.015(\xi-\xi_e)$ (stated before (i)) gives $\xi\ge\xi_e+u'/1.015\ge\max(\xi_e,u'_b/1.015)\ge\lambda/1.015$.
- $1.0001\cdot1.015^{\mu_T}\le1.0002$.
- Elsewhere $|k|\le1.22$. This includes the hole, by Lemma `lem:T1-hole`(c).
- A locally Lipschitz function with a.e. derivative bounded by $K$ is $K$-Lipschitz on an interval. So $K=1.22\lambda^{-3v}$ works, using $\lambda<1$, $\mu\le3v$ and $\mu_T=3v/(1+v)\le3v$.
- $1.22/\sqrt{12}=0.35218\le0.353$.

**Assembly.** $\max(5.3,\,4.15,\,0.353)\le5.4$, and $\lambda^{3/2-\mu},\lambda^{3/2-\mu_T}\le\lambda^{3/2-3v}$. The constant 5.4 is correct.

**Leftover.** In (iii), "$\le1.0001\,\varepsilon^{-\mu_T}$" is true and no longer used. It is harmless.

## (B) Prop `prop:T1-arcs`(2), checked line by line

1. **$\bar k$ bounds $|k|$ on all of $\mathsf A_2$.**
   - *Tail labels* ($\xi\in[\xi_e,0.1]$): $\sigma=\int_{\xi_e}^{\xi}w\le1.015(\xi-\xi_e)\le0.1015$. So $\xi\ge\xi_e+\sigma/1.015\ge\sigma/1.015$, and $|k|\le1.0001\,\xi^{-\mu_T}\le1.0001\cdot1.015^{\mu_T}\sigma^{-\mu_T}\le1.22\,\sigma^{-\mu_T}=\bar k(\sigma)$, because $\min(\sigma,1)=\sigma$.
   - *Labels outside the tail* ($\theta\in[\alpha^*,\alpha_0-0.1]$, where $\alpha^*$ is the start of $\mathsf A_2$): Lemma `lem:T1-bulk`(b) applies, since $|\theta-\alpha_0|\ge\eta=0.1$, and gives $|k|\le1.22\le\bar k(\sigma)$ because $\min(\sigma,1)\le1$.
   - $\bar k(0)=\infty$ only at the endpoint $E_Y$. That is a single point, and $\bar k$ is integrable there.
2. **The integral step is justified.** $\psi$ is $C^1$ with $\psi'=k$, since the front is $C^\infty$ on true labels. Along $[\lambda/2,s]$ the variable $\sigma=\sigma_a-s'$ runs over an interval $J=[c,c+L]$ with $c\ge\sigma_b\ge0$ and $L=|s-\lambda/2|$. Then $\int_J|k|\le\int_J\bar k=\int_0^L\bar k(c+t)\,dt\le\int_0^L\bar k(t)\,dt$, because $\bar k$ is non-increasing. This is a translation toward $\sigma=0$, not a true rearrangement, and it is valid. The text says only "since $\bar k$ is non-increasing". Optionally, add: "(for $c\ge0$, $\int_c^{c+L}\bar k=\int_0^L\bar k(c+t)\,dt\le\int_0^L\bar k$)". The formula $\int_0^L\bar k=1.22L^{1-\mu_T}/(1-\mu_T)$ needs $L\le1$, and here $L\le\lambda/2\le1/80$.
3. **Hypotheses of Lemma `lem:T1-elem`(b).** The lemma needs a unit-speed $C^1$ curve, which holds, and any unit vector, here $e^{im}$. Also $l(a,b)=\lambda$, because the labels are arclength, and $|e^{i\psi}-e^{im}|\le|\psi-m|$.
4. **Arithmetic.**
   - $\int_0^\lambda|s-\lambda/2|^{2-2\mu_T}ds=2(\lambda/2)^{3-2\mu_T}/(3-2\mu_T)$.
   - $(2/3)^{1/2}2^{-3/2}=1/\sqrt{12}$.
   - The correction factor is $(1-\mu_T)^{-1}(3/(3-2\mu_T))^{1/2}2^{\mu_T}=1+\mu_T(1+1/3+\ln2)+O(\mu_T^2)\le1+6.1\cdot10^{-6}\le1.000007$, using $\mu_T\le3\cdot10^{-6}$.
   - $1.000007\cdot0.352184=0.352186\le0.3522\le0.36$.
   - The hypothesis $\lambda\ge\varepsilon/2$ is not even needed.

## Numerical check (`code/referee/T1fix/`)

**Method.**
- `front.py` is copied from `code/referee/Q3_2/` (the exact touch-down front, validated there against direct ODE integration).
- `a2scan.py` meshes the tail of $\mathsf A_2$ in $\xi-\xi_e\in\{0\}\cup[\varepsilon/1000,0.25]$ (geometric, ratio 1.3), using Gauss-Legendre-10 per cell.
- It computes $\sigma$ (arclength from $E_Y$) and evaluates every mesh pair with $\varepsilon/2\le\lambda\le1/40$.
- $N^2$ is computed with the exact identity $N^2=\int4w\sin^2((\psi-\varphi)/2)\,d\theta$, where $\varphi$ is the chord angle. This avoids cancellation in $l-c$.
- `validate.py` checks this identity against $2(l-c)$ from mpmath `quad`: the two agree to 12 digits.
- Pairs are classified by the case conditions of (A). The script also checks $|k|/\bar k(\sigma)$ and $|k|/(1.0001\,\xi^{-\mu_T})$ by central differences.
- Precision is mpmath at roughly $2.3\log_{10}(1/\varepsilon)+40$ digits. `summarize.py` prints the table.

**Results.** Maximum ratios over all scanned pairs:

| v | ε | ξ_e | pairs | N/λ^{3/2−μ_T} (≤0.36) | near-E_Y (≤4.15) | far N/λ^{3/2−3v} (≤0.353) | max abs(k)/k̄ | max abs(k)/(1.0001ξ^{−μ_T}) |
|---|---|---|---|---|---|---|---|---|
| 1e-6 | 1e-3 | 4.47e-2 | 479 | 0.28867 | – | 0.28867 | 0.8197 | 0.9999 |
| 1e-6 | 1e-6 | 1.41e-3 | 1852 | 0.28867 | 0.28867 | 0.28867 | 0.8197 | 0.9999 |
| 1e-6 | 1e-12 | 1.41e-6 | 6719 | 0.28867 | 0.28867 | 0.28867 | 0.8197 | 0.9999 |
| 1e-6 | 1e-20 | 1.41e-10 | 17468 | 0.28867 | 0.28867 | 0.28867 | 0.8197 | 0.9999 |
| 1e-6 | 1e-30 | 1.41e-15 | 37924 | 0.28867 | 0.28867 | 0.28867 | 0.8197 | 0.9999 |
| 1e-3* | 1e-3 | 4.45e-2 | 480 | 0.28619 | – | 0.28619 | 0.8138 | 0.9940 |
| 1e-3* | 1e-6 | 1.40e-3 | 1852 | 0.28756 | 0.28756 | 0.28664 | 0.8148 | 0.9941 |
| 1e-3* | 1e-12 | 1.39e-6 | 6720 | 0.28772 | 0.28772 | 0.28662 | 0.8149 | 0.9941 |
| 1e-3* | 1e-20 | 1.38e-10 | 17469 | 0.28772 | 0.28772 | 0.28660 | 0.8149 | 0.9941 |
| 1e-3* | 1e-30 | 1.37e-15 | 37925 | 0.28772 | 0.28772 | 0.28661 | 0.8149 | 0.9941 |

\* $v=10^{-3}$ is outside the paper's range $v\le10^{-6}$. It is a stress test only.

**Reading the results.**
- $N/\lambda^{3/2}\approx1/\sqrt{12}=0.2887$ throughout. That is the value for a curve of curvature about 1.
- The true constant sits about 18% below 0.3522. The near-$E_Y$ bound 4.15 is very loose, but valid.
- The curvature law $|k|\approx\xi^{-\mu_T}$ is sharp (ratio 0.9999), so the tail bound is essentially attained. $\bar k$ dominates $|k|$ with margin about 0.82.
- There is no $\varepsilon$-dependence down to $10^{-30}$. Below that, the effect of $\xi^{-\mu_T}$ is a factor of at most $e^{\mu_T\ln(1/\xi_e)}$, which the analytic proof covers.

## Fix for the closing remark (lines 1184-1186)

The remark says the gap is "relevant only for $\varepsilon\lesssim10^{-57577}$". That threshold comes from `referee-RQ3-2.md` §4 and concerns the (T1) far-case Lipschitz constant. For Prop (2) it is wrong:
- The old argument used $K=1.22\,\xi_e^{-\mu_T}$, which is a valid Lipschitz constant. The only invalid step was the conversion $\xi_e^{-\mu_T}\to\lambda^{-\mu_T}$.
- The old conclusion $0.36\,\lambda^{3/2-\mu_T}$ therefore follows unless $(\lambda/\xi_e)^{\mu_T}>0.36\sqrt{12}/1.22=1.0222$.
- At $v=10^{-6}$ this happens once $\varepsilon\lesssim10^{-6359}$, not $10^{-57577}$.

Suggested exact text:

> (a reversed inequality, relevant only for astronomically small $\varepsilon$: below about $10^{-6000}$ for Proposition~\ref{prop:T1-arcs}(2) and $10^{-28000}$ for \textup{(T1)})

Simpler alternative: "relevant only for astronomically small $\varepsilon$". The same number appears in the v4 changelog of `referee/P8a-claims.md` line 5 and should be fixed there too.

No other issues found.
