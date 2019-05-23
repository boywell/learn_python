# -*- coding:utf-8 -*-

# 列表
person = ['钢铁侠','蜘蛛侠','奇异博士','绿巨人','美国队长','黑寡妇']
print(type(person))
# 列表长度
print(len(person))
print(person[1])
# 获取最后一个元素
print(person[-1])
print(person[len(person)-1])

# 指定位置插入 insert(index,x)
person.insert(1,10)
print(person)

# 末尾添加就是append
person.append("程度")
print(person)

# 修改值
person[-1]='你好'
print(person)

# 删除 pop() 删除尾部元素，并返回删除元素
deleteValue = person.pop()
print(deleteValue)
