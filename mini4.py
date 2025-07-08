import tkinter as tk

def convert():
    try:
        value = float(entry.get())
        if var.get() == "cm_to_inch":
            result = value / 2.54
            result_label.config(text=f"{value} cm = {result:.2f} inches")
        elif var.get() == "inch_to_cm":
            result = value * 2.54
            result_label.config(text=f"{value} inches = {result:.2f} cm")
        elif var.get() == "c_to_f":
            result = (value * 9/5) + 32
            result_label.config(text=f"{value} °C = {result:.2f} °F")
        elif var.get() == "f_to_c":
            result = (value - 32) * 5/9
            result_label.config(text=f"{value} °F = {result:.2f} °C")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Main window
window = tk.Tk()
window.title("Unit Converter")

# Entry for input value
entry = tk.Entry(window, font=("Arial", 16))
entry.pack(pady=10)

# Option menu for conversion type
var = tk.StringVar(value="cm_to_inch")
options = [
    ("Centimeters to Inches", "cm_to_inch"),
    ("Inches to Centimeters", "inch_to_cm"),
    ("Celsius to Fahrenheit", "c_to_f"),
    ("Fahrenheit to Celsius", "f_to_c")
]

for text, value in options:
    tk.Radiobutton(window, text=text, variable=var, value=value).pack(anchor='w')

# Convert button
tk.Button(window, text="Convert", command=convert, bg="blue", fg="white").pack(pady=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=5)

window.mainloop()
