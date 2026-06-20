"""Model for *The Last Age of Impunity?*: the accountability chain.

Every number cited in the paper's modelled sections is a key in the dict this
module returns. The case population is drawn under a fixed seed (SEED), so the
run is reproducible to the last digit.

The frame. Whether a wrongful act meets a consequence is the product of a chain
of stage probabilities, after the seed's own accountability-chain expression:

    P(consequence) = p_discovery * p_attribution * p_publication
                     * p_prosecution * p_judgment * p_enforcement.

The first three stages are the evidence stages: discovery, linkage, and
getting the finding into public, legible form. The last three are the
institutional stages that convert evidence into a sanction: a prosecutor acting,
an independent court judging, an enforcement actually applied. Generative AI,
OSINT, automated translation, and computational audit raise the evidence stages
toward one. They do not raise the institutional stages, which are human and
capturable, and a self-protective elite spends a budget to drive the cheapest
controllable stage toward a capture floor.

Three results follow. The bottleneck migrates: when evidence was scarce it was
the binding stage, so improving it improved accountability; once AI saturates
it, the binding stage becomes adjudication, and the optimal target of capture
migrates from suppressing evidence to capturing courts. Impunity is conserved:
the product is bounded by its weakest controllable stage, so a rational elite
that captures the new bottleneck absorbs nearly the whole evidence gain, and the
probability of consequence barely moves. And exposure decouples from
consequence: the evidence product rises toward one while the full product stays
low, so everything is known and little follows, the Panama-Papers pattern.

Magnitudes are illustrative; they are not estimates of any country or case.
"""
from __future__ import annotations

import numpy as np

SEED = 90240
N = 6000

# Chain stages: the first three are evidence (AI-improvable), the last three are
# institutional (capturable). Each entry is (mean baseline pass-probability,
# institutional flag).
EVIDENCE = ["discovery", "attribution", "publication"]
INSTITUTIONAL = ["prosecution", "judgment", "enforcement"]
STAGES = EVIDENCE + INSTITUTIONAL
BASELINE = {"discovery": 0.35, "attribution": 0.45, "publication": 0.50,
            "prosecution": 0.45, "judgment": 0.55, "enforcement": 0.50}
KAPPA = 8.0                 # Beta concentration for per-case heterogeneity

# capture costs: the price for the elite to drive a stage to the capture floor.
# Institutional stages are cheap chokepoints (one chief prosecutor, one high
# court). Evidence stages are cheap to suppress when scarce and centralized but
# become expensive once AI distributes them (you cannot un-leak a database).
INST_COST = 0.6
EVID_COST_PRE = 0.5         # evidence cost when scarce/centralized (low AI)
EVID_COST_POST = 3.0        # evidence cost when distributed (high AI)
CAPTURE_FLOOR = 0.12        # what a captured stage's pass-probability falls to
BUDGET = 1.4               # the elite's capture budget


def make_cases(seed: int = SEED, n: int = N) -> dict:
    rng = np.random.default_rng(seed)
    p = {}
    for s in STAGES:
        m = BASELINE[s]
        p[s] = rng.beta(m * KAPPA, (1 - m) * KAPPA, n)
    return {"p": p, "rng": rng}


def _ai_lift(p_stage: np.ndarray, alpha: float) -> np.ndarray:
    """AI raises an evidence stage toward 1: p -> p + alpha (1 - p)."""
    return p_stage + alpha * (1.0 - p_stage)


def _stage_probs(cases: dict, alpha: float, captured: set) -> dict:
    out = {}
    for s in STAGES:
        v = cases["p"][s].copy()
        if s in EVIDENCE:
            v = _ai_lift(v, alpha)
        if s in captured:
            v = np.minimum(v, CAPTURE_FLOOR)
        out[s] = v
    return out


def _consequence(stage_probs: dict) -> np.ndarray:
    out = np.ones_like(stage_probs[STAGES[0]])
    for s in STAGES:
        out = out * stage_probs[s]
    return out


def _exposure(stage_probs: dict) -> np.ndarray:
    out = np.ones_like(stage_probs[EVIDENCE[0]])
    for s in EVIDENCE:
        out = out * stage_probs[s]
    return out


def _capture_cost(stage: str, alpha: float) -> float:
    if stage in INSTITUTIONAL:
        return INST_COST
    return EVID_COST_PRE + alpha * (EVID_COST_POST - EVID_COST_PRE)


def _optimal_capture(cases: dict, alpha: float, budget: float = BUDGET) -> set:
    """The elite greedily captures stages cheapest-first within budget.

    Driving any stage to the floor multiplies every case's product by roughly the
    same factor, so leverage is equal across stages and the elite simply buys the
    cheapest reductions: it captures the lowest-cost stages its budget affords.
    """
    order = sorted(STAGES, key=lambda s: _capture_cost(s, alpha))
    captured, spent = set(), 0.0
    for s in order:
        c = _capture_cost(s, alpha)
        if spent + c <= budget:
            captured.add(s)
            spent += c
    return captured


# ---------------------------------------------------------------------------
# Study 1: bottleneck migration. Where is the binding stage, and where does the
# elite's capture budget go, before and after AI saturates the evidence stages?
# ---------------------------------------------------------------------------
def bottleneck_migration() -> dict:
    cases = make_cases()
    alphas = np.linspace(0.0, 1.0, 21)
    sweep = []
    for a in alphas:
        sp = _stage_probs(cases, float(a), set())
        means = {s: float(sp[s].mean()) for s in STAGES}
        binding = min(means, key=means.get)
        cap = _optimal_capture(cases, float(a))
        cap_evidence = len(cap & set(EVIDENCE))
        cap_inst = len(cap & set(INSTITUTIONAL))
        sweep.append({"alpha": float(a), "binding_stage": binding,
                      "binding_is_institutional": binding in INSTITUTIONAL,
                      "stage_means": means,
                      "captured_evidence": cap_evidence,
                      "captured_institutional": cap_inst})
    # the institutional ceiling: the product of the late, capturable stages,
    # which bounds the probability of consequence no matter how good the evidence
    inst_ceiling = np.ones(N)
    for s in INSTITUTIONAL:
        inst_ceiling = inst_ceiling * cases["p"][s]
    ceiling = float(inst_ceiling.mean())
    con_pre = float(_consequence(_stage_probs(cases, 0.0, set())).mean())
    con_post = float(_consequence(_stage_probs(cases, 1.0, set())).mean())
    # how close consequence sits to the institutional ceiling: evidence is the
    # binding constraint when this ratio is far below one, the institution is the
    # binding constraint when it is near one
    return {
        "sweep": sweep,
        "binding_pre_ai": sweep[0]["binding_stage"],
        "binding_post_ai": sweep[-1]["binding_stage"],
        "institutional_ceiling": ceiling,
        "consequence_over_ceiling_pre_ai": float(con_pre / ceiling) if ceiling else None,
        "consequence_over_ceiling_post_ai": float(con_post / ceiling) if ceiling else None,
    }


# ---------------------------------------------------------------------------
# Study 2: conservation of impunity. Mean probability of consequence under three
# regimes: pre-AI, post-AI without capture, post-AI with rational capture.
# ---------------------------------------------------------------------------
def conservation() -> dict:
    cases = make_cases()
    pre = _consequence(_stage_probs(cases, 0.0, set())).mean()
    post_free = _consequence(_stage_probs(cases, 1.0, set())).mean()
    cap = _optimal_capture(cases, 1.0)
    post_captured = _consequence(_stage_probs(cases, 1.0, cap)).mean()

    evidence_gain = post_free - pre
    capture_absorbs = post_free - post_captured
    absorption_fraction = capture_absorbs / evidence_gain if evidence_gain else None
    net_change = post_captured - pre
    return {
        "consequence_pre_ai": float(pre),
        "consequence_post_ai_no_capture": float(post_free),
        "consequence_post_ai_with_capture": float(post_captured),
        "captured_stages": sorted(cap),
        "evidence_gain": float(evidence_gain),
        "capture_absorbs": float(capture_absorbs),
        "absorption_fraction": float(absorption_fraction),
        "net_change_vs_pre_ai": float(net_change),
        "post_ai_no_capture_multiple_of_pre": float(post_free / pre) if pre else None,
    }


# ---------------------------------------------------------------------------
# Study 3: exposure decouples from consequence. The evidence product (what is
# publicly known) against the full product (what is sanctioned), pre and post AI
# with rational capture. The widening gap is exposure without consequence.
# ---------------------------------------------------------------------------
def exposure_gap() -> dict:
    cases = make_cases()
    sp_pre = _stage_probs(cases, 0.0, set())
    cap = _optimal_capture(cases, 1.0)
    sp_post = _stage_probs(cases, 1.0, cap)
    exp_pre = float(_exposure(sp_pre).mean())
    con_pre = float(_consequence(sp_pre).mean())
    exp_post = float(_exposure(sp_post).mean())
    con_post = float(_consequence(sp_post).mean())
    return {
        "exposure_pre_ai": exp_pre, "consequence_pre_ai": con_pre,
        "exposure_post_ai": exp_post, "consequence_post_ai": con_post,
        "gap_pre_ai": exp_pre - con_pre,
        "gap_post_ai": exp_post - con_post,
        "gap_multiple": float((exp_post - con_post) / (exp_pre - con_pre))
                        if (exp_pre - con_pre) else None,
    }


# ---------------------------------------------------------------------------
# Study 4: rights symmetry. The same chain run downward, the state's case
# against a subject. Captured machines raise the accusation stages and lower the
# subject's protective stages (appeal, independent review), so for the weak AI
# raises the probability of an adverse outcome rather than lowering it.
# ---------------------------------------------------------------------------
def rights_symmetry() -> dict:
    cases = make_cases()
    rng = cases["rng"]
    n = N
    # protective chain for a subject facing an automated adverse decision:
    # accusation/flagging, then human review, contestability, appeal. AI raises
    # the flagging (more cases initiated) and capture lowers the protections.
    flag = rng.beta(0.5 * KAPPA, 0.5 * KAPPA, n)
    review = rng.beta(0.55 * KAPPA, 0.45 * KAPPA, n)
    appeal = rng.beta(0.5 * KAPPA, 0.5 * KAPPA, n)
    # accountable regime: modest flagging, intact protections
    p_adverse_accountable = float((flag * (1 - review) * (1 - appeal) + flag * 0.0).mean())
    # adverse outcome occurs if flagged and the protections fail
    adverse_acc = float((flag * (1 - review) * (1 - appeal)).mean())
    # captured regime: AI raises flagging toward 1, capture removes protections
    flag_hi = _ai_lift(flag, 0.9)
    review_lo = np.minimum(review, CAPTURE_FLOOR)
    appeal_lo = np.minimum(appeal, CAPTURE_FLOOR)
    adverse_cap = float((flag_hi * (1 - review_lo) * (1 - appeal_lo)).mean())
    return {
        "adverse_outcome_accountable": adverse_acc,
        "adverse_outcome_captured": adverse_cap,
        "subject_harm_multiple": float(adverse_cap / adverse_acc) if adverse_acc else None,
    }


# ---------------------------------------------------------------------------
def run() -> dict:
    return {
        "params": {
            "n": N, "stages": STAGES, "baseline": BASELINE, "kappa": KAPPA,
            "inst_cost": INST_COST, "evid_cost_pre": EVID_COST_PRE,
            "evid_cost_post": EVID_COST_POST, "capture_floor": CAPTURE_FLOOR,
            "budget": BUDGET, "seed": SEED,
        },
        "bottleneck_migration": bottleneck_migration(),
        "conservation": conservation(),
        "exposure_gap": exposure_gap(),
        "rights_symmetry": rights_symmetry(),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2)[:3000])
