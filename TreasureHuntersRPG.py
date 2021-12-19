from model import Character
from myEnums.Gender import Gender
from myEnums.PlayerClass import PlayerClass
from myEnums.PlayerRace import PlayerRace


def run():
    game_state(1)
    play()


def play():
    game_state(2)
    menu()


def menu():
    option: int = 0
    try:
        option = int(input("===   Select an option: "))
    except ValueError:
        game_state(100)
        play()
    match option:
        case 1:
            new_game()
        case 2:
            load_game()
        case 3:
            options()
        case 4:
            exit()
        case _:
            game_state(100)
            play()


def game_state(state: int):
    match state:
        case 1:
            print("========================================")
            print("===   WELCOME TO TREASURE HUNTERS    ===")
            print("========================================")
        case 2:
            print("========================================")
            print("===            GAME MENU             ===")
            print("========================================")
            print("===       1 - NEW GAME               ===")
            print("===       2 - LOAD GAME              ===")
            print("===       3 - OPTIONS                ===")
            print("===       4 - EXIT                   ===")
            print("========================================")
        case 3:
            print("========================================")
            print("===            NEW GAME              ===")
            print("========================================")
            print("===       CREATE A CHARACTER         ===")
            print("========================================")
        case 4:
            print("========================================")
            print("===         Character Name           ===")
            print("========================================")
        case 5:
            print("========================================")
            print("===         Character Gender         ===")
            print("========================================")
            print("===   1 - MALE                       ===")
            print("===   2 - FEMALE                     ===")
            print("========================================")
        case 6:
            print("========================================")
            print("===         Character Class          ===")
            print("========================================")
            print("===   1 - WIZARD                     ===")
            print("===   2 - WARRIOR                    ===")
            print("===   3 - ROGUE                      ===")
            print("========================================")
        case 7:
            print("========================================")
            print("===         Character Race           ===")
            print("========================================")
            print("===   1 - HUMAN                      ===")
            print("===   2 - ELF                        ===")
            print("===   3 - DWARF                      ===")
            print("===   4 - ORC                        ===")
            print("===   5 - GOBLIN                     ===")
            print("===   6 - GNOME                      ===")
            print("===   7 - HALF GIANT                 ===")
            print("========================================")
        case 100:
            print("========================================")
            print("===      Not a proper option!        ===")
            print("===                                  ===")
            print("===          Try it again            ===")
            print("========================================")
        case 101:
            print("========================================")
            print("===      Name cannot be empty        ===")
            print("===       or a numeric value         ===")
            print("===                                  ===")
            print("===          Try it again            ===")
            print("========================================")


def new_game():
    game_state(3)
    create_character()


def load_game():
    pass


def options():
    pass


def set_name():
    game_state(4)
    name: str = ""
    try:
        name = input("===   Insert a name: ").capitalize()
    except ValueError:
        game_state(100)
        set_name()
    check_name(name)
    return name


def check_name(name: str):
    if name == "" or name.isspace() or name.isnumeric():
        game_state(101)
        set_name()


def set_gender():
    game_state(5)
    gender: int = 0
    try:
        gender = int(input("===   Select a gender: "))
    except ValueError:
        game_state(100)
        set_gender()
    return Gender(gender).name


def set_player_class():
    game_state(6)
    player_class: int = 0
    try:
        player_class = int(input("===   Select a class: "))
    except ValueError:
        game_state(100)
        set_player_class()

    return PlayerClass(player_class).name


def set_player_race():
    game_state(7)
    player_race: int = 0
    try:
        player_race = int(input("===   Select a race: "))
    except ValueError:
        game_state(100)
        set_player_race()
    return PlayerRace(player_race).name


def create_character():
    c: Character = Character.Character(set_name(), set_gender(), set_player_class(), set_player_race(), 0)
    print(c.name, c.gender, c.player_race, c.player_class, c.exp)
    return c


create_character()
run()
