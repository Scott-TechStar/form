from cProfile import label
from tkinter import *
from tkinter.tix import CheckList
from turtle import color
root = Tk()
root.geometry("500x500")
root.configure(bg='#856ff8')

def regvalues():
    print("Registered")

Label(root, text="Python Registration Form", font="ar 15 bold italic").grid(row=0, column=3)

name = Label(root, text="Full Name:")
email = Label(root, text="Email Address:")
phone = Label(root, text="Phone No.:")
gender = Label(root, text="Gender:")
emergency = Label(root, text="Emergency: ")
pmode = Label(root, text="Payment Mode:")

name.grid(row=1, column=2)
email.grid(row=3, column=2)
phone.grid(row=5, column=2)
gender.grid(row=7, column=2)
emergency.grid(row=9, column=2)
pmode.grid(row=11, column=2)


namevalue = StringVar
emailvalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
pmodevalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable=namevalue)
emailentry = Entry(root, textvariable=emailvalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
pmodeentry = Entry(root, textvariable=pmodevalue)

nameentry.grid(row=1, column=3)
emailentry.grid(row=3, column=3)
phoneentry.grid(row=5, column=3)
genderentry.grid(row=7, column=3)
emergencyentry.grid(row=9, column=3)
pmodeentry.grid(row=11, column=3)

checkbtn = Checkbutton(text="Remember me?", variable=checkvalue)

checkbtn.grid(row=12, column=3)

Button(text="Register", command=regvalues).grid(row=14, column=3)



root.mainloop()