import speech_recognition as sr
import sys
from datetime import date

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
          print(d2)
          exit(0)
      
