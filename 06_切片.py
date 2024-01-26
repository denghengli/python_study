# _*_ coding : utf_8 _*_
# @Time : 2024/1/26 14:55
# @Author : dhl
# @File : 06_切片.py
# @Project : 代码

# 切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。
# 切片的语法：[起始:结束:步长]，也可以简化使用 [起始:结束]
# 注意：选取的区间从"起始"位开始，到"结束"位的前一位结束（不包含结束位本身)，步长表示选取间隔。

s = 'hello world'
print(s[0:3])
print(s[0:6:2])

list = ['dsa', 'dd', 'fff']
print(list[0:2])

a_tuple = (1,2,3)
print(a_tuple[0:2])


