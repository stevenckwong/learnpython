from os.path import exists
print("Please provide 2 filenames:")
filename1 = input("File 1: ")
filename2 = input("File 2: ")

print(f"Copying {filename1} to {filename2}")

indata = open(filename1).read()
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exists? {exists(filename2)}")
input("Ready, hit RETURN to continue...")

out_file = open(filename2,"w")
out_file.write(indata)

print ("Alright. It's done!")

out_file.close()
