import requests

params = {"q": "pizza"}

r = requests.get('https://google.com/search', params)
print("Status:", r.status_code)

f = open('google.html', 'w+')
f.write(r.text)
f.close()
