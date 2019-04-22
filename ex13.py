# command line arguments
from sys import argv

# this line unpacks the array of arguments into variables from left to right
scriptname, first, second, third = argv

print ("the script name is: ", scriptname)
print ("the first variable is: ", first)
print (f"the second: {second} and the third: {third}")
