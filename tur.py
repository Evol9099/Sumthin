import turtle
import time

def initialise():
    canvas = turtle.Screen()
    canvas.title("Flag-It")
    soup = turtle.Turtle()
    canvas.bgcolor("white")
    soup.penup()
    soup.color("purple")
    return soup

#create functions here to draw lines and then functions to call these for the various numbers in your barcode.

pen = initialise()
def poly (len, side, color):
    pen.fillcolor(color)
    pen.begin_fill()
    for n in range (0,side):
        pen.forward(len)
        angle = 360/side
        pen.left(angle)
    pen.end_fill()

def rectangle (len,wid,color):
    pen.fillcolor(color)
    pen.begin_fill()
    for n in range (0,2):
        pen.forward(len)
        pen.left(90)
        pen.forward(wid)
        pen.left(90)
    pen.end_fill()

def star (len,color):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.right(18)
    for n in range (0,5):
        pen.forward(len)
        pen.right(144)
    pen.end_fill()
rectangle(250,150,"red")
pen.forward(83.3)
pen.left(90)
pen.forward(40)
star(90,"yellow")
time.sleep(5)
