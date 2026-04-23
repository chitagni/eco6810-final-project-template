from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUTS_DIR = ROOT / "outputs"


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def build_baseline_metric() -> dict:
    return {
        "metric_name": "replace_me_baseline",
        "value": 0.0,
        "unit": "replace_me_unit",
        "notes": "Template value. Replace this with your real baseline before the milestone.",
        "is_template": True,
    }


def build_primary_metric() -> dict:
    return {
        "metric_name": "replace_me_primary",
        "value": 0.0,
        "threshold": 0.0,
        "passed": False,
        "notes": "Template value. Replace this with your real project metric before the final submission.",
        "is_template": True,
    }


def build_milestone_manifest() -> dict:
    return {
        "charter_locked": False,
        "sources": [
            {
                "name": "replace_me_source",
                "status": "blocked",
                "probe_artifact": "artifacts/probes/replace_me_probe.md",
                "note": "Replace this with a real one-row or one-response source probe.",
            }
        ],
        "baseline_ready": False,
        "primary_metric_schema_ready": True,
        "run_command": "uv run main.py",
        "template_warning": "This scaffold runs, but it is not submission-ready until you replace the placeholders.",
    }


def main() -> None:
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    baseline_metric = build_baseline_metric()
    primary_metric = build_primary_metric()
    milestone_manifest = build_milestone_manifest()

    write_json(OUTPUTS_DIR / "baseline_metric.json", baseline_metric)
    write_json(OUTPUTS_DIR / "primary_metric.json", primary_metric)
    write_json(OUTPUTS_DIR / "milestone_manifest.json", milestone_manifest)

    print("Template outputs written to outputs/.")
    print("Replace the placeholder fields before you submit the milestone or the final project.")


if __name__ == "__main__":
    main()
