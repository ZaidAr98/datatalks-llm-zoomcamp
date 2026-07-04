# Module 3 Homework — AI Orchestration with Kestra

LLM Zoomcamp 2026 · Cohort 2026
Homework: https://courses.datatalks.club/llm-zoomcamp-2026/homework/hw3
Instructions: https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2026/03-orchestration/homework.md

## Setup
- Kestra running locally at http://localhost:8080 (Docker Compose)
- LLM provider: Google Gemini (`gemini-2.5-flash`), free API key
- Flows imported from `03-orchestration/flows/`

---

## Q1 — Context Engineering
**Prompt tested:** "Create a Kestra flow that loads NYC taxi data from CSV to BigQuery"

**Answer:** AI Copilot has access to current Kestra plugin documentation

**Why:** Kestra's Copilot is *grounded* in the current plugin docs, so it emits valid
`type:` values and real property names. Generic ChatGPT guesses from training data and
often invents plugins/properties that don't exist.

---

## Q2 — RAG vs No RAG
Ran `1_chat_without_rag.yaml` and `2_chat_with_rag.yaml`, asking about Kestra 1.1 features.

**Answer:** Vague, generic, or fabricated — the model guesses from training data

**Why:** Without retrieved context, the model has no knowledge of the specific release
notes, so it produces a generic/hallucinated answer. The RAG version is accurate because
the real docs are injected as context.

---

## Q3 — Token Usage (short summary)
Ran `4_simple_agent.yaml` with `summary_length = short`.
Read `multilingual_agent` OUTPUT tokens from the `log_token_usage` task logs.

**Observed output tokens:** <FILL IN — the number you see>
**Answer (bucket):** <FILL IN — e.g. 60-100 tokens>

---

## Q4 — Token Usage (long summary)
Ran `4_simple_agent.yaml` with `summary_length = long`.
Compared `multilingual_agent` output tokens vs Q3.

**Observed output tokens (long):** <FILL IN>
**Multiplier vs Q3:** <FILL IN>
**Answer (bucket):** <FILL IN — e.g. 2-5x more>

---

## Q5 — Modifying a Flow
Edited `english_brevity` task: changed prompt from **1 sentence** to **3 sentences**.
Saved, ran with `summary_length = long`.

**english_brevity output tokens (1 sentence):** <FILL IN>
**english_brevity output tokens (3 sentences):** <FILL IN>
**Answer (bucket):** <FILL IN — e.g. 2-4x more>

---

## Q6 — Best Practices
Production workflows needing deterministic results + strict compliance
(financial reporting, regulated industries).

**Answer:** Use traditional task-based workflows for predictability and auditability

**Why:** AI agents are non-deterministic (same input can give different output) and hard
to audit. Regulated/financial work needs reproducible, auditable, deterministic steps —
classic task-based flows, not agents.

---

## Notes
- Q1, Q2, Q6 are conceptual (answers above, with reasoning).
- Q3, Q4, Q5 require running the flows and recording the ACTUAL token counts observed.
