
# allows the user to answer from a given choice of options,
# if the response is not one of them, sends an error and tries again
def multi_choice_checker(question, valid_answer, error):
    # Loop to keep the question going till answered properly
    while True:

        response = input(question).lower()

        # checks if the user response is one of the valid answers
        for word in valid_answer:

            # if the response shares the same first letter or is the same word, the program returns the answer
            if response == word[:1] or response == word:
                return word

        print(error)
        print()

