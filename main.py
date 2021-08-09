from classes.game import BColor
from classes.player_character_manager import PlayerCharacterManager
from classes.enemy_manager import EnemyManager
from classes.battle_manager import BattleManager


def battle_won(heroes):
    for hero in heroes:
        hero.rest()
        print("hero " + hero.get_name() + " level up")
        hero.level_up()


def start_battle(players):
    running = True
    Enemy_manager = EnemyManager()
    enemies = Enemy_manager.create_enemy_list()
    battle_manager = BattleManager(players, enemies)

    while running:
        battle_manager.show_status()

        battle_manager.player_turn()

        #check if player won
        if battle_manager.check_if_all_enemies_hp_is_zero():
            print(BColor.OKGREEN + " YOU WON!" + BColor.ENDC)
            return True

        battle_manager.enemy_turn()

        #check if player lost
        if battle_manager.check_if_all_players_hp_is_zero():
            print(BColor.FAIL + "YOU LOST" + BColor.ENDC)
            return False


def show_heroes_status(players):
    for player in players:
        player.show_person_status()
        print("\n")


def show_options():
    print("options")
    print("select 1 to start battle ")
    print("select 2 to see heroes status ")
    print("select 3 to exit ")


def show_main_menu():
    player_character_manager = PlayerCharacterManager()
    heroes = player_character_manager.create_Players_list()
    continue_flag = True
    while continue_flag:
        show_options()
        option_choice = int(input("    Choose options: "))

        if option_choice == 1:
            battle_result = start_battle(heroes)
            if battle_result:
                battle_won(heroes)
            else:
                print("reset heroes ")
                heroes = player_character_manager.create_Players_list()
        elif option_choice == 2:
            show_heroes_status(heroes)
        elif option_choice == 3:
            print(" good bye")
            continue_flag = False
        else:
            print("wrong number, chose again ")


show_main_menu()






