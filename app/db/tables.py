"""Defined database tables and underling relationships."""
from sqlmodel import Relationship, Field

from app.models import core

class Shopping(core.ShoppingList, table=True):
    
    id: int | None = Field(default=None, primary_key=True)
    items: list["ItemInstance"] = Relationship(back_populates="shopping")

class ItemInstance(core.ItemInstance, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    shopping_id: int = Field(default=None, foreign_key="shopping.id")
    item_id: int = Field(default=None, foreign_key="item.id")
    shopping: Shopping = Relationship(back_populates="items")  # pyright: ignore[reportAny]
    item: "Item" = Relationship(back_populates="items")  # pyright: ignore[reportAny]

class Item(core.Item, table=True):
    id: int | None = Field(default=None, primary_key=True)
    items: list["ItemInstance"] = Relationship(back_populates="item")
