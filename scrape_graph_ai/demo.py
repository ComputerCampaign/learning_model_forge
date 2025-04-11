# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/9 11:43
  file:  demo
  Description :
-------------------------------------------------
"""
from scrapegraphai.graphs import SmartScraperGraph
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

graph_config = {
    "llm": {
        "model": "ollama/qwen2:7b",
        "model_tokens": 32768,  # 必须显式声明
        "temperature": 0,
        "base_url": "http://localhost:11434",
        "force_rag": True  # 新增强制标志
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",
        "must_use": True  # 禁用缓存
    },
    "rag": {
        "enable": True,
        "min_activate_size": 0,  # 强制所有内容触发 RAG
        "chunk_size": 512,
        "vector_store": {
            "type": "chroma",
            "path": "/tmp/chroma_db"  # 使用绝对路径
        }
    },
    "verbose": 2
}

smart_scraper_graph = SmartScraperGraph(
    prompt="返回该网站所有文章的标题、日期、文章链接",
    source="https://textdata.cn/blog/",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)
