from easygui import *
import sys
from pathlib import Path

jka=open("pmw.opentupyfinegitasmetaghost","r")
mica = jka.read()
l = 3
m =["D:\Py_Pj\gys\image\lj2-aaea2a92746432d6cc7d71e8e626c30b_1440w.gif"]
klf=True
while l > 0:
    if klf:
        b = passwordbox( "Enter Password" , "E-Photo" )
    if b == mica :
        klf=False
        v = buttonbox("Choice Mode", "E-Photo", choices=["See", "Add", "ReSetPassword","Exit"])
        if v=="See":
            for i in range(0,len(m)):
                msgbox(msg="1", title="Image1", ok_button="OK", image=m[i])
                continue
        elif v=="Add":
            add=enterbox("Enter Photo Path(Only .jpg/.png/.gif/.jpeg/.ico)",title="E-Photo")
            add_p=Path(add)
            if add_p.is_file():
                m.append(add)
                msgbox("Add Done!","E-Photo")
            else:
                msgbox("Error Path","E-Photo")
                continue
        elif v=="Exit":
            sys.exit()
        elif v=="ReSetPassword":
            oldp=passwordbox("OldPassword:","E-Photo")
            if oldp==mica:
                newp=passwordbox("NewPassword:","E-Photo")
                m=open("pmw.opentupyfinegitasmetaghost","w")
                m.write(newp)
            elif oldp!=mica:
                msgbox( "Password Error!","E-Photo")
                continue
            else:
                continue
        elif v=="Other Tools":
            jika=buttonbox("Choice Mode\n(Text Writer)","Other Tools",choices = ["New","Delete","Read","Add"])
            if jika=="New":
                enterbox("")
        else:
            continue
    else:
        msgbox("Password Error!,Count:" + str(l - 1), "E-Photo")
        l -= 1
        klf=True
msgbox("Exit,Time out!", "E-Photo")