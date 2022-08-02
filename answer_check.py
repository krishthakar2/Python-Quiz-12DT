def check_answer(answer,
                 answer_tried):  # checks the answer entered by the user with the correct answer and gives the points and prints the statement
    global score

    if answer == answer_tried:  # checks the answer written by user but the real answer
        print("That's correct! Good job")  # prints this statement if the answer is correct
        score = score + 1  # when the answer is correct user gets one point
        print("Your score is:", score)
        return 1  # gives player one point per correct question
    else:
        print("Incorrect! Better luck next question")
        print("Your score is:", score)
        return 0  # gives player no points of answer is wrong
