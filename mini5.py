import tkinter as tk

# Add task to the listbox
def add_task():
    task = entry.get().strip()
    if task != "":
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

# Remove selected task(s)
def remove_task():
    selected = task_list.curselection()
    for index in reversed(selected):  # Remove from last to avoid index shift
        task_list.delete(index)

# Main window
window = tk.Tk()
window.title("To-Do List App")
window.geometry("300x400")

# Entry for new task
entry = tk.Entry(window, font=("Arial", 14), borderwidth=4, relief="solid")
entry.pack(pady=10, padx=10, fill='x')

# Add button
add_button = tk.Button(window, text="Add Task", command=add_task, bg="green", fg="white")
add_button.pack(pady=5)

# Listbox to show tasks
task_list = tk.Listbox(window, font=("Arial", 12), selectmode=tk.MULTIPLE, height=15)
task_list.pack(pady=10, padx=10, fill='both', expand=True)

# Remove button
remove_button = tk.Button(window, text="Remove Selected", command=remove_task, bg="red", fg="white")
remove_button.pack(pady=5)

window.mainloop()
