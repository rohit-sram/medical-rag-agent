from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List
from langchain_core.documents import Document


# Step 1 - Extract Data From the PDF File
def load_pdf_files(data):
  loader = DirectoryLoader(
    data,
    glob="*.pdf",
    loader_cls=PyPDFLoader
  )
  docs = loader.load()
  
  return docs


## Step 2 - Exrtract data from doc/source
def filter_docs(docs: List[Document]) -> List[Document]:
  """
  Given a list of Document objects, return a new list of Document objects
  containing only 'source' in metadata and the original page_content.
  """
  min_docs: List[Document] = []
  for doc in docs:
    src = doc.metadata.get("source")
    min_docs.append(
      Document(
        page_content=doc.page_content,
        metadata={"source": src}
      )
    )
    
  return min_docs


## Step 3 - Chunking
def chunk_text(docs):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=20, 
    length_function=len
  )
  
  text_chunks = text_splitter.split_documents(docs)
  return text_chunks



# Download Embeddings from HuggingFace 
def load_embeddings():
  """
  Download and return the HuggingFace embeddings model.
  """
  model_name = "sentence-transformers/all-MiniLM-L6-v2"
  embedding = HuggingFaceEmbeddings(
      model_name=model_name
  )
  return embedding