# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/10 14:51
  file:  main
  Description :
-------------------------------------------------
"""
from rag_core import SimpleRAG
from config import CONFIG


def main():
    # 初始化系统
    rag = SimpleRAG(CONFIG)
    rag.initialize_models()

    # 加载文档
    documents = rag.load_documents("data/sample.txt")

    # 创建向量库
    vector_store = rag.create_vector_store(documents)

    # 交互问答
    while True:
        question = input("\n请输入问题（输入q退出）：")
        if question.lower() == 'q':
            break
        answer = rag.ask(vector_store, question)
        print(f"\n答案：{answer}")


if __name__ == "__main__":
    main()
