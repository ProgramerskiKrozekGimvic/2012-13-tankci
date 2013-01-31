import pyglet
from pyglet.window import key
from . import resources

class Tank(pyglet.sprite.Sprite):
    def __init__(self, *args,**kwargs):
        super().__init__(img = resources.tank_image, *args,**kwargs)
        self.angle = 45
        self.hose = pyglet.sprite.Sprite(img=resources.hose_image)
        self.hose.x = self.width/2 - self.hose.width/2
        self.hose.y = self.hose.width
        self.hose.rotation = self.angle

        self.bullet = None
        self.force = 200
        self.rotate_speed = 50

        self.key_handler = key.KeyStateHandler()

    def draw(self):
        self.hose.draw()
        super().draw()
        

    def chooseBullet(self, bullet):
        self.bullet = bullet

    def update(self, dt):
        self.rotate(dt)

    def shoot(self):
        self.bullet.shootForce(self.force)

    def rotate(self, dt):
        if(self.key_handler[key.UP]):
            self.hose.rotation -= self.rotate_speed * dt
            if(self.hose.rotation > 90 and self.hose.rotation < 270):
                self.hose.rotation = 90
        elif(self.key_handler[key.DOWN]):
            self.hose.rotation += self.rotate_speed * dt
            if(self.hose.rotation > 90 and self.hose.rotation < 270):
                self.hose.rotation = 90
        
 
    
        
        
