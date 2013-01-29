import pyglet

class Tank(pyglet.sprite.Sprite):
    def __init__(*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.angle = 45

        self.bullet = None
        self.force = 200

    def chooseBullet(self, bullet):
        self.bullet = bullet

    def shoot(self):
        self.bullet.shootForce(self.force)
