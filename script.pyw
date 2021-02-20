import urllib.request
import json
import ctypes
import re

apodurl= "https://api.nasa.gov/planetary/apod?"
mykey='api_key=dHBo0AWnNFt27udgQo1o5dk6ewzBkDna6SmNMhv0'

apodurlobj=urllib.request.urlopen(apodurl+mykey)

apodread=apodurlobj.read()

decodeapod=json.loads(apodread.decode("utf-8"))

path="C:\\Users\\lesdm\\Pictures"
decodeapod["title"]=re.sub('[!@#$_,.;:]', '', decodeapod["title"])

if "hdurl" in decodeapod :
	urllib.request.urlretrieve(decodeapod["hdurl"],"%s\\NASA\\PicOfTheDay\\%s.jpg"%(path,decodeapod["title"]))
	ctypes.windll.user32.SystemParametersInfoW(20, 0, "%s\\NASA\\PicOfTheDay\\%s.jpg" %(path,decodeapod["title"]), 0)
else:
    print("error")

