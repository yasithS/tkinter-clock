from tkinter import *
from time import *

def update():
    time_string = strftime('%I:%M:%S %p')
    time_label.config(text=time_string)

    day_string = strftime('%A')
    day_label.config(text=day_string)

    date_string = strftime('%B %d, %Y')
    date_label.config(text=date_string)

    time_label.after(1000, update)

window = Tk()

window.title("Clock")

welcome_label = Label(window, text="Hello Yasith,", font=('Times New Roman', 30), fg="black", bg="#8ac75b")
welcome_label.pack(fill=X)

time_label = Label(window, font=('Arial', 50), fg='black', bg='#f3cf60')
time_label.pack(fill=X)

day_label = Label(window, font=('Times New Roman', 30), fg='black', bg='#f4e6dc')
day_label.pack(fill=X)

date_label = Label(window, font=('Ariel', 40), fg='black', bg='#db3f30')
date_label.pack(fill=X)

update()

window.mainloop()



