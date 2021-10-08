from ursina import *

def update():
    test_square.x -= 1

app = Ursina()

test_square = Entity(model ='quad', color = color.red, scale=(1,4))

app.run()
