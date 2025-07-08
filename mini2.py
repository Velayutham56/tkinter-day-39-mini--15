import tkinter as tk
def submit_value():
    nameentry.delete(0, tk.END)
    messageentry.delete(1.0, tk.END)
window = tk.Tk()
namelabel = tk.Label(window,text="Name",font=("Arial",14,"bold"),fg="green")
namelabel.pack()

nameentry = tk.Entry(window)
nameentry.pack()

messagelabel = tk.Label(window,text="message",font=("Arial",14,"bold"),fg="green")
messagelabel.pack()

messageentry = tk.Text(window, height=20,width=20)
messageentry.pack()

button = tk.Button(window,text="submit",command=submit_value)
button.pack()


window.mainloop()