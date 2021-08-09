import random

class BColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:

    def __init__(self, name, hp, mp, attack, defence, magic, items):
        self.name = name
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.attack = attack
        self.defence = defence
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def get_name(self):
        return self.name.replace(" ","")

    def get_spaces_after_name(self):
        list_of_name = list(self.name)
        spaces = ""
        for c in list_of_name:
            if c == " ":
                spaces += " "
        return spaces

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMp

    def get_defence(self):
        return self.defence

    def show_person_status(self):
        print("Hero name:" + self.get_name())
        print("     hp:" + str(self.maxHp))
        print("     mp:" + str(self.maxMp))
        print("     attack:" + str(self.attack))
        print("     defence:" + str(self.defence))
        self.show_magic_list()
        self.show_item_list()

    def show_magic_list(self):
        print("     magic list: ")
        for spell in self.magic:
            if str.lower(spell.type) == "black":
                print("             spell:" + spell.name + " cost: " + str(spell.cost) + " base damage: " + str(spell.damage) )
            else:
                print("             spell:" + spell.name + " cost: " + str(spell.cost) + " base healing: " + str(spell.damage))

    def show_item_list(self):
        print("     Item list: ")
        for item in self.items:
            the_item = item["Item"]
            quantity = item["quantity"]
            if the_item.type == "Potion":
                print("             name: " + the_item.name + ", Description: heal hero for " + str(the_item.prop)
                      + ", quantity:" + str(quantity))
            elif the_item.type == "attack":
                print("             name: " + the_item.name + ", Description: attack enemy for " + str(the_item.prop)
                      + ", quantity:" + str(quantity))
            elif the_item.type == "elixir":
                print("             name: " + the_item.name + ", Description: fully restores HP and MP for hero "
                      + ", quantity:" + str(quantity))
            elif the_item.type == "megaElixir":
                print("             name: " + the_item.name + ", Description: fully restores HP and MP for hero "
                      + ", quantity:" + str(quantity))

    def generate_damage(self):
        present = self.attack*0.2
        attack_low = int(self.attack - present)
        attack_high = int(self.attack + present)
        return random.randrange(attack_low, attack_high)

    def take_damage(self, damage):
        taken_damage = damage - (self.defence*0.5)
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return taken_damage

    def reduce_mp(self, cost):
        self.mp -= cost

    def heal(self, damage):
        self.hp += damage
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def rest(self):
        self.hp = self.maxHp
        self.mp = self.maxMp

    def level_up(self):
        temp = self.maxHp * 0.1
        self.maxHp = self.maxHp + temp
        self.hp = self.maxHp
        temp = self.maxMp * 0.05
        self.maxMp = self.maxMp + temp
        self.mp = self.maxMp
        temp = self.attack * 0.1
        self.attack = self.attack + temp
        temp = self.defence * 0.1
        self.defence = self.defence + temp

    def choose_action(self):
        i = 1
        print("\n    " + BColor.BOLD + self.name + BColor.ENDC)
        print(BColor.OKBLUE + BColor.BOLD + "    ACTIONS:" + BColor.ENDC)
        for action in self.actions:
            print("    "+str(i) + ".", action)
            i += 1

    def choose_target(self, targets):
        i = 1
        print("\n" + BColor.FAIL + BColor.BOLD + "    TARGET:" + BColor.ENDC)
        for target in targets:
            print("        " + str(i) + ".", target.get_name())
            i += 1
        choice = int(input("    choose target:")) - 1
        return choice

    def choose_magic(self):
        i = 1
        print("\n" + BColor.OKBLUE + BColor.BOLD + "    MAGIC:" + BColor.ENDC)
        for spell in self.magic:
            print("    "+str(i)+".", spell.name, " cost:(", spell.cost, ")")
            i += 1
        print("Choose 0 to go back ")

    def choose_item(self):
        i = 1
        print("\n" + BColor.OKGREEN + BColor.BOLD + "    ITEMS: " + BColor.ENDC)
        for item in self.items:
            print("    "+str(i) + ".", item["Item"].name, ":", item["Item"].description,
                  "(x" + str(item["quantity"]) + ")")
            i += 1
        print("Choose 0 to go back ")

    def find_item(self, item_name):
        for item in self.items:
            if item["Item"].name == item_name:
                return item

    def add_item(self, item_name, quantity_to_add):
        for item in self.items:
            if item["Item"].name == item_name:
                new_quantity = item["quantity"] + quantity_to_add
                if new_quantity < 0:
                    item["quantity"] = 0
                else:
                    item["quantity"] = new_quantity

    def get_stats(self):
        number_of_health_bars = 100 / 4
        health_bar = self.get_health_bar(number_of_health_bars)
        number_of_mana_bars = 100 / 10
        mana_bar = self.get_mana_bar(number_of_mana_bars)
        health_status = self.get_health_status()
        mp_status = self.get_mana_status()
        upper_lines_for_health_bar = self.get_upper_lines_for_bars(number_of_health_bars)
        upper_lines_for_mana_bar = self.get_upper_lines_for_bars(number_of_mana_bars)

        print("                                       " + upper_lines_for_health_bar + "              "
              + upper_lines_for_mana_bar)
        print(BColor.BOLD + self.get_name() + ":" + self.get_spaces_after_name()+"              " +
        str(health_status) + " " + BColor.OKGREEN +
        "|" + health_bar + "|"
        + BColor.ENDC + BColor.BOLD
        + "   " + mp_status + BColor.OKBLUE +
        "|"+ mana_bar +"|" + BColor.ENDC)

    def get_enemy_stats(self):
        number_of_health_bars = 100 / 2
        health_bar = self.get_health_bar(number_of_health_bars)
        health_status = self.get_health_status()
        upper_lines_for_health_bar = self.get_upper_lines_for_bars(number_of_health_bars)

        print("                                           " + upper_lines_for_health_bar)
        print(BColor.BOLD + self.get_name() + ":" + self.get_spaces_after_name() + "              " +
        str(health_status) + " " + BColor.FAIL +
        "|" + health_bar + "|" + BColor.ENDC)

    def get_health_bar(self, number_of_bars):
        health_bar = ""
        bar_ticks = (self.hp / self.maxHp) * number_of_bars
        while bar_ticks > 0:
            health_bar += "█"
            bar_ticks -= 1

        while len(health_bar) < number_of_bars:
            health_bar += " "

        return health_bar

    def get_mana_bar(self, number_of_bars):
        mana_bar = ""
        bar_ticks = (self.mp / self.maxMp) * number_of_bars
        while bar_ticks > 0:
            mana_bar += "█"
            bar_ticks -= 1

        while len(mana_bar) < number_of_bars:
            mana_bar += " "

        return mana_bar

    def get_health_status(self):
        current_hp = str(self.hp)
        current_max_hp = str(self.maxHp)

        while len(current_hp) < 6:
            current_hp = " " + current_hp

        while len(current_max_hp) < 6:
            current_max_hp = current_max_hp + " "

        health_status = current_hp + "/" + current_max_hp
        return health_status

    def get_mana_status(self):
        current_mp = str(self.mp)
        current_max_mp = str(self.maxMp)

        while len(current_mp) < 4:
            current_mp = " " + current_mp

        while len(current_max_mp) < 4:
            current_max_mp = current_max_mp + " "

        mp_status = current_mp + "/" + current_max_mp
        return mp_status

    def get_upper_lines_for_bars(self, number_of_bars):
        bars = ""
        for i in range(1, int(number_of_bars+1)):
            bars += "_"
        return bars



