from tkinter import *
from ClassCitizen import Citizen
from init_code import initializer


if __name__ == '__main__':
    root = Tk()
    root.iconbitmap("../Templates/icon.ico")
    initializer()
    app = Citizen(root)
    root.mainloop()
