def choice_checker(question, empty_valid, multi_choice, error=None, valid_answer=None):
    # Loop to keep the question going till answered properly

    if multi_choice == "yes" and empty_valid == "no":

        while True:

            response = input(question).lower()

            for word in valid_answer:
                if response == word[:1] or response == word:
                    return word

            print(error)
            print()

    elif multi_choice == "no" and empty_valid == "no":

        while True:

            response = input(question)

            if response == "":
                print("|>=+--- Your response to this cannot be blank ---+=<|")
                print("")

            else:
                return response

    elif multi_choice == "no" and empty_valid == "yes":

        while True:
            response = input(question)
            return response


def multi_choice(question, error, valid_answer):

    # Loop to keep the question going till answered properly
    while True:

        response = input(question).lower()

        for word in valid_answer:
            if response == word[:1] or response == word:
                return word

        print(error)
        print()

