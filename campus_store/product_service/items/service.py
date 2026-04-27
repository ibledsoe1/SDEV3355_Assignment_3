from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.items import Item
from .schemas import ItemCreateModel
from sqlmodel import select


class ItemService:
    # this provides the methods to do create, read, delete methods
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_all_items(self):
        statement = select(Item).order_by(Item.id)
        result = await self.session.exec(statement)
        return result.all()
    
    async def create_item(self, item_create_data: ItemCreateModel):
        new_item = Item(**item_create_data.model_dump())
        self.session.add(new_item)
        await self.session.commit()
        return new_item

    async def delete_item(self, item_id):
        statement = select(Item).where(Item.id == item_id)
        result = await self.session.exec(statement)
        item = result.first()
        await self.session.delete(item)
        await self.session.commit()