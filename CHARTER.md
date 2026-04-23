# Project Charter — ECO 6810 Final Project

> Need the big picture first? Read the [Final Project brief](./FINAL_PROJECT.md) before you fill this out.
>
> **What this is.** A contract between your team and the course. You define success *before* you start building, so grading later is about whether you hit what you said you would hit — not whether a human liked the topic. Once the charter is approved, the numbers below become the grading spec.
>
> **What this is not.** A project plan, a slide deck, or a brainstorm. It is a short, precise, falsifiable commitment.
>
> **Where it fits.** This is the approval gate for the single 50-point final project. The milestone (20%) and final submission (30%) are both judged against this locked contract.
>
> **How to fill it.** Copy this file. Answer every field. Keep it under two pages. If a field says "numeric", write an actual number with a unit — not an adjective. The AI charter reviewer will reject vague answers and point at the exact field to fix.
>
> **Submission.** Submit as PDF to Classroom. The reviewer runs automatically and returns a verdict in under five minutes. You may iterate as many times as you want before the deadline; once approved, the charter is locked.

---

## Header

| Field | Value |
|---|---|
| Team members | _(names, 2–3 people)_ |
| Project type | _(predictive / causal / descriptive — pick one)_ |
| Estimated hours per person | _(be honest; 40–60 is typical)_ |
| Charter version | v1 |
| Date | _(YYYY-MM-DD)_ |

**Project type notes.** Predictive = you are trying to forecast or predict a quantity. Causal = you are trying to estimate the effect of a policy/intervention. Descriptive = you are quantifying patterns or disparities without causal claims. The success threshold looks different for each; pick the one that fits your primary question.

---

## 1. Problem and stakeholder

One paragraph. Who is the specific person, institution, or policy body that would care about the answer, and what decision does the answer inform? Generic "policymakers" is not a stakeholder; "the Ministry of Petroleum and Natural Gas deciding whether to extend PMUY subsidies in FY 2026-27" is.

*Write here:*

---

## 2. Primary outcome variable

The single number your project centres on. State:

- **Name** of the variable
- **Unit** (percentage, Rs/month, points, deaths per 1000, etc.)
- **Source table/column/field**
- **Population / panel** (which rows: which years, which geographies, which people)

Only one primary. Secondary outcomes go under "Scope fences" as things you *may* report but will not be graded on.

*Write here:*

---

## 3. Primary quantitative success threshold

A single numeric bar. Your project is a success if the delivered metric crosses this bar, and a failure if it does not. Pick one form:

- **Predictive:** "Out-of-sample [metric] on [held-out slice] is at most X, versus baseline Y."
- **Causal:** "Point estimate of [parameter] has 95% CI excluding zero, and |estimate| ≥ X [unit]."
- **Descriptive:** "Produce stratified estimates of [outcome] across [N ≥ __] strata, each with sample size ≥ __ and documented standard error."

If you cannot write a number, you do not yet have a project — you have a topic. Go back to Section 2.

*Write here:*

---

## 4. Baseline to beat

The naive or prior number your threshold is measured against. Examples:

- A previous study's coefficient or error.
- A simple AR(1) or last-value forecast.
- An unadjusted before-after difference.

State **what the baseline produces numerically** if you know it, or how you will compute it before the checkpoint if you do not. You must compute the baseline *before* you build anything fancy.

*Write here:*

---

## 5. Falsifiable hypothesis

One sentence the data can prove wrong. A sign, a threshold, or a rank ordering. Not "we will analyse X" — "X will be greater than Y by at least Z".

*Write here:*

---

## 6. Data sources and access plan

For each source:

- **Name and URL/API endpoint**
- **Licence or permission to use**
- **Access method** (direct download, API call, authenticated portal)
- **A 10-line script or notebook cell** that fetches one row and prints it

If any source requires manual scraping, permissions, or a login you do not yet have, flag it here with a mitigation plan.

*Write here:*

---

## 7. Scope fences

Bullet list of things you are **not** claiming and **not** responsible for. Examples:

- "We will not estimate a structural causal effect of monetary policy."
- "We will not harmonise district boundaries across NFHS rounds; analysis is at state level."
- "We will not ship a mobile version of the app."

Scope fences protect you at grading time. If a graded criterion asks about something you fenced out, the AI will not hold it against you.

*Write here:*

---

## 8. Risks and fallback

One named failure mode, and the fallback analysis you will run if it materialises. Examples:

- "If the 2022-23 PPAC data is not released by the checkpoint, we will use the FY 2021-22 panel and document the truncation."
- "If DiD parallel-trends fails visually, we fall back to a state-fixed-effects panel regression with year trends and report both."

One risk is enough. Two is fine. Zero means you have not thought hard enough.

*Write here:*

---

## 9. Reproducibility contract

Your final repo must satisfy all of these mechanically — no human judgement needed:

- [ ] `uv run main.py` runs end-to-end in under 10 minutes on a clean machine with no manual intervention.
- [ ] It writes `outputs/primary_metric.json` containing a single JSON object with at least `{"metric_name": "...", "value": <number>, "threshold": <number>, "passed": <bool>}`.
- [ ] It writes `outputs/baseline_metric.json` in the same shape.
- [ ] A `README.md` documents the commands and expected outputs in ≤ 20 lines.
- [ ] All data sources are either fetched in-script or committed under `data/` with a licence note.

If you cannot commit to this, your project is not yet scoped for automated grading. Talk to the instructor before proceeding.

---

## Sign-off

By submitting this charter, the team commits to being graded against Sections 3, 4, 5, and 9 as numeric targets, and against Sections 1, 2, 6, 7, 8 for framing and honesty. The milestone and final-project graders both use this contract. The instructor reserves the right to adjust a grade upward for exceptional work, but will not adjust downward for topic difficulty once the charter is approved.

*Signed:* _(team member names)_
