from turtle import *

bgcolor("black")
hideturtle()
pensize(2)
speed(15)

for i in range(20):
    for colors in ["green", "cyan"]:
        color(colors)
        circle(100)
        left(10)
done()