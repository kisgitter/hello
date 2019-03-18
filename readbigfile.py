#分块读取，rb速度比r快非常多
def readInChunks(fileObj, chunkSize=4096):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 4kB.
    """
    while 1:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data

f = open('1.txt','rb')
for chuck in readInChunks(f):
     pass
f.close()
#使用with open,这个代码在打开文件的过程中，不会一次性读取全部文件，而是采用每次读取一行的方式，类似于buffer机制
with open("1.txt",'rb') as f:
    for line in f:
       pass

