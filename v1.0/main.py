import pyglet
from game import bullet
from game import resources
from game import tank

from game.maps import *

from game.screen import *




@game_window.event
def on_draw():
    game_window.clear()
    landscape.draw()

    
    test.draw()
   
def update(dt):

    test.update(dt)
    


test = tank.Tank()
test.shoot()

game_window.push_handlers(test.key_handler)





if(__name__== '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
