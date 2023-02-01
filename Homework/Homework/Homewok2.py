from hotelinfo import Hotel
import tkinter as tk
from tkinter import messagebox, END, Label, Entry, StringVar, Radiobutton


window = tk.Tk()
window.title('Hotel Registra')
window.geometry('750x700')

hotel_info = []
def add():
    hotel_inf = Hotel(
        name.get(),
        full_name.get(),
        price.get(),
    )
    hotel_info.append(hotel_inf.get_attr(as_dict=True))
    messagebox.showinfo("HOTEL information has been added")



def age():
    today = date.today()
    print(today)
    year = int(inputFiled.get())
    if year <= 0 or year >= 2023:
        label['text'] = 'Xato'
    else:
        jj = today.year - year

        label['text'] = 'You ' + str(jj) + ' years old'


name_ = Label(window, text='Your name:')
name_.place(x=165, y=10)
name = Entry(window, width=30, borderwidth=3)
name.place(x=230, y=10)


full_ = Label(window, text='Your full_name:')
full_.place(x=133, y=35)
full_name = Entry(window, width=30, borderwidth=3)
full_name.place(x=230, y=35)


gender = StringVar()
gender_Ty = {'room_1': "Standart", 'room_2': 'Luxy', 'room_3': 'Biznes'}
gender_ = Label(window, text='Room types:', padx=20, pady=95)
gender_.grid(row=30, column=2)
room_1 = Radiobutton(
    window, text=gender_Ty.get('room_1'), value='room_1', variable=gender
)
room_1.place(x=110, y=125)

room_2 = Radiobutton(
    window, text=gender_Ty.get('room_2'), value='room_2', variable=gender
)
room_2.place(x=200, y=125)

room_3 = Radiobutton(
    window, text=gender_Ty.get('room_3'), value='room_3', variable=gender
)
room_3.place(x=280, y=125)



if __name__ == '__main__':
    window.mainloop()

