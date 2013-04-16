import pyglet
from game import bullet
from game import resources
from game import tank
from pyglet.window import key
from game.maps import *
from game.screen import *
from game import splosno
from game import explosion
from game import menu

game_playing= False
@game_window.event
def on_draw():
    game_window.clear()
    
    if(game_playing):
        landscape.draw()
        for tank in splosno.tank_list:
            tank.draw()
        for i in splosno.explosion_list:
            i.draw()
    else:
        game_menu.draw()

@game_window.event
def on_mouse_press(x, y, button, modifiers):
    button = game_menu.on_press(x,y)
    if(button):
        if(button.lower() == "play"):
            global game_playing
            initGame()
            game_playing = True
        elif(button.lower() == "up"):
            splosno.NumPlayer += 1
            #print(splosno.NumPlayer)
            game_menu.player_counter.text = str(splosno.NumPlayer)
            
            
        elif(button.lower() == "down"):
            splosno.NumPlayer -= 1
            game_menu.player_counter.text = str(splosno.NumPlayer)
            
    
   
def update(dt):
    
        
    if(game_playing):
        counter = 0

        for tank in splosno.tank_list:
            tank.update(dt)
            
        for tank in splosno.tank_list:
            if(tank.alive == True):
                counter+=1
                
        if(counter <= 1):
            pyglet.clock.schedule_once(end_game,3)
            
        if(counter <= 1):
            game_window.close()


def initGame():
    keys = [ {"key1": key.W, "key2": key.A,"key3":key.D},
         {"key1": key.UP, "key2": key.LEFT,"key3":key.RIGHT},
         {"key1": key.I, "key2": key.J,"key3":key.L},
         {"key1": key.NUM_8, "key2": key.NUM_4,"key3":key.NUM_6} ]
    
    for i in range(splosno.NumPlayer):
        splosno.tank_list.append(tank.Tank(x=i*350, **keys[i]))    
    
def end_game(dt):
    game_window.close()
    


game_menu = menu.Menu()

if(__name__== '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
