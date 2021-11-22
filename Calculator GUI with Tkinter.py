# Calculator GUI with Tkinter

import tkinter as tk

num = ''
A = ''
result = ''
operator = ''

def b0():
    global num
    num = num + "0"
    output.set(num)

def b1():
    global num
    num = num + "1"
    output.set(num)

def b2():
    global num
    num = num + "2"
    output.set(num)

def b3():
    global num
    num = num + "3"
    output.set(num)


def b4():
    global num
    num = num + "4"
    output.set(num)


def b5():
    global num
    num = num + "5"
    output.set(num)


def b6():
    global num
    num = num + "6"
    output.set(num)


def b7():
    global num
    num = num + "7"
    output.set(num)


def b8():
    global num
    num = num + "8"
    output.set(num)

def b9():
    global num
    num = num + "9"
    output.set(num)

def bdecimal():
    global num
    num = num + "."
    output.set(num)

def bplus():
    global num
    global operator
    global A
    A = int(num)  # used to convert num to integer
    operator = "+"  # declare operator
    num = num + "+"
    output.set(num)

def bminus():
    global num
    global operator
    global A
    A = int(num)  # used to convert num to integer
    num = num + "-"
    operator = "-"  # declare operator
    output.set(num)

def bmult():
    global num
    global operator
    global A
    A = int(num)  # used to convert num to integer
    num = num + "*"
    operator = "*"  # declare operator
    output.set(num)

def bdiv():
    global num
    global operator
    global A
    A = int(num)  # used to convert num to integer
    num = num + "/"
    operator = "/"  # declare operator
    output.set(num)

def bclear():
    global num
    global operator
    global A
    num = ""
    operator = ""
    A = int(0)
    output.set(num)

def brslt():
    global num
    global operator
    global A
    num2 = num
    if operator == "+":
        x =int(num2.split("+")[1])
        sum = A + x
        output.set(sum)
        num=str(sum)
    elif operator == "-":
        x = int(num2.split("-")[1])
        sum = A - x
        output.set(sum)
        num = str(sum)

    elif operator == "*":
        x = int(num2.split("*")[1])
        sum = A * x
        output.set(sum)
        num = str(sum)

    elif operator == "/":
        try:
            x = int(num2.split("/")[1])
            sum = A / x
            output.set(sum)
            num = str(sum)
        except ZeroDivisionError:
            return print("Cannot divie by Zero")


###### Tkinter ######

root = tk.Tk()
root.configure(bg="#000000")
root.title("Calculator")
root.geometry("+500+300")

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)

frame = tk.Frame(root, pady=5, padx=10,
                 borderwidth=2, relief=tk.RAISED,
                 bg="#000000",)
frame.rowconfigure([0,1,2,3,4], minsize=80)
frame.columnconfigure([0,1,2,3], minsize=60)
frame.pack(fill="both", expand=True)

output = tk.StringVar()  # screen readout
lbl_read = tk.Label(frame, anchor='center', relief=tk.SUNKEN,
                    border=10, font=("verdana", 23),
                      bg="#5DADE2",
                      textvariable=output  # print status
                      )
lbl_read.grid(row=0, column=0, columnspan=4, sticky="nsew")

# buttons
btn0 = tk.Button(frame, text="0",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=b0,
                 )
btn0.grid(row=5, column=0, columnspan=2, sticky="nsew")

btn1 = tk.Button(frame, text="1",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=b1,
                 )
btn1.grid(row=4, column=0, sticky="nsew")

btn2 = tk.Button(frame, text="2",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=b2,
                 )
btn2.grid(row=4, column=1, sticky="nsew")

btn3 = tk.Button(frame, text="3",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=b3,
                 )
btn3.grid(row=4, column=2, sticky="nsew")

btn4 = tk.Button(frame, text="4",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=b4,
                 )
btn4.grid(row=3, column=0, sticky="nsew")

btn5 = tk.Button(frame, text="5",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=b5,
                 )
btn5.grid(row=3, column=1, sticky="nsew")

btn6 = tk.Button(frame, text="6",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=b6,
                 )
btn6.grid(row=3, column=2, sticky="nsew")

btn7 = tk.Button(frame, text="7",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=b7,
                 )
btn7.grid(row=2, column=0, sticky="nsew")

btn8 = tk.Button(frame, text="8",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=b8,
                 )
btn8.grid(row=2, column=1, sticky="nsew")

btn9 = tk.Button(frame, text="9",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=b9,
                 )
btn9.grid(row=2, column=2, sticky="nsew")

btndiv = tk.Button(frame, text="/",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=bdiv,
                 )
btndiv.grid(row=1, column=0, sticky="nsew")

btnmult = tk.Button(frame, text="*",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=bmult,
                 )
btnmult.grid(row=1, column=1, sticky="nsew")

btnminus = tk.Button(frame, text="-",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=bminus,
                 )
btnminus.grid(row=1, column=2, sticky="nsew")

btnplus = tk.Button(frame, text="+",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=bplus,
                 )
btnplus.grid(row=1, column=3, sticky="nsew")

btnclear = tk.Button(frame, text="C",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=bclear,
                 )
btnclear.grid(row=2, column=3, sticky="nsew")

btndecimal = tk.Button(frame, text=".",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=bdecimal,
                 )
btndecimal.grid(row=5, column=2, sticky="nsew")

btnrslt = tk.Button(frame, text="=",
                 font=("verdana", 15),
                 padx=1, pady=1, anchor="center",
                 activebackground="#7B68EE",
                 bg="#A569BD", relief=tk.GROOVE, borderwidth=7,
                 command=brslt,
                 )
btnrslt.grid(row=3, rowspan= 3, column=3, sticky="nsew")


root.mainloop()