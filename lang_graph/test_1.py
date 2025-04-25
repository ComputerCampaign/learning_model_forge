# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/24 14:51
  file:  test
  Description :
  https://ywctech.net/ml-ai/langchain-langgraph-agent-part1/
  用TypedDict宣告每个key 的型态，
  如果单纯用StateGraph(state_schema=dict)，没有预告，LangGraph 不知道每个node 回传的key 重不重要，于是实作上会「很快忘记」那些key : 如果某个步骤没有回传某个key，下一步就会失去那个key 的资讯
-------------------------------------------------
"""
from langgraph.graph import StateGraph, START, END
from typing import TypedDict


# **State**
class MyState(TypedDict):  # from typing import TypedDict
    i: int
    j: int


# Functions on **nodes**
def fn1(state: MyState):
    print(f"Enter fn1: {state['i']}")
    return {"i": 1}


def fn2(state: MyState):
    i = state["i"]
    return {"i": i + 1}


# Conditional **edge** function
def is_big_enough(state: MyState):
    if state["i"] > 10:
        return END
    else:
        return "n2"


# The Graph!  The "Program" !!
workflow = StateGraph(MyState)

workflow.add_node("n1", fn1)
workflow.add_node("n2", fn2)
workflow.set_entry_point("n1")

workflow.add_edge("n1", "n2")
workflow.add_conditional_edges(
    source="n2", path=is_big_enough
)

# Compile, and then run
graph = workflow.compile()
r = graph.invoke({"i": 1000, "j": 123})
print(r)

for s in graph.stream({"i": 1000}):
    print(s)