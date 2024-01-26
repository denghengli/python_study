# _*_ coding : utf_8 _*_
# @Time : 2024/1/26 11:13
# @Author : dhl
# @File : 02_条件控制语句
# @Project : 代码

# if关键字的语句结构
# if 判断条件:
#     代码

ageStr = input("请输入你的年龄:")
age = int(ageStr)
if age > 20:
    print('你的年龄（%d）大于20' % age)
elif age == 20:
    print('你的年龄（%d）等于20' % age)
else:
    print('你的年龄（%d）小于20' % age)



