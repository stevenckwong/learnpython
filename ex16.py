# Read / Write __file__

filename = input("Please enter a filename > ")

print(f"We're going to erase {filename}")
print("Press CTRL-C if you want to cancel this operation")
print("Press ENTER to continue")
input("Decide now: ")

print(f"Opening the file called {filename}")
target = open(filename, "w")

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I am going to ask you for 3 lines...")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I am going to write these into the file")

target.write(f"{line1}\n{line2}\n{line3}")
# target.write(line2+"\n")
# target.write(line3+"\n")

target.close()

print("Done.")
