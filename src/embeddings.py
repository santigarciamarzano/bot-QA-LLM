from langchain.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import os

def create_and_persist_embeddings(fragmentos, persist_directory, embedding_model_name="sentence-transformers/all-MiniLM-L6-v2"):
    os.makedirs(persist_directory, exist_ok=True)
    hf_embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

    vectordb = Chroma.from_texts(
        texts=[fragment.page_content for fragment in fragmentos],
        embedding=hf_embeddings,
        persist_directory=persist_directory
    )
    vectordb.persist()
    print(f"Embeddings guardados en: {persist_directory}")
    return vectordb

def load_embeddings(persist_directory, embedding_model_name="sentence-transformers/all-MiniLM-L6-v2"):
    hf_embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=hf_embeddings
    )
    return vectordb
