# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-06-20 — Initial implementation from seed chat
Scope: full paper built from `chats/chat.md` (deep-research on the "last age of impunity" / anticipatory-counterrevolution hypothesis) through the PIATRA pipeline.
Decision: ships a simulation in a NEW frame for the corpus — a serial-reliability / weakest-link accountability chain with adversarial capture — to keep the set from sounding like one instrument.
Changes:
  - Took the seed's own accountability-chain expression (ESC = p_d x p_a x p_adm x p_j x p_e x S) and the verdict ("evidence scarcity to adjudication scarcity") and made the conservation result computable.
  - Defeated the strong thesis (anticipatory counterrevolution against machine justice) on chronology/motive grounds, kept the narrow mechanism, and priced it.
  - Three results + a fourth: (1) BOTTLENECK MIGRATION — pre-AI consequence is 0.078 of the institutional ceiling (evidence-bound); post-AI it sits at the ceiling exactly (institution-bound); binding stage discovery -> prosecution at AI capability ~0.2; (2) CONSERVATION OF IMPUNITY — cheaper evidence multiplies consequence ~12.8x (0.010 -> 0.123), but rational capture of prosecution+judgment absorbs 102% of the gain, returning consequence to 0.007 (marginally below pre-AI); the capture budget migrates from suppressing 2 evidence stages (cheap when scarce) to capturing 2 institutional stages (cheap chokepoints) as AI distributes the evidence; (3) EXPOSURE DECOUPLES — exposure 0.078 -> 1.000, consequence flat, gap widens 14.6x (the Panama Papers pattern, all 28 acquitted); (4) RIGHTS SYMMETRY — the chain run downward harms a subject 6.5x under capture (Scott's ambivalence).
  - The conservation is structural: a product is bounded by its weakest controllable link, and a self-protective elite always has one, so improvements confined to the uncapturable (evidence) stages are absorbed at the capturable (institutional) one. This predicts attacks on courts over documents WITHOUT the strong thesis's anticipatory motive.
  - Calibration fix: Study 1 first used absolute d(consequence)/d(alpha), which RISES (artifact of the growing product) rather than showing the intended saturation; replaced with the institutional ceiling and the consequence/ceiling ratio (0.078 -> 1.000), which states the bottleneck migration cleanly.
  - Built simulation/ (numpy + matplotlib, uv): analyses.py (4 studies), figures.py (3 figures), run_all.py. Seeded case population (6,000); reproducible to the last digit.
  - Wrote PAPER.md (7 sections, distinctive titles, objections in §1 and boundary in §7), metadata.yaml, brief/research/sources, README.
  - 18-source bibliography, all engaged in-text, verified against the real literature (Becker; Scott; Power; Mutz; Alstadsaeter/Johannesen/Zucman; ICIJ; V-Dem; WJP; Transparency International; Levitsky & Ziblatt; Arendt; Foucault; Eubanks; O'Neil; Noble; Crawford; Zuboff; Cohen). 0 confabulated (refs MISSING = 0). Empirical indices cited as institutional authors; specific figures attributed in prose.
Verification:
  - voice: 0 errors, 8 review-candidate warns. Converted "twenty-eight" -> 28; thinned "exactly" (7 -> ~5); added short sentences for rhythm.
  - refs: 0 missing, 0 unused (18 in-text keys, 18 bib entries).
  - claims: 10 prose decimals, 0 without a matching results.json value.
  - build: 10 pages, 0 missing-character warnings.
  - check => PASS
