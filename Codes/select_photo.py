from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from errors import photo_not_selected


def get_image(photo_frame, photo, btn_photo, is_init=False):
    global ID_photo

    if is_init:
        ID_photo = None

    else:
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("All files", "*.*"),
                                                         ("png files", "*.png"),
                                                         ("jpeg files", "*.jpeg"),
                                                         ("jpg files", "*.jpg")))

        if len(filename) == 0:
            return photo_not_selected(None)
        img = Image.open(filename)
        ID_photo = img.resize((135, 170))
        ID_photo_show = ImageTk.PhotoImage(ID_photo)

        photo.destroy()
        photo = Label(photo_frame, image=ID_photo_show, relief=RIDGE, borderwidth=5)
        photo.image = ID_photo_show
        photo.grid(row=5, column=0,)

        btn_photo.destroy()
        btn_photo = Button(photo_frame, text="Télécharger", background="grey", bd=3,
                           font=("Arial", 16, 'bold'),
                           relief=RIDGE, command=lambda: get_image(photo_frame, photo, btn_photo))
        btn_photo.grid(row=6, column=0, ipadx=0, ipady=0, padx=2, pady=5)
    return ID_photo
