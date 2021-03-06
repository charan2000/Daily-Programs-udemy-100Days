from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Gameu")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameOn = True
while gameOn:
    screen.update()
    # scoreboard.writeScore()
    time.sleep(0.1)
    snake.move()
    # Detect collision from food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.writeScore()

    # Detect if snake hits wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.update_score()
        snake.reset()
        scoreboard.reset()

    # Detect collision with tail:
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            scoreboard.update_score()
            snake.reset()
            scoreboard.reset()

screen.exitonclick()
