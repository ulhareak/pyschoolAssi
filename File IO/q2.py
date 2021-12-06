# write(str). Write a string to the file.
# Create a function that appends the name and email to the end of a named file.
def addEmail(filename, name, email):
    filename = "/home/ak/Desktop/Pyschool Practice/File IO/"+filename
    mode = 'w'
    f = open(filename, mode)  # replace the mode

    # Append name and email, each record should end with '\n'.
    f.write(name+"\n")
    f.write(email)

    # close file
    f.close()
    return f  # do not remove this line


print(addEmail('emails.txt', 'Mary', 'mary@gmail.com'))
print(addEmail('emails.txt', 'John', 'john@gmail.com'))
