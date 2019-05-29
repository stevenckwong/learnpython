from sys import exit

## Python does not support in out parameters or call by reference.
## But we can return multiple values as shown in this example.

def test_io_params(inParam, inOutParam):
    inParam = 10 + int(inParam);
    inOutParam = 20 * int(inOutParam);

    return inParam, inOutParam;

i = input("Please enter a number for inParam: ")
io = input("Please enter a number for inOutParam: ")

if i.isdigit():
    if io.isdigit():
        ret1, ret2 = test_io_params(i,io)
        print (f"inParam is now {i}")
        print (f"inOutParam is now {io}")
        print (f"inParam used by function to add 10 to its original value is now {ret1}")
        print (f"inOutParam used by function to multiply its original value by 20 is now {ret2}")
    else:
        print ("Dont use the program if you cant follow instructions.")
else:
    print ("Dont use the program if you cant follow instructions.")
