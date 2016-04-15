from tkinter import *

root = Tk()

topFrame = Frame(root);
topFrame.pack()

bottomFrame = Frame(root);
bottomFrame.pack(side=BOTTOM)

#these are just widgets ,that they are just created
button1 = Button(topFrame,text="Button 1",fg="green");
button2 = Button(topFrame,text="Button 2",fg="red");
button3 = Button(topFrame,text="Button 3",fg="blue");
button4 = Button(bottomFrame,text="Button 4",fg="pink");

#packing the buttons
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)


root.mainloop()
