import itertools

class NumberError(Exception):
  pass
#global vars
total = 0
player = itertools.cycle('12')

# Game loop
while True:
	# Validation loop
	while True:
		print(f"\nThe current total is {total}.")
		try:
			step = int(input(f"Player {next(player)}, choose a number between 1 and 10 to add: "))
			if not (1 <= step <= 10):
				next(player)
				raise ValueError
			break
		except ValueError:
			print("Invalid entry")
	total += step
	if total == 100:
		print(f"Player {player} wins!")
		break

	
	