from tkinter import *

root =Tk()

def print_loop(event):

    for x in range(5,50,5):
        print("PRinting numbers :\t",x);

button_1 = Button(root,text="Printing the LOOP Thing",command=print_loop,fg="red");
button_1.bind("Button-1",print_loop)
button_1.pack();
        

root.mainloop()
