import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rules = [#R2 P2 S2
         [0, 2, 1], #R1
         [1, 0, 2], #P1
         [2, 1, 0], #S1
        ]

visual = [rock, paper, scissors] 

round_result = ["draw", "You Win", "Computer Wins"]

player_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 Scissors: "))

print(visual[player_choice])

computer_choice = random.randint(0, 2)

print("Computer Chose: \n")
print(visual[computer_choice])

result = rules[player_choice][computer_choice]

print(round_result[result])
