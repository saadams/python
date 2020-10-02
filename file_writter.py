
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu
from random import randint
def showCoolText():
	print("hello")
	num = randint(0, 100)
	print(num)

window = Tk()
window.geometry('500x500')
window.title("welcome to tkinter")

main_lbl = Label(window, text = "Hello world", font = ("Arial Bold",20), )
main_lbl.grid(column = 0, row = 0)

def clicked():
	res = "welcome to " + txt.get()
	lbl.configure(text = res)
	print(selected.get())

btn = Button(window, text = "Click Me", bg = "black", command = clicked, font = ("Arial",20))
btn.grid(column = 0, row = 2)

# get txt using input. get input
txt = Entry(window,width = 0)
# use the grid or pack funtion to add it to the window.
txt.grid(column = 0, row = 1)







window.mainloop()
showCoolText()