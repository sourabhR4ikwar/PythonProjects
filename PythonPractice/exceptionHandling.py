import random

game_number = random.randint(1,10);
player_number = input('Guess a Number Between 1 and 10\n>> ')
if(str(game_number) is player_number):
    print("You won")
else:
    print("Better Luck Next Time! The number was",game_number)
