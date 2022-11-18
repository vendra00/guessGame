import logging
import random
from enum import Enum
from collections import namedtuple

# Global Variables for default values
DEFAULT_CONDITION: int = 100
HEAVY_ARMOR: str = "Heavy Armor"
LIGHT_ARMOR: str = "Light Armor"

# Pieces Names
HELMET: str = 'Helmet'
ARMOR: str = 'Armor'
SHOULDERS: str = 'Shoulders'
BRACERS: str = 'Bracers'
BOOTS: str = 'Boots'
SHIELD: str = 'Shield'

# Pieces Material Types
LEATHER: str = 'Leather'
HIDE: str = 'Hide'
SCALED: str = 'Scaled'
IRON: str = 'Iron'
STEEL: str = 'Steel'


class LeatherSet(namedtuple('LeatherSet', 'condition armor weight type the_name'), Enum):
    Helmet = DEFAULT_CONDITION, 12, 2, LIGHT_ARMOR, LEATHER + ' ' + HELMET
    Armor = DEFAULT_CONDITION, 26, 6, LIGHT_ARMOR, LEATHER + ' ' + ARMOR
    Bracers = DEFAULT_CONDITION, 7, 2, LIGHT_ARMOR, LEATHER + ' ' + BRACERS
    Boots = DEFAULT_CONDITION, 7, 2, LIGHT_ARMOR, LEATHER + ' ' + BOOTS
    Shoulders = DEFAULT_CONDITION, 7, 2, LIGHT_ARMOR, LEATHER + ' ' + SHOULDERS


class HideSet(namedtuple('HideSet', 'condition armor weight type the_name'), Enum):
    Helmet = DEFAULT_CONDITION, 10, 2, LIGHT_ARMOR, HIDE + ' ' + HELMET
    Armor = DEFAULT_CONDITION, 20, 5, LIGHT_ARMOR, HIDE + ' ' + ARMOR
    Bracers = DEFAULT_CONDITION, 5, 1, LIGHT_ARMOR, HIDE + ' ' + BRACERS
    Boots = DEFAULT_CONDITION, 5, 1, LIGHT_ARMOR, HIDE + ' ' + BOOTS
    Shoulders = DEFAULT_CONDITION, 5, 1, LIGHT_ARMOR, HIDE + ' ' + SHOULDERS


class ScaledSet(namedtuple('ScaledSet', 'condition armor weight type the_name'), Enum):
    Helmet = DEFAULT_CONDITION, 14, 2, LIGHT_ARMOR, SCALED + ' ' + HELMET
    Armor = DEFAULT_CONDITION, 32, 6, LIGHT_ARMOR, SCALED + ' ' + ARMOR
    Bracers = DEFAULT_CONDITION, 9, 2, LIGHT_ARMOR, SCALED + ' ' + BRACERS
    Boots = DEFAULT_CONDITION, 9, 2, LIGHT_ARMOR, SCALED + ' ' + BOOTS
    Shoulders = DEFAULT_CONDITION, 8, 3, LIGHT_ARMOR, SCALED + ' ' + SHOULDERS


class IronSet(namedtuple('IronSet', 'condition armor weight type the_name'), Enum):
    Helmet = DEFAULT_CONDITION, 15, 5, HEAVY_ARMOR, IRON + ' ' + HELMET
    Armor = DEFAULT_CONDITION, 25, 30, HEAVY_ARMOR, IRON + ' ' + ARMOR
    Bracers = DEFAULT_CONDITION, 10, 5, HEAVY_ARMOR, IRON + ' ' + BRACERS
    Boots = DEFAULT_CONDITION, 10, 6, HEAVY_ARMOR, IRON + ' ' + BOOTS
    Shoulders = DEFAULT_CONDITION, 7, 6, HEAVY_ARMOR, IRON + ' ' + SHOULDERS
    Shield = DEFAULT_CONDITION, 20, 12, HEAVY_ARMOR, IRON + ' ' + SHIELD


class SteelSet(namedtuple('SteelSet', 'condition armor weight type the_name'), Enum):
    Helmet = DEFAULT_CONDITION, 17, 5, HEAVY_ARMOR, STEEL + ' ' + HELMET
    Armor = DEFAULT_CONDITION, 31, 35, HEAVY_ARMOR, STEEL + ' ' + ARMOR
    Bracers = DEFAULT_CONDITION, 12, 4, HEAVY_ARMOR, STEEL + ' ' + BRACERS
    Boots = DEFAULT_CONDITION, 12, 8, HEAVY_ARMOR, STEEL + ' ' + BOOTS
    Shoulders = DEFAULT_CONDITION, 11, 6, HEAVY_ARMOR, STEEL + ' ' + SHOULDERS
    Shield = DEFAULT_CONDITION, 24, 12, HEAVY_ARMOR, STEEL + ' ' + SHIELD


def take_armor_set():
    logging.info('called')
    set_list = [LeatherSet, HideSet, IronSet, SteelSet, ScaledSet]
    return random.choice(list(set_list))
