from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk

root=Tk()
root.title("weather forecasting")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False,False)


def getweather():
    city=textfield.get()

    geoloacator=Nominatim(user_agent="geoapiExercises")
    location=geoloacator.geocode(city)
    obj=TimezoneFinder()

    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)} °N,{round(location.longitude,4)} °E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)

    #weather
    api="https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=93b0867ddd75fb0f5bec5a8418a1150c"
    # response=requests.get(api)
    # print(response.status_code)
    json_data=requests.get(api).json()
    print(json_data)

    # #current
    temp=json_data["main"]["temp"]
    humidity=json_data['main']['humidity']
    pressure=json_data['main']['pressure']
    wind=json_data['wind']['speed']
    description=json_data['weather'][0]['description']

    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)

    api2="https://api.openweathermap.org/data/2.5/forecast?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=93b0867ddd75fb0f5bec5a8418a1150c"
    json_data2=requests.get(api2).json()
    #print(json_data2)

    # #FIRST CELL
    firstdayimage=json_data2['list'][0]['weather'][0]['icon']
    photo1=ImageTk.PhotoImage(file=f"weather icons/{firstdayimage}@2x.png")
    Firstimage.config(image=photo1)
    Firstimage.image=photo1

    day1temp.config(text=str(json_data2['list'][0]['main']['temp'])+"°C")

    
    
    
    # #second cell
    day2temp.config(text=str(json_data2['list'][1]['main']['temp'])+"°C")
    day2H.config(text=str(json_data2['list'][1]['main']['humidity'])+"%")
    day2W.config(text=str(json_data2['list'][1]['wind']['speed'])+"m/s")
    day2D.config(text=str(json_data2['list'][1]['weather'][0]['main']))
    
    # #third cell
    day3temp.config(text=str(json_data2['list'][2]['main']['temp'])+"°C")
    day3H.config(text=str(json_data2['list'][2]['main']['humidity'])+"%")
    day3W.config(text=str(json_data2['list'][2]['wind']['speed'])+"m/s")
    day3D.config(text=str(json_data2['list'][2]['weather'][0]['main']))
    
    # #fourth cell
    day4temp.config(text=str(json_data2['list'][3]['main']['temp'])+"°C")
    day4H.config(text=str(json_data2['list'][3]['main']['humidity'])+"%")
    day4W.config(text=str(json_data2['list'][3]['wind']['speed'])+"m/s")
    day4D.config(text=str(json_data2['list'][3]['weather'][0]['main']))
    
    # #fifth cell
    day5temp.config(text=str(json_data2['list'][4]['main']['temp'])+"°C")
    day5H.config(text=str(json_data2['list'][4]['main']['humidity'])+"%")
    day5W.config(text=str(json_data2['list'][4]['wind']['speed'])+"m/s")
    day5D.config(text=str(json_data2['list'][4]['weather'][0]['main']))
    
    # #sixth cell
    day6temp.config(text=str(json_data2['list'][5]['main']['temp'])+"°C")
    day6H.config(text=str(json_data2['list'][5]['main']['humidity'])+"%")
    day6W.config(text=str(json_data2['list'][5]['wind']['speed'])+"m/s")
    day6D.config(text=str(json_data2['list'][5]['weather'][0]['main']))
    
    # #seventh cell
    day7temp.config(text=f"{(json_data2['list'][6]['main']['temp'])}"+"°C")
    day7H.config(text=str(json_data2['list'][6]['main']['humidity'])+"%")
    day7W.config(text=str(json_data2['list'][6]['wind']['speed'])+"m/s")
    day7D.config(text=str(json_data2['list'][6]['weather'][0]['main']))


    #days getting printed on the bottom boxes
    first=datetime.now()
    day1.config(text=first.strftime("%A"))

    second= first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third= first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth= first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth= first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth= first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))
    
    seventh= first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))
    
    
image_icon=PhotoImage(file="bigger icons and backgrounds/logo.png")
root.iconphoto(False,image_icon)

round_box=PhotoImage(file="bigger icons and backgrounds/Rounded Rectangle 1.png")
Label(root,image=round_box,bg="#57adff").place(x=30,y=110)

#Label
label1=Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=50,y=160)

label4=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=50,y=180)

label5=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="#203243")
label5.place(x=50,y=200)




#search Box
Search_box=PhotoImage(file="bigger icons and backgrounds/Rounded Rectangle 3.png")
myimage=Label(image=Search_box,bg="#57adff")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="bigger icons and backgrounds/Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)


search_icon=PhotoImage(file="bigger icons and backgrounds/Layer 6.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getweather)
myimage_icon.place(x=645,y=125)





#Bottom layer
frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox=PhotoImage(file="bigger icons and backgrounds/Rounded Rectangle 2.png")
secondbox=PhotoImage(file="bigger icons and backgrounds/Rounded Rectangle 2 copy.png")


Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=30)





#clock (here we will place time)
clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)








#putting the values of current weather in the rounded box in their respective title
t=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t.place(x=150,y=120) 

h=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=150,y=140)

p=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=150,y=160)

w=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=150,y=180)

d=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=150,y=200)






#first cell(big one)
firstframe=Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=35,y=315)

day1=Label(firstframe,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=108,y=5)

Firstimage=Label(firstframe,bg="#282829")
Firstimage.place(x=7,y=20)

day1temp=Label(firstframe,bg="#282829",fg="#57adff",font="arial 15 bold")
day1temp.place(x=100,y=50)



#second cell
secondframe=Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=305,y=325)

day2=Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=10,y=5)

# secondimage=Label(secondframe,bg="#282829")
# secondimage.place(x=7,y=20)

day2temp=Label(secondframe,bg="#282829",fg="#57adff",font="roboto 8")
day2temp.place(x=10,y=25)

day2H=Label(secondframe,bg="#282829",fg="#57adff",font="roboto 8")
day2H.place(x=10,y=45)

day2W=Label(secondframe,bg="#282829",fg="#57adff",font="roboto 8")
day2W.place(x=10,y=65)

day2D=Label(secondframe,bg="#282829",fg="#57adff",font="roboto 8")
day2D.place(x=10,y=85)





#third cell
thirdframe=Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=405,y=325)


day3=Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=10,y=5)

day3temp=Label(thirdframe,bg="#282829",fg="#57adff",font="roboto 8")
day3temp.place(x=10,y=25)

day3H=Label(thirdframe,bg="#282829",fg="#57adff",font="roboto 8")
day3H.place(x=10,y=45)

day3W=Label(thirdframe,bg="#282829",fg="#57adff",font="roboto 8")
day3W.place(x=10,y=65)

day3D=Label(thirdframe,bg="#282829",fg="#57adff",font="roboto 8")
day3D.place(x=10,y=85)



#fourth cell
fourthframe=Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=505,y=325)

day4=Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=10,y=5)

day4temp=Label(fourthframe,bg="#282829",fg="#57adff",font="roboto 8")
day4temp.place(x=10,y=25)

day4H=Label(fourthframe,bg="#282829",fg="#57adff",font="roboto 8")
day4H.place(x=10,y=45)

day4W=Label(fourthframe,bg="#282829",fg="#57adff",font="roboto 8")
day4W.place(x=10,y=65)

day4D=Label(fourthframe,bg="#282829",fg="#57adff",font="roboto 8")
day4D.place(x=10,y=85)


#fifth cell
fifthframe=Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=605,y=325)

day5=Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=1,y=5)

day5temp=Label(fifthframe,bg="#282829",fg="#57adff",font="roboto 8")
day5temp.place(x=10,y=25)

day5H=Label(fifthframe,bg="#282829",fg="#57adff",font="roboto 8")
day5H.place(x=10,y=45)

day5W=Label(fifthframe,bg="#282829",fg="#57adff",font="roboto 8")
day5W.place(x=10,y=65)

day5D=Label(fifthframe,bg="#282829",fg="#57adff",font="roboto 8")
day5D.place(x=10,y=85)



#sixth cell
sixthframe=Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=705,y=325)

day6=Label(sixthframe,bg="#282829",fg="#fff")
day6.place(x=10,y=5)

day6temp=Label(sixthframe,bg="#282829",fg="#57adff",font="roboto 8")
day6temp.place(x=10,y=25)

day6H=Label(sixthframe,bg="#282829",fg="#57adff",font="roboto 8")
day6H.place(x=10,y=45)

day6W=Label(sixthframe,bg="#282829",fg="#57adff",font="roboto 8")
day6W.place(x=10,y=65)

day6D=Label(sixthframe,bg="#282829",fg="#57adff",font="roboto 8")
day6D.place(x=10,y=85)

#seventh cell
seventhframe=Frame(root,width=70,height=115,bg="#282829")
seventhframe.place(x=805,y=325)

day7=Label(seventhframe,bg="#282829",fg="#fff")
day7.place(x=10,y=5)

day7temp=Label(seventhframe,bg="#282829",fg="#57adff",font="roboto 8")
day7temp.place(x=10,y=25)

day7H=Label(seventhframe,bg="#282829",fg="#57adff",font="roboto 8")
day7H.place(x=10,y=45)

day7W=Label(seventhframe,bg="#282829",fg="#57adff",font="roboto 8")
day7W.place(x=10,y=65)

day7D=Label(seventhframe,bg="#282829",fg="#57adff",font="roboto 8")
day7D.place(x=10,y=85)

root.mainloop()