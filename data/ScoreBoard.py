from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.penup()
        self.score = -1
        with open("data/data.txt") as f:
            self.high_score = int(f.readlines()[0])
        self.scoreCount()
    
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Score: {self.score},  High Score: {self.high_score}", move= True, align= "center", font= "Arial")

    
    def scoreCount(self):
        self.clear()
        self.goto(0, 275)
        self.score += 1
        self.write(f"Score: {self.score},  High Score: {self.high_score}", move= True, align= "center", font= "Arial")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data/data.txt", "w") as file:
                file.write(str(self.high_score))
