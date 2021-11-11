from ursina import *

class Bubbles(Entity):
    def __init__(self,x,y, mycolor):
        super().__init__()
        self.parent=camera.ui
        self.model="circle"
        self.color=mycolor
        self.scale=0.012
        self.x0=x
        self.y0=y
        self.x=x
        self.y=y
    def update(self):
        self.x+=random.randint(-2,2)/1000
        self.y+=random.randint(0,2)/500
        self.scale-=0.00015
        if self.scale <= 0.005:
            self.x=self.x0
            self.y=self.y0

def CreateBubbles():
    num=10
    e=[None]*num
    mycolor=color.random_color()
    for i in range(num):
        e[i]=Bubbles(mouse.x, mouse.y, mycolor)

app=Ursina()

B=Button(text='', color=color.rgb(255,255,255,0),scale=2)
B.on_click=CreateBubbles

app.run()