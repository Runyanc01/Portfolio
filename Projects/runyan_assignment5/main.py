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
    screen = Screen()
    screen.title("Timmy the Turtle Cross")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    #create instance of Player
    player = Player()

    #create instance of CarManager
    car_manager = CarManager()

    #create instance of Scoreboard
    scoreboard = Scoreboard()


    # Listen to keyboard events
    # Invoke player.go_up() method if Up key is pressed
    screen.listen()
    screen.onkey(player.go_up, "Up")
    
    #run game while player has not been hit by car
    game_is_on = True
    while game_is_on:

        # Code inside loop is refreshed every 0.1 seconds
        time.sleep(0.1)
        screen.update()

        # Invoke the create_car() method of car_manager
        car_manager.create_car()

        # Invoke the move_cars() method of car_manager
        car_manager.move_cars()

        # Detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        #invoke Boolean function is_at_finish_line
        #move player to start if Boolean function returns True
        #increase car movement speed
        #increase level
        if player.is_at_finish_line() == True:
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

    # Exit when player clicks on game window
    screen.exitonclick()

if __name__ == "__main__":
    main()
