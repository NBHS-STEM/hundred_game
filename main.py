import itertools
class NumberError(Exception):
  pass
# global vars
total = 0
player = itertools.cycle('12')

step = (input(f"Player {next(player)},a number between 1 and 10: "))

while True:
  print(f"\nThe current total is {total}.")
  try:
    if int(step)%1 != 0:
      raise NumberError
    elif int(step)<1:
      raise NumberError
    elif int(step)>10:
      raise NumberError
    else:
      pass
  except ValueError:
    print("ints only")
  except NumberError:
    print("Not Valid")
  else:
    break

  total += step
  if total == 100:
	  print(f"Player {player} wins!")
	  break
	
	
	