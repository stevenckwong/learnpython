from sys import exit

def test_io_params(inParam, inOutParam):
    inParam = 10 + inParam;
    inOutParam = 20 * inOutParam;

i = input("Please enter a number for inParam: ")
io = input("Please enter a number for inOutParam: ")

if i.isdigit():
    if io.isdigit():
        test_io_params(int(i),int(io))
        print (f"inParam is now {i}")
        print (f"inOutParam is now {io}")
    else:
        print ("Dont use the program if you cant follow instructions.")
else:
    print ("Dont use the program if you cant follow instructions.")
