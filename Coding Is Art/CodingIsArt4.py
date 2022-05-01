from turtle import *

color("black")
pensize(3)
speed(7)
bgcolor("white")
penup()
goto(-100,-100)
pendown()
left(150)

begin_fill()
for i in range(220):
    forward(1.2)
    right(0.6)
for i in range(20):
    forward(0.8)
    right(2)
forward(35)
left(40)
forward(35)
for i in range(20):
    forward(0.8)
    right(2)
for i in range(60):
    forward(1.2)
    right(0.6)
right(75)
for i in range(90):
    forward(1.4)
    left(1)
right(45)
for i in range(20):
    forward(1.2)
    right(1.4)
right(10)
for i in range(20):
    forward(1)
    right(0.4)
forward(10)
right(15)
for i in range(35):
    forward(1.2)
    right(0.8)
for i in range(20):
    forward(0.8)
    right(2)
forward(40)
left(65)
forward(50)
right(45)
forward(20)
end_fill()
penup()
goto(-35,115)
pendown()
right(95)

begin_fill()
for i in range(80):
    forward(2)
    right(0.8)
right(115)
for i in range(80):
    forward(2)
    right(0.8)
end_fill()