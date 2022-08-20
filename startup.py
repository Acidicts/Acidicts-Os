import tkinter as tk
import os
import sys

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=500, bg="#263D42")
canvas.grid(columnspan=1, rowspan=10)


def login():
    os.system("login.py")
    sys.exit()


def setup():
    os.system("setup.py")
    sys.exit()


tit = tk.Label(text="Login or Setup")
tit.grid(column=0, row=1)

con = tk.Button(text="Setup", command=setup, bg="black", fg="white")
con.grid(column=0, row=3)

log = tk.Button(text="Login", command=login, bg="black", fg="white")
log.grid(column=0, row=4)

root.mainloop()
