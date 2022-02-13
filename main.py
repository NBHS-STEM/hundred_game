import itertools

# global vars
total = 0
player = itertools.cycle('12')
class NumError(Exception):
  pass

print(f"\nThe current total is {total}.")
while True:
  step = input(f"Player {next(player)}, choose a number to add: ")
  try:
    if int(step)<1:
      raise NumError 
    elif int(step)>10:
      raise NumError
    elif int(step)%1 != 0:
      raise NumError
    else:
      pass
  except NumError:
    print("CORRECT NUMBERS PLEASE\n")
  except ValueError:
    print("AN INTEGER, PLEASE\n")
  else:
    break
total += int(step)
if total == 100:
    print(f"Player {player} wins!")