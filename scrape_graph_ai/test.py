# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/9 16:09
  file:  test
  Description :
-------------------------------------------------
"""
# from langchain_text_splitters import RecursiveCharacterTextSplitter
#
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=512,
#     chunk_overlap=64
# )
# print(text_splitter.split_text("长文本示例..."))

import chromadb

client = chromadb.PersistentClient(path="/tmp/chroma_db")
print(client.list_collections())
