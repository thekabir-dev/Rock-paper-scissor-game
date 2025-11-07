import random

rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
user_choice=int(input("Choose your play!! \nType 0 for rock\nType 1 for paper\nType 2 for scissors\nYour choice="))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])
else:
    print("The number given is Invalid")
computer_choice=random.randint(0,2)
print(f"computer choose: {computer_choice}")
print((game_images[computer_choice]))
if user_choice == computer_choice:
        print("It's a draw!!")
elif (user_choice == 0 and computer_choice == 2) or \
                (user_choice == 1 and computer_choice == 0) or \
                (user_choice == 2 and computer_choice == 1):
            print("You win!!")
else:
    print("You lose!!")



