# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/10 17:10
  file:  main
  Description :
-------------------------------------------------
"""
from agent_core import AgentSystem


def main():
    system = AgentSystem()
    system.initialize_models()
    system.create_agent()

    # 定义完整的测试用例集
    test_queries = [
        # 数学计算测试
        "3的平方加上4的立方是多少？",
        "计算15除以(7-4)*2的结果",

        # 网络搜索测试
        "搜索OpenAI最新发布的模型",
        "查询巴黎今天的天气",

        # 文本处理测试（自然语言格式）
        "把'hello world'转换为大写",
        "计算'langchain'这个字符串的长度",
        "反转'abcdefg'这个字符串",

        # 结构化格式测试
        "hello world | upper",
        "langchain | length",
        "abcdefg | reverse",

        # 错误处理测试
        "无效的数学表达式：5 + * 3",
        "搜索不存在的特殊关键词：ASDFGHJKL",
        "处理无效指令：把123转换成二进制"
    ]

    print("【开始Agent测试】\n")
    for i, query in enumerate(test_queries, 1):
        print(f"测试用例 {i}/12")
        print(f"输入：{query}")
        response = system.process_query(query)
        print(f"输出：{response}")
        print("-" * 60)

    print("\n【测试完成】")


if __name__ == "__main__":
    main()
