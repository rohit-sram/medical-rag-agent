from dotenv import load_dotenv
import os
from src.helper import load_pdf_files, filter_docs, chunk_text, load_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec 
from langchain_pinecone import PineconeVectorStore

load_dotenv()
vec_dims = 384    # from trials

PINECONE_API_KEY = pc_api_key = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Loading, Filtering, and chunking data
extracted_data = load_pdf_files(data='data/')
min_docs = filter_docs(extracted_data)
text_chunks = chunk_text(min_docs)
embeddings = load_embeddings()

pc = Pinecone(api_key=pc_api_key)
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# create index for Pinecone (vector DB) - running on cloud
index_name = "medical-agent"

if not pc.has_index(index_name):
  pc.create_index(
    name=index_name,
    dimension=vec_dims,   # len of vector embed.
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1")
  )
  
index = pc.Index(index_name)

# RAG from pinecone index
doc_search = PineconeVectorStore.from_documents(
  documents=text_chunks,
  embedding=embeddings,
  index_name=index_name
)