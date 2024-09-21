from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
from llama_index.core import StorageContext,load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter


import sys
from exception import customexeption
from logger import logging

def download_gemini_embedding(model,document):
    try:
        logging.info("")
        gemini_embed_model = GeminiEmbedding(model_name = "models/embedding-001")
        Settings.llm =  model
        Settings.embed_model = gemini_embed_model
        Settings.node_parser = SentenceSplitter(chunk_size=800, chunk_overlap=20)

        logging.infp("")
        index = VectorStoreIndex.from_documents(document,service_context=Settings)
        index.storage_context.persist()

        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexeption(e,sys) 