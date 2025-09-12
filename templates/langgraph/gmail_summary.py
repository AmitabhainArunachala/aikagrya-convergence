# Minimal LangGraph starter: Daily Gmail summary -> Slack + Sheets
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List

class State(TypedDict):
	emails: List[str]
	summary: str


def fetch_emails(state: State) -> State:
	# TODO: implement Gmail fetch
	return {**state, "emails": ["hello", "world"]}


def summarize(state: State) -> State:
	# TODO: call LLM
	return {**state, "summary": f"{len(state['emails'])} emails"}


def post_and_log(state: State) -> State:
	# TODO: Slack + Google Sheets
	return state


g = StateGraph(State)
g.add_node("fetch", fetch_emails)

g.add_node("sum", summarize)

g.add_node("post", post_and_log)

g.add_edge(START, "fetch")

g.add_edge("fetch", "sum")

g.add_edge("sum", "post")

g.add_edge("post", END)

app = g.compile()
