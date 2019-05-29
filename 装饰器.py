# Author:jiang
import time


# 函数装饰器
def zhuang(func):
    def funczhuang(*args, **kw):
        print(time.time())
        print("_______________________________________________")
        func(*args, **kw)

    return funczhuang


# 函数装饰器传参
def zhuang1(hao):
    def zhuang2(func1):
        def funczhuang(*args, **kw):
            print(time.time())
            print(hao)
            print("第三层")
            func1(*args, *kw)

        print("第二层+可套代码")
        return funczhuang

    print('第一层+可套代码')
    return zhuang2


# 类装饰器
class Clswrapper(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(time.time())

        return self.func(*args, **kwargs)


# 传参类装饰器
class Zhuang(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(time.time())
            print(self.name)
            func(*args, **kwargs)

        return wrapper


@zhuang
def func1(name, age):
    print("This is func1" + name)
    print(age)


@zhuang
@zhuang1("nihao")
def func2(name, age, school):
    print("This is func1" + name)
    print(age)
    print(school)


if __name__ == "__main__":
    # func1("jiang", 20)
    func2("shuang", 21, "chaungxing")
