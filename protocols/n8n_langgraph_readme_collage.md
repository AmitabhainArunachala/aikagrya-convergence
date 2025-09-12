n8n × LangGraph — Workflow vs. Agentic Graph Collage

A practical side-by-side for building and converting between visual automations (n8n) and agentic/stateful LLM graphs (LangGraph).

## What each is best at

- n8n: visual orchestration, 400+ integrations, triggers, credentials, error branches, audit of runs.
- LangGraph: agentic loops, tool-use, memory/state, interrupts/checkpoints, programmatic control and testing.

## Hello world (side-by-side)

- n8n (importable JSON): daily Gmail summary to Slack + log to Sheets
  - See template: templates/n8n/gmail_summary.json (configure credentials)
- LangGraph (minimal Python): same intent via graph with tool calls
```python
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class S(TypedDict):
    emails: list
    summary: str

def fetch_emails(state: S) -> S:
    # TODO: call Gmail API
    return {**state, "emails": ["hello", "world"]}

def summarize(state: S) -> S:
    # TODO: call LLM
    return {**state, "summary": f"{len(state['emails'])} emails"}

def post_and_log(state: S) -> S:
    # TODO: Slack + Sheets
    return state

g = StateGraph(S)
g.add_node("fetch", fetch_emails)
g.add_node("sum", summarize)
g.add_node("post", post_and_log)
g.add_edge(START, "fetch")
g.add_edge("fetch", "sum")
g.add_edge("sum", "post")
g.add_edge("post", END)
app = g.compile()
```

## Core concepts map

- Triggers vs. Entrypoints
  - n8n: Cron/Manual/Webhook triggers
  - LangGraph: external scheduler calls into graph entry; use checkpointers for resumes
- Nodes vs. Graph nodes
  - n8n: prebuilt nodes (Gmail, Slack, Sheets), expressions, credentials
  - LangGraph: Python functions, tools, model calls; explicit state typing
- Error handling
  - n8n: error branch per node; continue on fail
  - LangGraph: try/except in nodes, retry policies, resumable checkpoints
- Secrets
  - n8n: credentials UI
  - LangGraph: env vars/secret store; inject into tool functions

## Pattern: Email triage → Slack + Sheets

- n8n steps:
  1) Trigger (Cron 8am)
  2) Gmail: search unread since yesterday
  3) Format data; LLM summarize (OpenAI/Anthropic node)
  4) Slack: post summary
  5) Google Sheets: append log
  6) Error path: log to Sheets and notify

- LangGraph steps:
  1) fetch_emails tool (Gmail API)
  2) summarize tool (LLM call)
  3) post_to_slack, append_sheet tools
  4) try/except around each; checkpoint after fetch

## Convert checklist (n8n → LangGraph)

- Identify nodes, inputs, and credentials
- Define typed state and node functions
- Replace expressions with Python transforms
- Map error branches to try/except + fallback edges
- Add checkpoints at long calls (API/LLM)
- Provide .env and secrets loader

## Gotchas

- Auth and quotas: set sandbox credentials; watch rate limits
- n8n red nodes: missing creds or required params
- LangGraph testing: stub tools and deterministic prompts

## Sources and links

- Local mirrors in resources/collage_sources/downloaded/
- Official docs (live):
  - n8n: https://docs.n8n.io
  - LangGraph: https://langchain-ai.github.io/langgraph/
  - Anthropic Agents: https://docs.anthropic.com/en/docs/agents/overview
  - OpenAI Agents: https://platform.openai.com/docs
  - xAI Grok: https://docs.x.ai/docs
  - Google Gemini: https://ai.google.dev/gemini-api
  - DeepMind research: https://www.deepmind.com/research

---

Use this as the canonical starting point. Import the n8n template, or run the LangGraph script, then iterate with your own tools and secrets.

