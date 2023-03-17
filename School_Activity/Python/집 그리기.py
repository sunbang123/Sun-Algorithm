import math
import turtle

t = turtle.Turtle()
root = math.sqrt

t.shape("turtle")

a = 0

t.fd(70)
t.left(90)
t.fd(75)
t.right(90)
t.fd(25)

t.left(135)

while a < 2:
   
    t.fd(100*root(2))
    t.left(90)

    a += 1;

t.left(45)

t.fd(25)
t.right(90)
t.fd(75)
t.left(90)
t.fd(50)

a = 0

while a < 4:

    t.fd(50)
    t.left(90)

    a += 1;

t.penup()
t.left(90)
t.fd(20)
t.right(90)
t.fd(8)
t.pendown()

a = 0

while a < 4:

    t.fd(7)
    t.left(90)

    a += 1;

t.penup()
t.fd(25)
