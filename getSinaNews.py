# 获取新浪新闻列表
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
news = requests.get("http://news.sina.com.cn/china/")
news.encoding='utf8'
soup = BeautifulSoup(news.text,'html.parser')
for new in soup.select('.news-item')[0:10]:
    if len(new.select('h2')) > 0: 
        h2 = new.select('h2')
        a = h2[0].select('a')
        time = new.select('.time')
        # print(time[0].text,h2[0].text,a[0]['href'])
        print(a[0]['href'])
        newsURL = a[0]['href']
        newsDetail = requests.get(newsURL)
        newsDetail.encoding = 'utf-8'
        newsDetailSoup = BeautifulSoup(newsDetail.text,'html.parser')
        # 获取新闻标题
        newsTitle = newsDetailSoup.select('#artibodyTitle')[0].text
        print(newsTitle)
        # 获取新闻时间
        newsTime = newsDetailSoup.select('.time-source')[0].contents[0].strip()
        print(newsTime)
        # 获取新闻来源
        newsFrom = newsDetailSoup.select('.time-source span a')[0].text
        print(newsFrom)
        # 获取新闻内容
        newsContent = '\n'.join([p.text.strip() for p in newsDetailSoup.select(".article p")[:-1]])
        print(newsContent)
        # 获取新闻编辑者
        newsEditer = newsDetailSoup.select('.article-editor')[0].text.lstrip('责任编辑：')
        print(newsEditer)
        # 获取新闻评论数
        # 获取文章唯一编码值
        newsCode = newsURL.split('/')[-1].split('.')[0].split('-')[-1][1:]
        requestCommentsURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-'+newsCode+'&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
        newsComments = requests.get(requestCommentsURL)
        newsComments = json.loads(newsComments.text.strip("var data="))
        newsCommentCount = newsComments['result']['count']['total']
        print(newsCommentCount)
