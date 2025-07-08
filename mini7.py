import tkinter as tk
import time

def log_temperature():
    temp = temp_entry.get().strip()
    if temp:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_text.insert(tk.END, f"{timestamp} - {temp} °C\n")
        temp_entry.delete(0, tk.END)

# Setup the main window
window = tk.Tk()
window.title("Temperature Logger")
window.geometry("400x300")

# Entry for temperature input
tk.Label(window, text="Enter Temperature (°C):", font=("Arial", 14)).pack(pady=5)
temp_entry = tk.Entry(window, font=("Arial", 14), borderwidth=3, relief="ridge")
temp_entry.pack(padx=10, pady=5, fill='x')

# Button to log temperature
tk.Button(window, text="Log Temperature", command=log_temperature, bg="blue", fg="white").pack(pady=10)

# Text widget to display the log
log_text = tk.Text(window, font=("Courier", 12), height=10, borderwidth=3, relief="sunken")
log_text.pack(padx=10, pady=5, fill='both', expand=True)

window.mainloop()
