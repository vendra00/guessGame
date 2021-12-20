from myEnums.Gender import Gender
from myEnums.PlayerClass import PlayerClass
from myEnums.PlayerRace import PlayerRace


# Class that represents a Character in the game
class Character(object):

    # Constructor with arguments
    def __init__(self, name: str = None, gender: Gender = None, player_class: PlayerClass = None,
                 player_race: PlayerRace = None, exp: int = 0):
        self.name = name
        self.gender = gender
        self.player_class = player_class
        self.player_race = player_race
        self.exp = exp
