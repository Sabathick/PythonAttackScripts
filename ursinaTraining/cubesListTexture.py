from ursina import *

def update():
    for entity in cubes:
        entity.rotation_y=entity.rotation_y + time.dt *100

app = Ursina()

cubes=[]
cube = Entity(model="cube", rotation=(45,45,0), color=color.rgb(255,0,0), texture="white-cube")
cube2 = Entity(model="cube", color=color.red, position=(2,0,0), texture="brick")
cube3 = Entity(model="cube", color=color.red, position=(4,0,0), texture="radial_gradient")
cube4 = Entity(model="cube", color=color.red, position=(-2,0,0), texture="sky_sunset")
cube5 = Entity(model="cube", color=color.red, position=(-4,0,0), texture="horizontal_gradient")
cubes.append(cube)
cubes.append(cube2)
cubes.append(cube3)
cubes.append(cube4)
cubes.append(cube5)
app.run()
