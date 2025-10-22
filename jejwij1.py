import turtle as t

t.bgcolor("#606060")
t.hideturtle()
t.pensize(5)
t.pencolor("#FFFFFF")
def _draw():
    while True:
        for i in range(10):
            for i in range(20):
                t.forward(1)
                t.left(1)
            t.clear()

_draw()
t.update()
t.done()