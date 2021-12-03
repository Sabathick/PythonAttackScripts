from ursina import *
from random import uniform
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

Sky()
player = FirstPersonController(y=2,origin_y=-0.5)
ground=Entity(model="plane", scale=(100,1,100), color=color.lime, texture="white_cube",texture_scale=(100,100), collider='box')

wall_1=Entity(model="cube", collider="box", position=(-8,0,0), scale=(8,5,1), rotation=(0,0,0), texture="brick", texture_scale=(5,5), color=color.rgb(255,128,0))
wall_2=duplicate(wall_1, z=5)
wall3 = duplicate(wall_1,z=10)
wall_4= Entity(model="cube", collider='box', position=(-15,0,10), scale=(1,5,20), rotation=(0,0,0), texture="brick", texture_scale=(5,5), color=color.rgb(255,128,0))


app.run()