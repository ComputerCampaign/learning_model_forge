# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/10 17:10
  file:  tools
  Description :
-------------------------------------------------
"""
import math
import requests
from pydantic import BaseModel


class TextProcessorInput(BaseModel):
    text: str
    operation: str


def math_tool(query: str):
    """数学计算工具"""
    try:
        return str(eval(query))
    except:
        return "无效的数学表达式"


def web_search(query: str):
    """网络搜索工具"""
    try:
        response = requests.get(
            "http://api.duckduckgo.com",
            params={"q": query, "format": "json"}
        )
        return response.json().get('Abstract', '未找到相关信息')
    except Exception as e:
        return f"搜索失败：{str(e)}"


def text_processor(params: str | dict):
    """智能文本处理工具"""
    try:
        # 自动检测输入类型
        if isinstance(params, dict):
            text = params.get('text', '')
            operation = params.get('operation', '')
        elif '|' in params:
            text, operation = params.split('|', 1)
        else:
            # 处理自然语言指令
            if '大写' in params:
                text = params.replace('转换为大写', '').strip("' ")
                operation = 'upper'
            elif '反转' in params:
                text = params.replace('反转', '').strip("' ")
                operation = 'reverse'
            elif '长度' in params:
                text = params.replace('计算长度', '').strip("' ")
                operation = 'length'
            else:
                return "无法解析指令"

        operations = {
            "length": len,
            "reverse": lambda x: x,
            "upper": str.upper
        }

        func = operations.get(operation.lower())
        if not func:
            return f"不支持的操作：{operation}"

        return str(func(text.strip("'")))
    except Exception as e:
        return f"处理错误：{str(e)}"
