from sqlmodel import SQLModel, Field,Column
import sqlalchemy.dialects.postgresql as pg

class Item(SQLModel, table = True):
    __tablename__ = 'items'
    __table_args__ = {'extend_existing': True}
    id:int | None = Field(default=None, primary_key=True)
    name:str
    price:float    