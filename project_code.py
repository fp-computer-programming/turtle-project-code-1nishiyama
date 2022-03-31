# Author: ATN 3/28/22

import turtle

window = turtle.Screen()
window.setup(500, 500)
t = turtle.Turtle()
t.hideturtle()
t.pensize(3)
window.bgcolor('light blue')
length = window.numinput("Length", "Please choose the length for the base to be (100-150px): ")

def draw_door():
    t.penup()
    t.goto(-25, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor('#654321')
    for x in range(2):
        t.right(90)
        t.forward(35)
        t.right(90)
        t.forward(25)
    t.end_fill()

def draw_double_door():
    t.penup()
    t.goto(-25, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor('#654321')
    for x in range(2):
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(25)
    t.end_fill()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor('#654321')
    for x in range(2):
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(25)
    t.end_fill()


def draw_base():
    t.speed(3)
    t.begin_fill()
    t.right(180)
    t.forward(length / 2)
    for x in range(3):
        t.right(90)
        t.forward(length)
    t.right(90)
    t.forward(length / 2)
    t.fillcolor(window.textinput("Color", "Please choose a base color: "))
    t.end_fill()

def draw_bg():
    t.speed(0)
    t.goto(-500, -500)
    t.pendown()
    t.begin_fill()
    t.goto(-500, 0)
    t.goto(500, 0)
    t.goto(500, -500)
    t.fillcolor('light green')
    t.end_fill()
    t.penup()
    t.speed(3)


def type_a():
    t.goto(-(length / 2), length)
    t.begin_fill()
    t.pendown()
    t.right(140)
    t.forward(length / 1.5)
    t.goto(length / 2, length)
    t.fillcolor(window.textinput("Color", "Please choose a roof color: "))
    t.end_fill()

def type_b():
    t.goto(-(length / 2), length)
    t.begin_fill()
    t.pendown()
    t.right(165)
    t.forward(length / 1.5)
    t.goto(length / 2, length)
    t.fillcolor(window.textinput("Color", "Please choose a roof color: "))
    t.end_fill()

def door():
    t.goto(-(length / 2), 0)
    t.pencolor("brown")
    for x in range(2):
        t.left(90)
        t.forward(length / 8)
    

draw_base()
num_doors = window.textinput("Roof", "Please choose '1' or '2' doors: ")
if num_doors == 1:
    draw_door()
elif num_doors == 2:
    draw_double_door()
draw_bg()
roof_type = window.textinput("Roof", "Please choose roof type 'a' or 'b': ")
if roof_type.lower() == 'a':
    type_a()
elif roof_type.lower() == 'b':
    type_b()


window.mainloop()
