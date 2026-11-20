# D2 claims (statements and proofs only)

Normalisation d = 1, 0 < ε < 1, 0 < v < 1. Points of R² are identified with C; a·b := Re(a b̄).
Harry's path P : [0, ∞) → C is 1-Lipschitz with P(0) = 0, fixed in advance. Candidate α: S_α(0) = e^{iα},
S_α' = v (S_α − P)/|S_α − P| while S_α ≠ P. Candidate α is *seen* if |S_α(t) − P(t)| ≤ ε for some t.
Chord: χ(θ, φ) := |e^{iθ} − e^{iφ}| (≤ |θ − φ|). L := log(1/ε).

## Claim 1 (the field F). PROVED
Let π_ε be the metric projection onto the closed disc B̄(0, ε) and F(x) := π_ε(x)/ε = x / max(|x|, ε). Then
(a) |F| ≤ 1, F is ε^{-1}-Lipschitz, and (F(x) − F(y))·(x − y) ≥ 0;
(b) |F(x) − F(y)| ≤ |x − y| / max(ε, min(|x|, |y|)).

*Proof.* (a) |π_ε(x)| ≤ ε. The projection onto a closed convex set is firmly non-expansive:
(π_ε x − π_ε y)·(x − y) ≥ |π_ε x − π_ε y|²; this gives monotonicity and, with Cauchy–Schwarz, |π_ε x − π_ε y| ≤ |x − y|.
(b) If min(|x|, |y|) ≤ ε the right side is |x − y|/ε and (a) applies. If |x|, |y| > ε then F(x) = x/|x|, F(y) = y/|y|, and
|x − y|² − |x||y|·|x/|x| − y/|y||² = |x|² + |y|² − 2|x||y| = (|x| − |y|)² ≥ 0, so
|F(x) − F(y)| ≤ |x − y|/√(|x||y|) ≤ |x − y|/min(|x|, |y|). ∎

## Claim 2 (virtual candidates). PROVED
For a continuous path P define the *virtual candidate* θ by S̃_θ(0) = e^{iθ}, S̃_θ' = v F(S̃_θ − P), and
ρ_θ(t) := |S̃_θ(t) − P(t)|, J_θ(t) := ∫_0^t ds / max(ε, ρ_θ(s)).
(a) S̃_θ exists and is unique on [0, ∞), |S̃_θ'| ≤ v, and |S̃_θ(t) − S̃_φ(t)| ≤ e^{vt/ε} |θ − φ|.
(b) |S̃_θ(t) − S̃_φ(t)| is non-decreasing in t; in particular it is ≥ χ(θ, φ).
(c) If ρ_θ(t) ≤ ε for some t, then the (true) candidate θ is seen by time t.
(d) For every θ and t: limsup_{φ→θ} |S̃_φ(t) − S̃_θ(t)| / |φ − θ| ≤ exp(v J_θ(t)).

*Proof.* (a) The right side is continuous in (t, S) and (v/ε)-Lipschitz in S (Claim 1a): global existence, uniqueness,
and Gronwall. (b) With x = S̃_θ − P, y = S̃_φ − P: (d/dt)|S̃_θ − S̃_φ|² = 2v (F(x) − F(y))·(x − y) ≥ 0 (Claim 1a).
(c) Let t0 := inf{s : ρ_θ(s) ≤ ε} ≤ t. On [0, t0], |S̃_θ − P| ≥ ε, where F(x) = x/|x|; so S̃_θ solves the true equation on
[0, t0] with S̃_θ ≠ P. The true equation has locally Lipschitz right side on {S ≠ P(t)}, hence S_θ = S̃_θ on [0, t0], and
|S_θ(t0) − P(t0)| = ρ_θ(t0) ≤ ε by continuity.
(d) Fix φ ≠ θ (mod 2π), D(s) := |S̃_φ(s) − S̃_θ(s)| > 0 (by (b)). D is Lipschitz, and for a.e. s, with x, y as above,
|x| = ρ_θ, |y| ≥ ρ_θ − D, Claim 1b gives D' ≤ v|F(y) − F(x)| ≤ v D a_φ(s), a_φ(s) := 1/max(ε, ρ_θ(s) − D(s)). Gronwall:
D(t) ≤ D(0) exp(v ∫_0^t a_φ) and D(0) ≤ |φ − θ|. As φ → θ, sup_{[0,t]} D → 0 by (a), so a_φ(s) → 1/max(ε, ρ_θ(s))
pointwise, with a_φ ≤ 1/ε; dominated convergence gives the claim. ∎

## Claim 3 (local Lipschitz bound ⇒ length bound). PROVED
If γ : [c, d] → C is continuous and limsup_{φ'→φ} |γ(φ') − γ(φ)|/|φ' − φ| ≤ Λ for every φ ∈ [c, d], then γ is Λ-Lipschitz;
in particular its length on any [a, b] ⊂ [c, d] is ≤ Λ(b − a).

*Proof.* Fix η > 0 and a ∈ [c, d). Let b* := sup{b ∈ [a, d] : |γ(b') − γ(a)| ≤ (Λ + η)(b' − a) for all b' ∈ [a, b]}.
By continuity the inequality holds at b*. If b* < d, the hypothesis at b* gives δ > 0 with
|γ(b') − γ(b*)| ≤ (Λ + η)(b' − b*) for b' ∈ (b*, b* + δ); with the triangle inequality the inequality extends past b*,
a contradiction. So γ is (Λ + η)-Lipschitz for every η > 0. ∎

## Construction W (the exact-front window walk)
Put ℓ := ε/v. All objects below are computed from P on earlier times only, so P is fixed in advance.

*Connector 1.* P(s) := s (s ≥ 0, real) until P meets S̃_0, at time τ'_1. Set a_1 := 0.
(S̃_0 stays on the positive real axis with ρ_0 = Re S̃_0 − s, ρ_0' = −1 + v min(1, ρ_0/ε) ≤ −(1 − v), ρ_0(0) = 1; so
τ'_1 ≤ 1/(1 − v) and P(τ'_1) = S̃_0(τ'_1).)

*Walk j (j ≥ 1).* Given P on [0, τ'_j] with P(τ'_j) = S̃_{a_j}(τ'_j): let Γ_j(φ) := S̃_φ(τ'_j), φ ∈ [a_j, 2π]
(Lipschitz by Claim 2a), σ_j(φ) := length of Γ_j on [a_j, φ] (continuous, non-decreasing),
a_{j+1} := max{φ ∈ [a_j, 2π] : σ_j(φ) ≤ ℓ}, w_j := σ_j(a_{j+1}), τ_{j+1} := τ'_j + w_j, and for s ∈ [0, w_j]
P(τ'_j + s) := Γ_j(φ) for any φ with σ_j(φ) = s (well defined since Γ_j is constant on intervals where σ_j is). If
a_{j+1} = 2π the walk is *final*: the construction stops and P is constant afterwards. Otherwise w_j = ℓ.

*Connector j + 1 (after a non-final walk j).* Harry runs at unit speed straight towards S̃_{a_{j+1}} until he meets it,
at time τ'_{j+1}. (At τ_{j+1}, P = Γ_j(a_{j+1}) = S̃_{a_{j+1}}(τ'_j), so ρ_{a_{j+1}}(τ_{j+1}) ≤ v w_j = vℓ = ε. With
u the unit vector from P(τ_{j+1}) to S̃_{a_{j+1}}(τ_{j+1}), the ansatz P = P(τ_{j+1}) + (s − τ_{j+1})u,
S̃_{a_{j+1}} = P(τ_{j+1}) + r u solves both equations with ρ = r − (s − τ_{j+1}), ρ' = −1 + v min(1, ρ/ε) ≤ −(1 − v);
by uniqueness this is the motion. Hence the connector is a segment, ρ_{a_{j+1}} decreases on it, and its duration is
c_{j+1} := τ'_{j+1} − τ_{j+1} ≤ ε/(1 − v); P(τ'_{j+1}) = S̃_{a_{j+1}}(τ'_{j+1}).)

P is 1-Lipschitz (connectors are unit-speed segments, walks are arclength parametrisations), continuous at every junction.

## Claim 4 (seeing by construction). PROVED
Let v < 1, ε ∈ (0, 1). (a) Every φ ∈ [a_j, a_{j+1}] is seen by time s_φ := τ'_j + σ_j(φ).
(b) For s ∈ [τ'_1, ∞) during the construction let θ*(s) := a_j on connector j (j ≥ 2) and
θ*(s) := max{φ : σ_j(φ) = s − τ'_j} on walk j. Then |P(s) − S̃_{θ*(s)}(s)| ≤ ε.
(c) If the construction stops (some walk is final), every direction is seen, by the stopping time.

*Proof.* (a) P(s_φ) = Γ_j(φ) = S̃_φ(τ'_j) and |S̃_φ'| ≤ v, so ρ_φ(s_φ) ≤ v σ_j(φ) ≤ vℓ = ε; apply Claim 2c.
(b) On walk j, P(s) = S̃_{θ*(s)}(τ'_j) and s − τ'_j ≤ ℓ. On connector j, ρ_{a_j} is decreasing from a value ≤ ε.
(c) The intervals [a_j, a_{j+1}] cover [0, 2π]; apply (a). ∎

## Claim 5 (time bound). PROVED
Let Λ ≥ 1, L := log(1/ε), and
  (1 − v) J*(Λ) := 2 + 2 log(2/((1 − v)ε)) + 2πΛ L + 2 + 2πΛ.
If v J*(Λ) ≤ log Λ, then construction W stops after at most 1 + 2πΛ/ℓ walks, at a time
  T ≤ (1 + 2πΛ)/(1 − v),
and (Claim 4c) every direction is seen by time T. Moreover every walked front Γ_j is Λ-Lipschitz on [a_j, 2π].

*Proof.* For j ≥ 1 let (B_j) be: J_φ(t) ≤ J*(Λ) for all φ ∈ [0, 2π] and t ∈ [0, τ'_j]. By Claim 2d and Claim 3, (B_j)
implies that Γ_j is e^{vJ*}-Lipschitz, hence Λ-Lipschitz, on [a_j, 2π]; then σ_j(b) − σ_j(a) ≤ Λ(b − a), and if walk j is
not final, ℓ = σ_j(a_{j+1}) ≤ Λ(a_{j+1} − a_j).

*Phase-1 estimate.* For t ≤ τ'_1, P(s) = s, and g(s) := Re S̃_φ(s) − s has g' ∈ [−1 − v, −(1 − v)], |g(0)| ≤ 1, so
|g| ≤ R := 1 + (1 + v)/(1 − v) = 2/(1 − v) on [0, τ'_1]. As ρ_φ ≥ |g| and g is decreasing with |g'| ≥ 1 − v,
  J_φ(τ'_1) ≤ (1/(1 − v)) ∫_{−R}^{R} du / max(ε, |u|) = (2/(1 − v))(1 + log(R/ε)) =: J^{(1)}.
J^{(1)} ≤ J*, which is (B_1).

*Step (B_j) ⇒ (B_{j+1}) (walk j non-final).* By (B_1), …, (B_j) (note (B_i) ⇐ (B_j) for i ≤ j), walks 1, …, j are on
Λ-Lipschitz fronts and walks 1, …, j are non-final, so a_{i+1} − a_i ≥ ℓ/Λ (i ≤ j) and j ≤ 2πΛ/ℓ. Connectors 2, …, j + 1
last ≤ ε/(1 − v) each. Fix φ and t ∈ (τ'_1, τ'_{j+1}].
Lower bound: for s ∈ [τ'_1, t], by Claim 4b and Claim 2b, ρ_φ(s) ≥ |S̃_φ(s) − S̃_{θ*(s)}(s)| − ε ≥ χ(φ, θ*(s)) − ε, hence
max(ε, ρ_φ(s)) ≥ ψ(s) := max(ε, χ(φ, θ*(s))/2) (if χ ≤ 2ε use ε ≥ χ/2, otherwise χ − ε ≥ χ/2).
Layer cake: since 1/ψ = ∫_0^∞ 1{ψ < y} y^{−2} dy and ψ ≥ ε,
  ∫_{τ'_1}^t ds / max(ε, ρ_φ) ≤ ∫_ε^∞ m(y) y^{−2} dy,  m(y) := |{s ∈ [τ'_1, t] : ψ(s) < y}|.
For y > 1: m(y) ≤ t − τ'_1 ≤ Σ_{i≤j} w_i + Σ_{i=2}^{j+1} c_i ≤ 2πΛ + j ε/(1 − v) ≤ 2πΛ + 2πΛ v/(1 − v) = 2πΛ/(1 − v)
(Σ w_i ≤ Λ Σ (a_{i+1} − a_i) ≤ 2πΛ; ε/ℓ = v).
For ε < y ≤ 1: ψ(s) < y forces θ*(s) ∈ A_y := {ϑ ∈ [0, 2π] : χ(φ, ϑ) < 2y}, a union of at most two intervals of total
length ≤ 4 arcsin y ≤ 2πy. On walk i, θ*(s) ∈ [c, d] implies s − τ'_i = σ_i(θ*(s)) ∈ [σ_i(c), σ_i(d)], so the walking time
with θ*(s) ∈ A_y is ≤ Λ|A_y| ≤ 2πΛy in total (the parameter intervals [a_i, a_{i+1}] are non-overlapping). The connectors
i ≥ 2 with a_i ∈ A_y: within each of the ≤ 2 intervals of A_y consecutive such a_i differ by ≥ ℓ/Λ, so there are at most
2 + 2πyΛ/ℓ of them, each of duration ≤ ε/(1 − v). Therefore
  m(y) ≤ 2πΛy + (2 + 2πΛ y v/ε) ε/(1 − v) = (2πΛy + 2ε)/(1 − v).
Hence ∫_ε^1 m(y) y^{−2} dy ≤ (2πΛ L + 2ε(1/ε − 1))/(1 − v) ≤ (2πΛL + 2)/(1 − v), and ∫_1^∞ m y^{−2} dy ≤ 2πΛ/(1 − v).
Adding J^{(1)}: J_φ(t) ≤ J*(Λ). This is (B_{j+1}).

*Termination and time.* Each non-final walk advances a by ≥ ℓ/Λ within [0, 2π], so there are at most 2πΛ/ℓ non-final
walks and the construction stops. The stopping time is τ'_1 + Σ w_i + Σ c_i ≤ 1/(1 − v) + 2πΛ/(1 − v). ∎

## Theorem D2. PROVED
For every ε ∈ (0, 1) (in units of d) and every
  v ≤ v_2(ε) := 1 / (22 log(1/ε) + 28),
construction W (with ℓ = εd/v) is a path fixed in advance, of speed ≤ 1, along which every direction is seen by time
(1 + 4π)/(1 − v) · d ≤ 14.1 d.

*Proof.* Scale to d = 1. Apply Claim 5 with Λ = 2; it suffices that vJ*(2) ≤ log 2. Let L ≥ 0 and v ≤ 1/(22L + 28) ≤ 1/28.
Then 1 − v ≥ 27/28 and log(1/(1 − v)) ≤ v/(1 − v) ≤ 1/27, so
(1 − v)J*(2) = (2 + 4π)L + 4 + 4π + 2 log 2 + 2 log(1/(1 − v)) ≤ 14.567 L + 18.028, and
v J*(2) ≤ (14.567 L + 18.028) / ((22L + 28)(27/28)) = (14.567 L + 18.028)/(21.215 L + 27)
       ≤ max(14.567/21.215, 18.028/27) = max(0.6867, 0.6677) < 0.6931 < log 2.
The time is ≤ (1 + 4π)/(1 − v) ≤ (1 + 4π)·28/27 < 14.07. ∎

## Corollary D2.1 (reduction of the goal; PROVED implication)
Let v < 1 and ε ∈ (0, 1). If in construction W every walked front Γ_j is Λ-Lipschitz on [a_j, a_{j+1}], then the
construction stops after at most 1 + 2πΛ/ℓ walks, by time (1 + 2πΛ)/(1 − v), and every direction is seen.

*Proof.* This is the "termination and time" paragraph of Claim 5 (which used only the Λ-Lipschitz property of the walked
parts and the connector durations ≤ ε/(1 − v)), together with Claim 4c. ∎
