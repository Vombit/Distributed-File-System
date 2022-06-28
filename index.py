from ast import For
from os import fsencode
from tkinter import N
from dirsync import sync
import math
sourcedir = 'C:\\qwe'
targetdir = 'E:\\test'

def syncFile(x, y):
    return sync(x, y, 'sync', purge = True, create = True, content = True)

# syncFile(sourcedir, targetdir)

filename = "test.png"
splitter_mode = 0
chunks = 3

file_size = 0
with open(filename, "rb") as frb:
    for line in frb:
        file_size += len(line)
chunks_size = math.ceil(file_size/chunks)
print(f"Размер чанка: {chunks_size/1024} килобайт")

with open(filename, "rb") as fr:
    files_chunks_name = ''
    i = 0
    while i < chunks:
        with open(f'output/{filename+str(i+1)}', 'wb') as f:
            f.write(fr.read(chunks_size))
        files_chunks_name = files_chunks_name + f"+\"{filename+str(i+1)}\""
        i+=1

with open('output/stapler.bat', 'a') as fs:
    fs.write(f'Copy /b {files_chunks_name[1:]} "chunks"\nRename "chunks" "{filename}"\nDel {files_chunks_name.replace("+", " ")} "stapler.bat"')

print("Файл поделён")