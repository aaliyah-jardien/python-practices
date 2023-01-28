# write a program that can ask a user’s name and save it to a file.

# create variable to store file info
# use path to locate file
path = "/home/wtc/student_work/file-handling/names.txt"

# ask users name, using the input function
name = input("What's your name?")

# declaring variable to handle the "file"
# opening file, put in read mode
file = open(path)

# appending to file
file = open(path, "a")
file.write(name + '\n') # adds each input on a new line

# printing all content read from file
file = open(path, "r")
print(file.readlines())

# closing the file
# file.close()














# # reads all content in file
# file.read()

# # reading the file line by line
# file.readline()

# # reading all content line by line
# file.readlines()