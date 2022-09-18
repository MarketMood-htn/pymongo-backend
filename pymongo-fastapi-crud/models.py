import uuid
from typing import Optional, List
from pydantic import BaseModel, Field

class Article(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    link: str = Field(...)
    pos: float = Field(...)
    neu: float = Field(...)
    neg: float = Field(...)
    prediction: str = Field(...)
    date: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6a",
                "title": "Stock News",
                "link": "https://docs.python.org/3/library/datetime.html",
                "pos": 50,
                "neu": 50,
                "neg": 0,
                "prediction": "unknown",
                "date": "today"
            }
        }

class StockTicker(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    all_articles: List[Article] = Field(...)
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6c",
                "all_articles": [
                    {
                        "_id": "066de609-b04a-4b30-b46c-32537c7f1f6a",
                        "title": "Stock News",
                        "link": "https://docs.python.org/3/library/datetime.html",
                        "pos": 50,
                        "neu": 50,
                        "neg": 0,
                        "date": "today"
                    },
                    {
                        "_id": "066de609-b04a-4b30-b46c-32537c7f1f6f",
                        "title": "Other News",
                        "link": "https://google.com",
                        "pos": 0,
                        "neu": 50,
                        "neg": 50,
                        "date": "yesterday"
                    }
                ]
            }
        }

class StockTickerUpdate(BaseModel):
    all_articles: Optional[List[Article]]
    class Config:
        schema_extra = {
            "example": {
                "all_articles": [
                    {
                        "_id": "066de609-b04a-4b30-b46c-32537c7f1f6a",
                        "title": "Stock News",
                        "link": "https://docs.python.org/3/library/datetime.html",
                        "pos": 60,
                        "neu": 40,
                        "neg": 0,
                        "prediction": "unknown",
                        "date": "today"
                    },
                    {
                        "title": "Other News",
                        "link": "https://google.com",
                        "pos": 0,
                        "neu": 40,
                        "neg": 60,
                        "prediction": "unknown",
                        "date": "yesterday"
                    }
                ]
            }
        }

class Stock(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    ticker: StockTicker = Field(...)
    price: float = Field(...)
    dateUpdated: str = Field(...)
    name: str = Field(...)
    abbreviation: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6b",
                "ticker": {
                    "_id": "066de609-b04a-4b30-b46c-32537c7f1f6c",
                    "all_articles": [
                        {
                            "_id": "066de609-b04a-4b30-b46c-32537c7f1f6a",
                            "title": "Stock News",
                            "link": "https://docs.python.org/3/library/datetime.html",
                            "pos": 50,
                            "neu": 50,
                            "neg": 0,
                            "prediction": "unknown",
                            "date": "today"
                        },
                        {
                            "_id": "066de609-b04a-4b30-b46c-32537c7f1f6f",
                            "title": "Other News",
                            "link": "https://google.com",
                            "pos": 0,
                            "neu": 50,
                            "neg": 50,
                            "prediction": "unknown",
                            "date": "yesterday"
                        }
                    ]
                },
                "price": 100.0,
                "dateUpdated": "Sept 17 2022",
                "name": "Apple",
                "abbreviation": "APPL"
            }
        }

class StockUpdate(BaseModel):
    ticker: Optional[StockTicker]
    price: Optional[float]
    dateUpdated: Optional[str]
    name: Optional[str]
    abbreviation: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "price": 110.0,
                "dateUpdated": "Sept 18 2022",
            }
        }

class ArticleUpdate(BaseModel):
    title: Optional[str]
    link: Optional[str]
    pos: Optional[float]
    neu: Optional[float]
    neg: Optional[float]
    prediction: Optional[str]
    date: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "pos": 60,
                "neu": 40,
            }
        }

class Book(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    author: str = Field(...)
    synopsis: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "..."
            }
        }

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "Don Quixote is a Spanish novel by Miguel de Cervantes..."
            }
        }