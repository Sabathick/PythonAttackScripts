import tkinter as tk
from math import *
import re


def filterMath(equation):
    equation = re.sub('[a-zA-z,.:()" "]', '', equation)
    print(str(equation))
    return equation

def evaluate(event):
    equation.configure(text = "Result:" + str(eval(entry.get())))
    

app = tk.Tk()
app.geometry('300x400')
app.title('Calculator')
app.resizable(False,False)

tk.Label(app, text="Your expression:").pack()
entry = tk.Entry(app)
entry.bind("<Return>", evaluate(filterMath))
entry.pack()
equation = tk.Label(app)
equation.pack()

quit = tk.Button(app, text="QUIT", command=app.destroy)
quit.pack(side="bottom")

app.mainloop()