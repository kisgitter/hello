#b本模块实现单例模式
#Singleton1使用__new__来实现
class Singleton1(object):
   def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance 对象
         if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton1, cls).__new__(cls)
         return cls.instance
   
#另外一个__new__实例
class Singleton2(object):
    __instance = None
    def __new__( cls , *args , **kwargs):
            if cls.__instance is None:
               cls.__instance = object.__new__(cls)
               return cls.__instance
            else:
               return cls.__instance

obj1 = Singleton1()
obj2 = Singleton1()

obj1.attr1 = 'value1'
print(obj1.attr1, obj2.attr1)
print (obj1 is obj2)

#使用模块
# mysingle.py
class MySingle:
   def foo(self):
       pass
sinleton = MySingle()
# 将上面的代码保存在文件mysingle.py 中，然后这样使用：
#from mysingle import sinleton
#singleton.foo()

#使用装饰器
def singleton(cls):
   instances = {}
   def getinstance(*args,**kwargs):
       if cls not in instances:
             instances[cls] = cls(*args,**kwargs)
       return instances[cls]
   return getinstance

@singleton
class MyClass:
    a = 1
c1 = MyClass()
c2 = MyClass()
print(c1 == c2) # True
# 在上面，我们定义了一个装饰器singleton，它返回了一个内部函数getinstance，
#该函数会判断某个类是否在字典instances 中，如果不存在，则会将cls 作为key，cls(*args, **kw) 作为value 存到instances 中，
# 否则，直接返回instances[cls]。
