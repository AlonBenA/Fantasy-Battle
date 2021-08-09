import random

class SpellList:

    def __init__(self):
        # Create Black Magic
        self.fire = Spell("Fire", 10, 1000, "black")
        self.thunder = Spell("Thunder", 13, 1240, "black")
        self.blizzard = Spell("Blizzard", 15, 2000, "black")
        self.quake = Spell("Quake", 20, 2500, "black")
        self.meteor = Spell("Meteor", 60, 9000, "black")

        # Create White Magic
        self.cure = Spell("Cure", 12, 1200, "white")
        self.cura = Spell("Cura", 18, 2000, "white")


class Spell:

    def __init__(self, name, cost, damage, type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type

    def generate_damage(self):
        present = self.damage*0.1
        magic_low = self.damage - present
        magic_high = self.damage + present
        return random.randrange(magic_low, magic_high)


