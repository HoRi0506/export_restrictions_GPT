from pydantic import BaseModel


class esSearchResult(BaseModel):
    query: str
    text: str


class Query(BaseModel):
    text: str


class Item(BaseModel):
    name: str