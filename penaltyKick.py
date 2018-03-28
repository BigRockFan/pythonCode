# ------------------------------------------------------------------------------
# Rohan Putcha
# 3/21/2018
# penaltyKick_Putcha.py
# ------------------------------------------------------------------------------
from turtle import *
import time
import random

# ******************************************************************************
# shootBall
# ******************************************************************************

def shootBall():
    writer.undo()
    ball.up()
    ang = ball.towards(ballX, ballY)
    ball.setheading(ang)
    goalie.up()
    global blockhit_history
    blockhit_history = []
    while ball.ycor() < 220:
        randX = random.randint(-250, 250)
        goalie.up()
        goalie.goto(randX, 220)
        goalie.down()
        ball.fd(40)
        if ball.ycor() > 205: #since the ball has a radius, it is tested for every possible time it is in the range of even the edge of the ball touching the goalie
            blockhit_history = blockhit_history + goalOrBlocked(blockhit_history)

    if "miss" in blockhit_history:
        result = "MISS"
        color = "dark grey"
        
    elif "blocked" in blockhit_history: #If even one "blocked" is in the list, then it is blocked (because that means the goalie touched the ball at some point)
        result = "BLOCK"
        color = "red"
        
    else:
        result = "GOAL"
        color = "blue"

    writer.up()
    writer.goto(0, -20)
    writer.down()
    writer.color(color)
    writer.write(result, align = "center", font = ("Arial", 35, "bold"))
    
# ******************************************************************************
# goalOrBlocked
# ******************************************************************************

def goalOrBlocked(blockhit_history):
    goalpos = int(goalie.xcor())
    pos = int(ball.xcor())

    if ((pos < -200) or (pos > 200)):
        return ["miss"]
    postup = list(range(pos-35, pos+35))
    
    for i in range(goalpos-55, goalpos+55):
        if i in postup:
            blockhit_history = blockhit_history + ["blocked"]
        else:
            blockhit_history = blockhit_history + ["hit"]
    return blockhit_history
    
# ******************************************************************************
# placeBall
# ******************************************************************************

def placeBall(x,y):
    global ballX
    global ballY
    ballX = x
    ballY = y
    shootBall()

# ******************************************************************************
# main
# ******************************************************************************

setup(1010, 700)
bgcolor("forestgreen")

writer = Pen()
writer.ht()
writer.speed(0)
writer.color("white")
writer.width(4)
writer.up()
writer.goto(-200, 340)
writer.down()
writer.right(90)
writer.fd(100)
writer.goto(-200, 340)
writer.left(90)
writer.fd(400)
writer.right(90)
writer.fd(100)
writer.up()
writer.goto(-260, 240)
writer.down()
writer.setheading(270)
writer.fd(200)
writer.left(90)
writer.fd(520)
writer.left(90)
writer.fd(200)

writer.up()
writer.goto(-500, 240)
writer.down()
writer.setheading(0)
writer.fd(1000)

writer.up()
writer.goto(-400, 240)
writer.down()
writer.seth(270)
writer.fd(480)
writer.left(90)
writer.fd(800)
writer.left(90)
writer.fd(480)

writer.up()
writer.setheading(270)
writer.goto(-100, -240)
writer.down()
writer.circle(100, 180)
register_shape("ball.gif")

ball = Pen()
ball.shape("ball.gif")
ball.speed(0)
ball.up()
ball.left(90)
ball.goto(0,-300)


global ballX
global ballY
ballX = 0
ballY = 0

goalie = Pen("square")
goalie.up()
goalie.goto(0,220)
goalie.down()
goalie.shapesize(1,5)

writer.up()
writer.goto(0, -200)
writer.down()
writer.write("Drag the ball to a location and release to kick", align = "center", font = ("Arial", 20, "bold"))


ball.onrelease(placeBall)
done()

