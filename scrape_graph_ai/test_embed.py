# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/9 16:17
  file:  test_embed
  Description :
-------------------------------------------------
"""
import requests

resp = requests.post(
    "http://localhost:11434/api/embeddings",
    json={"model": "nomic-embed-text", "prompt": "test"}
)
assert len(resp.json()["embedding"]) == 768, "嵌入维度错误"
