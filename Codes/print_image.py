import win32print, win32ui
from PIL import Image, ImageWin


def image_printer(image_to_print):

        #printable area
        Horiz = 85
        Vert = 54

        #Logpixel
        LOGPIXELX = 8
        LOGPIXELY = 10

        #physical dim
        PHYSICAL_WIDTH = 85
        PHYSICAL_HEIGTH = 54

        #OFFSET
        PHYSICAL_OFFSET_X = 86
        PHYSICAL_OFFSET_Y = 55

        #get Printer
        printer_name = win32print.GetDefaultPrinter()
        filename = image_to_print

        #create device context
        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(printer_name)
        printable_area = hDC.GetDeviceCaps(Horiz), hDC.GetDeviceCaps(Vert)
        printer_size = hDC.GetDeviceCaps(PHYSICAL_WIDTH), hDC.GetDeviceCaps(PHYSICAL_HEIGTH)
        printer_margin = hDC.GetDeviceCaps(PHYSICAL_OFFSET_X), hDC.GetDeviceCaps(PHYSICAL_OFFSET_Y)

        #open image
        bmp = Image.open(filename)
        ratios = [1.0*printable_area[0]/bmp.size[0], 1.0*printable_area[1]/bmp.size[1]]
        scale = min(ratios)

        #start printing
        hDC.StartDoc(filename)
        hDC.StartPage()

        dib = ImageWin.Dib(bmp)
        scaled_width, scaled_height = [int(scale*i) for i in bmp.size]
        x1 = int((printer_size[0]-scaled_width)/2)
        y1 = int((printer_size[1]-scaled_height)/2)
        x2 = x1 + scaled_width
        y2 = y1 + scaled_height

        dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))

        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()