from urllib.request import urlopen
from bs4 import BeautifulSoup
 
url = 'http://www.weather.com.cn/weather/101200101.shtml'
bs = BeautifulSoup(urlopen(url),'lxml')
list = bs.findAll("li",{'class':{'sky skyid lv3 on','sky skyid lv3','sky skyid lv2','sky skyid lv1'}})
print('武汉天气:\n')
for i in list:
    print(i.get_text().replace('\n',' '))
