import random as r
import requests
import math as m
import time as t

def URL_post(wheel, distance, speed):
    x = t.time()

    y = x / 3600

    z = m.floor(y)

    v = z * 3600 - 1

    url = "http://www.hackminster.co.uk/URLpost.php"

    myobj = {'datetime': v,'distance': distance, 'wheel': wheel, 'speed': speed}

    x = requests.post(url, data = myobj)

    print(x.text)
    
step = 3600 # time step in seconds

x = t.time() / step

y = m.ceil(x) * step

while 1:
    
    if (t.time() > y):
        
        y = y + step

        for x in range(20):
            
            wheel = x + 101
            
            distance = r.randint(0,100)
            
            speed = r.randint(200,600)/100
            
            print("Wheel: ", wheel, " Distance: ", distance, " Speed: ", speed)

            try:
                URL_post(wheel, distance, speed)
            except:
                print("URL post error, wheel: ", wheel)
            
        
