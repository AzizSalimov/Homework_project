import codecs
import tkinter as tk
import csv, os
from tkinter import *
from tkinter import messagebox, Label, Entry, StringVar, Radiobutton
from ffff.Glass.Hoework.Car import Car
from tkcalendar import DateEntry

window = tk.Tk()
window.title("Rent a car")
window.geometry('700x700')

cars = []


def add():
    carss = Car(
        name.get(),
        full_name_.get(),
        age.get(),
    )
    cars.append(carss.get_attr(as_dict=True))
    messagebox.showinfo("Added machine data")


def save():
    with open('../car.csv', 'a', newline='\n') as f:
        header = ["Name,Age,Car name,Color,price"]
        csv_writer = csv.DictWriter(f, header)
        if os.path.getsize('../car.csv') == 0:
            csv_writer.writeheader()
        csv_writer.writerows(cars)
        messagebox.showinfo('Information', 'Saved successfully')


def clear():
    name.delete(0, END)
    full_name_.delete(0, END)
    age.delete(0, END)


def information():
    file_name = "../car.csv"
    encoding = 'utf-8'

    with codecs.open(file_name, "r", encoding) as fp:
        reader = csv.reader(fp)
        for i in reader:
            print(i)


# your name
name_ = Label(window, text='Your name:')
name_.place(x=165, y=10)
name = Entry(window, width=30, borderwidth=3)
name.place(x=230, y=10)

# your full name
full_ = Label(window, text='Your full name:')
full_.place(x=165, y=35)
full_name_ = Entry(window, width=30, borderwidth=3)
full_name_.place(x=255, y=35)
# # age
#
age_ = Label(window, text='Your age:')
age_.place(x=165, y=60)
age = Entry(window, width=30, borderwidth=3)
age.place(x=220, y=60)

# # car name
gender = StringVar()
gender_Ty = {"bmw_1": "BMW I7 EV", "bmw_2": "BMW X3 M SPORTS", "bmw_3": "BMW GRAN COUPE",
             "bmw_4": "BMW M5 SEDAN", "bmw_5": "BMW I7 ELECTERIC",
             "bmw_6": "BMW Z4 ROADSTER", "bmw_7": "BMW M8 COMPETITION"}
gender_label = Label(window, text='Car name:', padx=20, pady=95)
gender_label.grid(row=30, column=2)
bmw_1 = Radiobutton(
    window, text=gender_Ty.get('bmw_1'), value='bmw_1', variable=gender
)
bmw_1.place(x=110, y=125)

bmw_2 = Radiobutton(
    window, text=gender_Ty.get('bmw_2'), value='bmw_2', variable=gender
)
bmw_2.place(x=200, y=125)

bmw_3 = Radiobutton(
    window, text=gender_Ty.get('bmw_3'), value='bmw_3', variable=gender
)
bmw_3.place(x=340, y=125)

bmw_4 = Radiobutton(
    window, text=gender_Ty.get('bmw_4'), value='bmw_4', variable=gender
)
bmw_4.place(x=100, y=160)

bmw_5 = Radiobutton(
    window, text=gender_Ty.get('bmw_5'), value='bmw_5', variable=gender
)
bmw_5.place(x=240, y=160)

bmw_6 = Radiobutton(
    window, text=gender_Ty.get('bmw_6'), value='bmw_6', variable=gender
)
bmw_6.place(x=380, y=160)

dob_label = Label(window, text="Car rental day and return day: ", padx=1, pady=20)
dob_label.grid(row=45, column=3)
dob_entry = DateEntry(window)
dob_entry.grid(row=45, column=60)

# color
color = Label(window, text='Car color:', padx=20, pady=10)
color.place(x=40, y=270)

button = Button(window, text='BLUE', bg='blue', fg='white')
button.place(x=160, y=280)

bu = Button(window, text='Black', bg='black', fg='white')
bu.place(x=210, y=280)

buk = Button(window, text='Gray', bg='gray', fg='white')
buk.place(x=260, y=280)

# save
save_ = Button(window, text='SAVE', padx=20, pady=10, command=save)
save_.place(x=100, y=340)

info = Button(window, text='info', padx=20, pady=10, command=information)
info.place(x=200, y=340)

clear_ = Button(window, text='clear', padx=20, pady=10, command=clear)
clear_.place(x=300, y=340)

quit_btn = Button(window, text='EXIT', padx=20, pady=10, command=window.quit)
quit_btn.place(x=400, y=340)

if __name__ == '__main__':
    window.mainloop()
