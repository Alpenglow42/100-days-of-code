from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food.
    if snake.head.distance(food) < 15:
        #print("yay food")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
    #detectect collision with tail
    for seg in snake.segment:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()

screen.exitonclick()
# FOOD DOESN'T CYCLE THROUGH LIST OR CHANGE COLOR AFTER EATEN!