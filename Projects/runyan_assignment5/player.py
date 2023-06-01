# Import the Turtle class from the turtle module
from turtle import Turtle

# Initialize global constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Create Player class that inherits from Turtle class
class Player(Turtle):

    # Initializer for Player class
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)
        
        

    # This method moves player up by the MOVE_DISTANCE
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        

    # This method resets position to starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)
        

    # This method checks if player reached finish line
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
