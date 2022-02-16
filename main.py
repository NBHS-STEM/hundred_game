import itertools
import os


# Instructions & setup
os.system('clear')
print("This is the 💯 game - on your turn you'll choose a whole number between 1 and 10 to add to the shared total.\nWhichever player reaches 100 first wins the game!\n")

total = 0
player = itertools.cycle('12')

# Game loop
while True:
	player_num = next(player)
	# Validation loop
	while True:
		print(f"\nThe current total is {total}.")
		try:
			step = int(input(f"Player {player_num}, choose a number between 1 and 10 to add: "))
			if not (1 <= step <= 10):
				raise ValueError
			break
		except ValueError:
			print("Invalid entry")
	total += step
	if total >= 100:
		print(f"Player {player} wins!")
		break
	
	
	