import requests
from bs4 import BeautifulSoup
hotJokes = requests.get("https://www.qiushibaike.com/hot/page/1/")
hotJokes.encoding = 'utf-8'
hotJokerSoup = BeautifulSoup(hotJokes.text,'html.parser')
pageNum = hotJokerSoup.select('.page-numbers')[-1].text
print(pageNum)
for jokeDetail in hotJokerSoup.select('.article'):
    print(jokeDetail.select(".content span")[0].text)