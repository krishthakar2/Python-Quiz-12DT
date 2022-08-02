from main import questions, answers, check_answer


def new_game():  # whenever this function is called a new quiz game will be created
    answer_tried = []
    correct_guesses = 0
    number_questions = 1  # represents the first questions

    for key in questions:  # loops the questions
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  # seperates the questions with a line
        print(key)  # prints the questions
        for i in answers[number_questions - 1]:  # for loop prints and lists the questions,-1 so receive 0 as index
            print(i)
        answer = input(" Please Enter (A,  B, C, or D): ")  # lets the user what to enter
        if answer == "":  # if the user enters nothing and just enters the code prints Please Enter A,  B, C, or D next time
            print("Please Enter A,  B, C, or D next time")
        print("")  # prints blank like to make it look nicer
        answer = answer.upper()  # if the user rights the letter in lowercase this line makes the letter into uppercase
        answer_tried.append(answer)

        correct_guesses += check_answer(questions.get(key),
                                        answer)  # receive the answer of the questions as well as the answer written by the user
        number_questions += 1
