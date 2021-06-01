from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

score = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()


screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detects collision with wall
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()

    # Detects collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detects if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r()

screen.exitonclick()
