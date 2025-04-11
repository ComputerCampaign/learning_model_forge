# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/10 14:51
  file:  rag_core.py
  Description :
-------------------------------------------------
"""
import logging
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class SimpleRAG:
    def __init__(self, config):
        self.config = config
        self.llm = None
        self.embeddings = None

    def initialize_models(self):
        """初始化模型"""
        logging.info("Initializing models...")
        self.llm = Ollama(
            model=self.config["llm_model"],
            base_url=self.config["base_url"]
        )
        self.embeddings = OllamaEmbeddings(
            model=self.config["embed_model"],
            base_url=self.config["base_url"]
        )

    def load_documents(self, file_path):
        """加载文档"""
        try:
            loader = TextLoader(file_path)
            docs = loader.load()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.config["chunk_size"],
                chunk_overlap=self.config["chunk_overlap"]
            )
            return splitter.split_documents(docs)
        except Exception as e:
            logging.error(f"文档加载失败: {str(e)}")
            raise

    def create_vector_store(self, documents):
        """创建向量数据库"""
        logging.info("Creating vector store...")
        return FAISS.from_documents(
            documents=documents,
            embedding=self.embeddings
        )

    def ask(self, vector_store, question):
        """执行问答"""
        context = vector_store.similarity_search(question, k=2)
        prompt = f"请根据以下上下文回答：\n{context[0].page_content}\n\n问题：{question}\n回答："
        return self.llm(prompt)
