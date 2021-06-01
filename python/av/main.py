import JarvisAI
import pyttsx3 as psy

engine = psy.init()
engine.setProperty('rate', 100)
engine.setProperty('voice', 'spanish')
engine.setProperty('volume', 100)
engine.runAndWait()

obj = JarvisAI.JarvisAssistant()
response = obj.mic_input()
psy.speak(response)
