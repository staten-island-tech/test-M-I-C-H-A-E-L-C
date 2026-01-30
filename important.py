import turtle
from turtle import *
t = Turtle()

t.speed(50)

for i in range(300):
    t.forward(100)
    t.left(90)
    t.right(5)

def triangle(x,y):

    sidelength = 100
rotate = 91
def square(x,y):
    for i in range(4):
        t.forward(x+y)
        t.left(y)
square(110,90)
    


