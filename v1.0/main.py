import pyglet
from game import bullet
from game import resources
from game import tank
from pyglet.window import key
from game.maps import *
from game.screen import *
from game.splosno import *




@game_window.event
def on_draw():
    game_window.clear()
    landscape.draw()
    for tank in tank_list:
        tank.draw()
   
def update(dt):
    for tank in tank_list:
        tank.update(dt)
    
    


tank_list.append(tank.Tank(key1 = key.SPACE, key2  =key.UP, key3=key.DOWN,x = 50))
tank_list.append(tank.Tank(key1 = key.D, key2  =key.W, key3=key.S,x = 1000))





if(__name__== '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
