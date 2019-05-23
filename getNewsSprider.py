import requests
res = requests.get('http://news.163.com/')
print(res.encoding)