from tkinter import *


def get_sex(Middles, F_box, M_box, sexe, value):
    global gender
    male = StringVar()
    female = StringVar()
    if value is None:
        gender = 'Homme'
        return gender
    if str(sexe) == str('male'):
        M_box.destroy()
        if str(value) == str(1):
            citizen_sex_male = Checkbutton(Middles, text='Homme', variable=male,
                                           command=lambda: get_sex(Middles,F_box, citizen_sex_male, 'male', male.get()),
                                           font=('Times New Roman', 10, 'normal'))
            citizen_sex_male.grid(row=4, column=2, sticky=W, padx=80)
            citizen_sex_male.select()
            F_box.destroy()
            citizen_sex_female = Checkbutton(Middles, text='Femme', variable=female,
                                             command=lambda: get_sex(Middles, citizen_sex_female, citizen_sex_male, 'female',
                                                                     female.get()),
                                             font=('Times New Roman', 10, 'normal'))
            citizen_sex_female.grid(row=4, column=2, sticky=W)
            citizen_sex_female.deselect()
            gender = 'Homme'
        else:
            citizen_sex_male = Checkbutton(Middles, text='Homme', variable=male,
                                           command=lambda: get_sex(Middles,F_box, citizen_sex_male,  'male', male.get()),
                                           font=('Times New Roman', 10, 'normal'))
            citizen_sex_male.grid(row=4, column=2, sticky=W, padx=80)
            citizen_sex_male.deselect()
            F_box.destroy()
            citizen_sex_female = Checkbutton(Middles, text='Femme', variable=female,
                                             command=lambda: get_sex(Middles, citizen_sex_female, citizen_sex_male, 'female',
                                                                     female.get()),
                                             font=('Times New Roman', 10, 'normal'))
            citizen_sex_female.grid(row=4, column=2, sticky=W)
            citizen_sex_female.select()
            gender = 'Femme'
    else:
        F_box.destroy()
        if str(value) == str(1):
            citizen_sex_female = Checkbutton(Middles, text='Femme', variable=female,
                                           command=lambda: get_sex(Middles, citizen_sex_female, M_box, 'female', female.get()),
                                           font=('Times New Roman', 10, 'normal'))
            citizen_sex_female.grid(row=4, column=2, sticky=W)
            citizen_sex_female.select()
            M_box.destroy()
            citizen_sex_male = Checkbutton(Middles, text='Homme', variable=male,
                                           command=lambda: get_sex(Middles, citizen_sex_female, citizen_sex_male, 'male',
                                                                   male.get()),
                                           font=('Times New Roman', 10, 'normal'))
            citizen_sex_male.grid(row=4, column=2, sticky=W, padx=80)
            citizen_sex_male.deselect()
            gender = 'Femme'

        else:
            citizen_sex_female = Checkbutton(Middles, text='Femme', variable=female,
                                           command=lambda: get_sex(Middles, citizen_sex_female, M_box,  'female', female.get()),
                                           font=('Times New Roman', 10, 'normal'))
            citizen_sex_female.grid(row=4, column=2, sticky=W)
            citizen_sex_female.deselect()

            M_box.destroy()
            citizen_sex_male = Checkbutton(Middles, text='Homme', variable=male,
                                           command=lambda: get_sex(Middles, citizen_sex_female, citizen_sex_male, 'male',
                                                                   male.get()),
                                           font=('Times New Roman', 10, 'normal'))
            citizen_sex_male.grid(row=4, column=2, sticky=W, padx=80)
            citizen_sex_male.select()
            gender = 'Homme'
