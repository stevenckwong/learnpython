#String formatting

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print (joke_evaluation.format(hilarious))

a = "Adam"
b = "Bob"
c = "Cathryn"

friends = "There were once 3 friends named {}, {} and {}"
print (friends.format(a,b,c))

# positioning of the variables corresponds to the location of the {} in the string
bfgf = "{} and {} were in love and {} was jealous"
print (bfgf.format(a,c,b))

bfgf2 = f"Because of this {b} left the group, and {a} and {c} broke up"
print (bfgf2)

w = "This is eh left side of .... "
e = "a string with a right side."

print (w + e)
