# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/9 14:38
  file:  demo2
  Description :
-------------------------------------------------
"""
from scrapegraphai.graphs import SmartScraperGraph

graph_config = {
    "llm": {
        "model": "ollama/qwen2:7b",
        "temperature": 0,
        "format": "json",  # Ollama 需要显式指定格式
        "base_url": "http://localhost:11434",  # 设置 Ollama URL
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",  # 设置 Ollama URL
    },
    "verbose": True,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="返回该页面所有书的名字、作者名、评分、书籍链接",
    source="https://book.douban.com/top250",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)
