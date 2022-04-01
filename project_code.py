# Author: ATN 3/28/22

import turtle

window = turtle.Screen()
window.setup(500, 500)

a = turtle.Turtle()
a.hideturtle()
a.pensize(3)

b = turtle.Turtle()
b.hideturtle()
b.pensize(3)

c = turtle.Turtle()
c.hideturtle()
c.pensize(3)

window.bgcolor('light blue')
length = window.numinput("Length", "Please choose the length for the base to be (100-150px): ")

def draw_door():
    a.penup()
    a.goto(-12.5, 0)
    a.pendown()
    a.begin_fill()
    a.fillcolor('#654321')
    for x in range(2):
        a.right(90)
        a.forward(35)
        a.right(90)
        a.forward(25)
    a.end_fill()


def draw_double_door():
    a.penup()
    a.goto(-25, 0)
    a.pendown()
    a.begin_fill()
    a.fillcolor('#654321')
    for x in range(2):
        a.right(90)
        a.forward(30)
        a.right(90)
        a.forward(25)
    a.end_fill()
    a.penup()
    a.goto(0, 0)
    a.pendown()
    a.begin_fill()
    a.fillcolor('#654321')
    for x in range(2):
        a.right(90)
        a.forward(30)
        a.right(90)
        a.forward(25)
    a.end_fill()


def draw_base():
    a.speed(3)
    a.begin_fill()
    a.right(180)
    a.forward(length / 2)
    a.right(90)
    a.forward(length / 1.5)
    a.right(90)
    a.forward(length)
    a.right(90)
    a.forward(length / 1.5)
    a.right(90)
    a.forward(length / 2)
    a.fillcolor(window.textinput("Color", "Please choose a base color: "))
    a.end_fill()
    draw_bg()


def draw_bg():
    a.speed(0)
    a.goto(-500, -500)
    a.pendown()
    a.begin_fill()
    a.goto(-500, 0)
    a.goto(500, 0)
    a.goto(500, -500)
    a.fillcolor('light green')
    a.end_fill()
    a.penup()
    a.speed(3)


def type_1():
    a.penup()
    a.goto(-(length / 2), length / 1.5)
    a.begin_fill()
    a.pendown()
    a.right(140)
    a.forward(length / 1.5)
    a.goto(length / 2, length / 1.5)
    a.fillcolor(window.textinput("Color", "Please choose a roof color: "))
    a.end_fill()


def type_2():
    a.penup()
    a.goto(-(length / 2), length / 1.5)
    a.begin_fill()
    a.pendown()
    a.right(165)
    a.forward(length / 1.5)
    a.goto(length / 2, length / 1.5)
    a.fillcolor(window.textinput("Color", "Please choose a roof color: "))
    a.end_fill()


def door():
    a.goto(-(length / 2), 0)
    a.pencolor("brown")
    for x in range(2):
        a.left(90)
        a.forward(length / 8)


def draw_trees():
    b.penup()
    b.goto(-100, 0)
    b.pendown()
    b.begin_fill()
    b.fillcolor('#654321')
    for x in range(2):
        b.right(90)
        b.forward(35)
        b.right(90)
        b.forward(15)
    b.end_fill()
    b.penup()
    b.goto(-107.5, -2.5)
    b.begin_fill()
    b.fillcolor('green')
    b.circle(25)
    b.end_fill()
    b.penup()
    b.goto(115, 0)
    b.pendown()
    b.begin_fill()
    b.fillcolor('#654321')
    for x in range(2):
        b.right(90)
        b.forward(35)
        b.right(90)
        b.forward(15)
    b.end_fill()
    b.penup()
    b.goto(107.5, -2.5)
    b.begin_fill()
    b.fillcolor('green')
    b.circle(25)
    b.end_fill()


def draw_driveway():
    c.goto(0, 0)
    c.begin_fill()
    c.fillcolor('#3A3B3C')
    c.right(45)
    c.forward(350)
    c.goto(0, 0)
    c.right(135)
    c.forward(50)
    c.left(135)
    c.forward(350)
    c.left(45)
    c.forward(50)
    c.end_fill()
    
    


draw_base()
num_doors = window.numinput("Doors", "Please choose '1' or '2' doors: ")
if num_doors == 1:
    draw_door()
elif num_doors == 2:
    draw_double_door()
roof_type = window.numinput("Roof", "Please choose roof type '1' or '2': ")
if roof_type == 1:
    type_1()
elif roof_type == 2:
    type_2()
trees = window.textinput("Trees", "Would you like trees? (Y/N) ")
if trees.lower() == 'y':
    draw_trees()
driveway = window.textinput("Driveway", "Would you like a driveway? (Y/N) ")
if driveway.lower() == 'y':
    draw_driveway()
window.mainloop()
