import pyglet
from pyglet.window import key
from . import resources

class Tank(pyglet.sprite.Sprite):
    def __init__(self, *args,**kwargs):
        super().__init__(img = resources.tank_image, *args,**kwargs)
        self.angle = 45
        self.hose = pyglet.sprite.Sprite(img=resources.hose_image)
        self.hose.x = self.width/2 - self.hose.width/2
        self.hose.y = self.y
        #self.rotation = self.angle

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
#        print("Rotate")
#        print(self.key_handler[key.UP])
        if(self.key_handler[key.UP]):
 #           print("Gor")
            self.hose.rotation += self.rotate_speed * dt
        elif(self.key_handler[key.DOWN]):
  #          print("Dol")
            self.hose.rotation -= self.rotate_speed * dt
        
 
    
        
        
