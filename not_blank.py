def not_blank(question):

    # loop to repeat until a valid answer is received
    while True:

        response = input(question)

        # if the response is blank, print an error
        if response == "":
            print("|>=+--- Your response to this cannot be blank ---+=<|")
            print("")

        # if the response is not blank return response
        else:
            return response
