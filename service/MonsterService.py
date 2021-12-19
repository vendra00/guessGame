from model import Monster
import random

from model.Equipment import Equipment
from myEnums.Bestiary import Bestiary
from myEnums.EquipmentName import LeatherSet
from myEnums.EquipmentPlacement import EquipmentPlacement
from myEnums.MonsterType import MonsterType
from myEnums.Size import Size


def generate_monster():
    monster: Monster = Monster.Monster()
    set_name(monster)
    set_monster_type(monster)
    set_size(monster)
    set_equipment(monster)
    set_hp(monster)
    set_attack(monster)
    set_armor(monster)
    set_exp(monster)
    # name: Bestiary, monster_type: MonsterType, equipment: Equipment,
    # size: Size, hp: int, attack: int, armor: int, exp: int

    print(monster.name.name, monster.monster_type.name, monster.size.name, monster.hp,
          monster.attack, monster.armor, monster.exp)


def set_name(monster: Monster):
    monster.name = random.choice(list(Bestiary))


def set_monster_type(monster: Monster):
    if monster.name.value == Bestiary(1).value or monster.name.value == Bestiary(3).value:
        monster.monster_type = MonsterType(1)
    elif monster.name.value == Bestiary(4).value or monster.name.value == Bestiary(7).value:
        monster.monster_type = MonsterType(5)
    elif monster.name.value == Bestiary(2).value or monster.name.value == Bestiary(8).value:
        monster.monster_type = MonsterType(3)
    elif monster.name.value == Bestiary(6).value or monster.name.value == Bestiary(9).value:
        monster.monster_type = MonsterType(2)
    elif monster.name.value == Bestiary(5).value:
        monster.monster_type = MonsterType(7)


def set_size(monster):
    if monster.name.value == Bestiary(2).value or monster.name.value == Bestiary(5).value \
            or monster.name.value == Bestiary(6).value or monster.name.value == Bestiary(8).value:
        monster.size = Size(1)
    elif monster.name.value == Bestiary(1).value or monster.name.value == Bestiary(3).value \
            or monster.name.value == Bestiary(4).value or monster.name.value == Bestiary(7).value \
            or monster.name.value == Bestiary(9).value:
        monster.size = Size(2)


def set_equipment(monster):
    inventory = []
    # name: EquipmentName, placement: EquipmentPlacement, condition: int, armor: int
    if monster.name.value == Bestiary(4).value or monster.name.value == Bestiary(7).value:
        inventory.append(Equipment(LeatherSet.Leather_Helmet.name, EquipmentPlacement(1).name,
                                   int(LeatherSet.Leather_Helmet.condition),
                                   int(LeatherSet.Leather_Helmet.armor)))
        inventory.append(Equipment(LeatherSet.Leather_Armor.name, EquipmentPlacement(5).name,
                                   int(LeatherSet.Leather_Armor.condition),
                                   int(LeatherSet.Leather_Armor.armor)))
        inventory.append(Equipment(LeatherSet.Leather_Bracers.name, EquipmentPlacement(6).name,
                                   int(LeatherSet.Leather_Bracers.condition),
                                   int(LeatherSet.Leather_Bracers.armor)))
        inventory.append(Equipment(LeatherSet.Leather_Bracers.name, EquipmentPlacement(7).name,
                                   int(LeatherSet.Leather_Bracers.condition),
                                   int(LeatherSet.Leather_Bracers.armor)))
        inventory.append(Equipment(LeatherSet.Leather_Boots.name, EquipmentPlacement(13).name,
                                   int(LeatherSet.Leather_Boots.condition),
                                   int(LeatherSet.Leather_Boots.armor)))
        inventory.append(Equipment(LeatherSet.Leather_Boots.name, EquipmentPlacement(14).name,
                                   int(LeatherSet.Leather_Boots.condition),
                                   int(LeatherSet.Leather_Boots.armor)))
        inventory.append(Equipment(LeatherSet.Leather_Shoulders.name, EquipmentPlacement(3).name,
                                   int(LeatherSet.Leather_Shoulders.condition),
                                   int(LeatherSet.Leather_Shoulders.armor)))
        inventory.append(Equipment(LeatherSet.Leather_Shoulders.name, EquipmentPlacement(4).name,
                                   int(LeatherSet.Leather_Shoulders.condition),
                                   int(LeatherSet.Leather_Shoulders.armor)))
        monster.equipment = inventory


def set_hp(monster):
    if monster.size.value == Size(1).value:
        monster.hp = 50
    elif monster.size.value == Size(2).value:
        monster.hp = 100
    elif monster.size.value == Size(3).value:
        monster.hp = 200


def set_attack(monster):
    if monster.size.value == Size(1).value:
        monster.attack = 5
    elif monster.size.value == Size(2).value:
        monster.attack = 12
    elif monster.size.value == Size(3).value:
        monster.attack = 22


def set_armor(monster):
    if monster.equipment != [None]:
        for equipment in monster.equipment:
            monster.armor += equipment.armor


def set_exp(monster):
    monster.exp = 100


generate_monster()
