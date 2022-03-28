# Author: ATN 3/28/22

import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.hideturtle()

def draw_base():
    t.pensize(window.numinput("Width", "Please choose how wide for the base to be (px): "))
    t.fillcolor(window.textinput("Color", "Please choose a base color: "))
    t.begin_fill()
    for x in range(4):
        t.right(90)
        t.forward(100)
    t.end_fill()
    t.penup()


# first roof type
def type_a():
    t.pensize(window.numinput("Width", "Please choose how wide for the roof to be (px): "))
    t.fillcolor(window.textinput("Color", "Please choose a roof color: "))
    t.begin_fill()
    t.goto(-100, 0)
    t.pendown()
    t.left(45)
    t.forward(71)
    t.right(90)
    t.forward(71)
    t.end_fill()


draw_base()
type_a()

window.mainloop()
