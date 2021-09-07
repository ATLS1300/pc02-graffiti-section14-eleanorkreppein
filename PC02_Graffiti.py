#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.up()
turtle.goto(40,84)
turtle.down()
turtle.color("firebrick2")
turtle.left(90)
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.up()
turtle.goto(250,100)
turtle.down()
turtle.color("green2")
turtle.pensize(16)
turtle.right(180)
turtle.forward(300)
turtle.up()
turtle.goto(111,-90)
turtle.color("purple3")
turtle.pensize(5)
turtle.right(90)
turtle.down()
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.up()
turtle.goto(-150,200)
turtle.left(90)
turtle.color("gray0")
turtle.pensize(10)
turtle.down()
turtle.begin_fill()
turtle.forward(120)
turtle.left(120)
turtle.forward(120)
turtle.left(120)
turtle.forward(120)
turtle.end_fill()

turtle.done()


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()

