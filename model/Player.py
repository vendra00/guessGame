class Player:
    def __init__(self, name: str = None, high_score: int = None):
        self.name = name
        self.high_score = high_score

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_high_score(self):
        return self.high_score

    def set_high_score(self, high_score: int):
        self.high_score = high_score
