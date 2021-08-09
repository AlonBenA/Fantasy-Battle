from classes.game import BColor
import random


class BattleManager:

    def __init__(self, players, enemies):
        self.players = players
        self.enemies = enemies

    def player_turn(self):

        for player in self.players:
            if player.get_hp() == 0:
                print(player.get_name() + " is unconscious")
            else:
                repeat_the_turn_flag = True
                while repeat_the_turn_flag:
                    repeat_the_turn_flag = False
                    player.choose_action()

                    choice = int(input("    Choose action:")) - 1

                    if choice is 0:
                        self.player_choose_attack(player)
                    elif choice is 1:
                        repeat_the_turn_flag = self.player_choose_magic(player)
                    elif choice is 2:
                        repeat_the_turn_flag = self.player_choose_item(player)

            if self.check_if_all_enemies_hp_is_zero():
                return

    def player_choose_attack(self, player):
        enemy_target = player.choose_target(self.enemies)
        taken_damage = self.enemies[enemy_target].take_damage(player.generate_damage())
        print(player.get_name() + " attack " + self.enemies[enemy_target].get_name() + " for", taken_damage,
              "points of damage.")

        if self.enemies[enemy_target].get_hp() == 0:
            print(player.get_name() + " defeated " + self.enemies[enemy_target].get_name())
            del self.enemies[enemy_target]

    def player_choose_magic(self, player):
        choose_magic_flag = True
        while choose_magic_flag:
            choose_magic_flag = False
            player.choose_magic()
            magic_choice = int(input("    Choose magic:")) - 1

            if magic_choice == -1:
                return True

            spell = player.magic[magic_choice]
            current_mp = player.get_mp()

            print("you chose", spell.name)

            if spell.cost > current_mp:
                print(BColor.FAIL + "\n Not enough MP /n" + BColor.ENDC)
                choose_magic_flag = True
            else:
                self.player_magic_use(player, spell)

        return False

    def player_choose_item(self, player):

        choose_item_flag = True
        while choose_item_flag:
            choose_item_flag = False
            player.choose_item()
            item_choice = int(input("    Choose Item: ")) - 1

            if item_choice == -1:
                return True

            item = player.items[item_choice]["Item"]

        player.add_item(item.name, -1)

        if item.type == "Potion":
            player.heal(item.prop)
            print(BColor.OKGREEN + "\n", item.name, "heals for " + str(item.prop), " HP" + BColor.ENDC)
        elif item.type == "attack":
            enemy_target = player.choose_target(self.enemies)
            self.enemies[enemy_target].take_damage(item.prop)
            print(BColor.FAIL + player.name + " use ", item.name, " for", str(item.prop),
                  "points of damage. to " +
                  self.enemies[enemy_target].get_name() + BColor.ENDC)
        elif item.type == "elixir":
            if item.name == "elixir":
                player.rest()
                print(BColor.OKGREEN + "\n", item.name, "fully restores HP and MP" + BColor.ENDC)
            elif item.name == "megaElixir":
                for player_temp in self.players:
                    player_temp.rest()
                print(BColor.OKGREEN + "\n", item.name,
                      "fully restores HP and MP to every member of player party " + BColor.ENDC)

        delete_index = -1

        for i in range(0, len(player.items)):
            if player.items[i]["quantity"] <= 0:
                delete_index = i

        if delete_index >= 0:
            del player.items[delete_index]

    def check_if_all_enemies_hp_is_zero(self):

        for character in self.enemies:
            if character.get_hp() is not 0:
                return False
        return True

    def check_if_all_players_hp_is_zero(self):
        for character in self.players:
            if character.get_hp() is not 0:
                return False
        return True

    def show_status(self):
        print("-----------------------")
        print("players:")

        print("\n\nNAME                            HP:                                 MP:")
        for player in self.players:
            player.get_stats()

        print("===============================")
        print("-----------------------")
        print("Enemies:")

        print("\n\nNAME                            HP:                                    ")
        for enemy in self.enemies:
            enemy.get_enemy_stats()
        print("===============================")

    def enemy_turn(self):
        # Enemy attack phase
        for enemy in self.enemies:

            repeat_the_turn_flag = True
            while repeat_the_turn_flag:
                repeat_the_turn_flag = False
                enemy_choice = random.randrange(0, 3)

                if enemy_choice == 0:
                    self.enemy_chose_attack(enemy)
                elif enemy_choice == 1:
                    if len(enemy.magic) > 0:
                        self.enemy_chose_magic(enemy)
                    else:
                        repeat_the_turn_flag = True
                else:
                    if len(enemy.items) > 0:
                        self.enemy_chose_item(enemy)
                    else:
                        repeat_the_turn_flag = True

        if self.check_if_all_players_hp_is_zero():
            return


    def enemy_chose_attack(self, enemy):
        target = random.randrange(0, len(self.players))
        taken_damage = self.players[target].take_damage(enemy.generate_damage())
        print(enemy.get_name() + " attack " + self.players[target].get_name() + " for",
              taken_damage, "points of damage.")

    def enemy_chose_magic(self, enemy):

        magic_choice = random.randrange(0, len(enemy.magic))
        spell = enemy.magic[magic_choice]
        if enemy.mp < spell.cost:
            print(BColor.FAIL + enemy.get_name() + " try to use " + spell.name + " but it fall " + BColor.ENDC)
            print("So " + enemy.get_name() + " chose to attack instead ")
            self.enemy_chose_attack(enemy)
        else:
            self.enemy_magic_use(enemy, spell)

    def enemy_chose_item(self, enemy):

        item_choice = self.enemy_chose_which_item_to_use(enemy)

        item = enemy.items[item_choice]["Item"]

        enemy.add_item(item.name, -1)

        if item.type == "Potion":
            enemy.heal(item.prop)
            print(BColor.OKGREEN + "\n", item.name, "heals for " + str(item.prop), " HP to", enemy.get_name() + BColor.ENDC)
        elif item.type == "attack":
            player_target = random.randrange(0 , len(self.players))
            self.players[player_target].take_damage(item.prop)
            print(BColor.FAIL + enemy.get_name() + " use ", item.name, " for", str(item.prop),
                  "points of damage. to " +
                  self.players[player_target].get_name() + BColor.ENDC)
        elif item.type == "elixir":
            if item.name == "elixir":
                enemy.rest()
                print(BColor.OKGREEN + "\n", item.name, "fully restores HP and MP to", enemy.get_name() + BColor.ENDC)
            elif item.name == "megaElixir":
                for enemy_temp in self.enemies:
                    enemy_temp.rest()
                print(BColor.OKGREEN + "\n", item.name, "fully restores HP and MP to every member of enemy party"
                      + BColor.ENDC)

        delete_index = -1

        for i in range(0, len(enemy.items)):
            if enemy.items[i]["quantity"] <= 0:
                delete_index = i

        if delete_index >= 0:
            del enemy.items[delete_index]

    def enemy_chose_which_item_to_use(self,enemy):
        return random.randrange(0, len(enemy.items))

    def player_magic_use(self, player, spell):
        player.reduce_mp(spell.cost)
        if str.lower(spell.type) == "white":
            magic_heal = spell.generate_damage()
            ally_target = player.choose_target(self.players)
            self.players[ally_target].heal(magic_heal)
            print(BColor.OKBLUE + spell.name, "heals " + self.players[ally_target].get_name() + " for",
                  str(magic_heal) + BColor.ENDC)
            print(BColor.OKGREEN + self.players[ally_target].get_name() + " current hp: "
                  + str(self.players[ally_target].get_hp()) + BColor.ENDC)
        elif str.lower(spell.type) == "black":
            magic_damage = spell.generate_damage()
            enemy_target = player.choose_target(self.enemies)
            self.enemies[enemy_target].take_damage(magic_damage)
            print(BColor.OKBLUE + player.name + " used", spell.name, "for", str(magic_damage),
                  "points of damage. to " + self.enemies[enemy_target].get_name() + BColor.ENDC)

    def enemy_magic_use(self, enemy, spell):
        enemy.reduce_mp(spell.cost)

        if str.lower(spell.type) == "white":
            magic_heal = spell.generate_damage()
            ally_target = self.enemy_chose_who_to_heal()
            self.enemies[ally_target].heal(magic_heal)
            print(BColor.OKBLUE + enemy.get_name() + " used", spell.name, "heals "
                  + self.enemies[ally_target].get_name() + " for", str(magic_heal) + BColor.ENDC)
            print(BColor.OKGREEN + self.enemies[ally_target].get_name() + " current hp: "
                  + str(self.enemies[ally_target].get_hp()) + BColor.ENDC)
        elif str.lower(spell.type) == "black":
            magic_damage = spell.generate_damage()
            player_target = random.randrange(0, len(self.players))
            self.players[player_target].take_damage(magic_damage)
            print(BColor.OKBLUE + enemy.get_name() + " used", spell.name, "for", str(magic_damage),
                  "points of damage. to " + self.players[player_target].get_name() + BColor.ENDC)

    def enemy_chose_who_to_heal(self):
        lowest_hp_enemy_index = 0
        for i in range(1, len(self.enemies)):
            if self.enemies[i].get_hp() < self.enemies[lowest_hp_enemy_index].get_hp():
                lowest_hp_enemy_index = i
        return lowest_hp_enemy_index
