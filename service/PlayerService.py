import re
import logging

from model import Character
from myEnums.Gender import Gender
from myEnums.PlayerClass import PlayerClass
from myEnums.PlayerRace import PlayerRace
from service.GameStateService import game_state
from utils.LoggerConfig import log_config


# Method that set a character name
def set_name(character: Character):
    logging.info('called')
    game_state(4)
    try:
        character.name = input("===   Insert a name: ")
    except ValueError as e:
        logging.error('Given value (%s) has raised an error -->\n (%s)', character.name, e)
        game_state(100)
        set_name(character)
    check_name(character)


# Method that verify if the name is valid
def check_name(character: Character):
    logging.info('called')
    if not re.search(r"^([a-zA-Z]+\s?[a-zA-Z]+)+?$", character.name):
        logging.warning('Given value (%s) is not allowed!', character.name)
        game_state(101)
        set_name(character)


# Method that set a character gender
def set_gender(character: Character):
    logging.info('called')
    game_state(5)
    try:
        character.gender = Gender(int(input("===   Select a gender: ")))
    except ValueError as e:
        logging.error('Given value (%s) has raised an error -->\n (%s)', character.gender, e)
        game_state(100)
        set_gender(character)


# Method that set a character main class
def set_player_class(character: Character):
    logging.info('called')
    game_state(6)
    try:
        character.player_class = PlayerClass(int(input("===   Select a class: ")))
    except ValueError as e:
        logging.error('Given value (%s) has raised an error -->\n (%s)', character.player_class, e)
        game_state(100)
        set_player_class(character)


# Method that set character race
def set_player_race(character: Character):
    logging.info('called')
    game_state(7)
    try:
        character.player_race = PlayerRace(int(input("===   Select a race: ")))
    except ValueError as e:
        logging.error('Given value (%s) has raised an error --> (%s)', character.player_race, e)
        game_state(100)
        set_player_race(character)


# Method that create and set a character
def create_character():
    logging.info('called')
    character: Character = Character.Character()
    try:
        set_name(character)
        set_gender(character)
        set_player_class(character)
        set_player_race(character)
        print(character.name.capitalize(), character.gender.name, character.player_class.name, character.player_race.name)
    except Exception as e:
        logging.error('Given object (%s) has raised an error --> (%s)', character, e)


log_config()
create_character()
