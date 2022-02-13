import itertools

class NumberError(Exception):
  pass
#global vars
total = 0
player = itertools.cycle('12')

while True:
	print(f"\nThe current total is {total}.")
	step = int(input(f"Player {next(player)}, choose a number between 1 and 10 to add: "))
	try:
		if step < 0 or step > 10:
			raise NumberError
	except NumberError:
		print(f"\nNumber not between 1 and 10")
	if step > 0 and step <= 10:
		total += step
	if total == 100:
		print(f"Player {player} wins!")
		break
	
	
	