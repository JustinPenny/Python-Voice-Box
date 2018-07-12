# My voice box present for Tay

import pygame
import time
import os.path


import pygame

# Function defs pulled from https://gist.github.com/juehan/1869090
def playsound(soundfile):
    """Play sound through default mixer channel in blocking manner.
       This will load the whole sound into memory before playback
    """    
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        print "Playing..."
        clock.tick(1000)

def playmusic(soundfile):
    """Stream music with mixer.music module in blocking manner.
       This will stream the sound from disk while playing.
    """
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        ##print "Playing..."
        clock.tick(1000)
        

def stopmusic():
    """stop currently playing music"""
    pygame.mixer.music.stop()

def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
	BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
	FREQ, SIZE, CHAN = getmixerargs()

# Greeting to play automatically so that she knows it has started up properly.
playmusic('welcome')

while 1:

    # Getting choice of file to play
    selection = raw_input()
    type(selection)
    
    # Error checking inputs
    if len(selection) < 3:
        if (selection == '0'):
            selection = 'skrrt' # Easter egg
        else:    
            selection = 'lessthan3'
        
    elif len(selection) > 3:
        selection = 'greaterthan3'

    # Getting the file name
    file = 'clip' + selection #+ '.mp3'

    if os.path.isfile(file) == True:
         
        # Playing the file
        playmusic(file)
    else:
        playmusic('notfound')

