from pyautogui import *
from time import sleep as slp

def _kdw(keyy):
    keyDown(keyy)
    keyUp(keyy)
hotkey("Win","9")
slp(3)
click(1187,698,duration=0.3)
typewrite("zhongguo")
_kdw("space")
_kdw("enter")
click(1216,1143,duration=0.3)
slp(8)
click(1144,1339,duration=0.3)
slp(6)
scroll(-200)
slp(2)
hotkey("Win","4")
hotkey("Ctrl","A")
hotkey("Ctrl","C")
slp(3)
hotkey("Win","8")
hotkey("Ctrl", "V")
