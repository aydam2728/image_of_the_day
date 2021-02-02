import urllib.request
import json
import webbrowser
import ctypes

apodurl= "https://api.nasa.gov/planetary/apod?"
mykey='api_key=your api key here'

apodurlobj=urllib.request.urlopen(apodurl+mykey)

apodread=apodurlobj.read()
decodeapod=json.loads(apodread.decode("utf-8"))


urllib.request.urlretrieve(decodeapod["hdurl"],"your directory here\\%s.jpg"%(decodeapod["title"]))
ctypes.windll.user32.SystemParametersInfoW(20, 0, "your directory here\\%s.jpg" %(decodeapod["title"]), 0)
