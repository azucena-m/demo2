import requests

response = requests.get('http://api.open-notify.org/astros.json')
people = response.json()


print('The pople currently in space are:')
for p in people['people']:
    print(p['name'])