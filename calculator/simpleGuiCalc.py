import PySimpleGUI as sg

def addText(btnStr):
    sg.InputText() 

def CBtn(button_text):
    return sg.Button(button_text, button_color=('white','blue'), size=(5,1), font=("Helvetica", 20))
sg.theme('Dark Blue 3')

layout = [[sg.Text('Calculator')],
        [sg.InputText()],
        [CBtn(t) for t in ('1','2','3','log','ln','-')],
        [CBtn(t) for t in ('4','5','6','sin','cos','+')],
        [CBtn(t) for t in ('7','8','9','tg','e','*')],
        [CBtn(t) for t in (',','0','!','^2','\u221A','/')],
        [CBtn(t) for t in ('Clear','=','Exit')]]

window = sg.Window("Calculator", layout, margins=(100, 50))

while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == '1': addText('1')
    elif event == '2': addText('2')
    elif event == '3': addText('3')
    elif event == '4': addText('4')
    elif event == '5': addText('5')
    elif event == '6': addText('6')
    elif event == '7': addText('7')
    elif event == '8': addText('8')
    elif event == '9': addText('9')
    elif event == '0': addText('0')
    elif event == '+': addText('+')
    elif event == '-': addText('-')
    elif event == '/': addText('/')
    elif event == '*': addText('*')

window.Close()