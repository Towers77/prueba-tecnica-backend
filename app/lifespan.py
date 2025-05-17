from contextlib import asynccontextmanager
from fastapi import FastAPI
from utils.vector_index import initialize_index
from dotenv import load_dotenv

@asynccontextmanager
async def lifespan(app: FastAPI):
  load_dotenv()

  initialize_index()
                        
  yield 