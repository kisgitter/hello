#-------------python杂记------------------------------------
#1.列表去重并保证原来的序列
a = ['a','b','c','d','f','a','b']
b = list(set(a))
b = sorted(b,key = lambda x:a.index(x))
print(b)

#2.random模块的详细使用方法
import random
a = random.random()    #生成0-1随机浮点数
b = random.randint(3,5)#生成3-5随机整数
c = random.uniform(1,9)#生成1-9随机浮点数
d = random.choice(list(range(1,100))) #从列表里随机选择数据
e = random.shuffle(list(range(1,100)))#打乱列表
f = random.randrange(1,20,2) #从1到20按照基数2递增选取数字
g = random.sample(list(range(1,100)),4) #从指定序列1,100，获取长度为4的序列并随机排序

