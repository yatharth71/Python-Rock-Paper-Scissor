import random

def Win(computer, you):
    if computer==you:
        return None
    if computer=='s':
        if you == 'r':
            return True
        if you == 'p':
            return False
    if computer=='r':
        if you == 'p':
            return True
        if you == 's':
            return False
    if computer=='p':
        if you == 's':
            return True
        if you == 'r':
            return False
random_num = random.randint(1,3)
if random_num == 1:
    computer = 's'
if random_num == 2:
    computer = 'p'
if random_num == 3:
    computer = 'r'

print("Enter s for Scissors, p for Paper and r for Rock")
you = input("Your Turn : ")

answer = Win(computer, you)

if answer == None:
    print("Tie")
elif answer:
    print("You win")
else:
    print("You Lose")