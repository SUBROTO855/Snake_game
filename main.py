from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up screen and giving title name.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

# creating snake object
snake = Snake()

# creating food object
food = Food()

# creating scoreboard object
scoreboard = Scoreboard()

# Setting buttons for movement.
screen.listen()
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #   Detecting snake contact with food and extending length of snake.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_update()

    # Detecting snake's collision with screen wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset()

    #   Detecting snake collision's with itself.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()




screen.exitonclick()
