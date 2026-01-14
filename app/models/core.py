"""Defines underlying data structures of database models."""
from sqlmodel import JSON, Column, Field, SQLModel

class ShoppingList(SQLModel):
    name: str

class Quantity(SQLModel):
    amount: float 
    unit: str

class ItemInstance(SQLModel):
    checked: bool | None = Field(False)
    quantity: Quantity | None = Field(default=None, sa_column=Column(JSON))

class Item(SQLModel):
    name: str
