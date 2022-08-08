import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Muhammed's pong game")
screen.bgcolor("black")
screen.tracer(0)
ball = Ball()
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.deflect_y()

    if ball.distance(paddle2) < 50 or ball.distance(paddle1) < 50:
        ball.deflect_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
