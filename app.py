from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from src.embeddings import create_and_persist_embeddings, load_embeddings
from src.model import load_model
from src.retriever import create_qa_chain
import src.config as config
import os

def main():
    # Solicitar al usuario el nombre del PDF
    pdf_path = input("Ingrese el nombre del archivo PDF (con extensión): ").strip()
    if not os.path.exists(pdf_path):
        print(f"El archivo '{pdf_path}' no existe. Por favor, verifica la ruta.")
        return

    # Actualizar la configuración con el PDF ingresado
    config.PDF_PATH = pdf_path

    # Cargar y procesar el PDF
    print("Procesando el PDF...")
    loader = PyPDFLoader(config.PDF_PATH)
    docs = loader.load()
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=650,
        chunk_overlap=85,
        length_function=len
    )
    fragmentos = splitter.split_documents(docs)

    # Crear o cargar embeddings
    print("Generando embeddings...")
    vectordb = create_and_persist_embeddings(fragmentos, config.PERSIST_DIRECTORY)

    # Cargar el modelo de lenguaje
    print("Cargando el modelo de lenguaje...")
    llm = load_model(config.LLM_MODEL_NAME)

    # Crear el QA Chain
    print("Creando el QA Chain...")
    qa_chain = create_qa_chain(llm, vectordb.as_retriever())

    # Hacer una consulta
    question = input("Ingrese su pregunta: ").strip()
    print("Consultando...")
    result = qa_chain({"query": question})

    # Mostrar resultados
    print("\n--- Respuesta ---")
    print(result["result"])
    print("\n--- Documentos fuente ---")
    for idx, doc in enumerate(result["source_documents"], 1):
        print(f"Documento {idx}: {doc.page_content}")

if __name__ == "__main__":
    main()

