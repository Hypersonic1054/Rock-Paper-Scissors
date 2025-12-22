import random as rd
import os

games_played = 0
games_won = 0

def get_user_choice():
  while True:
    user_choice = input("rock, paper, or scissors: ").strip().lower()
    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
      return user_choice
    else:
      print("Invalid input. Please enter rock, paper, or scissors.")

def get_computer_choice():
  return rd.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "tie"
  elif user_choice == "rock":
    if computer_choice == "scissors":
      return "win"
    else:
      return "lose"
  elif user_choice == "paper":
    if computer_choice == "rock":
      return "win"
    else:
      return "lose"
  elif user_choice == "scissors":
    if computer_choice == "paper":
      return "win"
    else:
      return "lose"

def main():
  games_played = 0
  games_won = 0

  while True:
    os.system("clear")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print("Computer chose " + computer_choice + ".")

    result = determine_winner(user_choice, computer_choice)

    games_played += 1
    if result == "win":
      print("You win!")
      games_won += 1
    elif result == "lose":
      print("Computer wins!")
    else:
      print("It's a tie!")

    print("SCOREBOARD")
    print("----------")
    print("Games Won: %s" % (games_won))
    print("Games Played: %s" % (games_played))

    again = input("Play again? (y/n): ").lower()
    if again != "y":
      break

main()
