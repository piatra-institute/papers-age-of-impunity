---
title: |
  The Last Age of Impunity?\
  The Accountability Chain and the Conservation of Impunity
author: PIATRA . INSTITUTE
date: June 2026
---

## Abstract

One reading of the present authoritarian and plutocratic turn treats it as an anticipatory counterrevolution against a near future in which AI, open-source investigation, automated translation and computational audit make impunity impossible. The strong form fails: the movements predate the technology and are explained by status threat, nationalism, elite economic interest and institutional weakness. A narrower mechanism remains, and we model it. The probability that a wrongful act meets a consequence is the product of six stage probabilities (discovery, attribution, publication, prosecution, independent judgment and enforcement), so it is bounded by its weakest term. Generative AI raises the three evidence stages toward one and leaves the three institutional stages, which are human and capturable, unchanged. Over 6,000 simulated cases, three results follow. Before AI, consequence runs at 0.078 of the ceiling set by the institutional stages; with saturated evidence it reaches that ceiling, and the stage with the lowest pass probability shifts from discovery to prosecution at an AI capability of 0.15. Cheaper evidence alone would raise the mean probability of consequence nearly thirteenfold, from 0.010 to 0.123, but an elite that spends a fixed budget capturing prosecution and judgment returns it to 0.007, slightly below the pre-AI level. The gap between exposure and consequence widens about fifteenfold, from 0.068 to 0.993. Run in the opposite direction, as a state's automated case against a subject, the same chain raises the probability of an adverse outcome 6.5-fold under capture. AI thus makes impunity visible without ending it, and the remaining constraint lies in courts and enforcement.

## 1. Introduction

A widely circulated reading of the present treats the strongman, the oligarch and the anti-institutional billionaire as responding to a future they can anticipate. In that future, artificial intelligence, open-source investigation, automated translation, leaked archives and computational audit dissolve the opacity on which power has depended, so that the long period in which the powerful could rely on delay, secrecy, better lawyers and public forgetting is ending, and attacks on courts, journalists, inspectors and archives form an anticipatory counterrevolution against machine-amplified justice. The thesis has moral weight, and its strong form is false.

It fails on chronology and motive. Authoritarian nationalism, oligarchic capture and charismatic anti-institutionalism are far older than machine learning; fascism, patrimonial rule and the imperial police state managed information and suppressed oversight without any model. The movements the thesis names were largely formed before generative AI reached its present capabilities, and their support is well explained by other forces: status threat, in the most carefully studied case, outweighs personal economic hardship (Mutz, 2018), alongside nationalism, religious mobilization, demographic anxiety, the collapse of local media and the ordinary preference of those in power for fewer constraints. An attack on a prosecutor demonstrates opposition to constraint and implies no foreknowledge of computational audit. The strong thesis attributes a sophisticated, future-directed motive where self-preservation, ideology and resentment already suffice.

A narrower mechanism survives. As the cost of discovering and linking evidence falls, actors who benefit from opacity gain a stronger incentive to disable, discredit, defund or capture the institutions that convert evidence into consequences. The mechanism requires no leader to expect prosecution by an algorithm. It requires only that independent record-keeping, professional administration, investigative journalism and open courts act as constraints, and that cheaper evidence raises the value of controlling them. The question is whether this mechanism produces a final age of impunity, after which the powerful can no longer escape. In the model below it does not: the transition runs from scarce evidence to scarce adjudication, and impunity is conserved across it.

## 2. Model: the accountability chain

Whether a wrongful act meets a consequence depends on the survival of a chain of events. The act must be discovered, the conduct attributed to a responsible agent, the finding brought into a public and legible form, acted on by a prosecutor or regulator, judged by an independent forum, and sanctioned by actual enforcement. The probability that an act of type $m$ ends in a consequence is the product of the stage pass probabilities,

$$P_m = p_{\text{disc}}\, p_{\text{attr}}\, p_{\text{pub}}\, p_{\text{pros}}\, p_{\text{judg}}\, p_{\text{enf}},$$

which enters the economics of deterrence through the condition that misconduct remains attractive while its expected benefit exceeds the expected sanction, $B_m > P_m S_m + R_m$, with $S_m$ the magnitude of the sanction and $R_m$ the reputational cost (Becker, 1968). A product is bounded above by its smallest term. A chain with one near-zero link has a near-zero value however strong its other links, so the probability of consequence is governed by the weakest stage.

The six stages fall into two groups. Discovery, attribution and publication are evidence stages: finding, connecting and surfacing information. Generative AI, entity resolution, automated translation, optical character recognition over scanned archives, network analysis and open-source investigation now perform this work at a scale that once required a large organization. The offshore leaks and cross-border investigations demonstrate the capability: the FinCEN Files joined reporters in 88 countries, and automatic international exchange of bank information has been estimated to close most of the offshore tax gap it covers (Alstadsæter, Johannesen and Zucman, 2019; International Consortium of Investigative Journalists, 2024). Prosecution, independent judgment and enforcement are institutional stages, in which an institution converts a finding into a consequence. No model performs them. They are carried out by prosecutors who can be replaced, courts that can be packed and enforcement agencies that can decline to act, and they are therefore human and capturable.

In the simulation, 6,000 cases each draw six stage probabilities from Beta distributions (concentration 8) with means 0.35, 0.45 and 0.50 for the evidence stages and 0.45, 0.55 and 0.50 for the institutional stages. An AI capability parameter $\alpha \in [0,1]$ lifts each evidence stage as $p \to p + \alpha(1-p)$ and leaves the institutional stages unchanged. A self-protective elite holds a capture budget of 1.4 and captures stages cheapest first, driving each captured stage to a floor of 0.12. An institutional stage costs 0.6 to capture; an evidence stage costs 0.5 when evidence is scarce and centralized and rises linearly to 3.0 at $\alpha = 1$, when evidence is distributed. All magnitudes are illustrative.

## 3. Results

### 3.1 Migration of the bottleneck

The product of the three institutional stages defines a ceiling on consequence, the highest probability attainable if every wrongful act were discovered, attributed and published. In the simulated population the ceiling is 0.123. Before AI the mean probability of consequence is 0.078 of that ceiling: the institutions could convert far more than they receive, because evidence rarely reaches them. Evidence is the binding constraint, and improving it improves accountability, which is why earlier expansions of information, from the printed pamphlet to the leaked diplomatic cable, reduced opacity.

As $\alpha$ rises, the evidence stages approach one and the probability of consequence rises toward the institutional ceiling, reaching it at $\alpha = 1$ (Figure 1, left). The stage with the lowest mean pass probability changes from discovery to prosecution at $\alpha = 0.15$ (closed form 0.154, since stage means are linear in $\alpha$). At that point the product is still only 0.14 of the ceiling, because the evidence stages continue to multiply it down; the remaining gain accrues gradually as all three evidence stages approach one. With saturated evidence, further discovery adds nothing: the product equals the institutional product and cannot exceed it. The constraint has moved from evidence to adjudication.

![Left: mean probability of consequence as a fraction of the institutional ceiling (the product of the prosecution, judgment and enforcement stages) against AI capability $\alpha$; the ratio rises from 0.078 at $\alpha = 0$ to 1 at $\alpha = 1$, and the dashed line marks $\alpha = 0.15$, where prosecution replaces discovery as the stage with the lowest mean pass probability. Right: number of evidence and institutional stages captured by an elite budget of 1.4 against $\alpha$; the budget switches from evidence to institutional stages when the cost of capturing an evidence stage exceeds that of an institutional stage, at $\alpha = 0.04$.](../simulation/output/figures/migration.png){width=95%}

The allocation of the capture budget changes as well (Figure 1, right). An elite suppresses the chain where suppression is cheapest per unit of effect. When evidence is scarce and centralized, the evidence stages are cheap to suppress: one witness to intimidate, one archive to control, one newspaper to buy. When evidence is distributed, suppression becomes expensive, because a leaked database cannot be recalled and an open method cannot be made secret, and the cheapest remaining targets are institutions. In the model the budget switches from two evidence stages to prosecution and judgment once an evidence stage costs more than an institutional one, at $\alpha = 0.04$. This threshold follows from the stipulated cost schedule, and it lies below the binding-stage crossover of 0.15.

### 3.2 Conservation of impunity

The elite's response determines the outcome. Given a fixed budget to drive stages toward the capture floor, the elite allocates it to minimize the probability of consequence. Driving any stage to the floor multiplies every case's product by a similar factor, so the leverage of capture is roughly equal across stages and the elite buys the cheapest captures its budget allows. With saturated evidence these are the institutional chokepoints, a chief prosecutor and a high court; in the model the budget captures prosecution and judgment.

Before AI the mean probability of consequence is 0.010. If AI raises the evidence stages without any capture, consequence rises to 0.123, 12.8 times higher. If the elite captures the new bottleneck, consequence falls to 0.007, slightly below the pre-AI level; capture absorbs 102 percent of the evidence gain (Figure 2). Impunity is conserved: the evidence gain occurs and the probability of consequence ends where it began.

![Mean probability of consequence under three regimes. Without capture, saturated evidence raises it from 0.010 to 0.123 (green); an elite budget that captures prosecution and judgment returns it to 0.007 (red), slightly below the pre-AI level, absorbing 102 percent of the evidence gain.](../simulation/output/figures/conservation.png){width=70%}

The conservation follows from the structure of the chain. A product is bounded by its weakest controllable link, and a self-protective elite can always hold one controllable link down, so improvements confined to the links it cannot control are absorbed at the links it can. Historically, no medium has abolished impunity. Writing, double-entry bookkeeping, the printing press, public statistics, photography, the telegraph, freedom-of-information law, the leak and the smartphone each lowered an information cost, and each was met by censorship, ownership, secrecy, procedural obstruction, overload or control of enforcement (Scott, 1998; Power, 1997). No final accountability medium can exist while the conversion stages remain capturable. The model also explains why the powerful attack courts and prosecutors instead of documents: once evidence is cheap, courts are the bottleneck, and capture pays at the bottleneck. The marginal logic of a weakest-link chain suffices, and no anticipation of machine justice is required.

### 3.3 Exposure without consequence

Exposure is the evidence product alone, the probability that an act is discovered, attributed and made public; consequence is the full product. Before AI both are small, and the gap between them is 0.068. After AI, with rational capture, exposure reaches one while consequence stays at 0.007, and the gap widens to 0.993, 14.6 times its earlier size (Figure 3). Wrongdoing by the powerful becomes publicly legible and remains unsanctioned.

![Mean exposure (the probability that wrongdoing becomes publicly known) and mean consequence (the probability that it is sanctioned) before AI and after AI with rational capture. Exposure rises from 0.078 to 1 while consequence falls from 0.010 to 0.007, so the gap between them widens 14.6-fold.](../simulation/output/figures/exposure_gap.png){width=70%}

The pattern is already visible in the record. The Panama Papers were among the largest financial leaks in history, read by hundreds of journalists across dozens of countries, and the principal money-laundering trial they produced in Panama ended in 2024 with all 28 defendants acquitted (International Consortium of Investigative Journalists, 2024). Discovery succeeded and enforcement failed, the shape of a chain with saturated evidence stages and captured institutional stages. Broader indicators point the same way. V-Dem counts dozens of autocratizing states containing a large share of the world's population, the World Justice Project reports declines in oversight, checks on executive power and freedom of expression in most countries, and Transparency International places most jurisdictions below the midpoint of its scale (V-Dem Institute, 2025; World Justice Project, 2024; Transparency International, 2025). The measured decline is concentrated in the institutions that convert evidence into consequence, where the model locates capture. Visible impunity may damage legitimacy more than hidden impunity, because unanswered and visible wrongdoing teaches a public that consequences apply to the weak, which erodes the belief on which institutions depend (Arendt, 1973; Levitsky and Ziblatt, 2018).

### 3.4 The chain applied to subjects of the state

The same structure applies when the state builds an automated case against an individual. The early stage is then accusation, the flagging of a person by a predictive or scoring system, and the later stages are protections: human review, contestability and appeal. AI raises the accusation stage, initiating many more cases, as it raised discovery, and a captured administration drives review and appeal to the same floor it applied to the courts. In the model, a subject's probability of an adverse automated outcome rises from 0.113 under an accountable configuration to 0.736 under a captured one, a factor of 6.5. The tools that uncover a powerful actor's hidden conduct also flag a poor claimant's benefits application, and institutions determine which use prevails (Foucault, 1977; Eubanks, 2018; O'Neil, 2016; Noble, 2018).

Legibility therefore differs from justice, as the analysis of state simplification established before these systems existed: the standardization that lets an authority detect fraud also lets it classify, exclude and discipline a population (Scott, 1998; Crawford, 2021; Zuboff, 2019). What separates democratic from authoritarian use is the direction of the capability. Democratic accountability seeks high legibility of public power and limited, legally bounded legibility of private life; authoritarian administration reverses the relation, with opacity above and legibility below. The capability itself is symmetric, and politics sets its direction. The legal order that determines that direction is itself increasingly shaped by the powerful, through the construction of informational capitalism in which control over data, classification and platforms becomes a form of governing power (Cohen, 2019).

## 4. Limitations

The model describes an incentive structure and measures no country. The values 0.010 and 0.123 and the fifteenfold gap are properties of a stipulated chain chosen for transparency, and the model predicts no specific trial. The capture costs and budget determine which stages are captured and when the allocation switches; the conservation result depends on the budget being large enough to capture two institutional stages. The Beta-distributed stages are independent across stages within a case, whereas in practice capture of one institution may affect others.

The results do not support the strong thesis. The anticipatory-counterrevolution reading remains false, the movements predate the technology, and their motives are multicausal, with status threat, nationalism and the ordinary preference for unconstrained power carrying the explanation. The model adds only that, given such movements, cheaper evidence strengthens their incentive to do what they are observed doing, which is to capture the institutions that convert evidence into consequence.

## 5. Conclusion

The expectation embedded in the strong thesis was that abundant evidence would produce its own verdicts and end impunity without further institutional change. In the model, AI raises only the probability of finding, and finding was never the scarce resource that protected the powerful. The scarce resources were a prosecutor willing to act, a court able to judge without fear and enforcement that followed. No model supplies these stages, they are now under the heaviest attack, and the conservation result shows that gains in evidence are absorbed by an actor who controls them. The remaining work is institutional: independent prosecutors, courts insulated from capture and enforcement that binds the strong. The period that AI opens makes impunity visible, and whether visible impunity is answered depends on courts and enforcement.

## Reproducibility

The simulation is in `simulation/` (`analyses.py`, `figures.py`, `run_all.py`) and runs with `uv run python run_all.py`, seeded with 90240; it writes every modelled number to `simulation/output/results.json` and the figures to `simulation/output/figures/`. The run checks that the closed-form binding-stage crossover lies inside the 0.05 grid step where the sweep detects it, that the capture crossover lies between the first two grid points, and that consequence equals the institutional ceiling at $\alpha = 1$.

## References

Alstadsæter, A., Johannesen, N., and Zucman, G. (2019). Tax evasion and inequality. *American Economic Review*, 109(6), 2073–2103.

Arendt, H. (1973). *The Origins of Totalitarianism* (new ed.). Harcourt Brace Jovanovich.

Becker, G. S. (1968). Crime and punishment: an economic approach. *Journal of Political Economy*, 76(2), 169–217.

Cohen, J. E. (2019). *Between Truth and Power: The Legal Constructions of Informational Capitalism*. Oxford University Press.

Crawford, K. (2021). *Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence*. Yale University Press.

Eubanks, V. (2018). *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor*. St. Martin's Press.

Foucault, M. (1977). *Discipline and Punish: The Birth of the Prison* (A. Sheridan, Trans.). Pantheon Books.

International Consortium of Investigative Journalists. (2024). *Panama Papers and FinCEN Files investigations*. ICIJ.

Levitsky, S., and Ziblatt, D. (2018). *How Democracies Die*. Crown.

Mutz, D. C. (2018). Status threat, not economic hardship, explains the 2016 presidential vote. *Proceedings of the National Academy of Sciences*, 115(19), E4330–E4339.

Noble, S. U. (2018). *Algorithms of Oppression: How Search Engines Reinforce Racism*. New York University Press.

O'Neil, C. (2016). *Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy*. Crown.

Power, M. (1997). *The Audit Society: Rituals of Verification*. Oxford University Press.

Scott, J. C. (1998). *Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed*. Yale University Press.

Transparency International. (2025). *Corruption Perceptions Index 2024*. Transparency International.

V-Dem Institute. (2025). *Democracy Report 2025*. University of Gothenburg, V-Dem Institute.

World Justice Project. (2024). *Rule of Law Index 2024*. World Justice Project.

Zuboff, S. (2019). *The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power*. PublicAffairs.
