from replit import clear
from art import logo


bidder_dictionary = {}

def get_max_bider(bidder_dictionary):
  max_bidder = "", 0
  for name,price in bidder_dictionary.items():
    if price >= max_bidder[1]:
      max_bidder = name, price

  print(f"the winner is: {max_bidder[0]}")
    

def main():
  name = input("what is your name ? : \n")
  price = float(input("what price do you bid ? : \n"))

  bidder_dictionary[name] = price

  other_bidder = input("is there another person who wants to bid ? : \n")

  clear()


  if other_bider in "yes":
    main()
  else:
    get_max_bidder(bidder_dictionary)  

print(logo)
main()
