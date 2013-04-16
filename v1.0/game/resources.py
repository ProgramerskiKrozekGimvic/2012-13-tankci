import pyglet
#from . import bullet

pyglet.resource.path = ["../resources"]
pyglet.resource.reindex()

bullet_image = pyglet.resource.image('bullet.png')

tank_image = pyglet.resource.image('tank_body.png')


hose_image = pyglet.resource.image('tank_hose.png')
hose_image.anchor_x = hose_image.width/2 
hose_image.anchor_y = 0
explosion_ani = pyglet.image.load_animation("../resources/explosion.gif")
play_img = pyglet.resource.image('play_button.png')
down_img = pyglet.resource.image('down_button.png')
up_img = pyglet.resource.image('up_button.png')
pyglet.font.add_file('../resources/Top Secret.ttf')
custom = pyglet.font.load('Top Secret')
