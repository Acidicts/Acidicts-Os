import os.path
from tkinter import *
import sys

def main():
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None

class Window:
    def __init__(self, root):
        self.u = "1"
        self.root = root
        self.root.geometry('750x500')
        self.root.title("Setup")

        # Creates Text
        self.l = Label(self.root, text="Username")
        self.l.grid(row=0, column=3)

        self.textspace = Entry(self.root)
        self.textspace.grid(row=1, column=3)

        self.la = Label(self.root, text="Password")
        self.la.grid(row=3, column=3)

        self.textspace2 = Entry(self.root)
        self.textspace2.grid(row=4, column=3)

        # Create open and save
        Button(self.root, text='Save', command=self.setup).grid(row=6, column=3)

        return None

    def setup(self):
        self.name = self.textspace.get()

        if os.path.isfile("User/1.txt"):
            self.u = "2"
        elif os.path.isfile("User/2.txt"):
            self == "3"
        else:
            self.u = "1"

        with open("User/" + self.u + ".txt", "w+") as file:
            file.writelines(self.textspace.get() + ",")
            file.writelines(self.textspace2.get())
            file.close()

        self.le = Label(text="User Added")
        self.le.grid(row=7, column=3)




if __name__ == '__main__':
    main()
