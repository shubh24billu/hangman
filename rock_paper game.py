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

#Write your code below this line 👇
import random
images=[rock,paper,scissors]
your_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(images[your_choice])
computer_choice=random.randint(0,2)
print("computer chose")
print(images[computer_choice])

if your_choice>=3 and your_choice<0:
  print("you chose wrong no.")
elif your_choice==0 and computer_choice==2:
  print("you win")
elif your_choice==2 and computer_choice==0:
  print("you loose")
elif your_choice==computer_choice:
  print("it's a tie try again")
elif your_choice<computer_choice:
  print("you loose")
elif your_choice>computer_choice:
  print("you won")

