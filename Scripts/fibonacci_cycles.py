from scamp import *

s = Session()
s.tempo = 120

clarinet = s.new_part("clarinet")

a, b = 8, 7
while True:
    print(a, end=", ")
    clarinet.play_note(55 + a, 0.7, 0.25)
    a, b = b, (a + b) % 29