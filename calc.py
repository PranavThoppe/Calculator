import tkinter as tk

def add(a, b):
    answer = a + b
    result_label.config(text=str(a) + " + " + str( b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    result_label.config(text=str(a) + " - " + str(b ) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a*b
    result_label.config(text=str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    if b == 0:
        result_label.config(text="Error: division by zero\n")
    else:
        answer = a / b
        result_label.config(text=str(a) + " / " + str(b) + " = " + str(answer) + "\n")

def calculate():
    operation = operation_var.get()
    a = int(first_num_entry.get())
    b = int(second_num_entry.get())

    if operation == "Addition":
        add(a, b)
    elif operation == "Subtraction":
        sub(a, b)
    elif operation == "Multiplication":
        mul(a, b)
    elif operation == "Division":
        div(a, b)

root = tk.Tk()
root.title("Calculator")

# Menu options
operation_var = tk.StringVar()
operation_var.set("Addition")
options = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_menu = tk.OptionMenu(root, operation_var, *options)
operation_menu.pack()

# Show all menu options
operation_menu["menu"].configure(bg="white", activebackground="gray", activeforeground="white", foreground="black")

# Input fields
first_num_label = tk.Label(root, text="First Number:")
first_num_label.pack()
first_num_entry = tk.Entry(root)
first_num_entry.pack()

second_num_label = tk.Label(root, text="Second Number:")
second_num_label.pack()
second_num_entry = tk.Entry(root)
second_num_entry.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
