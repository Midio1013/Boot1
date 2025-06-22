import easygui as eg
m=0
a=eg.ynbox(msg="6256+7172=13328?",title="Question&Answer",choices=("Yes","No"))
if not a:
     eg.msgbox(msg="Yes,great!",title="Question&Answer")
     m+=1
else:
    eg.msgbox(msg="No,Keep up the good work", title="Question&Answer")
a = eg.ynbox(msg="Math=Mathematics?", title="Question&Answer", choices=("Yes", "No"))
if a:
    eg.msgbox(msg="Yes,great!", title="Question&Answer")
    m+=1
else:
    eg.msgbox(msg="No,Keep up the good work", title="Question&Answer")
a = eg.ynbox(msg="Zh-CN=Chinese Simplified?", title="Question&Answer", choices=("Yes", "No"))
if a:
    eg.msgbox(msg="Yes,great!", title="Question&Answer")
    m+=1
else:
    eg.msgbox(msg="No,Keep up the good work", title="Question&Answer")
a = eg.ynbox(msg="En-UK=English?", title="Question&Answer", choices=("Yes", "No"))
if a:
    eg.msgbox(msg="Yes,great!", title="Question&Answer")
    m+=1
else:
    eg.msgbox(msg="No,Keep up the good work", title="Question&Answer")
eg.msgbox(msg=f"Score={m},thank you for your attend！",title="Question&Answer")
print(a)