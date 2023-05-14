from turtle import Turtle

FONT = ("Courier", 24, "normal")

# Create Scoreboard class that inherits from the Turtle class
class Scoreboard(Turtle):

    def __init__(self):
        # Call the initializer of parent class
        # Do not alter this part
        super().__init__()

        # Complete this part
        # Initialize level attribute to 1
        # Hide the turtle
        # Lift the pen (penup)
        # Goto position (-280, 250)
        # invoke update_scoreboard() method


    def update_scoreboard(self):
        # Complete this part
        # Clear the scoreboard object
        # Write the the string "Level: {current level attribute value}" 
        # Align it left, and set the font to the FONT constant above


    def increase_level(self):
        # Increase the level attribute by 1
        # Invoke update_scoreboard() method


    def game_over(self):
        # Go to position (0,0) and  write GAME OVER centered
        # using the font FONT
        # Do not alter this part
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
