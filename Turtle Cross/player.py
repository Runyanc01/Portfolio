# Import the Turtle class from the turtle module
# Do not alter this part
from turtle import Turtle

# Initialize global constants
# Do not alter this part
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Create Player class that inherits from Turtle class
class Player(Turtle):

    # Initializer for Player class
    def __init__(self):
        # Invoke initializer of parent class
        # Set shape attribute to turtle
        # Invoke penup() method
        # Invoke go_to_start() method
        # Invoke setheading() method with a value of 90
        # Complete this part
        

    # This method moves player up by the MOVE_DISTANCE
    def go_up(self):
        # Invoke the forward() method and pass the MOVE_DISTANCE
        # as a parameter.
        # Complete this part
        

    # This method resets position to starting position
    def go_to_start(self):
        # Invoke the goto() method and pass the STARTING_POSITION
        # as a parameter.
        # Complete this part
        

    # This method checks if player reached finish line
    # Do not alter this part
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
