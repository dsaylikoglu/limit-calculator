from sympy import *
from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Limit Calculator")
root.iconbitmap("math.png")
root.geometry("500x420")


# define font
myFont = font.Font(family='Helvetica', size=18, weight='bold')


def instruction():
	instr = Toplevel()
	instr.title("Instructions")
	instr.iconbitmap("math.png")
	instr.geometry("400x180")

	instr1_label = Label(instr, text="For multiplication use, *").pack()
	instr2_label = Label(instr, text="For division use, /").pack()
	instr3_label = Label(instr, text="For addition use, +").pack()
	instr4_label = Label(instr, text="For substraction use, -").pack()
	instr5_label = Label(instr, text="For power, use **").pack()
	instr6_label = Label(instr, text="For trigonometric funcs and logs, use them normally").pack()
	instr7_label = Label(instr, text="For infinity, use oo (double o), for negative infinity use -oo").pack()
	instr8_label = Label(instr, text="For decimal notation, use '.'").pack()


# Instructions button
instr_btn = Button(root, text="Instructions", command=instruction, fg="blue")
instr_btn.grid(row=0, column=0, pady=(20, 10))

# Alert and function entry
lbl = Label(root, text="To calculate the limit, enter your function correctly!", fg="red")
lbl.grid(row=1, column=0, pady=10)
e = Entry(root, width=50)
e.grid(row=2, column=0, padx=100, pady=(0, 10))

# Variable entry
lbl1 = Label(root, text="Variable:", fg="red")
lbl1.grid(row=3,column=0, pady=5)
e1 = Entry(root, width=20)
e1.grid(row=4, column=0, padx=8, pady=(0, 10))

# Approached number entry
lbl2 = Label(root, text="The approaching number:", fg="red")
lbl2.grid(row=5,column=0, pady=5)
e2 = Entry(root, width=20)
e2.grid(row=6, column=0, padx=5, pady=(0, 15))

# Two sided limit function
def lim():
	func = e.get()
	var = e1.get()
	if e2.get() == "oo":
		appr_num = oo
	else:
		appr_num = float(e2.get())

	var = symbols(var)
	if appr_num == oo:
		ans1 = limit(func, var, appr_num)
		ans2 = limit(func, var, appr_num)
	ans1 = limit(func, var, appr_num, dir="-")
	ans2 = limit(func, var, appr_num, dir="+")

	for slave in root.grid_slaves(row=10, column=0):
		slave.grid_forget()

	if ans1==ans2:
		ans_lbl = Label(root, text=str(ans1), relief=GROOVE, borderwidth=4)
		if ans1 == oo:
			ans_lbl = Label(root, text="∞", relief=GROOVE, borderwidth=4)
		ans_lbl['font'] = myFont
		ans_lbl.grid(row=10, column=0, pady=10)
	else:
		ans_lbl = Label(root, text="The limit doesn't exist.", relief=GROOVE, borderwidth=4)
		ans_lbl['font'] = myFont
		anslbl.grid(row=10, column=0, pady=10)

# Limit from the right
def lim_from_right():
	func = e.get()
	var = e1.get()
	if e2.get() == "oo":
		appr_num = oo
	appr_num = float(e2.get())

	var = symbols(var)
	ans = limit(func, var, appr_num, dir="+")

	for slave in root.grid_slaves(row=10, column=0):
		slave.grid_forget()

	ans_lbl = Label(root, text=str(ans), relief=GROOVE, borderwidth=4)
	ans_lbl.grid(row=10, column=0, pady=5)

# Limit from the left
def lim_from_left():
	func = e.get()
	var = e1.get()
	if e2.get() == "oo":
		appr_num = oo
	appr_num = float(e2.get())

	var = symbols(var)
	ans = limit(func, var, appr_num, dir="-")

	for slave in root.grid_slaves(row=10, column=0):
		slave.grid_forget()

	ans_lbl = Label(root, text=str(ans), relief=GROOVE, borderwidth=4)
	ans_lbl.grid(row=10, column=0, pady=5)

# Calculate limit button
lim_calc = Button(root, text="Calculate the Limit", command=lim, fg="blue")
lim_calc.grid(row=7, column=0, pady=5)

# Calculate limit from right button
lim_calc = Button(root, text="Calculate the Limit from +", command=lim_from_right, fg="blue")
lim_calc.grid(row=8, column=0, pady=5)

# Calculate limit from left button
lim_calc = Button(root, text="Calculate the Limit from -", command=lim_from_left, fg="blue")
lim_calc.grid(row=9, column=0, pady=5)

root.mainloop()