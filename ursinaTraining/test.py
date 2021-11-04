from ursina import *

def update():
    cube.x=cube.x+time.dt





app = Ursina()
cube = Entity(model="cube", rotation=(45,45,0), color=color.rgb(255,0,0))
txt = Text(text="This is a red cube", scale=2)

app.run()

