import turtle as t
import random

t.bgcolor("black")
t.color("pink")
t.speed(0)
t.shape("turtle")

t.up() 
t.goto(300,300) 
t.down() 

t.forward(-300)
t.right(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)


t.up() 
t.goto(0,0)
t.down()

r = random.randint(1, 360) 
t.left(r)

while 0<=t.xcor()<=300 and 0<=t.ycor()<=300:
    t.forward(1.95)
    if t.ycor()>= 300:
        angle = t.heading()
        if 0 <= t.heading() <= 90:
            t.right(1.95*angle)
            t.forward(7)
        else:
            t.left(-1.95*angle)
            t.forward(7)
    if t.xcor()<= 0:
        angle = t.heading()
        if 90 <= t.heading() <= 180:
            t.left(170-1.95*angle)
            t.forward(7)
        else:
            t.right(1.95*angle-170)
            t.forward(7)
    if t.ycor()<= 0:
        angle = t.heading()
        if 180 <= t.heading() <= 270:
            t.left(-1.95*angle)
            t.forward(7)
        else:
            t.right(1.95*angle)
            t.forward(7)
    if t.xcor()>= 300:
        angle = t.heading()
        if 270<= t.heading() <= 360:
            t.left(170-1.95*angle)
            t.forward(7)
        else:
            t.right(1.95*angle-170)
            t.forward(7)


    
