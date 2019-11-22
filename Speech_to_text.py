import speech_recognition as sr
import tkinter as tk
from tkinter.filedialog import askopenfilename

def ask():
    r = sr.Recognizer()
    file = askopenfilename()
    if file.endswith('.wav'):
        with sr.AudioFile(file) as source:
            audio = r.record(source) 
        try:
            print("The audio file contains: " + r.recognize_google(audio))
        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio") 
        except sr.RequestError as e: 
            print("Could not request results from Google Speech Recognition service; {0}".format(e))	
    else:
        print("Please select wav format file")

tk.Tk().withdraw()
