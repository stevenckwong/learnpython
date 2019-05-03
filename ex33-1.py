start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
interval = int(input("Enter interval: "))

i = start
elements = []

while i <= end:
    elements.append(i)
    i = i + interval

print(f"Done. All the elements are now in the list that looks like {elements}")

index = int(input(f"Enter a random number between 1 and {len(elements)}: "))

# index - 1 because index of a list starts at 0.
print(f"Great! You selected the winning number {elements[index-1]}")
