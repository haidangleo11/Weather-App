from tkinter import *
from geopy.geocoders import Nominatim
from tkintermapview import TkinterMapView
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests, pytz

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="abcd")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result) 

        timezonez.config(text=home)

        
        lnglat.config(text=f"{round(location.latitude, 4)}°, {round(location.longitude, 4)}°")
        name.config(text="CURRENT WEATHER")
        code = "a0f0adeafb53c3f3217338a506f7fd43"
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={code}"
        
        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        pressure = json_data["main"]["pressure"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)
        humidity = json_data["main"]["humidity"]
        wind = round(json_data["wind"]["speed"], 2)
        hightemp = json_data["main"]["temp_max"]
        lowtemp = json_data["main"]["temp_min"]
        visibility_ = json_data["visibility"]
        winddeg = json_data["wind"]["deg"]
        sunrise = datetime.utcfromtimestamp(json_data["sys"]["sunrise"] + json_data["timezone"])
        sunset = datetime.utcfromtimestamp(json_data["sys"]["sunset"] + json_data["timezone"])

        t.config(text=(f"{temp}°C"))
        c.config(text=(condition, "|", "FEELS", "LIKE", f"{temp}°C"))
        visibility.config(text=f"Visibility: {visibility_}m         Wind Degree: {winddeg}°")
        
        if (len(description) > 15):
            d.place(x=380, y=425)
            d.config(text=description)
        if (len(description) == 15):
            d.place(x=400, y=425)
            d.config(text=description)
        if (10 > len(description) < 15):
            d.place(x=415, y=425)
            d.config(text=description)
        if (len(description) == 10): 
            d.place(x=430, y=425)
            d.config(text=description)
        if (6 >= len(description) <= 9):
            d.place(x=420, y=425)
            d.config(text=description)
        if (len(description) == 5):
            d.place(x=440, y=425)
            d.config(text=description)
        if (len(description) <= 4):
            d.place(x=470, y=425)
            d.config(text=description)
        if (description == "broken clouds"):
            icon_for_temp.config(image=d4)
            d.place(x=410, y=425)
            d.config(text=description)
        if (description == "scattered clouds"):
            icon_for_temp.config(image=d3)
            d.place(x=400, y=425)
            d.config(text=description)
        if (description == "few clouds"):
            icon_for_temp.config(image=d2)
        if (description == "overcast clouds"):
            icon_for_temp.config(image=d4)
        if (description == "clear sky"):
            icon_for_temp.config(image=d1)
            d.place(x=440, y=425)
            d.config(text=description)
        if (description == "thunderstorm with rain"):
            d.place(x=360, y=425)
            d.config(text=description)
        if (description == "moderate rain"):
            d.place(x=410, y=425)
            d.config(text=description)
        if description == "light rain":
            d.place(x=439, y=425)
            d.config(text=description)
        if (description == "light shower intensity"):
            d.place(x=280, y=425)
            d.config(text=description)
        if (description == "light rain" or description == "moderate rain" or description == "heavy intensity rain" or
            description == "very heavy rain" or description == "extreme rain"): icon_for_temp.config(image=d10)
        if (description == "freezing rain"): icon_for_temp.config(image=d13)
        if (description == "light intensity shower rain" or description == "shower rain" or 
            description == "heavy intensity shower rain" or description == "ragged shower rain"): icon_for_temp.config(image=d9)
        if (description == "mist" or description == "smoke" or description == "haze" or description == "sand/dust whirls" or description == "fog" or
            description == "tornado" or description == "squalls" or description == "volcano ash" or description == "dust" or description == "sand"):
            icon_for_temp.config(image=d50)
        if ("snow" in description or "sleet" in description):
            icon_for_temp.config(image=d13)
        if ("drizzle" in description):
            icon_for_temp.config(image=d9)
        if ("thunderstorm" in description):
            icon_for_temp.config(image=d11)
        
        w.config(text=round(wind, 2))
        h.config(text=f"{humidity}")
        p.config(text=pressure)
        chigh = round((hightemp - 273.15), 2)
        clow = round((lowtemp - 273.15), 2)
        high.config(text=f"Highest Temperature: {chigh}°C or {round((round(chigh, 2) * 1.8 + 32), 2)}°F or {round(hightemp, 2)}°K")
        low.config(text=f"Lowest Temperature: {clow}°C or {round((round(clow, 2) * 1.8 + 32), 2)}°F or {round(lowtemp, 2)}°K")
        rise.config(text=f"Sunrise: {sunrise} in local time")
        sset.config(text=f"Sunset: {sunset} in local time")

        current = datetime.now(home)
        real = current.strftime("%d/%m/%Y\n%H:%M %p")
        clock.config(text=real)
        clock.after(1000, getWeather)

    except Exception:
        messagebox.showerror("Weather App", "Check your internet connection!\nCheck the name of your city/country\nOr try to run the program again.")

root = Tk()
root.title("Weather App")
root.geometry("910x500") 
root.resizable(0, 0)
root.config(bg="#82d0e8")
icon = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\images\\logo.png")
root.iconphoto(False, icon)

search_img = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\images\\Rounded Rectangle 3.png")
my_img = Label(image=search_img, bg="#82d0e8")
my_img.place(x=40, y=20)

textfield = Entry(root, justify=CENTER, width=17, font=("poppins", 25, "bold"), bg="#203243", border=0, fg="white")
textfield.place(x=110, y=30)
textfield.focus()

search_ico = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\images\\Layer 6.png")
myimg_ico = Button(image=search_ico, bd=0, cursor="hand2", bg="#203243", command=getWeather)
myimg_ico.place(x=417, y=24)

Label(image=icon, bg="#82d0e8").place(x=150, y=100)

lgfr = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\Copy of Box.png")
frame = Label(image=lgfr, bg="#82d0e8")
frame.place(x=55, y=380)

Label(root, text="WIND:", font="Helvetica 15 bold", fg="white", bg="#1ab5ef").place(x=120, y=400)
Label(root, text="HUMIDITY:", font="Helvetica 15 bold", fg="white", bg="#1ab5ef").place(x=245, y=400) # add 20
Label(root, text="DESCRIPTION:", font="Helvetica 15 bold", fg="white", bg="#1ab5ef").place(x=430, y=400)
Label(root, text="PRESSURE:", font="Helvetica 15 bold", fg="white", bg="#1ab5ef").place(x=650, y=400)

t = Label(font="arial 70 bold", fg="#ee666d", bg="#82d0e8")
t.place(x=400, y=110)
c = Label(font="arial 15 bold", bg="#82d0e8")
c.place(x=400, y=210)

w = Label(text="......", font="arial 20 bold", bg="#1ab5ef")
w.place(x=120, y=425)
h = Label(text=".....", font="arial 20 bold", bg="#1ab5ef")
h.place(x=269, y=425)
d = Label(text=".......", font="arial 20 bold", bg="#1ab5ef")
d.place(x=470, y=425)
p = Label(text=".......", font="arial 20 bold", bg="#1ab5ef")
p.place(x=675, y=425)

high = Label(font="arial 10 bold", bg="#82d0e8")
high.place(x=400, y=240)
low = Label(font="arial 10 bold", bg="#82d0e8")
low.place(x=400, y=260)
rise = Label(font="arial 10 bold", bg="#82d0e8")
rise.place(x=400, y=280)
sset = Label(font="arial 10 bold", bg="#82d0e8")
sset.place(x=400, y=300)

under = Label(root, text="km/h                              %                                                                                                     hPa",
              font="arial 10", bg="#1ab5ef").place(x=130, y=455)

name = Label(root, font="arial 15 bold", bg="#82d0e8")
name.place(x=30, y=100)
clock = Label(root, font="helvetica 20", bg="#82d0e8")
clock.place(x=30, y=130)

d1 = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\icon\\01d@2x.png")
d2 = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\icon\\02d@2x.png")
d3 = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\icon\\03d@2x.png")
d4 = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\icon\\04d@2x.png")
d9 = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\icon\\09d@2x.png")
d10 = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\icon\\10d@2x.png")
d11 = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\icon\\11d@2x.png")
d13 = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\icon\\13d@2x.png")
d50 = PhotoImage(file="C:\\Users\\Nguyen Hai Dang\\PycharmProjects\\Tkinter\\Tkinter\\Weather App\\icon\\50d@2x.png")
icon_for_temp = Label(bg="#82d0e8")
icon_for_temp.place(x=740, y=3)

timezonez = Label(root, font="arial 12", bg="#82d0e8")
timezonez.place(x=500, y=30)

visibility = Label(root, font="arial 25", bg="#82d0e8")
visibility.place(x=120, y=500)

lnglat = Label(root, font="arial 14", bg="#82d0e8")
lnglat.place(x=500, y=60)

root.mainloop()