import random as r
import requests
import math as m
import time as t
import numpy
import datetime as dt

def URL_post(wheel, distance, speed):
    x = t.time()

    y = x / 3600

    z = m.floor(y)

    v = z * 3600 - 1

    url = "http://www.hackminster.co.uk/URLpost.php"

    myobj = {'datetime': v,'distance': distance, 'wheel': wheel, 'speed': speed}

    x = requests.post(url, data = myobj)

    print(x.text)

def randomDist():
    a = r.randint(1,4)

    if a == 1:
        b = r.randint(10,30)
    else:
        b = 0
        
    return b

distProfile = (0,0,0,80,50,0,0,0,0,0,0,0,0,0,0,0,0,0,50,100,80,100,0,0)


step = 3600 # time step in seconds

x = t.time() / step

y = m.ceil(x) * step

# speed normal distribution parameters:
mean = 3.5  # mean speed (m/s)
sigma = 1   # standard deviation (m/s)

while 1:
    
    if (t.time() > y):
        
        y = y + step

        for x in range(20):
            
            wheel = x + 101
            
            distance = randomDist() + distProfile[dt.datetime.now().hour] * r.randint(5,10)/10

            s = numpy.random.normal(mean,sigma,1)
            
            speed = '%.3f' % s[0]
            
            print("Wheel: ", wheel, " Distance: ", distance, " Speed: ", speed)

            try:
                URL_post(wheel, distance, speed)
            except:
                print("URL post error, wheel: ", wheel)
            
        
