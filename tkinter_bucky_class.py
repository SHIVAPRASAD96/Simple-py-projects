from tkinter import *


class shiva_buttons:

    def __init__(self,master):

        frame =Frame(master);
        frame.pack()

        self.print_Button= Button(frame,text="Print Message",command=self.printMessage)
        self.print_Button.pack(side=RIGHT);

        self.quit_Button= Button(frame,text="QUIT ",command=frame.quit)
        self.quit_Button.pack(side=LEFT);

    def printMessage(self):
        print("How it workd");

root = Tk()

s = shiva_buttons(root)

root.mainloop()
