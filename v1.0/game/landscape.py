import pyglet
from pyglet.gl import *
from .screen import *

class Landscape():
    def __init__(self,height = None, color = (0, 1, 0)):
        self.color = color
        self.height = None
        if(height == None):
            self.height = game_window.width //4
        else:       
            self.height = height

    def draw(self):
        glColor3f(*self.color)
        pyglet.graphics.draw_indexed(4, GL_TRIANGLES, [0, 1, 2, 0, 2, 3], 
                         ('v2i', (0, 0,
                                  0, self.height,
                                  game_window.width, self.height,
                                  game_window.width, 0 ))
                                 )
