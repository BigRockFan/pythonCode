# ------------------------------------------------------------------------------
# K.Franchi
# 3/21/2018
# penaltyKick_Franchi.py
# ------------------------------------------------------------------------------
from turtle import *
import time
import random

# ******************************************************************************
# shootBall
# ******************************************************************************

def shootBall():
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
        if ball.ycor() > 190:
            blockhis_history = goalOrBlocked(blockhit_history)

    if "blocked" in blockhit_history:
        print("blocked")
        
    else:
        print("goal")
        print(blockhit_history)

# ******************************************************************************
# goalOrBlocked
# ******************************************************************************

def goalOrBlocked(blockhit_history):
    goalpos = goalie.position()
    pos = ball.pos()
    goaliepos = int(goalpos[0])
    poss = int(pos[0])
    
    postup = tuple(range(poss-40, poss+40))
    
    for i in range(goaliepos-55, goaliepos+55):
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


ball.onrelease(placeBall)
done()

