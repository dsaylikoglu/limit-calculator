from sympy import *
from tkinter import *

root = Tk()
root.title("Limit Calculator")
root.iconbitmap("C:/Users/lenovo/Desktop/Matematik/hesap için kodlar/exe/lim.ico")
root.geometry("500x325")

def instruction():
	instr = Toplevel()
	instr.title("Instructions")
	instr.iconbitmap("C:/Users/lenovo/Desktop/Matematik/hesap için kodlar/exe/lim.ico")
	instr.geometry("400x160")

	instr1_label = Label(instr, text="For multiplication use, *").pack()
	instr2_label = Label(instr, text="For division use, /").pack()
	instr3_label = Label(instr, text="For addition use, +").pack()
	instr4_label = Label(instr, text="For substraction use, -").pack()
	instr5_label = Label(instr, text="For power, use **").pack()
	instr8_label = Label(instr, text="For trigonometric funcs and logs, use them normally").pack()
	instr7_label = Label(instr, text="For infinity, use oo (double o), for negative infinity use -oo").pack()

instr_btn = Button(root, text="Instructions", command=instruction, fg="blue")
instr_btn.grid(row=0, column=0, pady=5)

lbl = Label(root, text="To calculate the limit, enter your function correctly!", fg="red")
lbl.grid(row=1, column=0, pady=10)
e = Entry(root, width=50)
e.grid(row=2, column=0, padx=100)

lbl1 = Label(root, text="Variable:", fg="red")
lbl1.grid(row=3,column=0, pady=5)
e1 = Entry(root, width=20)
e1.grid(row=4, column=0,padx=5)

lbl2 = Label(root, text="The approaching number:", fg="red")
lbl2.grid(row=5,column=0, pady=5)
e2 = Entry(root, width=20)
e2.grid(row=6,column=0,padx=5)

def lim():
	func = e.get()
	var = e1.get()
	app_num = int(e2.get())

	var = symbols(var)
	ans1 = limit(func, var, app_num, dir="-")
	ans2 = limit(func, var, app_num, dir="+")
	if ans1==ans2:
		ans_lbl = Label(root, text=str(ans1))
		ans_lbl.grid(row=10, column=0, pady=5)

def lim_from_r():
	func = e.get()
	var = e1.get()
	app_num = int(e2.get())

	var = symbols(var)
	ans = limit(func, var, app_num, dir="+")
	ans_lbl = Label(root, text=str(ans))
	ans_lbl.grid(row=10, column=0, pady=5)

def lim_from_l():
	func = e.get()
	var = e1.get()
	app_num = int(e2.get())

	var = symbols(var)
	ans = limit(func, var, app_num, dir="-")
	ans_lbl = Label(root, text=str(ans))
	ans_lbl.grid(row=10, column=0, pady=5)

lim_calc = Button(root, text="Calculate the Limit", command=lim, fg="blue")
lim_calc.grid(row=7, column=0, pady=5)

lim_calc = Button(root, text="Calculate the Limit from +", command=lim_from_r, fg="blue")
lim_calc.grid(row=8, column=0, pady=5)

lim_calc = Button(root, text="Calculate the Limit from -", command=lim_from_l, fg="blue")
lim_calc.grid(row=9, column=0, pady=5)

root.mainloop()