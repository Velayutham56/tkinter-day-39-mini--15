import tkinter as tk

def show_summary():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    color = color_entry.get().strip()

    summary = f"Hello {name}!\nYou are {age} years old and love {color}."
    summary_label.config(text=summary)

# Main window setup
window = tk.Tk()
window.title("Survey App")
window.geometry("300x350")

# Name field
tk.Label(window, text="Name:", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(window, font=("Arial", 12), borderwidth=3, relief="ridge")
name_entry.pack(pady=5)

# Age field
tk.Label(window, text="Age:", font=("Arial", 12)).pack(pady=5)
age_entry = tk.Entry(window, font=("Arial", 12), borderwidth=3, relief="ridge")
age_entry.pack(pady=5)

# Favorite color field
tk.Label(window, text="Favorite Color:", font=("Arial", 12)).pack(pady=5)
color_entry = tk.Entry(window, font=("Arial", 12), borderwidth=3, relief="ridge")
color_entry.pack(pady=5)

# Submit button
tk.Button(window, text="Submit", command=show_summary, bg="green", fg="white").pack(pady=10)

# Summary label
summary_label = tk.Label(window, text="", font=("Arial", 12), fg="blue", justify="left")
summary_label.pack(pady=10)

window.mainloop()
