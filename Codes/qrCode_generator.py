import qrcode


def qr_code_generator(data, path):
    # create instance of qr code
    qr = qrcode.QRCode(version=1, box_size=50, border=1)

    # add data to the qr code
    qr.add_data(data)
    qr.make(fit=True)

    code = qr.make_image(fill_color='black', back_color='white')
    code.save(f'{path}/QrCode.jpeg')
