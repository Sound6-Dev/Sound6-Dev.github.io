class DiceGame:
    def __init__(self):
        self.turn = 1
        self.point = None
        self.finished = False
        self.result = ""

    def reset(self):
        self.turn = 1
        self.point = None
        self.finished = False
        self.result = ""

    def validate_roll(self, roll):
        if not isinstance(roll, int):
            return False
        return 2 <= roll <= 12

    def play_turn(self, roll):
        if self.finished:
            return

        if not self.validate_roll(roll):
            self.result = "Error: Roll must be between 2 and 12."
            return

        # FIRST TURN LOGIC
        if self.turn == 1:
            if roll in (2, 3, 12):
                self.result = f"Turn {self.turn}: You rolled {roll}. You lose!"
                self.finished = True
            elif roll in (7, 11):
                self.result = f"Turn {self.turn}: You rolled {roll}. You win!"
                self.finished = True
            else:
                self.point = roll
                self.result = f"Turn {self.turn}: You rolled {roll}. Point is now {self.point}."
                self.turn += 1

        # LATER TURNS
        else:
            if roll == 7:
                self.result = f"Turn {self.turn}: You rolled 7. You lose!"
                self.finished = True
            elif roll == self.point:
                self.result = f"Turn {self.turn}: You rolled {roll}. You win!"
                self.finished = True
            else:
                self.result = f"Turn {self.turn}: You rolled {roll}. Keep rolling..."
                self.turn += 1
