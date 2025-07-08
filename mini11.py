import tkinter as tk

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    if name and phone:
        contact_text.insert(tk.END, f"{name}: {phone}\n")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("Contact Book")
window.geometry("400x300")

# Name input
tk.Label(window, text="Name:", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(window, font=("Arial", 12), borderwidth=3, relief="ridge")
name_entry.pack(fill='x', padx=10)

# Phone number input
tk.Label(window, text="Phone Number:", font=("Arial", 12)).pack(pady=5)
phone_entry = tk.Entry(window, font=("Arial", 12), borderwidth=3, relief="ridge")
phone_entry.pack(fill='x', padx=10)

# Add button
tk.Button(window, text="Add Contact", command=add_contact, bg="green", fg="white").pack(pady=10)

# Text widget to show contacts
contact_text = tk.Text(window, font=("Courier", 12), height=10, borderwidth=3, relief="sunken")
contact_text.pack(fill='both', padx=10, pady=5, expand=True)

window.mainloop()
