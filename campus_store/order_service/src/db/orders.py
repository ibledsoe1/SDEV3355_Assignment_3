from sqlmodel import SQLModel, Field,Column
import sqlalchemy.dialects.postgresql as pg

class Order(SQLModel, table = True):
    __tablename__ = 'orders'
    __table_args__ = {'extend_existing': True}
    id:int | None = Field(default=None, primary_key=True)
    customer_name:str
    address:str
    item_id:int