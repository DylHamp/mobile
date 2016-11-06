name = input("Hi, what is your name? ")
print("Hello " + name + ", will you be my friend?")
rel = input("(y/n)? ")
if rel == "y":
	print("Yay! We are friends!")
	adj = ['Friend', name]
if rel == "n":
	print("Well fuck you then.")
	adj = ['You dick', 'poop head']
req = "none"
while req != "bye":
	print("What can I do for you " + adj[1] + "?")
	req = input()
	if "die" in req:
		print("Jokes on you I'm not even alive! " + adj[0] + ".")
	elif "money" in req:
		print("MONEY MONEY MONEY... MONEY!... MONEY")
	else:
		print("I'm not google... I am not made for that.")
print("Later " + adj[1] + ".")
