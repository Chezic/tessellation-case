# Case-study #6
# Developers:   Aksenov A. (%),
#               Soloveychik D. (%),
#               Labuzov A. (%)
import turtle as t
from math import sqrt

def turtle_area():
    t.pensize(3)
    t.left(90)
    t.fd(500)
    t.right(90)
    t.fd(500)
    t.right(90)
    t.fd(500)
    t.right(90)
    t.fd(500)

def right_fd(angle,side_len, times):
    while times != 0:
        t.right(angle)
        t.fd(side_len)
        times -= 1

def draw_hexagon(x, y, side_len, color):
    t.goto(x,y)
    x_side = (side_len * sqrt(3)) / 2
    y_side = side_len / 2
    t.setheading(-90)
    t.fd(y_side)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.left(120)
    t.fd(side_len)
    right_fd(60, side_len, 6)
    t.end_fill()





turtle_area()
draw_hexagon(0,400,50,'red')

t.mainloop()