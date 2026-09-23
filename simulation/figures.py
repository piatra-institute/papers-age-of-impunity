"""Figures for *The Last Age of Impunity?*. Each reads the results dict and writes
one PNG. No new computation; every plotted value is a results key.
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def plot_migration(results: dict, path: str) -> None:
    m = results["bottleneck_migration"]
    al = [r["alpha"] for r in m["sweep"]]
    inst = [r["captured_institutional"] for r in m["sweep"]]
    evid = [r["captured_evidence"] for r in m["sweep"]]
    ratio = [r["consequence_over_ceiling"] for r in m["sweep"]]
    fig, (ax0, ax) = plt.subplots(1, 2, figsize=(11, 4))
    ax0.plot(al, ratio, "o-", color="#333", ms=3)
    ax0.axvline(m["binding_crossover_alpha_exact"], color="#b2182b", ls="--", lw=1,
                label=f"binding stage becomes institutional ($\\alpha$ = {m['binding_crossover_alpha_exact']:.2f})")
    ax0.set_xlabel("AI capability $\\alpha$")
    ax0.set_ylabel("consequence / institutional ceiling")
    ax0.set_ylim(0, 1.05)
    ax0.set_title("Mean probability of consequence relative to the institutional ceiling", fontsize=9)
    ax0.legend(fontsize=8, loc="lower right")
    ax.plot(al, evid, "o-", color="#2166ac", ms=3, label="evidence stages captured")
    ax.plot(al, inst, "s-", color="#b2182b", ms=3, label="institutional stages captured")
    ax.axvline(m["capture_crossover_alpha_exact"], color="#777", ls=":", lw=1,
               label=f"cost crossover ($\\alpha$ = {m['capture_crossover_alpha_exact']:.2f})")
    ax.set_xlabel("AI capability $\\alpha$")
    ax.set_ylabel("stages captured by the budget")
    ax.set_ylim(-0.1, 2.6)
    ax.set_title("Stages captured by the elite budget (1.4) against AI capability", fontsize=9)
    ax.legend(fontsize=8, loc="center right")
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


def plot_conservation(results: dict, path: str) -> None:
    c = results["conservation"]
    labels = ["pre-AI", "post-AI\nno capture", "post-AI\nwith capture"]
    vals = [c["consequence_pre_ai"], c["consequence_post_ai_no_capture"],
            c["consequence_post_ai_with_capture"]]
    fig, ax = plt.subplots(figsize=(6.6, 4))
    ax.bar(labels, vals, color=["#999", "#1a9850", "#b2182b"])
    ax.set_ylabel("mean probability of consequence")
    ax.set_title("Mean probability of consequence under three regimes")
    for i, v in enumerate(vals):
        ax.text(i, v + 0.003, f"{v:.3f}", ha="center", fontsize=9)
    ax.set_ylim(0, 0.14)
    ax.text(2, 0.03, f"capture absorbs\n{c['absorption_fraction']*100:.0f}% of the\nevidence gain",
            fontsize=8, color="#b2182b", ha="center")
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


def plot_exposure_gap(results: dict, path: str) -> None:
    e = results["exposure_gap"]
    fig, ax = plt.subplots(figsize=(6.6, 4))
    x = [0, 1]
    ax.bar([i - 0.2 for i in x], [e["exposure_pre_ai"], e["exposure_post_ai"]],
           width=0.4, color="#2166ac", label="exposure (what is known)")
    ax.bar([i + 0.2 for i in x], [e["consequence_pre_ai"], e["consequence_post_ai"]],
           width=0.4, color="#b2182b", label="consequence (what is sanctioned)")
    ax.set_xticks(x)
    ax.set_xticklabels(["pre-AI", "post-AI (with capture)"])
    ax.set_ylabel("mean probability")
    ax.set_title("Exposure and consequence before and after AI (with capture)")
    ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)
