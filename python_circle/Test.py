# -*- coding:utf-8 -*-
add = 3+4
print('3+4 = {}'.format(add))

# 除法 和整除
div = 7/2
print('7/2 = {}',format(div))

round_div = 7//2
print('7//2 = {}'.format(round_div))

# 字符串操作
welcome = 'Welcome to China'
# 首字母大写
print(welcome.title())
# 转小写
print(welcome.lower())
# 转大写
print(welcome.upper())
# 大写转小写，小写转大写
print(welcome.swapcase())
# 是否全是数字\英文,因为有空格，所以也是false
print(welcome.isalnum())
# 是否全是整数
print(welcome.isdigit())

# 按照行分隔
print('1+2\n+3+4'.splitlines())

world = ' nd '
# 清空两端的空格
print(world.strip())
# 清除左侧的空格
print(world.lstrip())
# 清除右侧的空格
print(world.rstrip())


# slice 分片
print(welcome[0:2])
print(welcome[:])
print(welcome[::2])

print(type(world))
print(type(1))
print(type(1.1))

# 转换为字符串
print(str(1.1))