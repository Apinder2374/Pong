from turtle import Turtle, Screen
from platform import Platform
from ball import Ball
from scoreboard import Scoreboard



screen = Screen()
screen.bgcolor("black")
screen.screensize(800, 600)
screen.title("Pong")
platform = Platform((400, 0))
platform2 = Platform((-400, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(platform.up, "Up")
screen.onkeypress(platform2.up, "w")
screen.onkeypress(platform.down, "Down")
screen.onkeypress(platform2.down, "s")

game_is_on = True
while game_is_on:
    
    screen.update()
    ball.move()
    if ball.ycor() > 400 or ball.ycor() < -400:
        ball.bounce_y()
    
    if ball.distance(platform) < 55 and ball.xcor() > 360 or ball.distance(platform2) < 55 and ball.xcor() < -360:
        ball.bounce_x()
        scoreboard.increase_score()

    if ball.xcor() > 430 or ball.xcor() < -440:
        scoreboard.game_over()
        game_is_on = False



screen.exitonclick()


