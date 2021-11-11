from ursina import *




app = Ursina()

e1=Entity(model="quad", position=(-4,2))
e1.animate_x(4, duration=1, loop=True)

e2= Entity(model="cirlce", position=(-4,-2), color=color.green)
e2.animate_color(color.red, duration=1, loop=True)

e3=Entity(model="cube", color=color.orange)
e3.animate_scale(3, duration=2, loop=True)
e3.animate_color(color.yellow, duration=2, loop=True)

e4=Entity(model="quad", position=(4,-2), color=color.cyan, texture="brick")
e4.animate_rotation_z(45, duration=1, loop=True, delay=2)

app.run()