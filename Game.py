class Game: 
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins) 

    def get_score(self):
        score = 0
        rolly_index = 0
        # [10,3,4,0,0,0,0,0,]
        for frame in range(10): 
            if self.strike_catcher(rolly_index):
                score += 10 + self.rolls[rolly_index+1] + self.rolls[rolly_index+2]
                rolly_index += 1
            elif self.spare_catcher(rolly_index): 
                score += 10 + self.rolls[rolly_index+2]
                rolly_index += 2
            else:
                score += self.rolls[rolly_index] + self.rolls[rolly_index+1]
                rolly_index += 2
        return score
    
    def spare_catcher(self, rolly_index):
        return self.rolls[rolly_index] + self.rolls[rolly_index+1] == 10
    
    def strike_catcher(self, rolly_index):
        return self.rolls[rolly_index] == 10

    

