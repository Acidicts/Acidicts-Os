import tkinter as tk
import os
import time
import sys

global on


def on(on):
    on = 1
    if on == 1:
        print(" ")

on(on)

root = tk.Tk()

global rebot
global lock
global shutdown


def menu():
    global rebot
    global lock
    global on
    global shutdown

    if on == 1:
        def reboot():
            time.sleep(1)
            os.system("startup.py")
            sys.exit()

        def lok():
            os.system("login.py")
            sys.exit()

        def shut():
            sys.exit()

        rebot = tk.Button(text="Restart", bg="#263D42", fg="white", command=reboot)
        rebot.grid(column=0, row=196)

        lock = tk.Button(text="Lock", bg="#263D42", fg="white", command=lok)
        lock.grid(column=0, row=197)

        shutdown = tk.Button(text="Shutdown", bg="#263D42", fg="white", command=shut)
        shutdown.grid(column=0, row=198)

        on = 0

    else:
        on = 1

        rebot.grid_remove()
        shutdown.grid_remove()
        lock.grid_remove()


class Application:
    def __init__(self, name, icon, file_loc, x, y, master):
        self.x = x
        self.y = y
        self.icon = icon
        self.master = master
        self.file_loc = file_loc
        self.name = name
        self.display()
        self.app = None

    def display(self):
        self.app = tk.Button(self.master, text=self.name, bg='#30D5C8', fg="white", command=self.com)
        self.app.grid(column=self.x, row=self.y)

    def com(self):
        os.system(self.file_loc)


canvas = tk.Canvas(width=1000, height=700, bg="#263D42")
canvas.grid(columnspan=1000, rowspan=2000)

options = tk.Button(text="Options", padx=10, pady=10, command=menu)
options.grid(column=0, row=1999)

notebook = Application(name="notebook", icon=None, file_loc="notebook.py", x=1, y=10, master=root)
calculator = Application(name="Calculator", icon=None, file_loc="calculator.py", x=1, y=15, master=root)

root.mainloop()
