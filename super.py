#本例用于学习super(),super可以使子类调用父类的函数，同时避免多重继承情况下，父类被初始化多次
#只有一个父类情况下，BaseClass.work(self)没问题，多重继承(砖石继承 ：B C 继承A,D继承A)就会导致基类被调用多次，产生错误，此时用super()避免这样的情况
class BaseClass(object):
    num_base_calls = 0 #记录基类被调用次数
    def work(self):
        print("work method of calling base class")
        self.num_base_calls += 1

class BClass(BaseClass):
    num_bclass_calls = 0 #记录被调用次数
    def work(self):
        super(BClass,self).work() #python2写法，python3 可以写作 super().work()
        print("work method of calling BClass class")
        self.num_bclass_calls += 1

class AClass(BaseClass):
    num_aclass_calls = 0 #记录被调用次数
    def work(self):
        super(AClass,self).work()
        print("work method of calling AClass class")
        self.num_aclass_calls += 1


class CClass(BClass, AClass):
    num_cclass_calls = 0 #记录被调用次数
    def work(self):
        super(CClass,self).work()
        print("Calling work method on CClass")
        self.num_cclass_calls += 1

if __name__ == '__main__':

    c = CClass()
    c.work()
    #print(c.num_cclass_calls, c.num_aclass_calls, c.num_bclass_calls, c.num_base_calls)

#super()样例2
exp = '''
class A(object):
    def __init__(self):
        print "init A Class"

class B(A):
    def __init__(self):
        print"init B class"
        super(B, self).__init__()

class C(A):
    def __init__(self):
        print"init C class"
        super(C, self).__init__()

class D(B,C):
    def __init__(self):
        print "init D class"
        super(D, self).__init__()

class E(A):
    def __init__(self):
        print "init E class"
        super(E, self).__init__()

class F(D,E):
    def __init__(self):
        print "init F class"
        super(F, self).__init__()
F = F()

结果：
init F class
init D class
init B class
init C class
init E class
init A Class
'''