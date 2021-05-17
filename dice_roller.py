import random

dice_roll = int(input('How many dice would you like to roll? '))
dice_size = int(input('How many sides on a dice? '))
dice_sum = 0

for i in range(0, dice_roll):
    roll = random.randint(1, dice_size)
    dice_sum += roll
    if roll == 1:
        print(f'You rolled a {roll}! Critical fail')
    elif roll == dice_size:
        print(f'You rolled a {roll}! Critical succes')
    else:
        print(f'You rolled a {roll}!')
print(f'You rolled a total of {dice_sum}')

"""def main():
  print(f'You rolled a {roll}')

if __name__== "__main__":
  main()"""
