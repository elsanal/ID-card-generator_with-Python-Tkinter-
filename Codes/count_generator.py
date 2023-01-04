import os


def numGenerator(path, card_num, is_to_add=False):
    path = path
    numb = "1"
    if os.path.exists(path):
        if is_to_add:
            with open(path, 'w') as file:
                file.write(str(card_num))
                numb = card_num
        else:
            file = open(path, 'r')
            numb = file.read()
            file.close()
    else:
        with open(path, 'x') as file:
            file.write(numb)

    if len(numb) < 3:
        numb = (5 - len(numb))*'0' + numb
    return numb
