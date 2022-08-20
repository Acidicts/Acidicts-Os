import os
import sys
from tkinter import *

def main():
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None

class Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry('750x500')
        self.root.title("Notepad")

        # Creates Text
        self.textspace = Text(self.root)
        self.textspace.grid(row=0, column=0)

        # Create open and save
        Button(self.root, text='Save', command=self.savefile).grid(row=0, column=1)
        Button(self.root, text='Open', command=self.openfile).grid(row=0, column=2)
        Button(self.root, text='Close', command=self.close).grid(row=1, column=2)
        Button(self.root, text='Delete', command=self.delete).grid(row=1, column=1)


        pass

    def close(self):
        sys.exit()

    def delete(self):
        deletegui = Tk()
        deletegui.geometry('560x50')
        filecontents = self.textspace.get(0.0, END)

        def deletefile():
            os.remove("Notes/" + file_name.get() + ".txt")
            deletegui.destroy()

        Label(deletegui, text="File Name").grid(row=0, column=0)
        file_name = Entry(deletegui, width=40)
        file_name.grid(row=0, column=1)

        Button(deletegui, text="Delete", command=deletefile).grid(row=0, column=2)

        return None

    def savefile(self):
        savegui = Tk()
        savegui.geometry('560x50')
        filecontents = self.textspace.get(0.0, END)

        def writefile():
            with open("Notes/" + file_name.get() + ".txt", "w+") as file:
                file.write(filecontents)
                file.close()
                savegui.destroy()

        Label(savegui, text="File Name").grid(row=0, column=0)
        file_name = Entry(savegui, width=40)
        file_name.grid(row=0, column=1)

        Button(savegui, text="Save", command=writefile).grid(row=0, column=2)

        return None

    def openfile(self):
        opengui = Tk()
        opengui.geometry('560x50')

        def opennew():
            try:
                with open("Notes/" + file_name.get() + ".txt", "r") as file:
                    self.textspace.delete(0.0, END)
                    self.textspace.insert(0.0, file.read())
                    file.close()
                    opengui.destroy()
            except FileNotFoundError:
                file_name.delete(0.0, END)
                file_name.insert(0.0, "File Not Found")

        Label(opengui, text="File Name").grid(row=0, column=0)
        file_name = Entry(opengui, width=40)
        file_name.grid(row=0, column=1)

        Button(opengui, text="Open", command=opennew).grid(row=0, column=2)

        return None

if __name__ == '__main__':
    main()