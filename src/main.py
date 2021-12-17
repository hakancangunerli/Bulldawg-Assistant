import speech_recognition as sr
from datetime import date
from tkinter import *
from tkinter import messagebox
from urllib.request import urlopen
from datetime import date
from datetime import datetime
import requests
import calendar
from busOccupancy import bus_occupancy, get_bus_num


def check_question(input): #This Function checks the what the question is being asked
   possible_dates = ["date", "today", "month", "day", "today's"]
   possible_bus = ["central", "loop", "east", "campus", "science", "health"]
   possible_dining = ["snelling", "bolton", "ohouse", "house", "village", "summit", "joe", "frank", "niche"]

   for i in input:
     if i in possible_dates:
       return "date"
     elif i.lower() in possible_bus:
       return i.lower()
     elif i.lower() in possible_dining:
       return i.lower()
  

def speak(): #The main one
  recognizer = sr.Recognizer()
  print("Say something for 5 seconds:")
  with sr.Microphone() as source:
    audio_data = recognizer.record(source, duration=5) # just made it five seconds here for testing. 
    print("Recognizing...")
    try:
      text = recognizer.recognize_google(audio_data, language = 'en-US')
    except Exception as e:
      return "None"
    #text = "what is the dining capacity at o house"
    print("Your Input:" , text)

  text_list = (text.split(' '))

  output = check_question(text_list)
  print(output)
  if output == "date":
    d2 = my_date.strftime("%B %d, %Y")
    messagebox.showinfo('information', d2)
  elif output == "central":
    bus_occupancy("Central Loop")
  elif output == "east":
    bus_occupancy("East Campus")
  elif output == "health":
    bus_occupancy("Health Science")
  else:
    from dining import dining_status
    dining_status(output)

if __name__ == "__main__":
  gui = Tk()
  gui.title("UGA Assistant")
  gui.configure(background="grey")
  gui.geometry("640x420")
  res = Button(gui, text= 'Speak', fg = 'Black', bg='grey', command = lambda: speak(), height=5, width=10)
  res.grid(columnspan=4, ipadx=70)


#gui.mainloop()
speak()