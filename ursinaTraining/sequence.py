from ursina import *

def input(key):
    actions={"1": s1.start, "2": s1.pause, "3":s2.start, "4":s2.pause, "5":s3.start, "6":s3.pause}
    if key in actions:
        actions[key]()


app = Ursina()

e1 = Entity(model="circle")
e2 = Entity(model="quad", color=color.orange, position=(3,0,0))
e3 = Entity(model="quad", color=color.cyan, position=(-3,0,0), scale=(1,2,1))

s1=Sequence(1, Func(e1.blink, duration=1), loop=True)
s2=Sequence(1, Func(e2.blink, duration=2), Func(e2.shake, duration=2), loop=True)
s3=Sequence(2, Func(e3.fade_out, duration=2), 2, Func(e3.fade_in, duration = 2), loop=True)

s1.start()
s2.start()
s3.start()
app.run()
