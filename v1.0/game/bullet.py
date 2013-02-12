import pyglet
from . import resources
import math

class Bullet(pyglet.sprite.Sprite):
    def __init__(self, tank, *args,**kwargs):
        super().__init__(img = resources.bullet_image, batch = tank.bulletsBatch, *args,**kwargs)
        self.tank = tank
        self.angle=-self.tank.hose.rotation + 90
        
        
        self.x = self.tank.x + self.tank.width/2 + math.cos(math.radians(self.angle))*self.tank.hose.height
        self.y = self.tank.y + self.tank.hose.width/2 + math.sin(math.radians(self.angle))*self.tank.hose.height




        
        self.dx = self.x - self.tank.hose.x
        self.dy = self.y - self.tank.hose.y


        self.vx = (self.dx/ ((self.dx**2 + self.dy**2)**(1/2)))* self.tank.force        
        self.vy = (self.dy/ ((self.dx**2 + self.dy**2)**(1/2)))* self.tank.force
        print(self.vx, self.vy, self.angle)
        self.gravity=1000
        
    
    def update(self,dt):


        self.vy -= self.gravity * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        
