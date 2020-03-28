from requests import get, post

print(get('http://localhost:5000/api/news').json())

print(get('http://localhost:5000/api/news/1').json())

print(get('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

print(get('http://localhost:5000/api/v2/news', json={'title': 'News2'}).json() )

print(post('http://localhost:5000/api/news').json())
print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок'}).json())


