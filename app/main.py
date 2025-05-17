from fastapi import FastAPI, HTTPException, status, logger, Depends

from llama_index.core import StorageContext, load_index_from_storage

from DTO.get_query_dto import GetQueryDTO
from lifespan import lifespan

app = FastAPI(lifespan=lifespan)

@app.get("/query")
def get_query(q: str) -> GetQueryDTO:

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