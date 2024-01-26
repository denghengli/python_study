# _*_ coding : utf_8 _*_
# @Time : 2024/1/26 11:33
# @Author : dhl
# @File : 03_循环控制语句
# @Project : 代码

'''
一、for循环控制语句格式：
for 变量 in 要遍历的数据:
    方法体
'''

# 1、循环（遍历）字符串
print('\r\n遍历字符串')
# range(5)
# range(1,6)
# range(1,10,3)
s = 'china'
for i in s:
    print(i)

# range(5)的结果是 0~4 的对象
print("range(5)")
for i in range(5):
    print(i)
# range(1,5)的结果是 1~4 的对象, 表示 rang（起始值, 结束值）
print("range(1,5)")
for i in range(1,5):
    print(i)
# range(1,10,3)的结果是 1~10步长为3的对象, 表示 rang（起始值, 结束值， 步长）
print("range(1,10,3)")
for i in range(1,10,3):
    print(i)

# 2、循环（遍历）一个列表
# 应用场景：会爬取一个列表返回给我们
print('\r\n遍历列表')
# 直接变量列表中的元素
a_list = ['11', '22', '33']
for i in a_list:
    print(i)
# 通过下标遍历元素，len() 为获取列表中元素的个数
a_len = len(a_list)
print('列表中的元素个数=%d' % a_len)
for i in range(a_len):
    print(a_list[i])



