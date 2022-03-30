# Author: ATN 3/28/22

import turtle

window = turtle.Screen()
turtle.screensize(500, 500)
t = turtle.Turtle()
t.hideturtle()
t.pensize(3)

length = window.numinput("Length", "Please choose the length for the base to be (px): ")

def draw_base():
    t.begin_fill()
    for x in range(4):
        t.right(90)
        t.forward(length)
    t.fillcolor(window.textinput("Color", "Please choose a base color: "))
    t.end_fill()
    t.penup()


def type_a():
    t.begin_fill()
    t.goto(-(length), 0)
    a1 = window.numinput("Side 1", "Please choose the angle for the roof: ")
    t.pendown()
    t.left(a1)
    t.forward(a1)
    t.goto(0, 0)
    t.fillcolor(window.textinput("Color", "Please choose a roof color: "))
    t.end_fill()


def type_b():
    t.begin_fill()
    t.goto(-(length), 0)
    a1 = window.numinput("Side 1", "Please choose the angle for left side of the roof (0-90): ")
    t.pendown()
    t.left(a1)
    t.forward(length)
    a2 = window.numinput("Side 2", "Please choose the angle for right side of the roof (0-90): ")
    t.left(a2)
    t.goto(0, 0)
    t.fillcolor(window.textinput("Color", "Please choose a roof color: "))
    t.end_fill()
    t.penup()

def door():
    t.goto(-(length / 2), 0)
    t.pencolor("brown")
    for x in range(2):
        t.left(90)
        t.forward(length / 8)
    

draw_base()
type_b()
door()

window.mainloop()
