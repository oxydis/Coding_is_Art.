from turtle import *

color("cyan")
bgcolor("black")
speed(7)

penup()
goto(-100,-100)
pendown()
pensize(2.5)

for i in range(1):
    circle(35)
    penup()
    goto(-65,-70)
    pendown()
    right(80)
    circle(35)
penup()
goto(-100,-30)
left(180)
pendown()

for i in range(120):
    forward(2)
    right(0.2)

for i in range(90):
    forward(1)
    right(1.8)

left(7.5)

for i in range(120):
    forward(2)
    right(0.2)

penup()
goto(-60,232)
left(12)
pendown()
forward(35)

penup()
goto(-25,175)
pendown()
right(80)

for i in range(44):
    forward(1.7)
    right(0.4)

hideturtle()