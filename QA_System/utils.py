from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

print("Pinecone API Key set successfully.")

def pinecone_config():
    document_store = PineconeDocumentStore(
        index_name="default",
        namespace="default",
        dimension=768,
    )
    return document_store