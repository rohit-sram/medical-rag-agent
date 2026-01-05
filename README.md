# Medical-RAG-agent

# HOW TO RUN?
### STEPS:

Clone the repository

```bash
git clone https://github.com/rohit-sram/medical-rag-agent.git
```

### STEP 01- Install uv [package manager] and and initialize project create a venv.

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


### STEP 02- install the requirements
```bash
uv add -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows: