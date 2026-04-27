from src.db.items import Item
from pydantic import BaseModel

class ItemResponseModel(Item):
    # this is used to validate response when getting items
    pass

class ItemCreateModel(BaseModel):
    # this is used to validate request when creating/updating a store item
    id:int
    name:str
    price:float