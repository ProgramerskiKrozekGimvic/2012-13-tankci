import pyglet
#import main
from pyglet.gl import *
from .screen import *

class Landscape():
    def __init__(self, color = (0, 1, 0)):
        self.color = color
        
    def draw(self):
        glColor3f(*self.color)
        pyglet.graphics.draw_indexed(4, GL_TRIANGLES, [0, 1, 2, 0, 2, 3], 
                         ('v2i', (0, 0,
                                  0, game_window.height//4,
                                  game_window.width, game_window.height//4,
                                  game_window.width, 0 ))
                                 )
