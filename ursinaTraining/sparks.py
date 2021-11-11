from ursina import *

class Sparks(Entity):
    def __init__(self,x,y):
        super().__init__()
        self.parent=camera.ui
        self.model="circle"
        self.color=color.white
        self.scale=0.012
        self.x=x
        self.y=y
        self.dx=random.randint(-2,2)/1000
        self.dy=random.randint(-2,2)/1000
        self.ds=random.randint(1,3)/5000
    
    def update(self):
        self.x+=self.dx
        self.y+=self.dy
        self.scale-=self.ds
        if self.scale<=0.005:
            destroy(self)

def CreateSparks():
    num=9
    e=[None]*num
    for i in range(num):
        e[i]=Sparks(mouse.x, mouse.y)

app = Ursina()

B=Button(text="", color=color.rgb(255,255,255,0), scale=2)
B.on_click=CreateSparks

app.run()