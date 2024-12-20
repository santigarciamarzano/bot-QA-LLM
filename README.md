# Sistema de Preguntas y Respuestas basado en PDFs

Este proyecto implementa un sistema de preguntas y respuestas basado en archivos PDF. Utiliza el modelo de lenguaje Flan-T5 Large para generar respuestas y el modelo de embeddings sentence-transformers/all-MiniLM-L6-v2 para representar semánticamente los fragmentos de texto.

Estos modelos son configurables, por lo que puedes reemplazarlos por otros modelos de Hugging Face según tus necesidades, simplemente modificando los valores en el archivo src/config.py
---

## **Estructura del Proyecto**
- **src/:**
  - **`embeddings.py`:** Genera y carga embeddings para los fragmentos del PDF.
  - **`model.py`:** Carga el modelo de lenguaje.
  - **`retriever.py`:** Configura el sistema de preguntas y respuestas (QA Chain).
  - **`config.py`:** Archivo de configuración del proyecto.
- **app.py:** Archivo principal que permite interactuar con el sistema desde la terminal.
  - **`config.py`:** Contiene la clave de API utilizada por LangChain para conectarse con modelos de OpenAI. Este archivo está excluido del repositorio mediante `.gitignore` para garantizar la seguridad.
- **main.ipynb:** Notebook para correr las funciones por bloque.  

---

## **Requisitos Previos**
Antes de comenzar, asegúrate de tener instalados los paquetes necesarios. Puedes instalarlos utilizando el archivo requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
---


## **Uso**

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>  
cd <NOMBRE_DEL_REPOSITORIO>  
```
2. Agregar un archivo PDF:

Coloca un archivo PDF que deseas procesar en el mismo directorio donde se encuentra el archivo app.py.

3. Ejecutar la aplicación:
```bash
    python app.py  
```
    Interacción:
    - Ingresa el nombre del archivo PDF (incluye la extensión .pdf).
    - Escribe una pregunta sobre el contenido del PDF.
    - Recibirás la respuesta generada por el sistema y los documentos fuente relacionados.

---

## **Configuración Personalizada**

El comportamiento del sistema puede personalizarse modificando el archivo src/config.py.

**`EMBEDDING_MODEL_NAME`**: Define el modelo de embeddings (por defecto: sentence-transformers/all-MiniLM-L6-v2).
**`LLM_MODEL_NAME`**: Define el modelo de lenguaje (por defecto: google/flan-t5-large).

---

## Notas

    Formato del PDF: Asegúrate de que el archivo PDF sea legible y contenga texto. Archivos con texto escaneado (como imágenes) no funcionarán correctamente.
    Embeddings: Los embeddings generados se guardan en la carpeta chroma_embeddings. Si ya existen embeddings para un PDF, se cargarán automáticamente en lugar de volver a generarlos.

