from model.Equipment import Equipment
from myEnums.Bestiary import Bestiary
from myEnums.MonsterType import MonsterType
from myEnums.Size import Size


class Monster(object):

    def __init__(self, name: Bestiary = None, monster_type: MonsterType = None, equipment: [Equipment] = None,
                 size: Size = None, hp: int = None, attack: int = None, armor: int = 0, exp: int = 0):
        self.name = name
        self.monster_type = monster_type
        self.size = size
        self.equipment = [equipment]
        self.hp = hp
        self.attack = attack
        self.armor = armor
        self.exp = exp
