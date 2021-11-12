from ursina import *

def update():
    e.rotation_y= e.rotation_y + time.dt * 100

app = Ursina()

Entity(model="quad", scale=(20,10), texture="assets/blueSky.png")
Entity(model="quad", scale=(20,10), texture="assets/grassLongPlatform.png", z=-0.01)

e=Entity(model="assets/trees/trees9.obj", scale=2, y=-1,z=-1, texture="assets/trees/Bark___0.jpg")

app.run()