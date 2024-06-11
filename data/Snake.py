from turtle import Turtle

RIGHT = 0
UP = 90 
LEFT = 180
DOWN = 270
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake():
    def __init__(self):
        self.fullSnake = []
        self.create()
        self.head = self.fullSnake[0]    
       
    def add_tail(self, position):
        snake = Turtle(shape= "square")
        snake.color("white")
        snake.penup()
        snake.speed(0)
        snake.goto(position)
        self.fullSnake.append(snake)
          
    def create(self):
        for pos in POSITIONS:
            self.add_tail(pos)

    def extend(self):
        self.add_tail(self.fullSnake[-1].position())
                
    def move(self):
        for i in range(len(self.fullSnake)-1, 0, -1):
            snakePosition = self.fullSnake[i - 1].position()
            self.fullSnake[i].goto(snakePosition)
        self.fullSnake[0].forward(20)
            
    def wMove(self):
        if self.fullSnake[0].heading() != DOWN:
            self.fullSnake[0].setheading(UP)

    def sMove(self):
        if self.fullSnake[0].heading() != UP:
            self.fullSnake[0].setheading(DOWN)

    def dMove(self):
        if self.fullSnake[0].heading() != LEFT:
            self.fullSnake[0].setheading(RIGHT)

    def aMove(self):
        if self.fullSnake[0].heading() != RIGHT:
            self.fullSnake[0].setheading(LEFT)