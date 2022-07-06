import math

filename = "test.mkv"
chunks = 3

cnk_size = 10485760

file_size = 0
with open(filename, "rb") as frb:
    for line in frb:
        file_size += len(line)
chunks_size = math.ceil(file_size/cnk_size)




i = 0
with open(filename, "rb") as fr:
    files_chunks_name = ''
    while i < chunks_size:
        with open(f'output/{filename+str(i+1)}', 'wb') as f:
            f.write(fr.read(cnk_size))
        files_chunks_name = files_chunks_name + f"+\"{filename+str(i+1)}\""
        i+=1

with open('output/stapler.bat', 'a') as fs:
    fs.write(f'Copy /b {files_chunks_name[1:]} "chunks"')

with open('output/stapler2.bat', 'a') as fs:
    fs.write(f'Rename "chunks" "{filename}"')

with open('output/stapler3.bat', 'a') as fs:
    fs.write(f'Del {files_chunks_name.replace("+", " ")} "stapler.bat" "stapler2.bat" "stapler3.bat"')

print("Файл поделён")