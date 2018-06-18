num_players = 0
player_lifepoints = []
player_names = []
run = True

def getPlayers():
	global num_players
	print("How many players are there?")
	num_players = int(input())

def getPlayerNames(x):
	global player_names
	print ("\033[H\033[J")
	for i in range(x):
		print("Please enter player", i + 1, "name.")
		player_names.append(input())

def setStartingLifepoints(x):
	global player_lifepoints
	print ("\033[H\033[J")
	for i in range(x):
		player_lifepoints.append(8000)
	print("\n")

def displayCurrentStats(x):
	global player_names, player_lifepoints
	print ("\033[H\033[J")
	for i in range(x):
		print(player_names[i], "lifepoints =", player_lifepoints[i])
	print("\n")
	displayMenu()

def displayMenu():
	global run
	print("-------------------")
	print("|    ", "Options", "    |")
	print("+-----------------+")
	print("| ", "(A)pply Damage", "|")
	print("|", "(D)isplay Stats", "|")
	print("|", "(I)ncrease Life", "|")
	print("|    ", "(Q)uit", "     |")
	print("-------------------", "\n")
	print("What would you like to do?")
	choice = input()
	if choice == "A" or choice == "a":
		applyDamage()
	elif choice == "I" or choice == "i":
		increaseLife()
	elif choice == "D" or choice == "d":
		displayCurrentStats(num_players)
	elif choice == "Q" or choice == "q":
		run = False

def applyDamage():
	global player_lifepoints
	print ("\033[H\033[J")
	print("Please enter player number.")
	damaged = int(input())
	print("Please enter damage.")
	damage = int(input())
	player_lifepoints[damaged - 1] = player_lifepoints[damaged - 1] - damage
	print("\n")
	displayCurrentStats(num_players)

def increaseLife():
	global player_lifepoints
	print ("\033[H\033[J")
	print("Please enter player number.")
	healed = int(input())
	print("Please enter life.")
	life = int(input())
	player_lifepoints[healed - 1] = player_lifepoints[healed - 1] + life
	print("\n")
	displayCurrentStats(num_players)

def playGame():
	while run == True:
		print ("\033[H\033[J")
		getPlayers()
		getPlayerNames(num_players)
		setStartingLifepoints(num_players)
		displayMenu()
		# applyDamage()

playGame()