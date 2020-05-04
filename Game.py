class Game: 
    def __init__(self):
        self.score = 0

    def roll(self, pins):
        self.score += pins

    def get_score(self):
        return self.score
        
