# P6c2-claims: the regularity class of the left arm at the entry time (Round 6c)

Only PROVED statements, with proofs. Context and numerics: `reports/P6c-1.md`, "Round 6c". Notation and standing
assumptions of `referee/P6c-claims.md`, Round 6b: construction C_cut of P6a, v ≤ 1/100, ε ≤ 10⁻³, θ_0 = δ = 0.1, label sets
R = [0, 2δ], B = [2δ, 2π − 2δ], 𝒜 = [2π − δ, b_e], r_b = |x_b(t_0) − O|, D = r_{a_j} (base radius), Lemma G, Claim 8.
Used from P6a (unrefereed): Lemma 1(ii),(iii) (ψ_t = −(v/ρ) sin φ cos φ; ∂_sρ = cos φ, ∂_sφ = −κ − sin φ/ρ; valid where
ρ > ε and the front is C²), Lemma VC, Lemma C(4).

**What is and is not proved here (summary).** The scale-invariant class "tangent angle κ₁-Lipschitz in the logarithm of
the distance from the far end of the arm" is
 * PROVED exactly, with κ₁ = v/(2(1+v)), for the straight-departure model (Claim 13);
 * PROVED for the real construction C_cut at the entry time **only on scales r ≥ r_1(v) := exp(−1/(4.46 vC_A))**
   (Claim 15), conditional on (A1), (A2) and with the constant expressed through Q_0 (the same quantity at t_0);
   below r_1(v) the proof gives only the power-loss class |r ψ_r| ≤ C r^{−2κ}, κ = 2.23 vC_A;
 * NOT proved without loss on all scales ≥ ε. The exact laws that a lossless proof must use are Claim 14.

## Hypotheses on the path (to be supplied by the bulk theorem)

**(A1) no dawdling at the corner.** There is C_A ≥ 1 with vC_A ≤ 1/100 such that for every leg start t_j of C_cut with
a_j ∈ R = [0, 0.2]: t_j − t_0 ≤ C_A (r_{a_j} + ε), where r_a = |x_a(t_0) − O|, O = P(t_0), t_0 = end of leg 0.
**(A2) entry time.** The first leg start t_{j_1} with a_{j_1} ≥ 2π − 2δ satisfies 16 v (t_{j_1} − t_0) ≤ 0.18.

## Claim 13 (the model arm is exactly log-Lipschitz). PROVED

In the setting of Claim 4 (ray Q_r(0) = r e^{i(π−ω)}, Harry P(s) = s, cos ω > v, ω < π/2), let ψ(r, s) be the tangent
angle of the curve r ↦ Q_r(s). Then for all r, s > 0

  |∂ψ/∂ log r| = (v s/ρ) |sin φ cos φ| ≤ v/(2(1 + v)),

and if κ is the curvature of the curve r ↦ Q_r(s) and L(r) its arclength from the end r = 0, then
κ L ≤ C_L v/(2(1+v)) with C_L := (c_1 + A/(1 − v'))/c_2 + A/((1 − v')A_2), v' = v/(1+v),
c_1 = [1 + (1−v²)/(cos ω − v) + (1+v)(cos ω − v)]/(1 − v²), c_2 = (v + cos ω)(cos ω − v)/(1 − v²),
A as in Claim 4, A_2 = [g(π−ω)(cos ω − v)/(cos ω − v + 1 − v²)]^{1/(1+v)}.

*Proof.* The dynamics and the initial ray are invariant under (x, t) ↦ (cx, ct), so Q_{cr}(cs) = c Q_r(s); hence
∂_r Q_r(s) depends only on s/r, ψ(r, s) = Ψ(s/r), and r ψ_r = −s ψ_s. The tangent vector ∂_r Q_r solves the variational
equation ∂_s(∂_rQ) = (v/ρ)(I − r̂r̂ᵀ)∂_rQ, whose rotation rate is ψ_s = ∓(v/ρ) sin φ cos φ. In the proof of Claim 4(d),
ρ ≥ (1+v)s. For the second statement, κ = |ψ_r|/|∂_rQ_r| and L(r) = ∫_0^r |∂_rQ_{r1}| dr1. By Claim 4(b),(d) and its
consequence (ii): |∂_rQ_{r1}| ≤ c_1 + A (s/r1)^{v'} (using A ≤ 1, so ρ sin²β/r1 ≤ 1 + (1−v²)/(cos ω − v)), hence
L(r) ≤ r[c_1 + A λ^{v'}/(1 − v')], λ = s/r; and |∂_rQ_r| ≥ max(ρ_r, λ sin β) ≥ max(c_2, A_2 λ^{v'} 1_{λ≥1}). Divide. ∎

(For the tip, ω = 2 arcsin v and small v: c_1 ≈ 3, c_2 ≈ 1, A/A_2 ≈ 2, so κL ≲ 3.6 v.)

## Claim 14 (exact laws for the log-derivative of the tangent angle). PROVED

Let r be any C¹ label of an arc of the front with ρ > ε, C² in the label, w := |∂_r x|, Q := r ∂_rψ (= r w κ),
β the bearing from Harry, φ = β − ψ. Then
(a) Q_t = (v/ρ) cos 2φ · Q + (v r w/ρ²) sin φ (3cos²φ − 1);
(b) φ_t = β_t + (v/ρ) sin φ cos φ, with |β_t| ≤ |P_t|/ρ;
(c) where sin 2φ ≠ 0, Z := Q/sin 2φ satisfies Z_t = (v r w/ρ²)(3cos²φ − 1)/(2 cos φ) − 2 Z cot 2φ · β_t.
In particular the homogeneous amplification of Q is exactly the factor sin 2φ(t)/sin 2φ(t1), up to exp(∫ 2|cot 2φ β_t|):
Q is amplified while the tangent is nearly radial and *damped* once it has turned past π/4.

*Proof.* (a) ψ_t = −(v/2ρ) sin 2φ; ∂_s of the right side is (v/ρ) cos 2φ κ + (v/ρ²) sin φ (3cos²φ − 1) (Lemma 1(iii) of
P6a: ∂_sφ = −κ − sin φ/ρ, ∂_sρ = cos φ); ∂_r = w∂_s commutes with ∂_t, and r w κ = Q. (b) ψ_t as above, and the bearing of
x − P changes only through P (the candidate moves radially): |β_t| ≤ |P_t|/ρ. (c) Z_t = Q_t/sin 2φ − 2 Z cot 2φ φ_t, and
by (a), (b) the terms (v/ρ) cos 2φ Z cancel. ∎

## Claim 15 (the arm of C_cut at the entry time, on scales ≥ r_1(v)). PROVED, conditional on (A1), (A2)

Let b ∈ 𝒜 with r := r_b ≥ 16ε, parametrise 𝒜 by the t_0-radius r (Lemma G3), Q := r ∂_rψ, Q_0 := |Q| at t_0, and
κ := 2.23 vC_A. Then at every time t in a leg with base label ≤ 2π − 2δ, in particular at the entry time t_{j_1}:

  |Q(t)| ≤ 1.24 r^{−κ} Q_0(r) + 31 vC_A r^{−2κ} + 706 v (t − t_0) r^{1−κ}.

Consequently, for r ≥ r_1(v) := exp(−1/(4.46 vC_A)) (so that r^{−2κ} ≤ e):
|Q(t)| ≤ Q̄ := 2.1 sup Q_0 + 85 vC_A + 1200 v (t − t_0) r (by (A2) the last term is ≤ 13.5 r ≤ 1.4, and it is
negligible for tiny v or small r), and for two arm labels with t_0-radii r ≤ r' ≤ 1.125 r (r ≥ r_1(v), r ≥ 16ε):

  E(r, r'; t) ≤ ½ l_t(r, r') (Q̄ log(r'/r))² ≤ ½ l_t(r, r') (Q̄ (r' − r)/r)².

*Proof.* Arm points with r ≥ 16ε have ρ ≥ 0.45 r > ε during the departure and ρ ≥ 0.065 afterwards (Claim 8), and they are
true candidates that were never in the ε-disc, so the front is C^∞ there and Claim 14(a) applies:
|Q_t| ≤ (v/ρ)|Q| + 2 v r w/ρ². *Departure (base in R).* By Claim 8: exp(∫ v/ρ) ≤ 1.035 (1 + D/r)^κ ≤ 1.035 r^{−κ}
(r + D < 1), w ≤ 1.0021 · 1.035 (1 + D/r)^κ ≤ 1.04 r^{−κ}, ρ ≥ 0.45(r + D), and ∫ ds/(r + D(s))² ≤ 2.4 C_A/r
(layer cake as in Claim 10). So ∫ 2 v r w ρ^{-2} ds ≤ 2v r · 1.04 r^{−κ} · 2.4 C_A/(0.2025 r) ≤ 24.7 vC_A r^{−κ}, and
|Q| ≤ 1.035 r^{−κ}[Q_0 + 24.7 vC_A r^{−κ}]. *Base in B.* ρ ≥ 0.065, w ≤ 1.04 r^{−κ} e^{0.18} ≤ 1.25 r^{−κ}:
|Q_t| ≤ 15.4 v |Q| + 592 v r^{1−κ}; with (A2), e^{15.4 v Δt} ≤ 1.19. Combine: 1.19 · 1.035 ≤ 1.24, 1.24 · 24.7 ≤ 31,
1.19 · 592 ≤ 706. For the excess: the tangent angle varies by ≤ Q̄ log(r'/r) between the two labels, the chord
direction lies in the cone spanned by the tangents, and E = ∫(1 − T·e) ds ≤ l (1 − cos(osc ψ)) ≤ l (osc ψ)²/2. ∎

*Remarks.* (1) Q_0 is a property of the explicit front of Lemma G; an analytic bound is not derived here (numerically
sup Q_0 ≤ 0.1 on 𝒜, attained at the outer end, and Q_0 = O(r)). (2) In terms of the current arclength L from the far
end: L(r) ≤ ∫_0^r w ≤ 1.04 r^{1−κ}/(1 − κ), and L(r) ≥ r − r_{b_e} (with r_{b_e} ≤ 1.6ε by the argument of Claim 1(f); not re-derived for the shifted t_0); so for r ≥ r_1(v), 0.9 r ≤ L ≤ 1.8 r, and Claim 15 reads
E ≤ 1.7 Q̄² λ³/L² for pairs of current length λ ≤ L/16 at distance L ≥ 1.8 max(r_1(v), 16ε) from the far end.
(3) Below r_1(v) the same inequality only gives |Q| ≤ C r^{−2κ}: a power loss, which is the crude amplification
exp(∫v/ρ) and is not the truth (Claim 13, Claim 14(c)).
