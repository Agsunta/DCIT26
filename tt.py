import pyttsx3
engine = pyttsx3.init() # object creation
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
engine.setProperty('rate', 150)
engine.say("Hello fucking World!")
engine.runAndWait()
