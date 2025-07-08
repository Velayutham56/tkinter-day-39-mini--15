import tkinter as tk

def calculate_bmi():
    try:
        height = float(height_entry.get()) / 100 
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")


root = tk.Tk()
root.title("BMI Calculator")


tk.Label(root, text="Height (cm):").grid(row=0, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1, padx=10, pady=10)


tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)


calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_button.grid(row=2, columnspan=2, pady=10)

result_label = tk.Label(root, text="Your BMI will appear here.")
result_label.grid(row=3, columnspan=2, pady=10)

root.mainloop()
