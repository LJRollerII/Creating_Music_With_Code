from music21 import converter
import pygame

def play_song():
    # Load the MuseScore file as a music21 Score object
    score = converter.parse("yoursong.mscx")

    # Convert the score to a MIDI file
    midi_data = score.write('midi')

    # Save the MIDI file
    midi_file = "yoursong.mid"
    with open(midi_file, 'wb') as file:
        midi_data.write(file)

    # Initialize the pygame mixer
    pygame.mixer.init()

    # Load and play the MIDI file
    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.play()

    # Wait while the music is playing
    while pygame.mixer.music.get_busy():
        continue

    # Clean up and exit
    pygame.mixer.quit()
    pygame.quit()

# Call the function to play the song
play_song()
