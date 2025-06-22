from tkinter import messagebox as msgb
import easygui
import random

m=10
for i in range(6):
    Yui=easygui.enterbox(title="Random",msg="Press 1 Number(1~99)")
    o=random.randint(1,100)
    if Yui==str(o):
        m+=6
    else:
        m-=7
msgb.showinfo('Random','Store='+str(m))