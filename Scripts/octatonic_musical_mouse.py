from scamp import *
from scamp_extensions.pitch import Scale

s = Session()

scale = Scale.pentatonic(60)
basoon = s.new_part("basoon")

countdown = 0.1
last_position = (0,0)

def mouse_mouse_listener(x,y):
    global countdown, last_position
    dx, dy = x - last_position[0], y - last_position[1]
    countdown -= (dx ** 2 + dy ** 2) ** 0.5
    if countdown < 0:
        basoon.play_note(scale.round(34 + 40 * (1-y)), x, 0.1,
                         blocking=False)
        countdown = 0.1

s.register_mouse_listener(on_move=mouse_mouse_listener,
                          relative_coordinates=True)

s.wait_forever()
