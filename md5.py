#摘要算法用处,防止文档被篡改，判断是否同一文档，加密密码等
import hashlib
import random

#MD5摘要算法，生成128bit，32个十六进制数
md5 = hashlib.md5()
#字符串过长可多次update
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.update('123456'.encode('utf-8'))
print(md5.hexdigest())
#d26a53750bc40b38b65a520292f69306

#SHA1摘要算法用法同MD5，安全性更高，160bit,40个二进制数
#此外还有SHA156、SHA512，安全性更好，但速度算法慢，生成摘要更长
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8')) #注意一定要编码
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

#简单密码验证案例
def get_md5(password):
     md5 =  hashlib.md5()
     md5.update(password.encode('utf-8'))
     return md5.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    return get_md5(password) ==db[user]

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

#加盐，给口令加上一些东西，一起计算摘要，保证更安全
def calc_md5(password):
    return get_md5(password + 'the-Salt')

#动态加盐登录口令实例
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db ={
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
    }
def login(username, password):
    user = db[username]
    return user.password == get_md5(password)

