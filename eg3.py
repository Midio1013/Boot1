import easygui as eg

m=0
a=eg.buttonbox(msg="""17//2=?
a.2,b.4,c.7,d.6""",title="Title",choices=("a","b","c","d"))
if a=="c":
    eg.msgbox(title="Title",msg="Yes!")
    m+=6
elif a=="b":
    eg.msgbox(title="Title",msg="No!")
elif a=="d":
    eg.msgbox(title="Title",msg="No!")
elif a=="a":
    eg.msgbox(title="Title",msg="No!")
a=eg.buttonbox(msg="""17//3=?
a.9,b.2,c.5,d.3""",title="Title",choices=("a","b","c","d"))
if a=="c":
    eg.msgbox(title="Title",msg="Yes!")
    m+=6
elif a=="b":
    eg.msgbox(title="Title",msg="No!")
elif a=="d":
    eg.msgbox(title="Title",msg="No!")
elif a=="a":
    eg.msgbox(title="Title",msg="No!")
a=eg.ynbox(msg="a+a=b?",title="Question&Answer",choices=("Yes","No"))
if not a:
     eg.msgbox(msg="Yes,great!",title="Question&Answer")
     m+=6
else:
    eg.msgbox(msg="No,Keep up the good work!", title="Question&Answer")
a=eg.enterbox("1+362625=?","Title")
if a=="362626":
    eg.msgbox(msg="Yes,great!",title="Question&Answer")
    m+=6
else:
    eg.msgbox(msg="No,Keep up the good work!", title="Question&Answer")
eg.msgbox("Store="+str(m),"Title")