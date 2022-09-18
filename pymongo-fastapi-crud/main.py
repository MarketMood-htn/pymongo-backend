from fastapi import FastAPI
from decouple import config
from pymongo import MongoClient
from .tutorial_routes import router as book_router
from .article_routes import router as article_router
from .stock_routes import router as stock_router
#from .stock_ticker_routes import router as stock_ticker_router

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config("ATLAS_URI"))
    app.database = app.mongodb_client[config("DB_NAME")]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

# app.include_router(book_router, tags=["books"], prefix="/book")
app.include_router(article_router, tags=["articles"], prefix="/article")
app.include_router(stock_router, tags=["stocks"], prefix="/stock")
