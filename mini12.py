import tkinter as tk

def display_info():
    name = name_entry.get().strip()
    address = address_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()

    info = (
        f"Name: {name}\n"
        f"Address: {address}\n"
        f"Phone: {phone}\n"
        f"Email: {email}"
    )
    summary_label.config(text=info)

# Main window
window = tk.Tk()
window.title("Address Form")
window.geometry("350x300")

# Name Entry
tk.Label(window, text="Name:", font=("Arial", 12)).pack()
name_entry = tk.Entry(window, font=("Arial", 12), borderwidth=3, relief="ridge")
name_entry.pack(pady=5)

# Address Entry
tk.Label(window, text="Address:", font=("Arial", 12)).pack()
address_entry = tk.Entry(window, font=("Arial", 12), borderwidth=3, relief="ridge")
address_entry.pack(pady=5)

# Phone Entry
tk.Label(window, text="Phone:", font=("Arial", 12)).pack()
phone_entry = tk.Entry(window, font=("Arial", 12), borderwidth=3, relief="ridge")
phone_entry.pack(pady=5)

# Email Entry
tk.Label(window, text="Email:", font=("Arial", 12)).pack()
email_entry = tk.Entry(window, font=("Arial", 12), borderwidth=3, relief="ridge")
email_entry.pack(pady=5)

# Submit Button
tk.Button(window, text="Submit", command=display_info, bg="green", fg="white").pack(pady=10)

# Label to display submitted info
summary_label = tk.Label(window, text="", font=("Arial", 12), justify="left", fg="blue")
summary_label.pack()

window.mainloop()
