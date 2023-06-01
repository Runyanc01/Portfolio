from turtle import Turtle

FONT = ("Courier", 24, "normal")

# Create Scoreboard class that inherits from the Turtle class
class Scoreboard(Turtle):

    #initializer of Scoreboard class
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    #update scoreboard and write current level
    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align = 'left', font = FONT)

    #increase level attribute and invoke update_scoreboard method
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        # Go to position (0,0) and  write GAME OVER centered
        # using the font FONT
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
