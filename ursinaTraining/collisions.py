from ursina import *
from random import randint

def update():
    global dx
    ball.x=ball.x + dx
    hit_info = ball.intersects()
    if hit_info.hit:
        dx=-dx


app=Ursina()
ball=Entity(model="sphere", scale=0.5, position=(0,0,0), collider = "box")
box_1 = Entity(model="cube", color=color.cyan, texture = "white_cube", scale=(2,4,2), position = (4,0,0), collider="box")
box_2 = duplicate(box_1, x=-4)
dx = 0.05
app.run()