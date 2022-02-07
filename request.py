import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Income':50000, 'Age':30})

print(r.json())