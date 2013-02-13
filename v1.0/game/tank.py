
import pyglet
from pyglet.window import key
from . import bullet
from . import resources
from time import time
from .screen import *
from .maps import *

class Tank(pyglet.sprite.Sprite):
    def __init__(self,key1= None,key2 = None,key3 = None,x = None, *args,**kwargs):
        super().__init__(img = resources.tank_image,*args,**kwargs)

        self.key1 = key1
        self.key2 = key2
        self.key3 = key3
        self.x = x
        self.y = landscape.height
        self.angle = 45
        self.hose = pyglet.sprite.Sprite(img=resources.hose_image)
        self.hose.x = self.x + self.width/2 
        self.hose.y = self.y + self.hose.width
        self.hose.rotation = self.angle
        self.force = 600
        self.rotate_speed = 50
        self.key_handler = key.KeyStateHandler()

        self.bullets = []
        self.bulletsBatch = pyglet.graphics.Batch()

        self.timerbase = 1
        self.timer = self.timerbase

    


    def draw(self):
        self.hose.draw()
    
        self.bulletsBatch.draw()
        super().draw()
        

    def chooseBullet(self, bullet):
        self.bullet = bullet.Bullet(self)

    def update(self, dt):
        self.timer -= dt
        self.keys()
        self.rotate(dt)
       
        for i in self.bullets[:]:
            i.update(dt)
            if(i.x <= 0 or i.x >=500):
                self.bullets.remove(i)
            if(i.y <= landscape.height):
                self.bullets.remove(i)
       
       

    def shoot(self):
        if(self.timer <= 0):
            self.bullets.append(bullet.Bullet(self))
            self.timer = self.timerbase
            print(self.bullets)
        
                    

    def rotate(self, dt):
        if(self.key_handler[self.key2]):
            self.hose.rotation -= self.rotate_speed * dt
            if(self.hose.rotation < -90 and self.hose.rotation > -270):
                self.hose.rotation = -90
        elif(self.key_handler[self.key3]):
            self.hose.rotation += self.rotate_speed * dt
            if(self.hose.rotation > 90 and self.hose.rotation < 270):
                self.hose.rotation = 90


    def keys(self):
        if(self.key_handler[self.key1]):
            self.shoot()
    
        
        

