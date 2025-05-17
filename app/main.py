from fastapi import FastAPI
from routes.query import query_router
from lifespan import lifespan

app = FastAPI(
    title="FastAPI + llamaIndex Technical Test API",
    lifespan=lifespan
    )

app.include_router(query_router)

@app.get("/")
def root():
    return {"message": "This is a FastAPI + llamaIndex technical Test API."}