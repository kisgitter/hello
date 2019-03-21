def consumer():
    r = ''
    while True:
        m = yield r #yield r 返回 r ,上一次执行到yield r 终止，再次开启从 m 开始，同时m的值等于produce中发送过来的n
        if not m:
            return
        print('[CONSUMER] Consuming %s...' % m)
        r = '200 OK'

def produce(c):
    #启动生成器,也可以写作next(c),效果一样i
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) #发送数据给生成器，下一步执行consumer() 中的 n = yield r
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

