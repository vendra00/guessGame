from service.GameStateService import game_state
from service.PlayerService import create_character


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


def new_game():
    game_state(3)
    create_character()


def load_game():
    pass


def options():
    pass


run()
