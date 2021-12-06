# writelines(seq). Write a sequence of strings to the file. writelines() does not add line separators.
output = []
for x in range(5):
    output.append(str(x))
f = open('/home/ak/Desktop/Pyschool Practice/File IO/tmp.txt', 'w')
f.writelines(output)            # content is "01234"
f.writelines("\n".join(output)) # content is "012340\n1\n2\n3\n4"
f.close()
# Which of the following sequences will give a TypeError when passed to writeline method?
#seq = [1, 2, 3, 4]