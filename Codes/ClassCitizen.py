from tkinter import *
import time
from PIL import ImageTk, Image, ImageFont
import select_photo
from sex import get_sex
from count_generator import numGenerator
from date_generator import calendar_win
from validation import show_card
from printer import printer
import my_directory


class Citizen:
    def __init__(self, root):
        self.root = root
        self.root.title("Carte consulaire")

        # geometry
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.root.minsize(int((self.width * 2) / 3), int((self.height * 2) / 3))

        # Date
        today = StringVar()
        today.set(time.strftime("%d-%m-%Y"))

        global emblem_image
        global flag_image
        global qr
        global flag_image_back
        global filename
        filename = 'none'
        Male = StringVar()
        Female = StringVar()
        card_numb = numGenerator('../Data/card_numb.txt', None, is_to_add=False)

        # background emblem image
        emblem_file = Image.open("../Templates/emblem_bf.jpeg")
        emblem_resized = emblem_file.resize((150, 150), Image.ANTIALIAS)
        emblem_image = ImageTk.PhotoImage(emblem_resized)

        # header flag image
        flag_file = Image.open("../Templates/flag_bf.jpeg")
        flag_resized = flag_file.resize((200, 150), Image.ANTIALIAS)
        flag_image = ImageTk.PhotoImage(flag_resized)

        img = Image.open("../Templates/ID_avatar.jpeg")
        ID_avatar = img.resize((135, 170), Image.ANTIALIAS)
        ID_avatar = ImageTk.PhotoImage(ID_avatar)

        # Frames
        MainFrame = Frame(root, pady=0)
        MainFrame.pack()

        # Header

        Tops = Frame(MainFrame, background='white', bd=10, relief=RIDGE, padx=0, pady=0,
                     highlightthickness=0, height=200, width=900)
        Tops.pack(side=TOP, anchor="w")
        self.emblem = Canvas(Tops, background='#FFFFFF', height=120, width=150, border=0,
                             highlightbackground='#FFFFFF')
        self.emblem.place(x=0, y=0)
        self.emblem.grid(row=0, column=0)
        self.emblem.create_image(90, 70, image=emblem_image)

        title_font_fr = ImageFont.truetype("../Fonts/BERNHC.TTF", size=27)
        title_font_fr = ImageFont.truetype("../Fonts/BERNHC.TTF", size=27)
        self.amb_name = Label(Tops, bg='#FFFFFF', text="AMBASSADE DU BURKINA FASO EN CHINE",
                              font=("Arial", 30, 'bold'),anchor="center")
        self.amb_name.grid(row=0, column=1)
        self.program_title = Label(Tops, bg='#FFFFFF', text="Carte Consulaire", font=("Arial", 25, 'bold'),
                                   anchor="center")
        self.program_title.grid(row=1, column=1)

        self.emblem1 = Canvas(Tops, background='white', height=120, width=170)
        self.emblem1.place(x=0, y=0, anchor="e")
        self.emblem1.grid(row=0, column=2, )
        self.emblem1.create_image(90, 60, image=flag_image)

        # # Body
        ContentFrame = Frame(MainFrame, padx=10, pady=5, highlightthickness=0, borderwidth=0)
        ContentFrame.pack(padx=20, pady=5, anchor="w", side=TOP)

        Middles = Frame(ContentFrame, padx=10, pady=5, highlightthickness=0, borderwidth=0)
        Middles.grid(row=0, column=0)

        # ImageFrame
        PhotoFrame = Frame(ContentFrame, padx=5, highlightthickness=0,
                           borderwidth=0)
        PhotoFrame.grid(row=0, column=1, columnspan=2, sticky=N, padx=20, ipady=0, pady=5)

        # Button
        Buttons = Frame(MainFrame, highlightthickness=0, borderwidth=0, )
        Buttons.pack(padx=20, pady=3, anchor="center")

        ######################################### Widgets ##########################################
        font_size = 18
        font_size1 = 16
        pady = 3
        self.citizen_name = Label(Middles, text="Nom (姓) ： ", font=("Arial", font_size, 'bold'), )
        self.citizen_name.grid(row=0, column=0, sticky=W)
        self.citizen_name_text = Entry(Middles, font=("Arial", font_size1), borderwidth=3, highlightthickness=0,
                                       relief="ridge")
        self.citizen_name_text.grid(row=0, column=2, ipadx=50, pady=pady, sticky=W)

        self.citizen_surname = Label(Middles, text="Prénom (名) ： ", font=("Arial", font_size, 'bold'), )
        self.citizen_surname.grid(row=1, column=0, sticky=W)
        self.citizen_surname_text = Entry(Middles, font=("Arial", font_size1), borderwidth=3, highlightthickness=0,
                                          relief="ridge")
        self.citizen_surname_text.grid(row=1, column=2, ipadx=50, pady=pady, sticky=W)

        self.citizen_birthday = Label(Middles, text="Date de naissance (生日) ： ", font=("Arial", font_size, 'bold'), )
        self.citizen_birthday.grid(row=2, column=0, sticky=W)
        self.citizen_birthday_text = Entry(Middles, font=("Arial", font_size1), borderwidth=3, highlightthickness=0,
                                           relief="ridge", width=18)
        self.citizen_birthday_text.grid(row=2, column=2, ipadx=2, pady=pady, sticky=W)

        self.citizen_birthday_place = Label(Middles, text="Lieu de naissance (出生地) ： ",
                                            font=("Arial", font_size, 'bold'), )
        self.citizen_birthday_place.grid(row=3, column=0, sticky=W)
        self.citizen_birthday_place_text = Entry(Middles, font=("Arial", font_size1), borderwidth=3,
                                                 highlightthickness=0, relief="ridge")
        self.citizen_birthday_place_text.grid(row=3, column=2, ipadx=50, pady=pady, sticky=W)

        self.citizen_sex = Label(Middles, text="Sexe (性别) ： ", font=("Arial", font_size, 'bold'), )
        self.citizen_sex.grid(row=4, column=0, sticky=W)
        self.citizen_sex_female = Checkbutton(Middles, text='Femme', variable=Female,
                                              command=lambda: get_sex(Middles, self.citizen_sex_female,
                                                            self.citizen_sex_male,'female', Female.get()),
                                              font=('Times New Roman', 10, 'normal'),)
        self.citizen_sex_female.grid(row=4, column=2, sticky=W)
        self.citizen_sex_female.deselect()
        self.citizen_sex_male = Checkbutton(Middles, text='Homme', variable=Male,
                                            command=lambda: get_sex(Middles, self.citizen_sex_female,
                                                                        self.citizen_sex_male,'male', Male.get()),
                                            font=('Times New Roman', 10, 'normal'))
        self.citizen_sex_male.grid(row=4, column=2, sticky=W, padx=80)
        self.citizen_sex_male.select()


        self.citizen_tel = Label(Middles, text="Téléphone (电话) ： ", font=("Arial", font_size, 'bold'), )
        self.citizen_tel.grid(row=5, column=0, sticky=W)
        self.citizen_tel_text = Entry(Middles, font=("Arial", font_size1), borderwidth=3, highlightthickness=0,
                                      relief="ridge")
        self.citizen_tel_text.grid(row=5, column=2, ipadx=50, pady=pady, sticky=W)

        self.citizen_email = Label(Middles, text="Email (电子邮件) ： ", font=("Arial", font_size, 'bold'), )
        self.citizen_email.grid(row=6, column=0, sticky=W)
        self.citizen_email_text = Entry(Middles, font=("Arial", font_size1), borderwidth=3, highlightthickness=0,
                                        relief="ridge")
        self.citizen_email_text.grid(row=6, column=2, ipadx=50, pady=pady, sticky=W)

        self.citizen_residence = Label(Middles, text="Residence (住宅) ： ", font=("Arial", font_size, 'bold'), )
        self.citizen_residence.grid(row=7, column=0, sticky=W)
        self.citizen_residence_text = Entry(Middles, font=("Arial", font_size1), borderwidth=3, highlightthickness=0,
                                            relief="ridge")
        self.citizen_residence_text.grid(row=7, column=2, ipadx=50, pady=pady, sticky=W)

        self.citizen_address = Label(Middles, text="Adresse (地址) ： ", font=("Arial", font_size, 'bold'), )
        self.citizen_address.grid(row=8, column=0, sticky=W)
        self.citizen_address_text = Entry(Middles, font=("Arial", font_size1), borderwidth=3, highlightthickness=0,
                                          relief="ridge")
        self.citizen_address_text.grid(row=8, column=2, ipadx=50, pady=pady, sticky=W)

        self.citizen_postal_code = Label(Middles, text="Code postal (邮编号) ： ", font=("Arial", font_size, 'bold'), )
        self.citizen_postal_code.grid(row=9, column=0, sticky=W)
        self.citizen_postal_code_text = Entry(Middles, font=("Arial", font_size1), borderwidth=3, highlightthickness=0,
                                              relief="ridge")
        self.citizen_postal_code_text.grid(row=9, column=2, ipadx=50, pady=pady, sticky=W)

        self.carte_deliver_day = Label(Middles, text="Date de livraison (交货日期) ： ",
                                       font=("Arial", font_size, 'bold'), )
        self.carte_deliver_day.grid(row=10, column=0, sticky=W)
        self.carte_deliver_day_text = Entry(Middles, font=("Arial", font_size1), borderwidth=3, highlightthickness=0,
                                            relief="ridge", width=18)
        self.carte_deliver_day_text.grid(row=10, column=2, ipadx=2, pady=pady, sticky=W)

        self.carte_expire_day = Label(Middles, text="Date d'expiration (到期日) ： ",
                                      font=("Arial", font_size, 'bold'), )
        self.carte_expire_day.grid(row=11, column=0, sticky=W)
        self.carte_expire_day_text = Entry(Middles, font=("Arial", font_size1), borderwidth=3, highlightthickness=0,
                                           relief="ridge", width=18)
        self.carte_expire_day_text.grid(row=11, column=2, ipadx=2, pady=pady, sticky=W)

        self.browser_box = Label(Middles, text="Choisir l'emplacement ： ",
                                      font=("Arial", font_size, 'bold'), )
        self.browser_box.grid(row=12, column=0, sticky=W)
        self.browser_box_text = Entry(Middles, font=('Times New Roman', 10, 'normal'), borderwidth=3,
                                 highlightthickness=0, relief="ridge", width=34)
        self.browser_box_text.insert(0, str(open('../Data/path.txt', 'r').read()))
        self.browser_box_text.grid(row=12, column=2, ipadx=2, pady=pady, sticky=W)
        self.browser = Button(Middles, text="Choisir le dossier", font=('Times New Roman', 10, 'normal'), borderwidth=3,
                              highlightthickness=0,
                              command=lambda: my_directory.get_directory('C:/', Middles, self.browser_box_text))
        self.browser.grid(row=12, column=2, ipadx=10, pady=pady, sticky=E)

        ########################################################## Photos #############################################


        self.citizen_card_num = Label(PhotoFrame, text="Numero de carte (卡号) ： ", font=("Arial", 14, 'bold'), )
        self.citizen_card_num.grid(row=0, column=0, sticky=N, )
        self.citizen_card_num_label = Label(PhotoFrame, text="N°ABFPK/",
                                            font=("Arial", 14, 'bold'), )
        self.citizen_card_num_label.grid(row=1, column=0,ipadx=2, pady=pady, sticky=W)
        self.citizen_card_num_text = Entry(PhotoFrame, font=("Arial", font_size1, 'bold'), borderwidth=3, highlightthickness=0,
                                          relief="ridge", width=11,)
        self.citizen_card_num_text.insert(0, card_numb)
        self.citizen_card_num_text.grid(row=1, column=0, ipadx=2, pady=0, sticky=E)
        Label(PhotoFrame).grid(row=2, column=0, pady=15)
        self.photo = Label(PhotoFrame, image=ID_avatar, relief=RIDGE, borderwidth=5)
        self.photo.image = ID_avatar
        self.photo.grid(row=5, column=0,)
        # ########################################################## Buttons ############################################
        self.btn_birth = Button(Middles, text="Choisir la date", font=('Times New Roman', 10, 'normal'), borderwidth=3,
                                highlightthickness=0, command=lambda: calendar_win(label=self.citizen_birthday_text))
        self.btn_birth.grid(row=2, column=2, ipadx=10, pady=pady, sticky=E)

        self.btn_deliver_day = Button(Middles, text="Choisir la date", font=('Times New Roman', 10, 'normal'),
                                      borderwidth=3,
                                      highlightthickness=0,
                                      command=lambda: calendar_win(label=self.carte_deliver_day_text))
        self.btn_deliver_day.grid(row=10, column=2, ipadx=10, pady=pady, sticky=E)

        self.btn_expire_day = Button(Middles, text="Choisir la date", font=('Times New Roman', 10, 'normal'),
                                     borderwidth=3,
                                     highlightthickness=0,
                                     command=lambda: calendar_win(label=self.carte_expire_day_text))
        self.btn_expire_day.grid(row=11, column=2, ipadx=10, pady=pady, sticky=E)

        self.btn_photo = Button(PhotoFrame, text="Télécharger", background="grey", bd=3, font=("Arial", 16, 'bold'),
                                relief=RIDGE,
                                command=lambda: select_photo.get_image(PhotoFrame, self.photo, self.btn_photo))
        self.btn_photo.grid(row=6, column=0, ipadx=0, ipady=0, padx=2, pady=5)

        self.btn_preview = Button(Buttons, text="Verifier", background="green", bd=3, font=("Arial", 16, 'bold'),
                                  relief=RIDGE,
                                  command=lambda: show_card(self.citizen_card_num_text.get(),
                                                            self.citizen_name_text.get(),
                                                            self.citizen_surname_text.get(),
                                                            self.citizen_birthday_text.get(),
                                                            self.citizen_birthday_place_text.get(),
                                                            self.citizen_address_text.get(),
                                                            self.carte_deliver_day_text.get(),
                                                            self.carte_expire_day_text.get(), select_photo.ID_photo,
                                                            '_', False))

        self.btn_preview.grid(row=0, column=0, ipadx=0, ipady=0, padx=2, pady=2)

        self.btn_print_save = Button(Buttons, text="Sauvegarder", background="blue", bd=3, font=("Arial", 16, 'bold'),
                                     relief=RIDGE, command=lambda: printer(name=self.citizen_name_text.get(),
                                      surname=self.citizen_surname_text.get(), birth=self.citizen_birthday_text.get(),
                                      birth_place=self.citizen_birthday_place_text.get(), tel=self.citizen_tel_text.get(),
                                      email=self.citizen_email_text.get(), add=self.citizen_address_text.get(),
                                      resid=self.citizen_residence_text.get(), DL=self.carte_deliver_day_text.get(),
                                      DE=self.carte_expire_day_text.get(), filename=select_photo.ID_photo,
                                      card_num=self.citizen_card_num_text.get(), cp=self.citizen_postal_code_text.get(),
                                      doc_path=open("../Data/path.txt", 'r').read(), is_printing=False))
        self.btn_print_save.grid(row=0, column=1, ipadx=0, ipady=0, padx=2, pady=2)

        self.btn_save = Button(Buttons, text="Sauvegarder and Imprimer", background="red", bd=3,
                               font=("Arial", 16, 'bold'), relief=RIDGE, command=lambda: printer(
                name=self.citizen_name_text.get(),
                surname=self.citizen_surname_text.get(),
                birth=self.citizen_birthday_text.get(), birth_place=self.citizen_birthday_place_text.get(),
                tel=self.citizen_tel_text.get(), email=self.citizen_email_text.get(),
                add=self.citizen_address_text.get(), resid=self.citizen_residence_text.get(),
                DL=self.carte_deliver_day_text.get(), DE=self.carte_expire_day_text.get(),
                filename=select_photo.ID_photo, card_num=self.citizen_card_num_text.get(),
                cp=self.citizen_postal_code_text.get(),
                doc_path=open("../Data/path.txt", 'r').read(), is_printing=True))
        self.btn_save.grid(row=0, column=2, ipadx=0, ipady=0, padx=2, pady=2)
