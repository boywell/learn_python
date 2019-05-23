# 获取纯洁的微笑文章列表
import requests
from bs4 import BeautifulSoup
articles = requests.get("https://mp.weixin.qq.com/s?__biz=MzI4NDY5Mjc1Mg==&mid=100000548&idx=1&sn=774cf4802575f58a1e215adae334af2a&chksm=6bf6db5b5c81524db8ae90c622bd5aa07b865f97c2e5c3ade8d5c7fef4379a8876527da1d1d6&scene=18#wechat_redirect")
articles.encoding = "utf-8"
soap = BeautifulSoup(articles.text,'html.parser')
print(articles.text)
# for artul in soap.select('.list-paddingleft-2')[0:1]:
#     print(artul)
