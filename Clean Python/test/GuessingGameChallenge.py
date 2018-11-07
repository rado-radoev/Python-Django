from random import randint

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

MIN = 1
MAX = 100
RAND_NUM = randint(MIN, MAX) + 1
print(RAND_NUM)
player_number= 0

guesses = 0
guessed = False
prevGuess = False

cold_message = "COLD"
warm_message = "WARM"

while guessed != True:

    while player_number not in range(MIN,MAX,1):

        player_number = int(input("Choose a number between {min} and {max}:\n".format(min=MIN, max=MAX)))

        if (player_number < 1 or player_number > 100):
            print("OUT OF BOUNDS")
        elif (player_number == RAND_NUM):
            print("You guessed it. Took you {attempts} attempts".format(attempts=guesses))
            guessed = True
            break

        if (player_number in range(MIN,MAX,1)):
            guesses += 1

    if (guessed != True):

        if (prevGuess):
            cold_message = "COLDER"
            warm_message = "WARMER"

        if (player_number in range(RAND_NUM-10, RAND_NUM+10,1)):
            print(warm_message)
        else:
            print(cold_message)

        prevGuess = True
        player_number = 0
