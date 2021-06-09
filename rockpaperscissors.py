import os, ctypes, random

if os.name =='nt':
	os.system('cls')
	ctypes.windll.kernel32.SetConsoleTitleW(f"Rock! Paper! Scissors!")

choices = ["Rock", "Paper", "Scissors"]
botChoice = random.choice(choices)
userChoice = (input("Choose one! Rock, Paper or Scissors\n"))
result = ["Tied!", "Lost!", "Won!"]

if userChoice not in choices:
    print("That is not a valid option!")
    exit()

elif userChoice == choices[0] and botChoice == choices[0]:
    result = result[0]

elif userChoice == choices[0] and botChoice == choices[1]:
    result = result[1]

elif userChoice == choices[0] and botChoice == choices[2]:
    result = result[2]

elif userChoice == choices[1] and botChoice == choices[1]:
    result = result[0]

elif userChoice == choices[1] and botChoice == choices[2]:
    result = result[1]

elif userChoice == choices[1] and botChoice == choices[0]:
    result = result[2]

elif userChoice == choices[2] and botChoice == choices[2]:
    result = result[0]

elif userChoice == choices[2] and botChoice == choices[0]:
    result = result[1]

elif userChoice == choices[2] and botChoice == choices[1]:
    result = result[2]

os.system('cls')
print(f"Your Choice: {userChoice}\nBots Choice: {botChoice}\nYou {result}")
exit()