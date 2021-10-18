import PySimpleGUI as sg

sg.theme('Dark Blue 3')

layout = [[sg.Text('Calculator')],
        [sg.InputText()],
        [sg.Button('Ok'),sg.Button('Clear'),sg.Button('Exit')]]

window = sg.Window("Calculator", layout, margins=(100, 50))
event, values = window.read()