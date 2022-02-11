import itertools
class NumberError(Exception):
  pass

# global vars
total = 0
player = itertools.cycle('12')

while True:
  print(f"\nThe current total is {total}.")
  while True:
    step = (input(f"Player {next(player)}, choose a number between 1 and 10 to add: "))
    try:
      if int(step)%1 != 0:
        raise NumberError
      elif int(step)>10:
        raise NumberError
      elif int(step)<1:
        raise NumberError
    except NumberError:
      print("ONE IN TEN\n")
    except ValueError:
      print("Whole Numbers Only\n")
    else:
      break
  total += int(step)
  if total == 100:
	  print(f"Player {player} wins!")
	  break