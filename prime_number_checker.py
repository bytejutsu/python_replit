def prime_checker(number):
  is_prime = True
  for i in range(2,number):
    if number % i == 0:
      is_prime = False
      break

  print("is prime") if is_prime else print("not prime")


n = int(input("Check this number: "))
prime_checker(number=n)
