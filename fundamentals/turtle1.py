#This program uses turtle
import turtle
wn=turtle.Screen()
hubert=turtle.Turtle()
dist=50
angle=90
for a in range(15):
    hubert.forward(dist)
    hubert.right(angle)
    dist+=10
    angle-=3

wn.exitonclick()