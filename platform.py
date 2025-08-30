from turtle import Turtle
 
class Platform(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(8,2)
        self.penup()
        self.goto(position)
        

    def up(self):
        newy_cor = self.ycor() + 20
        self.goto(self.xcor(), newy_cor)
    def down(self):
        newy_cor = self.ycor() - 20
        self.goto(self.xcor(), newy_cor)        

