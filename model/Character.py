class Character(object):

    def __init__(self, name: str = None, gender: str = None, player_class: str = None,
                 player_race: str = None, exp: int = None):
        self.name = name
        self.gender = gender
        self.player_class = player_class
        self.player_race = player_race
        self.exp = exp
