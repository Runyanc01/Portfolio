# Import relevant modules
# Do not alter this part
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Important note: this projects requires Python 3.8 or later 
# version to run smoothly. If an older version is used,
# it may not work properly.

def main():
    # Set up game window
    # Do not alter this part
    screen = Screen()
    # Feel free to change the title to one of your choosing
    screen.title("Hopper the Turtle!")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # create an instance of the Player class and assign it
    # to player.
    # Complete this part

    # Create an instance of the CarManager class and assign it
    # to car_manager.
    # Complete this part

    # Create an instance of the Scoreboard class and assing it
    # to scoreboard.    
    # Complete this part


    # Listen to keyboard events
    # Invoke player.go_up() method if Up key is pressed
    # Do not alter this part
    screen.listen()
    screen.onkey(player.go_up, "Up")
    
    game_is_on = True
    while game_is_on:

        # Code inside loop is refreshed every 0.1 seconds
        time.sleep(0.1)
        screen.update()

        # Invoke the create_car() method of car_manager
        # Complete this part

        # Invoke the move_cars() method of car_manager
        # Complete this part

        # Detect collision with car
        # Do not alter this part
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        # Detect successful crossing
        # Use the is_at_finish_line() method of player object
        # to check whether turtle reached the finish line.
        # If so invoke the player go_to_start() method,
        # invoke the car_manager level_up() method, and
        # invoke the scoreboard increase_level() method.
        # Complete this part

    # Exit when player clicks on game window
    # Do not alter this part
    screen.exitonclick()

if __name__ == "__main__":
    main()
