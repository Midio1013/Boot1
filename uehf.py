from tkinter import *

root = Tk()
root.geometry('300x200')
root.title("记算器")
for i in range(5):
    root.rowconfigure(i,weight=1)
for i in range(4):
    root.columnconfigure(i,weight=i+1)

for i in range(5):
    for j in range(4):
        la=Label(root,text='{}行{}列'.format(i,j))
        la.grid(row=i,column=j)

root.mainloop()