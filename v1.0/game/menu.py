import pyglet
from pyglet.gl import *

class Menu():
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
        self.label_play= pyglet.text.Label(text="PLAY",
                                           color=(0,0,0,255),
                                           width = 400,
                                           height = 50,
                                           font_size = 50
                                           )
        self.label_up=pyglet.text.Label(text='+',
                                        x = 50,
                                        y=56,
                                        color=(0,0,0,255),
                                        font_size = 15)
        self.label_down=pyglet.text.Label(text='-',
                                        x = 17,
                                        y=58,
                                        color=(0,0,0,255),
                                        font_size = 15)



    def draw(self):
        #playbutton
        pyglet.graphics.draw_indexed(4, GL_TRIANGLES, [0, 1, 2, 1, 2, 3],
                                      ('v2i',(0,0,
                                              0,50,
                                              170,0,
                                              170,50)))
        self.label_play.draw()
        #player up
        pyglet.graphics.draw_indexed(3, GL_TRIANGLES,[0,1,2],
                                     ('v2i',(50,50,
                                             70,63,
                                             50,75)))
        self.label_up.draw()
        #player down
        pyglet.graphics.draw_indexed(3, GL_TRIANGLES,[0,1,2],
                                     ('v2i',(25,50,
                                             5,63,
                                             25,75)))
        self.label_down.draw()
                                             
        
