import tkinter as tk

def get_input(event=None):
    user_input = entry.get()  # Get the text from the entry widget
    print(f"User entered: {user_input}")  # Print it to the console
    entry.delete(0, tk.END)  # Clear the entry field

# Create the main window
root = tk.Tk()
root.title("Input Example with Enter Key")

# Create a label
label = tk.Label(root, text="Escribe cualquier bobada y presiona ENTER:")
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Bind the Enter key to the get_input function
root.bind('<Return>', get_input)

# Create a button to submit input
submit_button = tk.Button(root, text="presiona viejito... dale sin pena", command=get_input)
submit_button.pack(pady=10)

# Run the application
root.mainloop()
