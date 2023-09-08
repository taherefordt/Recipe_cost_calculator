
# function used for checking ingredient quantities, costs, and total no. of servings
def num_check(question, flint, low=None, exit_code=None):
    while True:

        # if the number doesn't need a low, a different error is generated compared to when there is one
        if low is not None:
            error = f"|>=+--- Please enter a number that is more than or equal to {low} ---+=<|"

        else:
            error = "|>=+--- Please enter a number ---+=<|"

        # continues to attempt code below until a valid answer is given
        try:
            response = input(question)

            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer or float depending on flint
            if flint == "int":
                response_conv = int(response)

            else:
                response_conv = float(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response_conv < low:
                print(error)
                continue

            return response

        # checks input is a number, if not sends an error
        except ValueError:
            print(error)

            continue
