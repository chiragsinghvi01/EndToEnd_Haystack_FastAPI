from haystack import Pipeline
from haystack.utils import Secret
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack.components.builders import PromptBuilder
from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
from haystack.components.generators import HuggingFaceAPIGenerator
import os
from dotenv import load_dotenv

def get_result():
    pass

if __name__ == "__main__":
    get_result()