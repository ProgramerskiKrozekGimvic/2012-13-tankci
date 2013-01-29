import pyglet
from game import bullet



game_window = pyglet.window.Window(width = 500, height = 500, caption="Tanks")
@game_window.event
def on_draw():
    game_window.clear()
    bullet.draw()
def update(dt):
    bullet.update(dt)
bullet = bullet.Bullet( pyglet.resource.image("bullet.png"))

if(__name__== '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
