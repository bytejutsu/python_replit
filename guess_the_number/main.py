import random
from art import logo 

difficulties = ["easy", "hard"]

def set_number_of_attempts(difficultie):
  if difficultie == "easy":
    return 10
  else:
    return 5

def check_entered_number(my_number, goal_number):
  if my_number < goal_number:
    print("too low")
    return False
  elif my_number > goal_number:
    print("too high")
    return False
  else:
    print("you guessed the right number")
    return True    

def main(goal_number, difficulty):
  attempts = set_number_of_attempts(difficulty)

  while not check_entered_number(int(input("enter a number: ")), goal_number) and attempts > 0:
    attempts -= 1
    if(attempts == 0):
      print(f"you didn't guess the right number it is {goal_number}")
      break
    print(f"you have {attempts} attempts left")

print(logo)    
difficulty = input("type easy for easy difficulty and hard for hard difficulty: ")  
goal_number = random.choice(range(100))  

main(goal_number, difficulty)    

