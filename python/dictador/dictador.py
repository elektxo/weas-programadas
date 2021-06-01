import pyttsx3 

engine = pyttsx3.init()
engine.setProperty('rate', 100)
engine.setProperty('voice', 'spanish')
engine.setProperty('volume', 10)

engine.say("la suegra de mi creador es una pesada")
engine.runAndWait()
