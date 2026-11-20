# Referee report RQ1-1 on referee/Q1-claims.md (Theorem End*, Corollary End*, Lemmas Q1.L1–L4)

Referee: independent and adversarial. I read Q1-claims.md in full, then paper/sec_E.tex (lem:E-facts, Construction C cut at
b_E, thm:End and its proof, Steps 1–5, (b), (c), cor:End, rem:E-B, rem:E-restart) and paper/sec_B.tex (lem:B-V, B-VC, B-1,
B-2, B-3, B-4, B-C, thm:R and its Claim, thm:Bulk Steps 1–5). I did **not** read reports/Q1-1.md or code/Q1. After the proof
check I read code/Q1/out/optimise.txt **only** for the printed parameter values of the run
"DATA round6 a=1/2" (a′ = 1/2, C0 = 0.86, λ0 = 0.025, c_sep = 0.024, U_max = 6.5).
My code: `code/referee/Q1_1/check.py` (side conditions, 50-digit mpmath, written from §1–§3 of the claims only;
output `check_out.txt`) and `code/referee/Q1_1/lemmas.py` (numerical sanity checks of Lemma 4.2, 4.3, the H-majorant,
chain sums, the Step 4(i) inequality; output `lemmas_out.txt`).

## Verdict summary

| claim | verdict |
|---|---|
| Lemma 4.1 (Duhamel, general ratio) | OK |
| Lemma 4.2 (gap–time integrals) | OK with fix F1 (hypothesis of (ii)) |
| Lemma 4.3 | OK (also checked numerically) |
| Step 0 / continuity argument / (Imp*) closing | OK (strict room: θ < 1 from (P0),(P6); L_J < κ1 from (P7)) |
| Step 1 (a) dichotomy, (b), (c), (d) = (E-star*) | OK (advance ≥ ε/κ1 is a correct tightening) |
| Step 2: tilt lemma with ratio q, C_A, C_B, C_TL, any γ ∈ (0,1) | OK |
| (E-mu*) via lem:E-facts(b) with C_A | OK |
| Step 3 far pairs: distance, c_amp, amplification, far forcing (g > ηR via Lemma 4.2), forcing g ≤ ηR, three terms, (P5) | OK |
| Step 4 near pairs: Term I (D_I), Term II short case (new D_IIs), long case (D_IIl), (P6) | OK |
| Step 5 length: X_far, B_5, I_5 (both γ ≤ 1/2 and γ > 1/2), near increase, (P7) | OK |
| (b), (c), (d), (e) of Theorem End* | OK (remarks R1, R2 on (c), (d) at the optimum) |
| Corollary End* (incl. weakened (C1)–(C3)) | OK |
| Removal of the cap γ ≤ 1/4 | OK (every implicit use located and replaced, list below) |
| Monotonicity in v and U; uniformity in ε | OK |
| Lemma Q1.L1 | OK |
| Lemma Q1.L2 | OK |
| Lemma Q1.L3 | OK with fix F2 (wording of (1)) |
| Lemma Q1.L4 | OK with fix F3 ("iff" → "if") |
| Numerics at the reported optimum (a′,C0,λ0,c_sep,U) = (1/2,0.86,1/40,0.024,6.5) | OK at v = 5.8273751e-5·(1−10⁻⁶), as claimed; at the printed v itself (P7) fails by 2·10⁻⁸ relative, an artefact of the 7–8-digit printout (see §3) |

No GAP and no FALSE claim found.

## 1. Step-by-step comparison with the old proof (sec_E thm:End + quoted sec_B pieces)

**Lemma 4.1** = lem:B-3(e) without inserting 1/4: N_η N_η′ = E′ ≤ αN² + βN with the exact α of lem:B-3(c). Needs only
ρ_m ≥ ε. With ρ_m ≥ K l, α ≤ (1+1/K+2/K²)v/ρ_m. OK.

**Lemma 4.2** replaces (E-1c)/(B-1c) (constants 2ε, 4 → dε, χ = κ1d). (i): for attained gaps g_1 > … > g_n = g_min (one per
leg, spacing ≥ ε/κ1 by Step 1(a), including the first leg j_s+1), h(g_i) ≤ (κ1/ε)∫_{g_i−ε/κ1}^{g_i} h, disjoint intervals in
[g_min,∞); legs (also the current partial one) last ≤ dε. Correct. All applications use h of the form (non-increasing)·1{g ≤ X}
or ·1{g < X}, which is non-increasing: checked for g^{-1}1{g≤min(g(τ),K_RR)}, g^{-2}1{g≤K_RR}, g^{ν+γ−2}1{g≤ηR},
c_6h̄·1{g<K_fλ}, h2·1{g<K_fλ}, H(g/λ)1{g<K_fλ}, g^{2γ−1}1{g≤ηR} (γ ≤ 1/2). (ii): the proof integrates h over
[g_i, g_i+ε/κ1] up to G+ε/κ1, so the hypothesis must be monotonicity on [0, G+ε/κ1] (fix F1); the only application
(h = g^{2γ−1}, γ > 1/2, 𝒯 = final segment {g ≤ ηR}) is increasing on [0,∞), so nothing changes. (iii) correct. Random
schedules (3000 trials) confirm (i)–(iii) (`lemmas.py`).

**Lemma 4.3.** All formulas, z·h1(z) ≤ λ, ∫_0^{Kλ}h1 = λ(2+log K), z h3 = G(z/λ): verified symbolically and by quadrature.

**Step 0 / continuity.** Legs ≤ ε/(1−v) ≤ dε by lem:B-C(2) and (P1); |P−x_{a_j}| ≤ e^{2μ}ε ≤ δ1ε by lem:B-C(4) and (P1);
P ∈ [x_{a_j}, x_{a_{j+1}}]. (CA*) from (S1*) and lem:B-VC(b). Closing: on [t*, t*+δ], l ≤ e^{2vδ/ε}L_Jλ, |E′| ≤ (4v/ε)l,
λ ≥ ε/2, so δ depends on (v, ε, M, γ, κ1, θ, L_J) only; strict room θ < 1 ((P0) f < 1, (P6)) and L_J < κ1 ((P7)). F(t) ⊂ F(t*).
Non-circular: every family bound used at time τ is for τ ≤ t ≤ t* (closed by continuity), and Step 1 is used only at leg
starts ≤ t*. OK.

**Step 1.** (α): pair (a_j, s), λ = ε/2 ≤ R (K_ε ≥ 3/2), in F(t_j) (first point a_j belongs to both the leg-j and leg-(j+1)
families); κ1ε/2 ≤ ε. Non-final: l_{t_j}(a_j,a_{j+1}) = ε by maximality and continuity; (a_j,a_{j+1}) ∈ F(t_j) with λ ∈
[ε/2, ε] ⊂ [ε/2, R]; (J1*) gives advance ≥ ε/κ1 (tightening of the old [ε/2, ε], correct). (β): the new step uses
l_{t_j}(a_{j−1},a_j) ≥ l_{t_{j−1}}(a_{j−1},a_j) = ε (lengths non-decreasing, leg j non-final) instead of ≥ λ_1;
κ1(λ_1+λ_2) − ε < (4/3)(3ε/2) − ε = ε. Pair (a_{j−1}, b_E) has λ ∈ [ε/κ1, 3ε/2) ⊂ [ε/2, R]. OK.
(b): advances of legs j_s+1, …, j+1 (each fixed at its start by (α)) sum to ≤ U, so ≤ κ1U/ε legs, elapsed ≤ χU. OK.
(d) (E-star*): first form from (CA*) for w_s ≥ ε/2, trivial (negative) for w_s < ε/2 since δ1 ≥ 1 > c_A/2; second form:
c_A − 1/c_6 = c_Aδ1/(1+δ1) > 0 and the case split is correct. OK.

**Step 2 (tilt lemma).** One step: lem:B-4(a) with l(J_1) ≤ κ1λ_{J_1}, N(I_1) ≤ M(rλ_{J_1})^{1/2+γ},
E(J_1) ≤ ½M²λ_{J_1}^{1+2γ}, c(J_1) ≥ c_Aλ_{J_1} (λ_{J_1} ≤ R ≤ K_RR), Mλ^γ ≤ m: gives exactly c_t(r). No smallness of m is
used (old: M λ^γ ≤ 0.005). Chain (A) with ratio q: for k < k_1, q^kλ_J < λ_I, so Σ (q^kλ_J)^γ ≤ λ_I^γ Σ_i q^{−iγ} = S_q λ_I^γ
for every γ > 0 (old: S ≤ 1.5714/γ by concavity on [0,1/4] — the first implicit use of γ ≤ 1/4, now removed). (B): arcs
(a′_k, b) start at ≥ a° ∈ {a, a_{j+1}}, family pairs, sum ≤ C_A Mλ(a°,b)^γ ≤ C_A Mλ_I^γ. (C): λ(a_{j+1},b) ≥ λ_J ≥ ε/2,
ratio ≤ 3, c_t(3). Same left end: C_A; same right end: (B)+(C) = C_B; general: C_TL = C_A + C_B (old 2S+1 with
"1 ≤ 0.25/γ" — second implicit use of γ ≤ 1/4, removed). OK.

**(E-mu*).** lem:E-facts(b) with û = e_ab is an identity: ∫_J|T−e_ab|² = N(J)² + c(J)|e_J−e_ab|². All uses are sub-arcs J of
(a,b) with left end a (J_y; (a,s); Ψ_τ; (a, a_{j+1}) in Term II(i)), so C_A (not C_TL) is legitimate; λ_J^{2γ} ≤ λ^{2γ}.
CμA = 1+κ1C_A², C1A = (κ1CμA)^{1/2}. OK.

**Step 3 (far).** g ≥ K_fλ ≥ 3ε/2 > ε ≥ advance ⇒ a > a_{j+1}; far on all of [t_s,t]. ρ_m ≥ ρ_a − l (hull ⊂ B(x_a,l)) with
(E-star*) at s = a: case g ≤ K_RR gives ρ_m ≥ c_A g − (2δ1+κ1)λ ≥ c_ρ g (ε ≤ 2λ, λ ≤ g/K_f); case g > K_RR gives
ρ_m ≥ c_R R (ε ≤ R/K_ε, λ ≤ R). ρ_m ≥ ε from (P2); ρ_m ≥ K_1 l resp. K_2 l. OK.
*Amplification / c_amp:* initial segment g > K_RR of length ≤ χU: a_2vχU/(c_RR); on g ≤ K_RR, Lemma 4.2(i) with g_min = g(t)
≥ K_fλ: (a_1v/c_ρ)[dε/g(t) + χ log(·)] ≤ 2a_1dv/(c_ρK_f) + c_amp v log(·), c_amp = a_1χ/c_ρ (old 1.375·4·4 = 22). With
(P3), (P4) and the ratio ≥ 1 the claim follows; if g(t) > K_RR the ratio is 1. OK.
*Far forcing g > ηR (tightened):* |p_a| ≤ ρ_a ≤ ρ_m + l ≤ ρ_m(1+1/K_i); β ≤ 2vκ1^{3/2}λ^{3/2}(1+1/K_i)/ρ_m². Regime g > K_RR
lasts ≤ χU → B_2U χU/R²; regime ηR < g ≤ K_RR via Lemma 4.2(i), g0 = ηR: ∫g^{-2} ≤ dε/(ηR)² + χ/(ηR) ≤ (d/(K_εη²) + χ/η)/R
→ B_2η/R. Correct (old: 408 v T_B λ^{3/2}/R² over the whole time).
*Forcing g ≤ ηR:* family membership of (a′,a), (a′,b): λ(a′,a) ≥ g − ε ≥ (K_f/2−1)ε ≥ ε/2 (K_f ≥ 3), λ(a′,b) ≤ ηR(1+1/K_f)
≤ R (η ≤ K_f/(K_f+1)); ratio λ(a′,b)/λ(a′,a) ≤ 1+1/(K_f−2) = r_f (λ(a′,a) ≥ (K_f−2)λ) — one step c_t(r_f); same-right-end
tilt C_B(1+1/K_f)^γ; c(a′,a) ≤ κ1 g. C_p, B_3 correct; ρ_m ≥ c_ρg since ηR ≤ K_RR.
*Result:* first term via (S2*) (g_s = u_a): (min(min(g_s,K_RR),K_fλ)/g_2)^ν ≤ 1; if g_2 > K_RR ratio 1. Second term:
(K_RR/ĝ_2)^ν ≤ max(1,K_R/K_f)^ν(R/λ)^ν, λ^{3/2}(R/λ)^ν ≤ λ^{1/2+γ}R^{1−γ} (needs γ+ν ≤ 1), R^{−γ} = M/m. Third term: Lemma
4.2(i) with h = g^{ν+γ−2}, ∫_{g_2}^∞ g^{ν+γ−2} = g_2^{ν+γ−1}/(1−γ−ν) (needs γ+ν < 1, (P0)); g_2^{γ−1} ≤ (K_fλ)^{γ−1} (γ < 1;
old: 64^{−3/4} and 1−γ−ν ≥ 0.74 — implicit uses of γ ≤ 1/4, removed). (P5) is exactly the sum. OK.

**Step 4 (near).** Starting value ½f²M²λ^{1+2γ} (Step 3 at the switching time in the leg-j family; or (S2*) with s0 ≤ f).
*Term I:* a*-layer-cake identity correct. For y ≥ ε, (y+δ1ε)/c_A ≤ c_6y; if (y+δ1ε)/c_A ≤ K_RR, {ρ_s < y} ⊂ J_y (also for
w_s < ε/2, trivially); otherwise c_6y > K_RR ≥ λ and ω ≤ N² ≤ CμA M²λ^{2γ}λ. Piece ω(ε)/ε ≠ 0 only if g < c_6ε (uses
c_6ε ≤ K_RR, from (P2) and (S3*)). Piece ∫: substitution z = c_6y gives c_6h1(c_6ρ̄), c_6ρ̄ ≥ z(g) = max(c_6ε, min(g,K_Rλ)).
Time integral: ≤ (κ1c_6+1) legs with g < c_6ε (Lemma 4.2(iii)) → d(κ1c_6+1)λ; Lemma 4.2(i) → dλ + c_6χλΨ (Ψ correct in both
cases K_f ≤ K_R and K_f > K_R, h1(K_Rλ) = 1/K_R). τ_I, D_I correct.
*Term II, short case (K_f+1)λ ≤ R — the new D_IIs derivation:* w_s < (K_f+1)λ ≤ R ≤ K_RR so D(s) ≥ max(w_s/c_6, ε).
p(s) = (x_s−x_a)×e + p_a, |(x_s−x_a)×e| ≤ C1A Mλ^γ max(σ_s,ε/2) (sub-arc from a, enlarged inside (a,b)); |p_a| ≤ max over
a′ ∈ {a_j,a_{j+1}} (|·×e| convex along the segment).
(i) g = 0: a_{j+1} ≤ b: (a,a_{j+1}) is a family pair (advance ∈ [ε/κ1, ε]), bound C1A Mλ^γε; a_{j+1} > b: I_0 = (a_j,a_{j+1})
⊃ (a,b) same left end, |e_{I_0}×e_ab| ≤ |e_{I_0}−e_ab| ≤ C_A Mε^γ, ε^γ ≤ 2^γλ^γ: k_0 correct.
g > 0 (g ≥ ε/κ1): g′ ≥ ε/2: pairs (a′,a), (a′,b) in family (λ(a′,b) < (K_f+1)λ ≤ R), C_A + C_B = C_TL, c(a′,a) ≤ κ1g′ ≤ κ1g.
0 < g′ < ε/2: J_0 ⊂ (a′,b) is a family pair (u_b − u_{a′} > λ ≥ ε/2), Cauchy–Schwarz on (a′,a) ⊂ J_0 plus lem:E-facts(b),
(ε/2)^{2γ} ≤ (g+λ)^{2γ}, ε ≤ κ1g, and (κ1^{1/2}/2)(1+κ1C_TL²)^{1/2} ≤ C_TL ⇔ κ1 ≤ C_TL²(4−κ1²), true since C_TL ≥ c_t(3) ≥ √3
and κ1 ≤ 4/3 (checked). So |p_a| ≤ κ1C_TL M(g+λ)^γ g. Correct.
(ii) max(σ_s, ε/2) ≤ c_6D; φ_1, φ_2 = φ_1² as layer-cake integrals; Fubini; Ψ_τ(y) = 0 for y ≤ g and ≤ C1A Mλ^γ min(λ,y) for
y ≥ ε/2. II_α ≤ v c_6²C1A²M²λ^{2γ}h1(max(c_6ε,g)); II_β(g=0) ≤ 2c_6C1Ak_0 vM²λ^{2γ}; II_β(g>0) ≤ 2c_6²κ1C_TL C1A
vM²λ^{2γ}(1+x)^γG(x). H majorant: (1+x)^γ/x is decreasing for every γ < 1 (derivative ∝ γx − 1 − x < 0), H continuous at 1,
H(0) = 2^γ (old: 2^{1/4} — implicit γ ≤ 1/4, removed). ∫_0^{K_f}H ≤ 2^γ[3/4 + (K_f^γ−1)/(2γ)] via (1+x)^γ ≤ (2x)^γ on [1,K_f];
(K_f^γ−1)/γ is finite for every γ > 0 (no uniformity in γ → 0 is claimed). Time integrals: τ_α (dε h1(c_6ε) ≤ dλ/c_6),
g = 0 one leg ≤ 2dλ, g > 0 with g0 ∈ (0, ε/κ1]. D_IIs = c_6²C1A²τ_α + 2c_6²κ1C_TLC1Aτ_β + 4dc_6C1Ak_0 is exactly what the
written derivation gives. Checked numerically (H) in `lemmas.py`.
*Long case:* |q| ≤ 1/D, 1/D ≤ φ_1(w_s) for w_s ≤ K_RR and ≤ c_6/(K_RR) otherwise (both majorants summed — fine);
∫|τ| ≤ κ1^{1/2}Mλ^{1+γ}; indicator vanishes unless K_f+1 > K_R (ι); near duration ≤ τ_nλ; Mλ^γ > m(K_f+1)^{−γ}.
D_IIl correct. (P6) closes with θ. OK.

**Step 5 (length).** g > ηR: (log l)′ ≤ v/ρ_m, X_far correct (Lemma 4.2(i), ∫ dt/g ≤ d/(K_εη) + χlog(K_R/η)).
g ≤ ηR: lem:B-3(c) divided by l, N²/l ≤ M²(g/K_f)^{2γ} (l ≥ λ), l^{1/2}N ≤ κ1^{1/2}M(g/K_f)^{1+γ}: B_5 correct. γ ≤ 1/2:
h = g^{2γ−1} non-increasing, g_min ≥ K_fε/2; γ > 1/2: Lemma 4.2(ii) on the final segment {g ≤ ηR} with G = ηR (old: only
γ ≤ 1/2 handled, via 2ε(32ε)^{2γ−1} — implicit cap, removed). Both ≤ I_5R^{2γ} (the max(1,·) in I_5 is a harmless
over-estimate). Near: m̃(y) ≤ l(J_y) ≤ κ1min(λ,c_6y); increase ≤ vκ1τ_Iλ (additive, independent of l). Far phase precedes
near phase ⇒ l ≤ L_Jλ. (P7) closes. OK.

**(b)** Count ≤ κ1U/ε, T_stop ≤ t_s + κ1U/(1−v), seen-ness via lem:B-C(3) for the cut construction. OK.
**(c)** (F_b): E ≤ ½M²λ^{1+2γ} ≤ ½m²l(l/R)^{2γ}, c_0 + c_1 = m²/2 ≤ 1/4 by (Pc). (S): l > R ⇒ λ > R/κ1 ⇒ (E-star*)
ρ_s ≥ c_AR/κ1 − δ1R/K_ε = r_1 ∈ (0,1]. K̃ by the Claim of thm:R with L_s = κ1U; the covering of [a_j, b_E] by leg-(j+1)
family pairs is correct (merged last piece < 3ε/2 ≤ R). OK.
**(d)**, **(e)** = Steps 2, 1(d). OK.

**Places where the old proof used γ ≤ 1/4 (implicitly) and how End* handles them:** S ≤ 1.5714/γ (concavity on [0,1/4]) →
exact S_q; 3^{1/2+γ} ≤ 3^{3/4} → c_t(r); "1 ≤ 0.25/γ" in C_TL → C_A + C_B; 1−γ−ν ≥ 0.74 and 64^{−3/4} → 1/(1−γ−ν), K_f^{γ−1};
2^{1/4} in Term II and k_0 → 2^γ; 65^{2γ} → (K_f+1)^γ; Step 5 monotonicity of g^{2γ−1} (needs γ ≤ 1/2) → Lemma 4.2(ii);
ν ≤ γ in cor:End → (C5); old smallness Mλ^γ ≤ 0.005, ϑ ≤ 2 → not needed. Also thm:R needs γ ≤ 1: holds (γ < 1). No
remaining hidden use found.

**Corollary End*.** (S2*): C0λ^{a′} ≤ s0m min(1,K_f/K_R)^ν (λ/R)^{γ+ν} by (C6),(C5), λ ≤ R; and
min(1,K_f/K_R)(λ/R) ≤ min(1,(K_f/K_R)(λ/R)) ≤ min(1, K_fλ/min(u_a,K_RR)). (S1*): φ(λ) = λ − ½C0²λ^{1+2a′} is concave; the
three ranges with (C2), (C3), (C4) are correct, including K_RR ≥ λ0 (then (C3) is void and (C2) covers λ ≤ λ0). (C0) is not
actually needed. Monotonicity: v and U enter (P1)–(P7) only increasingly; (P2), (Pc), (C*) do not involve v or U (R is a
parameter). Uniformity in ε: ε enters only via (S3*). OK.

## 2. Lemmas Q1.L1–L4

- **L1** OK. I re-traced every invocation of (CA*): one-step tilts (Step 2 chains, Step 3 forcing, Term II(i) incl. I_0),
  and (E-star*) at labels s ∈ [a,b] with base a_{j(τ)} (Step 3 at s = a, Term I, Term II, Step 5), plus (a_j,s),
  s ∈ (a_{j+1}, b_E] in (c). No other use.
- **L2** OK (list of used pairs complete; the enlargement to [a_j, max(b,a_{j+1})] is needed exactly for I_0).
- **L3** OK; fix F2: in (1) "only through" should read "directly only through …; other start data enter only via the family
  bounds and (CA*) of the used pairs (L1, L2)". (2) is correct: Lemma 4.1 and the amplification claim on [t_w,t]; the first
  term with g_w in place of g_s; forcing integrals over subsets; Step 5 with (1+δ).
- **L4** OK with fix F3: "admissible iff (P7_δ)" → "admissible if (P7_δ)" (only sufficiency is proved). Note: at the reported
  optimum itself the admissible δ_tail is < 2.3·10⁻⁸ (optimise.txt line 16); δ_tail = 2·10⁻⁵ needs the separate runs.
  The "few per cent" cost claim refers to reports/Q1-1.md, which I did not read; not refereed.

## 3. Numerics at the reported optimum (independent code)

Free parameters as printed (8 digits): γ = 0.49969322, m = 0.15404426, s0 = 0.14974996, κ1 = 1.021961, c_A = 0.9914861,
K_R = 31.998834, K_f = 5.0653198, K_ε = 998.43371, η = 0.36162923, q = 2.3008062; v = 5.8273751e-5. I recomputed every
derived constant from §1 and set the dependent ones with equality: d = 1/(1−v), δ1 = e^{2v/(1−v)}, ν = c_amp v, A0 from (P4),
f from (P5), R = min of the (C6), (C4), (C1) bounds.

- All derived constants agree with the printed ones to all printed digits (C_A = 7.114586, C_B = 10.25004, C_TL = 17.36463,
  c_6 = 2.017292, c_ρ = 0.3948418, c_R = 30.70344, c_amp = 5.262752, C1A = 7.340771, CμA = 52.72894, C_p = 12.92317,
  B_3 = 433.7915, B_5 = 5501.995, I_5 = 0.3720804, D_I = 607.9761, D_IIs = 7592.576, D_IIl = 993.3139, R = 7.186817e-4,
  A0 = 1.018453, f = 0.2103450, L_J = 1.021961).
- At v·(1 − 10⁻⁶) (the point at which the author states verification): **all** of (P0)–(P7), (Pc), (C0)–(C6) hold. Slacks:
  (P2) c_ρK_f ≥ 2: 2.6e-8; (P6): 2.15e-6; (P7): 1.9e-9; (C2): 9.7e-6; (C5): 2.0e-7; (C6): equality by choice of R.
- At the printed v itself, (P7) fails by 2·10⁻⁸ relative. Cause: κ1 is printed to 7 digits and (P7) has relative slack 2.3e-8
  in the author's full-precision run. Bisection at the printed digits gives v_max = 5.82737e-5 (binding (P7)), i.e. the
  reported value to 6 digits. Not an error of the claim; recommendation: print the free parameters to ≥ 20 digits.
- All conditions hold on a 40-point grid of v ∈ (0, v_max] (consistent with the monotonicity claim).

## 4. Remarks (not errors)

- **R1 (conclusion (c) at the optimum).** K̃ ≤ 16δ1 + 2m²(1+1/γ) + 2δ1κ1U/r_1 = 1.909·10⁴ and μK̃ ≈ 1.11 > 1, so thm:R
  cannot be invoked with these parameter values. (c) only claims the bounds, so it is correct; a downstream user wanting
  thm:R must add μK* < 1 as a further side condition.
- **R2 (conclusion (d) at the optimum).** C_TL m = 2.675 > 2, so (d) is vacuous at scale λ_I = R and informative only for
  λ_I/R < (2/2.675)^{1/γ} ≈ 0.56. The proof of End* never needs small tilts, but any consumer that does (e.g. the old
  "0.33" of thm:End(d)) must impose a cap such as C_TL m ≤ 0.33 (optimise.txt contains such runs; not refereed here).
- **R3.** The binding conditions at this optimum are (P2) c_ρK_f ≥ 2, (P6), (P7), (C2), (C5), (C6), not (P6) alone.

## 5. Fixes (exact text)

- **F1** (Lemma 4.2(ii)): replace "If h ≥ 0 is non-decreasing on [0, G]" by "If h ≥ 0 is non-decreasing on [0, G + ε/κ1]".
- **F2** (Lemma Q1.L3(1)): replace "data at t_s enter the proof of (Imp*) for that pair only through" by "data at t_s enter
  the proof of (Imp*) for that pair directly only through", and append "(all other start data enter only through the
  family bounds and (CA*) of the used pairs listed in Lemmas Q1.L1, Q1.L2)".
- **F3** (Lemma Q1.L4): replace "is admissible iff (P7_δ) holds" by "is admissible if (P7_δ) holds".
