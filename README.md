# Medical-RAG-agent

### Steps:
Clone the repository

```bash
git clone https://github.com/rohit-sram/medical-rag-agent.git
```

### STEP 01 - Install uv [package manager] and and initialize project create a venv.

```bash
uv init .
uv venv <NAME_OF_VENV>
```

```bash
source .venv/bin/activate
```

<!-- ```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
``` -->


### STEP 02 — Install dependencies

```bash
uv add -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

### Required (always)

```ini
PINECONE_API_KEY=<YOUR_PINECONE_API_KEY>
```

### Optional (only if using OpenAI)

```ini
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```

> **Note:** If you are using Ollama (local models), you do **NOT** need an OpenAI API key.

---

## Option 1 — ChatOllama (Recommended: Free & Local)

### Requirements

* Ollama installed locally
  👉 [https://ollama.com](https://ollama.com)

Ensure the Ollama server is running:

```bash
ollama serve
```

### Pull a supported model

Recommended lightweight RAG model:

```bash
ollama pull nemotron-mini:latest
```

or,
```bash
ollama pull nemotron-mini:4b
```

### Configure model selection (optional)

You may set the model via environment variable:

```bash
export OLLAMA_MODEL="nemotron-mini:latest"
```


### Usage in code (already integrated)

The application uses:

```python
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="nemotron-mini:latest",
    temperature=0
)
```

### Pros & Cons

* ✅ No API key
* ✅ No billing
* ✅ No personal data required
* ✅ Unlimited local usage

* ❌ Hardware-bound
---

## Option 2 — ChatOpenAI (Cloud, Paid)

### Requirements

* OpenAI account
* Valid API key with available credits

Add to `.env`:

```ini
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```

### Usage in code

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)
```

### Notes

* Subject to rate limits and quota
* Requires active billing
* Higher reasoning quality than small local models

---

## Vector Database Setup (Pinecone)

Before running the app, push embeddings to Pinecone:

```bash
python push_index.py
```

This step:

* Loads PDFs
* Chunks text
* Generates embeddings
* Uploads vectors to Pinecone

---

## Start the Application

```bash
python app.py
```

Open your browser and navigate to:

```
http://localhost:8080
```
### Techstack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone

AWS Generated URI - 211125561250.dkr.ecr.us-east-1.amazonaws.com/medicalagent