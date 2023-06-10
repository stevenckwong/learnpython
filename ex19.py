# Functions

def print_no_of_args(*args):
    print(f"You called this function with {len(args)} number of args")

def print_two_args(arg1, arg2):
    print(f"The 2 args you passed in are: {arg1}, {arg2}")


print_no_of_args("one","two","three","four","five")

print_two_args("Samuel", "Samantha")
