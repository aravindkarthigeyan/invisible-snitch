# Numerics

Simulation code and constant computations. None of it is part of the proof, except that the paper's constants are checked by [`../paper/verify_constants.py`](../paper/verify_constants.py).

| Path | What it does |
|---|---|
| `simulate_design_T.py` | Standalone simulation of the proof's path; writes the README animation (`--gif`). Needs numpy, plus matplotlib and pillow for the GIF. |
| `constants/Q1/` | The end theorem with every constant a parameter (`q1const.py`) and an optimiser for the admissible speed (`optimise.py`). |
| `constants/Q3/constants.py` | The touch-down constants as functions of the speed bound and window width; checks the 51 touch-down conditions. |
| `constants/Q4/final.py` | Puts the whole chain together and finds the final $v_0 = 6\cdot10^{-5}$ and $T_0 = 10.13$. Run from `constants/Q4/`. |
| `endgame/N7/` | Deep-scale simulations (down to remaining distances of about $10^{-137}$, with multiprecision checks) of the head-on start's spiral endgame. |
| `endgame/N8/` | Exploration of alternative starts that led to the proof's tangential design ("design T"). |

These scripts were written during the research and are kept mostly as they were. Some expect to be run from their own folder, and some write into an `out/` subfolder.
