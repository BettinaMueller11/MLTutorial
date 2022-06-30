import requests

url = 'https://www.metaweather.com/api/location/search/?query=(query)'
params = {'query': 'berlin'}
response = request.get(url, params)

print(response)
