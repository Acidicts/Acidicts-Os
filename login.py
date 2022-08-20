import tkinter as tk
import os
import sys

root = tk.Tk()

canvas = tk.Canvas(bg="#263D42")
canvas.pack()


def c():
    e = entry1.get()
    a = entry2.get()

    usernames = []
    passwords = []

    for n in range(100):
        try:
            with open("User/" + str(n) + ".txt", "r") as f:
                u3 = f.read()
                username, password = u3.split(",")
                usernames.append(username)
                passwords.append(password)
                f.close()
        except FileNotFoundError:
            print("Oof")

    print(usernames + passwords)

    for i in range(len(usernames)):
        if e == usernames[i]:
            if a == passwords[i]:
                os.system("acidicts.py")
                sys.exit()
    print("Failed")




entry1 = tk.Entry(text="Username", bg="#263D42", fg="white")
entry1.pack()

entry2 = tk.Entry(text="Password", bg="#263D42", fg="white")
entry2.pack()

enter = tk.Button(text="Enter", command=c)
enter.pack()

root.mainloop()
