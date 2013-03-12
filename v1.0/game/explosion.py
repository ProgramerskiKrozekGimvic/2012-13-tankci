import pyglet
from . import resources
from . import splosno

class Explosion(pyglet.sprite.Sprite):
    def __init__(self, tank, *args,**kwargs):
        super().__init__(img = resources.explosion_ani ,  *args,**kwargs)
        self.tank = tank
        self.x = tank.x
        self.y = 0
        

    
        
        
        
