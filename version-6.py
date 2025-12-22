import random as rd
import os


def get_user_choice():
  while True:
    user_choice = input("Rock, paper, or scissors: ").strip().lower()

    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
      return user_choice
    else:
      print("Invalid input. Please enter rock, paper, or scissors.")

def get_computer_choice():
  computer_choice = rd.choice(['rock', 'paper', 'scissors'])
  return computer_choice
  
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It's a tie!"

  elif user_choice == "rock":
    if computer_choice == "scissors":
      return "You win!"
    else:
      return "Computer wins!"

  elif user_choice == "paper":
    if computer_choice == "rock":
      return "You win!"
    else:
      return "Computer wins!"

  elif user_choice == "scissors":
    if computer_choice == "paper":
      return "You win!"
    else:
      return "Computer wins!"

def main():
    while True:
      user_choice = get_user_choice() 
      computer_choice = get_computer_choice()
     
      print("Computer chose " + computer_choice + ".")  
      result = determine_winner(user_choice, computer_choice)
      print(result)
      again = input("Play again? (y/n): ").lower()
      if again != "y":
        break
main()

  
