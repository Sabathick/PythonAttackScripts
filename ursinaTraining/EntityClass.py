from ursina import *

class Player(Entity):
    def __init__(self, x, speed):
        super().__init__()
        self.model = 'cube'
        self.color = color.red
        self.scale_y=2
        self.x=x
        self.speed=speed

    def update(self):
        self.x+=held_keys['right arrow']*time.dt*self.speed
        self.x-=held_keys['left arrow']*time.dt*self.speed
        self.y+=held_keys['up arrow']*time.dt*self.speed
        self.y-=held_keys['down arrow']*time.dt*self.speed
    
    def input(self,key):
        if key =="space":
            self.color = color.random_color()
        if key == 'r':
            self.rotation_z+=time.dt*500
        if key == '0':
            Player.reset(self)
        
    def reset(self):
        self.color=color.red
        self.rotation_z=0
        self.x=x

app = Ursina()
Entity(model="quad", color=color.green, position = (0,0,1), scale=1.5, rotation = (0,0,45))
x=-2
speed=10
player=Player(x,speed)

app.run()