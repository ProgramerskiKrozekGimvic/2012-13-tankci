import pyglet
window = pyglet.window.Window(width=200,height=200)
label = pyglet.text.Label(text="test",x = 50,y = 50,
                          color =(255,255,255,255), font_size = 2.4,
                          height = 10, width = 50)
@window.event
def on_draw():
    window.clear()
    label.draw()
    label2.draw()

def update(dt):
    pass


x = 5
label2 = pyglet.text.Label(text="BLABLA")
label2.text=str(x)
pyglet.clock.schedule_interval(update, 1/120)
pyglet.app.run()
