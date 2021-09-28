import urllib.request
import json
import ctypes
import re
import os
import random


apodurl= "https://api.nasa.gov/planetary/apod?"
mykey='api_key='

def wallpaper(image):
    global path
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "%s\\NASA\\PicOfTheDay\\%s" %(path,image), 0)


apodurlobj=urllib.request.urlopen(apodurl+mykey)

apodread=apodurlobj.read()

decodeapod=json.loads(apodread.decode("utf-8"))

path="B:\\Pictures"
decodeapod["title"]=re.sub('[!@#$_,.;:]', '', decodeapod["title"])

if "hdurl" in decodeapod :
    urllib.request.urlretrieve(decodeapod["hdurl"],"%s\\NASA\\PicOfTheDay\\%s"%(path,decodeapod["title"]+".jpg"))
    wallpaper(decodeapod["title"]+".jpg")

else:
    list=[x for x in os.listdir('.') if x.endswith('.jpg')]
    image_random=list[random.randint(0,len(list)-1)]
    wallpaper(image_random)
    
