from sys import exit

def test-io-params(inParam, inOutParam):
    inParam = 10 + inParam;
    inOutParam = 20 * inOutParam;

i = input("Please enter a number for inParam: ")
io = input("Please enter a number for inOutParam: ")

if i.isdigit():
    if io.isdigit():
        test-io-params(i,io)
        print (f"inParam is now {inParam}")
        print (f"inOutParam is now {inOutParam}")
    else:
        print ("Dont use the program if you cant follow instructions.")
else:
    print ("Dont use the program if you cant follow instructions.")
