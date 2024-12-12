from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
score =0
screen = Screen()
screen.setup(width= 600,height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(key = "Up",fun = snake.up)
screen.onkey(key = "Down",fun = snake.down)
screen.onkey(key = "Left",fun = snake.left)
screen.onkey(key = "Right",fun = snake.right)

game_on = True
while game_on:
     screen.update()
     time.sleep(0.1)
     snake.move()

     #detect collision with food
     if snake.head.distance(food) <14:
          food.refresh()
          snake.extend()
          score.increase_score()

     #detect collision with wall
     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
          game_on = False
          score.game_over()

     #detect collision with tail
     #if head collides with any part of body -> trigger game_over()
     for i in snake.t[1:]:
          if snake.head.distance(i) < 10:
                    game_on = False
                    score.game_over()










screen.exitonclick()
