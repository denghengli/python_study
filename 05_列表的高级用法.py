# _*_ coding : utf_8 _*_
# @Time : 2024/1/26 13:41
# @Author : dhl
# @File : 05_列表的高级用法
# @Project : 代码

# 一、列表添加元素
# 添加元素有一下几个方法:
# append 在末尾添加元素
# insert 在指定位置插入元素
# extend 合并两个列表

print('列表元素操作 - append 在末尾添加元素')
list = ['111', '222', '333']
list.append('444')
print(list)

print('列表元素操作 - insert 在指定位置插入元素')
list.insert(1, 'qq')
print(list)

print('列表元素操作 - extend 合并两个列表')
list1 = ['dsaf']
list.extend(list1)
print(list)

# 二、列表修改元素
# 我们是通过指定下标来访问列表元素，因此修改元素的时候，为指定的列表下标赋值即可
city_list = ['北京', '上海', '武汉']
city_list[0] = '北京修改'
print(city_list)


# 三、列表查找元素
# 所谓的查找，就是看看指定的元素是否存在，主要包含一下几个方法
# in 和 not in
# in（存在）,如果存在那么结果为true，否则为false
# not in（不存在），如果不存在那么结果为true，否则false
city_list = ['北京', '上海', '武汉']
# city = input("请输入城市：")
city = '北京'
if city in city_list:
    print('在列表中')
else:
    print('不在列表中')


# 四、列表删除元素
# 类比现实生活中，如果某位同学调班了，那么就应该把这个条走后的学生的姓名删除掉；在开发中经常会用到删除这种功能。
# 列表元素的常用删除方法有：
# del：根据下标进行删除
# pop：删除最后一个元素
# remove：根据元素的值进行删除
movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']
print('‐‐‐‐‐‐删除之前‐‐‐‐‐‐movieName=%s' % movieName)
# del movieName[1]
movieName.__delitem__(1)
print('‐‐‐‐‐‐del删除之后‐‐‐‐‐‐movieName=%s' % movieName)
movieName.pop()
print('‐‐‐‐‐‐pop删除之后‐‐‐‐‐‐movieName=%s' % movieName)
movieName.remove('指环王')
print('‐‐‐‐‐‐remove删除之后‐‐‐‐‐‐movieName=%s' % movieName)

