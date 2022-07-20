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

hands = [rock, paper, scissors]

ans = int(input("What you gonna choose ? Type 0 for rock, 1 for paper or 2 for scissor:"))

num = random.randint(0, 2)

answer = hands[ans]
print(f'You choose  : {answer}')

print(f'Computer choose : {hands[num]}')

if num == 2 and ans == 0:
    print("You Wins")
elif num == 0 and ans == 2:
    print("You Lose")
elif ans > num:
    print("You Win")
elif ans == num:
    print("It is a draw")
else:
    print("You Lose")
