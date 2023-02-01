from tkinter import *
from tkinter import Entry, Label, Button
from datetime import date

window = Tk()
window.title("Age calculator")
window.geometry('300x150')



def age():
    today = date.today()
    print(today)
    year = int(inputFiled.get())
    if year <= 0 or year >= 2023:
        label['text'] = 'Xato'
    else:
        jj = today.year - year

        label['text'] = 'You ' + str(jj) + ' years old'



inputFiled = Entry(window, width=20, font=22)
button = Button(window, text='Age', font=20, pady=10, command=age)
label = Label(window, text='Enter year', font=20)

inputFiled.pack()
button.pack()
label.pack()

window.mainloop()
