def consumer():
    r = ''
    while True:
        m = yield r
        if not m:
            return
        print('[CONSUMER] Consuming %s...' % m)
        r = '200 OK'

def produce(c):
    #启动生成器
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

