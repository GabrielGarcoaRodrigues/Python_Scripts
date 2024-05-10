import requests

# http -> 80
# https -> 443
url = 'https://www.google.com.br'

response = requests.get(url)

print(response.status_code)
# print(response.text)
# print(response.headers)
print(response.request.headers)
print(response.request.method)
print(response.request.url)