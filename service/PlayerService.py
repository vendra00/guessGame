import re

from model import Character
from myEnums.Gender import Gender
from myEnums.PlayerClass import PlayerClass
from myEnums.PlayerRace import PlayerRace
from service.GameStateService import game_state


def set_name(character: Character):
    game_state(4)
    try:
        character.name = input("===   Insert a name: ")
    except ValueError:
        game_state(100)
        set_name(character)
    check_name(character)


def check_name(character: Character):
    if not re.search(r"^([a-zA-Z]+\s?[a-zA-Z]+)+?$", character.name):
        game_state(101)
        set_name(character)


def set_gender(character: Character):
    game_state(5)
    try:
        character.gender = Gender(int(input("===   Select a gender: ")))
    except ValueError:
        game_state(100)
        set_gender(character)


def set_player_class(character: Character):
    game_state(6)
    try:
        player_class = int(input("===   Select a class: "))
    except ValueError:
        game_state(100)
        set_player_class()
    PlayerClass(player_class)


def set_player_race(character: Character):
    game_state(7)
    try:
        player_race = int(input("===   Select a race: "))
    except ValueError:
        game_state(100)
        set_player_race()
    PlayerRace(player_race)


def create_character():
    # name: str = None, gender: Gender = None, player_class: PlayerClass = None,
    # player_race: PlayerRace = None, exp: int = 0
    character: Character = Character.Character()
    set_name(character)
    set_gender(character)
    set_player_class(character)
    set_player_race(character)
    print(character.name, character.gender.name.capitalize())

