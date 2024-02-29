import tkinter as tk

# Function to update the display
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear the display
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the expression
def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

# Setting up the GUI window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

expression = ""
input_text = tk.StringVar()

# Creating the entry widget for displaying the input/output
input_entry = tk.Entry(root, textvariable=input_text, font=('arial', 20, 'bold'), bd=15, insertwidth=4, bg="powder blue", justify='right')
input_entry.grid(columnspan=4)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Add buttons to the GUI
row = 2
col = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'),
              bd=8, relief='raised',
              command=lambda item=button: button_click(item) if item != '=' else button_equal() if item == '=' else button_clear()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
