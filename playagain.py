def play_again():  # allows the user to play the game again
    """
    Asks the user if they want to play again.
    :return:
    """
    while True:
        quiz_again = str(input(
            "Would you like to play again? (yes/no)\n").lower().strip())  # asks the user if they would like to play again
        if quiz_again == "no":  # is user says no it prints thanks for playing
            print("")
            return False  # if the return value is false/no it will block the run
        elif quiz_again == "yes":  # is the user the  prints yes it replays the quiz
            print("")
            return True  # if the return value is true/yes it will continue the run
        else:
            print(
                "I'm sorry, I didn't understand that. Please try again.")  # is the user writes anything but a yes or no the quiz prints this and asks the user to re enter a answer (yes/no)

