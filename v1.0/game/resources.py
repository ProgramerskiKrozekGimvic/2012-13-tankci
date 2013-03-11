import pyglet
#from . import bullet

pyglet.resource.path = ["../resources"]
pyglet.resource.reindex()

bullet_image = pyglet.resource.image('bullet.png')

tank_image = pyglet.resource.image('tank_body.png')


hose_image = pyglet.resource.image('tank_hose.png')
hose_image.anchor_x = hose_image.width/2 
hose_image.anchor_y = 0

explosion_frames = ("../resources/Untitled-20000.png",
                    "../resources/Untitled-20003.png",
                    "../resources/Untitled-20006.png",
                    "../resources/Untitled-20009.png",
                    "../resources/Untitled-20012.png",
                    "../resources/Untitled-20015.png",
                    "../resources/Untitled-20018.png",
                    "../resources/Untitled-20021.png",
                    "../resources/Untitled-20024.png",
                    "../resources/Untitled-20027.png",
                    "../resources/Untitled-20030.png",
                    "../resources/Untitled-20033.png",
                    "../resources/Untitled-20036.png",
                    "../resources/Untitled-20039.png",
                    "../resources/Untitled-20042.png",
                    "../resources/Untitled-20045.png",
                    "../resources/Untitled-20048.png")
explosion_img= map(lambda img: pyglet.image.load(img),explosion_frames)
explosion_ani= pyglet.image.Animation.from_image_sequence(explosion_img,0.12,loop = None)
#explosion = pyglet.sprite.Sprite(explosion_ani)
