#more on tkiter

from tkinter import *

from PIL import Image, ImageTk

class window(Frame):
    def __init__(self,master= None):
        Frame.__init__(self,master)
        self.master=master;
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

      #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Welocome to GUI PYTHON")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)


        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)    

        # create the file object)
        login = Menu(menu)

        login.add_command(label="Login", command=self.Entry)

        #added "file" to our menu
        menu.add_cascade(label="enter", menu=login)

        aboutus = Menu(menu)

        aboutus.add_command(label="About Us",command=self.abtus)

        menu.add_cascade(label="About us", menu=aboutus)
        
    def abtus(self):
        text = Label(self, text="We Desing, Develop and do much more. Website:- code-ed.in")
        text.pack()
        
            
    def showImg(self):
        load = Image.open("py001.jpg")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


    def showText(self):
        text = Label(self, text="Welcome to Tkinter Version By SHIVAPRASAD. version 1.0")
        text.pack()

    def Entry(self):
        L1 = Label(root, text="User Name")
        L1.pack( side = LEFT)
        E1 = Entry(root, bd =5,bg="red")
        E1.pack(side = RIGHT)

        L2 = Label(root, text="Pass Word")
        L2.pack( side = LEFT)
        E2 = Entry(root, bd =5, bg="blue")
        E2.pack(side = RIGHT)
        

    def client_exit(self):
        exit()

root=Tk()

root.geometry("600x600")

app=window(root)

root.mainloop()
