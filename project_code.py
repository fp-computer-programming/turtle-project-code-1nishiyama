# Author: ATN 3/28/22

import turtle

# setting up the screen size for the player
window = turtle.Screen()
window.setup(500, 500)

# defining all three turtles for their creations. each turtle will be hidden with the same pen size for consistency
a = turtle.Turtle()
a.hideturtle()
a.pensize(3)

b = turtle.Turtle()
b.hideturtle()
b.pensize(3)

c = turtle.Turtle()
c.hideturtle()
c.pensize(3)

d = turtle.Turtle()
d.hideturtle()
d.pensize(3)

# light blue bg for an accurate "sky"
window.bgcolor('light blue')
# 100-150px will be the best size relative to the door
length = window.numinput("Length", "Please choose the length for the base to be (100-150px): ")

# function for the door
def draw_door():
    a.penup()
    a.goto(-12.5, 0)
    a.pendown()
    a.begin_fill()
    a.fillcolor('#654321')
    # constructing the shape in the most efficient way that i saw fit
    for x in range(2):
        a.right(90)
        a.forward(35)
        a.right(90)
        a.forward(25)
    a.end_fill()
    d.pendown()
    d.speed(0)
    d.goto(6.5, 10)
    d.begin_fill()
    d.fillcolor('yellow')
    d.circle(3)
    d.end_fill()
    d.penup()

# for the second option of a door, i found that it wouldn't function properly without writing it out as such
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
    d.pendown()
    d.speed(0)
    d.goto(6.5, 10)
    d.begin_fill()
    d.fillcolor('yellow')
    d.circle(3)
    d.end_fill()
    d.penup()
    d.goto(-6.5, 10)
    d.pendown()
    d.begin_fill()
    d.fillcolor('yellow')
    d.circle(3)
    d.end_fill()
    d.penup()

# constructing the basic shape of the house 
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

# i drew a nice basic background using the fastest speed offered in order make it less boring for the user
def draw_bg():
    a.speed(0)
    a.goto(-500, -500)
    a.pendown()
    a.begin_fill()
    a.goto(-500, 0)
    a.goto(500, 0)
    a.goto(500, -500)
    # light green color for the "grass"
    a.fillcolor('light green')
    a.end_fill()
    a.penup()
    # the speed changes back to it's default
    a.speed(3)

# defines the first type of roof 
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

# defines the second type of roof
def type_2():
    a.penup()
    a.goto(-(length / 2), length / 1.5)
    a.begin_fill()
    a.pendown()
    a.right(165)
    a.forward(length / 1.25)
    a.goto(length / 2, length / 1.5)
    a.fillcolor(window.textinput("Color", "Please choose a roof color: "))
    a.end_fill()

# i tried to do some perspective work in creating these trees because it is extremely difficult and time-consuming
# to make detailed art
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
    c.penup()
    c.goto(175, 0)
    c.pendown()
    c.begin_fill()
    c.fillcolor('#3A3B3C')
    c.right(75)
    c.forward(350)
    c.goto(175, 0)
    c.right(105)
    c.forward(50)
    c.left(105)
    c.forward(350)
    c.left(105)
    c.forward(50)
    c.end_fill()
    

# i called the draw_base function to begin the program, then asked the user the following conditionals
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
