#序列化
import pickle

d = dict(name = 'bob',age = 15 ,score=99 )
#dumps把任意对象转化为bytes，写入文件
d_byte = pickle.dumps(d)
#loads把对象还原
rd = pickle.loads(d_byte)

#也可以使用dump将对象序列化直接写入文件
f = open('dump.txt','wb')
pickle.dump(d,f)
#还原的时候使用load
from_file = pickle.load(f)

#json 的序列化
import json
d = dict(name = 'bob', age = 20 ,score =88)

# json.dumps()返回str,标准json
str_json = json.dumps(d)
#json.loads还原为dict
re_d = str_json.loads(str_json)

#json对象写入文件,注意这里只能是json对象
f_write = open('json.txt','wb')
json.dump(str_json,f_write)

#从json file里还原一个json串
f_read = open('json.txt','rb')
json.load(f)

