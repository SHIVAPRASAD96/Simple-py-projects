from tkinter import *

root = Tk()

one= Label(root,text="One",bg="red",fg="white")
one.pack()

two= Label(root,text="Two",bg="green",fg="white")
two.pack(fill=X)

three= Label(root,text="Three",bg="blue",fg="white")
three.pack(side=RIGHT,fill=Y)


root.mailoop()
