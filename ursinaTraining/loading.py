from ursina import *
app = Ursina()

def update():
    global t,m
    m+=1
    if m%10==0:
        t+=1 
        for i in range(num):
            circles[i].color=color.rgba(255,255,255,transp[i-t%12])
num=12
circles=[]
transp = [t*255/11 for t in range(num)]

for t in range(num):
    angle =30 * t * math.pi/180
    x = math.cos(90 * math.pi/180 - angle)
    y = math.sin(90*math.pi/180 - angle)
    e = Entity(model="circle", scale=0.3, position=(x,y), color=color.rgba(255,255,255,transp[t]))
    circles.append(e)

t=0
m=0

app.run()