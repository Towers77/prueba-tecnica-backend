from fastapi import APIRouter, HTTPException, status, logger
from llama_index.core import StorageContext, load_index_from_storage
from DTO.get_query_dto import GetQueryDTO

query_router = APIRouter()

@query_router.get("/query")
def get_query(q: str) -> GetQueryDTO:
  """Respond to a given query with llamaIndex.
  
  This endpoint takes a query string as input and returns a response based on the
  data indexed from the data dir to the storage dir.
  """
  if not q.strip():
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                          detail="Query cannot be empty")
  
  try:
      storage = StorageContext.from_defaults(persist_dir="storage")
      query_engine = load_index_from_storage(storage).as_query_engine()
      resp = query_engine.query(q)
      return GetQueryDTO(res=resp.response)
  except Exception as e:
      logger.error(f"Error processing query: {e}")
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                          detail="Internal Server Error")