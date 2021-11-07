import urllib, json

url = "https://swapi.dev/api/films/"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print (data)