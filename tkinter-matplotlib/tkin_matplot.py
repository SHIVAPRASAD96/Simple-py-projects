
from tkinter import *

import matplotlib.pyplot as plt

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

        gui_mat = Menu(menu)

        gui_mat.add_command(label="Bar Graph",command=self.matplot_lib01)

        gui_mat.add_command(label="Scatter Graph",command=self.matplot_lib02)

        gui_mat.add_command(label="Histogram Graph",command=self.matplot_lib03) 

        menu.add_cascade(label="Graphs",menu=gui_mat)
        
    def abtus(self):
        text = Label(self, text="We Desing, Develop and do much more. Website:- code-ed.in")
        text.pack()
        
            
    def showImg(self):
        load = Image.open("python_logo.png")
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

    def matplot_lib01(self):

        x=[10,4,5,6]
        y=[8,6,4,7]

        x2=[1,3,5,9]
        y2=[2,4,6,8]

        plt.bar(x,y,label="Bars 01",color="green")
        plt.bar(x2,y2,label="Bars 02",color="Black")

        plt.xlabel("plot var 01")
        plt.ylabel("Important variable")
        plt.title(" Matplotlib Graph\nFirst One")
        plt.legend()
        #to show it on screen from background
        plt.show()

    def matplot_lib02(self):

        x=[10,4,5,6,89,12]
        y=[8,6,4,7,22,24]

        plt.scatter(x,y,label="Skc sit",color="green",marker="*",s=500)

        plt.xlabel("plot var 01")
        plt.ylabel("Important variable")

        plt.title(" Matplotlib Graph\nFirst One")
        plt.legend()
        #to show it on screen from background
        plt.show()


    def matplot_lib03(self):

        x_ages=[22,25,31,32,134,136,138,124,126,78,98,45,25,15,65,65,45,13,84,31,23]

        ids = [x for x in range(len(x_ages))]

        #plt.bar(ids,x_ages)

        bins =[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

        plt.hist(x_ages,bins,histtype='bar',rwidth=0.8)

        plt.xlabel("plot var 01")
        plt.ylabel("Important variable")
        plt.title(" Matplotlib Graph\nFirst One")
        #to show it on screen from background
        plt.legend()
        plt.show()

        
     
root=Tk()

root.geometry("600x600")

app=window(root)

root.mainloop()
