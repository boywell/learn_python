print("tangxy")
print("good luky")
a = "www.baidu.com"
print(a.split("."))
print(a.replace("a","b"))
# strip 替换两端空格或者指定替换内容
b = ' python is best   '
print(b.strip())
# format
c = "{} is best ".format("java")
print(c)
phoneNum = '13000066666'
print(phoneNum.replace(phoneNum[3:7],'*'*4))

def hello():
    if 1 >2 :
        print("false")
    else:
        print("true")
print(hello())            
list = ["tom" ,"jerry","jei"]
print(list[0])