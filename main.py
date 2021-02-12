import requests
from tkinter import *
from keys import *
from urllib.request import urlopen
from PIL import Image, ImageTk
import urllib3
MOVIE = "Big Trouble in Little China"

parameters = {
    "apikey": API_KEY,
    "s": MOVIE
}

response = requests.get("http://www.omdbapi.com/", params=parameters)
response.raise_for_status()
poster_url = response.json()["Search"][0]["Poster"]
window = Tk()
window.title("moviestuff")
img = ImageTk.PhotoImage(Image.open(urlopen(poster_url)))
real_poster = Label(image=img)
real_poster.grid(row=0, column=0)

submit_button = Button(text="submit")


window.mainloop()