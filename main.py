import itertools

# global vars
total = 0
player = itertools.cycle('12')

while True:
	print(f"\nThe current total is {total}.")
	step = int(input(f"Player {next(player)}, choose a number between 1 and 10 to add: "))
	total += step
	if total == 100:
		print(f"Player {player} wins!")
		break
	
	
	