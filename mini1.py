import tkinter as tk
from tkinter import messagebox

window = tk.Tk()


name = "1234"
passwo = "1234"
def check_validate():
    uservalue =nameentry.get()
    userpass = passwordentry.get()
    if name == uservalue and passwo == userpass:
        messagebox.showinfo("your pass word correct")
        nameentry.delete(0, tk.END)
        passwordentry.delete(0, tk.END)
      
    else:
        messagebox.showwarning("invalid pass word or user name")
        nameentry.delete(0, tk.END)
        passwordentry.delete(0, tk.END)
namelabel = tk.Label(window, text="name",font=("Arial",16,"bold"),fg="blue")
namelabel.pack()

nameentry = tk.Entry(window,borderwidth=5,relief="solid")
nameentry.pack()

passwordlabel = tk.Label(window,text="Password",font=("Arial",16,"bold"),fg="blue")
passwordlabel.pack()

passwordentry = tk.Entry(window,show="*")
passwordentry.pack()

button = tk.Button(window,bg="red",text="submit",command=check_validate)
button.pack()
window.mainloop()

