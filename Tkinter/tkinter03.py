import sys
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

root.title("My Calci :D ")

num1=StringVar()

topframe = Frame(root)
topframe.pack(side  Top)
txtDisplay Entry(frame,textvariable  num1, bd 20, insertwidth 1,font 20)
txtDisplay.pack(side  Top)  



root.mainloop()

