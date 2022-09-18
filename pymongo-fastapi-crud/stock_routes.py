from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from .models import Stock, StockUpdate

router = APIRouter()

@router.post("/", response_description="Create a new stock", status_code=status.HTTP_201_CREATED, response_model=Stock)
def create_stock(request: Request, stock: Stock = Body(...)):
    stock = jsonable_encoder(stock)
    new_stock = request.app.database["stocks"].insert_one(stock)
    created_book = request.app.database["stocks"].find_one(
        {"_id": new_stock.inserted_id}
    )

    return created_book

@router.get("/", response_description="List all stocks", response_model=List[Stock])
def list_stocks(request: Request):
    stocks = list(request.app.database["stocks"].find(limit=100))
    return stocks

@router.get("/{id}", response_description="Get a single stock by id", response_model=Stock)
def find_stock(id: str, request: Request):
    if (Stock := request.app.database["stocks"].find_one({"_id": id})) is not None:
        return Stock
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock with ID {id} not found")

@router.get("/ticker/{ticker}", response_description="Get a single stock by ticker", response_model=Stock)
def find_stock_by_ticker(ticker: str, request: Request):
    if (Stock := request.app.database["stocks"].find_one({"ticker": ticker})) is not None:
        return Stock
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock with Ticker {ticker} not found")


@router.put("/{id}", response_description="Update a stock", response_model=Stock)
def update_stock(id: str, request: Request, stock: StockUpdate = Body(...)):
    stock = {k: v for k, v in stock.dict().items() if v is not None}
    if len(stock) >= 1:
        update_result = request.app.database["stocks"].update_one(
            {"_id": id}, {"$set": stock}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock with ID {id} not found")

    if (
        existing_stock := request.app.database["stocks"].find_one({"_id": id})
    ) is not None:
        return existing_stock

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock with ID {id} not found")

@router.delete("/{id}", response_description="Delete a stock")
def delete_stock(id: str, request: Request, response: Response):
    delete_result = request.app.database["stocks"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock with ID {id} not found")