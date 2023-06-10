filename = input("Please enter a filename > ")
try:
    target = open(filename,"a")
    target.write("hello world\n")
    target.close()
except IsADirectoryError:
    newfilename = filename + "/output.txt"
    target = open(newfilename,"a")
    target.write("a whole new world\n")
    target.close()