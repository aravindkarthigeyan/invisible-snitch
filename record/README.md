# The research record

[`research-record.pdf`](research-record.pdf) (163 pages) collects everything the project found, in the order it was found. That includes the main theorem in two versions ($v_0 = 4\cdot10^{-51}$, then $6\cdot10^{-5}$), weaker results for $\varepsilon > 0$, lower bounds, conditional results, refuted conjectures and numerics. Each section ends with a status remark saying who checked it and how.

For the proof of the main theorem alone, read the much shorter [`../paper/readable/snitch-readable.pdf`](../paper/readable/snitch-readable.pdf) (readable, existence of $v_0$) or [`../paper/snitch.pdf`](../paper/snitch.pdf) (explicit $v_0 = 5.8\cdot10^{-3}$) instead.

- `tex/`: LaTeX source of the record; build with `pdflatex main.tex` twice.
- `reports/`: research reports, referee reports and audits. The record cites them by file name.
- `claims/`: the statements and proofs as they were sent to referees, with version history.

The record also cites some files and code paths that are not in this repository, such as working scripts and the problem author's original notes. Those references are kept for traceability.
