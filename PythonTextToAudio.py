# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO CONVERT THE USER-INPUT TEXT TO AUDIO FILE AND PLAY THE SAVED AUDIO FILE
# using gTTS and pygame modules of Python
#
# gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google
# Translate’s text-to-speech API. Writes spoken mp3 data to a file, a file-like object
# (bytestring) for further audio manipulation, or stdout. It features flexible pre-processing
# and tokenizing.
#
# pygame is a Free and Open Source cross-platform library for the development of multimedia
# applications like video games on Python. It uses the Simple DirectMedia Layer library and
# several other popular libraries to abstract most common functions and makes writing these
# program a more intuitive task.
#
# The modules can be installed using the command - pip install gTTS, pip install pygame

# Importing the necessary packages
import pygame
from gtts import gTTS

# Initializing the pygame
pygame.mixer.init()

# Defining convertToAudio() with user-input filename and input_string as the parameters
def convertToAudio(audioName, i_inputString):
    # Creating object of gTTS() engine with user-input string as the text language
    # (lang) as English(en). Optional Parameter slow=True means audio will have slow speed
    gtts_obj = gTTS(text=i_inputString, lang='en')

    # Saving the converted audio with user-input audio name in the specified path
    # Please specify YOUR SYSTEM PATH in place of YOUR_DESTINATION_PATH
    gtts_obj.save("YOUR_DESTINATION_PATH" + audioName)
    print("\nAUDIO SAVED SUCCESSFULLY USING gTTS MODULE")

    # Loading the saved audio file for playback using the music.load() method
    # Please specify YOUR SYSTEM PATH in place of YOUR_DESTINATION_PATH
    pygame.mixer.music.load("YOUR_DESTINATION_PATH" + audioName)
    # Starting the playback of the music stream
    pygame.mixer.music.play()

    # Checking if music stream is playing
    while pygame.mixer.music.get_busy():
        continue

if __name__ == '__main__':
    # Prompting the user to enter a name for the saved audio file
    audioFileName = input("\nNAME FOR THE AUDIO FILE WITH .mp3 EXTENSION : ")
    # Prompting the user to enter a string
    inputString = input("\nSTRING TO BE SAVED AS AUDIO : ")
    # Calling the convertToAudio() with the user-input values as the parameters
    convertToAudio(audioFileName, inputString)
