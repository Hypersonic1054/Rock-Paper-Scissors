import random as rd


def get_computer_choice():
  computer_choice = rd.choice(['rock', 'paper', 'scissors'])
  return computer_choice
  
choice = get_computer_choice()
print(choice)
