from ast import For
from tkinter import N
from dirsync import sync
import math
sourcedir = 'C:\\qwe'
targetdir = 'E:\\test'

def syncFile(x, y):
    return sync(x, y, 'sync', purge = True, create = True, content = True)


# syncFile(sourcedir, targetdir)

splitter_mode = 0

filename = "test.zip"
chunks = 2


files = open(filename, "rb")
data = files.read()

# print (len(data))

file_size = len(data)


chunks_size = file_size/chunks
print('Размер чанка:'+chunks_size)

files.close()

files = open(filename, "rb")

i=0
while i < chunks:
    with open(filename+str(i+1), 'wb') as f:
        f.write(files.read(math.ceil(chunks_size)))
    i+=1
print("Файлы записаны")


files.close()