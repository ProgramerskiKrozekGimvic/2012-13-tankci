import pyglet
from game import bullet
from game import resources
from game import tank
from game import landscape as ls
from game.screen import *




@game_window.event
def on_draw():
    game_window.clear()
    landscape.draw()

    
    test.draw()
   
def update(dt):
#    metek1.update(dt)
    test.update(dt)
    

#metek1 = bullet.Bullet()
test = tank.Tank()
test.shoot()

game_window.push_handlers(test.key_handler)

landscape = ls.Landscape(color = (1, 1, 1))



if(__name__== '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
