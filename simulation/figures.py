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
    binding_inst = [1 if r["binding_is_institutional"] else 0 for r in m["sweep"]]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(al, evid, "o-", color="#2166ac", ms=3, label="evidence stages captured")
    ax.plot(al, inst, "s-", color="#b2182b", ms=3, label="institutional stages captured")
    ax.fill_between(al, 0, [3 * b for b in binding_inst], color="#fde0d0", alpha=0.5,
                    label="binding stage is institutional")
    ax.set_xlabel("AI capability $\\alpha$")
    ax.set_ylabel("stages captured by the budget")
    ax.set_title("The bottleneck, and capture, migrate to adjudication")
    ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


def plot_conservation(results: dict, path: str) -> None:
    c = results["conservation"]
    labels = ["pre-AI", "post-AI\nno capture", "post-AI\nwith capture"]
    vals = [c["consequence_pre_ai"], c["consequence_post_ai_no_capture"],
            c["consequence_post_ai_with_capture"]]
    fig, ax = plt.subplots(figsize=(6.6, 4))
    ax.bar(labels, vals, color=["#999", "#1a9850", "#b2182b"])
    ax.set_ylabel("mean probability of consequence")
    ax.set_title("Conservation of impunity: capture absorbs the evidence gain")
    for i, v in enumerate(vals):
        ax.text(i, v + 0.003, f"{v:.3f}", ha="center", fontsize=9)
    ax.annotate("", xy=(2, vals[2]), xytext=(1, vals[1]),
                arrowprops=dict(arrowstyle="->", color="#b2182b"))
    ax.text(1.5, (vals[1] + vals[2]) / 2 + 0.01,
            f"{c['absorption_fraction']*100:.0f}% absorbed", fontsize=8,
            color="#b2182b", ha="center")
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
    ax.set_title("Exposure decouples from consequence")
    ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)
