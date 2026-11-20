# P6a2 — additional claims (round 6c), for independent referees

Stream P6a. This file supplements `referee/P6a-claims.md` (notation, Lemmas V, VC, 1–4, C, Theorems R, B there; Theorem B
is under review and is used here as a black box, statement only). It also uses, as EXTERNAL inputs not checked by me,
Lemma G and Claim 8 of `referee/P6c-claims.md` (construction C_cut, θ₀ = 0.1, label sets R = [0, 2θ₀],
B = [2θ₀, 2π − 2θ₀], 𝒜 = [2π − θ₀, b_e], O = P(t₀), r_a := |x_a(t₀) − O|, K_arm, hypothesis (A1), standing assumptions
v ≤ 1/100, ε ≤ 10⁻³). Theorems R and B hold verbatim for C_cut (their proofs use the last label only as the end of
the arc; in Theorem B only the arc from the base to b* ≤ b_e occurs).

Claimed PROVED here: Corollary N (no-dawdling = P6c's (A1), from Theorem B) and Theorem F (assembled conditional
theorem). **Not proved: the goal.** Remaining hypotheses are listed in Theorem F: (ST⁺) and (FS). The requested
"Theorem B′" (a self-similar copy of Theorem B on the left-behind arm) is NOT proved and, in the form requested,
I believe it is false for a fixed-constant class; see `reports/P6a-1.md`, Round 6c, for the mechanism and numerics.

---------------------------------------------------------------------------------------------------------------------

## Corollary N (no-dawdling)

Assume the hypotheses of Theorem B at the leg start t_s = t_{j_s} (labels u ∈ [0, U], constants κ, R; v ≤ 10⁻¹²,
v(4U + 2) ≤ 10⁻⁶R), and in addition, for some m ≥ 1 with 2vm ≤ 1:
   t_s − t₀ ≤ mε  and  r_{a_{j_s}} ≤ mε.
Put K := max(2, U/(16R)) and C_A := 2.01K(m + 1) + m. Then for every leg start t_j with j ≥ j_s and u_{a_j} ≤ U − ε/2,
and trivially for every j ≤ j_s:
   t_j − t₀ ≤ C_A (r_{a_j} + ε).
In particular, if the arc [a_{j_s}, b*] contains R ∪ [2θ₀, 2θ₀ + ε] (labels of the paper), hypothesis (A1) of P6c's Claim 8
holds with this C_A (and vC_A ≤ 1/100 whenever v ≤ 1/(100C_A)).

*Proof.* For j ≤ j_s: t_j − t₀ ≤ t_s − t₀ ≤ mε ≤ C_Aε. Let j > j_s, u := u_{a_j} ≤ U − ε/2.
(i) Every leg i+1 with j_s ≤ i < j advances the base label by ≥ ε/2: u_{a_i} + ε/2 ≤ U, so the pair (a_i, s) with
u_s = u_{a_i} + ε/2 belongs to the family 𝔉(t_i) of Theorem B, and (I1) gives l_{t_i}(a_i, s) ≤ ε; by the maximality in the
definition of a_{i+1}, a_{i+1} ≥ s. Hence j − j_s ≤ 2u/ε, and since a leg lasts ≤ ε/(1 − v): t_j − t_s ≤ 2u/(1 − v) ≤ 2.01u.
(ii) u ≤ K·c(a_{j_s}, a_j; t_s): if u ≤ 32R this is (CA) of Theorem B (c ≥ u/2); if u > 32R, (IC2) gives
c ≥ 16R ≥ 16R·u/U.
(iii) Every virtual candidate has speed ≤ v, so c(a_{j_s}, a_j; t_s) ≤ c(a_{j_s}, a_j; t₀) + 2v(t_s − t₀)
≤ r_{a_j} + r_{a_{j_s}} + 2vmε ≤ r_{a_j} + (m + 1)ε.
Therefore t_j − t₀ ≤ mε + 2.01K(r_{a_j} + (m + 1)ε) ≤ C_A(r_{a_j} + ε). ∎

## Theorem F (assembled conditional theorem)

Setting: construction C_cut; constants κ, R, m, L_s, K_A; v ≤ v_F, ε ≤ ε_F := min(10⁻³, R/64).
**Hypotheses.**
* **(ST⁺) start.** There is a leg start t_s = t_{j_s} with t_s − t₀ ≤ mε, r_{a_{j_s}} ≤ mε, a_{j_s} ≤ 2θ₀, remaining length
  R_{j_s} := l_{t_s}(a_{j_s}, b_e) ≤ L_s, at which (ST) of Theorem B holds on the arc [a_{j_s}, 2π − θ₀/2] with constants κ, R.
* **(FS) final stretch.** For every leg j+1 > j_s with base label a_j > 2π − 2θ₀ and every t in it:
  K̃(t) := ∫_{a_{j+1}}^{b_e} T·AT ds ≤ K_A.
* **External:** Lemma G and Claim 8 of `referee/P6c-claims.md`.
Let K := max(2, L_s/(16R)), C_A := 2.01K(m + 1) + m, K_T := 50 + 5.3C_A², K_I := 32 + 1/1960 + 32L_s/R + K_T,
K* := max(K_I, K_A), and
   v_F := min(10⁻¹², 10⁻⁶R/(4L_s + 2), 1/(100C_A), 1/(2K*), 1/(2m)).
**Conclusion.** For v ≤ v_F and ε ≤ ε_F, C_cut stops by time t_s + 2.1L_s ≤ 1.02 + mε + 2.1L_s and every direction is seen.
If the hypotheses hold with the same constants along a sequence ε → 0, every direction is caught exactly by a path of
speed ≤ 1 (Lemma A4.1 of the paper).

*Proof.* U := l_{t_s}(a_{j_s}, 2π − θ₀/2) ≤ L_s, so Theorem B applies with b* = 2π − θ₀/2. Since |∂_θx| ≥ 1, the label
b' := 2π − θ₀ has u_{b'} ≤ U − θ₀/2 ≤ U − ε/2; hence (F_b), (S) of Theorem R hold with b' in the place of b*
(γ = 1/4, r₀ = R, c₀ = 1/39200, c₁ = 0, r₁ = R/8) for every leg j+1 > j_s with a_{j+1} < b'.
Corollary N gives (A1) with the constant C_A (all a_j ∈ R have u_{a_j} ≤ U − ε/2; legs before j_s are covered by
t_j − t₀ ≤ mε; vC_A ≤ 1/100). So Claim 8 of P6c applies: for every t ≥ t₀ in a leg with a_j ≤ 2π − 2θ₀,
K_tip(t) ≤ K_arm(t) ≤ max(50 + 5.3C_A², 2.4e^{16v(t − t₀)}), where K_tip is taken with b* = b' (the labels > b' lie in 𝒜).
Let j₁ be the first leg index (if any) at which the conclusion "t_j ≤ t_s + 2.1L_s" fails; for legs before it,
16v(t − t₀) ≤ 16v(2.1L_s + 1) < 10⁻⁵, so K_tip ≤ K_T. Now run the proof of Theorem R from leg j_s: its *Claim*
(R_j ≤ L_s ⇒ K̃ ≤ K* on leg j+1) holds for legs with a_j ≤ 2π − 2θ₀ by (F_b), (S) and K_tip ≤ K_T (if a_{j+1} ≥ b' the
bulk part is empty), with 16e^{2μ} + 20c₀ + 2e^{2μ}L_s·8/R + K_T ≤ K_I; and for legs with a_j > 2π − 2θ₀ by (FS). The
*Induction* of that proof then gives R_{j+1} ≤ R_j − ε(1 − μK*) with μK* ≤ 0.51, at most L_s/(0.49ε) further legs, each
of duration ≤ ε/(1 − v): every leg start satisfies t_j ≤ t_s + 2.1L_s, so j₁ does not exist, and the construction
stops. Seeing: Lemma C(3) and P6c's G0 (labels beyond b_e). t₀ ≤ 1/(1 − v). ∎

**Remarks.** (1) By Claim 9 of P6c, (FS) follows from flatness relative to the remaining length, (F_a), with
K_A = 16e^{2μ} + 4c₀(1 + 1/γ) + 2c₁; but (F_a) with ε-independent c₀ is probably false as ε → 0 at fixed v (report,
Round 6c), whereas (FS) only needs the integrated quantity K̃. (2) If (FS) is only available down to remaining length
Mε, a last-blob lemma (P6c's Claim 5) is needed in addition; that hand-off is not written here.
