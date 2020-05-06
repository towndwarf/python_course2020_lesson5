import requests as rq
r = rq.get('https://api.github.com/events')
print('EVENTS:', r.content)
r = rq.post('https://httpbin.org/post', data = {'key':'value'})
r = rq.put('https://httpbin.org/put', data = {'key':'value'})
print('PUT:', r)
r = rq.delete('https://httpbin.org/delete')
print('DELETE:', r)
r = rq.head('https://httpbin.org/get')
print('HEAD:', r.content)
r = rq.options('https://httpbin.org/get')

payload = {'key1': 'value1', 'key2': 'value2'}
r = rq.get('https://httpbin.org/get', params=payload)
print(r.url)

r = rq.get('https://api.github.com/events')
print(r.text)
print(r.json())