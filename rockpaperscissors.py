import os, ctypes, random
from playsound import playsound

if os.name is 'nt':
    clear = os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Rock! Paper! Scissors!")
else:
    clear = os.system('clear')

userScore, botScore = 0, 0

while True:
    choices = ["Rock", "Paper", "Scissors"]
    result = ["Tied!", "Lost!", "Won!"]
    invalidSongs = ["android", "omg"]
    idiot = random.choice(invalidSongs)
    botChoice = random.choice(choices)
    clear
    userChoice = (input("Choose one! Rock, Paper or Scissors\n"))

    if userChoice not in choices:
        playsound(f'sounds/{idiot}.wav')
        print("That is not a valid option!")
        exit()

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

    clear
    print(f"Your Choice: {userChoice} | Bot Choice: {botChoice}\nYou {result}\n\nYour Score: {userScore} | Bot Score: {botScore}")

    retry = input("Would you like to play again? (Y/N): ")
    if retry not in ["y", "Y", "Yes"]:
        print("See you next time!")
        break
    else:
        playsound("sounds/yeahyeah.wav")
