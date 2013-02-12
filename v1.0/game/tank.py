
import pyglet
from pyglet.window import key
from . import bullet
from . import resources
from time import time

class Tank(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(img = resources.tank_image,*args,**kwargs)
        self.x = 200
        self.y = 200
        self.angle = 45
        self.hose = pyglet.sprite.Sprite(img=resources.hose_image)
        self.hose.x = self.x + self.width/2 
        self.hose.y = self.y + self.hose.width
        self.hose.rotation = self.angle
        self.force = 500
        self.rotate_speed = 50
        self.key_handler = key.KeyStateHandler()

        self.bullets = []
        self.bulletsBatch = pyglet.graphics.Batch()

        self.timerbase = 1
        self.timer = self.timerbase

    


    def draw(self):
        self.hose.draw()
        #self.bullet.draw()
        #for i in self.bullet:
        #    bullet.draw()
        self.bulletsBatch.draw()
        super().draw()
        

    def chooseBullet(self, bullet):
        self.bullet = bullet.Bullet(self)

    def update(self, dt):
        self.timer -= dt
        self.keys()
        self.rotate(dt)
        #self.bullet.update(dt)
        for i in self.bullets:
            i.update(dt)
        #print(self.hose.rotation)
       

    def shoot(self):
        if(self.timer <= 0):
            self.bullets.append(bullet.Bullet(self))
            self.timer = self.timerbase
        
                    

    def rotate(self, dt):
        if(self.key_handler[key.UP]):
            self.hose.rotation -= self.rotate_speed * dt
            if(self.hose.rotation < -90 and self.hose.rotation > -270):
                self.hose.rotation = -90
        elif(self.key_handler[key.DOWN]):
            self.hose.rotation += self.rotate_speed * dt
            if(self.hose.rotation > 90 and self.hose.rotation < 270):
                self.hose.rotation = 90


    def keys(self):
        if(self.key_handler[key.SPACE]):
            self.shoot()
    
        
        

