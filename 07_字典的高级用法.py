# _*_ coding : utf_8 _*_
# @Time : 2024/1/26 15:34
# @Author : dhl
# @File : 07_字典的高级用法
# @Project : 代码

person = {'name':'dhl','age': 28}

# 1、查看元素
# (1)使用 [key] 方法来获取
# 这种方式获取字典中不存在的key时会发生异常，报错keyerror
print(person)
print(person['name'])
print(person['age'])
# print(person['sex']) #会报错

# (2)使用 .get(key) 方法来获取数据
# 使用这种方式获取字典中不存在的key时，会返回None值，不会插入新的数据！！！
print(person.get('name'))
print(person.get('age'))
print(person.get('sex'))
print(person)

# 2、修改字典
# 字典的每个元素中的数据是可以修改的，只要通过key找到，即可修改
person['name'] = 'ddd'
print(person.get('name'))

# 3、添加元素
# 如果在使用 变量名['键'] = 数据 时，这个“键”在字典中，不存在，那么就会新增这个元素
person['sex'] = '男'
print(person)

# 4、删除元素
# 对字典进行删除操作，有一下几种：
# del
#   （1）删除指定的元素
#   （2）删除整个字典,删完后字典不可再用，字典的结构也一并被删除了
# clear() 清空整个字典，指的是将字典中所有的数据都删除掉，而保留字典的结构
del person['age']
print(person)

# del person
# print(person)

# person.clear()
# print(person)

# 5、字典遍历
# （1）遍历字典的key（键）
for key in person.keys():
    print(key)
# （2）遍历字典的value（值）
for value in person.values():
    print(value)
# （3）遍历字典的项（元素）
for item in person.items():
    print(item)
# （4）遍历字典的key-value（键值对）
for key,value in person.items():
    print('key=%s,value=%s' % (key,value))






