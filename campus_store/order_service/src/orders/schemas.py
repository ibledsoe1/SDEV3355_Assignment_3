from ..db.orders import Order
from pydantic import BaseModel

class OrderResponseModel(Order):
    # this is used to validate response when getting items
    pass

class OrderCreateModel(BaseModel):
    # this is used to validate request when creating/updating a store item
    id:int
    customer_name:str
    address:str
    item_id:int