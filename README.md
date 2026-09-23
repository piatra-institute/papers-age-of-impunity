# The Last Age of Impunity?

One reading of the present authoritarian and plutocratic turn treats it as an anticipatory counterrevolution against a near future in which AI, open-source investigation, automated translation and computational audit make impunity impossible. The strong form fails: the movements predate the technology and are explained by status threat, nationalism, elite economic interest and institutional weakness. A narrower mechanism remains, and we model it. The probability that a wrongful act meets a consequence is the product of six stage probabilities (discovery, attribution, publication, prosecution, independent judgment and enforcement), so it is bounded by its weakest term. Generative AI raises the three evidence stages toward one and leaves the three institutional stages, which are human and capturable, unchanged. Over 6,000 simulated cases, three results follow. Before AI, consequence runs at 0.078 of the ceiling set by the institutional stages; with saturated evidence it reaches that ceiling, and the stage with the lowest pass probability shifts from discovery to prosecution at an AI capability of 0.15. Cheaper evidence alone would raise the mean probability of consequence nearly thirteenfold, from 0.010 to 0.123, but an elite that spends a fixed budget capturing prosecution and judgment returns it to 0.007, slightly below the pre-AI level. The gap between exposure and consequence widens about fifteenfold, from 0.068 to 0.993. Run in the opposite direction, as a state's automated case against a subject, the same chain raises the probability of an adverse outcome 6.5-fold under capture. AI thus makes impunity visible without ending it, and the remaining constraint lies in courts and enforcement.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build age-of-impunity`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
