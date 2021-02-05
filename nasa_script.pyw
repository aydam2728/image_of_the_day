import urllib.request
import json
import webbrowser
import ctypes

apodurl= "https://api.nasa.gov/planetary/apod?"
mykey='api_key=dHBo0AWnNFt27udgQo1o5dk6ewzBkDna6SmNMhv0'

apodurlobj=urllib.request.urlopen(apodurl+mykey)

apodread=apodurlobj.read()

decodeapod=json.loads(apodread.decode("utf-8"))

if "hdurl" in decodeapod :
	urllib.request.urlretrieve(decodeapod["hdurl"],"C:\\Users\\lesdm\\Pictures\\NASA\\PicOfTheDay\\%s.jpg"%(decodeapod["title"]))
	ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\lesdm\\Pictures\\NASA\\PicOfTheDay\\%s.jpg" %(decodeapod["title"]), 0)

