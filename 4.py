from pyautogui import *

sleep(5)
def cf(ax,ay,bx,by):
    moveTo(ax,ay,duration=0.3)
    keyDown("Ctrl")
    dragTo(bx,by,duration=0.3)
    keyUp("Ctrl")
    click(2000,200)
def tf(ax,ay,bx,by):
    moveTo(ax, ay, duration=0.3)
    dragTo(bx, by, duration=0.3)
    click(2000, 200)

cf(1435,341,1308,341)
cf(1544,341,1308,341)
cf(1797,341,1308,341)
tf(1922,341,1308,341)
tf(1684,341,1308,341)
tf(2014,341,1308,341)