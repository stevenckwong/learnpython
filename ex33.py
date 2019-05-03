# While Loops
i = 0
elements = []

while i < 6:
    print(f"i is currently {i}")
    i = i + 1
    elements.append(i)
    print(f"Elements currently look like {elements}")
    print(f"i is now {i}")

print("While loop ended")

print("For loop starting")
for current in elements:
    print(f"Element: {current}")
