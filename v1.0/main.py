import pyglet
from game import bullet
from game import resources
from game import tank
from pyglet.window import key
from game.maps import *
from game.screen import *
from game.splosno import *
from game import explosion
from game import menu


    

@game_window.event
def on_draw():
    game_window.clear()
    game_menu.draw()
    """if(game_playing):
        landscape.draw()
        for tank in tank_list:
            tank.draw()
        for i in explosion_list:
            i.draw()
    else:
        startmenu.draw()"""
        
@game_window.event
def on_mouse_press(x, y, button, modifiers):
    print(x,y,button, modifiers)

   
def update(dt):
    """if(game_playing):
        counter = 0

        for tank in tank_list:
            tank.update(dt)
            
            
        for tank in tank_list:
            if(tank.alive == True):

<<<<<<< HEAD
            counter += 1
    if(counter <= 1):
        pyglet.clock.schedule_once(end_game,3)

        
=======
                counter += 1
        if(counter <= 1):
            game_window.close()"""
>>>>>>> miha je gej

    
    
def end_game(dt):
    game_window.close()
    
#preberemo stevilo igralcev
stIgralcev = 4

keys = [ {"key1": key.W, "key2": key.A,"key3":key.D},
         {"key1": key.UP, "key2": key.LEFT,"key3":key.RIGHT},
         {"key1": key.I, "key2": key.J,"key3":key.L},
         {"key1": key.NUM_8, "key2": key.NUM_4,"key3":key.NUM_6} ]

game_menu = menu.Menu()

for i in range(stIgralcev):
    tank_list.append(tank.Tank(x=i*350, **keys[i]))
   
        



if(__name__== '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
