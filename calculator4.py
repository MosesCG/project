import tkinter as tk

calculator = "" 

def add_to_calculation(symbol):
    global calculator
    calculator += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculator)

def evaluate_calculation():
    global calculator
    try:
        result = str(eval(calculator))
        calculator = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except Exception as e:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculator
    calculator = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    if text == 'C':
        btn = tk.Button(root, text=text, command=clear_field, width=5, font=("Arial", 14))
    elif text == '=':
        btn = tk.Button(root, text=text, command=evaluate_calculation, width=5, font=("Arial", 14))
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=("Arial", 14))
    
    btn.grid(row=row, column=column)

root.mainloop()