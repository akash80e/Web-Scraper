import requests
URL = "http://geeksforgeeks.org/data-structures/"
r = requests.get(URL)
print(r.content)