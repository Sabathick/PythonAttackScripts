import tkinter as tk
import calculator

app = tk.Tk()
app.geometry('300x400')
app.title('Calculator')
app.resizable(False,False)

sumBut = tk.Button(app, text="+", width=5, height=2)
sumBut.pack(side='left')
sumBut.pack = calculator.sum
labelSum = tk.Label(app, text =str(calculator.sum))

minBut = tk.Button(app, text="-", width=5, height=2)
minBut.pack(side='right')

mulBut = tk.Button(app, text="*", width=5, height=2)
mulBut.pack(side='left')

divBut = tk.Button(app, text="/", width=5, height=2)
divBut.pack(side='right')

app.mainloop()
