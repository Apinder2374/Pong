from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
        newx_cor = self.xcor() + self.x_move
        newy_cor = self.ycor() + self.y_move
        self.goto(newx_cor, newy_cor)
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        