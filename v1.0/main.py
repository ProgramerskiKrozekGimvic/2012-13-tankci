import pyglet
from game import bullet
from game import resources
from game import tank
#from game.screen import *



game_window = pyglet.window.Window(width = 500, height = 500, caption="Tanks")
@game_window.event
def on_draw():
    game_window.clear()
#    metek1.draw()
    test.draw()
def update(dt):
#    metek1.update(dt)
    test.update(dt)


#metek1 = bullet.Bullet()
test = tank.Tank()

game_window.push_handlers(test.key_handler)

if(__name__== '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
