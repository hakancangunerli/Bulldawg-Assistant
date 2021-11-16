import speech_recognition as sr
from datetime import date
from tkinter import *
from tkinter import messagebox
from urllib.request import urlopen
from datetime import date
import requests
import calendar




CENTRAL_LOOP = 4918
EAST_CAMPUS = 4921
HEALTH_SCIENCE = 2611
my_date = date.today()
weekday = calendar.day_name[my_date.weekday()]

if __name__ == "__main__":
  gui = Tk()
  gui.title("UGA Assistant")
  gui.configure(background="grey")
  gui.geometry("640x420")
  res = Button(gui, text= 'Speak', fg = 'Black', bg='grey', command = lambda: speak(), height=5, width=10)
  res.grid(columnspan=4, ipadx=70)



def bus_occupancy(bus_name):
    user_input = bus_name
    result = ""
    bus_num = get_bus_num(bus_name.replace(" ", ""))

    if bus_num == -1:
        result += "This bus is not supported by this program"
        messagebox.showinfo('information', result)
        return 
  
    url = "https://routes.uga.edu/Route/" + str(bus_num) + "/Vehicles"
    r = requests.get(url)
    data = r.json()
    list_data = list(data)
    num_bus_active = len(list_data)

    if num_bus_active == 0:
        result = "There are no buses active for the route: " + user_input
        messagebox.showinfo('information', result)
        return
    elif num_bus_active == 1:
        result += "There are " + str(num_bus_active) + " bus active for the route: " + user_input
    else:
        result += "There are " + str(num_bus_active) + " buses active for the route: " + user_input

    for i in range(0, num_bus_active):
        result += "\nBus " + str(i + 1) + " is " + str( list(list_data[i].values())[1]) + "% full"
    
    messagebox.showinfo('information', result)

def get_bus_num(bus_name):
    if(bus_name.lower() == "centralloop"):
        return CENTRAL_LOOP
    elif(bus_name.lower() == "eastcampus"):
        return EAST_CAMPUS
    elif(bus_name.lower() == "healthscience"):
        return HEALTH_SCIENCE
    else:
        return -1

def dining_occupancy(input):
  user_dining = input
  user_dining = user_dining.replace(" ", "")

  url = "https://apps.auxiliary.uga.edu/Dining/OccupancyCounter/api/occupancy.php"
  try:
      urlopen(url)
  except:
      print("Error opening the URL")



  #print(soup)

  r = requests.get(url)
  data = r.json()
  lst = list(data.values())

  dining_halls = lst[3]


  availability = list(dining_halls.values())

  bolton = availability[0]
  village_summit = availability[1]
  o_house = availability[2]
  snelling = availability[3]
  niche = availability[4]

  bolton_list = list(bolton.values())
  bolton_num = bolton_list[0]

  village_summit_list = list(village_summit.values())
  village_summit_num = village_summit_list[0]

  o_house_list = list(o_house.values())
  o_house_num = o_house_list[0]

  snelling_list = list(snelling.values())
  snelling_num = snelling_list[0]

  niche_list = list(niche.values())
  niche_num = niche_list[0]

  bolton_open = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  village_open = bolton_open
  ohouse_open = bolton_open[0:5]
  snelling_open = bolton_open[0:5]
  niche_open = bolton_open[0:5]

  if(user_dining.lower() == "bolton" and weekday in bolton_open):
      print(100 - bolton_num)
      messagebox.showinfo('information', "Bolton has " + str(100 - bolton_num) + "% occupacy left")

  elif((user_dining.lower() == "village" or user_dining.lower() == "summit" or user_dining.lower() == "joe" or user_dining.lower() == "frank")and weekday in village_open):
      print(100 - village_summit_num)
      messagebox.showinfo('information', "Village Summit has " + str(100 - village_summit_num) + "% occupacy left")

  elif((user_dining.lower() == "ohouse" or user_dining.lower() == "house" ) and weekday in ohouse_open):
      print(100 - o_house_num)
      messagebox.showinfo('information', "O House has " + str(100 - o_house_num) + "% occupacy left")

  elif(user_dining.lower() == "snelling" and weekday in snelling_open):
      print(100 - snelling_num)
      messagebox.showinfo('information', "Snelling has " + str(100 - snelling_num) + "% occupacy left")

  elif(user_dining.lower() == "niche" and weekday in niche_open):
      print(100 - niche_num)
      messagebox.showinfo('information', "Niche has " + str(100 - niche_num) + "% occupacy left")
  else:
      
      messagebox.showinfo('information', "Either this dining does not exists or it is closed today. Try Bolton or Village Summit")

def check_question(input):
   possible_dates = ["date", "today", "month", "day", "today's"]
   possible_bus = ["Central", "Loop", "East", "Campus", "Science", "Health"]
   possible_dining = ["Snelling", "Bolton", "OHouse" "House", "Village", "Summit", "Joe", "Frank", "Niche"]

   for i in input:
     if i in possible_dates:
       return "date"
     elif i in possible_bus:
       return i
     elif i in possible_dining:
       return i
  

def speak():
  recognizer = sr.Recognizer()
  print("Say something for 5 seconds:")
  with sr.Microphone() as source:
    #audio_data = recognizer.record(source, duration=5) # just made it five seconds here for testing. 
    print("Recognizing...")
    #text = recognizer.recognize_google(audio_data)
    text = "What is the dining occupancy at Bolton"
    print("Your Input:" , text)
   

    text_list = (text.split(' '))

    output = check_question(text_list)
    print(output)
    if output == "date":
      d2 = my_date.strftime("%B %d, %Y")
      messagebox.showinfo('information', d2)
    elif output == "Central":
      bus_occupancy("Central Loop")
    elif output == "East":
      bus_occupancy("East Campus")
    elif output == "Health":
      bus_occupancy("Health Science")
    else:
      dining_occupancy(output)

#gui.mainloop()
speak()
