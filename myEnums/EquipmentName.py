from enum import Enum
from collections import namedtuple
import random


class LeatherSet(namedtuple('LeatherSet', 'condition armor weight type the_name'), Enum):
    Helmet = 100, 12, 2, 'Light Armor', 'Leather Helmet'
    Armor = 100, 26, 6, 'Light Armor', 'Leather Armor'
    Bracers = 100, 7, 2, 'Light Armor', 'Leather Bracers'
    Boots = 100, 7, 2, 'Light Armor', 'Leather Boots'
    Shoulders = 100, 7, 2, 'Light Armor', 'Leather Shoulders'


class HideSet(namedtuple('HideSet', 'condition armor weight type the_name'), Enum):
    Helmet = 100, 10, 2, 'Light Armor', 'Hide Helmet'
    Armor = 100, 20, 5, 'Light Armor', 'Hide Armor'
    Bracers = 100, 5, 1, 'Light Armor', 'Hide Bracer'
    Boots = 100, 5, 1, 'Light Armor', 'Hide Boots'
    Shoulders = 100, 5, 1, 'Light Armor', 'Hide Shoulders'


class IronSet(namedtuple('IronSet', 'condition armor weight type the_name'), Enum):
    Helmet = 100, 15, 5, 'Heavy Armor', 'Iron Helmet'
    Armor = 100, 25, 30, 'Heavy Armor', 'Iron Armor'
    Bracers = 100, 10, 5, 'Heavy Armor', 'Iron Bracers'
    Boots = 100, 10, 6, 'Heavy Armor', 'Iron Boots'
    Shoulders = 100, 7, 6, 'Heavy Armor', 'Iron Shoulders'
    Shield = 100, 20, 12, 'Heavy Armor', 'Iron Shield'


class SteelSet(namedtuple('SteelSet', 'condition armor weight type the_name'), Enum):
    Helmet = 100, 17, 5, 'Heavy Armor', 'Steel Helmet'
    Armor = 100, 31, 35, 'Heavy Armor', 'Steel Armor'
    Bracers = 100, 12, 4, 'Heavy Armor', 'Steel Bracers'
    Boots = 100, 12, 8, 'Heavy Armor', 'Steel Boots'
    Shoulders = 100, 11, 6, 'Heavy Armor', 'Steel Shoulders'
    Shield = 100, 24, 12, 'Heavy Armor', 'Steel Shield'


def take_armor_set():
    setList = [LeatherSet, HideSet, IronSet, SteelSet]
    return random.choice(list(setList))
