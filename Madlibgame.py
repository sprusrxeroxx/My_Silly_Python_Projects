#!/usr/bin/python3

import os
import getpass

from time import sleep

'''
    This game will write you a short story, with promts of your choosing. 
    The tale is written in the 2nd person narrative, and will be an impressionistic
    form
'''

#1.Create a story
story = '''
The train rattles through the steel skeleton of the city, each tremor echoing in the cavernous emptiness inside you.
Sunlight, filtered through a film of exhaust and dust, paints the carriage the color of old memories. 
Faces blur past the window, masks hiding the stories etched in tired eyes.
You trace the condensation on the glass, your fingernail leaving a thin streak across the cityscape reflected within.
Each droplet becomes a tiny mirror, showing a different, fragmented version of yourself - 
the one laughing with forgotten friends, the one chasing dreams now shrouded in mist, the one lost in the quiet ache of loneliness.

The station announcement crackles, the name of your stop garbled and indistinct. You rise, limbs heavy with an invisible weight, and shuffle onto the platform. 
The air is thick with the scent of diesel and damp stone, a familiar melancholy clinging to the very air. 
You walk, aimlessly at first, then drawn by a forgotten melody playing from a dusty gramophone on a street corner.

An old woman sits beside it, her fingers gnarled with time, coaxing the music from the worn grooves.
Her eyes, the color of faded denim, meet yours for a fleeting moment, a shared understanding passing between you. 
You stop, drawn by an invisible thread, and listen. The music speaks of love lost, of hopes broken, of the bittersweet ache of time passing. 
Each note hangs heavy in the air, a poignant echo of your own unspoken symphony.

As the melody fades, the woman closes the gramophone with a sigh. 
A single tear rolls down her cheek, mirroring the rain that begins to fall, a gentle curtain blurring the world around you. 
You offer her a smile, small and sad, and she returns it, a knowing glint in her eyes. 
In that shared silence, a silent connection sparks, a fleeting recognition of shared souls navigating the same storm.

Then, she turns, disappearing into the maze of streets, leaving you to the rhythm of raindrops and the distant rumble of the city. 
You continue your walk, the melody lingering in your heart like a half-forgotten dream.
Perhaps the melancholic tune serves as a reminder, a whisper in the wind, that even in the midst of sorrow, 
there exists a quiet beauty, a shared connection, a faint echo of hope waiting to be rediscovered.
'''

#2.Ask User for Input
os.system('clear')

print("The train rattles through the rusty steel skeleton of ...")

adj = input("Which town did you have your most fondest of memories?\n")

sleep(1)
os.system('clear')

print(f"The train rattles through the steel skeleton of old {adj}")

sleep(3)
os.system('clear')

print("Sunlight,filtered through a film of exhaust and dust, paints your carriage...")

sleep(2)

adj = input(f"What color is the carriage you're travelling in ?\n")

sleep(3)
os.system('clear')

print(f"Sunlight,filtered through a film of exhaust and dust, paints your carriage the smokey {adj} hue of yesterday")

sleep(3)
os.system('clear')

print("Faces blur past the window, some holding the stories you once you knew them by;")

sleep(2)

print("while most are just hollow masks stuffed with tired eyes.")

sleep(3)
os.system('clear')

print("You trace a smiley face on the frosted window, the cold sting on your fingernail")

sleep(3)

print(":)")

sleep(4)
os.system('clear')

print("Burns like forgotten laughter, caged in those inferntile eyes staring back")

sleep(4)
adj = getpass.getpass(prompt="Who is your childhood best friend ?\n")

sleep(2)
os.system('clear')

print(f"The one laughing with {adj}")



#3.Replace story Items with User Input
#4.Print Story

