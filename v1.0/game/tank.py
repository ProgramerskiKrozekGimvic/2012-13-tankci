from . import splosno
import pyglet
from pyglet.gl import *
from pyglet.window import key
from . import bullet
from . import resources
from time import time
from .screen import *
from .maps import *
from .splosno import *

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
        self.force = 1000
        self.rotate_speed = 50
        self.key_handler = key.KeyStateHandler()
        self.hp = 100
        self.alive = True

        self.bulletsBatch = pyglet.graphics.Batch()
        self.hpBar = True
        self.timerbase = 1
        self.timer = self.timerbase
        self.timer2 = self.timerbase
        resources.explosion.x = self.x
        resources.explosion.y = self.y
        
        
        


        game_window.push_handlers(self.key_handler)
        

    def draw(self):
        self.hose.draw()
        self.bulletsBatch.draw()
        super().draw()
        #hpbar 
        glColor3f(1, 0, 0)
        pyglet.graphics.draw_indexed(4, GL_TRIANGLES, [0, 1, 2, 0, 2, 3], 
                         ('v2i', (self.x, self.y + self.height + 30,
                                  self.x, self.y + self.height + 20,
                                  self.x + int(self.width*(self.hp / 100)), self.y + self.height + 20,
                                  self.x + int(self.width*(self.hp / 100)), self.y + self.height + 30))
                                 )    
        

    def chooseBullet(self, bullet):
        self.bullet = bullet.Bullet(self)

    def update(self, dt):
        self.timer -= dt
        self.keys()
        self.rotate(dt)
        self.isHit()
        for i in splosno.bullets[:]:
            i.update(dt)
            if(i.x <= 0 or i.x >=game_window.width):
                splosno.bullets.remove(i)
            if(i.y <= landscape.height):
                splosno.bullets.remove(i)
            
                
    def isHit(self):
        for i in splosno.bullets[:]:
            if((i.x >= self.x and i.x <= self.x + self.width)
               and(i.y >= self.y and i.y <= self.y + self.height)):
               self.hp -= i.dmg
               splosno.bullets.remove(i)
        self.ifAlive()
    
    def ifAlive(self):
        if(self.hp <= 0):
            
            self.delete()
            tank_list.remove(self)
            self.Alive = False
            #resources.explosion.draw()
    
               

    def shoot(self):
       if(self.timer <= 0):
            splosno.bullets.append(bullet.Bullet(self))
            self.timer = self.timerbase
            
       
        
           
           
                        

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
        
    
        
        

