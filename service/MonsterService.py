from model import Monster
import random
import logging

from model.Equipment import Equipment
from myEnums.Bestiary import Bestiary
from myEnums.EquipmentName import take_armor_set
from myEnums.EquipmentPlacement import EquipmentPlacement
from myEnums.MonsterType import MonsterType
from myEnums.Size import Size
from utils.LoggerConfig import log_config


# Method that create and set a Monster in the game
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

    print(monster.name.name, monster.monster_type.name, monster.size.name, monster.hp,
          monster.attack, monster.armor, monster.exp)


# Method that set a name of a monster randomly from a list
def set_name(monster: Monster):
    logging.info('called')
    monster.name = random.choice(list(Bestiary))


# Method that set a monster type from an enum
def set_monster_type(monster: Monster):
    logging.info('called')
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


# Method that sets a monster size from an enum
def set_size(monster):
    logging.info('called')
    if monster.name.value == Bestiary(2).value or monster.name.value == Bestiary(5).value \
            or monster.name.value == Bestiary(6).value or monster.name.value == Bestiary(8).value:
        monster.size = Size(1)
    elif monster.name.value == Bestiary(1).value or monster.name.value == Bestiary(3).value \
            or monster.name.value == Bestiary(4).value or monster.name.value == Bestiary(7).value \
            or monster.name.value == Bestiary(9).value:
        monster.size = Size(2)


# Method that sets a monster equipment
def set_equipment(monster):
    logging.info('called')
    inventory = []
    # name: EquipmentName, placement: EquipmentPlacement, condition: int, armor: int
    if monster.name.value == Bestiary(4).value or monster.name.value == Bestiary(7).value:
        setType = take_armor_set()
        inventory.append(
            Equipment(setType.Helmet.the_name, EquipmentPlacement(1), setType.Helmet.condition, setType.Helmet.armor))
        inventory.append(
            Equipment(setType.Armor.the_name, EquipmentPlacement(5), setType.Armor.condition, setType.Armor.armor))
        inventory.append(
            Equipment(setType.Bracers.the_name, EquipmentPlacement(6), setType.Bracers.condition, setType.Bracers.armor))
        inventory.append(
            Equipment(setType.Bracers.the_name, EquipmentPlacement(7), setType.Bracers.condition, setType.Bracers.armor))
        inventory.append(
            Equipment(setType.Boots.the_name, EquipmentPlacement(13), setType.Boots.condition, setType.Boots.armor))
        inventory.append(
            Equipment(setType.Boots.the_name, EquipmentPlacement(14), setType.Boots.condition, setType.Boots.armor))
        inventory.append(
            Equipment(setType.Shoulders.the_name, EquipmentPlacement(3), setType.Shoulders.condition, setType.Shoulders.armor))
        inventory.append(
            Equipment(setType.Shoulders.the_name, EquipmentPlacement(4), setType.Shoulders.condition, setType.Shoulders.armor))
        monster.equipment = inventory


# Method that sets a monster hp based on his size
def set_hp(monster):
    logging.info('called')
    if monster.size.value == Size(1).value:
        monster.hp += 25
    elif monster.size.value == Size(2).value:
        monster.hp += 45
    elif monster.size.value == Size(3).value:
        monster.hp += 125


# Method that sets a monster attack based on his size
def set_attack(monster):
    logging.info('called')
    if monster.size.value == Size(1).value:
        monster.attack += 5
    elif monster.size.value == Size(2).value:
        monster.attack += 12
    elif monster.size.value == Size(3).value:
        monster.attack += 22


# Method that sets a monster armor based on his inventory
def set_armor(monster):
    logging.info('called')
    if monster.equipment != [None]:
        for equipment in monster.equipment:
            monster.armor += equipment.armor


# Method that sets a monster experience
def set_exp(monster):
    logging.info('called')
    monster.exp = 100


log_config()
generate_monster()
