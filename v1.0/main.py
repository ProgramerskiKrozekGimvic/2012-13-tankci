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
    counter = 0
    for tank in tank_list:
        tank.update(dt)
        
        
    for tank in tank_list:
        if(tank.alive == True):

            counter += 1
    if(counter <= 1):
        game_window.close()
    
    
#preberemo stevilo igralcev
stIgralcev = int(input("Number of players"))
RandomDigit = stIgralcev
keys = [ {"key1": key.W, "key2": key.A,"key3":key.D},
         {"key1": key.UP, "key2": key.LEFT,"key3":key.RIGHT},
         {"key1": key.I, "key2": key.J,"key3":key.L},
         {"key1": key.NUM_8, "key2": key.NUM_4,"key3":key.NUM_6} ]

for i in range(stIgralcev):
    tank_list.append(tank.Tank(x=i*350, **keys[i]))

"""tank_list.append(tank.Tank(key1 = key.SPACE, key2  =key.UP, key3=key.DOWN,x = 50))
tank_list.append(tank.Tank(key1 = key.D, key2  =key.W, key3=key.S,x = 1000))
tank_list.append(tank.Tank(key1 = key.SPACE, key2  =key.UP, key3=key.DOWN,x = 500))"""

if(__name__== '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
