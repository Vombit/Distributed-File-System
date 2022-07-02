from ast import For, While
from dataclasses import dataclass
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
        print(line)
chunks_size = math.ceil(file_size/chunks)
# print(f"Размер чанка: {chunks_size/1024} килобайт")
print(f"Размер чанка: {chunks_size} килобайт")

with open(filename, "rb") as fr:
    files_chunks_name = ''
    size = 0
    i = 0
    for line in fr:
        chunk_data = line

        with open(f'output/{filename+str(i+1)}', 'ab') as f:
                size += len(chunk_data)
                if size < chunks_size:
                    f.write(chunk_data)

                else:
                    i+=1
                    size=0
        print(size)

        # while i < chunks:
        #     while size < chunks_size:
        #         with open(f'output/{filename+str(i+1)}', 'a') as f:
        #             f.write(line)
        #         size += len(line)
        #     files_chunks_name = files_chunks_name + f"+\"{filename+str(i+1)}\""
        #     size=0
        #     i+=1

# with open('output/stapler.bat', 'a') as fs:
#     fs.write(f'Copy /b {files_chunks_name[1:]} "chunks"\nRename "chunks" "{filename}"\nDel {files_chunks_name.replace("+", " ")} "stapler.bat"')

print("Файл поделён")