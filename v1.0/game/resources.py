import pyglet
#from . import bullet

pyglet.resource.path = ["../resources"]
pyglet.resource.reindex()

bullet_image = pyglet.resource.image('bullet.png')

tank_image = pyglet.resource.image('tank_body.png')


hose_image = pyglet.resource.image('tank_hose.png')
hose_image.anchor_x = hose_image.width/2 
hose_image.anchor_y = 0

explosion_image = pyglet.resource.animation("explosion.gif")


