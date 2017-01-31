def help():
	req = "none"
	while req != "bye":
		print("What can I do for you " + adj[1] + "?")
		req = input()
		if "die" in req:
			print("Jokes on you I'm not even alive! " + adj[0] + ".")
		elif "money" in req:
			print("MONEY MONEY MONEY... MONEY!... MONEY")
		else:
			print("Sorry I am not google... ask me something I know.")
def game():
	print("What kind of game do you want to play?")
	game = input()
	if "adventure" in game:
		print("adventure()")
	else:
		print("I don't know that game. Maybe someother time")
name = input("Hi, what is your name? ")
print("Hello " + name + ", will you be my friend?")
rel = input("(y/n)? ")
if rel == "y":
	print("Yay! We are friends!")
	adj = ['Friend', name]
if rel == "n":
	print("Well fuck you then.")
	adj = ['You dick', 'poop head']
topic = "none"
while topic != "bye":
	topic = input("What do you want to talk about " + adj[1] + "? ")
	if "help" in topic:
		help()
	elif "game" in topic:
		game()
	else:
		print("How about something else?")
print("Later " + adj[1] + ".")
