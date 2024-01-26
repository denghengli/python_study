# _*_ coding : utf_8 _*_
# @Time : 2024/1/26 16:26
# @Author : dhl
# @File : 08_函数
# @Project : 代码

# 1、函数定义，格式如下
# def 函数名():
#     代码
def f1():
    print('111111')
    print('222222')
    print('333333')

# 2、函数调用
# 定义了函数之后，就相当于有了一个具有某些功能的代码，想要让这些代码能够执行，需要调用它
# 调用函数很简单的，通过 函数名() 即可完成调用
f1()

# 3、函数参数
def f2(a,b):
    print('a=%d,b=%d,sum=%d' % (a,b,a+b))
def f3(a,b):
    c = 0
    for i in range(a,b):
        c += i
    print('a=%d,b=%d,sum=%d' % (a,b,c))

f2(1,2)
f3(1,10)

# 4、函数返回值
def f4(a,b):
    return a+b

c = f4(10, 20)
print('c=%d' % c)


# 5、局部变量


# 6、全局变量

