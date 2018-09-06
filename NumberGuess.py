"""The program does the following:

Roll a pair of dice.
Add the values of the roll.
Ask the user to guess a number.
Compare the user's guess to the total value.
Determine the winner (user or computer)."""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input('Guess a whole number: '))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print('Maximum possible value is %d' % (max_val))
  guess = get_user_guess()
  if guess>max_val:
    print('Invalid guess, %d is greater than maximum guess %d.' % (guess,max_val))
  else:
    print('Rolling...')
    sleep(2)
    print('First roll: %d' % (first_roll))
    sleep(1)
    print('Second roll: %d' % (second_roll))
    sleep(1)
    total_roll = first_roll + second_roll
    print('Total roll: %d' % (total_roll))
    print('Result...')
    sleep(1)
    if guess == total_roll:
      print('Congrats you have won!')
    else:
      print('You have lost. Better luck next time!')
    
roll_dice(6)
