from ursina import *
from random import randint

def update():
    red=randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    cube.color=color.rgb(red,green,blue)
    cube.x=cube.x+time.dt
    cube.rotation_z=cube.rotation_z + time.dt * 100




app = Ursina()
cube = Entity(model="cube", rotation=(45,45,0), color=color.rgb(255,0,0))
txt = Text(text="This is a red cube", scale=2)

app.run()

