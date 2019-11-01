import speech_recognition as sr
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

class App():
	def __init__(self, master):
		frame = Frame(master, background='red')
		self.l1 = Label(text="Please select your audio file", font=("Helvitca", 12)).grid(column=0,row=0,padx=110,pady=15)
		self.button = Button(main,text='Select file',command=self.ask).grid(column=0,row=1)

	def ask(self):
		Tk().withdraw()
		file = askopenfilename()
		
		if file.endswith('.wav'):
			with sr.AudioFile(file) as source: 
				audio = r.record(source) 
			try: 
				#print("The audio file contains: " + r.recognize_google(audio))
				self.l2 = Label(text="The audio file contains: " + r.recognize_google(audio), font=("Helvitca", 13)).grid(column=0,row=3, pady=15, sticky="nsew")
			except sr.UnknownValueError: 
				print("Google Speech Recognition could not understand audio") 
			except sr.RequestError as e: 
				print("Could not request results from Google Speech Recognition service; {0}".format(e))	
		else:
			messagebox.showerror("Invalid","Please select wav format file")



main = Tk()
app = App(main)
r = sr.Recognizer()
main.geometry("400x200+300+250")
main.mainloop()