from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=620, height=620)
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
    if snake.head.distance(food) < 13:
        food.refresh()
        scoreboard.writeScore()

    # Detect if snake hits wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        gameOn = False
        scoreboard.game_over()

screen.exitonclick()
