import json
import turtle
import urllib.request

#web service url
url = "http://api.open-notify.org/astros.json"
#get info from web service
response = urllib.request.urlopen(url) 
#load info(json response) into Python data structure
#it returns HttpResponse, read method needed to turn that into bytes
result = json.loads(response.read())
print("Number of ppl currently in space: " + str(result['number']))
people = result['people']
for p in people:
    print(p['name'], "in", p['craft'])

url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
location = result['iss_position']
lon = location['longitude']
lat = location['latitude']
print(lat, lon)
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(float(lon), float(lat))


turtle.mainloop()
