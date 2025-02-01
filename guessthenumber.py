import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import random
import tkinter.messagebox
root = Tk()
root.geometry("400x300")
root.title("ԅ(≖◡≖ԅ)-suling chu")

number = random.randint(1,3759824633)

def saywords():
    tkinter.messagebox.showinfo("hint?",number)

def confirm():
    myname = namebox.get()
    tkinter.messagebox.showinfo("hello",myname+" im thinking of a number between 1 and 3,759,824,633")

def checknumber():
    guess = numberbox.get()
    guess = int(guess)
    if guess == number:
        tkinter.messagebox.showinfo("yaey","ᕙ(  •̀ ᗜ •́  )ᕗ")
    elif guess < number:
        tkinter.messagebox.showinfo("▄︻デ══━一💥","number needs to be higher")
    elif guess > number:
        tkinter.messagebox.showinfo("/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿💥","number needs to be higher")

label = Label(root,text = "this is a game where you guess a number between 1 and 3,759,824,633")
label.pack()

label2 = Label(root,text = "name")
label2.place(x = 10,y = 70)
namebox = Entry(root,width = 20)
namebox.place(x = 45,y = 70)

button = Button(root,text = "ok",command = confirm)
button.place(x = 175,y = 70)

label3 = Label(root,text = "guess a number between 1 and 3759824633")
label3.place(x = 10,y = 150)
numberbox = Entry(root,width = 20)
numberbox.place(x = 240,y = 150)

button2 = Button(root,text = "guess",command = checknumber)
button2.place(x = 290,y = 200)

button2 = Button(root,text = "hint",command = saywords)
button2.place(x = 290,y = 900)

root.mainloop()