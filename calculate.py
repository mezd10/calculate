import math
from tkinter import *
from tkinter import messagebox

def calculateF(key) :
    if key == "=":

        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("ERROR!", "Check the correctness of data")
            calc_entry.delete(0, END)

    elif key == "c":
        calc_entry.delete(0, END)

    elif key == "+/-":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

    elif key == "pi":
        calc_entry.insert(END, math.pi)

    elif key == 'xⁿ':
        calc_entry.insert(END, "**")

    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


buttonList = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "+/-", "pi",
    "0", ".", "c", "=", "xⁿ"
]
r = 1
c = 0

root = Tk()
root.configure(bg='black')
root.title("Калькулятор")

for i in buttonList:

    cmd = lambda x=i: calculateF(x)
    Button(root, text=i, width=7, height=1, command=cmd, bg='grey', fg='white', activebackground='orange').grid(row=r, column=c)

    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width=50, bg='grey', fg='black')
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()

