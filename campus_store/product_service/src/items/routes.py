# Item API endpoints
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from ..db.main import get_session
from http import HTTPStatus
from .service import ItemService
from .schemas import ItemCreateModel, ItemResponseModel

item_router = APIRouter()

@item_router.get("/")
def home():
    return {"message":"Welcome to the campus store website"}

@item_router.post("/items", status_code=HTTPStatus.CREATED)
async def add_product(item_create_data: ItemCreateModel, session: AsyncSession = Depends(get_session)):
    new_item = await ItemService(session).create_item(item_create_data)
    return new_item

@item_router.get("/items", response_model=List[ItemResponseModel])
async def get_products(session: AsyncSession = Depends(get_session)):
    items = await ItemService(session).get_all_items()
    return items

@item_router.delete("/items/{item_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_product(item_id: int, session: AsyncSession = Depends(get_session)):
    await ItemService(session).delete_item(item_id)
    return{}