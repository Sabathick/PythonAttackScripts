from ursina import *

class Health_bar(Entity):
    def __init__(self,x):
        self.model="quad"
        self.color=color.green
        self.z=-1
        self.origin=(-0.5,-0.5)
        self.scale_max=x
        self.scare_x=x
        self.scale=(self.scale_x,0.5)
    def update(self):
        self.scale_x -= held_keys['left arrow'] * time.dt * 5
        self.scale_x += held_keys['right arrow'] * time.dt * 5
        self.scale_x = clamp(self.scale_x, 0 ,self.scale_max)

app = Ursina()

x=100
full_bar = Entity(model="quad", origin=(-0.5,-0.5), position=(-x//2,0), scale=(x,0.5), color=color.red)
health_bar=Health_bar(x)
app.run()