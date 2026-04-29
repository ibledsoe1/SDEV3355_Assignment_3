# Order API endpoints
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from src.db.main import get_session
from http import HTTPStatus
from .service import OrderService
from .schemas import OrderCreateModel, OrderResponseModel

order_router = APIRouter()

@order_router.post("/orders", status_code=HTTPStatus.CREATED)
async def place_order(order_create_data: OrderCreateModel, session: AsyncSession = Depends(get_session)):
    new_order = await OrderService(session).create_order(order_create_data)
    return new_order

@order_router.get("/orders", response_model=List[OrderResponseModel])
async def get_orders(session: AsyncSession = Depends(get_session)):
    orders = await OrderService(session).get_all_orders()
    return orders

@order_router.delete("/orders/{order_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_order(order_id: int, session: AsyncSession = Depends(get_session)):
    await OrderService(session).delete_order(order_id)
    return{}