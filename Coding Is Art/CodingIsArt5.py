from turtle import *

bgcolor("black")
dist = 1
flag = 1400
speed(20)
while flag:
    for i in range(4):
        color("cyan")
        forward(dist)
        left(90)
        left(1)
        dist += 1
        flag -= 1
    for i in range(4):
        color('green')
        forward(dist)
        left(90)
        left(1)
        dist += 1
        flag -= 1
done()