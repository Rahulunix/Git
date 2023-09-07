player_guess = int(input("Enter the number"))

no = 17
no_of_guesses = n

if player_guess == no:
    print("you guessed correctly")
elif player_guess < 1 or player_guess > 100:
    print("OUT OF BOUND")
elif abs(no - player_guess) < 10:
    print("WARM")
elif abs(no - player_guess) > 10:
    print("COLD")

elif abs(no - player_guess) < 9:
    print("WARMER")
elif abs(no - player_guess) > 11 :
    print("WARMER")
    

