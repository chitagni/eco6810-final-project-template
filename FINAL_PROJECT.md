# ECO 6810 Final Project

One project. Two checkpoints. Fifty percent of the course.

- Project milestone: 20%
- Final submission: 30%

This is not a presentation contest, and it is not a "pick a cool topic and see what happens" assignment. You are building a real, measurable, reproducible economics project. We will grade whether you scoped it well, got the data, built the pipeline, and answered the question honestly.

Start here. Then use the [charter template](./CHARTER.md).

## At a Glance

| Item | Requirement |
|---|---|
| Team size | 2-3 students |
| Project types | Predictive, causal, or descriptive |
| First gate | Approved charter |
| Core standard | One primary metric, one baseline, one reproducible run |
| Final expectation | A repo that runs cleanly and writes the required outputs |

## GitHub And Colab

This repo is the home of the project.

If GitHub is new to you, start with [GITHUB_PRIMER.md](./GITHUB_PRIMER.md). The course template repo is public, but your team should normally create a **private** repo from it and add teammates as collaborators. If you prefer working in Colab for exploration, that is fine. Use Colab when it helps, then push the work back here. The final project should not live in one person's browser tab. GitHub is the shared source of truth. Colab is just one execution surface.

## What You Are Actually Building

Your team will pick one economic question and answer it with data.

Good projects are narrow. They have a clear stakeholder, a dataset you can actually access, and one primary number that tells us whether the project worked.

Examples:

- Predictive: forecast district-level inflation, rainfall shocks, demand, or program uptake
- Causal: estimate the effect of a policy, subsidy, intervention, or treatment
- Descriptive: measure disparities, trends, or patterns across groups, places, or time

## What A Good Project Looks Like

- The question matters to a real person, institution, or policy choice.
- The primary outcome is concrete and measurable.
- You can name the exact source of the data now, not later.
- You can compute a simple baseline before you build anything fancy.
- The scope fits one semester and a 2-3 person team.
- The final result can be reproduced from a clean run.

## What Usually Goes Wrong

- The question is too broad: "study inflation in India"
- The outcome is vague: "understand impact" or "analyze trends"
- The team wants to make a causal claim with data that only supports description
- The key dataset is inaccessible, dirty beyond repair, or arrives too late
- The project quietly changes direction after the charter is approved
- The work becomes a dashboard, app, or slide deck with no clear quantitative answer

## The Flow

### Step 1: Lock the charter

Before you build, you submit a charter using the [template](./CHARTER.md).

The charter does one job: it locks the contract. It tells us:

- what question you are answering
- who cares about the answer
- what your primary metric is
- what baseline you will compare against
- what success would look like numerically
- what data you will use
- what you are not claiming

The charter is reviewed quickly and comes back as `approved` or `needs_revision`. You can revise and resubmit before the deadline. Once it is approved, that becomes the grading contract for both the milestone and the final submission.

### Step 2: Submit the milestone

The milestone is worth 20 points. At this stage, you are proving that the project is real and runnable.

You must submit:

- your approved charter
- a repo link or repo snapshot
- one-row or one-response data probes for every primary source
- `outputs/baseline_metric.json`
- `outputs/milestone_manifest.json`
- a short `README.md` with the exact milestone run command

What we check:

| Criterion | Points | What earns the points |
|---|---:|---|
| Charter lock | 4 | Your milestone still matches the approved project type, primary metric, and baseline logic |
| Source access proof | 4 | Every declared source has a working probe or an explicitly approved fallback |
| Baseline before sophistication | 4 | You computed the simple baseline first and saved it in the required format |
| Reproducible dry run | 4 | The run command works and writes the milestone artifacts |
| Metric-schema readiness | 4 | You can already produce the final metric structure, even if the value is still preliminary |

### Step 3: Submit the final project

The final submission is worth 30 points. Now we grade execution.

You must submit:

- your approved charter
- the final repo
- `outputs/primary_metric.json`
- `outputs/baseline_metric.json`
- the final report as PDF or Markdown
- the tables and figures promised in the charter
- a short AI usage log

What we check:

| Criterion | Points | What earns the points |
|---|---:|---|
| Contract fidelity | 8 | You did not silently swap the question, metric, baseline, or project type |
| Technical execution and reproducibility | 8 | The repo runs cleanly, outputs are stable, and the README matches reality |
| Evidence completeness | 8 | The promised figures, tables, checks, and fallback analyses are actually there |
| Interpretation and limitations | 6 | You answer the stakeholder question honestly and state the limits without overclaiming |

## Important Grading Principle

You are not being graded on whether the world gives you a pretty result.

A null result can still earn a strong grade. A messy overclaim cannot.

If your project is well-scoped, reproducible, and honest, you can do well even if the effect is small, the forecast is hard, or the hypothesis fails. But if you never produce a valid primary metric, that is a serious problem, because the whole point of the project is to define and deliver one.

## Required Repo Shape

Use this as the default layout unless you have a good reason not to:

```text
your-project/
  README.md
  main.py
  data/
  outputs/
    baseline_metric.json
    primary_metric.json
    milestone_manifest.json
  report.md
```

Rules:

- `uv run main.py` should run end-to-end on a clean machine
- no manual clicking or hidden setup steps
- data should be fetched in code or stored with a licence note
- the README should be short and exact

If your project needs a different run command, clear it with the instructor early. Do not surprise us at the final submission stage.

## Required Output Files

### `outputs/baseline_metric.json`

Minimum shape:

```json
{
  "metric_name": "string",
  "value": 0.0,
  "unit": "string"
}
```

### `outputs/primary_metric.json`

Minimum shape:

```json
{
  "metric_name": "string",
  "value": 0.0,
  "threshold": 0.0,
  "passed": false
}
```

### `outputs/milestone_manifest.json`

Minimum shape:

```json
{
  "charter_locked": true,
  "sources": [
    {
      "name": "string",
      "status": "ok | fallback | blocked",
      "probe_artifact": "relative/path"
    }
  ],
  "baseline_ready": true,
  "primary_metric_schema_ready": true,
  "run_command": "uv run main.py"
}
```

You can add more fields if they help, but these fields must exist.

## Rules Of The Game

- Better a small clean project than a sprawling broken one.
- If you want to change the primary metric, baseline, or project type after charter approval, ask first.
- You may use AI. Log where you used it and what you checked yourself.
- Every team member should understand the core pipeline and be able to explain it.
- Honesty helps you. Bluffing does not.

## Submission Checklist

Before you submit the milestone or the final project, make sure all of this is true:

- the charter is approved
- the repo runs from the documented command
- the required JSON files are present
- the report matches what the code actually produced
- the claimed limitations are real
- the filenames are clean and the folder is easy to inspect

## How To Pick A Project Quickly

If you are stuck, start with this sequence:

1. Pick a stakeholder.
2. Pick one decision that stakeholder cares about.
3. Pick one outcome you can measure.
4. Check that the data exists and is accessible now.
5. Write the dumb baseline first.
6. Only then decide whether the project is predictive, causal, or descriptive.

That order saves a lot of pain.

## One Last Thing

Ambition is good. Scope control is better.

The strongest projects in this course will usually look a bit boring at first glance: one sharp question, one clean baseline, one honest result, one repo that just works.
