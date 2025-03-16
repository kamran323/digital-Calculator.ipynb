import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2 if num2 != 0 else "Error! Division by zero."
        else:
            result = "Invalid operation"
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

def clear_entries():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Digital Calculator")

# Create input fields
entry1 = tk.Entry(root)
entry1.pack(pady=10)

entry2 = tk.Entry(root)
entry2.pack(pady=10)

# Create buttons for operations
button_add = tk.Button(root, text="Add", command=lambda: calculate("add"))
button_add.pack(side=tk.LEFT, padx=5)

button_subtract = tk.Button(root, text="Subtract", command=lambda: calculate("subtract"))
button_subtract.pack(side=tk.LEFT, padx=5)

button_multiply = tk.Button(root, text="Multiply", command=lambda: calculate("multiply"))
button_multiply.pack(side=tk.LEFT, padx=5)

button_divide = tk.Button(root, text="Divide", command=lambda: calculate("divide"))
button_divide.pack(side=tk.LEFT, padx=5)

# Create a clear button
button_clear = tk.Button(root, text="Clear", command=clear_entries)
button_clear.pack(side=tk.LEFT, padx=5)

# Label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=20)

# Run the application
root.mainloop()
