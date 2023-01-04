from tkinter import *
from tkcalendar import Calendar


# def calendar window
def calendar_win(label=None):
    cal_view = Toplevel()
    cal_view.title("Select the date")
    cal = Calendar(cal_view, showothermonthdays=False, selectmode='day', date_pattern='dd/mm/yyyy')
    cal.pack()
    Button(cal_view, text="Confirmer la date", font=('Arial', 14, 'bold'), borderwidth=3, highlightthickness=3,
           bg='black', fg='white',
           command=lambda: set_date(label, cal.get_date(), cal_view)).pack(padx=5, pady=5, ipadx=5, ipady=5)


# #func set date
def set_date(label, date, cal_view):
    label.delete(0, END)
    label.insert(0, date)
    cal_view.destroy()
