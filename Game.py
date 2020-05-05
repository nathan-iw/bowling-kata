class Game: 
    def __init__(self):
        self.rolls = []
        self.total = 0

    def roll(self, pins):
        self.rolls.append(pins) 

    def get_score(self):
        score = 0
        rolly_index = 0
        # [10,3,4,0,0,0,0,0,]
        for frame in range(10): 
            if self.strike_catcher(rolly_index):
                score += self.strike_bonus(rolly_index)
                rolly_index += 1
            elif self.spare_catcher(rolly_index):
                score += self.spare_bonus(rolly_index)
                rolly_index += 2
            else:
                score += self.standard_score(rolly_index)
                rolly_index += 2
        return score
    
    def spare_catcher(self, rolly_index):
        return self.rolls[rolly_index] + self.rolls[rolly_index+1] == 10
    
    def strike_catcher(self, rolly_index):
        return self.rolls[rolly_index] == 10

    def strike_bonus(self, rolly_index):
        bonus = 10 + self.rolls[rolly_index+1] + self.rolls[rolly_index+2]
        return bonus

    def spare_bonus(self, rolly_index):
        bonus = 10 + self.rolls[rolly_index+2]
        return bonus

    def standard_score(self, rolly_index):
        standard = self.rolls[rolly_index] + self.rolls[rolly_index+1]
        return standard


    def get_current_score(self):
        frame_history = []
        score = 0
        rolly_index =0
        # [9,1,9,1]
        while rolly_index < len(self.rolls): 
            if self.strike_catcher(rolly_index) and rolly_index < len(self.rolls)-3:
                frame_total = self.strike_bonus(rolly_index)
                score += frame_total
                frame_history.append(frame_total)
                rolly_index += 1
            elif self.spare_catcher(rolly_index):
                if rolly_index < len(self.rolls)-2:
                    frame_total = self.spare_bonus(rolly_index)
                    score += frame_total
                    frame_history.append(frame_total)
                else:
                    frame_history.append("/")
                rolly_index += 2
            else:
                frame_total = self.standard_score(rolly_index)
                score += frame_total
                frame_history.append(frame_total) 
                rolly_index += 2
        self.total = score
        
        return frame_history


    def get_user_roll(self):
        user_roll = input("Do you know your roll: ")
        self.rolls.append(int(user_roll))