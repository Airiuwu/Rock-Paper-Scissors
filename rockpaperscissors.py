import os, ctypes, random, requests, time, shutil, getpass

if os.name == 'nt':
	os.system('cls')
	print("Installing Requirements....")
	os.system('py -m pip install -r requirements.txt')
	print("Done!")
from playsound import playsound

def main():
	ctypes.windll.kernel32.SetConsoleTitleW(f"Rock! Paper! Scissors!")
	os.system('cls')
	print("\n")
	print("\033[96m██████   ██████   ██████ ██   ██     ██████   █████  ██████  ███████ ██████      ███████  ██████ ██ ███████ ███████  ██████  ██████  ███████ ".center(shutil.get_terminal_size().columns))
	print("\033[96m██   ██ ██    ██ ██      ██  ██      ██   ██ ██   ██ ██   ██ ██      ██   ██     ██      ██      ██ ██      ██      ██    ██ ██   ██ ██      ".center(shutil.get_terminal_size().columns))
	print("\033[96m██████  ██    ██ ██      █████       ██████  ███████ ██████  █████   ██████      ███████ ██      ██ ███████ ███████ ██    ██ ██████  ███████ ".center(shutil.get_terminal_size().columns))
	print("\033[96m██   ██ ██    ██ ██      ██  ██      ██      ██   ██ ██      ██      ██   ██          ██ ██      ██      ██      ██ ██    ██ ██   ██      ██ ".center(shutil.get_terminal_size().columns))
	print("\033[96m██   ██  ██████   ██████ ██   ██     ██      ██   ██ ██      ███████ ██   ██     ███████  ██████ ██ ███████ ███████  ██████  ██   ██ ███████ ".center(shutil.get_terminal_size().columns))
	print("\n")
	print("\33[1m\33[35m(1) Singleplayer".center(shutil.get_terminal_size().columns))
	print("\33[1m\33[35m(2) Multiplayer".center(shutil.get_terminal_size().columns))
	print("\33[37m")
	answer = input()

	if answer == "1":
		singlePlayer()
	elif answer == "2":
		multiPlayer()
	else:
		troll()

def troll():
	gettingTrolled = True
	while gettingTrolled:
		os.system('cls')
		ctypes.windll.kernel32.SetConsoleTitleW(f"Trolled.")
		print("\n")
		print("░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄".center(shutil.get_terminal_size().columns))
		print("░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄".center(shutil.get_terminal_size().columns))
		print("░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█".center(shutil.get_terminal_size().columns))
		print("░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█".center(shutil.get_terminal_size().columns))
		print("░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█".center(shutil.get_terminal_size().columns))
		print("█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█".center(shutil.get_terminal_size().columns))
		print("█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█".center(shutil.get_terminal_size().columns))
		print("░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█".center(shutil.get_terminal_size().columns))
		print("░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█".center(shutil.get_terminal_size().columns))
		print("░░░█░░██░░▀█▄▄▄█▄▄█▄████░█".center(shutil.get_terminal_size().columns))
		print("░░░░█░░░▀▀▄░█░░░█░███████░█".center(shutil.get_terminal_size().columns))
		print("░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█".center(shutil.get_terminal_size().columns))
		print("░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█".center(shutil.get_terminal_size().columns))
		print("░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█".center(shutil.get_terminal_size().columns))
		print("░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█".center(shutil.get_terminal_size().columns))
		playsound('sounds/bruh.wav')

def singlePlayer():
	ctypes.windll.kernel32.SetConsoleTitleW(f"Rock! Paper! Scissors! (Singleplayer)")
	while True:
		userScore, botScore = 0, 0
		choices = ["Rock", "Paper", "Scissors"]
		result = ["Tied!", "Lost!", "Won!"]
		invalidSongs = ["android", "omg"]
		idiot = random.choice(invalidSongs)
		botChoice = random.choice(choices)
		os.system('cls')
		userChoice = (input("Choose one! Rock, Paper or Scissors\n"))

		if userChoice not in choices:
			playsound(f'sounds/{idiot}.wav')
			troll()

		elif userChoice == botChoice:
			result = result[0]
			playsound('sounds/bruh.wav')

		elif userChoice == choices[0] and botChoice == choices[1]:
			result = result[1]
			botScore += 1
			playsound('sounds/fart.wav')

		elif userChoice == choices[0] and botChoice == choices[2]:
			result = result[2]
			userScore += 1
			playsound('sounds/lessgo.wav')

		elif userChoice == choices[1] and botChoice == choices[2]:
			result = result[1]
			botScore += 1
			playsound('sounds/fart.wav')

		elif userChoice == choices[1] and botChoice == choices[0]:
			result = result[2]
			userScore += 1
			playsound('sounds/lessgo.wav')

		elif userChoice == choices[2] and botChoice == choices[0]:
			result = result[1]
			botScore += 1
			playsound('sounds/fart.wav')

		elif userChoice == choices[2] and botChoice == choices[1]:
			result = result[2]
			userScore += 1
			playsound('sounds/lessgo.wav')

		os.system('cls')
		print(f"Your Choice: {userChoice} | Bot Choice: {botChoice}\nYou {result}\n\nYour Score: {userScore} | Bot Score: {botScore}")

		retry = input("Would you like to play again? (Y/N): ")
		if retry not in ["y", "Y", "Yes"]:
			main()
			break
		else:
			playsound("sounds/yeahyeah.wav")

def multiPlayer():
	ctypes.windll.kernel32.SetConsoleTitleW(f"Rock! Paper! Scissors! (Multiplayer)")
	os.system('cls')
	print("\n")
	print("\033[96m██████   ██████   ██████ ██   ██     ██████   █████  ██████  ███████ ██████      ███████  ██████ ██ ███████ ███████  ██████  ██████  ███████ ".center(shutil.get_terminal_size().columns))
	print("\033[96m██   ██ ██    ██ ██      ██  ██      ██   ██ ██   ██ ██   ██ ██      ██   ██     ██      ██      ██ ██      ██      ██    ██ ██   ██ ██      ".center(shutil.get_terminal_size().columns))
	print("\033[96m██████  ██    ██ ██      █████       ██████  ███████ ██████  █████   ██████      ███████ ██      ██ ███████ ███████ ██    ██ ██████  ███████ ".center(shutil.get_terminal_size().columns))
	print("\033[96m██   ██ ██    ██ ██      ██  ██      ██      ██   ██ ██      ██      ██   ██          ██ ██      ██      ██      ██ ██    ██ ██   ██      ██ ".center(shutil.get_terminal_size().columns))
	print("\033[96m██   ██  ██████   ██████ ██   ██     ██      ██   ██ ██      ███████ ██   ██     ███████  ██████ ██ ███████ ███████  ██████  ██   ██ ███████ ".center(shutil.get_terminal_size().columns))
	print("\n")
	print("\33[1m\33[35m(1) Create Game".center(shutil.get_terminal_size().columns))
	print("\33[1m\33[35m(2) Join Game".center(shutil.get_terminal_size().columns))
	print("\33[37m")
	answer = input()

	if answer == "1":
		Searching = True

		os.system('cls')
		print("Please enter your username".center(shutil.get_terminal_size().columns))
		username = input()
		os.system('cls')
		match_password = getpass.getpass(prompt = "Please enter a match password".center(shutil.get_terminal_size().columns))
		requests.get(f"http://rps.airi.cf/api/v1/creategame?p={match_password}&u={username}")

		while Searching:
			time.sleep(2)
			request = requests.get(f"http://rps.airi.cf/api/v1/gameping?p={match_password}&u={username}").json()
			os.system('cls')
			print(request["message"].center(shutil.get_terminal_size().columns))

			if request["message"] != "Waiting for opponent..":
				Searching = False
				SearchingGame = True
				while SearchingGame:
					os.system('cls')
					print("Choose one! Rock, Paper or Scissors\n".center(shutil.get_terminal_size().columns))
					choice = input()
					if choice not in ["Rock", "Paper", "Scissors"]:
						troll()
					else:
						os.system('cls')
						print(f"You picked {choice}!".center(shutil.get_terminal_size().columns))
						requests.get(f"https://rps.airi.cf/api/v1/updategame?u={username}&p={match_password}&vsTvTFhPu7RrKepAg6KzHfRtXzaVkXmP=nXM8d93UPPCmPa5XVtpdLxAgYQAG5D6n&c={choice}&j=no")
						waitingForResponse = True
						while waitingForResponse:
							time.sleep(2)
							daRequest = requests.get(f"http://rps.airi.cf/api/v1/choiceinfo2?u={username}&p={match_password}")
							UwU = daRequest.json()['message']
							if UwU == "0":
								os.system('cls')
								print(f"Waiting for Opponents response...".center(shutil.get_terminal_size().columns))
								time.sleep(2)
							else:
								waitingForResponse = False
								choices = ["Rock", "Paper", "Scissors"]
								result = ["Tied!", "Lost!", "Won!"]

								if UwU == choice:
									result = result[0]
									playsound('sounds/bruh.wav')

								elif choice == choices[0] and UwU == choices[1]:
									result = result[1]
									playsound('sounds/fart.wav')

								elif choice == choices[0] and UwU == choices[2]:
									result = result[2]
									playsound('sounds/lessgo.wav')

								elif choice == choices[1] and UwU == choices[2]:
									result = result[1]
									playsound('sounds/fart.wav')

								elif choice == choices[1] and UwU == choices[0]:
									result = result[2]
									playsound('sounds/lessgo.wav')

								elif choice == choices[2] and UwU == choices[0]:
									result = result[1]
									playsound('sounds/fart.wav')

								elif choice == choices[2] and UwU == choices[1]:
									result = result[2]
									playsound('sounds/lessgo.wav')

								os.system('cls')
								print("Your Choice: {} | {}'s Choice: {}".format(choice, username, UwU).center(shutil.get_terminal_size().columns))
								print("You {}".format(result).center(shutil.get_terminal_size().columns))
								print("\n\n\n\n")
								print("Please type 'Quit' to return to the main menu!".center(shutil.get_terminal_size().columns))
								doYouQuit = input()
								if doYouQuit in ["q", "Quit", "quit"]:
									main()
								else:
									os.system("cls")
									print("YOU WERE TOLD TO QUIT.".center(shutil.get_terminal_size().columns))
									time.sleep(1)
									troll()
					
	elif answer == "2":
		Joining = True

		os.system('cls')
		print("Please enter your username".center(shutil.get_terminal_size().columns))
		userUsername = input()
		os.system('cls')
		print("Please enter the username of the user you want to join".center(shutil.get_terminal_size().columns))
		username = input()
		os.system('cls')
		match_password = getpass.getpass(prompt = "Please enter the match password".center(shutil.get_terminal_size().columns))
		requests.get(f"https://rps.airi.cf/api/v1/joingame?p={match_password}&u={username}&fu={userUsername}")

		while Joining:
			time.sleep(2)
			request = requests.get(f"https://rps.airi.cf/api/v1/gameping?p={match_password}&u={username}")
			OwO = request.json()['message']
			os.system('cls')
			print(OwO.center(shutil.get_terminal_size().columns))
			if OwO == "Match not found.":
				os.system('cls')
				print("Match Not Found.".center(shutil.get_terminal_size().columns))
				time.sleep(2)
				multiPlayer()
			elif OwO != "Joining Game..":
				Joining = False
				os.system('cls')
				print("Choose one! Rock, Paper or Scissors\n".center(shutil.get_terminal_size().columns))
				choice = input()
				if choice not in ["Rock", "Paper", "Scissors"]:
					troll()
				else:
					os.system('cls')
					print(f"You picked {choice}!".center(shutil.get_terminal_size().columns))
					requests.get(f"https://rps.airi.cf/api/v1/updategame?u={username}&u2={userUsername}&p={match_password}&vsTvTFhPu7RrKepAg6KzHfRtXzaVkXmP=nXM8d93UPPCmPa5XVtpdLxAgYQAG5D6n&c2={choice}&j=yes")
					waitingForResponse = True
					while waitingForResponse:
						time.sleep(2)
						daRequest = requests.get(f"http://rps.airi.cf/api/v1/choiceinfo?u={username}&p={match_password}&u2={userUsername}")
						UwU = daRequest.json()['message']
						if UwU == "0":
							os.system('cls')
							print(f"Waiting for {username}'s response...".center(shutil.get_terminal_size().columns))
							time.sleep(2)
						else:
							waitingForResponse = False
							choices = ["Rock", "Paper", "Scissors"]
							result = ["Tied!", "Lost!", "Won!"]

							if UwU == choice:
								result = result[0]
								playsound('sounds/bruh.wav')

							elif choice == choices[0] and UwU == choices[1]:
								result = result[1]
								playsound('sounds/fart.wav')

							elif choice == choices[0] and UwU == choices[2]:
								result = result[2]
								playsound('sounds/lessgo.wav')

							elif choice == choices[1] and UwU == choices[2]:
								result = result[1]
								playsound('sounds/fart.wav')

							elif choice == choices[1] and UwU == choices[0]:
								result = result[2]
								playsound('sounds/lessgo.wav')

							elif choice == choices[2] and UwU == choices[0]:
								result = result[1]
								playsound('sounds/fart.wav')

							elif choice == choices[2] and UwU == choices[1]:
								result = result[2]
								playsound('sounds/lessgo.wav')

							os.system('cls')
							print("Your Choice: {} | {}'s Choice: {}".format(choice, username, UwU).center(shutil.get_terminal_size().columns))
							print("You {}".format(result).center(shutil.get_terminal_size().columns))
							print("\n\n\n\n")
							print("Please type 'Quit' to return to the main menu!".center(shutil.get_terminal_size().columns))
							doYouQuit = input()
							if doYouQuit in ["q", "Quit", "quit"]:
								main()
							else:
								os.system("cls")
								print("YOU WERE TOLD TO QUIT.".center(shutil.get_terminal_size().columns))
								time.sleep(1)
								troll()

	else:
		troll()

main()
