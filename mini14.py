import tkinter as tk

def count_words():
    text = text_widget.get("1.0", tk.END)
    words = text.split()
    word_count = len(words)
    result_label.config(text=f"Word Count: {word_count}")

# Create main window
root = tk.Tk()
root.title("Word Counter")

# Text widget for input
text_widget = tk.Text(root, wrap="word", width=50, height=10)
text_widget.pack(padx=10, pady=10)

# Button to count words
count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack(pady=5)

# Label to display word count
result_label = tk.Label(root, text="Word count will appear here.")
result_label.pack(pady=5)

root.mainloop()
