import random, string
from tkinter import *

def password_10():
    list_1 = []
    list_2 = ("<", ">", ".", "!", "&", "%", ",", "-", "*", "+", "/")
    for i in range(2):
        list_1.append(random.choice(string.ascii_uppercase))
        list_1.append(random.choice(string.digits))
        list_1.append(random.choice(list_2))
        for a in range(2):
            list_1.append(random.choice(string.ascii_lowercase))
    random.shuffle(list_1)
    a =" ".join(list_1)
    return a

password = Tk()

canvas = Canvas(password, height=500, width=500)
canvas.pack()

frame = Frame(password, bg="dark red")
frame.place(relx=0.1, rely=0.1, relwidth=0.7, relheight=0.5)

password_lbl = Label(frame, text="PASSWORD", bg="white", font="ariel 20 bold")
password_lbl.pack(pady=40, side=TOP)

password_lbl2 = Label(frame, text=password_10(), bg="white", font="ariel 20")
password_lbl2.pack(padx=360, pady=1, side=TOP)

password_button = Button(frame, text=" New Password : ", command=password_10())
password_button.pack(padx=10, anchor=W)

password.mainloop()