from haystack import Pipeline
from haystack.utils import Secret
from haystack.utils.hf import HFGenerationAPIType
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.builders import ChatPromptBuilder
from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
from haystack.components.generators.chat import HuggingFaceAPIChatGenerator
from haystack.dataclasses import ChatMessage
from QA_System.utils import pinecone_config
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

prompt_template = [ChatMessage.from_user('''
You are a helpful AI assistant. Based on the provided documents, answer the question clearly and concisely.
Documents:
{% for doc in documents %}
{{ doc.content }}
{% endfor %}
Question: {{query}}
Please provide a clear, direct answer based on the information in the documents. If the documents don't contain relevant information to answer the question, say "I don't have enough relevant information to answer this question."
Answer:
''')]

pipeline = None

def get_pipeline():
    global pipeline
    if pipeline is None:
        pipeline = Pipeline()
        
        pipeline.add_component("embedder", SentenceTransformersTextEmbedder(progress_bar=False))
        pipeline.add_component("retriever", PineconeEmbeddingRetriever(
            document_store=pinecone_config(), top_k=2))
        pipeline.add_component("prompt_builder", ChatPromptBuilder(
            template=prompt_template, required_variables=["documents", "query"]))
        pipeline.add_component("llm", HuggingFaceAPIChatGenerator(
            api_type=HFGenerationAPIType.SERVERLESS_INFERENCE_API,
            api_params={"model": "HuggingFaceH4/zephyr-7b-beta"},
            token=Secret.from_env_var("HF_API_TOKEN")))
        
        pipeline.connect("embedder", "retriever")
        pipeline.connect("retriever", "prompt_builder.documents")
        pipeline.connect("prompt_builder.prompt", "llm.messages")

    return pipeline

def get_result(query):
    try:
        results = get_pipeline().run({
            "embedder": {"text": query},
            "prompt_builder": {"query": query}
        })
        return results["llm"]["replies"][0].text
    except:
        return None
    
# Test with hardcoded question
if __name__ == "__main__":
    test_question = "What is RAG token?"
    print(f"Question: {test_question}")
    answer = get_result(test_question)
    if answer:
        print(f"Answer: {answer}")
    else:
        print("No answer generated")