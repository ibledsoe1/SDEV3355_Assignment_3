from sqlmodel import SQLModel, Field,Column
import sqlalchemy.dialects.postgresql as pg

class Order(SQLModel, table = True):
    __tablename__ = 'orders'
    id:int | None = Field(default=None, primary_key=True)
    item_id:int
    quantity:int