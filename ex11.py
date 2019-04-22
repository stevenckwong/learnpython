#Getting inputs and decisions

# we put end=" " so that the cursor stays on the same line
print ("What's your name", end=" ")
name = input();

print ("How old are you (in years)?", end=" ")
age = int(input());

print ("How tall are you (in inches)?", end=" ")
height = float(input());

print ("How much do you weigh (in lbs)?", end=" ")
weight = float(input());

print (f"Hello {name}, you are {age} years old, weighs {weight} lbs and you are {height} inches tall")

if age > 40:
    young_or_old = "Old"
else:
    young_or_old = "Young"
print (f"At {age} years old, you are considered {young_or_old}")

if height > 65:
    if weight > 180:
        heavy = "heavy"
    else:
        heavy = "not heavy"
else:
    if weight > 150:
        heavy = "heavy"
    else:
        heavy = "not heavy"
print (f"At {height} inches tall and weighing {weight} lbs, you are {heavy}")
