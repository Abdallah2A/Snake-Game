from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.speed(0)
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.penup()
        self.refresh()
        
    def refresh(self):
        cors = (random.randint(-370, 370), random.randint(-270, 270))
        self.goto(cors)