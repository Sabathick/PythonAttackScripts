from ursina import *
from random import randint

def update():
    global speed,speed2,m,x

    m = m + 1
    num_frame=200
    n = m%num_frame

    if n<num_frame//2:
        cube.x=cube.x+time.dt
    else:
        cube.x=cube.x - time.dt

    red=randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    cube.color=color.rgb(red,green,blue)
    cube.x=cube.x+time.dt*speed

    if abs(cube.x)>3:
        speed=speed * -1
    cube.rotation_z=cube.rotation_z + time.dt * 100

    cube2.y = cube2.y + time.dt *speed2
    if abs(cube2.y) > 3:
        speed2=speed2 * -1

    x=x+time.dt*speed
    if abs(x)>3:
        speed=speed * -1

    camera.position = (x,0,-20)


app = Ursina()
speed=1
speed2=1
m = 0
x = 0
cube = Entity(model="cube", rotation=(45,45,0), color=color.rgb(255,0,0))
txt = Text(text="This is a red cube", scale=2)
cube2=Entity(model="cube", color=color.white)

app.run()

