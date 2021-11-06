from ursina import *
from random import randint

def update():
    global speed
    cube.rotation_y = cube.rotation_y + time.dt * speed

def input(key):
    global speed
    if held_keys['r']:
        speed=100
    if held_keys['s']:
        speed=0


#def input(key):
#move one time for each time the key is pressed
#   if key == "r":
#       cube.rotation_y=cube.rotation_y+time.dt * 100

#def update():
#held key to move
#   if held_keys['r']:
#       cube.rotation_y = cube.rotation_y + time.dt * 100

app=Ursina()
speed= 0 
cube=Entity(model="cube", color = color.red, texture= "white_cube", scale=2)
app.run()
