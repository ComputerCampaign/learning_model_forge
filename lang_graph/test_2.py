# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/25 16:17
  file:  test_2
  Description :
  https://ywctech.net/ml-ai/langchain-langgraph-agent-part2/
  若你想state 的某个变数被自动合并reduce（而非重新给值），用Annotated 把reducer function 挂在那个变数的型态宣告上
  在node function 里直接改变state 的行为跟python 本身类似

-------------------------------------------------
"""
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated


class MyState(TypedDict):
    v: int
    total: Annotated[int, lambda x, y: x + y]


def fn1(state: MyState):
    return {"v": 89, "total": 89}


def fn2(state: MyState):
    return {"v": 64, "total": 64}


workflow = StateGraph(MyState)
workflow.add_node(fn1)
workflow.add_node(fn2)
workflow.set_entry_point("fn1")
workflow.add_edge("fn1", "fn2")
workflow.add_edge("fn2", END)

graph = workflow.compile()
r = graph.invoke({"v": 0, "total": 0})

print(r)
