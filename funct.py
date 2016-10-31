def friend():
	name = input("Hi, what is your name? ")
	print("Hello " +  name + ", will you be my friend?")
	rel = input("(y/n)? ")
	if rel == "y":
		print("Yay! We are friends!")
	if rel == "n":
		print("Fuck you")
	else:
		print("Sorry I didn't understand you...")
		print("Please try again.")
