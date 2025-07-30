# EndToEnd Haystack FastAPI QA System

A powerful Question-Answering system built with Haystack and FastAPI that uses Retrieval-Augmented Generation (RAG) to answer questions based on PDF documents. The system ingests PDF documents, creates embeddings, stores them in Pinecone vector database, and provides a web interface for querying.

## 🚀 Features

- **PDF Document Ingestion**: Automatically processes and splits PDF documents
- **Vector Storage**: Uses Pinecone for efficient similarity search
- **RAG Pipeline**: Combines document retrieval with language generation
- **Web Interface**: FastAPI-based web application with HTML templates
- **Real-time Q&A**: Interactive question-answering interface
- **Modular Architecture**: Clean separation of concerns with dedicated modules

## 🛠️ Tech Stack

### Backend Framework
- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications

### AI/ML Components
- **Haystack**: Open-source framework for building search systems
- **Sentence Transformers**: For generating document and query embeddings
- **HuggingFace API**: Language model integration for text generation
- **PyPDF**: PDF document processing and text extraction

### Vector Database
- **Pinecone**: Cloud-based vector database for similarity search

### Frontend
- **Jinja2 Templates**: Server-side templating for HTML rendering
- **HTML/CSS**: Simple web interface

### Development Tools
- **Python-dotenv**: Environment variable management
- **Pathlib**: Modern file path handling

## 🔍 How It Works

### 1. Document Ingestion Pipeline
- **PDF Conversion**: Converts PDF documents to text using PyPDF
- **Text Splitting**: Splits documents into chunks of 200 words
- **Embedding Generation**: Creates vector embeddings using SentenceTransformers
- **Vector Storage**: Stores embeddings in Pinecone with metadata

### 2. Question-Answering Pipeline
- **Query Embedding**: Converts user questions to vector embeddings
- **Similarity Search**: Retrieves relevant document chunks from Pinecone
- **Context Building**: Constructs prompts with retrieved documents
- **Answer Generation**: Uses HuggingFace models to generate answers

### 3. Web Interface
- **Question Input**: Simple form for entering questions
- **Real-time Processing**: Processes questions through the RAG pipeline
- **Answer Display**: Shows generated answers with context

## 📊 System Architecture

```
User Question → FastAPI → Embedding → Pinecone → Retrieved Docs → LLM → Answer
                    ↓
              Web Interface
```

