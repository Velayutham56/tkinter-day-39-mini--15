import tkinter as tk

# Sample question and answer
question_text = "What is the capital of France?"
correct_answer = "Paris"

def check_answer():
    user_answer = answer_entry.get().strip()
    if user_answer.lower() == correct_answer.lower():
        result_label.config(text="✅ Correct!", fg="green")
    else:
        result_label.config(text="❌ Incorrect. Try again!", fg="red")

# Main window setup
root = tk.Tk()
root.title("Basic Quiz App")

# Question Label
question_label = tk.Label(root, text=question_text, font=("Arial", 14))
question_label.pack(pady=10)

# Answer Entry
answer_entry = tk.Entry(root, font=("Arial", 12))
answer_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit Answer", command=check_answer)
submit_button.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="Your result will appear here.", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
