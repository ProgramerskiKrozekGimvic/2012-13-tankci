import pyglet
from game import bullet
from game import resources
from game import tank
from pyglet.window import key
from game.maps import *
from game.screen import *




@game_window.event
def on_draw():
    game_window.clear()
    landscape.draw()
    test.draw()
    test2.draw()
   
def update(dt):
    test.update(dt)
    test2.update(dt)
    test.ifAlive()
    test2.ifAlive()
    print(test.hp)
    print(test2.hp)
    
    


test = tank.Tank(key1 = key.SPACE, key2  =key.UP, key3=key.DOWN,x = 50)
test2 = tank.Tank(key1 = key.D, key2  =key.W, key3=key.S,x = 450)
test.shoot()
test2.shoot()

game_window.push_handlers(test.key_handler)
game_window.push_handlers(test2.key_handler)





if(__name__== '__main__'):
    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()
