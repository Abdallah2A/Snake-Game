import time
from turtle import Screen
from data.Snake import Snake
from data.Food import Food
from data.ScoreBoard import ScoreBoard

# Make the background
screen = Screen()
screen.title("Snake Game")
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
# this making the background doesn't update auto 
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = ScoreBoard()

end = True

screen.listen()
screen.onkeypress(snake.wMove, "w")
screen.onkeypress(snake.sMove, "s")
screen.onkeypress(snake.aMove, "a")
screen.onkeypress(snake.dMove, "d")

while end:
    # now this to update the screen and wait after it 
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.scoreCount()
        snake.extend()

    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        end = False
        scoreboard.reset()
        scoreboard.game_over()
    
    for tail in snake.fullSnake[1:]:
        if snake.head.distance(tail) < 10:
            end = False
            scoreboard.reset()
            scoreboard.game_over()
        
screen.exitonclick()