from turtle import Turtle
import random

# Define global constants:
#     a list of colors for the obstacles
#     a starting move distance of 5
#     a move increment of 10
# Do not alter this part
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Create a CarManager class to handle our moving turtle/car
class CarManager:

    # Initialize object by creating the attributes:
    #     all_cars (an empty list)
    #     car_speed which starting with the value
    #     of the STARTING_MOVE_DISTANCE
    # Do not alter this part
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # This method will be used to create random
    # cars at random positions with a given color
    # from COLORS and add them to all_cars
    # Do not alter this part 
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # This method will iterate through the cars in all_cars
    # and make each move by invoking the backward() method
    # and passing to it the car_speed as input.
    def move_cars(self):
        # Complete this part

    # This method will increment car_speed by the
    # MOVE_INCREMENT constant value
    def level_up(self):
        # Complete this part
        
