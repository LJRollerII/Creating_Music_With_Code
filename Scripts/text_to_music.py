from scamp import *

s = Session()

piano = s.new_part("piano")

text = "music.py"

for char in text:
    if char == " ":
        wait(0.2) # wait a fifth of a second
    elif char.isalnum():
        piano.play_note(ord(char) - 20, 0.5, 0.06) #(pitch, volume, duration(sec))
    else:
        wait(0.2)
        piano.play_note(ord(char), 0.8, 0.06)
        wait(0.2)