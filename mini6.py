import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  


window = tk.Tk()
window.title("Digital Clock")
window.geometry("250x100")


clock_label = tk.Label(window, font=("Arial", 40), fg="blue")
clock_label.pack(pady=20)

update_clock()  
window.mainloop()
