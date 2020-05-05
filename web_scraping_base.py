import requests
r = requests.get('https://api.github.com/events')
print('EVENTS:', r.content)
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
r = requests.put('https://httpbin.org/put', data = {'key':'value'})
print('PUT:', r)
r = requests.delete('https://httpbin.org/delete')
print('DELETE:', r)
r = requests.head('https://httpbin.org/get')
print('HEAD:', r.content)
r = requests.options('https://httpbin.org/get')

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)

r = requests.get('https://api.github.com/events')
print(r.text)
print(r.json())