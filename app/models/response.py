from app.models import core

class Shopping(core.ShoppingList):
    class ItemInstance(core.ItemInstance):
        item: core.Item
    name: str
    items: list[ItemInstance]
