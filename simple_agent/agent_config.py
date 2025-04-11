# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/10 17:06
  file:  config
  Description :
-------------------------------------------------
"""
AGENT_CONFIG = {
    "base_url": "http://localhost:11434",  # 字符串
    "llm_model": "qwen2:7b",  # 字符串
    # "agent_type": "conversational-react-description",
    "agent_type": "structured-chat-zero-shot-react-description",
    "max_iterations": 5,
    "verbose": True
}
