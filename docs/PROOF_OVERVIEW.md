# How the proof works

This is a plain-language guide to [`paper/snitch.pdf`](../paper/snitch.pdf). Section numbers refer to the paper.

## 1. Chasing every Snitch at once

Harry does not know the starting direction $\alpha$, and his path is fixed in advance. So for each possible $\alpha$ there is a **candidate**: the Snitch that started in that direction, fleeing Harry along his fixed path. At time 0 the candidates sit on a circle of radius $d$. As Harry moves, they spread outward and form a closed curve, the **front**. Harry wins if every candidate is, at some moment, within distance $\varepsilon$ of him. We take $d = 1$; everything scales.

The candidates near Harry are the delicate ones. A candidate at distance $\rho$ is pushed straight away from him, so its direction of motion turns as Harry passes. Neighbouring candidates are pushed in slightly different directions, and the front near Harry bends. That bending is what the whole proof has to control.

## 2. Modified candidates (§2)

A real candidate is undefined once Harry reaches it, since its speed has no direction at distance 0. The proof uses **modified candidates** instead, which move by

$$x' = v\,\frac{x - H}{\max(|x-H|,\ \varepsilon)} .$$

They agree with the real candidates until each is first seen, so seeing all modified candidates means seeing all real ones. Their front is a smooth curve for all time, and two modified candidates never move closer together.

## 3. The quantity that stays bounded (§2–4)

For two points $a, b$ on the front, let $E(a,b)$ be the **arc length between them minus their straight-line distance**. It is zero for a straight segment and grows as the piece of front between them bends. The paper works with $N = \sqrt{2E}$.

The key estimate is that, for a pair of points a distance $\lambda$ apart along the front,

$$N(a,b) \;\le\; M\,\lambda^{1/2+\gamma}$$

**at every scale** $\varepsilon/2 \le \lambda \le R$, for fixed constants $M, \gamma, R$ that do not depend on $\varepsilon$. It is a scale-by-scale flatness statement. It allows the front to bend near Harry, but only by an amount that shrinks with the scale.

Bounds of this kind are what make the time to sweep the front finite and independent of $\varepsilon$. A flat front ahead of Harry means walking along it costs about its length, and its length grows only at a bounded rate.

## 4. The walk (Construction C, §3)

From a starting point on the front, Harry repeatedly heads straight for the point of the front at chord distance $\varepsilon$ ahead. Each leg sees everything it passes. The **end theorem** (Theorem 3.4) says that if the front ahead satisfies the flatness bound at the start, it keeps satisfying it for the whole walk, right up to the end of the arc. The proof is a first-failure-time argument:

- **Far pairs** (far from Harry compared with their size, Prop. 4.2): they feel only a smooth, slowly varying field, and their excess changes little.
- **Near pairs** (Prop. 4.3): Harry passes them quickly, and the total change during the passage is bounded by an integral that converges uniformly in $\varepsilon$.
- **Length** (Prop. 4.4): the total length of the remaining front grows at a bounded rate, so the walk ends in bounded time.

## 5. Why the start matters (§6–7)

The obvious start is to run at the front and turn at first contact. That leaves a **corner**: the two sides of the front meet at a slight angle. Whichever side Harry walks first, the other side is left behind at a small fixed angle. Over time it curls into a slowly winding spiral, and the flatness bound fails there. Simulations to depths of $10^{-137}$ show Harry still wins in that case, but only through a delicate self-correcting balance that resisted proof.

The proof's path avoids the corner:

1. **Run through** the front and a distance 1 beyond it. The front behind Harry stays smooth, apart from a small hole of already-seen directions.
2. **Touch down tangentially**, by running straight at the candidate at angle $\alpha_0 = \arccos(v + 1/t_1)$, the point where a straight line from Harry just grazes the front.

Both runs are straight, and for straight runs the candidates' motion has **exact conserved quantities**: $\rho\sin\beta/\tan^v(\beta/2)$ is constant, and $\rho(\cos\beta + v)$ decreases at the constant rate $1-v^2$. So the front at touch-down is known in closed form. Section 7 uses this to prove the flatness bound at touch-down, both ahead of Harry and at the end he leaves behind, which he left tangentially.

## 6. Leaving the end behind, and coming back (§5, §8)

At touch-down, the last end Harry will walk into is right behind him. The proof treats the pairs near that end separately at first:

- while Harry walks away from that end, it keeps its shape (the departure theorem, Thm 5.2);
- once he is far enough away, those pairs rejoin the main argument as far pairs, with exactly the bound the end theorem needs.

The assembly (§8) puts it together in one walk. Every pair of points at every time is covered by exactly one of these statements; the paper has a table.

## 7. From $\varepsilon > 0$ to exact capture (§2, Cor. 1.2)

For each vision radius $\varepsilon$ there is a path that sees everything by time $T_0 = 10.13$. Take $\varepsilon_N \to 0$. All these paths are 1-Lipschitz on the same interval $[0, T_0]$, so a subsequence converges uniformly to a 1-Lipschitz path $H$. If some direction were never caught exactly by $H$, it would stay a positive distance from $H$, and by continuity also from the nearby paths $H_N$. That contradicts their coming within $\varepsilon_N \to 0$ of it. So $H$ catches every direction exactly.

This step is why the time bound must not depend on $\varepsilon$.

## 8. The constants (Appendix A)

The proof has many explicit constants: thresholds for "near" and "far", exponents, scales, and the touch-down constants. They must satisfy 201 inequalities. `paper/verify_constants.py` checks every one in 50-digit arithmetic. The largest speed for which all of them hold, with safe rounding, is $v_0 = 6\cdot 10^{-5}$.

The binding inequalities belong to the near-pair estimate of Prop. 4.3, which is loose: simulations show about $10^5$ times less growth than it allows. With this method $v$ cannot go much beyond about $10^{-4}$. Going further would need a sharper near-pair estimate.
