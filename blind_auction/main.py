from replit import clear
from art import logo


bider_dictionary = {}

def get_max_bider(bider_dictionary):
  max_bider = "", 0
  for name,price in bider_dictionary.items():
    if price >= max_bider[1]:
      max_bider = name, price

  print(f"the winner is: {max_bider[0]}")
    

def main():
  name = input("what is your name ? : \n")
  price = float(input("what price do you bid ? : \n"))

  bider_dictionary[name] = price

  other_bider = input("is there another person who wants to bid ? : \n")

  clear()


  if other_bider in "yes":
    main()
  else:
    get_max_bider(bider_dictionary)  

print(logo)
main()
