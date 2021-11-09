import speech_recognition as sr
from datetime import date
from tkinter import *
from tkinter import messagebox

if __name__ == "__main__":
  gui = Tk()
  gui.title("UGA Assistant")
  gui.configure(background="grey")
  gui.geometry("640x420")
  res = Button(gui, text= 'Speak', fg = 'Black', bg='grey', command = lambda: speak(), height=5, width=10)
  res.grid(columnspan=4, ipadx=70)



def speak():
  recognizer = sr.Recognizer()
  print("Say something for 5 seconds:")
  with sr.Microphone() as source:
    audio_data = recognizer.record(source, duration=5) # just made it five seconds here for testing. 
    print("Recognizing...")
    text = recognizer.recognize_google(audio_data)
    print("Your Input:" , text)
    possible_dates = ["date", "today", "month", "day", "today's"]

    text_list = (text.split(' '))
  
    for i in text_list:
      for j in possible_dates:
        if i == j:
          today = date.today()
          d2 = today.strftime("%B %d, %Y")
          messagebox.showinfo('information', d2)
          exit(0)

gui.mainloop()

