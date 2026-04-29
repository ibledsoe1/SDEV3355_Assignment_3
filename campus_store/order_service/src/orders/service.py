from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.orders import Order
from .schemas import OrderCreateModel
from sqlmodel import select


class OrderService:
    # this provides the methods to do create, read, delete methods
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_all_orders(self):
        statement = select(Order).order_by(Order.id)
        result = await self.session.exec(statement)
        return result.all()
    
    async def create_order(self, order_create_data: OrderCreateModel):
        new_order = Order(**order_create_data.model_dump())
        self.session.add(new_order)
        await self.session.commit()
        return new_order

    async def delete_order(self, order_id):
        statement = select(Order).where(Order.id == order_id)
        result = await self.session.exec(statement)
        order = result.first()
        await self.session.delete(order)
        await self.session.commit()
