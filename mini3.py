import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get().replace('×', '*').replace('÷', '/')
        result = eval(expr)
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error")

# Create main window
window = tk.Tk()
window.title("Basic Calculator")
window.geometry("300x400")

# Entry widget for input
entry = tk.Entry(window, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.pack(padx=10, pady=10, fill='x')

# Label to display result
result_label = tk.Label(window, text="Result:", font=("Arial", 14))
result_label.pack(pady=5)

# Frame for buttons
btn_frame = tk.Frame(window)
btn_frame.pack()

# Define buttons
buttons = [
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons in grid
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        if char == '=':
            btn = tk.Button(btn_frame, text=char, width=6, height=2, command=calculate)
        else:
            btn = tk.Button(btn_frame, text=char, width=6, height=2, command=lambda ch=char: press(ch))
        btn.grid(row=r, column=c, padx=3, pady=3)

# Clear button
clear_btn = tk.Button(window, text="Clear", width=10, command=clear, bg="red", fg="white")
clear_btn.pack(pady=10)

window.mainloop()
