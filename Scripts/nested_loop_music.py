from scamp import *
from scamp_extensions.pitch import Scale

s = Session()

violin = s.new_part("violin")

d_minor = Scale.natural_minor(62)

while True:
    for n in range(3):
        for m in range(3):
            for l in range(3):
                for k in range(3):
                    for k in range(3):
                        violin.play_note(d_minor[k + l + m + n], 0.8, 0.25)
