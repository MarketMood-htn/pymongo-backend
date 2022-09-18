from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from .models import StockTicker, StockTickerUpdate

router = APIRouter()

@router.post("/", response_description="Create a new stock ticker", status_code=status.HTTP_201_CREATED, response_model=StockTicker)
def create_stock_ticker(request: Request, stock_ticker: StockTicker = Body(...)):
    stock_ticker = jsonable_encoder(stock_ticker)
    new_stock_ticker = request.app.database["stock tickers"].insert_one(stock_ticker)
    created_book = request.app.database["stock tickers"].find_one(
        {"_id": new_stock_ticker.inserted_id}
    )

    return created_book

@router.get("/", response_description="List all stock tickers", response_model=List[StockTicker])
def list_stock_tickers(request: Request):
    stock_tickers = list(request.app.database["stock tickers"].find(limit=100))
    return stock_tickers

@router.get("/{id}", response_description="Get a single stock_ticker by id", response_model=StockTicker)
def find_stock_ticker(id: str, request: Request):
    if (StockTicker := request.app.database["stock tickers"].find_one({"_id": id})) is not None:
        return StockTicker
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"StockTicker with ID {id} not found")

@router.put("/{id}", response_description="Update a stock ticker", response_model=StockTicker)
def update_stock_ticker(id: str, request: Request, stock_ticker: StockTickerUpdate = Body(...)):
    stock_ticker = {k: v for k, v in stock_ticker.dict().items() if v is not None}
    if len(stock_ticker) >= 1:
        update_result = request.app.database["stock ticker"].update_one(
            {"_id": id}, {"$set": stock_ticker}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"StockTicker with ID {id} not found")

    if (
        existing_stock_ticker := request.app.database["stock tickers"].find_one({"_id": id})
    ) is not None:
        return existing_stock_ticker

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"StockTicker with ID {id} not found")

@router.delete("/{id}", response_description="Delete a stock_ticker")
def delete_stock_ticker(id: str, request: Request, response: Response):
    delete_result = request.app.database["stock_tickers"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"StockTicker with ID {id} not found")