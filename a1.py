import easygui as e

l=['Chinese','Math','English','Art','Music','Physical Education','Geography','History']
m=['']
while True:
    c=e.buttonbox('Please select one.','Volcano library',choices=['Borrow','Still'])
    if c=='Borrow':
        a=e.enterbox('What are you want search book?','Volcano library')
        if a in l:
            b=e.ynbox('Do you want to borrow this book?','Volcano library')
            if b:
                e.msgbox('The loan was successful!','Volcano library')
            else:
                e.msgbox('Bye!','Volcano library')
        else:
            e.msgbox("404 Not found!","Volcano library")
