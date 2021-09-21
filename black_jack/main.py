
import random
from art import logo

print(logo)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

players = ["you", "dealer"]

result_matrix = [#   !dg21    dg21

                  ['closer wins', 'you win'], #!yg21
                  ['dealer wins', 'draw'],  #yg21

                ]

your_hand = [0,0,0]

dealers_hand = [0,0,0]

your_score = 0
dealers_score = 0


def display_hand(hand, player):

  hand_display = ['','','']
  for index, card in enumerate(hand):
    if hand[index] == 0:
      hand_display[index] = "_"
    else:
      if player == "dealer":
        if index > 0:
          hand_display[index] = "?"
        else:
          hand_display[index] = str(card)  
      else:
        hand_display[index] = str(card)

  return hand_display      
   
def calculate_score(hand):
  result = 0
  for card in hand:
    result += card
  return result

def dealer_gets_a_card(dealers_hand, turn_number):
  new_card = random.choice(cards)

  dealers_new_hand = dealers_hand

  dealers_new_hand[turn_number - 1] = new_card
    
  while calculate_score(dealers_new_hand) > 21 and 11 in dealers_new_hand:
    index = dealers_new_hand.index(11)
    dealers_new_hand[index] = 1


  return dealers_new_hand, calculate_score(dealers_new_hand)


def you_get_a_card(your_hand, turn_number):
  new_card = random.choice(cards)

  your_new_hand = your_hand

  if input("do want to get a card? y/n:") in "yes":
    your_new_hand[turn_number - 1] = new_card

    while calculate_score(your_new_hand) > 21 and 11 in your_new_hand:
      index = your_new_hand.index(11)
      your_new_hand[index] = 1

    return your_new_hand, calculate_score(your_new_hand)
  else:    
    your_new_hand[turn_number - 1] = 0
    return your_new_hand, calculate_score(your_new_hand)
  

def display_turn_hands(dealers_hand, your_hand, turn):
  print(f"turn number {turn}:")
  print("\tdealer: ")
  print(f"\t\t{display_hand(dealers_hand, players[1])}")
  print("\tyou: ")
  print(f"\t\t{display_hand(your_hand, players[0])}")  

display_turn_hands(dealers_hand, your_hand, 0)

def print_scores(dealers_score, your_score):
  print(f"dealers score is: {dealers_score}")
  print(f"your score is: {your_score}")

def get_result(dealers_score, your_score):
  you_above_21 = your_score > 21

  dealer_above_21 = dealers_score > 21

  result = result_matrix[you_above_21][dealer_above_21]

  if result == "closer wins":
    difference = your_score - dealers_score
    if difference > 0:
      return "you win"
    elif difference < 0:
      return "dealer wins"
    else:
      return "draw"      

  return result

def main(init_dealers_hand, init_dealers_score, init_your_hand, init_your_score):

  dealers_hand, dealers_score = init_dealers_hand , init_dealers_score

  your_hand, your_score = init_your_hand, init_your_score

  for i in range(3):
    
    dealers_hand, dealers_score = dealer_gets_a_card(dealers_hand, i+1)

    your_hand, your_score = you_get_a_card(your_hand, i+1)

    display_turn_hands(dealers_hand, your_hand,i+1)

  print_scores(dealers_score, your_score)
  print(get_result(dealers_score, your_score))

main(dealers_hand, dealers_score, your_hand, your_score)
