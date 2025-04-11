# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/10 17:07
  file:  agent_core
  Description :
-------------------------------------------------
"""
from langchain.agents import AgentExecutor, initialize_agent
from langchain.tools import StructuredTool
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import Ollama
from tools import math_tool, web_search, text_processor, TextProcessorInput
from agent_config import AGENT_CONFIG


class AgentSystem:
    def __init__(self):
        self.config = AGENT_CONFIG
        self.llm = None
        self.tools = []
        self.memory = None
        self.agent = None

    def initialize_models(self):
        """初始化模型和工具"""
        self.llm = Ollama(
            model=self.config["llm_model"],
            base_url=self.config["base_url"],
            temperature=0.3
        )

        # 修正2：完整的工具初始化
        self.tools = [
            StructuredTool.from_function(
                name="Calculator",
                func=math_tool,
                description="用于数学计算，输入应为可执行的数学表达式"
            ),
            StructuredTool.from_function(
                name="WebSearch",
                func=web_search,
                description="用于实时网络信息检索"
            ),
            StructuredTool.from_function(
                name="TextProcessor",
                func=text_processor,
                description="支持格式：1.文本|操作 2.自然语言指令",
                args_schema=TextProcessorInput
            )
        ]

        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

    def create_agent(self):
        """创建智能体"""
        self.agent = initialize_agent(
            self.tools,
            self.llm,
            agent=self.config["agent_type"],
            memory=self.memory,
            verbose=self.config["verbose"],
            max_iterations=self.config["max_iterations"],
            handle_parsing_errors=True
        )
        return self.agent

    def process_query(self, query: str):
        """增强型查询处理"""
        try:
            # 预处理自然语言指令
            if '转换为大写' in query:
                query = f"处理请求：{query}"
            return self.agent.run(input=query)
        except Exception as e:
            return f"系统错误：{str(e)}"
