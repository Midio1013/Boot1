import turtle as t
a=t.Pen()
a.setheading(270)
a.pencolor("yellow")
a.dot(450)
a.speed(0)

def pud(x,y):
    a.penup()
    a.goto(x,y)
    a.pendown()

a.pencolor("#000000")
a.pensize(1)
pud(-170,0)
sz=1
for i in range(90):
    a.forward(3)
    a.left(1)
    sz+=0.2
    a.pensize(sz)
for i in range(90):
    a.forward(3)
    a.left(1)
    sz-=0.2
    a.pensize(sz)
a.pencolor("#FFFFFF")
pud(-140,100)
a.pensize(45)
a.setheading(22.5)
a.circle(-100,60)
a.pencolor("#000000")
a.dot(45)
pud(30,100)
a.pencolor("#FFFFFF")
a.setheading(22.5)
a.circle(-100,60)
a.pencolor('#000000')
a.dot(45)

t.done()