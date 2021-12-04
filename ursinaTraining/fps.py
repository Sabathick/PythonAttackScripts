from ursina import *
from ursina import curve
from random import uniform
from ursina.prefabs.first_person_controller import FirstPersonController

def input(key):
    if key =="left mouse down":
        Audio("assets/laser_sound.wav")
        Animation("assets/spark", parent=camera.ui, fps=5, scale=(0.1), position=(0.19,-0.03), loop=False)
        
        for wasp in wasps:
            if wasp.hovered:
                destroy(wasp)
class Wasp(Button):
    def __init__(self, x,y,z):
        super().__init__(
            parent=scene,
            model="assets/wasp.obj",
            scale=0.1,
            position=(x,y,z),
            rotation=(0,90,0),
            collider="box"
        )

class HookBlock(Button):
    def __init__(self,position):
        super().__init__(
            parent=scene,
            model="cube",
            color=color.brown,
            position=position
        )
    self.on_click = Func(player.animate_position, self.position, duration=0.5, )

app = Ursina()

Sky()
player = FirstPersonController(y=2,origin_y=-0.5)
ground=Entity(model="plane", scale=(100,1,100), color=color.lime, texture="white_cube",texture_scale=(100,100), collider='box')

wall_1=Entity(model="cube", collider="box", position=(-8,0,0), scale=(8,5,1), rotation=(0,0,0), texture="brick", texture_scale=(5,5), color=color.rgb(255,128,0))
wall_2=duplicate(wall_1, z=5)
wall3 = duplicate(wall_1,z=10)
wall_4= Entity(model="cube", collider='box', position=(-15,0,10), scale=(1,5,20), rotation=(0,0,0), texture="brick", texture_scale=(5,5), color=color.rgb(255,128,0))
gun = Entity(model="assets/gun.obj", parent=camera.ui, scale=0.08, color=color.gold, position=(0.3,-0,2), rotation=(-5,-10,-10))

num=6
wasps = [None]*num
for i in range(num):
    wx=uniform(-12,-7)
    wy=uniform(0.1,1.8)
    wz=uniform(0.8,3.8)
    wasps[i]=Wasp(wx,wy,wz)
    wasps[i].animate_X(wx+0.5, duration=0.2, loop=True)
app.run()