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
        self.buttons.append(Button(name = "Play", img = resources.play_img, x =215 , y =225 , batch = self.buttons_batch))
        self.buttons.append(Button(name = "Up", img = resources.up_img , x = 270 , y =300 , batch = self.buttons_batch))
        self.buttons.append(Button(name = "Down", img = resources.down_img , x = 215, y =300 , batch = self.buttons_batch))
        self.player_counter = pyglet.text.Label(text = str(splosno.NumPlayer),x = 240, y = 300, width  = 25 , height = 25)
        
       



    def draw(self):
        self.buttons_batch.draw()
        self.player_counter.draw()
        
    def on_press(self, x, y):
        print(splosno.NumPlayer)
        for i in self.buttons[:]:
            if((x > i.x )and (x < (i.x + i.width))and (y > i.y and (y < (i.y + i.height)))):
                return(i.name)


class Button(pyglet.sprite.Sprite):
    def __init__(self, name = "Button", *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)

    
