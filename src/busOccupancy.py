import speech_recognition as sr
from datetime import date
from tkinter import *
from tkinter import messagebox
from urllib.request import urlopen
from datetime import date
from datetime import datetime
import requests
import calendar

CENTRAL_LOOP = 4918
EAST_CAMPUS = 4921
HEALTH_SCIENCE = 2611

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

if __name__ == "__main__":
    gui = Tk()
    gui.withdraw()
    bus_occupancy("Central Loop")