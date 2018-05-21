from tkinter import *
import os

root = Tk()
root.title('Alert!')
root.configure(background="white")
root.geometry("500x50") 
Label1=Label(root,text="No duplicates found",bg="white",font=("Arial", 12))
Label1.pack()
root.mainloop()
