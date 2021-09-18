for n in range (1, 101):
  flagged = False
  if n % 3 == 0:
    flagged = True
    print("fizz", end="")
  if n % 5 == 0:
    flagged = True
    print("buzz", end="")
  if flagged:
    print("\r")
  else:
    print(f"{n}")
