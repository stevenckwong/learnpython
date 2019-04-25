from sys import argv

scriptname, username = argv
prompt = "> "

print (f"Hello {username}, I am {scriptname} script.")
print ("I would like to ask you a few questions...")
print (f"Do you like me {username}?")
likes = input(prompt)

print (f"Where do you live {username}?")
address = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print (f"""
So, you said {likes} to liking me and you live at {address}.
Unfortunately for me, I don't know where that is.
You have a {computer} computer, so you're luckier than most.
""")
