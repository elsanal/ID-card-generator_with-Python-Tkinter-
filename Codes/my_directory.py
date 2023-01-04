from tkinter import filedialog
from tkinter import *


def get_directory(path, Middles, browser_box, is_init=False):
    global selected_path

    if is_init:
        path = open("../Data/path.txt", 'r').read()
        selected_path = path

    else:
        try:
            selected_path = filedialog.askdirectory(initialdir=path, title='Choisir un dossier')
            if selected_path:
                pass
            else:
                selected_path = open("../Data/path.txt", 'r').read()
        except Exception as e:
            print(e)
        open("../Data/path.txt", 'w').write(selected_path)
        browser_box.destroy()
        browser_box = Entry(Middles, font=('Times New Roman', 10, 'normal'), borderwidth=3,
                            highlightthickness=0, relief='ridge', width=34)

        browser_box.delete(0, END)
        browser_box.insert(0, selected_path)
        browser_box.grid(row=12, column=2, ipadx=2, pady=3, sticky=W)

    return selected_path
