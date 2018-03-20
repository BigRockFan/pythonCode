# Rohan Putcha
# 3 / 15 / 2018
# turtleRace.py
# Make turtles race on a track

from turtle import *
from random import *

title("Turtle Race")
bgcolor("orange")

writer = Pen()
writer.ht()
writer.speed(0)
writer.color("firebrick")
writer.up()
writer.left(90)
writer.fd(200)
writer.down()
writer.write("Turtle Race", align = "center", font = ("Arial", 35, "bold"))


track = Pen()
track.ht()
track.up()
track.speed(0)
track.right(180)
track.fd(300)
track.right(90)
track.fd(150)
track.right(180)
track.down()
x = 1
y = 0
xgoto = -260
#Makes Tracks
while y < 16:
    x = 0
    while x <= 16:
        track.fd(20)
        if (x % 2 == 0):
            track.down()
        else:
            track.up()
        x = x + 1
    track.up()
    track.goto(xgoto, 150)
    track.down()
    xgoto = xgoto + 40
    y = y + 1

x = -305
num = 0
#Numbers Tracks
for i in range(16):
    writer.up()
    writer.goto(x, -200)
    writer.down()
    writer.write(str(num), align = "left", font = "Arial")
    num = num + 1
    x = x + 40

racer1 = Pen("turtle")
racer2 = Pen("turtle")
racer3 = Pen("turtle")
racer4 = Pen("turtle")

racer1.color("red")
racer2.color("green")
racer3.color("blue")
racer4.color("aqua")

racer1.up()
racer2.up()
racer3.up()
racer4.up()



def race():
    
    racer1.turtlesize(1,1)
    racer2.turtlesize(1,1)
    racer3.turtlesize(1,1)
    racer4.turtlesize(1,1)
    
    racer1.goto(-305, 100)
    racer2.goto(-305, 50)
    racer3.goto(-305, 0)
    racer4.goto(-305, -50)

    while (True):
        racer1.fd(randint(1,3))
        racer2.fd(randint(1,3))
        racer3.fd(randint(1,3))
        racer4.fd(randint(1,3))
        coord1 = racer1.position()
        coord2 = racer2.position()
        coord3 = racer3.position()
        coord4 = racer4.position()
        if (coord1[0] > 300):
            winner = "RED WINS"
            winc = "red"
            racer1.turtlesize(2,2)
            for i in range(180):
                racer1.right(2)
            break
        elif(coord2[0] > 300):
            winner = "GREEN WINS"
            winc = "green"
            racer2.turtlesize(2,2)
            for i in range(180):
                racer2.right(2)
            break
        elif (coord3[0] > 300):
            winner = "BLUE WINS"
            winc = "blue"
            racer3.turtlesize(2,2)
            for i in range(180):
                racer3.right(2)
            break
        elif (coord4[0] > 300):
            winner = "AQUA WINS"
            winc = "aqua"
            racer4.turtlesize(2,2)
            for i in range(180):
                racer4.right(2)
            break
        
    writer.up()
    writer.goto(0, -250)
    writer.down()
    writer.color(winc)
    writer.write(winner, align = "center", font = ("Arial", 20, "bold"))
    

race()

writer.color("black")
writer.up()
writer.goto(0, 160)
writer.down()

writer.color("white")
writer.write("Press R to play again", align = "center", font = ("Arial", 20, "bold"))

onkey(race, "r")
listen()
done()


