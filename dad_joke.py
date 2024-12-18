
import requests

response = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php')
categories = response.json()
for category in categories["categories"]:
    print(category['strCategory'])



