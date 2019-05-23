from bs4 import BeautifulSoup
html_sample = '<html><body>\
<h1>hello world!</h1>\
<a href="#" >我是一个链接</a>\
<a href="#" >我是另外一个链接</a>\
</body>\
</html>'
soup = BeautifulSoup(html_sample,"html.parser")
print(soup.text)

# 如果只取某个标签
h1Str = soup.select('h1')
print(h1Str)
print(h1Str[0])
print(h1Str[0].text)
aStr = soup.select('a')
print(aStr)
for alink in aStr :
    print(alink)
    print(alink.text)

# 获取a标签中的属性
ahtml = '<a href="https://www.baidu.com" class="testa" sss=1111>hello 中国</a>'
asoup = BeautifulSoup(ahtml,"html.parser")
print(asoup)
print(asoup.select('a')[0]['sss'])