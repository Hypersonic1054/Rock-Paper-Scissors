def main():
    user_choice = get_user_choice() 
    computer_choice = get_computer_choice()
    print("Computer chose " + computer_choice + ".")  
    result = determine_winner(user_choice, computer_choice)
    print(result)

main()
