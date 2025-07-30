from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.converters import PyPDFToDocument
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from pathlib import Path
import os
from dotenv import load_dotenv
from QA_System.utils import pinecone_config

def ingest(document_store):
    
    indexing = Pipeline()
    indexing.add_component("converter", PyPDFToDocument())
    indexing.add_component("splitter", DocumentSplitter(split_by="word", split_length=200))
    indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
    indexing.add_component("writer", DocumentWriter(document_store))

    indexing.connect("converter", "splitter")
    indexing.connect("splitter", "embedder")
    indexing.connect("embedder", "writer")

    # Get all PDF files from the data directory
    data_path = Path(r"C:\Users\csing\VSCode\Projects\EndToEnd_Haystack_FastAPI\data")
    pdf_files = list(data_path.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in the data directory")
        return
    
    indexing.run({"converter": {"sources": pdf_files}})

if __name__ == "__main__":

    document_store = pinecone_config()
    ingest(document_store)