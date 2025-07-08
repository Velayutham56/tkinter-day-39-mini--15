import tkinter as tk

def load_file():
    path = entry.get().strip()
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)
    except Exception as e:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, f"Error: {e}")

# Window setup
window = tk.Tk()
window.title("Text File Viewer")
window.geometry("600x400")

# File path entry
tk.Label(window, text="Enter file path:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(window, font=("Arial", 12), borderwidth=3, relief="ridge")
entry.pack(fill='x', padx=10, pady=5)

# Load button
tk.Button(window, text="Load File", command=load_file, bg="blue", fg="white").pack(pady=5)

# Text widget to display file content
text_area = tk.Text(window, font=("Courier", 12), wrap="word", borderwidth=3, relief="sunken")
text_area.pack(fill='both', expand=True, padx=10, pady=5)

window.mainloop()
