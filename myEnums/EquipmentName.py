from enum import Enum
from collections import namedtuple


class LeatherSet(namedtuple('LeatherSet', 'condition armor'), Enum):
    Leather_Helmet = 100, 1
    Leather_Armor = 100, 3
    Leather_Bracers = 100, 1
    Leather_Boots = 100, 1
    Leather_Shoulders = 100, 1


class PlateSet(namedtuple('PlateSet', 'condition armor'), Enum):
    Plate_Helmet = 100, 2
    Plate_Armor = 100, 5
    Plate_Bracers = 100, 2
    Plate_Boots = 100, 2
    Plate_Shoulders = 100, 2
