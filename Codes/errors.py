from tkinter import messagebox


def photo_not_selected(photo):
    no_photo = False
    if photo is None:
        messagebox.showerror("Erreur", "Sélectionnez la photo d'identité!")
        no_photo = True
    return no_photo


def empty_input(inputs, is_important=True):
    is_error = False
    alt_msg = ''

    for elem in inputs:
        if len(elem['value']) < 2:
            if not elem['important']:
                alt_msg = "ou tapez Néant"
            messagebox.showerror("Erreur", f"Veuillez remplir la case {elem['key']} {alt_msg}")
            is_error = True
            return is_error
        if elem['value'] == ' ' * len(elem['value']):
            if not elem['important']:
                alt_msg = "ou tapez Néant"
            messagebox.showerror("Erreur", f"Veuillez remplir la case {elem['key']} {alt_msg}")
            is_error = True
            return is_error
    return is_error
