def snapCrackle():
  """
  Prints ({number} snap crackle) if number is divisible by 7 and 3 or the number contains either 7 or 3

   Prints ({number} snap) if number is divisible by 3 or the number contains 3

   Prints ({number} crackle) if number is divisible by 7 or the number contains 7

   If none of the contitions is met, print just the {number}

  """
  for n in range(1,101):
    if (n % 3 == 0 or '3' in str(n)) and (n % 7 == 0 or '7' in str(n)):
      print(f'{n} snap crackle')
    elif n % 3 == 0 or '3' in str(n):
      print(f'{n} snap')
    elif n % 7 == 0 or '7' in str(n):
      print(f'{n} crackle')
    else:
      print(n)
  return

snapCrackle()