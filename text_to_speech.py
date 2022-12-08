import pyttsx3

# Initializing our speech engine
engine = pyttsx3.init()

# Setting up the voice we will use
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.fiona')

# Setting the rate at which the words will be spoken by the engine
engine.setProperty('rate', 150)

# Getting the text we will convert into speech
text = input("Enter the desired spoken text: ")

# Speaking the text
engine.say(text)

# Starting the actual engine
engine.runAndWait()
