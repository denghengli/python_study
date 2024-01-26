# _*_ coding : utf_8 _*_
# @Time : 2024/1/26 13:22
# @Author : dhl
# @File : 04_字符串的高级用法
# @Project : 代码

# 字符串的常见操作包括：
# 获取长度:len len函数可以获取字符串的长度。
# 查找内容:find 查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第一次出现的开始位置索引值，如果不存在，则返回-1.
# 判断:startswith,endswith 判断字符串是不是以谁谁谁开头/结尾, 返回 True False
# 计算出现次数:count 返回 str在start和end之间 在 mystr里面出现的次数
# 替换内容:replace 替换字符串中指定的内容，如果指定次数count，则替换不会超过count次。返回替换后的新字符串
# 切割字符串:split 通过参数的内容切割字符串
# 修改大小写:upper,lower 将字符串中的大小写互换
# 空格处理:strip 去空格
# 字符串拼接:join 字符串拼接

print('字符串高级用法：len')
s = 'china'
print(len(s))

print('字符串高级用法：find')
print(s.find('a'))

print('字符串高级用法：startswith endswith')
print(s.startswith('c'))
print(s.endswith('a'))

print('字符串高级用法：count')
s1 = 'qqqqqq'
print(s1.count('q'))

print('字符串高级用法：replace')
print(s1.replace('q', 'w'))

print('字符串高级用法：split')
s2='1#2#3#4'
print(s2.split('#'))

print('字符串高级用法：upper')
print(s.upper())

print('字符串高级用法：strip')
s3 = '  fds  '
print(s3.split())

print('字符串高级用法：join')
print(s.join('a'))


