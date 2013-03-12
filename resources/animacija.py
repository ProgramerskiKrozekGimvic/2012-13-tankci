import pyglet


explosion_ani = pyglet.image.load_animation("explosion.gif")


class Explosion(pyglet.sprite.Sprite):
    def __init__(self, *args,**kwargs):
        super().__init__(img = explosion_ani ,  *args,**kwargs)
        self.x = 100
        self.y = 100
        
 


sprite = Explosion()
w = pyglet.window.Window(200,200)
@w.event
def on_draw():
    w.clear()
    sprite.draw()
pyglet.app.run()
    
