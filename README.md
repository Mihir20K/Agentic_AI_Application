# AI Agents for Stock Analysis & PDF Assistant

Two AI-powered agents for financial analysis and PDF document interaction using OpenAI/Groq models.

## Features

- **Stock Analysis Agent**
  - Real-time stock price tracking
  - Analyst recommendations summary
  - Company news aggregation
  - Multi-agent collaboration system

- **PDF Assistant**
  - PDF content extraction
  - Semantic search using vector embeddings
  - PostgreSQL-backed knowledge base
  - OpenAI/Groq LLM integration

## Installation


1. **Set Up Environment**
python -m venv .venv



2. **Install Dependencies**
pip install -r requirements.txt



## Configuration

1. **Environment Variables** (`.env`)

OPENAI_API_KEY=sk-your-key-here

GROQ_API_KEY=gsk-your-key-here

DB_URL=postgresql+psycopg://ai:ai@localhost:5532/ai


2. **Database Setup** (Docker)
   
docker run -d

-e POSTGRES_DB=ai

-e POSTGRES_USER=ai

-e POSTGRES_PASSWORD=ai

-p 5532:5432

--name pgvector

phidata/pgvector:16



## Usage

### Stock Analysis Agent
python playground.py


### PDF Assistant
python pdf_assistant.py



## Troubleshooting

**Q: Getting OpenAI quota errors with new account?**
1. Verify payment method added
2. Check API key validity
3. Test with smaller PDF first
4. Wait 48h after account activation

**Q: Hugging Face model not working?**
Switch to OpenAI embeddings in pdf_assistant.py
from phi.embedder.openai import OpenAIEmbedder
embedder = OpenAIEmbedder(model="text-embedding-3-small")
