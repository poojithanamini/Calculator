from tkinter import *
import parser


root = Tk()
root.title("Calculator")
root.geometry("312x324")

i=0
def get_values(num):
	global i
	inputfield.insert(i, num)
	i = i+1

def get_operator(operator):
	global i
	length=len(operator)
	inputfield.insert(i, operator)
	i = i+length

def clear_all():
	inputfield.delete(0, END)

def undo():
	entered_string = inputfield.get()
	new_string = entered_string[:-1]
	clear_all()
	inputfield.insert(0, new_string)

def calculate():
	entered_string = inputfield.get()
	try:
		a = parser.expr(entered_string).compile()
		result = eval(a)
		clear_all()
		inputfield.insert(0, result)
	except:
		clear_all()
		inputfield.insert(0, "Error")

inputframe = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
inputframe.pack(side=TOP)

# display = Entry(root)
# display.grid(row=1, columnspan=6, sticky=W+E)


inputfield = Entry(inputframe, font=('arial', 18, 'bold'), width=50, bg="#eee", bd=0, justify=RIGHT)
inputfield.grid(row=0, column=0)
inputfield.pack(ipady=10)

buttonsframe = Frame(root, width=312, height=272.5, bg="grey")
buttonsframe.pack()

#first row

Button(buttonsframe, text="1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: get_values(1)).grid(row=0, column=0, padx=1, pady=1)
Button(buttonsframe, text="2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: get_values(2)).grid(row=0, column=1, padx=1, pady=1)
Button(buttonsframe, text="3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: get_values(3)).grid(row=0, column=2, padx=1, pady=1)
Button(buttonsframe, text="+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command=lambda: get_values("+")).grid(row=0, column=3, padx=1, pady=1)

#second row

Button(buttonsframe, text="4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: get_values(4)).grid(row=1, column=0, padx=1, pady=1)
Button(buttonsframe, text="5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: get_values(5)).grid(row=1, column=1, padx=1, pady=1)
Button(buttonsframe, text="6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: get_values(6)).grid(row=1, column=2, padx=1, pady=1)
Button(buttonsframe, text="-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command=lambda: get_values("-")).grid(row=1, column=3, padx=1, pady=1)

#third row

Button(buttonsframe, text="7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: get_values(7)).grid(row=2, column=0, padx=1, pady=1)
Button(buttonsframe, text="8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: get_values(8)).grid(row=2, column=1, padx=1, pady=1)
Button(buttonsframe, text="9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command=lambda: get_values(9)).grid(row=2, column=2, padx=1, pady=1)
Button(buttonsframe, text="*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command=lambda: get_values("*")).grid(row=2, column=3, padx=1, pady=1)

#fourth row

Button(buttonsframe, text="0", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command=lambda: get_values(0)).grid(row=3, column=0, padx=1, pady=1)
Button(buttonsframe, text=".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command=lambda: get_values(".")).grid(row=3, column=1, padx=1, pady=1)
Button(buttonsframe, text="AC", fg = "black", width =10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command=lambda: clear_all()).grid(row=3, column=2, padx=1, pady=1)
Button(buttonsframe, text="/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command=lambda: get_operator("/")).grid(row=3, column=3, padx=1, pady=1)

#fifth row

Button(buttonsframe, text="(", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command=lambda: get_operator("(")).grid(row=4, column=0, padx=1, pady=1)
Button(buttonsframe, text=")", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command=lambda: get_operator(")")).grid(row=4, column=1, padx=1, pady=1)
Button(buttonsframe, text="<-", fg = "black", width =10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command=lambda: undo()).grid(row=4, column=2, padx=1, pady=1)
Button(buttonsframe, text="=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command=lambda: calculate()).grid(row=4, column=3, padx=1, pady=1)


root.mainloop()
