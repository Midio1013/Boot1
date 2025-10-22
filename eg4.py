import easygui as eg
import time as tm
from tkinter import messagebox

s=0
while True:
    ome=eg.buttonbox(msg="Login",title="None",choices=["Login","Sign Up"])
    if ome=="Sign Up":
        a=eg.enterbox(msg="输入你的帐号",title="帐号注册")
        b=eg.passwordbox(msg="输入你的密码",title="帐号注册")
    elif ome=="Login":
        c=eg.enterbox(msg="输入你的帐号",title="帐号登录")
        d=eg.passwordbox(msg="输入你的密码",title="帐号登录")
        if a == c:
            e=True
        else:
            e=False
        if b==d:
            f=True
        else:
         f=False
        if s>4:
            if e and f:
                eg.msgbox(msg="登陆成功",title="Login Done!")
                tm.sleep(3)
                messagebox.showinfo("Software End","Thank you for your use!")
                break
            else:
                s+=1
                eg.msgbox(msg="Error",title="Try again!")
                continue
        else:
            eg.msgbox("Time out,Please try again!","Please wait 1 minute!")
            tm.sleep(3)
            s=0