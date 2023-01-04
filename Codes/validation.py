import os
import textwrap
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
import time

import sex
from errors import photo_not_selected


def show_card(card_numb, name, surname, birth, birth_place, add, DL, DE, ID_photo, path, is_save=False):
    front_template = Image.open("../Templates/template_front.jpg")
    HEIGHT = 638
    WIDTH = 1039

    front_template = front_template.resize((550, 300), Image.ANTIALIAS)
    fr_font = ImageFont.truetype("../Fonts/times-new-roman.ttf", size=20, layout_engine=ImageFont.LAYOUT_RAQM)
    fr_font_input = ImageFont.truetype("../Fonts/times-new-roman.ttf", size=18, layout_engine=ImageFont.LAYOUT_RAQM)
    fr_font_input_bold = ImageFont.truetype("../Fonts/times new roman bold.ttf", size=18,
                                            layout_engine=ImageFont.LAYOUT_RAQM)
    zh_font = ImageFont.truetype("../Fonts/NotoSansSC-Medium.otf", size=14, layout_engine=ImageFont.LAYOUT_RAQM)
    title_font_fr = ImageFont.truetype("../Fonts/BERNHC.TTF", size=25, layout_engine=ImageFont.LAYOUT_RAQM)
    title_font_zh = ImageFont.truetype("../Fonts/NotoSansSC-Medium.otf", size=21, layout_engine=ImageFont.LAYOUT_RAQM)
    if not photo_not_selected(ID_photo):
        front_template.paste(im=ID_photo, box=(31, 83, 166, 253))
        draw = ImageDraw.Draw(front_template)

        draw.text((44, 15), f"CARTE D'IDENTITÉ CONSULAIRE/", fill='green', font=title_font_fr, language='fr')
        draw.text((337, 14), "布基纳法索领事卡", fill='green', font=title_font_zh, language='zh-Hans')
        draw.text((240, 50), f"N°ABFPK/{card_numb}", fill='black', font=fr_font_input_bold, language='fr')

        draw.text((180, 78), "Nom", fill='black', font=fr_font, language='fr')
        draw.text((222, 78), "/性:", fill='black', font=zh_font, language='zh-Hans')
        draw.text((250, 80), str(name), fill='black', font=fr_font_input_bold, language='fr')

        draw.text((180, 110), "Prénoms", fill='black', font=fr_font, language='fr')
        draw.text((252, 109), "/名:", fill='black', font=zh_font, language='zh-Hans')
        draw.text((285, 111), str(surname), fill='black', font=fr_font_input_bold, language='fr')
        if sex.gender == 'Femme':
            draw.text((180, 142), "Née le", fill='black', font=fr_font, language='fr')
            draw.text((233, 142), "/出日:", fill='black', font=zh_font, language='zh-Hans')
            draw.text((275, 143), str(birth), fill='black', font=fr_font_input_bold, language='fr')
            draw.text((360, 143), '  A  ' + str(birth_place), fill='black',
                      font=fr_font_input, language='fr')
        else:
            draw.text((180, 142), "Né le", fill='black', font=fr_font, language='fr')
            draw.text((225, 142), "/出日:", fill='black', font=zh_font, language='zh-Hans')
            draw.text((270, 143), str(birth), fill='black', font=fr_font_input_bold, language='fr')
            draw.text((355, 143), '  A  ' + str(birth_place), fill='black',
                  font=fr_font_input, language='fr')

        draw.text((180, 174), "Délivré le", fill='black', font=fr_font, language='fr')
        draw.text((262, 174), "/颁发时间:", fill='black', font=zh_font, language='zh-Hans')
        draw.text((335, 176), str(DL), fill='black', font=fr_font_input, language='fr')

        draw.text((180, 206), "Expire le", fill='black', font=fr_font, language='fr')
        draw.text((253, 207), "/到期时间:", fill='black', font=zh_font, language='zh-Hans')
        draw.text((325, 209), str(DE), fill='black', font=fr_font_input, language='fr')

        back_template = Image.open("../Templates/template_back.jpg")
        back_template = back_template.resize((550, 300), Image.ANTIALIAS)
        draw = ImageDraw.Draw(back_template)
        draw.text((125, 25), "AMBASSADE DU BURKINA FASO À BEIJING", fill='green', font=title_font_fr, language='fr')
        draw.text((230, 60), "布基纳法索驻大使馆", fill='green', font=title_font_zh, language='zh-Hans')
        draw.text((310, 200), "/地址：", fill='black', font=zh_font, language='zh-Hans')
        add = "Addresse de l'intéressé         " + add
        lines = textwrap.wrap(str(add), width=50)
        y_text = 200
        for line in lines:
            width, height = fr_font.getsize(line)
            draw.text((125, y_text), line, font=fr_font, fill='black', language='fr')
            y_text += height

        if is_save:
            time.sleep(0.5)
            front_template = front_template.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
            back_template = back_template.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
            qr_code_image = Image.open(str(os.path.join(path, 'QrCode.jpeg')))
            qr_code_image = qr_code_image.resize((170, 170), Image.ANTIALIAS)
            back_template.paste(im=qr_code_image, box=(55, 425, 225, 595))
            front_template.save(f"{path}page_devant.png")
            back_template.save(f"{path}page_arriere.png")

        else:
            card = Toplevel(borderwidth=1, relief=RIDGE, pady=20, padx=20)
            card.title("Carte consulaire")

            # Main pages
            FrontPage = Frame(card, borderwidth=1, relief=RIDGE, border=5, padx=10, pady=10)
            FrontPage.pack()

            front_template_show = ImageTk.PhotoImage(front_template)
            photo = Label(FrontPage, image=front_template_show, relief=RIDGE, borderwidth=5)
            photo.image = front_template_show
            photo.pack()

            back_template_show = ImageTk.PhotoImage(back_template)
            photo1 = Label(FrontPage, image=back_template_show, relief=RIDGE, borderwidth=5)
            photo1.image = back_template_show
            photo1.pack()
