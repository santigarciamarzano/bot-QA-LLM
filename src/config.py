import os

# Configuración
PDF_PATH = "computer.pdf"
PERSIST_DIRECTORY = os.path.join(os.getcwd(), "chroma_embeddings")
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL_NAME = "google/flan-t5-large"
