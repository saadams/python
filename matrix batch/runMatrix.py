import subprocess
import tkinter as tk

root= tk.Tk() 
root.title("Matrix Loader")
#root.iconphoto(self, default = False)
canvas1 = tk.Canvas(root, width = 350, height = 250) 
canvas1.pack()

def start_batch(): 
       subprocess.call([r'matrix.bat'])
           
button1 = tk.Button (root, text='Run The Matrix ',command=start_batch,bg='red',fg='white')
canvas1.create_window(170, 130, window=button1)

root.mainloop()