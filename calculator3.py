import tkinter as tk

def press_key(key):
    display.insert(tk.END, key)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def clear_display():
    display.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

display = tk.Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=40, pady=20, command=calculate).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(root, text=button, padx=40, pady=20, command=clear_display).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=40, pady=20, command=lambda key=button: press_key(key)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()