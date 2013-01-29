import pyglet
from . import resources

class Bullet(pyglet.sprite.Sprite):
    def __init__(self,*args, img = resources.bullet_image, **kwargs):
        super().__init__(img, *args,**kwargs)
        self.vy= 100
        self.vx= 150
        self.x = 0
        self.y = 0
        self.gravity=50
    def update(self,dt):
        self.vy -= self.gravity * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
