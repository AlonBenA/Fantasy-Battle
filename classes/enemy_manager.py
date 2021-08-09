from classes.game import Person
from classes.magic import SpellList
from classes.inventory import ItemManager
from copy import deepcopy
import random


class EnemyManager:

    def __init__(self):

        self.spellList = SpellList()
        self.item_manager = ItemManager()

        self.list_Of_Bosses = [
            Person("Priest       ", 30000, 360, 600, 300, [self.spellList.cure, self.spellList.cura,
                                                     self.spellList.fire, self.spellList.thunder,
                                                     self.spellList.blizzard],
                                                     [self.item_manager.create_item(self.item_manager.potion, 5)]),

            Person("barbarian    ", 50000, 0, 1500, 100, [],
                   [self.item_manager.create_item(self.item_manager.potion, 5),
                    self.item_manager.create_item(self.item_manager.highPotion , 3),
                    self.item_manager.create_item(self.item_manager.superPotion, 1)]),
            Person("Evil Wizard  ", 18000, 600, 200, 100, [self.spellList.fire, self.spellList.thunder,
                                                          self.spellList.blizzard,  self.spellList.quake,
                                                          self.spellList.meteor],
                   [self.item_manager.create_item(self.item_manager.potion, 5)]),
            Person("Boss         ", 25000, 120, 750, 200, [self.spellList.fire, self.spellList.thunder,
                                                        self.spellList.blizzard,  self.spellList.quake],
                   [self.item_manager.create_item(self.item_manager.potion, 5),
                    self.item_manager.create_item(self.item_manager.highPotion, 3),
                    self.item_manager.create_item(self.item_manager.superPotion, 1)]
                   ),
        ]

        self.list_of_minions = [
            Person("Pain         ", 3000, 1, 501, 50, [], []),
            Person("Panic        ", 3200, 1, 404, 45, [], []),
            Person("Magi         ", 2000, 100, 100, 30, [self.spellList.fire, self.spellList.thunder], []),
            Person("Super Magi   ", 1500, 200, 50, 20, [self.spellList.fire, self.spellList.meteor], []),
            Person("Tank         ", 3500, 1, 305, 600, [], []),
            Person("Evil Cleric  ", 3200, 100, 305, 400, [self.spellList.cure], []),
            Person("MegaE Cleric ", 4000, 180, 305, 400, [self.spellList.cure, self.spellList.cura], []),
            Person("Evil Cleric  ", 3200, 100, 305, 400, [self.spellList.cure], []),
        ]

    def create_enemy_list(self):
        number_of_bosses = random.randrange(0, 2)
        number_of_minions = random.randrange(2, 5)
        enemies = []

        super_hard_mod = random.randrange(0, 101)

        if super_hard_mod > 95:
            return self.super_hard_mod_time()
        else:
            for i in range(0, number_of_bosses):
                random_boss_number = random.randrange(0, len(self.list_Of_Bosses))
                boss = self.list_Of_Bosses[random_boss_number]
                new_boss = deepcopy(boss)
                enemies.append(new_boss)

            for i in range(0, number_of_minions):
                random_minion_number = random.randrange(0, len(self.list_of_minions))
                minion = self.list_of_minions[random_minion_number]
                new_minion = deepcopy(minion)
                enemies.append(new_minion)

            return enemies

    def super_hard_mod_time(self):
        enemies = []
        for i in range(0,len(self.list_Of_Bosses)):
            boss = self.list_Of_Bosses[i]
            new_boss = deepcopy(boss)
            enemies.append(new_boss)
        return enemies
