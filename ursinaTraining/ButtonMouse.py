from ursina import *
from random import randint

def PrintText():
    print_on_screen("Hello", position=(randint(-3,3)*0.1, randint(-3,3)*0.1))

def Colors():
    B.color = color.random_color()

app=Ursina()

B=Button(text="A button", color=color.azure, text_color=color.orange, scale=0.20, icon="sword", text_origin=(0.5,0))
B.on_click=Colors, PrintText
B.tooltip= Tooltip("Click me")
mouse.visible=False
app.run()