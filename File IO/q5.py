# tell() gives the file's current pointer position.
# seek(offset, [, whence]). Set the file pointer to the offset value.
# whence indicates the absolute/relative position to place the file pointer. The default(0) is always from the
# beginning of file.
f = open('tmp.txt', 'w')
f.write("abcdefghij")
f.close()
f = open('/home/ak/Desktop/Pyschool Practice/File IO/tmp.txt')
print(f.tell())
# 0L
f.seek(3, 0)  # move 3 bytes (4th character) from beginning of the file
print(f.tell())
# 3L
print(f.read(1))     # file pointer is advanced 1 positiion
# 'd'
print(f.tell())
# 4L
