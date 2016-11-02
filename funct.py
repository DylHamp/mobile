def friend():
	name = input("Hi, what is your name? ")
	print("Hello " +  name + ", will you be my friend?")
	rel = input("(y/n)? ")
	if rel == "y":
		print("Yay! We are friends!")
		print("What can I do for you friend?")
		help = input()
		if "lonely" in help:
			print("No worries, I am always with you")
		if "sad" in help:
                	print("Then I shall cheer you up!")
		else:
			print("Maybe someother time")
	elif rel == "n":
		print("Fuck you")
	else:
		print("Sorry I didn't understand you...")
		print("Please try again.")
