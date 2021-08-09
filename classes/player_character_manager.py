from classes.game import Person
from classes.magic import SpellList
from classes.inventory import ItemManager
from copy import deepcopy
import random


class PlayerCharacterManager:

    def __init__(self):

        self.spellList = SpellList()
        self.item_manager = ItemManager()

        mage_magic = [self.spellList.fire, self.spellList.thunder, self.spellList.blizzard, self.spellList.quake]
        alchemist_magic = [self.spellList.fire, self.spellList.thunder, self.spellList.blizzard, self.spellList.cure]
        arch_mage_magic = [self.spellList.fire, self.spellList.thunder, self.spellList.blizzard, self.spellList.quake,
                     self.spellList.meteor]

        mage_items = [self.item_manager.create_item(self.item_manager.potion, 5),
                         self.item_manager.create_item(self.item_manager.highPotion, 3),
                      self.item_manager.create_item(self.item_manager.superPotion, 1)]

        robot_items = [self.item_manager.create_item(self.item_manager.potion, 7),
                         self.item_manager.create_item(self.item_manager.highPotion, 5)]

        alchemist_items = [self.item_manager.create_item(self.item_manager.potion, 14),
                         self.item_manager.create_item(self.item_manager.highPotion, 12),
                         self.item_manager.create_item(self.item_manager.superPotion, 10),
                         self.item_manager.create_item(self.item_manager.elixir, 5),
                           self.item_manager.create_item(self.item_manager.grenade, 20)]

        archmage_items = [self.item_manager.create_item(self.item_manager.potion, 5),
                         self.item_manager.create_item(self.item_manager.highPotion, 3)]

        self.list_Of_heroes = [
        Person("Mage     ", 5000, 150, 250, 100, mage_magic, mage_items),
        Person("Robot    ", 10000, 1, 800, 800, [], robot_items),
        Person("Alchemist", 7000, 100, 500, 300, alchemist_magic, alchemist_items),
        Person("ArchMage ", 4000, 240, 200, 80, arch_mage_magic, archmage_items)
        ]

    def create_Players_list(self):

        # Hero magic and Inventory
        HeroMagic = [self.spellList.fire, self.spellList.thunder, self.spellList.blizzard, self.spellList.quake,
                     self.spellList.meteor, self.spellList.cure, self.spellList.cura]

        HeroInventory = [self.item_manager.create_item(self.item_manager.potion, 10),
                         self.item_manager.create_item(self.item_manager.highPotion, 5),
                         self.item_manager.create_item(self.item_manager.superPotion, 3),
                         self.item_manager.create_item(self.item_manager.elixir, 2),
                         self.item_manager.create_item(self.item_manager.megaElixir, 1),
                         self.item_manager.create_item(self.item_manager.megaElixir, 3)]

        number_of_heroes = random.randrange(2, 5)
        players = [Person("Hero     ", 10000, 120, 700, 300, HeroMagic, HeroInventory)]

        for i in range(0, number_of_heroes):
            random_hero_number = random.randrange(0, len(self.list_Of_heroes))
            hero = self.list_Of_heroes[random_hero_number]
            new_hero = deepcopy(hero)
            players.append(new_hero)

        return players




