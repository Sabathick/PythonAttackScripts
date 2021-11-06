from ursina import *
from random import randint

def update():
    #held key to move
    if held_keys['r']:
        cube.rotation_y = cube.rotation_y + time.dt * 100






app=Ursina()
cube=Entity(model="cube", color = color.red, texture= "white_cube", scale=2)
app.run()
