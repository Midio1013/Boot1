import sys
import time
from turtle import *
import turtle as tu

v=tu.Pen()
c=0
while True:
    b=numinput("Title", "请输入边数", 0, 0, 100000)
    try:
        b=int(b)
    except TypeError as fg:
        print("Error:"+str(fg))
        sys.exit()
    for i in range(b):
        v.forward(2)
        v.left(360/b)
    v.penup()
    c+=100
    v.setx(c)
    v.pendown()

turtle.done()