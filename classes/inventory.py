class ItemManager:

    def __init__(self):
        # Create Items
        self.potion = Item("Potion", "Potion", "Heal 50 HP", 50)
        self.highPotion = Item("High Potion", "Potion", "Heal 100 HP", 100)
        self.superPotion = Item("super Potion", "Potion", "Heal 500 HP", 500)
        self.elixir = Item("elixir", "elixir", "Fully restores HP and MP of one party member", 99999)
        self.megaElixir = Item("megaElixir", "elixir", "Fully restores party HP and MP", 99999)

        self.grenade = Item("grenade", "attack", "Deals 500 damage", 500)

    def create_item(self, item, amount):
        return {"Item": item, "quantity": amount}


class Item:

    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop



