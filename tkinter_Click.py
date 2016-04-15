from tkinter import *

root =Tk()

def left(event):

    print("Left Button\n");
                
def right(event):

    print("Right button\n");

def middle_click(event):

    print("Middle\n");

frame =Frame(root, width=600,height=400)
frame.bind("<Button-1>",left)

#scroll is middle button
frame.bind("<Button-2>",middle_click)
frame.bind("<Button-3>",right)
frame.pack()

root1.mainloop()
