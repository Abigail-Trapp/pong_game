from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard 


screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)



# set up net separating players
for ypos in range(-270,270,30):
    net = Turtle()
    net.color("white")
    net.penup()
    net.hideturtle()
    net.setpos(0.00,ypos)
    net.write("|", True, align="center", font=("Comic Sans MS", 15, "bold"))
  
scoreboard = Scoreboard()

# player paddle
player = Paddle()
player.setpos(350,0)
player.penup()

# computer paddle
computer = Paddle()
computer.setpos(-350,0)


screen.listen()
screen.onkey(player.up, "Up") #case sensitive
screen.onkey(player.down, "Down")
screen.onkey(computer.up, "w")
screen.onkey(computer.down, "s")

ball = Ball()

# How to solve the problem with screen.tracer 
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(player) < 50 and ball.xcor() > 320 or ball.distance(computer) < 50 and ball.xcor() < -320:
        ball.bounce_side()

    if ball.xcor() == 440:
        # print("Computer Wins")
        scoreboard.update_computer_score()
        ball.goto(0.00,0.00)
        ball.move_speed = 0.1
    elif ball.xcor() == -440:
        # print("You Win")
        scoreboard.update_player_score()
        ball.goto(0.00,0.00)
        ball.move_speed = 0.1

screen.exitonclick()