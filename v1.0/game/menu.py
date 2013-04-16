import pyglet
from pyglet.gl import *
from game import resources
from game import screen
from game import splosno

class Menu():
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        

        self.buttons_batch = pyglet.graphics.Batch()
        self.buttons = []
        self.buttons.append(Button(name = "Play", img = resources.play_img, x = int(screen.game_window.width/2 - 35) ,
                                   y =int(screen.game_window.height/2- 25) , batch = self.buttons_batch))
        self.buttons.append(Button(name = "Up", img = resources.up_img , x = 285, y =280 , batch = self.buttons_batch))
        self.buttons.append(Button(name = "Down", img = resources.down_img , x = 190, y =280 , batch = self.buttons_batch))
        self.player_counter = pyglet.text.Label(text = str(splosno.NumPlayer),x = 240, y = 280, width  = 25 , height = 25
                                                ,font_size = 25,font_name = 'Top Secret')
        self.header = pyglet.text.Label(text = "TANKS", x = 115, y = 350 , height = 60, width = 70, font_name = 'Top Secret', font_size = 60)
        self.sign  = pyglet.text.Label(text ="Number of players", x = 155 ,y=315, font_name='Top Secret')
        
       



    def draw(self):
        self.buttons_batch.draw()
        self.player_counter.draw()
        self.header.draw()
        self.sign.draw()
        
    def on_press(self, x, y):
        for i in self.buttons[:]:
            if((x > i.x )and (x < (i.x + i.width))and (y > i.y and (y < (i.y + i.height)))):
                return(i.name)


class Button(pyglet.sprite.Sprite):
    def __init__(self, name = "Button", *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)

    
