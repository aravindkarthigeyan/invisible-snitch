# Referee report RP7-2 — `referee/P7-claims.md` (version 1), second referee

Independent, adversarial. I did not read `reports/referee-RP7-1.md`, `reports/P7-1.md` or `code/P7/` before the verdict.
Read in full: `referee/P7-claims.md`, `paper/sec_B.tex` ([B]; assumed correct, hypotheses of every citation checked).
Code: `code/referee/P7_2/` (`constants.py`, `straight_exact.py`, `p7d_front.py`, `p7b_end.py`). Numerical results in §7.

## 0. Verdict

| Claim | Verdict |
|---|---|
| Facts 0.1–0.3 | **OK** |
| Theorem P7.B (a)–(d) | **OK** (all constants recomputed; three editorial fixes, F1–F3) |
| Corollary P7.E | **OK**; wasteful in γ (fix F4, optional), one fix to the *Remark* on restarts (F5, F6) |
| Lemma P7.A (passive far phase) | **OK** |
| Theorem P7.D (i)–(v) | **OK with fixes** (F7: "M₀ ≤ ϑ₀ without loss" is an assumption, not w.l.o.g.; F8: A_s vs. its majorant) |
| Proposition P7.D′ | **OK with fix** (F9: the "γ" of the consequence is not the γ of (D1); statement is about chord tilts, not N) |
| Lemma P7.H | **OK with fix** (F10: causality sentence — the first pass is not run to its end) |
| Corollary P7.T | **OK with fixes** (F10, F11: a′ = γ₁ − 7v is v-dependent and can be 0 under the stated hypotheses; F12: ρ₀ ≤ (1+v)D is forced) |
| Proposition P7.C | **OK** (identity checked to 1e-38; independent derivation via a second first integral) |

No FALSE statement and no GAP in a proof was found. The items below are (i) exact text fixes and (ii) interface
mismatches, which are not errors of the stated results but restrict how they can be chained. The most important
points for the user of these results:

* **(I-1)** The restart Remark of §2 halves γ and multiplies R by 16^{−1/γ₁} (= 1/65536 for γ₁ = 1/4) *per restart*; v₀
  drops by 4. It may be used O(1) times only. This is an artefact of γ := a′/2; the proof of P7.B supports
  γ = a′ − 22v (loss 22v per restart, R ↦ ≈ 8^{−1/γ₁}R), see §2 (F4, F6).
* **(I-2)** Corollary P7.T produces (E1) only on Γ, an arc of length U_Γ ≤ ρ₀/5 ≤ (1+v)D/5 ≤ R₁·20^{−1/γ₁}/5 next to E
  (≤ R₁/8·10⁵ for γ₁ = 1/4), with C₀ ≥ 2.8vT/ρ₀² + 2.9R₁^{−γ₁}; everything else needed by (ST_end) ((E1) on A∖Γ and
  for pairs straddling the far end of Γ, (E2), and the transport from t₁ to the second-pass leg start t_s) is not
  produced by any statement of P7. The authors say so ("design-dependent"); I confirm that this is the true extent.
* **(I-3)** The restriction U_Γ + D ≤ R₁·20^{−1/γ₁} **is stated** in Corollary P7.T. It comes from (D2) with ϑ₀ of Lemma
  P7.H. Its U_Γ-part is structural (alignment 1/20 of the arc with the line of departure, used for z_s ≥ u_s(1−1/800)
  and for ρ_m in (v)); its D-part is an artefact of one line of the proof of P7.D(iii) and can be removed (§4, F13).

## 1. REBUILD of the exponent bookkeeping (my own derivation, then comparison)

**Approach (bulk, far pairs).** Lemma 3(e) of [B]: N′ ≤ αN + β with α = 1.375v/ρ_m. For a pair at gap g the hull is at
distance ρ_m ≥ ĝ/4 and the base advances ≥ ε/2 per leg of duration ≤ 2ε, so ∫α dt ≤ 5.5v·4·log(g₁/g₂) + O(v):
the amplification between gaps is the *power* (g₁/g₂)^{ν}, ν = 22v (true value ≈ v: ρ_m ≈ g and dt ≈ dg; the factor 22 =
1.375·4·4 is waste, not ε-dependence). A pair of label length λ is far for 64λ ≤ g ≤ 32R (above 32R the rate is
≤ 5.5v/(32R), giving the factor A₀). Hence data N(t_s) ≤ C₀λ^{1/2+a′} arrive at the near zone with
 N ≤ A₀ C₀ λ^{1/2+a′} (R/2λ)^{ν} ≤ A₀ C₀R^{ν} λ^{1/2+a′−ν}.
So the invariant exponent that can be propagated is **any γ with γ ≤ a′ − ν** (the forcing terms need γ + ν < 1 and
are harmless: far forcing ∝ vC_TL M λ^{3/2}∫g^{ν+γ−2}; near terms ∝ v(C_μ + C_ϑ²)M²λ^{1+2γ}). The price of γ is the tilt
lemma: Σ_k (2^kλ)^γ gives C_TL ≈ 3.14c₁/γ, so C_μ, C_ϑ² ∝ γ^{−2} and the near increment is ΔE ≈ (1.3·10⁸/γ² resp.
4.5·10⁹/γ²)·v·M²λ^{1+2γ}; closing the bootstrap (ΔE ≤ M²λ^{1+2γ}/8) forces **v ≲ γ²/(3.6·10¹⁰)**. I get the same
structure and the same constants as the claims (all of Steps 2–5 recomputed in `constants.py` for
γ ∈ {1/4, 0.2, 0.1, 10⁻², 10⁻³, 10⁻⁶}: every inequality holds; the binding one is ΔE·v ≤ 0.09, which is 0.0896 at
v = 2·10⁻¹¹γ² — essentially tight for this proof, i.e. the constant 2·10⁻¹¹ cannot be raised without redoing Step 4).

*Resulting range.* With start exponent a′: admissible (γ, v) are γ ≤ min(a′ − 22v, 1/4), v ≤ 2·10⁻¹¹γ². The claimed
choice γ = min(a′/2, 1/4) is inside this set (22v ≤ 4.4·10⁻¹⁰γ² ≤ γ ≤ a′ − γ) — **correct, but it gives away a factor 4 in
v** (v ≤ 5·10⁻¹²a′² instead of ≈ 2·10⁻¹¹a′²) and, more importantly, makes the restart lossy (I-1).

**Tangential departure (my derivation from the exact straight-run integrals).** For a straight unit-speed run, with β
the angle between x − P and P′, and ρ ≥ ε:
 C := ρ sin β / tan^v(β/2) and h := ρ(cos β + v) satisfy C′ = 0, h′ = −(1 − v²)
(direct differentiation from ρ′ = v − cos β, ρβ′ = sin β). For a departure (P′ = −û; θ := π − β the angle between
x − P and û; y = ρ sin θ, z = ρ cos θ) the first says y·tan^v(θ/2) = const, and tan(θ/2) = y/(ρ + z), so **exactly**
 y(τ)/y(0) = [ (ρ + z)(τ) / (ρ + z)(0) ]^{v/(1+v)},  z − vρ = z₀ − vρ₀ + (1 − v²)τ.
(Checked against a 30-digit ODE solution: agreement 1e-33, §7.) For small angle, ρ + z ≈ 2(u + (1+v)τ): the
transversal offset of the candidate at arclength u grows exactly like (1 + (1+v)τ/u)^{v/(1+v)}. Differentiating in u
for a profile y₀ = k u^{1+γ}: tilt(u,τ) = k u^γ (1 + (1+v)τ/u)^{v/(1+v)} [1 + γ − vτ/(u+(1+v)τ)], i.e. for u ≪ τ
 tilt ≈ (1 + γ − v/(1+v)) (1+v)^{v/(1+v)} k τ^{v/(1+v)} u^{γ − v/(1+v)}.
So the **true loss of tilt exponent is exactly v/(1+v)**; Proposition P7.D′ (lower bound 0.96(1+(1+v)τ/u)^{v/(1+v)}) is
sharp in the exponent and in the base, and Theorem P7.D's "≤ 7v" is correct with a factor ≈ 7 of waste in the
exponent (4.1 = 2/0.49 from a* ≤ 2/max(ρ,ε) and max(ρ,ε) ≥ 0.49(u+ε+τ); the rest from p = 3/2 and rounding). Numerically
the pairwise quantity μ^{1/2} grows with effective exponent up to ≈ 3.5v for oscillating admissible profiles (§7), so
7v is not far off for pairs; it cannot be replaced by v/(1+v) for μ.

**Transversal departure.** With P′ = n̂ ⊥ ê, start (ρ,β) = (r, π/2): C = r, h₀ = vr, so with θ = π − β, t = tan(θ/2):
 ρ sin θ t^v = r,  (1 − v²)τ/r = v + (cos θ − v) t^{−v}/sin θ.
This is an *independent* closed form of the relation G(θ) = τ/r of P7.C (the difference of the two expressions is
v t^{−v}[t − tan(θ/2)] = 0; confirmed to 1e-38). From it: t^{−1−v} ≈ 2(1+v)τ/r, X·ê = r t^{−v}, X·n̂ → vr/(1−v) − vτ + …,
∂_rX·n̂ → μ, ∂_rX·ê ≈ t^{−v}/(1+v), hence tilt → μ(1+v)t^v = c_v (r/τ)^{v/(1+v)} with
c_v = μ(1+v)^{1/(1+v)}2^{−v/(1+v)}: **agrees with P7.C(iii)**. In arclength of the image (∝ r^{1/(1+v)}) the exponent is v. A
transversally left end has N ≈ c_v λ^{1/2}(λ/τ)^{v}: tilt exponent a′ = v with a *small constant* C₀ ≈ v τ^{−v}; it still
cannot be fed to P7.E (needs a′ ≥ γ + 22v > 22v), so the final Remark of §6 is correct. (It is correct for this proof;
it is not a proof that such ends are bad.)

## 2. Theorem P7.B and Corollary P7.E — line check of what is new, and the END

I re-derived every display of Steps 1–5 and of (b), (c); only the differences to [B] are commented.

* *Citations.* Lemma C(0),(2),(3),(4) of [B] indeed use the final label only as the right end of the arc and the
  path only from the leg start; Lemma VC(c) (virtual ρ ≤ ε ⇒ the **true** candidate has been seen) holds for an
  arbitrary 1-Lipschitz P (if ρ_θ(0) ≤ ε the candidate is seen at time 0, so "ρ_θ(0) = 1 > ε" in its proof is not
  needed). Lemma 3(e) is applied with ρ_m ≥ max(ε, 4l) verified (13.9λ ≥ 4·(9/8)λ). Lemma 4(a) with c ≥ λ/2 from
  (CA). The Claim of Theorem R is used with K_T = 0, b* = b_E, "2π" replaced by b_E in R_j and K̃: its proof only
  uses (F_b), (S), Lemma C(2),(4), Lemma 3(d), Lemma 4(b) and R_j ≤ L_s — all available. c₀ + c₁ = γ²/5000 ≤ 1/4. OK.
* *Step 1(a), the dichotomy (the heart of "an end").* (α) is [B, Step 1(a)] with 9/8. (β) is new and correct: the
  pair (a_{j−1}, b_E) has λ ∈ [ε/2, 3ε/2], belongs to the family of leg j, whose closed time interval contains t_j,
  and (J1) at t_j gives l_{t_j}(a_j,b_E) ≤ λ₁/8 + 9λ₂/8 < 11ε/16. This is the only place where the convention "at a
  switching time both legs count" is indispensable (also used in (c) for R_j and in Lemma P7.H) — see F1.
  The pair (a_{j−1},b_E) is *near with base a = a_{j−1}*; its (J1),(J2) are proved by Steps 4–5 in the cases
  "a = a_j, a′ = a_{j+1} ≤ b" — I checked that nothing there needs an arc beyond b. So **no pair is ever needed
  beyond b_E**: every estimate for (a,b) uses only labels in [a_j, b] and P ∈ [x_{a_j}, x_{a_{j+1}}], a_{j+1} ≤ b_E.
* *"remaining length ≤ ε ⇒ everything seen", for TRUE candidates:* yes. At T_stop = t_J: P = x_{a_J} and
  ρ_θ = c(a_J,θ) ≤ l_{T_stop}(a_J,θ) ≤ ε for θ ∈ [a_J, b_E]; Lemma VC(c) converts this into "the true candidate θ was
  within ε of Harry at some time ≤ T_stop". The same for [a_j,a_{j+1}] at t_j. This part is unconditional (needs
  no (ST_γ)); (ST_γ) is only needed for the leg count and the time bound. Confirmed by simulation with true
  candidates tracked separately (§7).
* *Adversarial ends tried (none breaks the statement).*
  (a) *Curl at scale just above ε/2 at b_E.* Not allowed beyond a turning angle ≲ √12·(M/8)(ε/2)^γ ≤ 0.005(ε/R)^γ:
  a pair of label length ≥ ε/2 containing a turn φ over length s has E ≳ sφ²/24, and (S2) bounds E by
  (M²/128)λ^{1+2γ}. So "tight curl at scale > ε/2" contradicts the hypothesis; the hypothesis is honest about it.
  (b) *Micro-curl below the resolution:* a full curl of length s ≪ ε^{1+2γ}M² at b_E *is* allowed by (S2)/(E1)
  (only pairs with λ ≥ ε/2 are constrained). The proof survives because every use of sub-scale arcs is through an
  enlargement to label length ε/2 and the trivial bound a* ≤ 2/ε (Term I: ω(ε)/ε; (J1): m̃(ε)/ε), and the
  amplification of its excess while far, (g₁/g₂)^{2ν}, is exactly what the weight in (S2) pays for. I found no step
  that uses regularity below ε/2.
  (c) *Wild already-seen labels beyond b_E* (the situation of the second pass of P7.T, whose end E is the base of
  ≈ 2U/ε old legs with their kinks): candidates do not interact, the family has u_b ≤ U, K̃ integrates to b_E
  only. Nothing in the proof looks beyond b_E. **But** the *conclusion* is then only about [a_s,b_E] and K̃ up to
  b_E: any later statement about the stretching of the whole front (e.g. a (T)-type tip bound in Theorem R) must
  treat labels beyond b_E separately. Not an error; state it (F3).
  (d) *A pair straddling the end* (a < b_E < b) is in no family, no invariant is claimed for it, and none is used.
  (e) *U − u_{a_j} just below/above ε/2*, *U < ε/2 at t_s*, *a_{j+1} = b_E reached with advance < ε/2*: all covered
  by (α)/(β); simulation shows final legs with l/ε anywhere in (0,1].
* *ε-dependence.* None in constants. Leg count 2U/ε enters only through times (≤ 2U/(1−v)) and through (B-1c),
  which converts sums over legs into ∫h(g)dg; amplification is a power of a gap ratio, never e^{cv·#legs}; the near
  period is ≤ 264λ. The δ of the continuity argument depends on ε, harmlessly.

**Fixes for §1.**
* **F1.** In the definition of 𝔉(t), replace "(at a switching time both legs count)" by: "at a switching time t_j
  (j > j_s), 𝔉(t_j) is the family of leg j, i.e. pairs with a = a_{j−1} or a ≥ a_j (it contains the family of leg
  j+1)". As written, "both legs count" can be read as the intersection.
* **F2.** In the proof of (c): "split [a_j,b_E] into consecutive family pairs of 𝔉(t_j) … the first starting at a_j":
  add "(pairs with first point in (a_j,a_{j+1}) belong to 𝔉(t_j) by F1; a last piece shorter than ε/2 is merged
  with its predecessor; for j = j_s, R_j = U)".
* **F3.** After the theorem add: "Nothing is claimed about labels > b_E or about pairs with b > b_E. The invariants
  at a time t depend only on P|[0,t]: if P leaves the construction at a leg start t_j, (a), (c), (d) remain valid
  on [t_s, t_j]." (Needed by Lemma P7.H and Corollary P7.T, see F10.)

**Corollary P7.E.** Proof checked: (S2) from C₀R^{a′} ≤ γ/400 and γ + ν ≤ a′; (λ/R)^ν ≤ min(1, 64λ/min(u_a,32R))^ν
because 64λ/min(u_a,32R) ≥ 2λ/R; (S1) from C₀λ₀^{a′} ≤ 1 and c_sep ≥ 16R. OK. "at arclength distance ≤ ε from the
end" = l_{T_stop}(a_J,b_E) ≤ ε. Constants depend on (a′,C₀,λ₀,c_sep,U) only. Implicit hypothesis worth printing: t_s
is a leg start, i.e. **P(t_s) = x_{a_s}(t_s)**, and b_E − a_s < 2π.
* **F4 (optional, recommended).** State the corollary with a free γ: "for every γ ∈ (0, min(a′, 1/4)] and
  v ≤ min(2·10⁻¹¹γ², (a′−γ)/22, 10⁻⁶γR/(4U+2)), with R := min(1, λ₀/32, c_sep/16, (γ/(400C₀))^{1/a′})". The proof
  is verbatim the same (it only uses γ + ν ≤ a′).

**Remark (same-side restart) — interface check.** Verified: for pairs with a ≥ a_j and old label λ ≥ ε/2, they are
in 𝔉(t_j) (F1), λ ≤ λ′ ≤ 9λ/8; c ≥ 4R₁/9 for λ′ > R₁. So (ST_end) holds with (a′,C₀,λ₀,c_sep) = (γ₁, M₁, R₁, 4R₁/9),
C₀λ₀^{a′} = γ₁/50 ≤ 1. Mismatches:
* **F5.** Edge case: if U − u_{a_j} < ε/2 a pair with λ′ ≥ ε/2 cannot be enlarged "inside [a_j,b_E]". Then use
  (a_{j−1},b_E) ⊃ (a,b) and Fact 0.1: N ≤ M₁(3ε/2)^{1/2+γ₁} ≤ 3^{3/4}M₁λ′^{1/2+γ₁}; or simply add "assume
  U − u_{a_j} ≥ ε/2 (otherwise leg j+1 is final by Step 1(β))".
* **F6.** The title says "Theorem P7.B / Theorem B". From [B, Theorem B] *verbatim* one only has (I1) l ≤ 2λ, so
  λ′ ≤ 2λ and c_sep = R/4 (not 4R/9), C₀ = R^{−1/4}/140, a′ = 1/4, and only on arcs/legs with u_{a_{j+1}} ≤ U. Say so.
  And state the cost explicitly: "the restarted theorem has γ = γ₁/2, R = 16^{−1/γ₁}R₁, v₀ ∝ γ₁²/4; the Remark must
  not be iterated a number of times that grows as ε → 0" (with F4: γ = γ₁ − 22v and R ≈ (8γ₁/γ)^{−1/γ₁}R₁; still
  O(1) restarts only — R degrades geometrically per restart for a reason that is not an artefact of F4: (S2)
  asks for the constant M/8 where the output has M).

## 3. Lemma P7.A — OK

(i) T·AT ≤ a*(ρ) = 1/ρ ≤ 1/ρ₀ on Γ (ρ ≥ dist(P,conv Γ) ≥ ρ₀ ≥ ε). (ii) Lemma 3(e) with ρ_m ≥ ρ₀ ≥ 4l_t(Γ) ≥ 4l;
|p_a| ≤ ρ_a ≤ ρ_m + l ≤ 1.25ρ_m. The E-form follows. No ε-dependence beyond ρ₀ ≥ ε. Note for users: for
ε-uniformity ρ₀ must not shrink with ε; the hypothesis l_{t′}(Γ)e^{Λ} ≤ ρ₀/4 then limits Γ to length ≤ ρ₀/4.

## 4. Theorem P7.D, Proposition P7.D′ — OK with fixes

Checked every line: (i); z_s(t_E) ≥ u_s − ū_s/800; (4.1) (2/0.49 = 4.082); (4.2); (4.3) (f/ρ ≤ a*); (4.4)
(0.49^{−2} = 4.165); (α), (β) (the dyadic bracket equals 1/(2^q−1) − 2^{−Kq}(1/(2^q−1) − 1) ≤ 1/(1 − 2η ln 2));
(ii) (1.0005 + 4.2·10⁻⁵ ≤ 1.01); (iii) (6.04, 106, 1.42, 0.0216, 8.5, 4.21, 4.3 all recomputed); (iv) (1.01·65^{1/4} =
2.868); (v) (1.012, 1.02, 2.03, 4.4, 5.61, 0.2 recomputed; Lemma 3(e) hypothesis ρ_m ≥ 0.99(g+τ′) ≥ max(ε,4l) holds).
No hidden ε: the dyadic sum has ≈ log₂(λ/ε) terms but is geometric; (1+τ/λ)^{7v} with λ ≥ ε/2 is ε-dependent *as a
constant*, and is correctly reported as an exponent loss (λ+τ)^{7v}λ^{−7v}.

* **F7.** Final sentence: "(M₀ ≤ ϑ₀ without loss)" is not w.l.o.g.: (D1) gives N(t_E) ≤ ϑ₀λ^{1/2}u_b^γ, which for far
  pairs is weaker than M₀λ^{1/2+γ}, and ϑ₀ cannot be enlarged freely because of (D2). Replace by "and M₀ ≤ 2.8ϑ₀"
  (then M₀ + 0.2vϑ₀ ≤ 2.9ϑ₀). In Lemma P7.H, M₁ ≤ ϑ₀ = 48M₁/γ₁ holds, so nothing downstream changes.
* **F8.** From (4.2) on, "A_s" is used for its majorant Ā_s := ((u_s+ε+τ)/(u_s+ε))^{4.1v} (e.g. "v log X ≤ A_s^{1/4.1}/e"
  is true for Ā_s, not for A_s). Say "from now on A_s denotes the right side of (4.2)"; all inequalities are
  monotone in A_s, so nothing else changes.
* **F13 (optional).** (D2) is used with U_E alone everywhere except in (iii), where u_b^{2γ}Z^{14v} ≤ 1.42(U_E+D)^{2γ}.
  Since also u_b^{2γ}Z^{14v} ≤ 2^{2γ}X₀^{2γ−14v}(X₀+D)^{14v}, (D2) may be weakened to
  "ϑ₀ U_E^{γ−7v}(U_E+D)^{7v} ≤ 1/20". With D ≤ 1/2 this removes D from the two-pass restriction up to the factor
  U_E^{−7v} (not ε-dependent). Then Corollary P7.T needs only 0.96R₁^{−γ₁}U_Γ^{γ₁−7v} ≤ 1/20 (and D ≤ 1/2) instead of U_Γ + D ≤ R₁·20^{−1/γ₁}; F12 below then no
  longer forces ρ₀ to be tiny.
* **P7.D′.** Proof correct (y_s′ = (v/ρ_s)y_s needs ρ_s ≥ ε on [t_E,t], which holds for u_s ≥ 1.01ε; 0.998/1.03 =
  0.969). Exact check in §7. **F9:** in the consequence write "sin∠_s(t_E) ≥ k u_s^{γ′} for some γ′ > 0 (e.g. γ′ = 1)":
  (D1) is only assumed with γ ≤ 1/4, and the example γ = 1 is another exponent. Also the Proposition is about
  the tilt of the chords from E; it shows that the tilt bound |e − û| ≲ ϑ₀u^γ cannot be propagated with the same
  exponent, **not** that (J2) with exponent γ fails for N (N measures variation of tilt; for y₀ = ku^{1+γ′} it does lose
  the same v/(1+v) by the computation in §1, but that is not what is proved). Reword the bold sentence accordingly.

## 5. Lemma P7.H, Corollary P7.T — OK with fixes; interface list

**P7.H.** Checked: (a⁺,b⁺), I = (a_{j−1},b⁺), (a_{j−1},a_j) are in 𝔉(t_j) (family of leg j at its closed end, F1);
λ⁽¹⁾_I ≤ u_b + 1.5ε ≤ min(4u_b, R₁); e_{(a_{j−1},a_j)}(t_j) = û by Lemma C(2); (TL) twice; Lemma 4(a) for the
enlargement (1.02 ≤ 1.1); 2·4^{γ₁}C_TL + 1.1 ≤ 2.86C_TL; 2.87·16.5 = 47.4 ≤ 48. The side is consistent with P7.D: û
points from x_{a_{j−1}} to x_{a_j}, the arc ahead has z_s ≈ u_s > 0, Harry retreats along −û over seen labels.
* **F10.** P7.H/P7.T say "let (J1),(J2) hold" / "let a first pass satisfy the conclusions of Theorem P7.B", but Harry
  leaves the construction at t_E, so the first pass as defined in §1 never reaches its T_stop. Replace by: "let
  the hypotheses of Theorem P7.B hold for (γ₁,R₁,M₁) and let P follow the construction on [t_s, t_E]; by causality
  (F3) the invariants (J1), (J2), (TL), Step 1 hold on [t_s,t_E]". (True: every step of the continuity argument at
  time t uses the path up to t only, and T_B bounds elapsed time for any prefix.)

**P7.T.** Proof checked (1.03·e^{1/200} = 1.0352 ≤ 1.036; 1.0352/5 ≤ 1/4; 2.9·0.96·e^{1.375/200} = 2.803; 2.6·1.036^{3/2} =
2.742; 0.998/1.036 = 0.963; enlargement step OK since U_Γ ≥ ε).
* **F11.** "(E1) with a′ = γ₁ − 7v": under the stated hypothesis v ≤ γ₁/7 this a′ may be 0, and a′, hence the
  threshold v₀(a′,…) of Corollary P7.E, depends on v. Fix: assume v ≤ γ₁/14 and state (E1) with **a′ := γ₁/2** (valid
  since λ₁ ≤ 1); or with F4 take any γ ≤ γ₁ − 29v. Also C₀λ₀^{a′} ≤ 1 of (ST_end) is *not* automatic: it requires
  λ₀ ≤ C₀^{−1/a′} in addition to λ₀ ≤ U_Γ (for pairs in Γ, (E2) then holds with c_sep = 0.95λ₀).
* **F12.** Phase (2) starts at t_E + D where dist(P, conv Γ) ≤ |P − x_E| = σ(D) ≤ (1+v)D. Hence the hypotheses force
  **ρ₀ ≤ (1+v)D**, U_Γ ≤ (1+v)D/5 and C₀ ≥ 2.8vT/ρ₀² with ρ₀ ≤ R₁·20^{−1/γ₁}: the corollary only treats the tiny arc
  next to E, and its constant is dominated by vT/ρ₀². Lemma P7.A allows a time-dependent ρ₀(t); the corollary
  should be stated with ∫dt/ρ₀(t)² (the proof is the same), otherwise the far-phase term is charged at the
  worst distance for the whole excursion. No ε-dependence as long as D is fixed independently of ε.

**Interface list (is P7.E usable from what the theorems produce verbatim?).**
1. *From P7.B at a later leg start, same side:* yes (Remark of §2), with F5; cost γ ↦ γ/2, R ↦ 16^{−1/γ₁}R₁.
2. *From [B, Theorem B] verbatim:* yes with c_sep = R/4, on the arc [a_j, label U] and only while targets stay
   inside it (F6).
3. *From P7.T:* only partially, and the authors' proviso is necessary. Produced: N-bound and c ≥ 0.95λ₁ for pairs
   ⊂ Γ, in **t₁-arclength labels**, scales ε/2 ≤ λ₁ ≤ l_{t₁}(Γ). Needed by (ST_end) and not produced: (i) t_s must be a
   leg start with P(t_s) on the front at a_s; if t_s > t₁ another passive transport t₁ → t_s (Lemma P7.A again,
   with its own ρ₀) is required and the labels change again (harmless: lengths grow by e^{Λ}); (ii) (E1) for pairs in
   A∖Γ and pairs straddling the far end of Γ (for these, Fact 0.1 does not help; one needs a tilt-matching
   estimate between Γ and the rest of A, of the type (TL)); (iii) (E2) for pairs not in Γ; (iv) F11.
   "Ahead": Γ is ahead of E for the *first* pass; for the second pass (reflected orientation) E = b_E and Γ is the
   terminal piece of A, so "pairs ahead of the base up to the end" are the pairs of Γ exactly in the last
   U_Γ of the sweep. Consistent.
4. *Scales:* P7.B's invariants are for λ ≤ R (label length at t_s); (E1) is for λ ≤ λ₀ and P7.E sets R ≤ λ₀/32;
   P7.H needs U_E ≤ R₁/2 and room U⁽¹⁾ − u⁽¹⁾_E ≥ R₁; P7.T needs U_Γ + D ≤ 20^{−1/γ₁}R₁. All consistent, each step
   shrinking the scale by a factor depending on γ only (not on ε).

## 6. Proposition P7.C — OK

Derivation checked symbolically (ρ′ = v + cos θ, ρθ′ = −sin θ, first integral, G′, X, ∂_rθ, D₁, D₂, both bounds of
(iii): D₂ − v(J − t^{1−v})/(1+v) = v[vJ cos θ + t^{1−v}(1−cos θ)]/(1+v) ≥ 0; D₁ ≤ t^{−v}(1+v−v cos θ)/(1+v) ≤ t^{−v} since J, cos θ ≥ 0)
and numerically (§7). Independent closed form via h in §1. The sentence "true and virtual candidates coincide"
concerns τ ≥ 0 only (the model does not say how the straight segment arose) — fine for a model statement.

## 7. Numerical tests (`code/referee/P7_2/`)

All are evidence, not proof. Outputs: `out_straight.txt`, `out_p7b.txt`, console of the other two scripts.

**(N1) Constants** (`constants.py`). Every numerical inequality of §1–§5 recomputed for γ ∈ {1/4, 0.2, 0.1, 10⁻², 10⁻³,
10⁻⁶} at the largest admissible v: all hold. Tight ones: ΔE·v ≤ 0.09 (0.0896), c₁ = 4.85 (4.841 at γ = 1/4),
C_TL·γ = 16.5 (16.46), 2.87·16.5 ≤ 48 (47.4). Restart: R₂/R₁ = 16^{−1/γ₁} = 1.5·10⁻⁵ (γ₁ = 1/4), 9·10⁻¹³ (γ₁ = 0.1).

**(N2) P7.C exact** (`straight_exact.py`, mpmath 40 digits; v ∈ {10⁻⁵, 10⁻², 0.1, 0.3}, τ/r ∈ {0.3, 3, 10², 10⁴, 10⁸}).
G(θ) = quadrature of ∫dϑ/(sin²ϑ tan^vϑ/2): rel. error ≤ 9·10⁻⁴¹. G = independent h-integral: ≤ 3·10⁻⁴⁰.
X(r,τ) against a Taylor ODE solution (τ/r ≤ 3): ≤ 2·10⁻³³. (D₁,D₂) against central differences of X in r:
≤ 3·10⁻²⁰ (= difference-quotient error). μt^v(1−2t^{1−v})/(1+v) ≤ tan Θ ≤ μ(1+v)t^v/(1−vμ): true in all 20 cases.
Θ/(c_v(r/τ)^{v/(1+v)}) → 1: e.g. v = 0.1: 0.617, 0.976, 0.9987, 0.99985 at τ/r = 3, 10², 10⁴, 10⁸; v = 10⁻⁵: 0.684, 0.990,
0.9999, 0.99999999. The hook is confirmed: e.g. v = 0.3, tan Θ = 0.169, 0.143, 0.053, 0.0064 at τ/r = 3, 10², 10⁴, 10⁸
(rigid rotation would give ≈ 0.3).

**(N3) P7.D′ exact** (same script; v ∈ {10⁻⁵, 10⁻², 0.2}, initial offsets y₀/z₀ ∈ {10⁻³, 0.05, 0.3}, τ/z₀ ∈ {0.5, 5}).
Exact law y/y₀ = ((ρ+z)/(ρ₀+z₀))^{v/(1+v)}: error ≤ 2·10⁻³³; h-law z − vρ = z₀ − vρ₀ + (1−v²)τ: ≤ 10⁻³⁴.
(y/y₀)/(1+(1+v)τ/u)^{v/(1+v)} with u = chord (the worst case of the Proposition): between 1.000000000 and 1.0025 in
all 18 cases — the lower bound of P7.D′ is attained to 9 digits for small tilt; the factor 0.96 is only needed for
the change of the chord length.

**(N4) P7.D on synthetic fronts** (`p7d_front.py`; ε = 10⁻³, U_E = 0.05, D = 0.2, γ = 1/4, ϑ₀ at 99.9% of (D2); tangent
angle ψ(u) = ϑ₀u^γ × {1, cos(6 log(u/ε)), sign cos(3 log(u/ε))}; ≈ 6·10³ pairs with λ ≥ ε/2; τ ∈ {0.002, 0.02, 0.2}).
Ratios measured/bound (must be ≤ 1), worst over profiles and times:

| v | (ii) | (iii) max l/λ (≤1.03), min c/λ (≥0.998) | (iv) | (v) | max eff. exponent of μ^{1/2} in units of v |
|---|---|---|---|---|---|
| 10⁻⁵ (in range) | 0.989 | 1.000006, 0.99951 | 0.852 | 0.999999 | 3.55 |
| 10⁻³ (outside (D3)) | 0.989 | 1.00058, 0.99951 | 0.846 | 0.99989 | 3.55 |
| 0.03 (outside (D3)) | 0.982 | 1.0173, 0.99951 | 0.679 | 0.9966 | 3.54 |

All bounds hold, also far outside the stated range of v. (ii) is nearly attained at τ → 0 (it is (D1) itself);
(v) is attained at v → 0 (it is N(t_E)). The effective growth exponent of μ^{1/2} for pairs reaches 3.5v for the
oscillating profile (pointwise offsets grow with exactly v/(1+v)), so "7v" is within a factor 2 of what
happens for pairs at scale ≈ ε.

**(N5) Construction cut at b_E** (`p7b_end.py`, `p7b_inrange.py`; unit circle, head-on start, t_s = t₃ resp. t₆; RK4;
virtual and **true** candidates integrated separately, a true candidate counts as seen when its distance to Harry
was ≤ ε at some step; a_{j+1} snapped to a grid of ε/40).

| run | U | non-final legs (≤ 2U/ε) | advance/ε in t_s-labels (∈[½,1]) | final l/ε (≤1) | time (≤ 2U/(1−v)) | all true candidates of [a_s,b_E] seen; max over arc of (min distance)/ε |
|---|---|---|---|---|---|---|
| v = 10⁻¹², ε = 3·10⁻⁵, R = 2·10⁻³, γ = ¼ — **all hypotheses of P7.B hold** | 0.00991 | 338 (661) | 0.975 … 1.000 | 0.825 | 0.00989 (0.0198) | yes; 0.825 |
| v = 10⁻¹², ε = 10⁻⁴ ((S2) fails for γ = ¼) | 0.0297 | 304 (594) | 0.975 … 1.000 | 0.625 | 0.0296 (0.0594) | yes; 0.625 |
| v = 0.05, ε = 2·10⁻³ (out of range) | 0.269 | 138 (269) | 0.953 … 0.983 | 0.906 | 0.282 (0.567) | yes; 0.906 |
| v = 0.3, ε = 2·10⁻³ (out of range) | 0.544 | 318 (544) | 0.712 … 0.957 | 0.317 | 0.777 (1.554) | yes; 0.358 |
| v = 0.05, corner made beforehand at label 0.25 (Harry touches the front there, retreats 0.3), b_E = 0.25 | 0.312 | 161 (312) | 0.937 … 0.983 | 0.644 | 0.327 (0.656) | yes; 0.252 |
| same, b_E = 0.2507 (end inside the corner zone, 0.35ε beyond the touched label) | 0.313 | 162 (313) | 0.937 … 0.983 | 0.426 | 0.329 (0.659) | yes; 0.440 |

The in-range run is a weak test (at v = 10⁻¹² the front does not move); it checks the bookkeeping of the end
(dichotomy, final leg, true candidates). The out-of-range runs show that the end mechanism is robust; two further
runs (v = 0.3 with a pre-made corner) did not complete because of a defect of my harness (zero-length leg after
snapping) and are not reported.

## 8. Summary of requested text changes

F1 (definition of 𝔉 at switching times), F2 (splitting in the proof of (c)), F3 (scope: nothing beyond b_E;
causality), F4 (free γ in P7.E; optional), F5 (edge case of the restart), F6 (restart from [B] verbatim: c_sep = R/4;
state the cost 16^{−1/γ₁}), F7 ("M₀ ≤ 2.8ϑ₀" is a hypothesis), F8 (A_s := its majorant), F9 (γ′ in P7.D′; tilt, not N),
F10 (first pass truncated at t_E), F11 (a′ := γ₁/2 with v ≤ γ₁/14; C₀λ₀^{a′} ≤ 1 to be imposed), F12 (ρ₀ ≤ (1+v)D is
forced; allow ρ₀(t)), F13 (optional: D can be removed from (D2) up to U_E^{−7v}).
None of them changes a constant of a theorem.
