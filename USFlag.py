#  File: Turtle.py
#  Description: Draw the US flag
#  Student's Name: Minh-Tri Ho
#  Student's UT EID: mh47723
#  Course Name: CS 313E
#  Unique Number: 50940
#
#  Date Created: 02/08/16
#  Date Last Modified: 02/08/16

import turtle, math

#Convert from Python's coordinates to standard coordinates
def convertX(x, width):
    return x - (width/2)

#Convert from Python's coordinates to standard coordinates
def convertY(y, height):
    return - y + (height/2)

#Draw a regular rectangle
def drawRectangle(ttl, x, y, height, width):
    #Setting up the color
    ttl.color("black")

    #Setting up the cursor
    ttl.setheading(0)
    ttl.penup()
    ttl.setposition(x, y)
    ttl.pendown()

    #Starting drawing
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(height)
    ttl.right(90)
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(height)

#Drawing a filled rectangle
def drawRectangleFill(ttl, x, y, height, width, color):
    #Setting up the color
    ttl.color(color)
    ttl.fillcolor(color)
    ttl.setheading(0)

    #Setting up the cursor
    ttl.penup()
    ttl.setposition(x, y)
    ttl.pendown()

    #Starting drawing
    ttl.begin_fill()
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(height)
    ttl.right(90)
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(height)
    ttl.end_fill()

#Drawing a White Star
def drawStar(ttl, x, y, height):
    ttl.color("#FFFFFF")
    ttl.fillcolor("#FFFFFF")
    ttl.setheading(90)

    #radius
    r = 4/5 * height/13

    #length
    #l = r/3
    l = math.cos(18*math.pi/360)*r/(2*(1+math.cos(72*math.pi/360)))

    #position the turtle
    ttl.penup()
    ttl.setposition(x, y)
    ttl.forward(r/2)
    ttl.pendown()

    #draw star
    ttl.begin_fill()
    ttl.setheading(252)
    ttl.forward(l)
    ttl.right(72)
    ttl.forward(l)
    ttl.left(144)
    ttl.forward(l)
    ttl.right(72)
    ttl.forward(l)
    ttl.left(144)
    ttl.forward(l)
    ttl.right(72)
    ttl.forward(l)
    ttl.left(144)
    ttl.forward(l)
    ttl.right(72)
    ttl.forward(l)
    ttl.left(144)
    ttl.forward(l)
    ttl.right(72)
    ttl.forward(l)

    ttl.end_fill()

def main():
    #Height
    hoist = (int)(input("Enter the vertical height of the flag in pixels: "))
    #Width
    fly = hoist * 1.9

    #Creating the Turtle and the Screen
    ttl = turtle.Turtle()
    screen = turtle.Screen()

    screen.setup(width = fly + 200, height = hoist + 200)#, startx = 200, starty = 200)
    screen.title("United States Flag")

    #draw Red Stripes
    for i in range(7):
        drawRectangleFill(ttl, convertX(0, fly), convertY(2*i*hoist/13, hoist), hoist/13, fly, "#B22234")

    #draw canton
    drawRectangleFill(ttl, convertX(0, fly), convertY(0, hoist), hoist*7/13, fly*2/5, "#3C3B6E")

    #draw star
    e = hoist/10 * 7/13 #heigth
    g = fly/12 * 2/5 #width
    for i in range(1, 12, 2):
        for j in range(1, 10, 2):
            drawStar(ttl, convertX(i*g, fly), convertY(j*e, hoist), hoist)
    for i in range(2, 12, 2):
        for j in range(2, 10, 2):
            drawStar(ttl, convertX(i*g, fly), convertY(j*e, hoist), hoist)

    #draw Flag
    drawRectangle(ttl, convertX(0, fly), convertY(0, hoist), hoist, fly)

    ttl.hideturtle()

main()
