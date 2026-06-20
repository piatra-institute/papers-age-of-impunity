"""Orchestrator: reproduces every modelled number in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. The case population is seeded
(analyses.SEED), so the run is reproducible to the last digit.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_migration, plot_conservation, plot_exposure_gap

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_migration(results, str(OUT / "figures" / "migration.png"))
    plot_conservation(results, str(OUT / "figures" / "conservation.png"))
    plot_exposure_gap(results, str(OUT / "figures" / "exposure_gap.png"))

    m, c, e, r = (results["bottleneck_migration"], results["conservation"],
                  results["exposure_gap"], results["rights_symmetry"])
    print("BOTTLENECK MIGRATION")
    print(f"  binding stage pre -> post AI  : {m['binding_pre_ai']} -> {m['binding_post_ai']}")
    print(f"  institutional ceiling         : {m['institutional_ceiling']:.4f}")
    print(f"  consequence/ceiling pre AI    : {m['consequence_over_ceiling_pre_ai']:.3f}")
    print(f"  consequence/ceiling post AI   : {m['consequence_over_ceiling_post_ai']:.3f}")
    print("CONSERVATION OF IMPUNITY")
    print(f"  consequence pre-AI            : {c['consequence_pre_ai']:.4f}")
    print(f"  consequence post-AI no capture: {c['consequence_post_ai_no_capture']:.4f} "
          f"({c['post_ai_no_capture_multiple_of_pre']:.1f}x pre)")
    print(f"  consequence post-AI w/ capture: {c['consequence_post_ai_with_capture']:.4f}")
    print(f"  capture absorbs               : {c['absorption_fraction']*100:.1f}% of the evidence gain")
    print(f"  captured stages               : {c['captured_stages']}")
    print("EXPOSURE GAP")
    print(f"  exposure pre / post           : {e['exposure_pre_ai']:.3f} / {e['exposure_post_ai']:.3f}")
    print(f"  consequence pre / post        : {e['consequence_pre_ai']:.4f} / {e['consequence_post_ai']:.4f}")
    print(f"  gap pre / post                : {e['gap_pre_ai']:.3f} / {e['gap_post_ai']:.3f} "
          f"({e['gap_multiple']:.1f}x)")
    print("RIGHTS SYMMETRY")
    print(f"  subject adverse accountable   : {r['adverse_outcome_accountable']:.3f}")
    print(f"  subject adverse captured      : {r['adverse_outcome_captured']:.3f} "
          f"({r['subject_harm_multiple']:.1f}x)")


if __name__ == "__main__":
    main()
