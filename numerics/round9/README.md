# Round 9 constants

Scripts behind version 2 of the paper (v0 = 5.8e-3). The paper's own check is `../../paper/verify_constants.py` (218 conditions).

- `tilt_constants.py`: the single tilt constant C_T of the new tilt lemma.
- `near_const.py`: the near-pair constant D' (a supremum over cells), double precision.
- `cert_Dprime.py`: certified evaluation of D' with interval arithmetic (mpmath.iv, outward-rounded inputs).
