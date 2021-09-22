import random
from art import logo, vs
from game_data import data
from replit import clear


def person_intro(person):
  return f"{person['name']} a {person['description']} from {person['country']}"

def person_vs_display(person_a, person_b):
  person_a_intro = person_intro(person_a)

  person_b_intro = person_intro(person_b)

  print(f"Compare A: {person_a_intro}")
  print(vs)
  print(f"Against B: {person_b_intro}")

def loss_display(other_person, answer_person):
  print(f"you lose {other_person['name']} has {other_person['follower_count']} m followers while {answer_person['name']} has only {answer_person['follower_count']} m followers") 

def game(person_a, person_b, score, pool):

  if len(pool) == 1:
    print("you won you guessed all right")
    return
  
  clear()
  print(logo)
  print(f"your score is: {score}")  

  if person_a == None:
    random.shuffle(pool)
    person_a = pool.pop()
  random.shuffle(pool)
  person_b = pool.pop()

  match_persons = {
    'a': person_a,
    'b': person_b
  }

  person_vs_display(match_persons['a'], match_persons['b'])
  
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  answer_person = match_persons[answer]
  del match_persons[answer]
  other_person = match_persons[next(iter(match_persons))]

  if answer_person["follower_count"] > other_person["follower_count"]:
    clear()
    score += 1
    game(person_a = answer_person, person_b = None, score = score, pool = pool)
  else:
     loss_display(other_person, answer_person)

game(person_a = None,person_b = None, score = 0, pool = data)  
