# ECO6810 Final Project Starter Repo

This repo is the home for your team's final project.

Use it to keep the charter, code, report, outputs, and team history in one place. If you like working in Colab, that is fine. Run notebooks there if you want, but push the important work back here. GitHub is the source of truth. Colab is just one place to run code.

## Start Here

1. Click `Use this template` on GitHub to create your team's own copy.
2. Rename the repo to something clear and short.
3. If GitHub is new, read [GITHUB_PRIMER.md](./GITHUB_PRIMER.md).
4. Read [FINAL_PROJECT.md](./FINAL_PROJECT.md).
5. Fill [CHARTER.md](./CHARTER.md) and get it approved.
6. Replace the placeholder fields in `main.py`, `report.md`, and `AI_USAGE_LOG.md`.
7. Run `uv sync && uv run main.py`.
8. Commit early. Commit often. Keep the repo readable.

## Why GitHub For The Project

For assignments, plain Colab was enough. For a team project, it starts to break down.

GitHub helps because:

- everyone sees the same current version
- code, report, figures, and outputs live in one place
- you can tell what changed and when
- reproducibility gets much easier
- handing the project to the instructor is just sharing the repo

The goal is not to turn you into software engineers overnight. The goal is to stop project coordination from becoming chaos.

## What This Repo Already Gives You

- a fast primer in [GITHUB_PRIMER.md](./GITHUB_PRIMER.md)
- the full project brief in [FINAL_PROJECT.md](./FINAL_PROJECT.md)
- the contract template in [CHARTER.md](./CHARTER.md)
- a runnable `main.py` that writes the required JSON outputs
- a report template in [report.md](./report.md)
- an AI usage log template in [AI_USAGE_LOG.md](./AI_USAGE_LOG.md)
- a `notebooks/` folder for Colab-first exploration
- probe and output folders in the right shape
- three worked charter examples in [`examples/`](./examples/)

## The Working Rule

One repo. One primary metric. One baseline. One documented run command.

If your team remembers only one thing, remember that.

## Repo Map

| Path | What it is for |
|---|---|
| `GITHUB_PRIMER.md` | Fast GitHub onboarding for students coming from Colab |
| `FINAL_PROJECT.md` | Full project requirements and grading |
| `CHARTER.md` | The contract you submit first |
| `main.py` | Your main reproducible run |
| `notebooks/` | Colab notebooks and exploratory work |
| `data/` | Data files or licence notes |
| `artifacts/probes/` | One-row or one-response source probes |
| `outputs/` | Required JSON outputs plus tables and figures |
| `report.md` | Final written report |
| `AI_USAGE_LOG.md` | What you used AI for and what you verified yourself |
| `examples/` | Sample approved charters by project type |

## Quick Setup

```bash
uv sync
uv run main.py
```

That first run is only a scaffold check. It writes placeholder outputs so you can see the required file shapes. Replace those placeholders before you submit anything.

Add project-specific packages in `pyproject.toml` as your work evolves. The starter environment is intentionally light.

## How To Work As A Team

- put the project question and stakeholder in the charter first
- assign clear ownership for data, analysis, writing, and cleanup
- keep commits small enough that teammates can understand them
- do not let the report drift away from what the code actually produced
- if you use a notebook, export the important logic into scripts before the end

## If You Prefer Colab

You can still use it.

Good pattern:

- explore in Colab if that is faster
- save the notebook in `notebooks/`
- move stable logic into `main.py` or helper scripts
- keep the final reproducible run inside the repo

Bad pattern:

- one teammate has the "real" notebook
- figures exist only in Colab outputs
- no one knows which version is current
- the final result depends on hidden notebook state

## Submission Logic

You are not submitting a random folder of files. You are submitting evidence that your project works.

For the milestone, we care whether the project is real and runnable.

For the final submission, we care whether you executed the approved contract honestly and reproducibly.

The exact grading rules are in [FINAL_PROJECT.md](./FINAL_PROJECT.md).

## Before You Submit

- the charter is approved
- the run command in `README.md` is accurate
- `outputs/baseline_metric.json` is real
- `outputs/primary_metric.json` is real
- `outputs/milestone_manifest.json` is real
- the report matches the code
- the AI usage log is honest

## One Good Habit

Do not wait until the final week to make the repo clean.

Messy projects do not usually fail because the idea was bad. They fail because the structure never became stable enough to trust.
