import logging

from myEnums import EquipmentName, EquipmentPlacement


class Equipment(object):

    def __init__(self, name: EquipmentName = None, placement: EquipmentPlacement = None,
                 condition: int = None, armor: int = None):
        logging.info('called')
        self.name = name
        self.placement = placement
        self.condition = condition
        self.armor = armor
