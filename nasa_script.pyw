import urllib.request
import json
import ctypes
import re

apodurl= "https://api.nasa.gov/planetary/apod?"
mykey='api_key=' #your api key here

apodurlobj=urllib.request.urlopen(apodurl+mykey)

apodread=apodurlobj.read()

decodeapod=json.loads(apodread.decode("utf-8"))

path="" #the path of the files here
decodeapod["title"]=re.sub('[!@#$_,.;:]', '', decodeapod["title"])

if "hdurl" in decodeapod :
	urllib.request.urlretrieve(decodeapod["hdurl"],"%s\\NASA\\PicOfTheDay\\%s.jpg"%(path,decodeapod["title"]))
	ctypes.windll.user32.SystemParametersInfoW(20, 0, "%s\\NASA\\PicOfTheDay\\%s.jpg" %(path,decodeapod["title"]), 0)
else:
    print("error")
