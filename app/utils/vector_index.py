from llama_index.core import ( VectorStoreIndex, 
                              SimpleDirectoryReader, 
                              Settings
                              )
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from os import getenv

def initialize_index():
  """Initialize vector index
  
  This function configures the embed model and llm model and then 
  loads the data from the data directory. It then sets the vector 
  index and persists the data to the storage directory.
  """
  api_key = getenv("GROQ_API_KEY")

  if not api_key:
    raise RuntimeError("Api key not set in environment variables")

  # load data
  documents = SimpleDirectoryReader("data").load_data()

  # Set LLM and embedding model
  Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
  Settings.llm = Groq(model="llama3-70b-8192", api_key=api_key)

  # Set vector index and persist data
  vector_index = VectorStoreIndex.from_documents(documents)
  vector_index.storage_context.persist("storage")
